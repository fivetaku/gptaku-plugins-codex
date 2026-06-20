# Writing Style 가이드 (Codex)

생성되는 Codex SKILL.md의 품질을 높이기 위한 작성 규칙. Codex 스킬은 에세이가 아니라 **운영 지시서**로 쓴다.

## 1. Imperative Form (명령형)

본문은 **명령형/원형 동사 시작** 지시문으로 작성한다. Second person("You should…") 금지.

올바른 예시:
```
Read the configuration file.
Validate the input before processing.
To accomplish X, do Y.
```
잘못된 예시:
```
You should read the configuration file.
You can use grep to search.
Codex should extract fields...
```

## 2. Description (Frontmatter)

```yaml
---
name: skill-name
description: This skill should be used when the user asks to "trigger1", "trigger2", "trigger3". {무엇을 하는지 + 왜}.
---
```

규칙:
- **Third-person** 필수: "This skill should be used when…".
- **구체적 trigger phrase 3-5개** — 사용자가 실제로 말할 문장.
- 한국어 + 영어 트리거 모두.
- "무엇을 하는지" + "언제 사용하는지" 모두.
- `name`은 소문자 kebab-case. `description`은 1024자 이하(quick_validate가 강제).

좋은 예시:
```yaml
description: This skill should be used when the user asks to "번역해줘", "translate this document", "문서 번역". Translates documents with glossary support and quality review.
```
나쁜 예시:
```yaml
description: Use this skill when translating.   # 인칭 틀림, 모호
description: 번역 스킬입니다.                     # third-person 아님, 트리거 없음
```

## 3. Concise 원칙

### 컨텍스트 윈도우는 공공재
스킬은 시스템 프롬프트·대화 기록·다른 스킬 메타데이터와 컨텍스트를 공유한다. 각 문장이 토큰 비용만큼 가치 있는지 자문한다.

### 기본 가정: Codex는 이미 똑똑하다
이미 아는 정보는 반복하지 않는다. 비자명한 절차적 지식만 포함한다.

### 분량 기준
| 파일 | 목표 |
|------|------|
| SKILL.md 본문 | 핵심만 — Codex가 큰 매뉴얼을 다시 읽지 않고 행동할 수 있을 만큼 짧게 |
| references/ 개별 파일 | 제한 없음 (필요 시만 로드) |
| description | 1-2문장, 1024자 이하 |

### Progressive Disclosure
1. 메타데이터(name + description) — 항상 로드.
2. SKILL.md 본문 — 트리거 시 로드.
3. references / scripts / assets — 필요 시만.

### 분리 기준
SKILL.md에 남길 것: 핵심 워크플로우, 빠른 참조 표, references/scripts/assets 포인터.
references/로 옮길 것: 상세 패턴, 스키마, 엣지 케이스, 긴 예시.

## 4. 파일 구조 규칙

### assets/ 폴더
출력물에 직접 쓰는 파일(템플릿, 이미지, 폰트, 샘플 데이터). 컨텍스트에 로드하지 않는다.

### scripts/ vs references/ vs assets/ 판단
| 질문 | Yes → |
|------|-------|
| 같은 코드를 반복 작성하나? | scripts/ |
| Codex가 참고할 문서인가? | references/ |
| 출력에 직접 쓰는 파일인가? | assets/ |

### 불필요한 파일 금지
- CHANGELOG.md, INSTALLATION_GUIDE.md 등 보조 문서 생성 금지.
- `commands/`·`agents/` 폴더 금지 — Codex에 없는 컴포넌트다.
- 포트 접미사(-port, -codex 등)를 붙인 중복 활성 문서를 만들지 않는다.

## 5. Codex 상호작용 스타일

- 채팅-우선 질문. 안전한 가정이 가능하면 행동 전 최대 1개만 묻는다.
- 선택 질문은 §A 번호형 블록(트레이드오프 한 줄). 존재하지 않는 위젯/카드 도구를 언급하지 않는다.
- 큰 파일 생성 전 구조 프리뷰를 보여준다.
- 사용 불가능한 도구를 가정하지 않는다. 외부 자격증명/서비스가 필요하면 설정·실패 동작을 명시한다(references에만 숨기지 않는다).

## 6. 규율형(Discipline) 스킬의 합리화 차단 장치

> 출처: obra/superpowers `writing-skills`. LLM은 압박받으면 규칙의 루프홀을 찾는다. 규칙을 **말하는 것**과 **지켜지게 만드는 것**은 다르다.

### 6-1. 먼저 판별 — 규율형인가?
| 부류 | 정의 | 예시 | 차단 장치 |
|------|------|------|----------|
| **규율형** | 압박받으면 건너뛰고 싶은 규칙을 강제 | "테스트 먼저", "근본원인 먼저", "완료 전 검증" | **필수 (아래 4종)** |
| **기법형** | 방법·패턴·워크플로우 안내 | 번역, 회의록 정리, 포맷팅 | 불필요 (넣으면 토큰 낭비) |

판별(하나라도 Yes → 규율형): "X 하기 전에 반드시 Y"를 강제하는가? AI가 시간 압박·단순함을 핑계로 건너뛸 유인이 있는가? 건너뛰면 **조용히** 실패하는가? 기법형이면 6-2~6-5를 생략한다.

### 6-2. Iron Law (절대 규칙 한 줄)
규율의 핵심을 한 줄 대문자 규칙으로. SKILL.md 상단(소개 직후)에 배치.
```
**Iron Law: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**
```
형식: `NO {행동} WITHOUT {선행조건} FIRST`. 한국어 병기 가능 — 단 모호어("적절히", "가능하면") 금지.

### 6-3. 합리화 차단표 (Excuse → Reality)
규칙을 건너뛸 변명을 미리 표로 반박한다.
```markdown
| 이런 변명이 떠오르면 | 현실 |
|---------------------|------|
| "이건 너무 간단해서 안 거쳐도 됨" | 간단한 게 사고 난다. 절차는 30초면 끝난다 |
| "급하니까 그냥 넘어가자" | 절차가 추측-수정 반복보다 빠르다 |
| "나중에 한꺼번에 검증하지" | '나중'은 안 온다 |
```

### 6-4. Red Flags 자기점검 리스트
규칙 위반 직전의 생각 신호를 나열한다.
```markdown
## Red Flags — STOP
- "그냥 이번 한 번만..."  - "확인 안 해도 될 것 같은데"  - "거의 다 됐으니 됐다고 하자"
→ 전부 같은 의미다: 규칙을 건너뛰는 중. 멈춰라.
```

### 6-5. Spirit vs Letter (루프홀 봉쇄)
```
**규칙의 문구(letter)를 어기는 것은 규칙의 의도(spirit)를 어기는 것이다.**
```

### 작성 절차
1. 핵심 규칙 1개 → Iron Law. 2. 건너뛸 변명 3-5개 → 합리화 차단표. 3. 위반 직전 신호 3-5개 → Red Flags. 4. Spirit vs Letter 한 줄.

> 주의: 이 4종은 *규율형 스킬에만*. 기법형(번역·포맷팅)에 넣으면 불필요한 압박 + 토큰 낭비. 6-1 판별을 먼저 통과한 경우만 적용한다.

## 7. 검증 체크리스트

**구조:** YAML frontmatter 존재 / name·description 필드 / 참조 파일 실재 / `commands`·`agents` 폴더 없음.
**Description:** third-person / 트리거 3-5개 / 한·영 모두 / 1024자 이하.
**Content:** 명령형 / 핵심만(상세는 references) / `$PLUGIN_ROOT` 경로 / references·scripts·assets 참조 명시.
**규율형일 때만:** Iron Law / 합리화 차단표 / Red Flags / Spirit vs Letter.
