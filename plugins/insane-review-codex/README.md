# insane-review-codex

GPT-5.5 Pro(웹 전용 — API 없음)를 Codex CLI 안으로 끌어오는 브리지 플러그인.

repomix로 관련 코드만 정밀 패킹 → 구독 ChatGPT 웹에 CDP 자동화로 투입 → 분석/리뷰 회수.
API 비용 0, 사용자의 ChatGPT 요금제로 동작.

## 사용 조건

- Comet 또는 Chrome — `--remote-debugging-port=9222`로 실행 + chatgpt.com 로그인 + 모델 GPT-5.5 Pro
- Python 의존성: `pip install playwright pyperclip`
- Node.js (npx — repomix 자동설치에 사용)

## 환경 점검

```bash
python3 scripts/pack_and_ask.py --check-env
# 부족한 pip 패키지 자동설치:
python3 scripts/pack_and_ask.py --check-env --install
```

## 기본 사용법

```bash
# 디렉토리를 통째로 패킹해 GPT Pro 리뷰 요청
python3 scripts/pack_and_ask.py \
  --target ./src \
  --model pro --require-model "GPT-5.5" \
  --prompt "이 모듈의 설계 리뷰를 해줘. 판정마다 파일:라인 인용 필수."

# 순수 질문만 (코드 없이)
python3 scripts/pack_and_ask.py \
  --model pro --force-answer-after 90 \
  --prompt "비동기 큐 설계에서 backpressure를 어떻게 다루면 좋을까?"
```

응답은 **현재 프로젝트의 `.insane-review/response_*.md`**에 저장된다.

## agent-council 웹 멤버로 등록

`skills/insane-review/references/council-setup.md` 참고.

```bash
# council 계약 검증 (stdout=응답만, stderr=로그)
python3 scripts/pack_and_ask.py --council --model pro \
  --force-answer-after 60 "한 문장으로: 1+1은?" 2>/dev/null
```

## 주요 플래그

| 플래그 | 설명 |
|--------|------|
| `--target <dir>` | 패킹 대상 디렉토리 (생략 시 프롬프트-only) |
| `--include <glob>` | repomix 포함 글롭 (정밀 선별) |
| `--model pro` | 추론단계 선택 |
| `--require-model "GPT-5.5"` | 모델명 검증 — 불일치 시 전송 중단 (fail-closed) |
| `--force-answer-after N` | N초 후 리즈닝 강제 종료 (빠른 의견용; 정밀 리뷰엔 쓰지 말 것) |
| `--pack-only` | 패킹만 하고 전송하지 않음 |
| `--council` | agent-council 멤버 모드 — 응답만 stdout |
| `--retries N` | 전송/회수 재시도 횟수 |
| `--delete-pack` | 응답 회수 후 패킹 파일 삭제 (시크릿 위생) |
| `--browser comet\|chrome` | 브라우저 선택 (기본: comet) |
| `--check-env` | 환경 점검 |
| `--install` | `--check-env`와 함께 — pip 의존성 자동설치 |

## 파일 구조

```
insane-review-codex/
  .codex-plugin/plugin.json       — 플러그인 메타데이터
  skills/insane-review/
    SKILL.md                      — 스킬 실행 지시서
    references/council-setup.md  — agent-council 등록 가이드
  scripts/
    pack_and_ask.py               — repomix 패킹 + ChatGPT CDP 브리지
  assets/                         — 아이콘 등 (예비)
  .gitignore
  README.md
```

## 주의사항

- **`--compress` 금지** (정밀 리뷰 시): 함수 본문이 제거돼 GPT가 구현을 추측하게 된다.
- **`--force-answer-after` 금지** (정밀 리뷰 시): Pro 추론을 중간에 끊는다. 빠른 의견·짧은 질문에만 사용.
- git submodule 안의 파일은 부모 레포 루트에서 패킹하면 repomix가 제외한다 — 서브모듈 디렉토리를 `--target`으로 직접 지정하라.
- 응답은 플러그인 내부가 아닌 **현재 작업 디렉토리의 `.insane-review/`**에 저장된다.
