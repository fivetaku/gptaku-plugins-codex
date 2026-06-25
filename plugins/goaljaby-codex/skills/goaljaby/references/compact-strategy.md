# 4,000자 자동 컴팩트 전략

골잡이의 핵심 약속 중 하나: `goal-command.md` 본문은 **항상 4,000자 이하**다. 경고로 끝내지 않는다. 사용자에게 결정을 미루지 않는다. 컴팩트는 스킬이 직접 수행한다.

**언어 정책 (shared/language-policy.md)**: `goal-command.md` 본문은 `output_lang`(사용자 언어) + 영어 식별자. PROTECTED_CLAUSES 정규식은 한국어/영어 둘 다 매칭하는 OR 패턴이라 ko/en 본문은 그대로 검증되고, 그 외 언어는 각 보호절에 ko 또는 en 앵커 표현을 유지해 매칭되게 한다.

**Codex 파일 포인터 패턴**: objective 본문은 `./PLANS.md`(및 VALIDATION/RECOVERY/PLAN)를 가리켜 길이를 줄인다. Codex `/goal`은 한 파일(PLANS.md)만 읽어도 컨텍스트를 잡으므로, 본문에 운영 규칙을 다 적지 않고 "상세는 ./PLANS.md / RECOVERY.md를 따른다"로 외부화하는 것이 4,000자 한도를 지키는 1차 수단이다.

## 보호 영역 (PROTECTED_CLAUSES)

다음 5개 절은 어떤 단계에서도 삭제·축약하지 않는다. 골의 안전성을 보장하는 핵심 절이기 때문이다.

| ID | 절 | 정규식 (한·영 OR 패턴, `grep -P` 기준) |
|----|-----|------|
| P1 | 명시적 정지 조건 | `(통과\|만족\|완료\|도달\|일치\|끝날 때까지\|passes?\|complete\|satisfied)` |
| P2 | scope 잠금 | `(scope\s*확장.{0,20}금지\|Do not.{0,40}(expand\|change).{0,20}scope)` |
| P3 | 3회 실패 규칙 | `(3회\|3 attempts\|three attempts)` |
| P4 | 문서 참조 | `(PRD\|VALIDATION\|RECOVERY\|PLAN\|PLANS)\.md.{0,200}(읽\|Read)\|(읽\|Read).{0,200}(PRD\|VALIDATION\|RECOVERY\|PLAN\|PLANS)\.md` |
| P5 | PROGRESS.md 업데이트 | `(PROGRESS\.md.{0,40}(업데이트\|갱신)\|Progress 섹션.{0,20}(업데이트\|갱신)\|[Uu]pdate (PROGRESS\.md\|the Progress section))` |

컴팩트 직후 5개 모두 정규식 매칭에 성공해야 한다. 하나라도 실패하면 컴팩트 결과를 폐기하고 구조적 오버플로우로 보고한다.

## 5단계 우선순위 (한도 도달 시 즉시 중단)

| 단계 | 작업 | 절감 효과 | 위험 |
|------|------|----------|------|
| 1. 정규화 | 중복 공백, 빈 줄 정리 | 5~10% | 없음 |
| 2. 외부화 | 운영 규칙을 RECOVERY.md/PLANS.md로 옮기고 본문엔 "RECOVERY.md를 따른다 / 상세는 ./PLANS.md"만 남김 | 20~30% | 낮음 (사용자가 PLANS.md를 읽음을 전제) |
| 3. 약어 치환 | `VALIDATION.md → V.md` `RECOVERY.md → R.md` `PLAN.md → P.md` `PROGRESS.md → PR.md` `PLANS.md → PL.md` + 본문 상단에 1줄 범례 | 10~15% | 중간 (가독성 저하) |
| 4. 마일스톤 요약 | 본문에 마일스톤 이름만 두고 상세는 PLAN.md/PLANS.md에 위임 | 15~25% | 낮음 |
| 5. 작업 유형별 군더더기 제거 | 해당 작업 유형에 무관한 표준 문구 삭제 (예: 문서 집필 골에서 빌드 관련 문구) | 5~10% | 낮음 |

### 단계 1: 정규화

```python
text = re.sub(r"[ \t]+", " ", text)           # 다중 공백 → 단일
text = re.sub(r"\n{3,}", "\n\n", text)        # 3+ 줄바꿈 → 2개
text = text.replace("  ", " ").strip()
```

### 단계 2: 외부화 (Externalization)

원본:
```
- 검증이 실패하면 먼저 실패 유형을 진단한다.
- 에러를 침묵 처리하지 않는다. 테스트를 skip 처리하지 않는다.
- 같은 검증이 3회(3 attempts) 실패하면 자체 수정을 멈추고 PROGRESS.md/Decision-Log에 기록한 뒤 사용자 결정을 기다린다.
- PLAN.md에 명시되지 않은 public API 변경은 금지한다.
```

컴팩트 후:
```
- 모든 실패 처리·scope 규칙·3회(3 attempts) 룰은 RECOVERY.md를 따른다. 상세 진행은 ./PLANS.md를 읽는다.
```

PROTECTED_CLAUSES P2·P3·P4는 한 줄 안에 압축되어 정규식 매칭이 유지된다.

### 단계 3: 약어 치환

본문 최상단에 추가:
```
[약어] V.md=VALIDATION.md, R.md=RECOVERY.md, P.md=PLAN.md, PR.md=PROGRESS.md, PL.md=PLANS.md
```

본문 내부:
```
편집 전에 V.md, R.md, P.md, PR.md, PL.md를 읽는다.
```

자체 검증: 본문 어디서도 정의 안 된 약어가 등장하지 않는지 확인.

### 단계 4: 마일스톤 요약

원본:
```
마일스톤 1: Auth refactor — /api/login을 세션에서 JWT로 마이그레이션, 테스트 갱신.
마일스톤 2: 프로필 페이지 — avatar 업로드 포함 새 레이아웃.
마일스톤 3: 설정 — 토글 영속화.
```

컴팩트 후:
```
P.md의 마일스톤을 순서대로 진행한다 (Auth refactor → 프로필 → 설정).
```

상세는 PLAN.md/PLANS.md에 위임. PLANS.md가 운영 단일 진실 원천이 된다.

### 단계 5: 작업 유형별 군더더기 제거

작업 유형이 "문서 집필"인데 본문에 빌드 관련 표준 문구가 있으면 삭제. 작업 유형 분류표는 `task-type-templates.md` 참조.

## 컴팩트 후 자체 검증

```python
import re

PROTECTED_CLAUSES = {
    "P1_stop":       r"(통과|만족|완료|도달|일치|끝날 때까지|passes?|complete|satisfied)",
    "P2_scope":      r"(scope\s*확장.{0,20}금지|Do not.{0,40}(expand|change).{0,20}scope)",
    "P3_3attempts":  r"(3회|3 attempts|three attempts)",
    "P4_read_docs":  r"(PRD|VALIDATION|RECOVERY|PLAN|PLANS)\.md.{0,200}(읽|Read)|(읽|Read).{0,200}(PRD|VALIDATION|RECOVERY|PLAN|PLANS)\.md",
    "P5_progress":   r"(PROGRESS\.md.{0,40}(업데이트|갱신)|Progress 섹션.{0,20}(업데이트|갱신)|[Uu]pdate (PROGRESS\.md|the Progress section))",
}

def verify_compact(text: str) -> list[str]:
    failures = []
    if len(text) > 4000:
        failures.append(f"length: {len(text)} > 4000")
    for pid, regex in PROTECTED_CLAUSES.items():
        if not re.search(regex, text):
            failures.append(f"protected clause missing: {pid}")
    if not text.strip().startswith("/goal "):
        failures.append("must start with '/goal ' followed by a condition")
    # 약어 검증
    abbreviations_used = re.findall(r"\b([A-Z]+)\.md\b", text)
    abbreviations_defined = set()
    if "[약어]" in text:
        legend = text.split("[약어]")[1].split("\n")[0]
        abbreviations_defined = set(re.findall(r"([A-Z]+)\.md=", legend))
    standard = {"VALIDATION", "RECOVERY", "PLAN", "PROGRESS", "PLANS", "PRD", "SDD"}
    for abbr in abbreviations_used:
        if abbr not in standard and abbr not in abbreviations_defined:
            failures.append(f"undefined abbreviation: {abbr}.md")
    return failures
```

`failures`가 비어 있어야 컴팩트 통과. 비어 있지 않으면 결과 폐기 + 구조적 오버플로우 보고.

**시작 검증 메모**: 영어 명령형 동사 시작 강제는 두지 않는다. `/goal ` 다음에 condition이 있는지만 검증한다. Codex `/goal`의 종료 판정도 비영어 condition(한국어 등 `output_lang`)을 처리한다. objective는 `./PLANS.md`를 가리키는 파일 포인터 형태를 권장한다.

> **Codex 핸드오프 주의**: 컴팩트를 통과한 `goal-command.md` 본문은 SKILL.md Step 10에서 **복사-실행용 `/goal` 명령**으로 그대로 제시한다. Codex 스킬은 슬래시 명령을 마지막 줄로 자동 발사할 수 없다(그건 Codex CLI 메커니즘). 따라서 본문은 "사용자가 복사해 붙여넣어 실행할" 한 줄로 완결되어야 한다.

## 구조적 오버플로우 보고 (모든 컴팩트 실패 시)

```text
🔴 골 문장이 4,000자를 자동 컴팩트로도 못 맞춥니다.

현재 길이: {current_length}자 (제한: 4,000자)
컴팩트 시도 단계: 1~5 모두 적용됨

원인 후보:
- 마일스톤이 너무 많음 (현재 {n}개 → 권장 ≤5)
- 작업 유형별 표준 문구가 모두 필수임 (엄격 모드 영향)
- PRD의 acceptance criteria 수가 많아 본문 인용이 길어짐

권장 조치:
1. PLAN.md의 마일스톤을 축소·분할 → goaljaby 재실행
2. 엄격도를 "엄격"에서 "표준"으로 변경
3. PRD 자체를 2개 골로 분할 (Phase 단위)

goal-command.md / PLANS.md는 생성되지 않았습니다. 위 조치 후 다시 호출하세요.
```
