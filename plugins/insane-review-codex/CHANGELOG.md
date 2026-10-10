# Changelog — insane-review-codex

본진판 `insane-review`의 기능 업데이트를 Codex 포트로 반영한 이력.
CLI 엔진(`bin/pack_and_ask.py`)은 본진 v0.6.8을 유지한다. Desktop 경로는 별도 로컬 기록 도구와 IAB 실행 지침으로 확장한다.

## 0.7.0 — 2026-10-11

- Codex Desktop에서 현재 내장 Browser/IAB 도구가 제공되면 CDP 온보딩보다 먼저 선택한다.
- `bin/iab_review.py`가 기존 패킹 엔진을 재사용해 준비 파일과 manifest를 만들고 sending/sent/complete를 원자적으로 기록한다.
- 실제 모델명/Pro, 첨부, 대화 URL, 신규 assistant 턴과 완료 상태를 현재 브라우저 UI에서 확인하는 절차를 추가한다.
- 중단 뒤 같은 IAB 대화에서 회수하며 별도 브라우저 기동이나 질문 재전송으로 폴백하지 않는다.
- 내장 도구가 없는 CLI와 agent-council의 CDP 엔진은 변경하지 않는다.

## 0.6.8 — 2026-09-08

본진 v0.5.3 → v0.6.8 엔진을 한 번에 동기화(`bin/pack_and_ask.py` 1:1, 2650행). 엔진 위치를 본진과 같은
플러그인 루트 `bin/`으로 옮기고(`scripts/` 제거) SKILL.md를 본진 스킬+커맨드 통합본으로 다시 썼다.
온보딩 분기는 전부 `shared/questioning-policy.md §A` 번호 선택지로 렌더한다. 가져온 기능:

- **저장 브라우저 자동 기동 `--ensure-env` (v0.5.3)**: 최초 1회 브라우저를 고르면 config에 저장되고 이후 CDP가 닫혀
  있어도 조용히 자동 기동(저장값-only·첫감지 폴백 없음·`wrong`이면 안 함). `--check-env`는 순수 점검으로 분리(CQS),
  `STATUS`에 `saved_browser=` 추가.
- **Pro 티어 검증만으로 플래그십 자동 추종 (v0.5.4~0.5.5)**: `--require-model` 하드코딩 핀 제거(옵트인 유지).
  로그인 3단계 판정(`ok/no/unknown`) + 세션 쿠키 진단(`cookie=`·`cookie_exp=`)으로 거짓 음성 재로그인 요구 제거.
  브라우저별 프로필 분리(앱별 쿠키 암호화 키 차이로 세션이 깨지던 문제).
- **스테일 CDP 자가복구 (v0.5.6)**: 실행 중 디스크 자동 업데이트로 `Browser context management is not supported`가
  나면 전용 프로필 프로세스만 재기동(로그인 보존) 후 1회 재연결.
- **모델 서브메뉴 하드닝 (v0.5.7)**: 서브메뉴의 모델 radio가 추론단계 판정을 덮어쓰던 오염 수정. 문서의 "GPT-5.5 Pro"를
  제네릭 "GPT Pro"로, council-setup `--require-model` 예시를 "GPT-5.6"(fail-closed 함정 경고 포함)으로 현행화.
- **타임아웃 최후수단 '지금 답변 받기' 자동 클릭 (v0.5.8)**: 최대 대기 소진 시 리즈닝 중이면 자동 클릭 후
  `INSANE_REVIEW_FORCE_GRACE`(240s) 유예 회수. cot v5 고정행 셀렉터 + force 클릭 폴백.
- **identity 결속 (v0.6.0)**: 대화 URL(`/c/<id>`) 고정·이탈 자동복귀, `page.url` 스테일 버그 수정(`location.href` 평가),
  message-id 차집합 판정, 재시도=회수 재시도(재전송 금지), run manifest 원자 기록, **`--harvest <채팅URL|manifest>`**,
  Pro 최대 대기 자동 3600s, 클립보드 오염 가드, "이번 첨부만 근거로" 가드 라인.
- **쿼터 감지 + 셀렉터 폴백 (v0.6.1)**: 사용량 한도를 dialog/alert 표면에서 감지해 `quota`로 조기 종료(`--harvest` 안내).
- **슬라이더 추론단계 UI 대응 (v0.6.2)**: radio → 슬라이더 개편에 맞춰 SliderControl focus + 화살표 키로 선택, 생성 중 Escape 오발 가드.
- **죽은 프로젝트 캐시 판정 (v0.6.3)**: 워크스페이스 이동으로 죽은 프로젝트 URL을 살아있다고 오판하던 결함 수정 —
  `g-p-<id>` 유지 + 에러 텍스트 부재 + 컴포저 존재 3중 판정, 사망 캐시 즉시 폐기.
- **회수 상태머신 재설계 (v0.6.5)**: 클라이언트 스트림 유실 스톨 복구(`INSANE_REVIEW_STALL_RELOAD` 45s, 결속 URL 재로드
  최대 3회), 턴완료 판정을 message-id 신규 노드 + 그 턴 컨테이너(`section[data-turn]`)의 copy 버튼으로 교체, 클립보드
  80자 미만 전체 대조, manifest 결속 즉시 기록, 프로젝트 생존 4상태(`ok/dead/auth/unknown`), projects.json 디렉터리 lock.
- **워크스페이스 결속 + 사이드바 API 탐색 (v0.6.6)**: 캐시 레코드 `{url, workspace_id}`(`_account` 쿠키; 구형 자동 승격),
  불일치면 goto 없이 즉시 dead. 프로젝트 탐색은 `/backend-api/gizmos/snorlax/sidebar` 표시이름 정확 일치 1순위, DOM 폴백.
- **launch_mode (v0.6.7)**: 전용 브라우저 실행 방식 `background`(기본·창 숨김·포커스 유지)/`foreground`/`headless`(권장 안 함 —
  ChatGPT가 컴포저를 안 내줌). `--set-launch-mode`, config 영속 + env `INSANE_REVIEW_LAUNCH_MODE` 우선, `STATUS`에 `launch_mode=`.
  SKILL 온보딩에 최초 1회 선택지 추가.
- **Chat/Work 토글 게이트 (v0.6.8)**: Work 모드엔 Pro 추론단계가 없고 선택이 sticky라 자동 실행이 조용히 비-Pro로
  나가던 문제 — 모델 스위처를 열기 전에 `ensure_chat_mode()`로 Chat 보정, 실패 시 `--model pro` 전송 fail-closed,
  `STATUS`에 `mode=` 노출.
- 본진 v0.6.4(첫 실행 셋업의 settings.json 파손 방지)는 setup 훅 전용이라 코덱스판에 해당 코드가 없다(N/A).
- 버전을 본진과 동일하게 0.6.8로 정렬. plugin.json·README 설명의 "GPT-5.5 Pro" → 제네릭 "GPT Pro".

플랫폼 N/A(미포팅, 변동 없음): `setup/setup.sh`·`setup/gptaku-update-check.cjs`(설치·업데이트 알림 훅), GitHub star opt-in,
본진 커맨드 파일(SKILL.md에 병합), 선택지 카드 UI(§A 번호 선택지로 치환).

## 0.5.2 — 2026-06-24

본진 v0.1.0 → v0.5.2 엔진을 한 번에 동기화. Codex 포트 규약상 setup 훅·GitHub star opt-in·
업데이트 알림 훅·선택지 카드 UI 프런트매터는 플랫폼 미지원으로 제외하고, 셋업/온보딩은
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
대체 문서화), `setup/gptaku-update-check.cjs`(업데이트 알림 훅), GitHub star opt-in, 선택지 카드 UI
프런트매터. Codex에는 hooks/agents 로스터/선택지 카드 UI가 없다.

## 0.1.0

- 초기 Codex 스텁: repomix 패킹 → 구독 ChatGPT Pro(CDP) → 리뷰 회수의 v2 엔진. 단독 리뷰어 + agent-council 웹 멤버.
