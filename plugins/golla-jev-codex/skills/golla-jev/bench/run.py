"""Jev 벤치 실행. 조건 4종을 Jev 에 보내고 호출 1회당 1행을 results/raw.jsonl 에 쌓는다.

  ko      질문·보기 한국어
  en      질문·보기 영어 (state 는 한국어 그대로)
  ko_rev  ko 와 같고 Choice 보기 순서만 거꾸로
  packed  Choice 문항을 6개씩 한 요청에 묶음(state.items 배열 + 문항별 질문, 경로를 items[i] 로 지정)
"""
import json, os, pathlib, ssl, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

try:  # 일부 python.org 파이썬은 CA 묶음이 연결돼 있지 않다
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()


def typesafe_key():
    """키는 환경변수 TYPESAFE_API_KEY 에서만 읽는다. 값은 출력하지 않는다."""
    key = os.environ.get('TYPESAFE_API_KEY', '').strip()
    if not key:
        raise SystemExit('TYPESAFE_API_KEY 환경변수가 비어 있습니다')
    return key

ROOT = pathlib.Path(__file__).parent
ITEMS = json.loads((ROOT / 'items.json').read_text())['items']
OUT = ROOT / 'results' / 'raw.jsonl'
REPS = int(os.environ.get('REPS', '2'))
URL = 'https://api.typesafe.ai/v1/systemone'
PACK = 6


def question(it, lang, reverse=False, prefix=None):
    text = it[lang]
    if prefix is not None:  # packed: `receipt` → `items[i].receipt`
        for k in it['state']:
            text = text.replace(f'`{k}', f'`{prefix}.{k}')
    q = {'type': it['type'], 'instructions': text}
    if it['type'] == 'choice':
        opts = list(reversed(it['options'])) if reverse else it['options']
        q['criteria'] = {o[lang]: o[f'{lang}_desc'] for o in opts}
    elif it['type'] == 'score':
        q['criteria'] = it[f'levels_{lang}']
    return q


def post(body, key):
    data = json.dumps(body, ensure_ascii=False).encode()
    for attempt in range(5):
        req = urllib.request.Request(URL, data=data, method='POST',
                                     headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'})
        t0 = time.perf_counter()
        try:
            with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
                resp = json.loads(r.read())
            return {'ok': True, 'ms': (time.perf_counter() - t0) * 1000, 'model': resp.get('model'),
                    'answers': resp['answers'], 'usage': resp.get('usage')}
        except urllib.error.HTTPError as e:
            if e.code in (429, 529) and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            return {'ok': False, 'error': f'HTTP {e.code}', 'detail': e.read().decode()[:300]}
        except Exception as e:  # noqa: BLE001
            if attempt < 2:
                time.sleep(1)
                continue
            return {'ok': False, 'error': type(e).__name__, 'detail': str(e)[:200]}
    return {'ok': False, 'error': 'retries exhausted'}


def jobs():
    out = []
    for rep in range(REPS):
        for it in ITEMS:
            for cond in ('ko', 'en'):
                out.append(('single', cond, rep, [it]))
            if it['type'] == 'choice':
                out.append(('single', 'ko_rev', rep, [it]))
        by_wf = {}
        for it in ITEMS:
            if it['type'] == 'choice':
                by_wf.setdefault(it['wf'], []).append(it)
        for group in by_wf.values():
            for s in range(0, len(group), PACK):
                out.append(('packed', 'packed', rep, group[s:s + PACK]))
    return out


def run_job(job, key):
    kind, cond, rep, its = job
    if kind == 'single':
        it = its[0]
        lang = 'en' if cond == 'en' else 'ko'
        res = post({'model': 'jev-latest', 'state': it['state'],
                    'questions': {'q': question(it, lang, reverse=(cond == 'ko_rev'))}}, key)
        ans = {it['id']: res.pop('answers', {}).get('q')} if res.get('ok') else {}
    else:
        state = {'items': [it['state'] for it in its]}
        qs = {f'q{i}': question(it, 'ko', prefix=f'items[{i}]') for i, it in enumerate(its)}
        res = post({'model': 'jev-latest', 'state': state, 'questions': qs}, key)
        raw = res.pop('answers', {}) if res.get('ok') else {}
        ans = {it['id']: raw.get(f'q{i}') for i, it in enumerate(its)}
    return {'cond': cond, 'rep': rep, 'ids': [it['id'] for it in its], 'answers': ans, 'ts': time.time(), **res}


def main():
    OUT.parent.mkdir(exist_ok=True)
    key = typesafe_key()
    js = jobs()
    print('jobs', len(js), flush=True)
    with OUT.open('a') as f, ThreadPoolExecutor(max_workers=6) as ex:
        for i, row in enumerate(ex.map(lambda j: run_job(j, key), js), 1):
            f.write(json.dumps(row, ensure_ascii=False) + '\n')
            f.flush()
            if i % 100 == 0 or not row.get('ok'):
                print(i, '/', len(js), row['cond'], row['ids'][0], 'ok' if row.get('ok') else row.get('error'), flush=True)


if __name__ == '__main__':
    main()
