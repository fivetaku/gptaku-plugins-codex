# 6개 파일 + /goal 명령어 템플릿 (Codex 판)

골잡이 Step 5에서 슬롯 치환에 사용한다. 본진 5종 템플릿의 한국어 적용판 + Codex `PLANS.md` ExecPlan 템플릿(G).

**언어 정책 (shared/language-policy.md §1·§5)**: 아래 템플릿은 **한국어로 표기**돼 있지만, 실제 생성 시 **모든 헤딩·본문을 `output_lang`(사용자 요청 언어)으로 렌더링**한다. 식별자(파일명/명령/`PRD` 같은 약어/`{SLOT}` 토큰)와 PLANS.md ExecPlan 표준 섹션명(`Progress`/`Validation`/`Decision-Log`)은 번역하지 않는다. 헤딩은 아래 **§헤딩 맵**의 canonical 번역을 쓰고, 맵에 없는 언어는 en 열을 기준으로 옮긴다. **한국 제작이라고 한국어를 기본값으로 두지 말 것.**

작업 유형별 강조 항목은 `task-type-templates.md` 참조.

슬롯 표기: `{SLOT_NAME}` — Step 1/3/4에서 추출한 값으로 치환. 비어 있으면 해당 줄 자체 제거 (placeholder 잔존 금지).

## §헤딩 맵 (canonical heading set — Step 7 #7 검증과 1:1)

생성 문서의 `## ` 헤딩은 `output_lang`에 맞춰 아래 표대로 렌더링한다. ko/en은 1급(결정론적 검증), 그 외 언어는 en 열을 번역한다. 슬롯(`{N}`,`{NAME}`)은 유지. PLANS.md의 `## Progress`/`## Validation`/`## Decision-Log`는 ExecPlan 표준 섹션명이므로 번역하지 않는다.

| 파일 | ko | en |
|------|-----|-----|
| VALIDATION | 필수 검증 | Required Checks |
| VALIDATION | 마일스톤별 검증 | Targeted Checks |
| VALIDATION | 수동 확인 절차 | Manual Verification |
| VALIDATION | 완료 기준 매핑 | Acceptance Criteria Mapping |
| VALIDATION | 완료로 보지 않는 조건 | Not Done If |
| VALIDATION | 시각 검증 (UI 작업) | Visual Verification |
| RECOVERY | 기본 원칙 | Core Rule |
| RECOVERY | 실패 루프 | Failure Loop |
| RECOVERY | 재시도 한계 | Retry Limit |
| RECOVERY | scope 잠금 | Scope Control |
| RECOVERY | 방향 재확인 규칙 | Reorientation Rule |
| RECOVERY | 되돌리기 규칙 | Revert Rule |
| PLAN | 목표 | Goal |
| PLAN | 참조 문서 | Source Documents |
| PLAN | 최종 완료 기준 | Final Completion Criteria |
| PLAN | 마일스톤 {N}: {NAME} | Milestone {N}: {NAME} |
| PROGRESS | 현재 골 | Current Goal |
| PROGRESS | 현재 마일스톤 | Current Milestone |
| PROGRESS | 완료 | Completed |
| PROGRESS | 마지막 검증 결과 | Last Validation |
| PROGRESS | 실패 시도 | Failed Attempts |
| PROGRESS | 현재 가장 안정적인 상태 | Current Best State |
| PROGRESS | 다음 단계 | Next Step |
| PROGRESS | 리스크 / 블로커 | Risks / Blockers |
| PROGRESS | 인수인계 메모 | Handoff Notes |

> 본문 단락·체크리스트·표 내용도 `output_lang`으로 번역한다(식별자 제외). F-1~F-6의 `/goal` 본문도 동일하되, PROTECTED_CLAUSES 앵커(정지조건/scope/3회/문서참조/PROGRESS)는 `compact-strategy.md`의 ko·en OR 정규식에 매칭되게 유지한다.

> **Codex CLI 슬롯 고정 문구** — 본진의 Codex CLI 전용 문구를 Codex 전용으로 치환한다:
> - `{RETRY_PAUSE_PHRASE}` → "자체 수정을 멈추고 PROGRESS.md(및 PLANS.md의 Decision-Log)에 실패 내역을 기록한 뒤 사용자의 결정을 기다린다"
> - `{RETRY_LIMIT_ACTIONS}` → "골이 진단·검토 모드로 전환되고 자체 수정을 멈춘다. PROGRESS.md와 PLANS.md의 Decision-Log에 3회 시도 내역을 기록하고 사용자 결정을 기다린다. 필요하면 새 `/goal`로 재설정한다."
> Codex `/goal`은 Codex CLI의 `/goal pause`와 다르므로 "보고 후 대기"로 표현한다.

---

## B. VALIDATION.md

````md
# VALIDATION — {PROJECT_NAME}

## 필수 검증

골 완료로 마크하기 전 다음 명령을 반드시 실행한다.

```bash
{REQUIRED_CHECK_COMMANDS}
```

## 마일스톤별 검증

각 마일스톤 종료 시 실행한다.

```bash
{TARGETED_CHECK_COMMANDS}
```

## 수동 확인 절차

{MANUAL_VERIFICATION_STEPS}

{VISUAL_VERIFICATION_BLOCK_OR_OMIT}

## 완료 기준 매핑

| PRD 완료 기준 | 검증 방식 | 상태 |
| --- | --- | --- |
{ACCEPTANCE_MAPPING_ROWS}

## 완료로 보지 않는 조건

- 필수 검증 중 하나라도 실패
- PLAN.md 밖의 scope로 변경됨
- 명시적 승인 없이 public API가 변경됨
- 수동 재현이 여전히 실패함
- 산출물이 생성됐지만 검토되지 않음
- 검증을 통과시키기 위해 테스트가 삭제·skip됨
- 진단 없이 에러가 침묵 처리됨
{TASK_TYPE_NOT_DONE_IF_ADDITIONS}
````

`{VISUAL_VERIFICATION_BLOCK_OR_OMIT}` 는 UI 작업일 때만 다음 블록을 삽입, 그 외에는 행 자체 제거:

```md
## 시각 검증 (UI 작업)

- [ ] 데스크톱 viewport 확인
- [ ] 모바일 viewport 확인
- [ ] 텍스트 겹침·잘림 없음
- [ ] 스크린샷 저장 위치: {SCREENSHOT_PATH}
```

---

## C. RECOVERY.md

`{RETRY_LIMIT_ACTIONS}` 는 위 Codex 전용 고정 문구로 치환된다.

````md
# RECOVERY

## 기본 원칙

검증이 실패하면 곧바로 광범위한 수정에 들어가지 않는다. 진단부터 한다.

## 실패 루프

검증 단계가 실패하면 다음 순서를 따른다.

1. 실패 출력을 끝까지 읽는다.
2. 실패 유형을 분류한다: 구현 버그 / 잘못된 테스트 / 의존성 누락 / 환경 문제 / 요구사항 불명확 / scope 충돌.
3. PRD.md, PLAN.md, VALIDATION.md와 비교한다.
4. 가장 작은 가역 수정 1회를 한다.
5. 가장 작은 관련 검증부터 재실행한다.
6. PROGRESS.md와 PLANS.md의 Progress 섹션을 업데이트한다.

## 재시도 한계

같은 검증이 서로 다른 3회 시도(3 attempts) 후에도 실패하면:

{RETRY_LIMIT_ACTIONS}

다음을 보고한다:
- 실패한 명령 또는 기준
- 시도한 3가지 수정
- 각각의 실패 이유
- 다음으로 안전한 옵션
- 사용자·제품 결정이 필요한지 여부

## scope 잠금

다음은 금지한다:
- 무관한 모듈을 다시 작성
- PLAN.md에 명시되지 않은 public API 변경
- SDD.md에 명시되지 않은 DB 스키마 변경
- 검증을 통과시키기 위해 테스트를 삭제·skip
- 이해 없이 에러를 침묵 처리
- 좁은 문제를 광범위한 refactor로 해결
- 검증 명령 자체를 다른 명령으로 교체
{TASK_TYPE_SCOPE_ADDITIONS}

## 방향 재확인 규칙

접근법을 바꾸기 전에:

1. 골 문장을 다시 읽는다.
2. PRD.md의 Non-goals를 다시 읽는다.
3. PLAN.md의 현재 마일스톤을 다시 읽는다.
4. 다음 수정이 현재 마일스톤에 직접 기여하는지 확인한다.

## 되돌리기 규칙

자기 자신의 마지막 실패 변경만 되돌린다. 단, 다음 중 하나일 때:
- 변경이 검증을 더 악화시켰을 때
- 무관한 변경을 함께 들여왔을 때
- PRD / PLAN과 충돌할 때

사용자가 수동으로 만든 변경은 명시적 지시 없이 절대 되돌리지 않는다.
````

---

## D. PLAN.md

`{MILESTONES_BLOCK}` 은 마일스톤 1~5개의 반복.

````md
# PLAN — {PROJECT_NAME}

## 목표

{GOAL_ONE_LINER}

## 참조 문서

- PRD.md ({PRD_PATH})
- VALIDATION.md
- RECOVERY.md
- PLANS.md (Codex ExecPlan)

{MILESTONES_BLOCK}

## 최종 완료 기준

- [ ] 모든 마일스톤 완료
- [ ] VALIDATION.md의 모든 검증 통과
- [ ] scope 위반 없음
- [ ] PROGRESS.md / PLANS.md Progress 섹션 업데이트
````

마일스톤 1개 형식:

```md
## 마일스톤 {N}: {MILESTONE_NAME}
- 범위(Scope): {MILESTONE_SCOPE}
- 완료 조건: {MILESTONE_COMPLETION}
- 검증: {MILESTONE_VALIDATION}
```

---

## E. PROGRESS.md (초기 빈 템플릿)

````md
# PROGRESS

## 현재 골

{GOAL_ONE_LINER}

## 현재 마일스톤

마일스톤 1 시작 전

## 완료

(없음)

## 마지막 검증 결과

```text
(골 실행 전)
```

## 실패 시도

| 시도 | 변경 | 결과 | 배운 점 |
| --- | --- | --- | --- |

## 현재 가장 안정적인 상태

골 실행 전 — 초기 상태

## 다음 단계

PLAN.md의 마일스톤 1부터 시작

## 리스크 / 블로커

{OPEN_QUESTIONS_FROM_PRD_OR_NONE}

## 인수인계 메모

이 PROGRESS.md는 골잡이가 생성했다. 골 실행 중 매 체크포인트마다 갱신된다. PLANS.md의 Progress 섹션과 동기화한다.
````

---

## F. goal-command.md (작업 유형별 본문 — 6종)

본문은 `/goal` 다음에 `output_lang`으로 시작하는 명령(아래 F-1~F-6은 한국어 표기 예시 — 생성 시 `output_lang`으로 옮긴다). Step 6 컴팩트 5단계 적용 전 원본은 다음 6개 중 작업 유형에 맞는 것을 사용한다.

`{RETRY_PAUSE_PHRASE}` 는 위 Codex 전용 고정 문구다.

각 본문은 **파일 포인터 패턴**을 쓴다 — 첫 줄에서 `./PLANS.md`를 실행 대상으로 가리킨다. 이것이 Codex 핸드오프의 핵심이며 4,000자 한도를 지키는 1차 수단이다.

> ⚠️ 모든 F 템플릿은 PROTECTED_CLAUSES 5종(P1~P5)을 포함한다. `output_lang`으로 옮긴 뒤에도 5종 정규식(ko·en OR)이 모두 매칭되어야 한다 — `output_lang`이 ko/en이 아니면 각 보호절에 ko 또는 en 앵커 표현을 유지한다 (Step 7 검증, `compact-strategy.md` 참조).

### F-1. 버그 수정

```text
/goal Execute ./PLANS.md to completion. {BUG_NAME} 버그가 더 이상 재현되지 않고 VALIDATION.md의 모든 검증이 통과될 때까지 멈추지 말고 수정한다.

먼저 PRD.md, VALIDATION.md, RECOVERY.md, PLAN.md, PLANS.md를 읽는다.
{SCOPE_MODULES}와 관련 테스트만 수정한다.
PRD.md와 PLAN.md를 벗어나는 scope 확장은 금지한다.
{NO_TOUCH_AREAS}는 변경하지 않는다.
수정 전에 버그를 재현한다.
각 체크포인트마다 PROGRESS.md와 PLANS.md의 Progress 섹션을 업데이트한다.
같은 검증이 3회(3 attempts) 실패하면 {RETRY_PAUSE_PHRASE}.
```

### F-2. 기능 구현

```text
/goal Execute ./PLANS.md to completion. PRD.md의 모든 acceptance criterion이 만족되고 VALIDATION.md의 필수 검증이 통과될 때까지 멈추지 말고 PLAN.md의 기능을 구현한다.

먼저 PRD.md, VALIDATION.md, RECOVERY.md, PLAN.md, PLANS.md를 읽는다.
마일스톤 단위로 작업한다.
PRD.md와 PLAN.md를 벗어나는 scope 확장은 금지한다.
Non-goals 항목이나 선택 기능은 구현하지 않는다.
각 마일스톤이 끝나면 검증을 실행한다.
각 마일스톤이 끝나면 PROGRESS.md와 PLANS.md의 Progress 섹션을 업데이트한다.
요구사항이 충돌하거나 검증이 3회(3 attempts) 실패하면 {RETRY_PAUSE_PHRASE}.
```

### F-3. UI 구현

```text
/goal Execute ./PLANS.md to completion. PLAN.md의 UI가 빌드되고 실행되며 VALIDATION.md의 참조 화면과 모든 viewport에서 일치할 때까지 멈추지 말고 구현한다.

먼저 PRD.md, VALIDATION.md, RECOVERY.md, PLAN.md, PLANS.md를 읽는다.
앱의 기존 디자인 패턴을 사용한다.
PRD.md와 PLAN.md를 벗어나는 scope 확장은 금지한다.
{VIEWPORTS_LIST} 레이아웃을 확인한다.
스크린샷을 증거로 캡처한다.
각 viewport 확인 후 PROGRESS.md와 PLANS.md의 Progress 섹션을 업데이트한다.
시각 출력이 3회(3 attempts) 시도 후에도 일치하지 않으면 {RETRY_PAUSE_PHRASE}.
```

### F-4. 문서 집필

```text
/goal Execute ./PLANS.md to completion. PLAN.md의 모든 섹션이 완료되고 VALIDATION.md의 모든 검토가 통과될 때까지 멈추지 말고 문서를 집필한다.

먼저 PRD.md, VALIDATION.md, RECOVERY.md, PLAN.md, PLANS.md를 읽는다.
한 번에 한 섹션씩 작성한다.
PRD.md와 PLAN.md를 벗어나는 scope 확장은 금지한다.
각 섹션 작성 후 VALIDATION.md 기준으로 자가 검토한다.
섹션이 검토에 실패하면 그 섹션만 다시 쓴다. 부분 패치 금지.
각 섹션 완료 후 PROGRESS.md와 PLANS.md의 Progress 섹션을 업데이트한다.
같은 섹션이 3회(3 attempts) 검토에 실패하면 {RETRY_PAUSE_PHRASE}.
PRD.md를 벗어나는 톤·scope·구조 변경은 금지한다.
```

### F-5. 마이그레이션

```text
/goal Execute ./PLANS.md to completion. {MIGRATION_TARGET}의 새 경로가 VALIDATION.md의 모든 계약 테스트와 패리티 체크를 통과할 때까지 멈추지 말고 마이그레이션한다.

먼저 PRD.md, VALIDATION.md, RECOVERY.md, PLAN.md, PLANS.md{SDD_INCLUDE}를 읽는다.
PLAN.md에서 명시하지 않는 한 legacy 경로를 유지한다.
PRD.md와 PLAN.md를 벗어나는 scope 확장은 금지한다.
승인 없이 public API를 변경하지 않는다.
각 단계마다 패리티 체크를 실행한다.
각 단계 완료 후 PROGRESS.md와 PLANS.md의 Progress 섹션을 업데이트한다.
패리티가 3회(3 attempts) 실패하면 {RETRY_PAUSE_PHRASE}.
```

### F-6. 프롬프트 / eval 개선

```text
/goal Execute ./PLANS.md to completion. PLAN.md의 프롬프트가 VALIDATION.md에서 정의한 eval 목표 점수에 도달하고 모든 검증이 통과될 때까지 멈추지 말고 최적화한다.

먼저 PRD.md, VALIDATION.md, RECOVERY.md, PLAN.md, PLANS.md를 읽는다.
베이스라인 점수를 먼저 기록한다.
PRD.md와 PLAN.md를 벗어나는 scope 확장은 금지한다.
한 번에 한 개의 프롬프트만 변경한다.
변경 후 eval을 실행한다.
각 eval 실행 후 PROGRESS.md와 PLANS.md의 Progress 섹션을 업데이트한다.
같은 eval 목표가 3회(3 attempts) 실패하면 {RETRY_PAUSE_PHRASE}.
```

---

## G. PLANS.md (Codex ExecPlan)

Codex `/goal`이 한 파일만 읽어도 컨텍스트를 잡도록 본진 5종을 한 곳에 모은 운영 진실 원천. 상세는 여전히 개별 파일에 위임한다. **Progress / Validation / Decision-Log** 세 섹션은 필수(Step 7 검증 6번).

````md
# PLANS — {PROJECT_NAME} (Codex ExecPlan)

> /goal Execute ./PLANS.md to completion; keep the Progress section current; stop when {FINAL_DONE_CONDITION}.

## 목표

{GOAL_ONE_LINER}

## 참조 문서

- PRD.md ({PRD_PATH}) / VALIDATION.md / RECOVERY.md / PLAN.md / PROGRESS.md / goal-command.md

## 마일스톤 (≤5)

{MILESTONES_ONELINE_BLOCK}

## Progress

- 현재 마일스톤: 마일스톤 1 시작 전
- 완료: (없음)
- 마지막 검증 결과: (골 실행 전)
- 다음 단계: PLAN.md의 마일스톤 1부터 시작
- (골 실행 중 매 체크포인트마다 이 섹션을 갱신한다.)

## Validation

골 완료로 마크하기 전 다음을 모두 통과해야 한다. 상세 명령·완료 기준 매핑은 VALIDATION.md를 따른다.

- 필수 검증: {REQUIRED_CHECK_COMMANDS_ONELINE}
- 완료로 보지 않는 조건 요약: 필수 검증 실패 / scope 위반 / 미검토 산출물 / 테스트 삭제·skip / 침묵 에러 처리
{TASK_TYPE_VALIDATION_ONELINE}

## Decision-Log

운영 규칙(실패 루프·scope 잠금·3회(3 attempts) 룰·되돌리기)은 RECOVERY.md를 따른다.

- scope 잠금: {KEY_SCOPE_LOCKS_ONELINE}
- 같은 검증이 3회(3 attempts) 실패하면 {RETRY_PAUSE_PHRASE}.
- (의사결정·방향 전환이 생기면 이 섹션에 한 줄씩 append한다.)
````

`{MILESTONES_ONELINE_BLOCK}` 형식 (마일스톤당 한 줄):

```md
1. {M1_NAME} — 완료: {M1_COMPLETION}
2. {M2_NAME} — 완료: {M2_COMPLETION}
```

---

## 슬롯 채움 순서 (Step 5 알고리즘)

1. Step 1 결과에서 `{PROJECT_NAME}`, `{GOAL_ONE_LINER}`, `{ACCEPTANCE_MAPPING_ROWS}`, `{OPEN_QUESTIONS_FROM_PRD_OR_NONE}` 추출
2. Step 2/3/4 인터뷰 결과에서 `{TASK_TYPE}`, 검증 명령 multiSelect, 마일스톤 확정 결과 추출
3. `task-type-templates.md`에서 `{TASK_TYPE}` 행을 읽어 `{TASK_TYPE_NOT_DONE_IF_ADDITIONS}`, `{TASK_TYPE_SCOPE_ADDITIONS}`, `{TASK_TYPE_VALIDATION_ONELINE}`, 사용할 /goal 템플릿(F-1~F-6) 결정
4. CLI 슬롯 (`{RETRY_LIMIT_ACTIONS}`, `{RETRY_PAUSE_PHRASE}`)은 위에 명시된 **Codex 전용 고정 문구**로 치환
5. `{FINAL_DONE_CONDITION}`은 VALIDATION.md의 필수 검증 + 모든 마일스톤 완료로 채운다 (모호한 "끝낼 때까지" 금지)
6. 6개 파일(B~G) 본문 생성. 마지막에 빈 `{...}` 슬롯 잔존 여부 확인 — 있으면 해당 줄 제거 또는 합리적 기본값으로 치환
7. goal-command.md만 Step 6 컴팩트로 전달. PLANS.md는 컴팩트 대상이 아니다(분량 제한 없음).
