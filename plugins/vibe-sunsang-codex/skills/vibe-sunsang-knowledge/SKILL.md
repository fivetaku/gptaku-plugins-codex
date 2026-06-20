---
name: vibe-sunsang-knowledge
description: Answer questions about the vibe-sunsang level system (v2 6-axis × 7 levels), anti-patterns, workspace types, six growth axes, prompt quality, and mentoring frameworks. Use when the user asks "바선생 안티패턴이 뭐야?", "바선생 레벨 시스템 설명해줘", "6축이 뭐야?", "바선생 성장 지표", "요청 품질", or "workspace types".
---

# vibe-sunsang-knowledge for Codex

> 바선생의 핵심 개념, 용어, 프레임워크에 대한 질문에 답한다. 설명 전용 스킬.

Codex는 skill-first다 (`commands/` 없음). 객관식은 Codex CLI에 카드 UI가 없으므로 `shared/questioning-policy.md §A` 번호 블록으로 채팅에서 묻는다.

## 참조 경로

- 지식 베이스: `$PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/`
- 유형 설정: `~/vibe-sunsang/config/workspace_types.json`

### 공통 (모든 워크스페이스 유형)
- 요청 품질 가이드: `references/common/prompt-quality.md`
- 멘토링 체크리스트: `references/common/mentoring-checklist.md`
- 회고 프레임워크: `references/common/retrospective-frameworks.md`

### 유형별 (Builder / Explorer / Designer / Operator)
- 안티패턴: `references/{type}/antipatterns.md`
- 핵심 개념: `references/{type}/concepts.md`
- 성장 지표 & 레벨: `references/{type}/growth-metrics.md`

## 워크스페이스 유형

| 유형 | 워크스페이스 목적 | 분석 기준 | 레벨 시스템 |
|------|-------------------|-----------|-------------|
| **Builder** | 코딩/개발 (바이브코딩 포함) | 에러 대응, 코드 이해도, 요청 품질 | Observer → Forgemaster |
| **Explorer** | 리서치/Q&A/학습 | 질문 깊이, 출처 검증, 비판적 사고 | Asker → Scholar |
| **Designer** | 기획/아이디에이션/콘텐츠 | 기획 구체성, 구조화, 실현 가능성 | Dreamer → Visionary |
| **Operator** | 업무 자동화/데이터 처리 | 에러 처리, 재사용성, 문서화 | User → Automator |

## 실행 흐름

### Step 0: 워크스페이스 유형 확인

유형별 질문인 경우 사용자의 워크스페이스 유형을 먼저 확인한다:
1. `~/vibe-sunsang/config/workspace_types.json`을 읽어 확인.
2. 파일이 없거나 유형 정보가 없으면 `shared/questioning-policy.md §A` 번호 블록:

```text
질문: 어떤 유형의 워크스페이스에 대해 알고 싶으신가요?
1. Builder (코딩) — 코딩/개발 프로젝트
2. Explorer (리서치/학습) — 리서치/Q&A/스터디
3. Designer (기획) — 기획/아이디에이션
4. Operator (자동화) — 업무 자동화/데이터처리
(모르면 가장 일반적인 1번 Builder로 설명하겠습니다)
```

공통 주제(요청 품질, 멘토링, 회고)는 유형 확인 없이 바로 진행한다.

### Step 1: 개념 선택

질문에서 관련 주제를 파악한다. 모호하면 `shared/questioning-policy.md §A` 번호 블록:

```text
질문: 어떤 개념에 대해 알고 싶으신가요?
1. 안티패턴 — AI 활용 시 피해야 할 나쁜 습관들
2. 레벨 시스템 — v2: 7단계(0.5 단위) 성장 레벨과 각 단계 특징
3. 6축 기술 차원 — DECOMP/VERIFY/ORCH/FAIL/CTX/META 6가지 평가 축
4. 워크스페이스 유형 — Builder/Explorer/Designer/Operator 설명
5. 요청 품질 — AI에게 좋은 요청을 하는 방법
6. 성장 지표 — 유형별 성장 측정 기준과 Fit Score
7. 멘토링 방법 — 효과적인 AI 활용 멘토링/코칭 방법
(여러 개면 1,3처럼 적어주세요)
```

### Step 2: 지식 베이스 로딩

주제별 참조 매핑 (base: `$PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/`):

| 질문 유형 | 참조 파일 |
|-----------|----------|
| 안티패턴, 나쁜 습관 | `{type}/antipatterns.md` |
| 레벨 시스템, 성장 단계 | `{type}/growth-metrics.md` |
| 6축 기술 차원, DECOMP/VERIFY 등 | `{type}/growth-metrics.md` + 아래 내장 설명 |
| 개념, 용어 설명 | `{type}/concepts.md` |
| 요청 잘 하는 법, 프롬프트 | `common/prompt-quality.md` |
| 멘토링, 코칭 방법 | `common/mentoring-checklist.md` |
| 회고, 리뷰 방법 | `common/retrospective-frameworks.md` |

### Step 2-1: 6축 기술 차원 내장 설명

"6축"이나 기술 차원 질문이면 다음을 기반으로 설명한다:

| 코드 | 기술 차원 | 한 줄 정의 |
|------|----------|-----------|
| **DECOMP** | 작업 분해 | 복잡한 요청을 AI가 처리 가능한 단위로 나누는 능력 |
| **VERIFY** | 검증 전략 | AI 출력물을 비판적으로 검토하고 품질을 확인하는 능력 |
| **ORCH** | 오케스트레이션 | 도구, 에이전트, 워크플로우를 조합하여 활용하는 능력 |
| **FAIL** | 실패 대응 | 오류, 한계, 예상치 못한 결과에 대처하는 능력 |
| **CTX** | 맥락 관리 | AI에게 적절한 배경 정보, 제약 조건, 목표를 제공하는 능력 |
| **META** | 메타인지 | 자신의 AI 활용 패턴을 인식하고 전략적으로 조정하는 능력 |

**유형별 가중치** (각 유형마다 중요한 축이 다름):
- Builder: DECOMP(25%) + VERIFY(25%) = 50% (만드는 사람은 분해와 검증이 핵심)
- Explorer: FAIL(20%) + CTX(20%) + META(20%) = 60% (조사하는 사람은 비판적 사고가 핵심)
- Designer: CTX(25%) + META(20%) = 45% (기획하는 사람은 맥락과 전략이 핵심)
- Operator: ORCH(25%) + FAIL(20%) = 45% (운영하는 사람은 도구 조합이 핵심)

**Fit Score**: 6축 점수에 유형별 가중치를 곱해 합산한 종합 점수.
**게이트 조건**: 특정 레벨 진입 시 반드시 충족해야 하는 필수 조건 (L3 구체성>0.5, L4 검증>0.15, L5 도구>8, L6 멀티에이전트, L7 외부기여).
**0.5 단위**: 내부는 소수점 2자리(예: 3.72), 공식 발표는 0.5 단위(예: 3.5).

### Step 2-2: 레벨명 테이블 (7단계, 0.5 단위)

| 레벨 | Builder | Explorer | Designer | Operator | 서사 단계 |
|------|---------|----------|----------|----------|----------|
| L1 | Observer (관찰자) | Asker (질문자) | Dreamer (꿈꾸는 사람) | User (사용자) | 수동 |
| L2 | Tinkerer (만지작거리는 사람) | Curious (호기심 많은 사람) | Sketcher (스케치하는 사람) | Repeater (반복자) | 수동→능동 |
| L3 | Collaborator (협력자) | Digger (파헤치는 사람) | Shaper (다듬는 사람) | Optimizer (최적화자) | 능동 |
| L4 | Pilot (조종사) | Investigator (탐구자) | Planner (설계자) | Builder (구축자) | 능동→주도 |
| L5 | Architect (설계자) | Analyst (분석가) | Strategist (전략가) | Engineer (엔지니어) | 주도 |
| L6 | Conductor (지휘자) | Synthesizer (통합자) | Director (감독) | Orchestrator (오케스트레이터) | 주도→창조 |
| L7 | Forgemaster (대장장이) | Scholar (학자) | Visionary (비전가) | Automator (자동화 마스터) | 창조 |

레벨은 "할 수 있는가"가 아닌 **"일관되게 하는가"**를 기준으로 삼는다 (3회 일관성 원칙).

### Step 3: 설명

읽은 reference 파일을 기반으로 설명한다:
1. 핵심 개념을 **한 문장**으로 요약.
2. 비유나 일상 예시로 쉽게 풀어 설명.
3. 관련된 다른 개념이 있으면 연결 (예: "6축을 이해했으니, 유형별 가중치도 궁금하시면 알려드릴게요").

## 대화 스타일

- 전문 용어에는 항상 **쉬운 설명**을 함께 제공.
- 비유와 일상 예시 적극 활용.
- 한국어로 응답 (기술 용어는 영어 병기 가능).
- 한 번에 너무 많은 정보를 주지 않고 핵심만 전달한 뒤 추가 질문을 유도.

## Guardrails

- 묻지 않은 전체 프레임워크를 한꺼번에 쏟아붓지 않는다.
- 예시는 AI 협업 행동에 근거를 둔다.
- 워크스페이스 유형이 불확실하면 가정을 밝힌다.
- Codex CLI에는 `AskUserQuestion` 카드 UI가 없다 → `shared/questioning-policy.md §A` 번호 블록을 쓴다.
