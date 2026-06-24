# Changelog — insane-review-codex

본진(Claude Code)판 `insane-review`의 기능 업데이트를 Codex 포트로 반영한 이력.
엔진(`scripts/pack_and_ask.py`)은 본진 `bin/pack_and_ask.py`와 1:1로 동일한 순수 Python이다.

## 0.5.2 — 2026-06-24

본진 v0.1.0 → v0.5.2 엔진을 한 번에 동기화. Codex 포트 규약상 setup 훅·GitHub star opt-in·
업데이트 알림 훅·`AskUserQuestion` 프런트매터는 플랫폼 미지원으로 제외하고, 셋업/온보딩은
SKILL.md의 수동 선행 단계로 문서화했다. 가져온 기능:

- **폴더명 ChatGPT 프로젝트 그룹핑 (v0.3.0)**: 매 실행이 일반 채팅 목록에 쌓이지 않도록 현재 폴더명
  프로젝트 안에 채팅을 정리(캐시→사이드바 탐색→생성, 실패 시 일반 채팅 폴백). `--project`/`--no-project`.
- **그룹핑 하드닝 (v0.3.1)**: 모든 예외를 폴백으로 환원, 표시이름 매칭 + 사이드바 스크롤(가상화/언어무관),
  캐시 키 `{절대경로}::{이름}`.
- **CDP 다이얼로그 레이스 핸들링 (v0.3.2)**: ChatGPT JS 다이얼로그 vs playwright auto-dismiss 레이스로
  인한 드라이버 크래시(100% CPU 스핀)를 자체 핸들러(`_guard_dialogs`)로 차단.
- **크로스플랫폼 온보딩 + 전용 프로필 (v0.4.0)**: mac/win/linux 브라우저 스캔/실행, 항상 별도
  `--user-data-dir`(전용 프로필; Chrome 136+는 이게 없으면 CDP가 안 열림), `--list-browsers`/
  `--launch-browser`, `--browser`가 임의 이름/경로 수용, 입력을 클립보드+⌘V → playwright `insert_text`로 교체.
- **전용 프로필 싱글톤 교착 자가복구 (v0.4.1)**: 스테일 인스턴스가 디버그 포트를 막으면 정리(로그인 보존) 후 1회 재시도.
- **첨부 멱등 셋업 정렬 + 모델/추론 검증 강화 (v0.4.2 / v0.5.0)**: hermetic repomix config(외부 설정의
  압축·본문생략·보안검사 변경 차단), 첨부 실패 시 인라인 폴백(상한 내) + 초과 시 fail-closed, 동명 폴더
  분리(자동 프로젝트명에 경로해시), 폴백 모델명은 메뉴에 모델이 하나일 때만 신뢰(fail-closed).
- 버전을 본진과 동일하게 0.5.2로 정렬.

플랫폼 N/A(미포팅): `setup/setup.sh`(+ pip 의존성 자동설치 훅 — SKILL.md에 수동 `--check-env --install`로
대체 문서화), `setup/gptaku-update-check.cjs`(업데이트 알림 훅), GitHub star opt-in, `AskUserQuestion`
프런트매터. Codex에는 hooks/agents 로스터/`AskUserQuestion`이 없다.

## 0.1.0

- 초기 Codex 스텁: repomix 패킹 → 구독 ChatGPT Pro(CDP) → 리뷰 회수의 v2 엔진. 단독 리뷰어 + agent-council 웹 멤버.
