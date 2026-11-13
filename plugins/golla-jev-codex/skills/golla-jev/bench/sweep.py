"""문턱별 자동 처리 비율과 사람에게 넘어가는 오답 수 (ko, rep0). dev 에서 고르고 holdout 으로 확인하는 절차의 표."""
import contextlib, io, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))  # 다른 폴더·격리 모드(-I)에서 실행해도 analyze 를 찾게

with contextlib.redirect_stdout(io.StringIO()):
    import analyze as A  # 채점 결과 graded 를 재사용

for split in ('dev', 'holdout', 'all'):
    rows = [g for g in A.graded if g[0] == 'ko' and g[1] == 0 and (split == 'all' or A.ITEMS[g[2]]['split'] == split)]
    print('==', split, len(rows), '건, 오답', sum(not g[3] for g in rows))
    for t in (0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95):
        auto = [g for g in rows if g[4] >= t]
        hum = [g for g in rows if g[4] < t]
        print(f' 문턱 {t:.2f}: 자동 {len(auto)}/{len(rows)} ({100 * len(auto) / len(rows):.0f}%), 자동 중 오답 {sum(not g[3] for g in auto)}'
              f' | 사람에게 {len(hum)}건, 그중 실제 오답 {sum(not g[3] for g in hum)}')
