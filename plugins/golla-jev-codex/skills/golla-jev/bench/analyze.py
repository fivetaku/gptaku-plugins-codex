"""R3 채점·집계. results/raw.jsonl → results/summary.json + 표준출력 요약."""
import json, pathlib, statistics
from collections import defaultdict

ROOT = pathlib.Path(__file__).parent
ITEMS = {it['id']: it for it in json.loads((ROOT / 'items.json').read_text())['items']}
ROWS = [json.loads(l) for l in (ROOT / 'results' / 'raw.jsonl').read_text().splitlines() if l.strip()]


def judge(it, ans, cond):
    """→ (맞음, 확실도, 예측). 확실도: Choice 고른 보기 확률, Score confidence, Noul max(p, 1-p)."""
    if not ans:
        return None
    if it['type'] == 'choice':
        lang = 'en' if cond == 'en' else 'ko'
        name2key = {o[lang]: o['key'] for o in it['options']}
        pred = name2key.get(ans.get('choice'))
        return pred == it['gold'], (ans.get('probabilities') or {}).get(ans.get('choice'), 0.0), pred
    if it['type'] == 'score':
        pred = int(round(ans['score']))
        return pred == it['gold'], ans.get('confidence', 0.0), pred
    p = ans['noul']
    return (p >= 0.5) == it['gold'], max(p, 1 - p), p >= 0.5


graded = []  # (cond, rep, id, ok, cert, pred)
lat = defaultdict(list)
fails = 0
for r in ROWS:
    if not r.get('ok'):
        fails += 1
        continue
    lat[r['cond']].append(r['ms'])
    for iid, ans in r['answers'].items():
        g = judge(ITEMS[iid], ans, r['cond'])
        if g:
            graded.append((r['cond'], r['rep'], iid, *g))


def acc(rows):
    return (sum(x[3] for x in rows), len(rows))


def pct(a):
    return f'{a[0]}/{a[1]} ({100 * a[0] / a[1]:.1f}%)' if a[1] else '-'


summary = {'calls': len(ROWS), 'failed_calls': fails}
conds = ['ko', 'en', 'ko_rev', 'packed']
wfs = sorted({it['wf'] for it in ITEMS.values()}, key=lambda w: list(ITEMS.values())[[i['wf'] for i in ITEMS.values()].index(w)]['id'])

print('== 정확도 (워크플로 × 조건, 반복 합산)')
table = {}
for wf in wfs:
    row = {}
    for c in conds:
        sel = [g for g in graded if g[0] == c and ITEMS[g[2]]['wf'] == wf]
        if sel:
            row[c] = acc(sel)
    table[wf] = row
    print(f'{wf:14s}', ' | '.join(f'{c}: {pct(row[c])}' for c in conds if c in row))
for c in conds:
    sel = [g for g in graded if g[0] == c]
    print(f'{"전체 " + c:14s}', pct(acc(sel)))
summary['accuracy'] = {wf: {c: list(v) for c, v in row.items()} for wf, row in table.items()}
summary['accuracy_total'] = {c: list(acc([g for g in graded if g[0] == c])) for c in conds}

print('\n== 질문 타입별 (ko)')
for t in ('choice', 'score', 'noul'):
    print(t, pct(acc([g for g in graded if g[0] == 'ko' and ITEMS[g[2]]['type'] == t])))

print('\n== 지연 (HTTP 왕복 ms, 요청 단위)')
summary['latency'] = {}
for c in conds:
    xs = sorted(lat[c])
    if xs:
        p50, p90 = statistics.median(xs), xs[int(len(xs) * 0.9) - 1]
        summary['latency'][c] = {'n': len(xs), 'p50': round(p50), 'p90': round(p90)}
        print(c, summary['latency'][c])

# 반복성: ko rep0 대 rep1 예측 일치
pred = defaultdict(dict)
for c, rep, iid, ok, cert, p in graded:
    pred[(c, iid)][rep] = (p, ok, cert)
same = [v[0][0] == v[1][0] for (c, _), v in pred.items() if c == 'ko' and 0 in v and 1 in v]
summary['repeat_ko'] = [sum(same), len(same)]
print('\n== 반복성 ko rep0=rep1', pct((sum(same), len(same))))

# 보기 순서: ko 대 ko_rev 예측이 갈린 문항
flips = [iid for (c, iid), v in pred.items() if c == 'ko' and ('ko_rev', iid) in pred
         and any(v.get(r, (None,))[0] != pred[('ko_rev', iid)].get(r, (None,))[0] for r in v)]
summary['order_flips'] = flips
print('== 보기 순서 뒤집기로 예측이 바뀐 문항', len(flips), flips)

# 문턱 절차: ko rep0, dev 에서 문턱을 고르고 holdout 에 적용
TARGET = 0.97
dev = [g for g in graded if g[0] == 'ko' and g[1] == 0 and ITEMS[g[2]]['split'] == 'dev']
hold = [g for g in graded if g[0] == 'ko' and g[1] == 0 and ITEMS[g[2]]['split'] == 'holdout']
cands = [round(x / 100, 2) for x in range(50, 100)]
best = None
for t in cands:
    cov = [g for g in dev if g[4] >= t]
    if cov and sum(g[3] for g in cov) / len(cov) >= TARGET:
        best = t
        break
summary['threshold'] = {'target_precision': TARGET, 'chosen_on_dev': best}
print(f'\n== 문턱 절차 (목표 정밀도 {TARGET:.0%}) dev 에서 고른 문턱:', best)
for name, rows in (('dev', dev), ('holdout', hold)):
    t = best if best is not None else 1.01
    cov = [g for g in rows if g[4] >= t]
    rest = [g for g in rows if g[4] < t]
    info = {'n': len(rows), 'auto': len(cov), 'auto_correct': sum(g[3] for g in cov),
            'to_human': len(rest), 'to_human_were_wrong': sum(not g[3] for g in rest)}
    summary['threshold'][name] = info
    print(name, info)

# 순서 일치 규칙을 더한 Choice 전용
rule2 = []
for g in hold:
    it = ITEMS[g[2]]
    if it['type'] != 'choice':
        continue
    rev = pred.get(('ko_rev', g[2]), {}).get(0)
    agree = rev is not None and rev[0] == g[5]
    rule2.append((g, (best is not None and g[4] >= best) and agree))
summary['threshold']['holdout_choice_with_order_check'] = {
    'n': len(rule2), 'auto': sum(a for _, a in rule2), 'auto_correct': sum(a and g[3] for g, a in rule2),
    'to_human_were_wrong': sum((not a) and (not g[3]) for g, a in rule2)}
print('holdout Choice + 순서 일치 규칙', summary['threshold']['holdout_choice_with_order_check'])

# 확실도 구간별 정확도 (ko, 반복 합산)
bins = [(0, 0.6), (0.6, 0.8), (0.8, 0.95), (0.95, 1.01)]
summary['calibration_ko'] = {}
print('\n== 확실도 구간별 정확도 (ko)')
for lo, hi in bins:
    sel = [g for g in graded if g[0] == 'ko' and lo <= g[4] < hi]
    summary['calibration_ko'][f'{lo}-{hi}'] = list(acc(sel))
    print(f'{lo:.2f}~{hi:.2f}', pct(acc(sel)))

# 틀린 문항 목록
wrong = defaultdict(list)
for c, rep, iid, ok, cert, p in graded:
    if not ok:
        wrong[iid].append(f'{c}#{rep}:{p}({cert:.2f})')
summary['wrong'] = {k: v for k, v in sorted(wrong.items())}
print('\n== 틀린 문항 (정답 → 조건#반복:예측(확실도))')
for k, v in sorted(wrong.items()):
    print(k, ITEMS[k]['wf'], 'gold=', ITEMS[k]['gold'], ' '.join(v))

(ROOT / 'results' / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1))
