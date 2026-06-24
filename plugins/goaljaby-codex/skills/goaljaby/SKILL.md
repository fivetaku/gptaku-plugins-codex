---
name: goaljaby
description: PRD 폴더를 받아 사용자 언어로 검토 문서 5종(VALIDATION/RECOVERY/PLAN/PROGRESS 대응 + PLANS.md ExecPlan)을 생성하고, 검토 요약을 대화창에 띄운 뒤 사용자 승인을 받으면 복사해서 실행할 수 있는 Codex `/goal` 명령을 건넨다. 트리거 — "/goaljaby", "골잡이", "골 셋업 만들어줘", "PRD에서 골 만들어줘", "PRD 골 변환", "VALIDATION RECOVERY 만들어줘", "골 실행 준비", "set up goal from PRD", "goaljaby", "prep goal docs", "make goal scaffolding". PRD 폴더가 있고 `/goal` 기반 장시간 세션으로 넘어가고 싶을 때 사용한다.
---

# 골잡이 (goaljaby) — Codex 판

> PRD를 Codex `/goal` 운영 계약으로 변환하는 브릿지 스킬. **사용자 언어로** 검토 문서 5종 + `PLANS.md` ExecPlan을 생성하고, 검토 요약을 대화창에 띄운 뒤 승인을 받으면 **복사해서 바로 실행할 수 있는 `/goal` 명령**을 건넨다.

Read these first:
- `references/templates.md`
- `references/compact-strategy.md`
- `references/task-type-classifier.md`
- `references/task-type-templates.md`

질문 정책은 `shared/questioning-policy.md` (특히 §A 렌더링 규칙 + §0~§2)을 상속한다.

## 첫 실행 설정 (수동 — 훅 아님)

> Codex 플러그인은 hooks를 지원하지 않는다. 본진 goaljaby의 `setup/setup.sh`(자동 스타·업데이트 체크)는 **이식하지 않는다.**
> 별도 부트스트랩이 필요하면 사용자가 직접 실행하는 1회 단계로만 안내한다(현재 이 스킬은 외부 부트스트랩이 필요 없다). 이 스킬은 PRD 읽기·검토 문서 쓰기 외에 아무 부수효과도 만들지 않는다.

## Claude Code 판과의 차이 (왜 Codex 판이 따로 있나)

본진 goaljaby는 "Claude Code 전용"이다. 마지막에 어시스턴트가 응답의 *마지막 줄*로 `/goal`을 출력하면 Claude Code가 그 줄을 다음 턴 입력으로 처리해 골 루프를 자동 시작한다. **Codex에는 이 메커니즘이 없다** — 스킬이 슬래시 명령을 마지막 줄로 "자동 발사"할 수 없다.

대신 Codex에는 **네이티브 `/goal`** (codex 0.139에서 `goals` 기능 stable=true)과 `/plan` 모드, 그리고 `PLANS.md`/ExecPlan 관례가 있다. 그래서 이 판은:

- 본진의 검토 문서 5종(VALIDATION/RECOVERY/PLAN/PROGRESS + goal-command)을 그대로 한국어로 생성하고,
- 추가로 `PLANS.md` ExecPlan 파일(**Progress / Validation / Decision-Log** 섹션)을 생성해 본진 5종을 그 위에 매핑한다.
- 마지막에 슬래시 명령을 자동 발사하는 대신, 사용자가 **복사해서 실행**할 `/goal` 명령 한 줄을 제시한다.
- objective는 ≤ 4,000자로 유지하고, **파일 포인터 패턴**을 쓴다 — objective 본문이 `./PLANS.md`를 가리킨다.

## 언어 정책 (shared/language-policy.md 상속)

> **출력 언어 = 사용자 요청 언어(`output_lang`)**. 본문을 읽기 전에 §1 자동 감지로 잠근다:
> 요청 텍스트의 언어 → 없으면 직전 대화 언어 → 둘 다 없으면(빈 호출) 영어. **한국 제작이라고 한국어를 기본값으로 두지 말 것.**

생성되는 6종 문서(5종 + PLANS.md)는 **`output_lang` 본문 + 영어 식별자**(파일명·명령·약어·슬롯). 핵심은 언어가 아니라 **"사용자가 읽고 검토할 수 있어야 승인에 의미가 있다"** 이다 — 그래서 한국어 사용자에겐 한국어로, 영어 사용자에겐 영어로 생성한다. 검토 불가능한 외국어 문서는 승인 게이트를 무의미하게 만든다.

- `output_lang ∈ {ko, en}`: 헤딩까지 1급 지원(결정론적 검증, Step 7 #7). 헤딩 세트는 `references/templates.md`의 §헤딩 맵 참조.
- 그 외 언어: 본문·헤딩을 번역하되 결정론적 헤딩 검증은 섹션 존재 검사로 폴백하고 그 한계를 Step 8 요약에 한 줄로 알린다(침묵 폴백 금지).
- 식별자(파일명/명령/약어/`{SLOT}`/`PRD`·`SDD`)와 PROTECTED_CLAUSES 앵커, PLANS.md의 ExecPlan 표준 섹션명(`Progress`/`Validation`/`Decision-Log`)은 번역하지 않는다(§2).

## 입력

- **필수**: PRD 디렉토리 경로 (**절대 경로 권장**, 예: `/Users/<username>/my-project/PRD/`). 최소 1개 `.md` 파일, acceptance criteria 포함 권장.
- **선택**: 작업 유형(자동 추정 가능), 골 엄격도, 출력 위치

상대 경로(`./PRD/`)도 동작하지만 세션 cwd가 달라지면 깨질 수 있으므로 절대 경로가 안전하다.

PRD가 없으면 `show-me-the-prd` 스킬로 위임한다 (Step 0). 인수 파싱:
- 인수 없음 → §A 번호 블록으로 PRD 디렉토리 경로를 묻는다 (아래 Step 0-B). PRD 자체가 없으면 `show-me-the-prd` 위임 옵션을 1번으로 제시.
- 절대/상대 경로 → 그 경로를 `prd_dir`로 사용.
- "분석 [경로]" → 기존 산출물 검토 모드 (덮어쓰기 전 확인).

## 출력

### 항상 생성되는 6개 파일 (모두 `output_lang` 본문)

```
[output_dir]/
├── VALIDATION.md      — 필수 검증 / 마일스톤별 검증 / 완료 기준 매핑 / 완료로 보지 않는 조건
├── RECOVERY.md        — 기본 원칙 / 실패 루프 / 재시도 한계 / scope 잠금 / 방향 재확인 / 되돌리기 규칙
├── PLAN.md            — 목표 / 참조 문서 / 마일스톤(≤5) / 최종 완료 기준
├── PROGRESS.md        — 빈 초기 템플릿 + Step 8에서 상단에 4줄 요약 prepend됨
├── goal-command.md    — `/goal` 실행 본문 (`output_lang`, 4,000자 강제, ./PLANS.md 포인터)
└── PLANS.md           — Codex ExecPlan (Progress / Validation / Decision-Log) — 위 5종을 한 파일에 매핑
```

검토 요약은 **별도 파일로 만들지 않는다.** Step 8에서 대화창에 직접 표시하고, 핸드오프 용도로 PROGRESS.md와 PLANS.md의 Progress 섹션 상단에만 4줄 요약을 prepend한다.

**보장사항**:
- `goal-command.md` 본문은 항상 4,000자 이하 (문자 수 기준, byte 아님).
- 5종 검토 문서 + PLANS.md는 모두 `output_lang` 헤딩 + 본문. 감지 언어와 다른 언어의 헤딩이 잔존하면 Step 7 검증에서 실패 → 결과물 폐기 (ko↔en 교차 검증, 그 외 언어는 섹션 존재 검사). 단 PLANS.md의 ExecPlan 표준 섹션명(`Progress`/`Validation`/`Decision-Log`)은 식별자로 보존.
- PROTECTED_CLAUSES 5종은 한국어/영어 OR 정규식으로 검증 (`compact-strategy.md` 참조).

### 본진 5종 → PLANS.md ExecPlan 매핑

| 본진 문서 | PLANS.md 섹션 |
|--|--|
| PLAN.md (목표 / 마일스톤) | `## 목표` + `## 마일스톤` |
| PROGRESS.md (진척) | `## Progress` |
| VALIDATION.md (필수 검증 / 완료 기준) | `## Validation` |
| RECOVERY.md (실패 루프 / scope 잠금 / 3회 룰) | `## Decision-Log` 상단 운영 규칙 요약 + "RECOVERY.md를 따른다" |
| goal-command.md (/goal 본문) | PLANS.md 최상단 `> /goal {…} ./PLANS.md` 인용 한 줄 |

PLANS.md는 5종을 대체하지 않는다 — **Codex /goal이 한 파일만 읽어도 컨텍스트를 잡도록** 5종을 한 곳에 모은 운영 진실 원천이다. 상세는 여전히 개별 파일(VALIDATION.md 등)에 위임한다.

## 워크플로우 (10단계)

> **언어 잠금 (먼저)**: 워크플로우 시작 전 `shared/language-policy.md §1`로 `output_lang`을 감지·고정한다. 이후 모든 산출물(6종 문서·헤딩·대화 요약·Step 10 핸드오프 안내)은 `output_lang`을 따른다. 식별자/슬롯/PROTECTED_CLAUSES 앵커/PLANS.md ExecPlan 표준 섹션명은 제외(§2).

### Step 0: PRD 사전 확인 + 입력 분기
**타입**: Bash + §A 번호 블록 (조건부)

PRD 디렉토리 인수와 내용을 확인한다.

**0-A) 인수 있음 + 디렉토리 존재 + `.md` 1개 이상**
- Bash로 acceptance criteria 패턴(`- [ ]`, "Acceptance Criteria", "완료 판정", "completion criteria") 확인. 없으면 Step 1에서 경고하지만 진행은 계속한다.
- 기존 산출물(VALIDATION.md / RECOVERY.md / PLAN.md / PROGRESS.md / goal-command.md / PLANS.md 중 하나라도) 존재 시 §A 번호 블록:
  - `1. 덮어쓰기 — 기존 6종을 새로 생성 (추천)`
  - `2. 이어가기 — 기존 PROGRESS.md/PLANS.md만 읽고 /goal 재실행을 안내`
  - `3. 취소`
- → Step 1 진입.

**0-B) 인수 없음 OR 디렉토리 없음 OR `.md` 0개**

§A 번호 블록 (질문: "PRD가 아직 없네요. 어떻게 시작할까요?"):
- `1. show-me-the-prd로 지금 만든다 (추천) — show-me-the-prd 스킬로 위임. PRD 폴더 생성 후 그 경로로 0-A 재진입`
- `2. 수동 작성한 PRD 폴더 경로를 알려준다 — 경로 받아 0-A 재진입`
- `3. PRD 없이 한 줄 목표만 입력하고 진행 — 임시 PRD.md 생성 (한 문장 goal + 자동 추출 1~2 acceptance), light 엄격도 + 마일스톤 1개 강제`
- `4. 취소`

§A 원칙: PRD에서 추론 가능한 건 묻지 않는다(§1). 경로가 인수로 이미 들어왔으면 0-B를 건너뛴다(§2c — 직접 답이 이미 있음).

### Step 1: PRD 분석
**타입**: prompt + Bash

PRD 본문을 읽고 추출:
- acceptance criteria (없으면 사용자에게 경고)
- non-goals
- open questions
- 작업 유형 추정 (한/영 키워드 동시 매칭 — `references/task-type-classifier.md` 참조)

### Step 2: 운영 컨텍스트 확정 (자동)
**타입**: 자동 (인터뷰 없음)

이 판은 Codex CLI(0.139+, `goals` 기능 stable) 전용이다. CLI 분기 인터뷰는 없고 `target_cli = codex`로 자동 고정한다. 결과적으로:
- `goal-command.md`는 4,000자 강제 (objective character 한도).
- objective는 `./PLANS.md`를 가리키는 파일 포인터 패턴을 쓴다.
- RECOVERY.md는 codex `/goal` 기준으로 작성한다. codex `/goal`에서 사람 결정 대기는 "자체 수정을 멈추고 PROGRESS.md/Decision-Log에 보고 후 사용자 결정을 기다린다"로 표현한다 (Step 5 CLI 슬롯 치환 참조).
- Step 10에서 어시스턴트는 슬래시 명령을 자동 발사하지 **않는다** — 사용자가 복사해 실행할 `/goal` 명령 한 줄을 제시한다. (대안: codex `/plan` 모드도 안내.)

### Step 3: 작업 유형 + 검증 방식 + 엄격도
**타입**: §A 번호 블록 (1~2회로 압축)

- 작업 유형 6종: 기능 구현 / 버그 수정 / UI 구현 / 문서 집필 / 마이그레이션 / eval 개선
  - 자동 추정값을 **1번(추천)**에 둔다. 추정 신뢰도가 약하면 6개를 평평하게 나열(`task-type-classifier.md`).
- 자동 검증 방식 (여러 개면 `1,3`처럼): 단위 테스트 / 빌드 / 수동 재현 / 스크린샷 / 섹션 자가 검토 / eval 스코어 / 통합 / 패리티
- 엄격도: `1. 표준(추천) / 2. 엄격 / 3. 가벼움`

§A 원칙: PRD에서 작업 유형이 명백하면(예: 추정 점수 압도적) 굳이 묻지 말고 기본값으로 확인만 한다(§1·§2c).

### Step 4: 마일스톤 추출 + 사용자 확정
**타입**: prompt + §A 번호 블록

PRD acceptance criteria를 그룹화하여 마일스톤 초안 생성. ≤5개 강제. 5개 초과 시 우선순위 상위 5개만 1차로 가져가고 나머지는 메모로 분리.

사용자에게 마일스톤 목록을 §A "예시 프리뷰"(번호 트리)로 먼저 보여주고 확정:

```text
예시 프리뷰
  1. {M1_NAME} — 완료: {M1_COMPLETION}
  2. {M2_NAME} — 완료: {M2_COMPLETION}
  ...

질문: 이 마일스톤으로 진행할까요?
1. 그대로 진행 (추천)
2. 문장으로 직접 수정 요청
```

### Step 5: 6개 파일 슬롯 채움
**타입**: rag + generate

`references/templates.md`의 템플릿(VALIDATION/RECOVERY/PLAN/PROGRESS/goal-command + PLANS.md ExecPlan)을 PRD 내용에 맞춰 슬롯 치환하고, **모든 헤딩·본문을 `output_lang`으로 렌더링**한다(템플릿은 한국어로 표기돼 있으니 §헤딩 맵으로 옮긴다. PLANS.md ExecPlan 표준 섹션명은 영어 그대로 유지). 작업 유형에 따라 강조 항목이 달라진다 — 매핑 표는 `references/task-type-templates.md` 참조.

치환 시 빈 슬롯(`{...}`)이 잔존하지 않도록 확인. 빈 슬롯이 남으면 해당 줄 자체 제거.

CLI 슬롯은 **codex 전용 고정 문구**로 치환한다:
- `{RETRY_LIMIT_ACTIONS}` / `{RETRY_PAUSE_PHRASE}` → "자체 수정을 멈추고 PROGRESS.md(및 PLANS.md의 Decision-Log)에 실패 내역을 기록한 뒤 사용자의 결정을 기다린다." (codex `/goal`은 일시정지 대신 보고-후-대기로 운영한다.)

### Step 6: goal-command.md 4,000자 자동 컴팩트
**타입**: prompt + Bash

`compact-strategy.md`의 5단계를 인라인으로 적용한다. 텍스트 변환은 어시스턴트가 수행, 단계별 길이 측정은 `python3 -c "print(len(open('goal-command.md').read()))"`로 결정론적으로 측정.

우선순위 5단계: 정규화 → 운영 규칙 외부화(본문엔 "RECOVERY.md를 따른다" + "상세는 ./PLANS.md") → 약어 치환 → 마일스톤 요약 → 작업 유형별 군더더기 제거.

**파일 포인터 패턴**: objective는 항상 `./PLANS.md`(및 VALIDATION/RECOVERY/PLAN)를 가리켜 본문 길이를 줄인다. 이것이 4,000자 한도를 지키는 1차 수단이다.

**PROTECTED_CLAUSES**: 정지조건/scope잠금/3회룰/문서참조/PROGRESS업데이트 5종은 절대 삭제 금지. 한·영 OR 정규식 패턴은 `references/compact-strategy.md` 참조.

### Step 7: 자체 검증
**타입**: Bash + Read

LLM 인지에만 의존하지 않는다. Bash 도구로 결정론적 검증한다.

1. **문자수 ≤ 4,000자**: `python3 -c "import sys; print(len(open(sys.argv[1]).read()))" goal-command.md` (UTF-8 char 단위).
2. **PROTECTED_CLAUSES 5종 한·영 OR 정규식 매칭**: `compact-strategy.md` §보호 영역의 5개 정규식을 `grep -P` 또는 Python으로 매칭. 5개 모두 hit 필수.
3. **`/goal ` 시작 검증**: `grep -cE '^/goal ' goal-command.md` 결과가 1 이상.
4. **약어 치환 후 미정의 약어 없음**: 본문에서 `\b[A-Z]+\.md\b` 패턴 추출 후 표준 약어(VALIDATION/RECOVERY/PLAN/PROGRESS/PRD/SDD/PLANS)와 본문 상단 `[약어]` 범례 정의 외에 등장하는지 확인.
5. **acceptance 매핑 누락 없음**: VALIDATION.md의 `## 완료 기준 매핑` 테이블 행 수가 PRD acceptance criterion 수 이상인지 확인.
6. **PLANS.md 필수 섹션 존재**: `grep -cE '^## (Progress|Validation|Decision-Log)' PLANS.md` 결과가 3 (세 섹션 모두 존재).
7. **헤딩 언어 일관성 검사 (`output_lang` 기준)**: 생성 문서 헤딩이 모두 감지 언어여야 한다 — 교차 언어 헤딩 0건. (단 PLANS.md의 `## Progress`/`## Validation`/`## Decision-Log`는 ExecPlan 표준 섹션명이므로 6번에서 의도적으로 허용하며 이 검사에서 제외한다.)
   - `output_lang = ko` → 영어 헤딩 잔존 검사: `grep -nE "^## (Required Checks|Targeted Checks|Manual Verification|Acceptance Criteria Mapping|Not Done If|Core Rule|Failure Loop|Retry Limit|Scope Control|Reorientation Rule|Revert Rule|Goal|Source Documents|Final Completion Criteria|Current Goal|Current Milestone|Completed|Last Validation|Failed Attempts|Current Best State|Next Step|Risks|Handoff Notes|Visual Verification|Milestone)\b"` → 0건.
   - `output_lang = en` → 한국어 헤딩 잔존 검사: `grep -nE "^## (필수 검증|마일스톤별 검증|수동 확인 절차|완료 기준 매핑|완료로 보지 않는 조건|시각 검증|기본 원칙|실패 루프|재시도 한계|scope 잠금|방향 재확인 규칙|되돌리기 규칙|목표|참조 문서|최종 완료 기준|현재 골|현재 마일스톤|마지막 검증 결과|실패 시도|현재 가장 안정적인 상태|다음 단계|리스크|인수인계 메모|마일스톤|완료)"` → 0건.
   - 그 외 언어 → 교차 grep 생략, 필수 섹션 키 존재 검사로 폴백 (VALIDATION 4 + RECOVERY 6 + PLAN 3 + PROGRESS 9 헤딩 개수 충족).
   위반 1건 이상이면 템플릿 언어 렌더링 실패 → 폐기.

하나라도 실패 → `compact-strategy.md` §구조적 오버플로우 보고로 분기. **6종 파일을 저장하지 않는다.**

### Step 8: 사용자 언어 검토 요약 표시 + PROGRESS.md / PLANS.md prepend
**타입**: prompt + Bash

별도 파일을 만들지 않는다. `output_lang` 검토 요약을 **대화창에 직접 출력**하고, 핸드오프 용도로 **PROGRESS.md 상단 + PLANS.md의 Progress 섹션 상단에 4줄 요약을 prepend**한다.

**대화창 출력 형식** (5섹션 + 시작 직전 확인 — 아래 헤딩도 `output_lang`으로 렌더링한다, 한국어는 예시):

```md
# 골 검토 요약 — {PROJECT_NAME}

## 목표 한 문장
{GOAL_ONE_LINER}

## 마일스톤 (≤5)
1. {MILESTONE_1_NAME} — 완료 조건: {M1_COMPLETION}
2. ...

## 필수 검증 명령
- `{VALIDATION_CMD_1}`
- ...

## scope 잠금 / Non-goals
- {NON_GOAL_1}
- ...

## 사람 결정이 남은 항목
- {OPEN_QUESTION_1}
- (없으면 "없음")

## 시작 직전 확인
- goal-command.md: {CHAR_COUNT}자 / 4,000자
- PROTECTED_CLAUSES 5종: 모두 통과
- PLANS.md 섹션(Progress/Validation/Decision-Log): 모두 존재
- 교차 언어 헤딩 잔존: 0건
- 생성된 파일: VALIDATION.md, RECOVERY.md, PLAN.md, PROGRESS.md, goal-command.md, PLANS.md
```

**PROGRESS.md / PLANS.md 상단 prepend (4줄)**:

```md
## 골 검토 요약 (Step 8 자동 생성)

- 목표: {GOAL_ONE_LINER}
- 마일스톤: {M1_NAME} / {M2_NAME} / ...
- 필수 검증: {REQUIRED_CHECK_COMMANDS_ONELINE}
- scope 잠금: {KEY_SCOPE_LOCKS_ONELINE}

---

```

이 요약을 화면 출력 후 Step 9로 넘어간다.

### Step 9: 사람 검토 + 승인 / 수정
**타입**: §A 번호 블록 (필수 게이트)

질문: "위 요약을 검토하셨나요? 어떻게 진행할까요?"

- `1. 승인 — /goal 핸드오프 명령을 받는다 (추천)`: Step 10으로 이동, 복사해서 실행할 `/goal` 명령을 제시한다.
- `2. 수정 필요`: 어느 파일을 어떻게 바꿀지 자유 텍스트 입력 받기. 입력 받은 뒤 해당 파일만 재생성 후 Step 7부터 재검증.
- `3. 나중에 직접 실행`: 핸드오프 명령을 제시하지 않음. `goal-command.md`/`PLANS.md` 위치만 안내하고 종료.
- `4. 취소`: 6종 파일을 그대로 두고 종료.

승인 게이트는 우회 불가. Codex는 슬래시 명령을 자동 발사할 수 없으므로 실제 `/goal` 실행은 항상 사용자가 한다 — 그래도 Step 9 확인은 필수다.

### Step 10: 승인 시 /goal 핸드오프 명령 제시
**타입**: prompt + Bash

승인이 들어오면:

1. **PROGRESS.md + PLANS.md Progress 섹션에 시작 기록** (Bash로 append):
   ```
   ## 골 시작 기록
   - 시작 시각: {ISO_TIMESTAMP}
   - 사용 CLI: codex
   - 컴팩트 후 본문 길이: {CHAR_COUNT}자
   ```

2. **응답 본문은 `output_lang`으로 간단히 정리**:
   - "검토 문서 6종이 준비됐습니다. 아래 `/goal` 명령을 복사해 실행하면 골 작업이 시작됩니다. 진척은 PROGRESS.md / PLANS.md의 Progress 섹션에서 확인하세요." 정도 한두 줄.
   - 생성 파일 6종 경로도 한 줄로 안내.

3. **복사용 `/goal` 명령을 코드블럭으로 제시** (Codex는 자동 발사 불가 → 사용자가 복사해 실행):
   - 파일 포인터 패턴 + verifiable done condition을 포함한다.
   - 형식 예:

   ````md
   아래 명령을 복사해 실행하세요:

   ```
   /goal Execute ./PLANS.md to completion; keep the Progress section current; PRD.md의 모든 acceptance criterion이 만족되고 VALIDATION.md의 필수 검증이 통과될 때까지 멈추지 말고 PLAN.md의 기능을 구현한다. stop when 모든 마일스톤이 끝나고 VALIDATION.md의 모든 검증이 통과될 때.
   ```

   (대안) 한 번에 끝까지 자동 실행 대신 단계별로 보고받고 싶으면 codex `/plan` 모드로 `./PLANS.md`를 따라 진행해도 됩니다.
   ````

   - `<verifiable done condition>` 슬롯은 VALIDATION.md의 필수 검증 + 모든 마일스톤 완료로 채운다 (모호한 "끝낼 때까지" 금지).
   - 명령 본문은 항상 goal-command.md(컴팩트 완료본)와 일치해야 한다 — Step 6/7을 통과한 본문을 그대로 한 줄로 쓴다.

**중요**: Codex 스킬은 마지막 줄로 슬래시 명령을 자동 발사할 수 없다(그건 Claude Code 메커니즘이다). 따라서 이 판은 **복사-실행 핸드오프**로 끝낸다 — 절대 "다음 턴에 자동 시작된다"고 약속하지 말 것.

## Settings (가변 요소)

| 설정 | 기본값 | 변경 방법 |
|------|--------|-----------|
| `task_type` | 자동 추정 | Step 3 §A 번호 블록 |
| `strictness` | `standard` | Step 3 §A 번호 블록 |
| `output_dir` | PRD 디렉토리와 동일 | 호출 시 인수 |
| `overwrite_existing` | `false` (확인 받음) | Step 0 분기 |

## References

- **`references/templates.md`** — 6개 파일 템플릿(5종 + PLANS.md ExecPlan, +§헤딩 맵 ko/en) + F-1~F-6 본문, `output_lang`으로 렌더링
- **`references/task-type-classifier.md`** — 한/영 키워드 기반 작업 유형 추정 규칙
- **`references/task-type-templates.md`** — 작업 유형 6종 × 파일 강조 항목 (`output_lang` additions)
- **`references/compact-strategy.md`** — 4,000자 자동 컴팩트 5단계 + 한·영 OR PROTECTED_CLAUSES 정규식

경로 참조 시 `$PLUGIN_ROOT`를 쓴다 (예: `$PLUGIN_ROOT/skills/goaljaby/references/templates.md`).

## 동작 메커니즘

이 스킬은 별도 Python 스크립트 없이 인라인으로 동작한다.

- **PRD 파싱 (Step 0~1)**: Bash + Grep으로 `.md` 파일 목록·acceptance 패턴·작업 유형 키워드 추출
- **자동 컴팩트 (Step 6)**: 어시스턴트가 `compact-strategy.md`의 5단계를 순서대로 적용 (텍스트 변환)
- **검증 (Step 7)**: Bash `grep -P` + `python3 -c "print(len(...))"`로 PROTECTED_CLAUSES 정규식·문자수·PLANS.md 섹션·교차 언어 헤딩 잔존을 결정론적으로 매칭
- **검토 요약 (Step 8)**: 대화창에 `output_lang` 요약 출력 + PROGRESS.md/PLANS.md 상단에 4줄 요약 prepend
- **골 핸드오프 (Step 10)**: 복사-실행용 `/goal` 명령을 코드블럭으로 제시 (자동 발사 아님)

## 핵심 원칙

- **사용자 언어 검토 우선**: 생성 문서는 `output_lang`(사용자 요청 언어)으로 떨어진다. 사용자가 읽고 검토할 수 있어야 승인에 의미가 있기 때문 — 검토 불가능한 언어로 생성하지 않는다(한국어 사용자=한국어, 영어 사용자=영어).
- **검토 요약은 채팅에만**: 별도 파일을 만들지 않는다. PROGRESS.md/PLANS.md 상단에 4줄 요약을 prepend해 핸드오프 시 컨텍스트만 보존한다.
- **경고로 끝내지 않는다**: 4,000자 초과는 항상 컴팩트로 해결. 못 맞추면 결과물 저장 안 함.
- **PROTECTED_CLAUSES는 불가침**: 5종은 어떤 컴팩트 단계에서도 삭제하지 않는다.
- **Codex 전용 핸드오프**: 슬래시 명령 자동 발사 불가 → 복사-실행 `/goal` 명령으로 끝낸다. objective는 ≤4,000자, `./PLANS.md` 파일 포인터.
- **사람 검토 안전장치 우회 금지**: Step 9 승인 게이트 없이 Step 10이 핸드오프 명령을 제시하지 않는다.
- **§A 상속**: 모든 선택 질문은 `shared/questioning-policy.md §A` 번호 블록으로. 존재하지 않는 카드 UI를 가정하지 말 것.
- **자기 시연 가능**: 이 스킬 자체를 만드는 작업도 골잡이로 가능하다.
