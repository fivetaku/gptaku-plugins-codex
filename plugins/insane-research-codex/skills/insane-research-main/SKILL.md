---
name: insane-research-main
description: Comprehensive, citation-heavy research workflow with session state, structured outputs, and source-quality checks. Use when the user wants deep research, a long-form report, or citation-backed analysis on a topic. Korean triggers — "리서치해줘", "딥리서치", "심층 연구", "[주제]에 대해 리서치해줘". English triggers — "deep research on", "research report".
---

# Insane Research for Codex

> 멀티페이즈 리서치 시스템 — 세션 상태 관리, 소스 검증, 구조화된 산출물. AI가 자율적으로 다단계 리서치를 수행하고 출처를 검증한다.

먼저 읽기:
- `$PLUGIN_ROOT/skills/insane-research-main/references/phase_contracts.md`
- `$PLUGIN_ROOT/skills/insane-research-main/references/citation_rules.md`
- `$PLUGIN_ROOT/skills/insane-research-main/references/quality_rubric.md`

필요할 때 읽기:
- `$PLUGIN_ROOT/skills/insane-research-main/references/query_generator.md`
- `$PLUGIN_ROOT/skills/insane-research-main/references/tool_strategy.md`
- `$PLUGIN_ROOT/skills/insane-research-main/references/agent_prompts.md`
- `$PLUGIN_ROOT/skills/insane-research-main/references/query_schema.json`
- `$PLUGIN_ROOT/skills/insane-research-main/examples/*.json`

## 트리거되면 즉시 실행

이 문서를 출력만 하지 말고, **리서치 플로우를 즉시 실행**한다. 사용자 입력에서 주제를 추출하고 아래 모드 판별로 들어간다.

## 모드 판별 (인자 파싱)

사용자 입력으로 동작을 결정한다:

| 입력 패턴 | 동작 |
|--|--|
| `resume [session_id]` | 이전 리서치 세션 재개 |
| `status` | 모든 리서치 세션과 진행도 나열 |
| `query` | 인터랙티브 쿼리 빌더 → `insane-research-query` 스킬로 위임 |
| `[그 외 텍스트]` | 주어진 주제로 새 리서치 시작 |
| (인자 없음) | 아래 §A 번호형 메뉴 출력 후 답변 대기 |

### 인자가 없을 때 — §A 번호형 메뉴

Codex CLI에는 `question prompt` 같은 객관식 카드 UI가 **없다**. `shared/questioning-policy.md §A`의 채팅 번호 블록으로 대체한다. 다음을 채팅에 출력하고 사용자 답변을 기다린다:

```text
무엇을 할까요?
1. 새 리서치 — 임의 주제로 딥리서치 시작 (주제 → 범위 → 멀티검색 → 종합 → 리포트, 10~30분)
2. 세션 재개 — 중단된 리서치를 마지막 체크포인트부터 이어서 (RESEARCH/*/state.json)
3. 세션 현황 — 모든 세션의 현재 페이즈/소스 수/갱신 시각 나열
4. 쿼리 빌더 — 모호한 주제를 구조화된 리서치 쿼리로 다듬기
(번호 또는 "X 주제로 새 리서치"처럼 문장으로 답해도 됩니다)
```

답변 후:
- **1 새 리서치** → 주제를 확인한 뒤 아래 7-페이즈 플로우 실행
- **2 세션 재개** → `RESEARCH/*/state.json` 목록 제시 → 선택 → 재개 프로토콜
- **3 세션 현황** → 모든 세션 진행 요약 출력
- **4 쿼리 빌더** → `insane-research-query` 스킬로 위임

## 질문 원칙 (shared/questioning-policy.md §A·§1·§2c)

리서치 전 범위 좁히기는 **추론 가능한 건 묻지 않는다(§1)**. 물어야 하면 기본값을 제시하고 확인받는다("종합 리포트로 가정할게요 — 아니면 말씀 주세요"). **요청이 이미 구체적이면 과잉질문 없이 바로 진행한다(§2c)**; 정말 underspecified일 때만 범위를 좁힌다.

언어 감지: 사용자 입력 언어에 맞춰 모든 질문/선택지/산출물 언어를 일치시킨다(한국어 입력 → 한국어).

범위가 진짜 모호하면 §A 번호 블록으로 한 번만, 가장 큰 미지수만 묻는다. 예:

```text
이 리서치의 초점은 무엇이 가장 가까운가요?
1. 모두 포함 (추천) — 현재 상태/기술/시장을 종합 분석
2. 현재 상태와 트렌드 — 최신 동향, 시장 현황, 주요 플레이어
3. 기술 심층 분석 — 아키텍처, 구현, 기술 스택
4. 문장으로 직접 지정
(여러 개면 1,3처럼 적어주세요 / 모르면 1번으로 진행하겠습니다)
```

산출물 형태(종합 리포트 / 요약 / 모듈형)·독자(기술팀 / 경영진 / 연구자 / 일반)·소스 선호(학술 / 산업 리포트 / 뉴스 / 전체)도 정말 모호할 때만 같은 번호 블록으로 확인한다. 이미 추론 가능하면 묻지 말고 기본값(종합 리포트 / 전체 소스)으로 진행한다.

---

## 7-페이즈 딥리서치 프로세스

### Phase 1: Question Scoping (범위 설정)
- 리서치 질문을 명확히 한다 (위 §1·§2c 원칙)
- 산출 형식과 성공 기준 정의
- 제약과 톤 식별
- 파라미터가 분명한 모호하지 않은 쿼리 생성

### Phase 2: Retrieval Planning (검색 계획)
- 메인 질문을 3~5개 서브토픽으로 분해
- 서브토픽별 구체적 검색 쿼리 생성
- 적합한 데이터 소스 선택
- 리서치 플랜을 사용자 승인용으로 정리

---

## DATE-AWARE 쿼리 생성 (필수)

**모든 검색 쿼리는 freshness를 위해 현재 날짜 맥락을 포함한다.**

검색 쿼리를 만들기 전에 시스템 컨텍스트에서 오늘 날짜를 먼저 확인한다.

1. **쿼리에 연도 추가:**
   - 나쁨: "AI code assistants market"
   - 좋음: "AI code assistants market 2026"
   - 좋음: "AI code assistants trends 2026"
2. **recency 연산자 사용:** "after:2025", "since:2025", "2025..2026"
3. **freshness 키워드:** "latest", "recent", "current", "new", "[현재연도] update"
4. **변환 예시:**
   | 사용자 쿼리 | 생성된 검색 쿼리 |
   |--|--|
   | AI 코딩 어시스턴트 | AI 코딩 어시스턴트 2026 최신 동향 |
   | startup trends | startup trends 2026 latest |
   | React vs Vue | React vs Vue 2026 comparison |
5. **학술/역사 리서치:** "state of" 쿼리에도 현재 연도 포함, 날짜 범위 사용 ("climate change research 2020-2026")

쿼리 템플릿: `[topic] [현재연도] [freshness_keyword] [specific_aspect]`

---

### Phase 3: Iterative Querying (반복 검색)
- 검색을 체계적으로 실행 (아래 Rate-Limit & Reliability Guard 준수)
- 관련 정보 추출·발췌
  - WebFetch/브라우징 실패 시 → `tool_strategy.md`의 플랫폼별 접근 전략 또는 Fallback 순서대로 시도
  - 우회 성공 시 소스 신뢰도에 `via_fallback` 태그 추가
  - 실패한 URL과 우회 시도 결과를 `sources/failed_urls.txt`에 기록
- 발견에 따라 새 쿼리 도출, 다중 검색 모달리티(웹·학술·코드) 활용

### Phase 4: Source Triangulation (출처 교차검증)
- 여러 소스에 걸쳐 발견 비교
- 핵심 주장은 최소 2개 소스로 교차 검증
- 불일치 처리·모순 기록
- A~E 등급으로 소스 신뢰도 평가

#### ⚠️ 핵심 주장 검증 레이어 (Claim Verification Layer) — 필수 산출 계약

핵심 주장(수치·점유율·날짜·법령·인과 등 "틀리면 손해 큰" 주장)은 매끄러운 문장으로 단정하기 전에 **claim ledger**를 만든다. ledger는 **반드시 `artifacts/claim_ledger.jsonl`에 한 줄당 1개 레코드(JSONL)**로 저장한다 — 이 파일이 Phase 6의 `validate_ledger.py` 게이트 입력이다. 각 핵심 주장 1건당 레코드:

```json
{
  "claim_id": "clm_001",
  "text": "주장 텍스트",
  "risk": "high | normal",
  "claim_type": "numeric | legal | causal | descriptive",
  "source_ids": ["src_001", "src_003"],
  "counter_search": "반증 검색 1회 결과 요약 (high-risk 필수)",
  "counter_refuted": false,
  "conflicting": false,
  "primary_source": true
}
```

> **`status`/`confidence`는 직접 쓰지 않는다.** `validate_ledger.py`가 source_ids를 레지스트리(`sources/sources.jsonl`)와 대조해 독립 도메인 수·counter_search 유무·1차소스·등급을 보고 **status를 계산**한다. `risk:"high"`는 수치/점유율/날짜/법령/인과/재무 주장에 부여한다. `source_ids`는 `sources/sources.jsonl`의 `id`와 정확히 일치해야 한다(불일치 시 게이트가 하드 에러).

**Abstention 강제 규칙 (불가침)** — 다음 중 하나라도 해당하면 게이트가 `status=unresolved`("미확정")로 계산하고, 해당 주장은 **본문에서 단정 금지**. "미확정 / 확인 필요"로 표기하고 `Unresolved` 섹션에 모은다:
- 독립 출처(도메인) 2개 미만
- 출처 간 충돌이 해소되지 않음 (`conflicting=true`)
- 1차 소스 미도달 (high-risk인데 `primary_source=false`)
- high-risk인데 B등급 이상 출처 없음

**경량 red-team (필수)** — 각 high-risk 주장마다 **반증 counter-search 1회**를 수행하고 `counter_search`에 요약을 기록한다(비어 있으면 게이트가 프로세스 위반으로 exit 1). 신뢰할 만한 반박이 나오면 `counter_refuted=true`로 두면 게이트가 `status=refuted`로 계산해 `Refuted` 섹션으로 보낸다(본문 단정 금지).

**1차 소스 우선** — 정부/법령 DB(law.go.kr·moleg), 공시(SEC/IR), 피어리뷰를 2차 애그리게이터·블로그보다 **먼저** 시도하고, `quality_rubric.md` 기준으로 등급을 매겨 `primary_source` 충족 여부를 ledger에 기록한다.

→ 이 레이어는 **핵심 주장에만** 적용한다. 본문의 폭넓은 서사·맥락·가독성은 유지하되, 핵심 수치/주장만 ledger 게이트를 통과시킨다.

### Phase 5: Knowledge Synthesis (지식 종합)
- 내용을 논리적으로 구조화
- 종합 섹션 작성
- 모든 주장에 인라인 인용 포함
- 관련 시 데이터 시각화 추가

#### ⚠️ Verified-only 합성 게이트 (불가침 — 데이터 흐름 락)

**Phase 5에 들어가기 전에 `validate_ledger.py`를 돌려 `outputs/verified_claims.json`을 먼저 생성해야 한다**(아래 Phase 6 "검증 레이어 마감"의 명령). 그 다음:

- **핵심 주장(수치·법령·인과·재무 등 high-risk)은 오직 `outputs/verified_claims.json`에 있는 항목만 본문에 단정형으로 쓴다.** raw 검색 결과(`sources.jsonl`·검색 findings)를 직접 보고 핵심 수치를 단정하지 않는다.
- `outputs/unresolved_claims.json`·`outputs/refuted_claims.json`의 주장은 **본문 단정 금지** — `Unresolved`/`Refuted` annex 섹션에만 노출한다.
- 폭넓은 서사·맥락·가독성 문장은 그대로 자유롭게 쓰되, **검증 게이트는 핵심 주장에만** 적용한다.

> 이유: 체커만이 `verified_claims.json`을 생산한다. 체커를 건너뛰면 합성할 입력이 비어 자기파괴적이므로, 검증을 우회할 수 없다(순수 프롬프트 권고가 아니라 데이터 의존성으로 강제).

### Phase 6: Quality Assurance (품질 보증)
- 환각·오류 점검
- 모든 인용이 내용과 일치하는지 검증
- 완전성·명료성 확보
- Chain-of-Verification 적용

#### 핵심 주장 검증 레이어 마감 (필수 — 결정론적 게이트)

**검증은 "권고"가 아니라 코드 게이트다.** `artifacts/claim_ledger.jsonl`과 `sources/sources.jsonl`이 준비되면 반드시 아래를 실행한다(Phase 5 합성 전에 1차 실행해 `verified_claims.json`을 만들고, Phase 7 직전에 재실행해 통과를 확정):

```bash
python3 "$PLUGIN_ROOT/skills/insane-research-main/scripts/validate_ledger.py" --session "RESEARCH/{topic}_{timestamp}"
```

종료 코드에 따라:
- **exit 2 (하드 에러)** — 스키마 깨짐·미등록 source id·A-E 등급 모순. 데이터를 고치고 재실행. **절대 Phase 7로 진행 금지.**
- **exit 1 (프로세스 위반)** — high-risk 주장에 `counter_search` 누락. 해당 주장에 반증 검색 1회를 수행해 ledger를 갱신하고 재실행.
- **exit 0 (통과)** — `outputs/{verified,unresolved,refuted}_claims.json` 생성, `state.json.verification.signature` 기록 완료. 이제 Phase 7 진행 가능.

마감 점검:
- **`state.json`에 `verification.signature`가 있고 `verification.passed=true`인지** 확인한다(없으면 게이트 미실행 = 미완).
- 보고서에 `Confidence` / `Refuted` / `Unresolved` 3개 섹션을 노출한다.
- `unresolved`/`refuted` 주장이 본문에 단정형으로 섞이지 않았는지 최종 점검한다(verified-only 합성 게이트 위반 여부).

#### Strict 모드 (옵트인 — 고위험 주장 재검증)

기본 모드는 빠르고 넓게 — 핵심 주장 ledger + 결정론적 게이트로 충분하다. 그러나 **틀리면 손해가 큰 주제(법률·의료·재무·규제·핵심 수치)** 이거나 사용자가 `strict`를 명시하면, ledger의 `unresolved` 또는 high-risk 주장만 골라 **적대적 재검증**한다:
1. Phase 4 ledger에서 게이트가 `unresolved`로 계산했거나 high-risk(강한 수치·법령·인과)인 주장을 추린다.
2. 각 주장을 검증 가능한 질문으로 바꿔 독립 검색으로 confirm/refute한다 (가능하면 1차 소스로). Codex에는 별도 Workflow 하네스가 없으므로 메인 스레드에서 추가 검색을 직접 수행한다.
3. 결과를 ledger에 머지(`source_ids`·`counter_search`·`counter_refuted`·`primary_source` 갱신)한 뒤 **`validate_ledger.py`를 재실행**해 status를 다시 계산한다: confirmed → verified 승격, refuted → Refuted, 여전히 inconclusive → Unresolved 유지.
4. **기본 모드는 이 단계를 건너뛴다(빠름).** strict 모드만 감사 가능한 재검증을 붙인다.

→ 넓이(기본 검색) + 정밀(strict 재검증)을 결합하되 **전체가 아니라 고위험/미확정 주장에만** 적용해 비용을 제어한다. 단정/합성은 항상 게이트가 만든 `verified_claims.json`만 근거로 한다.

### Phase 7: Output & Packaging (산출·패키징)
- 가독성 최적화 포맷
- 요약(executive summary) 포함
- 정식 bibliography 생성
- 요청 형식으로 export
- (선택) 인터랙티브 웹사이트 생성

#### 마감 자기검증 (필수 — 측정)

보고서를 다 쓴 뒤 평가 채점기를 돌려 본문이 검증 계약을 실제로 지켰는지 **숫자로 확인**한다:

```bash
python3 "$PLUGIN_ROOT/skills/insane-research-main/scripts/eval_report.py" --session "RESEARCH/{topic}_{timestamp}"
```

- `verdict: FAIL`이면(미검증/반박 주장이 본문에 샜거나 인용이 레지스트리에 없음) **고쳐서 다시 돌린다** — 그 상태로 마감 금지.
- 지표(`leak_rate`·`citation_resolution_rate`·`orphan_source_rate`·`verified_coverage_rate`)는 `outputs/eval_report.json`에 저장된다. 게이트 on/off A/B나 회귀 추적에 쓴다.

---

## 멀티 소스 리서치 전략

서브토픽·소스타입·교차검증을 나눠 커버리지를 높인다. Codex에서는 다음을 원칙으로 한다:

| 역할 | 초점 | 산출 |
|--|--|--|
| 웹 리서치 | 현재 정보·트렌드·뉴스 | 출처 URL 포함 구조화 요약 |
| 학술/기술 | 논문·스펙·방법론 | 인용 포함 기술 분석 |
| 교차검증 | 팩트체크·검증 | 핵심 발견의 confidence 등급 |

기본은 **메인 스레드 순차 실행**이다. 사용자가 명시적으로 병렬/팀 리서치를 요청할 때만 Codex 서브에이전트를 쓰고, 각 위임 서브토픽은 범위를 좁게 묶는다. 에이전트 프롬프트 템플릿과 Graph of Thoughts 통합:
`$PLUGIN_ROOT/skills/insane-research-main/references/agent_prompts.md`

### ⚠️ Rate-Limit & Reliability Guard (필수)

1. **동시 팬아웃 throttle** — 한 번에 다수 에이전트(또는 다수 병렬 검증 호출)를 동시 실행하면 구독 플랜 서버측 rate-limit에 걸려 무더기 실패한다. 병렬을 쓰더라도 **최대 2~3개씩 순차 배치**로 실행하고 한 배치 완료 후 다음 배치를 띄운다. 교차검증·fact-check처럼 호출 수가 많은 단계는 특히 순차로 처리한다.
2. **백그라운드 silent death 회피** — 백그라운드로 띄운 에이전트는 rate-limit·세션 부하에서 알림 없이 죽어 무산출이 될 수 있다. 백그라운드를 쓴 뒤에는 산출물/트랜스크립트로 생존을 확인하고, 죽었거나 불확실하면 **메인 스레드에서 순차로 직접 검색**하는 폴백으로 전환한다. 안정성이 중요하면 처음부터 포그라운드/메인스레드 순차를 우선한다.

---

## 도구 사용

기본 도구(웹 검색, 브라우징, `curl`/`gh` 등 셸)로 리서치를 수행한다. 플랫폼별 최적 접근법은 `tool_strategy.md`를 참조한다. 환경에 MCP 도구(Perplexity, Firecrawl, Exa, 브라우저 등)가 설치돼 있으면 우선 활용하되, 없어도 기본 도구만으로 충분하다.

큰 `background execution flag` 팬아웃은 피한다 — rate-limit에 걸리고 백그라운드 에이전트가 조용히 죽을 수 있으므로, 신뢰성이 중요하면 포그라운드/메인스레드 순차를 우선한다. 상세 전략·예시:
`$PLUGIN_ROOT/skills/insane-research-main/references/tool_strategy.md`

---

## 인용 요건

모든 사실 주장은 인라인 인용을 포함한다.

### 필수 표준
1. **Author/Organization** — 누가 주장했는지
2. **Date** — 발행 시점
3. **Source Title** — 논문·기사·리포트 이름
4. **URL/DOI** — 검증용 직접 링크
5. **Page Numbers** — 긴 문서일 때(해당 시)

### 소스 품질 등급
| 등급 | 설명 | 예시 |
|--|--|--|
| **A** | 피어리뷰·체계적 리뷰·메타분석 | Nature, Lancet, IEEE |
| **B** | 공식 문서·임상 가이드·코호트 연구 | FDA, W3C, WHO |
| **C** | 전문가 의견·사례 보고·산업 리포트 | Gartner, 컨퍼런스 |
| **D** | 예비 연구·프리프린트·백서 | arXiv, 회사 블로그 |
| **E** | 일화적·이론적·추측성 | 소셜미디어, 포럼 |

### Red Flags (신뢰 불가 소스)
저자 미상 / 발행일 누락 / 깨지거나 의심스러운 URL / 데이터 없는 주장 / 미공개 이해상충 / 약탈적 저널 / 철회된 논문.

상세 인용 규칙: `$PLUGIN_ROOT/skills/insane-research-main/references/citation_rules.md`
소스 품질 루브릭: `$PLUGIN_ROOT/skills/insane-research-main/references/quality_rubric.md`

---

## 환각 방지

1. **모든 진술을 소스에 grounding** — 검증 가능한 소스 없이 단정 금지. 불확실하면 추측 대신 "Source needed".
2. **핵심 주장엔 Chain-of-Verification** — 검증 질문 생성 → 독립 검색 → 검증 후에만 확정.
3. **다중 소스 교차참조** — 핵심 발견은 2개 이상 독립 소스. 소스가 충돌하면 명시.
4. **불확실성 명시** — "Studies show..." 대신 "According to [source]...". 예비/논쟁적 발견은 한정.

### 검증 체크리스트
- [ ] 모든 주장에 인라인 인용
- [ ] 모든 URL 접근 가능
- [ ] orphan 인용 없음
- [ ] 모순 명시
- [ ] 소스 품질 등급 적용

---

## 상태 관리

### state.json 스키마
```json
{
  "session_id": "Topic_Name_20260224_143000",
  "topic": "Research Topic",
  "created_at": "2026-02-24T14:30:00Z",
  "updated_at": "2026-02-24T15:45:00Z",
  "status": "PHASE_3_QUERYING",
  "current_phase": 3,
  "requirements": {
    "focus": ["aspect1", "aspect2"],
    "output_format": "comprehensive_report",
    "scope": {"timeframe": {}, "geography": {}},
    "sources": {"required_types": [], "min_quality": "B"},
    "audience": "executive",
    "special_requirements": []
  },
  "plan": {"subtopics": [], "search_queries": {}, "agent_assignments": []},
  "progress": {
    "phase_1": "completed", "phase_2": "completed", "phase_3": "in_progress",
    "phase_4": "pending", "phase_5": "pending", "phase_6": "pending", "phase_7": "pending"
  },
  "sources_count": 0,
  "artifacts": {},
  "errors": []
}
```

### sources.jsonl 스키마 (한 줄당 JSON 하나)
```json
{"id": "src_001", "url": "https://...", "title": "Article Title", "author": "Author", "date": "2024-06-15", "domain": "nature.com", "type": "academic", "quality_rating": "A", "snippet": "relevant excerpt...", "claims": ["claim1"], "verified": true}
```

페이즈 입출력 계약: `$PLUGIN_ROOT/skills/insane-research-main/references/phase_contracts.md`

---

## 산출 구조

```
RESEARCH/{topic}_{timestamp}/
├── state.json                    # 세션 상태 (재개 가능)
├── README.md                     # 네비게이션 가이드
├── artifacts/                    # 중간 산출물
│   ├── research_plan.json
│   ├── agent_results/
│   └── drafts/
├── sources/
│   ├── sources.jsonl            # 수집 소스 전체
│   ├── bibliography.md          # 정리된 인용
│   └── quality_report.md        # 소스 품질 등급
├── outputs/                     # 최종 산출물
│   ├── 00_executive_summary.md
│   ├── 01_full_report/
│   │   ├── 01_introduction.md
│   │   ├── 02_current_landscape.md
│   │   ├── 03_challenges.md
│   │   ├── 04_future_outlook.md
│   │   └── 05_conclusions.md
│   ├── 02_appendices/
│   └── comparison_data.json
└── website/                     # (선택) 비주얼 프레젠테이션
    ├── index.html
    ├── styles.css
    └── script.js
```

### 출력 템플릿

일관된 포맷을 위해 `$PLUGIN_ROOT/skills/insane-research-main/assets/templates/`의 템플릿을 사용한다:

| 템플릿 | 용도 |
|--|--|
| `executive_summary.md` | 요약 구조 |
| `full_report_section.md` | 개별 리포트 섹션 템플릿 |
| `bibliography.md` | 품질 분포 포함 bibliography |
| `readme_research.md` | 리서치 세션 README/네비게이션 |
| `website_template.html` | 인터랙티브 웹 프레젠테이션 |

---

### Research Type 기반 골격 동적 생성 (참고용 — 기본 5섹션 유지)

기본 5섹션 골격(introduction/landscape/challenges/future_outlook/conclusions)이 모든 리서치의 default. 사용자가 명시적으로 다른 type을 요청한 경우에만, 아래 **참고 예시 패턴**을 보고 사용자 리서치에 맞게 골격을 **즉석 동적 생성**한다.

> **주의**: 기본 7-Phase + 5섹션 + Date-aware는 모두 insane-research의 핵심 contract로 보존. type별 골격은 **사용자 명시 요청 시에만** 적용되는 advanced 옵션이며, 표는 메뉴가 아니라 **동적 생성 학습용 예시**다.

#### 참고 예시 (메뉴 아님 — 패턴 학습용)

| Research Type | 5섹션 패턴 예시 | 적합 사례 |
|--|--|--|
| **Exploratory** (새 영역 탐색) | introduction / landscape / opportunities / challenges / conclusions | 신규 시장/기술 탐색 |
| **Comparative** (A vs B 비교) | introduction / criteria / comparison_matrix / recommendation / conclusions | 도구/제품 비교 |
| **Predictive** (미래 시나리오) | introduction / current_state / trends / scenarios / risks_and_recommendations | 시장 예측 / 기술 로드맵 |
| **Analytical** (원인-결과) | introduction / problem / causes / effects / conclusions | 사건 분석 / 인과 추적 |
| **기본 (Generic)** | introduction / current_landscape / challenges / future_outlook / conclusions | 종합 리서치 (default) |

#### 적용 절차
1. Phase 1에서 사용자 자연어로부터 리서치 type 추정 (가장 가까운 패턴)
2. 예시 패턴을 학습 후, **사용자 주제에 맞춰 5 섹션 명을 동적 생성** (섹션 명 그대로 카피 금지)
3. 사용자에게 confirm (§A 번호 블록): "이 리서치는 [Comparative] 패턴에 가까워 보입니다 — 5섹션을 [introduction / X 비교 기준 / X vs Y 비교 / 추천 / 결론]으로 갈까요, 기본 5섹션으로 갈까요?"
4. confirm → 동적 골격 사용 / 미명시·모호 → **기본 5섹션 (안전 default)**
5. state.json `report_skeleton` 필드에 최종 골격 기록 (resume 가능)

#### ⚠️ 주의
- type 자동 결정 금지 — 사용자 confirm 필수
- 표는 카탈로그가 아닌 **패턴 예시집** — 새 type 사례를 표에 추가하지 말 것
- 7-Phase / minimum 2 sources / A-E quality / Hallucination Prevention 등 contract는 모두 그대로 유지

---

## 구조화 쿼리 지원

정밀 제어를 위해 다음 스키마를 따르는 구조화 JSON 쿼리를 받는다:
`$PLUGIN_ROOT/skills/insane-research-main/references/query_schema.json`

사용자가 JSON 객체를 입력으로 제공하면 스키마대로 파싱하고 Phase 1(Question Scoping)을 건너뛴다(요건이 이미 정의됨). 예시 쿼리:
`$PLUGIN_ROOT/skills/insane-research-main/examples/`

---

## Resume 프로토콜

resume 트리거 시:
1. 가용 세션 나열: `RESEARCH/*/state.json`
2. 선택 세션의 `state.json` 로드
3. `progress` 객체에서 마지막 완료 페이즈 확인
4. 다음 pending 페이즈부터 재개
5. 실행 루프 계속

```python
for phase_num in range(1, 8):
    phase_key = f"phase_{phase_num}"
    if state["progress"][phase_key] == "in_progress":
        resume_phase(phase_num); break
    elif state["progress"][phase_key] == "pending":
        start_phase(phase_num); break
```

---

## 에러 처리

### 페이즈 실패
1. `state.json` errors 배열에 에러 로깅
2. progress에서 페이즈를 `failed`로 표시
3. 사용자에게 상세 통지
4. 제안: Retry / Skip / Abort

### 네트워크 실패
- 백오프와 함께 최대 3회 재시도
- 여전히 실패 → `tool_strategy.md`의 "접근 불가 시 우회 전략(Fallback)" 참조 (모바일 UA curl → OGP 메타태그 → Google 캐시/Wayback → curl_cffi → 브라우저)
- 응답 검증 규칙으로 성공/실패 판정 (로그인 페이지·CAPTCHA·빈 SPA 감지)
- 실패 URL + fallback 결과를 `sources/failed_urls.txt`에 로깅
- 가용 소스(우회 회수 콘텐츠 포함)로 계속 진행

### 토큰 한계
- 긴 문서는 청크 분할 / 중간 결과 자주 저장 / 매우 긴 소스는 요약

---

## 완료 전 품질 체크리스트

- [ ] 모든 주장에 검증 가능한 소스
- [ ] 핵심 발견을 다중 소스가 뒷받침
- [ ] 모순이 명시·설명됨
- [ ] 소스가 최신·권위 있음
- [ ] 환각·미근거 주장 없음
- [ ] 증거→결론의 명확한 논리 흐름
- [ ] 전반에 걸친 정식 인용 포맷
- [ ] executive summary가 전체 내용 반영
- [ ] bibliography 완비
- [ ] 모든 백그라운드 작업 완료·결과 수집됨

---

## 스크립트와 유틸리티

스크립트: `$PLUGIN_ROOT/skills/insane-research-main/scripts/`

| 스크립트 | 용도 | 권위 |
|--|--|--|
| `validate_ledger.py` | **검증 게이트 (필수).** claim_ledger + sources를 읽어 status를 결정론적으로 계산, `verified_claims.json` 생산, `state.json`에 서명 기록 | **authoritative** — Phase 5/7 진입 게이트 |
| `eval_report.py` | **평가 채점기 (필수).** 본문이 검증 계약을 지켰는지 측정 — leak/citation-resolution/orphan/coverage 4지표, `eval_report.json` 생산 | **authoritative** — Phase 7 마감 자기검증 |
| `orchestrator.py` | 세션 폴더/`state.json` 생성·소스 append 등 **상태 헬퍼**. 내부 phase 전이 로직은 권위가 없다(SKILL.md 흐름이 오케스트레이션) | helper (정적 자산) |
| `pipelines.py` | 에이전트 프롬프트 템플릿·clarification·synthesis 프롬프트 **정적 자산** | helper (정적 자산) |

> **오케스트레이션은 프롬프트(이 SKILL.md)가, 검증은 코드(`validate_ledger.py`)가 담당한다.** `orchestrator.py`/`pipelines.py`의 state-machine·plan 스텁은 참고용 헬퍼일 뿐 실행 권위가 없으니, 검증/합성 게이트는 반드시 `validate_ledger.py`로 강제한다.

---

## References

| 레퍼런스 | 위치 |
|--|--|
| 인용 포맷 규칙 | `$PLUGIN_ROOT/skills/insane-research-main/references/citation_rules.md` |
| 페이즈 입출력 계약 | `$PLUGIN_ROOT/skills/insane-research-main/references/phase_contracts.md` |
| 소스 품질 루브릭 | `$PLUGIN_ROOT/skills/insane-research-main/references/quality_rubric.md` |
| 에이전트 프롬프트 템플릿 & GoT | `$PLUGIN_ROOT/skills/insane-research-main/references/agent_prompts.md` |
| 도구 전략 & 코드 예시 | `$PLUGIN_ROOT/skills/insane-research-main/references/tool_strategy.md` |
| 구조화 쿼리 스키마 | `$PLUGIN_ROOT/skills/insane-research-main/references/query_schema.json` |
| 쿼리 생성 가이드 | `$PLUGIN_ROOT/skills/insane-research-main/references/query_generator.md` |
