---
name: vibe-sunsang-onboard
description: Initialize vibe-sunsang for Codex — create the local workspace, classify workspace types, generate CLAUDE.md, and run the first Codex-session conversion. Use when the user says "바선생 시작", "vibe-sunsang setup", "온보딩", "초기 설정", "초기화", "셋업", or wants to start tracking AI-collaboration growth.
---

# vibe-sunsang-onboard for Codex

> 바선생 초기 설정. 처음 한 번만 실행한다. 로컬 워크스페이스 생성 → 유형 분류 → CLAUDE.md 생성 → 첫 변환.

Codex는 skill-first다 (`commands/` 없음). 객관식은 Codex CLI에 카드 UI가 없으므로 `shared/questioning-policy.md §A` 번호 블록으로 채팅에서 묻는다 (위젯 흉내 금지).

## 참조 경로

- 사용자 데이터 루트: `~/vibe-sunsang/`
- 설정: `~/vibe-sunsang/config/`
- 변환 결과: `~/vibe-sunsang/conversations/`
- 결과 저장: `~/vibe-sunsang/exports/`
- 종단 로그: `~/vibe-sunsang/growth-log/`
- Codex 세션 원본: `~/.codex/sessions/` (JSONL)
- CLAUDE.md 템플릿: `$PLUGIN_ROOT/skills/vibe-sunsang-onboard/references/CLAUDE-MD-TEMPLATE.md`
- 변환 스크립트: `$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py`

## Step 0: 사용자 데이터 디렉토리 준비

`~/vibe-sunsang/`가 있는지 확인한다.

**이미 존재하는 경우 (재온보딩)** → `shared/questioning-policy.md §A` 번호 블록:

```text
질문: 이전에 설정한 바선생 데이터가 있습니다. 어떻게 할까요?
1. 새 프로젝트만 추가 — 기존 설정을 유지하면서 새 프로젝트만 추가해요 (추천)
2. 처음부터 다시 — 기존 설정을 백업(*.bak)하고 새로 시작해요
(모르면 1번으로 진행하겠습니다)
```

- 1번 → 기존 config를 읽어 매핑된 프로젝트는 건너뛰고 새 프로젝트만 진행.
- 2번 → 기존 config를 `*.bak`로 백업 후 새로 생성.

**존재하지 않는 경우:**

```bash
mkdir -p "$HOME/vibe-sunsang/config" "$HOME/vibe-sunsang/conversations" "$HOME/vibe-sunsang/exports" "$HOME/vibe-sunsang/growth-log/weekly"
```

## Step 0.5: 워크스페이스 환경 구성

**CLAUDE.md 생성** — `~/vibe-sunsang/CLAUDE.md`가 없으면:
1. `$PLUGIN_ROOT/skills/vibe-sunsang-onboard/references/CLAUDE-MD-TEMPLATE.md`를 읽는다 (인라인 하드코딩 금지).
2. `~/vibe-sunsang/CLAUDE.md`로 저장한다.

이미 있으면: "기존 CLAUDE.md를 유지합니다."

**.gitignore 생성** — `~/vibe-sunsang/.gitignore`가 없으면 생성:

```
# Large conversation files
conversations/**/*.md
!conversations/INDEX.md
```

**git init** — `~/vibe-sunsang/.git`이 없으면 `cd "$HOME/vibe-sunsang" && git init`. 플러그인 디렉토리에서는 실행하지 않는다.

## Step 1: 환영 & 설명

다음을 보여준다:

---

**바선생에 오신 것을 환영합니다!**

바선생은 Codex와 나눈 대화를 돌아보고 **AI와 더 잘 협업하는 법**을 배우게 해주는 AI 멘토입니다.

매주 한 번 이번 주 대화를 리뷰하면:
- 내가 어떤 실수를 반복하고 있는지
- AI에게 어떻게 요청하면 더 효과적인지
- 어떤 개념을 모르고 넘어갔는지

를 발견할 수 있습니다. 지금부터 초기 설정을 진행하겠습니다.

---

## Step 2: Codex 세션 확인

`~/.codex/sessions/`를 확인하여 사용 가능한 세션(JSONL)이 있는지 본다:

```bash
ls "$HOME/.codex/sessions/"
```

세션이 없으면:
> "아직 Codex 대화 기록이 없습니다. 먼저 Codex로 작업한 후 다시 와주세요." → 종료

세션이 있으면 다음 단계로 진행한다.

## Step 3: 프로젝트(워크스페이스) 매핑

Codex 세션은 각 JSONL의 `session_meta.cwd`(작업 디렉토리)로 워크스페이스를 식별한다. 변환기가 cwd의 마지막 경로 조각을 워크스페이스 이름으로 쓴다.

1. 세션 파일을 가볍게 훑어 등장하는 cwd(워크스페이스) 목록과 각 빈도를 파악한다.
2. 알아보기 쉬운 이름을 붙일 수 있게 안내한다. 변경이 필요하면 `shared/questioning-policy.md §A` 번호 블록으로 워크스페이스별로 묻는다:

```text
질문: 이 워크스페이스(`~/code/my-project`, 세션 12개)의 이름을 뭐라고 할까요?
1. my-project — 디렉토리 경로에서 추측한 이름이에요 (추천)
2. 문장으로 직접 다른 이름 알려주세요
3. 건너뛰기 — 이 워크스페이스는 분석하지 않아요
(모르면 1번으로 진행하겠습니다)
```

> 질문과 1번 라벨은 각 워크스페이스에 맞게 동적 생성한다.

**규칙:**
- 한 번에 5개까지만 묻는다 (피로 방지). 5개 초과면 5개씩 나눠 "더 진행할까요?" 확인.
- 세션이 5개 미만인 워크스페이스는 자동으로 건너뛴다 (사용자에게 알림).
- "건너뛰기"는 매핑에서 제외. 재온보딩 시 이미 매핑된 워크스페이스는 건너뛴다.

결과를 `~/vibe-sunsang/config/project_names.json`에 저장한다 (cwd → 표시명 매핑).

## Step 4: 워크스페이스 유형 분류

각 워크스페이스 디렉토리(cwd)의 `CLAUDE.md`/`AGENTS.md`/`README.md`를 읽어 유형을 추론한다.

**유형 분류 기준:**

| 유형 | 키워드/패턴 | 설명 |
|------|------------|------|
| **Builder** (구현자) | build, test, deploy, component, API, 코딩, 개발, 앱 | 코딩/개발 |
| **Explorer** (탐험자) | research, study, analyze, 리서치, 학습, 스터디, Q&A | 리서치/Q&A/학습 |
| **Designer** (기획자) | plan, design, ideation, 기획, 아이디어, 콘텐츠, 글쓰기 | 기획/아이디에이션 |
| **Operator** (운영자) | automate, workflow, schedule, 자동화, 연동, 스크립트, MCP | 업무 자동화 |

문서를 못 찾으면 파일 구조를 간단히 확인(`.py`/`.js`가 많으면 Builder 등). 추론이 어려우면 `shared/questioning-policy.md §A` 번호 블록으로 묻는다:

```text
질문: [워크스페이스명]을(를) 분석해보니 [추론된 유형] 워크스페이스로 보입니다. 맞나요?
1. Builder (코딩) — 코딩/개발 프로젝트
2. Explorer (리서치/학습) — 리서치/Q&A/스터디
3. Designer (기획) — 기획/아이디에이션
4. Operator (자동화) — 업무 자동화/데이터처리
(추론한 유형이 맞으면 그 번호로, 아니면 다른 번호로 답해주세요)
```

> question은 각 워크스페이스 이름과 추론 유형으로 동적 생성. 여러 목적이면 주된 목적 1개. 같은 유형이 반복되면 묶어서 한 번에 확인.

결과를 `~/vibe-sunsang/config/workspace_types.json`에 저장:

```json
{
  "schema_version": 1,
  "type_definitions": {
    "builder": "코딩/개발",
    "explorer": "리서치/Q&A/스터디",
    "designer": "기획/아이디에이션",
    "operator": "자동화/데이터처리"
  },
  "default_type": "builder",
  "workspaces": {
    "my-app": {
      "type": "builder",
      "name": "my-app",
      "detected_from": "CLAUDE.md",
      "confirmed": true
    }
  }
}
```

## Step 5: 첫 변환 실행

```bash
python3 "$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py" --force --output-dir "$HOME/vibe-sunsang/conversations" 2>/dev/null || python "$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py" --force --output-dir "$HOME/vibe-sunsang/conversations"
```

변환 진행 상황을 보여주고 완료되면 요약한다:
- 총 워크스페이스 수
- 총 세션 수
- 가장 활발한 워크스페이스 TOP 3
- **유형별 분포** (Builder N개, Explorer N개, ...)

## Step 6: 사용법 안내

---

**설정 완료!** 유형별 맞춤 분석을 받을 수 있습니다:

| 유형 | 분석 내용 |
|------|----------|
| Builder (구현자) | 코딩 요청 품질, 에러 대응, 코드 이해도 |
| Explorer (탐험자) | 질문 깊이, 출처 검증, 비판적 사고 |
| Designer (기획자) | 기획 구체성, 구조화, 실현 가능성 |
| Operator (운영자) | 자동화 품질, 에러 처리, 재사용성 |

**v2 레벨 시스템** — 6가지 기술 차원으로 AI 활용 능력을 분석합니다:

| 기술 차원 | 쉬운 설명 |
|----------|----------|
| DECOMP (작업 분해) | 큰 요청을 작은 단계로 나누는 능력 |
| VERIFY (검증 전략) | AI 결과를 확인하고 검증하는 능력 |
| ORCH (오케스트레이션) | 여러 도구를 조합하여 활용하는 능력 |
| FAIL (실패 대응) | 오류가 나면 원인을 파악하고 대처하는 능력 |
| CTX (맥락 관리) | AI에게 필요한 정보를 잘 전달하는 능력 |
| META (메타인지) | 내가 AI를 어떻게 쓰는지 돌아보는 능력 |

레벨은 L1.0(입문)부터 L7.0(마스터)까지 0.5 단위로 측정됩니다. 유형마다 중요한 축이 달라 맞춤 분석을 받을 수 있어요.

사용할 수 있는 기능 (Codex skill로 실행):

| 기능 | 설명 |
|------|------|
| "변환해줘" (vibe-sunsang-retro) | 새 대화 변환 (매주 실행 권장) |
| "멘토링해줘" (vibe-sunsang-mentor) | AI 활용 능력 코칭 (유형별 6축 맞춤) |
| "성장 리포트 만들어줘" (vibe-sunsang-growth) | 성장 분석 리포트 (6축 레이더 차트 포함) |

**추천 루틴:** 매주 금요일 "변환해줘" → "멘토링해줘"로 이번 주 리뷰 → 행동 계획 실천.

---

## Step 7: 바로 시작할지 물어보기

`shared/questioning-policy.md §A` 번호 블록:

```text
질문: 바로 이번 주 리뷰를 시작해볼까요?
1. 멘토링 시작 — AI 활용 능력 코칭 세션을 바로 시작해요 (6축 분석)  → vibe-sunsang-mentor
2. 성장 리포트 생성 — 성장 분석 리포트를 자동 생성해요 (6축 레이더)  → vibe-sunsang-growth
3. 나중에 할게요 — 여기서 마무리할게요
(모르면 1번으로 진행하겠습니다)
```

선택에 따라: 1→ vibe-sunsang-mentor, 2→ vibe-sunsang-growth, 3→ 종료.

## Gotchas

- CLAUDE-MD-TEMPLATE.md를 인라인으로 하드코딩하지 않는다. 반드시 `$PLUGIN_ROOT/skills/vibe-sunsang-onboard/references/CLAUDE-MD-TEMPLATE.md`에서 읽는다.
- 기존 데이터가 있는 디렉토리를 덮어쓰지 않는다. 충돌 시 사용자에게 확인받는다.
- git init은 사용자 워크스페이스(`~/vibe-sunsang/`)에서만 실행한다.
- Codex 세션 원본은 `~/.codex/sessions/`다 (Claude Code의 `~/.claude/projects/`가 아님).
- 변환 중 분석이 완료됐다고 말하지 않는다. 변환은 데이터 준비일 뿐이다.
