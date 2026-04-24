# PM 프레임워크 레퍼런스

> PM 프리셋 팀원 프롬프트에 주입하는 프레임워크 지식.
> 출처: Teresa Torres, Marty Cagan, Alberto Savoia, Dan Olsen, Ash Maurya 등.

---

## 1. PRD 템플릿 (8-section)

PM 팀이 PRD를 작성할 때 반드시 이 구조를 따른다.

```
### 1. Executive Summary
[2-3문장: 무엇을, 누구를 위해, 왜 지금]

### 2. Background & Context
[문제 공간, 선행 리서치, 시장 맥락, 이 이니셔티브의 배경]

### 3. Objectives & Success Metrics
Goals (성공의 모습):
1. [구체적, 측정 가능한 목표]

Non-Goals (명시적 범위 밖):
1. [안 하는 것, 이유]

Success Metrics:
| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|

### 4. Target Users & Segments
[대상 사용자, 프로필, 세그먼트 크기]

### 5. User Stories & Requirements
P0 (Must Have):
| # | User Story | Acceptance Criteria |
P1 (Should Have):
P2 (Nice to Have / Future):

### 6. Solution Overview
[하이레벨 접근법, 핵심 설계 결정]

### 7. Open Questions
| Question | Owner | Deadline |

### 8. Timeline & Phasing
[마일스톤, 의존성, 페이즈 구분]
```

**핵심 원칙:**
- Non-goals는 goals만큼 중요 — scope creep 방지
- 성공 지표는 구체적: "NPS 개선" (X) → "NPS 32→45, 출시 90일 내" (O)
- 아이디어가 너무 크면 Phase 1만 스펙, 나머지는 Future

---

## 2. Opportunity Solution Tree (Teresa Torres)

디스커버리 작업 시 팀이 따라야 할 구조.

```
Desired Outcome (측정 가능한 목표)
  ├── Opportunity 1 (고객 관점의 문제/니즈)
  │     ├── Solution A
  │     │     └── Experiment (가설, 방법, 성공 기준)
  │     ├── Solution B
  │     └── Solution C
  ├── Opportunity 2
  │     ├── Solution D
  │     └── Solution E
  └── Opportunity 3
```

**4단계:**
1. **Desired Outcome** — 단일 측정 가능 지표 (OKR/전략에서 도출)
2. **Opportunities** — 고객 니즈/고통 (기능 아님). "I struggle to..." / "I wish I could..."
3. **Solutions** — 기회당 최소 3개 이상. 첫 아이디어 함정 회피.
4. **Experiments** — Value/Usability/Viability/Feasibility 리스크별 검증

**Opportunity Score** = Importance x (1 - Satisfaction)

---

## 3. Product Strategy Canvas (9-section)

전략 문서 작성 시 팀이 따라야 할 구조.

```
### 1. Vision — 영감을 주는 북극성 (2-3문장)
### 2. Target Segments — 누구를 위한 것인가 (누구를 위하지 않는지도)
### 3. Pain Points & Value — 해결하는 문제와 전달하는 가치
### 4. Value Propositions — JTBD 기반: When [상황], they want [동기], so they can [결과]
### 5. Strategic Trade-offs — 안 하기로 한 것 (전략의 핵심)
### 6. Key Metrics — North Star + Input Metrics + Health Metrics
### 7. Growth Engine — 획득/활성화/확장 메커니즘
### 8. Core Capabilities — Build / Buy / Partner
### 9. Defensibility — 모방 장벽 (네트워크 효과, 데이터, 브랜드, 전환비용)
```

**핵심 원칙:**
- 좋은 전략은 YES보다 NO가 더 많다 — Trade-offs를 강하게
- Vision은 감정적이고 기억에 남아야 한다 — 기업 성명서 X
- 초기 단계면 일부 섹션이 가설 — "가설"이라고 명시

---

## 4. Discovery Workflow (체이닝 패턴)

디스커버리 요청 시 팀장이 따라야 할 단계별 워크플로우.

```
Step 1: 컨텍스트 파악
  → 기존 제품 vs 신규 제품
  → 사전 리서치/데이터 확인

Step 2: 아이디어 발산 (Diverge)
  → PM/Designer/Engineer 관점에서 브레인스토밍
  → 상위 10개 아이디어 → 사용자에게 3-5개 선택 요청
  [CHECKPOINT: 사용자 확인]

Step 3: 가정 식별 (Critical Thinking)
  → 선택된 아이디어별 리스크 카테고리 분석
  → Value / Usability / Feasibility / Viability
  → 신규 제품이면 + Go-to-Market / Strategy / Team

Step 4: 가정 우선순위 (Focus)
  → Impact x Risk 매트릭스
  → "Leap of faith" 가정 식별
  [CHECKPOINT: 사용자 확인]

Step 5: 실험 설계 (Validate)
  → 핵심 가정당 1-2개 실험
  → 기존 제품: A/B 테스트, fake door, 프로토타입
  → 신규 제품: XYZ 가설, pretotype, 랜딩페이지, concierge MVP
  → 성공 기준 + 타임라인 + 노력도

Step 6: Discovery Plan 문서 산출
```

---

## 5. Assumption Mapping

가설 검증 작업 시 사용하는 프레임워크.

**리스크 카테고리 (기존 제품):**
| 카테고리 | 질문 |
|---------|------|
| Value | 사용자가 이것을 원하는가? |
| Usability | 사용자가 사용법을 이해하는가? |
| Feasibility | 우리가 만들 수 있는가? |
| Viability | 비즈니스 케이스가 성립하는가? |

**리스크 카테고리 (신규 제품 — 추가):**
| 카테고리 | 질문 |
|---------|------|
| Go-to-Market | 사용자에게 도달/전환할 수 있는가? |
| Strategy | 시장 타이밍/포지셔닝이 맞는가? |
| Team | 이것을 실행할 역량이 있는가? |
| Regulatory | 법적/규제 리스크가 있는가? |

**우선순위 매트릭스:**
```
          High Impact
              |
  [TEST FIRST]  |  [MONITOR]
              |
 ─────────────┼──────────────
              |
  [DEPRIORITIZE] | [PARK]
              |
          Low Impact
   High Uncertainty ← → Low Uncertainty
```

---

## 6. 우선순위 프레임워크 요약

| 프레임워크 | 공식 | 적합한 상황 |
|-----------|------|-----------|
| **RICE** | Reach x Impact x Confidence / Effort | 대규모 백로그 (50+) |
| **ICE** | Impact x Confidence x Ease | 빠른 판단, 소규모 팀 |
| **Opportunity Score** | Importance x (1 - Satisfaction) | 고객 니즈 기반 우선순위 |
| **MoSCoW** | Must/Should/Could/Won't | 스코프 협상, 스프린트 계획 |
| **Kano** | Must-be/Performance/Attractive | UX/기능 분류 |
| **Value vs Effort** | Value / Effort 2x2 매트릭스 | 가장 직관적, 빠른 판단 |

---

## 7. North Star Metric

| 구성 요소 | 설명 |
|----------|------|
| **North Star Metric** | 전체 비즈니스 성공을 대표하는 단일 지표 |
| **Input Metrics** | North Star를 움직이는 3-5개 레버 |
| **Health Metrics** | 가드레일 (North Star 추구 시 나빠지면 안 되는 것) |

**비즈니스 유형별 예시:**
| 유형 | North Star 예시 |
|------|----------------|
| Marketplace | 주간 거래 완료 수 |
| SaaS | 주간 활성 팀 수 |
| Consumer | 일간 활성 사용자(DAU) |
| E-commerce | 월간 구매 고객 수 |
| Content | 총 읽기 시간 |

---

## 8. Lean Canvas (간략)

```
| 문제 (Top 3)     | 솔루션           | 고유 가치 제안    | 불공정 우위      | 고객 세그먼트     |
| 기존 대안         |                  | (한 문장)        |                  | 얼리어답터        |
|                   | 핵심 지표         |                  |                  |                   |
|                   | 채널              |                  |                  |                   |
|                   | 비용 구조                            | 수익원                              |
```

---

## 팀원 프롬프트 주입 가이드

PM 프리셋에서 각 역할에 주입할 프레임워크:

| 역할 | 주입할 프레임워크 |
|------|-----------------|
| Lead (팀장) | 전체 워크플로우 + 체크포인트 패턴 + 우선순위 프레임워크 |
| Researcher | Assumption Mapping의 리스크 카테고리 + 경쟁 분석 관점 |
| Strategist | Strategy Canvas + OST + Lean Canvas + North Star |
| Writer | PRD 템플릿 + 문서 작성 원칙 (구체적 지표, Non-goals 강조) |
| Analyst | 우선순위 프레임워크 + 시장 규모 추정 (TAM/SAM/SOM) |
