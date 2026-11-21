# insane-review-codex

GPT Pro(웹 전용 — API 없음; 현 시점 최신 플래그십 모델의 Pro 추론)를 Codex CLI 안으로 끌어오는 브리지 플러그인. (v0.6.9)

repomix로 관련 코드만 정밀 패킹 → 구독 ChatGPT 웹에 CDP 자동화로 투입 → 분석/리뷰 회수.
API 비용 0, 사용자의 ChatGPT 요금제로 동작.

## 사용 조건

- 크로미움 계열 브라우저 1개(Chrome/Brave/Comet/Edge 등) — 스크립트가 **전용(격리) 프로필 + 디버그포트 9222**로 띄운다(기본은 창을 숨긴 background 실행). 그 창에서 chatgpt.com 로그인 1회.
- Python 의존성: `pip install playwright pyperclip` (또는 `--check-env --install`)
- Node.js (npx — repomix 자동설치에 사용)

## 환경 점검 / 온보딩

```bash
# 저장된 브라우저가 있으면 조용히 자동 기동 후 점검 (평소엔 이것만)
python3 bin/pack_and_ask.py --ensure-env
# 순수 점검(부작용 없음) / 부족한 pip 패키지 자동설치
python3 bin/pack_and_ask.py --check-env
python3 bin/pack_and_ask.py --check-env --install
# 최초 1회: 브라우저 선택·실행(선택은 ~/.insane-review/config.json에 저장) + 실행 방식
python3 bin/pack_and_ask.py --list-browsers
python3 bin/pack_and_ask.py --launch-browser "Chrome"
python3 bin/pack_and_ask.py --set-launch-mode background   # background(기본)|foreground|headless(권장 안 함)
```

마지막 줄 `STATUS node=… deps=… browser=… login=… cookie=… saved_browser=… launch_mode=… mode=…`로 막힌 단계를 판단한다. 스킬(`skills/insane-review/SKILL.md`)이 이 분기를 번호 선택지로 안내한다.

## 기본 사용법

```bash
# 디렉토리를 통째로 패킹해 GPT Pro 리뷰 요청 (Pro 추론단계 자동 선택·검증, 플래그십 자동 추종)
python3 bin/pack_and_ask.py \
  --target ./src \
  --model pro \
  --prompt "이 모듈의 설계 리뷰를 해줘. 판정마다 파일:라인 인용 필수."

# 순수 질문만 (코드 없이)
python3 bin/pack_and_ask.py \
  --model pro --force-answer-after 90 \
  --prompt "비동기 큐 설계에서 backpressure를 어떻게 다루면 좋을까?"

# 타임아웃·중단 뒤 회수만 (재전송 없이)
python3 bin/pack_and_ask.py --harvest '<채팅URL 또는 .insane-review/manifest_*.json>'
```

응답은 **현재 프로젝트의 `.insane-review/response_*.md`**에 저장된다. 전송 직후 대화 URL이 `.insane-review/manifest_*.json`에 기록되어 프로세스가 죽어도 `--harvest`로 회수할 수 있다.

## agent-council 웹 멤버로 등록

`skills/insane-review/references/council-setup.md` 참고.

```bash
# council 계약 검증 (stdout=응답만, stderr=로그)
python3 bin/pack_and_ask.py --council --model pro \
  --force-answer-after 60 "한 문장으로: 1+1은?" 2>/dev/null
```

## 주요 플래그

| 플래그 | 설명 |
|--------|------|
| `--target <dir>` | 패킹 대상 디렉토리 (생략 시 프롬프트-only) |
| `--include <glob>` | repomix 포함 글롭 (정밀 선별) |
| `--model pro` | 추론단계 Pro 선택·검증 (플래그십 자동 추종) |
| `--require-model "<이름>"` | 모델명 고정 핀 (부분 일치; 불일치 시 fail-closed — 플래그십 교체 시 갱신 필수) |
| `--force-answer-after N` | N초 후 리즈닝 강제 종료 (빠른 의견용; 정밀 리뷰엔 쓰지 말 것) |
| `--max-wait N` | 응답 최대 대기 초 (기본 20분, Pro 검증 시 자동 60분) |
| `--harvest <URL\|manifest>` | 전송 없이 기존 대화에서 완료된 응답만 회수 |
| `--pack-only` | 패킹만 하고 전송하지 않음 |
| `--council` | agent-council 멤버 모드 — 응답만 stdout |
| `--retries N` | 전송/회수 재시도 횟수 (대화 URL 확보 후엔 회수만 재시도) |
| `--delete-pack` | 응답 회수 후 패킹 파일 삭제 (시크릿 위생) |
| `--browser <이름\|경로>` | 자동화 브라우저 (생략: config 저장값 → 첫 감지) |
| `--launch-browser <이름>` | 전용 프로필+디버그포트로 실행하고 선택 저장 |
| `--set-launch-mode <모드>` | `background`(기본)/`foreground`/`headless` 저장 |
| `--project "<이름>"` / `--no-project` | ChatGPT 프로젝트 그룹핑 이름 지정 / 끄기 |
| `--check-env` / `--ensure-env` | 순수 점검 / 저장 브라우저 자동기동 + 점검 |
| `--install` | `--check-env`와 함께 — pip 의존성 자동설치 |

## 파일 구조

```
insane-review-codex/
  .codex-plugin/plugin.json       — 플러그인 메타데이터
  skills/insane-review/
    SKILL.md                      — 스킬 실행 지시서 (온보딩 분기 + 리뷰 절차)
    references/council-setup.md  — agent-council 등록 가이드
  bin/
    pack_and_ask.py               — repomix 패킹 + ChatGPT CDP 브리지
  shared/questioning-policy.md    — 번호형 선택지 질문 규약
  assets/                         — 아이콘 등 (예비)
  .gitignore
  CHANGELOG.md
  README.md
```

## 주의사항

- **`--compress` 금지** (정밀 리뷰 시): 함수 본문이 제거돼 GPT가 구현을 추측하게 된다.
- **`--force-answer-after` 금지** (정밀 리뷰 시): Pro 추론을 중간에 끊는다. 빠른 의견·짧은 질문에만 사용. (최대 대기를 넘기면 스크립트가 알아서 '지금 답변 받기'를 눌러 회수한다.)
- **ChatGPT Chat/Work 토글**: Work 모드엔 Pro 추론단계가 없다. 스크립트가 전송 전에 Chat으로 자동 전환하고, 실패하면 fail-closed로 중단한다.
- git submodule 안의 파일은 부모 레포 루트에서 패킹하면 repomix가 제외한다 — 서브모듈 디렉토리를 `--target`으로 직접 지정하라.
- 실행 중 전용 브라우저 창을 조작하지 말 것(background 모드면 창이 숨어 있다).
- 응답은 플러그인 내부가 아닌 **현재 작업 디렉토리의 `.insane-review/`**에 저장된다.
