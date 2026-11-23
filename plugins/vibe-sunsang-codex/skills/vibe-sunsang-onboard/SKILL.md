---
name: vibe-sunsang-onboard
description: 'Vibe-sunsang initial setup for Codex — self-heals the local workspace, links Codex session projects, classifies workspace types, generates AGENTS.md, and runs the first conversion. Korean triggers: "바선생 시작", "온보딩", "초기 설정", "초기화", "셋업". English triggers: "onboarding", "init", "setup", "start vibe-sunsang".'
---

# 바선생 온보딩 (Codex)

> 처음 한 번만 실행한다. 워크스페이스 자가 치유 → 프로젝트 매핑 → 유형 분류 → AGENTS.md 생성 → 첫 변환.

Codex는 skill-first다 (별도 커맨드 파일 없음). 객관식은 `$PLUGIN_ROOT/shared/questioning-policy.md §A`의 질문 도구(`request_user_input_async`, Plan 모드는 `request_user_input`)로 묻고, 두 도구가 모두 없을 때만 번호 블록으로 채팅에서 묻는다. async 도구는 부른 뒤 한 줄 안내만 쓰고 턴을 끝낸다(답은 다음 메시지로 온다). 아래 번호 블록 예시는 폴백일 때의 모양이다. 열린 코칭 질문은 도구 없이 평범한 채팅으로 묻는다 (도구가 없는데 위젯을 흉내 내지 말 것).

async 호출 형식: `{"questions":[{"title":"헤더 — 질문","options":["추천안 (추천) — 설명","대안 — 설명"]}]}`. 문항에는 `title`·`options`(문자열 배열)만 넣는다. `question`·`header`·`id`는 Plan 모드 `request_user_input` 전용이라 async에 넣으면 파싱 오류가 난다. "기타·직접 적기" 선택지는 넣지 않는다(자유 입력 칸이 자동으로 붙는다).

## 참조 경로

- 사용자 데이터 루트: `~/vibe-sunsang/`
- 설정: `~/vibe-sunsang/config/`
- 변환 결과: `~/vibe-sunsang/conversations/`
- 결과 저장: `~/vibe-sunsang/exports/`
- 종단 로그: `~/vibe-sunsang/growth-log/`
- Codex 세션 원본: `~/.codex/sessions/` (JSONL. `$CODEX_HOME/sessions`가 있으면 그쪽)
- AGENTS.md 템플릿: `$PLUGIN_ROOT/references/AGENTS-MD-TEMPLATE.md`
- 스크립트: `$PLUGIN_ROOT/scripts/ensure_workspace.py`, `$PLUGIN_ROOT/scripts/convert_sessions.py`

### Step 0: 사용자 데이터 디렉토리 준비

`~/vibe-sunsang/` 디렉토리가 있는지 확인합니다.

**이미 존재하는 경우 (재온보딩)** → `shared/questioning-policy.md §A` 질문 도구 1콜(`request_user_input_async`, Plan 모드는 `request_user_input`; 둘 다 없으면 번호 블록 폴백). 번호 블록 폴백일 때의 모양:

```text
질문: 이전에 설정한 바선생 데이터가 있습니다. 어떻게 할까요?
1. 새 프로젝트만 추가 — 기존 설정을 유지하면서 새 프로젝트만 추가해요 (추천)
2. 처음부터 다시 — 기존 config 파일을 백업(*.bak)하고 새로 시작해요
(모르면 1번으로 진행하겠습니다)
```

선택에 따라:
- 1번 → 기존 config 파일을 읽어 매핑된 프로젝트를 건너뛰고 새 프로젝트만 진행
- 2번 → 기존 config 파일을 백업(`*.bak`) 후 새로 생성

**존재하지 않거나 v1 구조인 경우 — 디렉토리 생성/마이그레이션은 스크립트에 위임:**

```bash
python3 "$PLUGIN_ROOT/scripts/ensure_workspace.py" 2>/dev/null || python "$PLUGIN_ROOT/scripts/ensure_workspace.py"
```

이 스크립트가 `config/ conversations/ exports/ growth-log/weekly/`를 보장하고, v1 번호 접두사 구조(`40-conversations`, `90-exports`, `30-growth-log`, **그리고 `10-scripts/*.json` config**)를 **비파괴적으로** 새 구조로 이관한다. 출력 `STATUS v1_migrated`면 다음과 같이 안내한다:

> "이전 버전의 폴더 구조를 감지해 데이터(대화·리포트·성장로그·설정)를 새 구조로 자동 이관했습니다. 기존 파일은 덮어쓰지 않았어요."

`00-system/`, `20-knowledge-base/` 등 나머지 v1 잔여물은 데이터가 아니므로 그대로 두거나, 사용자가 원하면 정리하도록 안내만 한다(자동 삭제 금지).

### Step 0.5: 워크스페이스 환경 구성

> 디렉토리 생성·마이그레이션은 Step 0의 `ensure_workspace.py`가 이미 끝냈다. 아래는 나머지 초기화만 수행한다.

**AGENTS.md 생성** (Codex가 이 폴더에서 읽는 지침 파일):

`~/vibe-sunsang/AGENTS.md`가 없으면:
1. `$PLUGIN_ROOT/references/AGENTS-MD-TEMPLATE.md`의 내용을 읽는다
2. `~/vibe-sunsang/AGENTS.md`에 저장한다

이미 있으면:
> "기존 AGENTS.md를 유지합니다."

**.gitignore 생성:**

`~/vibe-sunsang/.gitignore`가 없으면 생성:

```
# Large conversation files
conversations/**/*.md
!conversations/INDEX.md
```

이미 있으면 건너뛴다.

**git init:**

`~/vibe-sunsang/.git`이 없으면:
```bash
cd "$HOME/vibe-sunsang" && git init
```

이미 있으면 건너뛴다.

### Gotchas

- AGENTS-MD-TEMPLATE.md를 인라인으로 하드코딩하지 않는다. 반드시 `$PLUGIN_ROOT/references/AGENTS-MD-TEMPLATE.md`에서 읽는다.
- 마이그레이션 시 기존 데이터가 있는 디렉토리를 덮어쓰지 않도록 주의한다. 충돌 시 사용자에게 확인받는다.
- git init은 사용자 워크스페이스에서만 실행한다. 플러그인 디렉토리에서 실행하지 않는다.
- Codex 세션 원본은 `~/.codex/sessions/`다. 다른 코딩 에이전트의 세션 폴더는 변환기가 읽지 않는다 (형식이 다름).
- 변환 중 분석이 완료됐다고 말하지 않는다. 변환은 데이터 준비일 뿐이다.

### Step 1: 환영 & 설명

다음 메시지를 사용자에게 보여줍니다:

---

**바선생에 오신 것을 환영합니다!**

바선생은 Codex와 나눈 대화를 돌아보고, **AI와 더 잘 협업하는 법**을 배우게 해주는 AI 멘토 에이전트입니다.

매주 한 번 여기서 이번 주 대화를 리뷰하면:
- 내가 어떤 실수를 반복하고 있는지
- AI에게 어떻게 요청하면 더 효과적인지
- 어떤 개념을 모르고 넘어갔는지

를 발견할 수 있습니다.

지금부터 초기 설정을 진행하겠습니다.

---

### Step 2: Codex 세션 확인

변환기로 사용 가능한 프로젝트(작업 디렉토리) 목록을 가져옵니다. Codex 세션은 각 JSONL의 `session_meta.cwd`로 프로젝트가 식별됩니다:

```bash
python3 "$PLUGIN_ROOT/scripts/convert_sessions.py" --list-projects --names-file "$HOME/vibe-sunsang/config/project_names.json" 2>/dev/null || python "$PLUGIN_ROOT/scripts/convert_sessions.py" --list-projects --names-file "$HOME/vibe-sunsang/config/project_names.json"
```

출력은 `cwd<TAB>sessions<TAB>display_name` TSV(세션 수 내림차순)입니다.

세션 디렉토리가 없어 `[ERROR]`가 나오거나 목록이 비어 있으면:
> "아직 Codex 대화 기록이 없습니다. 먼저 다른 프로젝트에서 Codex를 사용한 후 다시 와주세요."
> → 여기서 종료

프로젝트가 있으면 다음 단계로 진행합니다.

### Step 3: 프로젝트 이름 매핑

발견된 프로젝트 목록을 보여주고, 사용자에게 읽기 좋은 이름을 지정하도록 안내합니다.

**안내 메시지:**

> Codex가 저장한 프로젝트들을 발견했습니다.
> 각 프로젝트에 알아보기 쉬운 이름을 붙여주세요.
>
> 경로가 복잡해 보여도 걱정하지 마세요 - 실제 작업 폴더 경로입니다.

각 프로젝트에 대해:
1. `display_name`(폴더명에서 자동 생성된 이름)을 추측값으로 쓴다. 같은 폴더명이 다른 경로에 있으면 변환기가 부모 폴더명을 접두로 붙여 구분해 준다.
2. `shared/questioning-policy.md §A` 질문 도구 1콜(`request_user_input_async`, Plan 모드는 `request_user_input`; 둘 다 없으면 번호 블록 폴백)으로 묻는다 (프로젝트별로 반복). 번호 블록 폴백일 때의 모양:

```text
질문: 이 프로젝트(`~/code/my-project`, 세션 12개)의 이름을 뭐라고 할까요?
1. my_project — 폴더 이름에서 추측한 이름이에요 (추천)
2. 문장으로 직접 다른 이름 알려주세요
3. 건너뛰기 — 이 프로젝트는 분석하지 않아요
(모르면 1번으로 진행하겠습니다)
```

> 질문과 1번 라벨은 각 프로젝트에 맞게 동적 생성한다.

**규칙:**
- 한 번에 5개까지만 질문합니다 (너무 많으면 피로)
- 프로젝트가 5개를 초과하면 5개씩 나눠서 반복합니다. 각 묶음 후 "더 진행할까요?"를 확인합니다.
- 세션이 5개 미만인 프로젝트는 자동으로 건너뜁니다 (사용자에게 알림). 임시 폴더(`/tmp`, `/private/var/folders`)에서 돈 세션도 건너뜁니다.
- "건너뛰기"를 선택한 프로젝트는 매핑에서 제외
- **재온보딩 시**: 이미 매핑된 프로젝트는 건너뛰고 새 프로젝트만 질문

결과를 `~/vibe-sunsang/config/project_names.json`에 저장합니다 (키 = cwd 경로, 값 = 표시 이름):

```json
{
  "/home/me/code/my-project": "my_project"
}
```

### Step 4: 워크스페이스 유형 분류

**각 프로젝트 폴더(cwd)의 AGENTS.md 또는 README.md를 읽어서 유형을 추론합니다.**

분류 흐름:
1. 프로젝트 경로에서 `AGENTS.md` 또는 `README.md`를 찾아 읽기
2. 내용을 기반으로 유형을 추론
3. 사용자에게 추론 결과를 보여주고 확인받기

**유형 분류 기준:**

| 유형 | 키워드/패턴 | 설명 |
|------|------------|------|
| **Builder** (구현자) | build, test, deploy, component, API, 코딩, 개발, 앱 | 코딩/개발 프로젝트 |
| **Explorer** (탐험자) | research, study, analyze, 리서치, 학습, 스터디, Q&A, 질문 | 리서치/Q&A/학습 |
| **Designer** (기획자) | plan, design, ideation, 기획, 아이디어, 콘텐츠, 글쓰기 | 기획/아이디에이션 |
| **Operator** (운영자) | automate, workflow, schedule, 자동화, 연동, 스크립트, MCP | 업무 자동화 |

**AGENTS.md/README를 찾을 수 없는 경우:**
- 해당 프로젝트의 파일 구조를 간단히 확인 (`.py`, `.js` 파일이 많으면 Builder 등)
- 추론이 어려우면 사용자에게 직접 질문

각 프로젝트에 대해 `shared/questioning-policy.md §A` 질문 도구 1콜(`request_user_input_async`, Plan 모드는 `request_user_input`; 둘 다 없으면 번호 블록 폴백)으로 확인한다. 번호 블록 폴백일 때의 모양:

```text
질문: [프로젝트명]의 AGENTS.md를 분석해보니 [유형] 워크스페이스로 보입니다. 맞나요?
1. Builder (코딩) — 코딩/개발 프로젝트
2. Explorer (리서치/학습) — 리서치/Q&A/스터디
3. Designer (기획) — 기획/아이디에이션
4. Operator (자동화) — 업무 자동화/데이터처리
(추론한 유형이 맞으면 그 번호로, 아니면 다른 번호로 답해주세요)
```

> 질문은 각 프로젝트의 이름과 추론된 유형으로 동적 생성한다.

**규칙:**
- 프로젝트가 여러 목적이면 주된 목적 1개를 선택
- 같은 유형이 여러 프로젝트에 반복되면 묶어서 한 번에 확인

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
    "my_project": {
      "type": "builder",
      "name": "my_project",
      "cwd": "/home/me/code/my-project",
      "detected_from": "AGENTS.md",
      "confirmed": true
    }
  }
}
```

> `workspaces`의 키는 변환 결과 폴더명과 같은 **표시 이름**(project_names.json의 값)으로 둔다. growth/mentor 스킬이 INDEX.md의 프로젝트명으로 유형을 찾기 때문이다.

### Step 5: 첫 변환 실행

```bash
python3 "$PLUGIN_ROOT/scripts/convert_sessions.py" --force --names-file "$HOME/vibe-sunsang/config/project_names.json" --output-dir "$HOME/vibe-sunsang/conversations" 2>/dev/null || python "$PLUGIN_ROOT/scripts/convert_sessions.py" --force --names-file "$HOME/vibe-sunsang/config/project_names.json" --output-dir "$HOME/vibe-sunsang/conversations"
```

변환 진행 상황을 보여주고, 완료되면 결과를 요약합니다:
- 총 프로젝트 수
- 총 세션 수
- 가장 활발한 프로젝트 TOP 3
- **유형별 분포** (Builder N개, Explorer N개, ...)

### Step 6: 사용법 안내

---

**설정 완료!**

프로젝트 유형별로 맞춤 분석을 받을 수 있습니다:

| 유형 | 분석 내용 |
|------|----------|
| Builder (구현자) | 코딩 요청 품질, 에러 대응, 코드 이해도 |
| Explorer (탐험자) | 질문 깊이, 출처 검증, 비판적 사고 |
| Designer (기획자) | 기획 구체성, 구조화, 실현 가능성 |
| Operator (운영자) | 자동화 품질, 에러 처리, 재사용성 |

**v2 레벨 시스템:**

바선생은 6가지 기술 차원으로 AI 활용 능력을 분석합니다:

| 기술 차원 | 쉬운 설명 |
|----------|----------|
| DECOMP (작업 분해) | 큰 요청을 작은 단계로 나누는 능력 |
| VERIFY (검증 전략) | AI 결과를 확인하고 검증하는 능력 |
| ORCH (오케스트레이션) | 여러 도구를 조합하여 활용하는 능력 |
| FAIL (실패 대응) | 오류가 나면 원인을 파악하고 대처하는 능력 |
| CTX (맥락 관리) | AI에게 필요한 정보를 잘 전달하는 능력 |
| META (메타인지) | 내가 AI를 어떻게 쓰는지 돌아보는 능력 |

레벨은 L1.0(입문)부터 L7.0(마스터)까지, 0.5 단위로 세밀하게 측정됩니다. 유형마다 중요한 축이 달라서, 나에게 맞는 맞춤 분석을 받을 수 있어요.

사용할 수 있는 기능 (Codex 스킬로 실행):

| 기능 | 설명 |
|------|------|
| "변환해줘" (vibe-sunsang-retro) | 새 대화 변환 (멘토링·성장 진입 시 자동 선행되므로 수동은 선택) |
| "멘토링해줘" (vibe-sunsang-mentor) | AI 활용 능력 코칭 (유형별 6축 맞춤, 지난 리뷰 이후 증분) |
| "성장 리포트 만들어줘" (vibe-sunsang-growth) | 성장 분석 리포트 (레벨 헤드라인 + 다음 한 수 3개) |

**추천 루틴:**
1. 매주 금요일, `~/vibe-sunsang/`에서 `codex` 실행
2. "멘토링해줘" 로 이번 주 리뷰 (새 대화는 자동 변환·선택됨)
3. 행동 계획 실천

---

### Step 7: 바로 시작할지 물어보기

`shared/questioning-policy.md §A` 질문 도구 1콜(`request_user_input_async`, Plan 모드는 `request_user_input`; 둘 다 없으면 번호 블록 폴백). 번호 블록 폴백일 때의 모양:

```text
질문: 바로 이번 주 리뷰를 시작해볼까요?
1. 멘토링 시작 — AI 활용 능력 코칭 세션을 바로 시작해요 (6축 분석)
2. 성장 리포트 생성 — 성장 분석 리포트를 자동 생성해요 (레벨 헤드라인 + 다음 한 수)
3. 나중에 할게요 — 여기서 마무리할게요
(모르면 1번으로 진행하겠습니다)
```

선택에 따라:
- 1번 → vibe-sunsang-mentor 스킬 실행
- 2번 → vibe-sunsang-growth 스킬 실행
- 3번 → 종료
