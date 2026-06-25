---
name: insane-research-query
description: Structured research-query builder that turns a vague topic into a research brief and machine-readable query before full insane-research starts. Use when the user wants help framing a research request. Korean triggers — "리서치 쿼리 만들어줘", "쿼리 빌더". English triggers — "research query builder", "structured research query".
---

# Insane Research Query Builder for Codex

> 모호한 리서치 아이디어를 구조화된 실행 가능한 리서치 쿼리로 변환한다.

먼저 읽기:
- `$PLUGIN_ROOT/skills/insane-research-query/references/query_schema.json`

이 스킬은 사용자가 모호한 아이디어를 본격 딥리서치 전에 리서치-레디 브리프로 다듬고 싶을 때 사용한다.

## 질문 원칙 (shared/questioning-policy.md §A·§1·§2c)

Codex CLI에는 `question prompt` 같은 객관식 카드 UI가 **없다**. `shared/questioning-policy.md §A`의 채팅 번호 블록으로 대체한다. 추론 가능한 건 묻지 말고(§1), 요청이 이미 구체적이면 과잉질문 없이 바로 브리프를 생성한다(§2c). 사용자 입력 언어에 맞춰 모든 질문/선택지/산출물 언어를 일치시킨다.

## Codex 워크플로우

### Phase 1: Discovery (주제·타입)

주제가 불명확할 때만 한 번, §A 번호 블록으로 가장 큰 미지수만 묻는다:

```text
어떤 유형의 리서치인가요?
1. Exploratory — 무엇이 존재하는지 탐색, 지형 매핑
2. Comparative — 기술/접근/제품 비교
3. Analytical — 원인·효과·메커니즘 심층 분석
4. Predictive — 미래 트렌드·전망·예측
(번호 또는 문장으로 답해도 됩니다)
```

예시를 보고 싶다는 답이 나오면 다음에서 로드해 제시한다:
`$PLUGIN_ROOT/skills/insane-research-main/examples/`

### Phase 2: Detailed Scoping (범위·소스 품질)

핵심 주제를 잡은 뒤, 정말 모호한 제약만 §A 번호 블록으로 확인한다(추론 가능하면 기본값으로 진행):

```text
지리적 범위는?
1. Global (추천) — 전 세계 관점
2. US/North America — 미국·북미 중심
3. Asia-Pacific — APAC 중심 (한국 포함)
4. Europe — 유럽 시장 중심
(문장으로 직접 지정해도 됩니다)
```

```text
필요한 소스 품질은?
1. B - High quality (추천) — 학술 + 공식 문서 + 검증된 리포트
2. A - Academic only — 피어리뷰 논문·메타분석만
3. C - Moderate — 전문가 의견·사례 연구 포함
4. D - Broad coverage — 프리프린트·전문가 블로그까지 폭넓게
(모르면 1번으로 진행하겠습니다)
```

### Phase 3: Query Generation (쿼리 생성)

모든 입력을 모은 뒤 생성한다:
1. **구조화 JSON 쿼리** — 스키마 준수: `$PLUGIN_ROOT/skills/insane-research-query/references/query_schema.json`
2. **사람이 읽는 리서치 브리프** — 마크다운
3. **실행 체크리스트** — 품질 검증용

#### JSON 쿼리 구조
```json
{
  "task": {
    "title": "[5-15 단어 간결한 제목]",
    "objective": "[명확한 리서치 목표 진술]",
    "type": "exploratory|comparative|analytical|predictive|evaluative"
  },
  "context": {
    "background": "[왜 이 리서치가 중요한가]",
    "audience": "technical|executive|academic|general|policy_maker",
    "use_case": "[리서치가 어떻게 쓰일지]",
    "prior_knowledge": ["가정 1", "가정 2"]
  },
  "questions": {
    "primary": "[메인 리서치 질문]",
    "secondary": ["서브 질문 1", "서브 질문 2", "서브 질문 3"],
    "hypotheses": ["검증 가능한 가정 1"],
    "exclusions": ["범위 밖 주제 1"]
  },
  "constraints": {
    "timeframe": {"start": "2024-01-01", "end": "present", "focus_period": "2025-2026"},
    "geography": {"scope": "global", "regions": [], "exclude_regions": []},
    "sources": {"required_types": ["peer_reviewed", "industry_reports"], "min_quality": "B", "language": ["en"]}
  },
  "output": {
    "format": "comprehensive_report",
    "length": {"min_words": 3000, "max_words": 10000},
    "structure": {"include_executive_summary": true, "include_bibliography": true, "generate_website": false},
    "citation_style": "APA",
    "tone": "professional"
  },
  "keywords": ["keyword1", "keyword2"],
  "special_instructions": []
}
```

#### 사람이 읽는 브리프
```markdown
# Research Brief: [Title]

## Objective
[명확한 진술]

## Research Questions
### Primary Question
> [메인 질문]

### Secondary Questions
1. [서브 질문 1]
2. [서브 질문 2]

## Scope & Constraints
| Dimension | Specification |
|-----------|--------------|
| Timeframe | [기간] |
| Geography | [범위] |
| Min Quality | Grade [X] |

## Execution Checklist
- [ ] Primary question fully answered
- [ ] All secondary questions addressed
- [ ] Sources meet quality threshold
- [ ] Citations properly formatted
```

### Phase 4: Confirmation and Handoff

브리프를 보여준 뒤 §A 번호 블록으로 다음 행동을 확인한다:

```text
쿼리가 괜찮으면 바로 리서치를 시작할까요?
1. 지금 리서치 시작 (추천) — 이 쿼리로 즉시 딥리서치 실행
2. 쿼리만 저장 — JSON 쿼리를 파일로 저장해 두기
3. 쿼리 수정 — 일부 파라미터를 바꾼 뒤 진행
(번호 또는 문장으로 답해도 됩니다)
```

- **1 지금 시작** → JSON 쿼리를 `insane-research-main` 스킬에 넘긴다
- **2 저장만** → JSON을 파일로 작성 (`RESEARCH/queries/{topic}_{timestamp}.json`)
- **3 수정** → 조정 사항을 모아 루프백

---

## 품질 검증 규칙

쿼리 확정 전 검증:

### Task
- [ ] 제목이 구체적 (generic한 "AI Research" 금지)
- [ ] 목표가 측정/검증 가능
- [ ] type이 리서치 접근과 일치

### Questions
- [ ] primary가 답변 가능 (너무 광범위하지 않음)
- [ ] secondary가 primary를 지지 (탈선 아님)
- [ ] exclusions가 scope creep 방지

### Constraints
- [ ] timeframe이 주제에 현실적
- [ ] geography가 주제 관련성과 일치
- [ ] 소스 요건이 달성 가능

### Output
- [ ] 길이가 요청 깊이와 일치
- [ ] 포맷이 독자에 적합

---

## 안티패턴

### 생성 금지
- 과도하게 광범위한 질문 ("What is AI?")
- 무한 timeframe ("all history")
- 충돌하는 제약 / generic 키워드 ("technology", "innovation")
- 측정 불가 목표 ("understand everything about...")

### 생성 권장
- 구체적·답변 가능한 질문 ("미국 병원의 AI 진단도구 현재 도입률은?")
- 현실적 범위 경계 (빠른 분야는 2~3년 timeframe)
- 구체적 성공 기준 ("시장 점유율 상위 10개 도구 식별")
- 실행 가능한 검색어 ("AI radiology FDA approved 2024 2025 adoption rate")
- 명확한 exclusions ("소비자 헬스 앱·행정 AI 제외")

---

## 언어 적응

모든 질문/선택지/산출물은 사용자 감지 언어에 맞춘다.

### 한국어 입력 처리
사용자가 한국어로 입력하면 (예: "헬스케어 AI 리서치 쿼리 만들어줘"):
- 모든 질문 한국어
- geography 옵션에 한국 관련 선택지
- source 옵션에 한국 리서치 DB
- 산출물에 한국어 인용 관례

### 다국어 키워드
최대 커버리지를 위해 사용자 언어와 영어 양쪽으로 검색 키워드 생성:
```
한국어 입력: "AI 의료 진단"
생성: ["AI 의료 진단 2026", "AI medical diagnostics 2026", "의료 AI 도입 현황", "clinical AI adoption"]
```

---

## insane-research 연동

생성된 쿼리는 `insane-research-main` 스킬로 직접 들어간다:
1. 쿼리 빌더가 구조화 JSON 출력
2. 사용자가 confirm 또는 조정
3. "지금 시작" 선택 시 JSON을 `insane-research-main`에 전달
4. 요건이 이미 정의됐으므로 Phase 1(Question Scoping) 건너뜀
5. 리서치는 Phase 2(Retrieval Planning)부터 시작

쿼리 저장 위치: `RESEARCH/queries/{topic}_{timestamp}.json`

## Guardrails

- 질문은 §A 번호 블록으로 compact하게, 추론 가능한 건 묻지 않는다.
- 빈칸으로 두지 말고 구체적 기본값을 채운다.
- query schema를 구조화 출력의 계약으로 취급한다.
- 위젯형 프롬프트에 의존하지 말고 채팅으로 묻는다.

---

## References
- Query schema: `$PLUGIN_ROOT/skills/insane-research-query/references/query_schema.json`
- Example queries: `$PLUGIN_ROOT/skills/insane-research-main/examples/`
