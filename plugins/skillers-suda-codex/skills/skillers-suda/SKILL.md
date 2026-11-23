---
name: skillers-suda
description: This skill should be used when the user asks to "스킬 만들어줘", "에이전트 만들어줘", "커맨드 만들어줘", "스킬러들의 수다", "수다", "Codex 스킬 만들어줘", "이 스킬 분석해줘", "이 스킬 개선해줘", "skill builder", "make a skill", "create a skill", "build a skill", "improve this skill". 4명의 전문가 sub-agent를 실제로 소집해 토론시키고, 그 결과로 바이브코더의 아이디어를 동작하는 Codex 스킬로 변환한다 — 인터뷰, 워크플로우 설계, 파일 생성, 자동 검증, eval, description 최적화, 패키징까지.
---

# 스킬러들의 수다

> 4명의 전문가 에이전트를 실제로 소집하여 토론시키고, 그 결과로 바이브코더의 아이디어를 동작하는 스킬로 변환합니다.

> **질문 원칙 (`$PLUGIN_ROOT/shared/questioning-policy.md`)**: 아이디어를 캐낼 때 가정형 말고 **과거 실제 행동**을 묻는다("지금 그걸 어떻게 하고 계세요?" — Mom Test). 표면·회피 답을 결론으로 받지 말고 한 번 더 구체 탐침(§2a·§2b). 이미 구체적이면 과잉질문 금지(§2c).

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

**이 문서는 참고 문서가 아니라 실행 지시서다.**

### 질문 렌더링 — §A 질문 도구 (Codex 전용)

이 문서에서 "선택지로 확인받는다"는 모두 `$PLUGIN_ROOT/shared/questioning-policy.md §A`를 따른다: 이번 세션 도구 목록에 `request_user_input_async`(기본 모드) 또는 `request_user_input`(Plan 모드)이 있으면 그 도구로 한 번에 묻는다. async 도구는 부른 뒤 한 줄 안내("위 질문에 답해 주시면 이어서 진행합니다")만 쓰고 **턴을 끝내며**, 답이 다음 사용자 메시지로 오면 이어간다(답에 달린 결정을 먼저 진행하지 않는다). 구조 프리뷰는 도구 호출 직전 채팅에 먼저 쓴다. 두 도구가 모두 없을 때만 아래 **번호형 선택지 블록(폴백)**을 채팅에 출력하고 사용자의 다음 자유 텍스트 답변을 읽는다. 이하 문서의 "§A 번호 블록" 예시는 모두 폴백일 때의 모양이다.

```text
예시 프리뷰            ← 구조를 보여줄 때만. 단순 선호 질문이면 생략.
  [User] --1:N--> [Skill]      (매번 실제 결과로 새로 생성, 하드코딩 금지)

질문: <한 줄 질문>
1. <추천안> (추천) — 무엇인지, 왜 좋은지, 트레이드오프
2. <대안> — 무엇인지, 트레이드오프
3. 문장으로 직접 수정 요청
(여러 개 고를 수 있으면: "여러 개면 1,3처럼 적어주세요")
```

- 추천안은 항상 **1번**. 선택지마다 설명 필수. 쉬운 말로.
- "잘 모르겠어요"는 별도 선택지로 만들지 말고 "모르면 1번으로 진행하겠습니다"로 안내한다.
- 핵심 문제 발굴(Phase A 첫 턴)은 질문 도구·번호 블록 대신 **열린 텍스트 질문**으로. 단순 분류/설정 고르기일수록 질문 도구(없으면 번호 블록)가 적합하다.
- 사용자가 번호가 아닌 문장으로 답해도 그대로 받는다.

### 진입점 판단 — 사용자가 어디에 있는지 파악하고 거기서 시작한다

요청 문장을 인수처럼 파싱해 동작을 결정한다:

| 상황 | 시작 지점 |
|------|----------|
| 아이디어 없음 ("스킬 만들어줘"만) | 인터랙티브 메뉴 → Phase A |
| 아이디어 있음 (요청에 포함) | Phase B (전문가 팀 소집) |
| 대화에 이미 워크플로우가 있음 ("이걸 스킬로 만들어줘") | 대화에서 추출 → Phase D (워크플로우 확인) |
| 이미 SKILL.md 드래프트가 있음 ("이 스킬 개선해줘") | Phase F (eval 실행) |
| "분석 [경로]" / "이 스킬 분석해줘" | 경로 판별 → 스킬 분석 모드 또는 에이전트 분석 모드 |
| "사용법 안내" | 아래 사용법 설명 후 종료 |

**경로 판별 (분석 모드):**
- 경로가 sub-agent 프롬프트 파일(`references/agents/*.md` 패턴 또는 에이전트 역할을 정의한 단일 `.md`)이면 → **에이전트 분석 모드**
- 경로가 스킬 디렉토리(SKILL.md 포함) 또는 SKILL.md 파일이면 → **스킬 분석 모드**

사용자가 "eval 안 해도 돼, 그냥 바이브로 가자"라고 하면 eval을 스킵하고 대화형으로 진행해도 된다.

### 인터랙티브 메뉴 (아이디어 없이 호출됐을 때)

§A 질문 도구로 즉시 묻는다(도구가 없으면 번호 블록 폴백 출력). 번호 블록 폴백일 때의 모양:

```text
질문: 어떤 걸 도와드릴까요?
1. 새 스킬 만들기 (추천) — 아이디어 하나만 말해주세요. 4명의 전문가가 인터뷰로 동작하는 스킬을 만들어드려요.
2. 기존 스킬 분석 — 만들어둔 스킬을 분석해서 개선점을 제안해드려요.
3. 사용법 안내 — 스킬러들의 수다가 뭔지, 어떻게 쓰는지 알려드려요.
```

- **1** → 아이디어가 없으면 Phase A의 열린 질문으로, 있으면 Phase B로
- **2** → 스킬 경로를 묻고 분석 모드 실행
- **3** → 쉬운 말로 설명: ① 한 문장으로 아이디어를 말하면 4명의 전문가가 수다를 떨며 인터뷰 시작 ② 3-5개 질문에 답하면 동작하는 스킬 파일이 완성 ③ 모든 질문에 설명과 장단점이 있으니 읽고 고르면 됨 ④ 모르겠으면 (추천) 표시된 걸 고르면 됨

---

## 소개

이 스킬은 코딩을 몰라도 됩니다. 아이디어만 있으면 돼요.

4명의 전문가 에이전트를 **실제로 소집**해서 여러분의 아이디어를 분석합니다. 시뮬레이션이 아니라 진짜 4개의 sub-agent가 병렬로 동시에 분석하고, 그 결과를 종합해서 동작하는 **Codex 스킬**(필요하면 임베드 sub-agent·플러그인 패키지 포함)을 만들어드립니다.

이 스킬이 만드는 결과물은 Codex 스킬이다 — `SKILL.md`(frontmatter는 `name`·`description` 두 필드) + 선택적 `references/`·`scripts/`·`assets/`. Codex에는 슬래시 커맨드 폴더도 에이전트 로스터 폴더도 없다. 진입은 항상 description 트리거로, 자율 실행 역할은 소유 스킬 안에 프롬프트로 임베드해 sub-agent로 스폰한다(`references/component-type-decision.md`).

**4명의 전문가 (검증 다중성 보장 — 인원수 4명은 유지, 페르소나 정의는 도메인별 가변):**

기본 set:
- **기획자** — 방향을 잡아줘요. "누가 쓸 건데? 뭘 해결하는 거야?"
- **사용자** — UX를 검증해요. "나라면 이걸 어떻게 쓸까?"
- **전문가** — 기술적 가능성을 따져요. "이 분야는 이런 점을 조심해야 해"
- **검수자** — 엣지 케이스를 잡아요. "이거 이 경우에도 돼?"

> 도메인 특화가 필요한 경우 `references/personas.md`의 동적 생성 절차 + 참고 예시를 보고 4명을 **매번 사용자 아이디어에 맞게 즉석 정의**한다. 카탈로그에서 메뉴처럼 고르는 게 아니라, 예시 패턴을 학습한 뒤 도메인 키워드를 4 차원(방향성/사용/전문성/검증)에 매핑하여 새로 생성. **인원수 4는 검증 다중성의 본질이므로 유지**.

---

## 워크플로우

### Phase A: 아이디어 수집

**목표:** 만들고 싶은 스킬의 핵심 아이디어를 파악합니다.

**대화 컨텍스트 추출:** 현재 대화에 이미 워크플로우가 있는 경우 (예: "이걸 스킬로 만들어줘"), 대화 히스토리에서 답을 먼저 추출한다 — 사용된 도구, 단계별 순서, 사용자가 한 수정, 입출력 형식. 사용자가 빈 부분을 채우고, 다음 단계로 넘어가기 전에 확인받는다.

요청에 아이디어가 포함되었으면 그대로 사용합니다. 없으면 **열린 텍스트 질문 하나**로 묻는다(핵심 문제 발굴은 번호 블록이 아니라 열린 질문 — §A·§1.2). 감을 잡을 수 있게 예시만 곁들인다:

```text
어떤 스킬을 만들고 싶으세요? 한 문장으로 말해주세요.
(예: "문서를 다른 언어로 번역해줘", "회의 내용을 요약하고 액션 아이템 뽑아줘", "코드를 분석해서 개선점 찾아줘")
```

사용자가 예시 중 하나를 골라 말해도 그것을 아이디어로 사용합니다.

아이디어가 너무 모호하면 (예: "좋은 스킬") **과거 행동 앵커**로 1개 추가 질문한다(§2b): "지금은 그걸 어떻게 하고 계세요?". 명확하면 바로 Phase B로 진행합니다(§2c).

---

### Phase B: 전문가 팀 소집 + 토론

**목표:** 4명의 전문가 sub-agent를 병렬로 스폰하여 아이디어를 다각도로 분석합니다.

#### Step 1: 팀 소집 안내

사용자에게 알립니다:

```
4명의 전문가를 소집할게요. 잠시만 기다려주세요...

소집 중: 기획자 / 사용자 / 전문가 / 검수자
```

#### Step 2: 4개 sub-agent 병렬 스폰

**반드시 Codex 런타임의 sub-agent 스폰으로 4개 에이전트를 동시에 (한 턴에서) 스폰한다.** 텍스트로 4명의 대화를 흉내내는 시뮬레이션은 금지다.

각 에이전트의 설정:

| 에이전트 | 종류 | 범위 | 한 줄 설명 |
|----------|------|------|-----------|
| 기획자 | 범용 sub-agent | 읽기 전용, 분석 1회 후 종료 | "기획자 관점 분석" |
| 사용자 | 범용 sub-agent | 읽기 전용, 분석 1회 후 종료 | "사용자 관점 분석" |
| 전문가 | 범용 sub-agent | 읽기 전용, 분석 1회 후 종료 | "전문가 관점 분석" |
| 검수자 | 범용 sub-agent | 읽기 전용, 분석 1회 후 종료 | "검수자 관점 분석" |

**에이전트 프롬프트:** `references/interview-guide.md` 섹션 2-1의 템플릿을 사용한다. `{아이디어}`를 사용자 아이디어로, `{추가정보}`를 Phase A 추가 정보로 교체. 각 프롬프트 끝에 "한줄 요약"을 요구한다.

**폴백:** 현재 환경이 sub-agent 위임을 지원하지 않으면(스폰 도구 부재) 조용히 메인 스레드에서 4 관점을 **순서대로 각각 독립 섹션으로** 작성해 종합한다. 존재하지 않는 도구를 가정하지 않는다.

#### Step 3: 토론 결과 종합

4개 에이전트의 응답을 수집한 뒤, **자연스러운 대화 형식**으로 종합하여 사용자에게 보여준다.

**종합 출력 형식:**

```
전문가 4명이 분석을 마쳤어요! 토론 결과를 정리할게요:

🎯 기획자: "{기획자 한줄 요약}"
→ {핵심 분석 1-2줄}

👤 사용자: "{사용자 한줄 요약}"
→ {핵심 분석 1-2줄}

🔧 전문가: "{전문가 한줄 요약}"
→ {핵심 분석 1-2줄}

🔍 검수자: "{검수자 한줄 요약}"
→ {핵심 분석 1-2줄}

💬 종합: {4명의 분석을 통합한 방향 제안 2-3줄}
```

**의견 충돌 처리:**

에이전트 간 의견이 다른 부분이 있으면 반드시 보여줍니다:

```
⚡ 의견이 갈렸어요:
- 기획자는 "{A}"를 제안했지만, 사용자는 "{B}"가 더 낫다고 했어요.
- 어떤 방향이 좋을까요?
```

#### Step 4: 방향 확인

§A 질문 도구(없으면 번호 블록 폴백)를 **토론 결과에 맞게 동적으로 구성**한다. 정적 템플릿을 그대로 쓰지 않는다.

**충돌이 있을 때** — 충돌 포인트 자체를 선택지로 만든다:

```text
질문: {충돌 내용을 구체적으로 — 예: '단일 스킬로 갈까요, 스킬 + 임베드 sub-agent로 갈까요?'}
1. {선택지A} (추천) — {왜 이게 나은지 — 전문가 근거 요약}
2. {선택지B} — {왜 이걸 고를 수 있는지 — 다른 전문가 근거}
3. 다시 토론해줘 — 추가 정보를 주면 전문가들이 다시 분석해요.
```

**충돌이 없을 때** — 핵심 결정 사항을 선택지 위 프리뷰에 요약하고 확인받는다:

```text
합의된 방향
  MVP 범위: {MVP 범위}
  핵심 워크플로우: {요약}
  컴포넌트 타입: {스킬 / 스킬 + 임베드 sub-agent / 플러그인 패키지}

질문: 전문가들이 합의한 방향이에요. 확인해주세요.
1. 좋아요, 진행 (추천) — 이 방향대로 워크플로우를 설계할게요.
2. 수정할 부분 있어요 — 어떤 부분을 바꾸고 싶은지 알려주세요.
3. 다시 토론해줘 — 추가 정보를 주면 전문가들이 다시 분석해요.
```

"다시 토론해줘" 선택 시: 사용자의 추가 정보를 받고 Step 2부터 다시 실행합니다.

---

### Phase C: 상세 인터뷰 (1-2개 추가 질문)

**목표:** 팀 토론에서 결정하지 못한 사항을 사용자에게 직접 물어봅니다.

팀 토론 결과에서 자동으로 판단한 내용:
- `purpose` — 기획자가 분석
- `input_type` / `output_type` — 사용자가 분석
- `trigger_keywords` — 기획자가 제안
- `domain` — 전문가가 판단
- `constraints` — 검수자가 식별

**추가로 확인이 필요한 경우만 질문합니다:**

자동 판단이 불확실한 항목에 대해서만 §A 질문 도구로 묻는다(없으면 번호 블록 폴백). 최대 2개까지. 선택지는 토론 결과에 맞게 동적으로 채운다. 예:

```text
질문: 결과물은 어떤 형태가 좋을까요?
1. 텍스트 요약 (추천) — 바로 대화창에 보여드려요.
2. 파일 생성 — .md/.txt/.csv 등 파일로 저장해요.
3. 여러 파일 세트 — 프로젝트 구조처럼 여러 파일을 만들어요.
```

팀 토론에서 충분히 파악되었으면 이 Phase를 스킵하고 Phase D로 바로 진행합니다.

**질문 규칙:**

- **핵심 결정**은 §A 질문 도구(없으면 번호 블록 폴백) — 컴포넌트 타입, 워크플로우 확인, eval 결과 등 선택지가 명확한 것
- **단순 확인이나 추가 질문**은 자연 대화도 OK — "혹시 이런 뜻인가요?" 같은 건 굳이 질문 도구·번호 블록을 강제하지 않는다
- 질문 도구·번호 블록 사용 시: 선택지마다 설명 필수, 추천 옵션은 첫 번째 + "(추천)", 쉬운 말로

---

### Phase D: 워크플로우 설계

**목표:** 팀 토론 결과 + 사용자 답변을 바탕으로 워크플로우를 설계합니다.

**6가지 단계 타입:**

1. **prompt** — 모델이 생각하는 단계 (분석, 요약, 판단, 창작)
2. **script** — 반복/일관성/API 작업을 위한 Python/Bash
3. **api_mcp** — 외부 도구 연동 (API > MCP > 직접 구현 우선순위)
4. **rag** — 참조 파일 검색 (`references/` 폴더)
5. **review** — 검토 단계 (api_mcp/rag 뒤에 반드시 포함)
6. **generate** — 최종 출력 (파일 생성, 보고서)

**단계 타입 선택 기준:**

1. 외부 서비스가 필요한가? → **api_mcp** (뒤에 review 추가)
2. 참조 문서/도메인 지식이 필요한가? → **rag** (뒤에 review/prompt 추가)
3. 반복 작업/정확한 형식이 필요한가? → **script**
4. 모델의 판단/창작이 필요한가? → **prompt**
5. 결과 확인이 필요한가? → **review**
6. 파일/보고서를 만들어야 하는가? → **generate**

**기존 에이전트 확인 (컴포넌트 타입 판단 전):**

임베드 sub-agent가 후보일 때, 대상 프로젝트의 스킬 디렉터리들을 스캔해 기존 sub-agent 프롬프트를 확인한다:

1. `skills/*/references/agents/*.md` 파일이 있으면 파일명과 첫 헤더/역할 줄만 빠르게 스캔
2. 새로 만들려는 에이전트와 역할이 겹치는 기존 에이전트가 있으면 사용자에게 안내:
   ```
   비슷한 역할의 전문가가 이미 있어요: [에이전트명] — [역할 한 줄]
   새로 만들까요, 기존 걸 개선할까요?
   ```
   §A 질문 도구(없으면 번호 블록 폴백)로 선택 받기:
   ```text
   질문: 비슷한 역할의 에이전트가 이미 있어요. 어떻게 할까요?
   1. 기존 걸 개선 (추천) — 기존 에이전트를 읽고 개선 버전으로 업데이트해드려요.
   2. 새로 만들기 — 기존 에이전트와 별개로 새 에이전트를 만들어요.
   ```
3. "기존 걸 개선" 선택 시 → 기존 에이전트 파일을 읽고, Phase E에서 개선 버전으로 덮어쓰기 (덮어쓰기 전 사용자 확인 필수)
4. "새로 만들기" 선택 시 → 기존 워크플로우 계속
5. 기존 에이전트가 없으면 → 조용히 기존 워크플로우 계속 (사용자에게 불필요한 안내 없음)

**컴포넌트 타입 (전문가 에이전트의 분석을 참고하여 결정, 상세: `references/component-type-decision.md`):**

| 타입 | 특징 | 언제 |
|------|------|------|
| **스킬** | 대화에 자연스럽게 녹아들어요. 단일 작업. 인수/상황 분기는 SKILL.md 안의 진입점 판단 표로. | 기본값 |
| **스킬 + 임베드 sub-agent** | 소유 스킬이 워크플로우 중 sub-agent를 스폰. 독립 컨텍스트. 다단계 자율 실행·병렬 검증. | 복잡한 자율 작업, 다관점 검증 |
| **플러그인 패키지** | 스킬 2개 이상 + 공용 references/MCP 설정 + 마켓 interface 메타데이터를 한 제품으로. | 제품 단위 배포 |

본진의 "커맨드"(명시적 슬래시 진입·인수 분기)는 Codex에 없다 — description에 트리거 문구를 넣고 진입점 판단 표로 분기하는 **스킬**로 만든다.

**Degrees of Freedom (자유도) 식별:**

워크플로우 설계 시 **고정 요소**와 **가변 요소**를 구분한다:

| 구분 | 설명 | 예시 |
|------|------|------|
| 고정 | 워크플로우 구조, 단계 순서, 필수 검증 | "항상 3단계로 실행" |
| 가변 | 사용자가 바꿀 수 있는 파라미터 | 출력 언어, 상세도, 포맷 |

가변 요소가 있으면 SKILL.md에 **기본값 + 변경 방법**을 명시한다. 워크플로우 내 §A 질문 도구(없으면 번호 블록 폴백)로 처리하거나, SKILL.md 상단에 설정 가능 항목으로 문서화한다.

**Eval 기준 정의:**

워크플로우 설계와 함께 eval 시나리오를 정의한다. 검수자 에이전트의 분석(엣지 케이스, 테스트 시나리오)을 활용.

evals.json 형식으로 저장:
```json
{
  "skill_name": "{skill-name}",
  "evals": [
    {
      "id": 1,
      "prompt": "현실적이고 구체적인 사용자 프롬프트",
      "expected_output": "기대 결과 설명",
      "should_trigger": true,
      "files": []
    }
  ]
}
```

**품질 메트릭 정의 (선택):**
expectations 외에, 출력 품질을 연속 점수로 평가할 quality_metrics를 정의할 수 있다. 스킬 유형에 맞는 메트릭을 `references/eval-guide.md` 섹션 6의 템플릿에서 선택한다. 각 메트릭에 criteria, evaluation_steps(3-5개), threshold를 정의한다.

**현실적 프롬프트 철학:** eval 프롬프트는 실제 사용자가 입력할 법한 구체적 문장으로 작성한다. 파일 경로, 개인 상황, 약어, 오타, 캐주얼한 표현을 자연스럽게 섞는다.
- BAD: `"이 데이터를 포맷해줘"`, `"PDF에서 텍스트 추출"`
- GOOD: `"다운로드 폴더에 'Q4 매출 최종_v2.xlsx' 있는데 C열이 매출이고 D열이 비용이야. 이익률 퍼센트 컬럼 추가해줘"`

**should-trigger / should-not-trigger 구분:**

| 유형 | 개수 | 설명 |
|------|------|------|
| should-trigger | 2-3개 | 스킬이 반드시 트리거되어야 하는 쿼리. 다양한 표현(격식/캐주얼)으로 커버리지 확보 |
| should-not-trigger | 1-2개 | 키워드는 겹치지만 실제로는 다른 작업. 명백히 무관한 쿼리는 피한다 |

정상 시나리오 2-3개 + 엣지 케이스 1-2개를 정의한다. 상세 가이드: `references/eval-guide.md` 참조. 스키마 상세: `references/schemas.md` 참조.

**워크플로우 + Eval 확인:**

워크플로우 설계 결과와 eval 시나리오를 텍스트(§A 프리뷰)로 보여준 후, 확인을 받는다.

**Step D-1: 워크플로우 + Eval을 보여주기**

단계별 흐름과 eval 시나리오 목록을 보여준다. 예시:
```
워크플로우 설계 결과:

1단계: [설명]
2단계: [설명]
...

Eval 시나리오:
- should-trigger: [시나리오 1], [시나리오 2]
- should-not-trigger: [시나리오 1]
```

**Step D-2: §A 질문 도구로 확인**

텍스트 출력 직후 질문 도구를 부르고 턴을 끝낸다(도구가 없으면 번호 블록 폴백). 번호 블록 폴백일 때의 모양:

```text
질문: 워크플로우와 테스트 기준을 확인해주세요.
1. 이대로 진행 (추천) — 이 워크플로우대로 파일을 만들고 자동 검증까지 해드릴게요.
2. 수정할 부분 있어 — 워크플로우나 테스트 기준을 바꾸고 싶은지 알려주세요.
3. 나중에 할게 — 여기서 멈출게요. 나중에 다시 시작할 수 있어요.
```

---

### Phase E: 파일 생성

**목표:** 확인된 워크플로우를 실제 파일로 만듭니다.

**생성할 파일 구조:**

```
skills/{skill-name}/
├── SKILL.md              # 워크플로우 (1,500-2,000 단어)
├── scripts/              # script 타입 단계용
│   └── {script}.py
├── references/           # rag 타입 단계용
│   ├── {reference}.md
│   └── agents/           # 임베드 sub-agent 프롬프트 (필요 시)
│       └── {agent-name}.md
└── assets/               # 출력에 사용되는 파일 (컨텍스트에 로드하지 않음)
    └── {template/image/font/etc.}
```

**assets/ 폴더 용도:**
- 템플릿 파일 (HTML, React 보일러플레이트 등)
- 이미지, 아이콘, 폰트
- 샘플 데이터, 설정 파일
- scripts/references와 달리 **컨텍스트에 로드하지 않고** 출력물에 직접 사용

필요 시 추가 생성:
- `references/agents/{agent-name}.md` — 임베드 sub-agent 프롬프트 (생성 시 `references/agent-templates.md`를 참조하여 표준 구조와 품질 기준을 적용하고, SKILL.md의 해당 단계에 "이 파일을 프롬프트로 sub-agent를 스폰한다"를 명시한다)
- `.codex-plugin/plugin.json` — 플러그인 패키지로 묶을 때만 (`name`·`version`·`description`·`skills: "./skills/"` + 선택적 `interface`)

슬래시 커맨드 파일과 별도 에이전트 로스터 폴더는 만들지 않는다 — Codex에 없는 컴포넌트다.

**SKILL.md 생성 템플릿:**

```markdown
---
name: {skill-name}
description: This skill should be used when the user asks to "{trigger1}", "{trigger2}", "{trigger3}". {무엇을 하는지 + 왜}.
---

# {Display Name}

> {한 줄 설명}

## 워크플로우

### Step 1: {단계 이름}
**타입**: {prompt/script/api_mcp/rag/review/generate}
{실행 지침}

### Step 2: ...

## References
- **`references/{file}.md`** — {설명}

## Scripts
- **`scripts/{file}.py`** — {설명}

## Assets
- **`assets/{file}`** — {설명}

## Settings (가변 요소가 있을 때만)
| 설정 | 기본값 | 변경 방법 |
|------|--------|-----------|
| {파라미터} | {기본값} | {번호형 질문 또는 요청 문장으로 변경} |
```

frontmatter는 `name`과 `description` **두 필드만** 쓴다. 본진 전용 필드(`allowed-tools` 등)는 넣지 않는다 — Codex 검증기가 거부한다.

**Description 작성 (Pushy 전략):**

description은 스킬 트리거의 핵심 메커니즘이다. 모델은 스킬을 트리거하지 않는 쪽으로 편향되어 있으므로 (undertrigger), description을 적극적으로 작성한다.

1. **Pushy description** — 스킬이 하는 것 + 구체적 트리거 상황을 함께 기술한다.
   - BAD: `"코드 리뷰 도구"`
   - GOOD: `"코드 리뷰, 코드 검토, 코드 봐줘, review my code, 버그 찾아줘. Make sure to use this skill whenever the user mentions code review, even if they don't explicitly ask for it."`
2. **Why 설명** — description에 "무엇을 하는가"뿐 아니라 "왜 하는가"를 포함한다.
   - BAD: `"코드를 리뷰합니다"`
   - GOOD: `"코드를 리뷰합니다 — 보안 취약점과 성능 병목을 조기에 발견하여 프로덕션 장애를 예방하기 위해"`
3. **한/영 혼합** — 한국어와 영어 트리거를 모두 포함한다.
4. **복잡한 쿼리만 트리거** — 단순 질문("Python이 뭐야?")이 아닌, 스킬이 필요한 복잡한 요청에 반응하도록 설계한다.

초안 description을 작성하되, Phase H에서 트리거 eval로 다듬는다.
상세 가이드: `references/trigger-mechanism.md` 참조.

**Writing Style 규칙 (SKILL.md 생성 시 적용):**

1. **Imperative form 사용** — "To accomplish X, do Y" 형식. "You should do X" 금지.
   - O: "Read the configuration file. Validate the input."
   - X: "You should read the configuration file."
2. **Description은 third-person** — "This skill should be used when..." 형식.
3. **Why 설명 우선** — 지시사항에서 ALWAYS/NEVER 대신 이유를 설명한다. LLM은 이유를 이해하면 더 잘 따른다.
4. **Concise 원칙** — SKILL.md 본문은 1,500-2,000 단어 이내. 상세 내용은 references/로 분리.
   - 컨텍스트 윈도우는 공공재. 모델이 이미 아는 정보는 반복하지 않는다.
5. **references 참조 명시** — SKILL.md에서 references/ 파일을 명확히 링크한다.
6. **규율형(Discipline) 스킬이면 합리화 차단 장치 필수** — 생성하려는 스킬이 "X 전에 반드시 Y"를 강제하거나 AI가 압박받으면 건너뛸 규칙을 담는다면(예: 검증·테스트·역할분리 강제), SKILL.md에 Iron Law + 합리화 차단표(Excuse→Reality) + Red Flags + "Spirit vs Letter" 4종을 포함한다. 번역·포맷팅 같은 기법형 스킬에는 넣지 않는다(토큰 낭비). 판별·템플릿: `references/writing-style-guide.md` §6.

상세 가이드: `references/writing-style-guide.md` 참조.

**스크립트 생성 규칙:**

Python:
```python
#!/usr/bin/env python3
# {설명}
import sys
import json

def main():
    # 에러는 stderr로
    # 결과는 JSON으로 stdout에
    pass

if __name__ == "__main__":
    main()
```

Bash:
```bash
#!/usr/bin/env bash
set -euo pipefail
# 에러는 stderr로: echo "에러" >&2
```

경로는 `$PLUGIN_ROOT`를 기준으로 합니다.

> `$PLUGIN_ROOT`는 Codex가 플러그인 실행 시 자동으로 설정하는 환경 변수로, 해당 플러그인의 루트 디렉토리를 가리킵니다.

**파일 덮어쓰기 규칙:** 같은 이름의 파일이 있으면 사용자에게 확인한다. 동의 없이 덮어쓰지 않는다.

---

### Phase E-verify: 자동 검증

**목표:** 생성된 SKILL.md의 구조적 품질을 자동 검증하고, FAIL 항목을 수정합니다.

**Step 1: verify-skill.py 실행**

파일 생성 직후, 셸에서 검증 스크립트를 실행한다:

```bash
python3 "$PLUGIN_ROOT/skills/skillers-suda/scripts/verify-skill.py" <생성된 SKILL.md 경로>
python3 "$PLUGIN_ROOT/skills/skillers-suda/scripts/quick_validate.py" <생성된 스킬 디렉토리>
```

Windows PowerShell에서는 `$PLUGIN_ROOT` 대신 `$env:PLUGIN_ROOT`를 사용하고, `python3`이 없으면 `python`으로 호출한다. `quick_validate.py`는 PyYAML(`pip install pyyaml`)이 필요하다 — 없으면 verify-skill.py 결과만으로 진행한다.

**Step 2: 결과 처리**

| 결과 | 조치 |
|------|------|
| 전체 PASS | Phase F로 진행 |
| WARN 있음 | 사용자에게 안내 후 Phase F 진행 |
| FAIL 있음 | 아래 자동 수정 → 재검증 |

**FAIL 자동 수정:**

| FAIL 항목 | 자동 수정 |
|-----------|-----------|
| third_person | description을 "This skill should be used when..." 형식으로 변환 |
| trigger_phrases | 워크플로우에서 트리거 키워드 추출하여 추가 |
| imperative_form | second-person 표현을 imperative로 변환 |
| references_exist | 누락 파일 생성 또는 참조 제거 |

word_count FAIL은 자동 수정 불가 — 사용자에게 어떤 부분을 references/로 분리할지 확인한다.

자동 수정 후 verify-skill.py를 재실행하여 PASS를 확인한다. 상세 가이드: `references/eval-guide.md` 참조.

---

### Phase F: Eval 실행 + 벤치마크

**목표:** Phase D에서 정의한 eval 시나리오를 실행하고, 정량적/정성적으로 평가합니다.

**Step 1: evals.json 생성**

Phase D에서 정의한 eval 시나리오를 `evals/evals.json`으로 저장한다. 스키마: `references/schemas.md` 참조.

**Step 2: 테스트 실행 (sub-agent 병렬)**

각 eval 케이스마다 2개 sub-agent를 동시에 스폰한다:
- **with_skill**: 생성된 SKILL.md 전문을 프롬프트에 포함해 eval prompt 실행
- **without_skill (baseline)**: 스킬 없이 동일 prompt 실행

결과를 `{skill-name}-workspace/iteration-{N}/eval-{ID}/` 에 저장한다 (각각 `with_skill/`, `without_skill/` 하위에 `outputs/` + 트랜스크립트).

각 eval 디렉토리에 `eval_metadata.json` 생성:
```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name",
  "prompt": "사용자 프롬프트",
  "assertions": []
}
```

> Codex 빌드에는 본진의 자동 러너(`run_eval.py`, 다른 에이전트 CLI를 서브프로세스로 구동)가 포함되지 않는다. 실행은 위와 같이 sub-agent 스폰으로 대체하고, sub-agent 위임이 불가능한 환경이면 각 프롬프트를 메인 스레드에서 순서대로 실행해 같은 디렉터리 구조로 저장한다.

**Step 3: assertion 작성 (실행 중)**

테스트 실행 중에 정량적 assertion을 작성한다. 객관적으로 검증 가능한 것만 assertion으로 만들고, 주관적 품질은 사용자 리뷰에 맡긴다.

**Step 4: 채점 + 벤치마크 + 뷰어**

모든 실행 완료 후:

1. **채점** — `references/agents/grader.md`를 프롬프트로 채점 sub-agent를 스폰해 assertion 평가. `grading.json` 저장.
2. **벤치마크 집계**:
   ```bash
   python3 "$PLUGIN_ROOT/skills/skillers-suda/scripts/aggregate_benchmark.py" {workspace}/iteration-N --skill-name {name}
   ```
3. **분석** — `references/agents/analyzer.md`를 프롬프트로 패턴 분석 (비차별 assertion, 고분산 eval 등).
4. **뷰어 실행**:
   ```bash
   python3 "$PLUGIN_ROOT/skills/skillers-suda/assets/eval-viewer/generate_review.py" {workspace}/iteration-N \
     --skill-name "{name}" --benchmark {workspace}/iteration-N/benchmark.json
   ```
   iteration 2+ 에서는 `--previous-workspace` 옵션 추가.

> **Windows 참고**: PowerShell에서는 백슬래시 라인 연결(`\`) 대신 백틱(`` ` ``)을 쓰거나 한 줄로 합친다. `python`이 `python3`을 가리키지 않으면 `py -3`으로 대체 가능.

**Step 5: 사용자 피드백 수집**

뷰어에서 사용자가 리뷰 후 "Submit All Reviews" → `feedback.json` 생성. 피드백 읽고 §A 질문 도구로 묻는다(없으면 번호 블록 폴백). 폴백일 때의 모양:

```text
질문: eval 결과를 확인했어요. 어떻게 할까요?
1. 좋아요, 다음 단계로! — 결과가 만족스러우면 description 최적화로 넘어갈게요.
2. 개선이 필요해요 — 피드백 기반으로 스킬을 개선하고 다시 테스트할게요.
3. eval 케이스 수정 — 테스트 시나리오를 바꾸고 싶어요.
```

"개선이 필요해요" 선택 시 Phase G로 진행합니다.

---

### Phase G: 반복 개선

**목표:** 피드백 기반으로 스킬을 개선하고, 다시 테스트합니다.

**개선 원칙** (`references/improvement-principles.md` 참조):

1. **일반화** — 특정 eval 케이스만 통과하도록 하드코딩하지 않는다. 개별 케이스가 아닌 패턴을 해결한다.
2. **Lean 유지** — 효과 없는 지시를 제거한다. 트랜스크립트를 읽고 비생산적인 부분을 파악한다.
3. **Why 설명** — ALWAYS/NEVER 대신 이유를 설명한다. LLM은 이유를 이해하면 더 잘 따른다.
4. **반복 코드 번들** — 테스트 실행에서 sub-agent들이 독립적으로 같은 스크립트를 작성했다면, 스킬에 번들한다.

**반복 루프:**

1. 피드백 기반으로 스킬 수정
2. 새 `iteration-{N+1}/` 디렉토리에 재실행 (baseline 포함)
3. `--previous-workspace`로 뷰어 실행하여 이전 iteration과 비교
4. 사용자 리뷰 → 피드백 수집
5. 반복 (사용자가 만족하거나 의미 있는 개선이 없을 때까지)

**Blind Comparison (선택사항):**

두 버전 간 엄밀 비교가 필요하면 `references/agents/comparator.md`와 `references/agents/analyzer.md`를 프롬프트로 독립 sub-agent를 스폰한다. 블라인드로 품질을 판단한다.

---

### Phase H: Description 최적화

**목표:** 스킬의 description을 최적화하여 트리거 정확도를 높입니다.

**Step 1: 트리거 eval 쿼리 생성**

should-trigger 8-10개 + should-not-trigger 8-10개 = 약 20개 eval 쿼리를 생성한다.
현실적이고 구체적인 프롬프트로 작성 (Phase D의 현실적 프롬프트 철학 적용).

**Step 2: 사용자 리뷰**

`assets/eval_review.html` 템플릿으로 eval 세트를 사용자에게 보여준다:
1. `__EVAL_DATA_PLACEHOLDER__`를 eval JSON으로 교체
2. `__SKILL_NAME_PLACEHOLDER__`를 스킬 이름으로 교체
3. `__SKILL_DESCRIPTION_PLACEHOLDER__`를 현재 description으로 교체
4. `/tmp/eval_review_{skill-name}.html`에 저장 후 열기
5. 사용자가 수정 후 "Export Eval Set" → `eval_set.json` 다운로드

**Step 3: 최적화 루프 실행**

eval_set을 60% train / 40% test로 나눈다. 최대 5회 반복:
1. 현재 description으로 **트리거 판정 sub-agent**를 스폰한다 — 프롬프트에 "설치된 스킬 목록: {name}: {description}"과 train 쿼리를 주고, 각 쿼리에 대해 스킬을 읽을지(트리거) 여부만 JSON으로 답하게 한다. 쿼리당 3회 반복해 트리거율을 측정한다.
2. 오답(놓친 should-trigger·잘못 잡은 should-not-trigger)을 근거로 description 후보를 새로 쓴다 (`references/trigger-mechanism.md`의 Pushy 전략·차별화 규칙).
3. train 점수가 오르면 test 쿼리에도 같은 판정을 돌려 test 점수를 기록한다.
4. **test score 기준**으로 best_description을 선택한다 (과적합 방지). 개선이 멈추면 조기 종료.

> Codex 빌드에는 본진의 자동 최적화기(`run_loop.py`, 외부 SDK 의존)가 포함되지 않는다. 위 절차가 그 대체이며, 판정 sub-agent를 쓸 수 없는 환경이면 메인 스레드에서 각 쿼리를 "이 description만 보고 스킬을 열겠는가?"로 판정한다.

**Step 4: 결과 적용**

`best_description`을 SKILL.md frontmatter에 적용. 사용자에게 before/after + 점수를 보여준다.

---

### Phase I: 패키징

**목표:** 완성된 스킬을 .skill 파일로 패키징합니다.

```bash
cd "$PLUGIN_ROOT/skills/skillers-suda" && python3 -m scripts.package_skill {스킬 폴더 절대경로}
```

패키징 후 `.skill` 파일 경로를 사용자에게 안내한다. 플러그인 패키지로 묶었으면 `.codex-plugin/plugin.json`을 JSON 파싱으로 검증하고 결과를 함께 보고한다.

---

### 스킬 분석 모드

"분석 [스킬 경로]" / "이 스킬 분석해줘 / 검토해줘" 로 실행됩니다.

주어진 경로의 SKILL.md(+ 주요 references)를 읽고 frontmatter·워크플로우를 파싱한 뒤, Phase B와 같은 방식으로 4명의 전문가 sub-agent를 병렬 스폰해 분석한다:

- **기획자 관점**: 목적이 명확한가? 트리거 키워드가 충분한가?
- **사용자 관점**: 바이브코더가 쓰기 쉬운가? 설명이 이해하기 쉬운가?
- **전문가 관점**: 워크플로우가 기술적으로 올바른가? 스크립트/API 활용이 적절한가?
- **검수자 관점**: 엣지 케이스가 처리되는가? 에러 핸들링이 있는가?

**결과 형식:**

```
분석 결과를 알려드릴게요!

기획자: "{평가}"
사용자: "{평가}"
전문가: "{평가}"
검수자: "{평가}"

개선 제안:
1. {제안 1}
2. {제안 2}
3. {제안 3}
```

이어서 §A 질문 도구로 확인받는다(없으면 번호 블록 폴백). 폴백일 때의 모양:

```text
질문: 개선해드릴까요?
1. 제안대로 수정해줘 (추천) — 제안 전부를 적용해요.
2. 일부만 수정하고 싶어 — 어떤 항목을 적용할지 알려주세요.
3. 지금 이대로 괜찮아 — 분석 결과만 참고할게요.
```

적용 시 파일을 수정하되, 덮어쓰기 전 변경 내용을 미리 보여주고 확인받는다.

---

### 에이전트 분석 모드

"분석 [sub-agent 프롬프트 경로]" (예: `skills/my-skill/references/agents/reviewer.md`) 로 실행됩니다.

**Step 1: 에이전트 파일 읽기**

대상 에이전트 파일을 읽고, frontmatter(있으면) + 본문을 파싱한다:
- `name`, `description`, `tools` 등 frontmatter 필드 추출
- 본문에서 역할 정의, 워크플로우, 도구 배정, 출력 형식 파악
- 소유 스킬의 SKILL.md에서 이 에이전트를 스폰하는 단계를 찾아 입력/출력 계약을 확인

**Step 2: 4명 전문가 분석 (Phase B와 동일)**

4명의 전문가 sub-agent를 병렬 스폰하여 에이전트를 분석한다 (반드시 실제 스폰, 시뮬레이션 금지):

| 전문가 | 분석 관점 |
|--------|-----------|
| 기획자 | 역할 명확성, 목적 적합성 |
| 사용자 | 트리거 자연스러움, 사용 편의성 |
| 전문가 | 도구 배정 적절성, 프롬프트 품질 |
| 검수자 | R&R 완성도, 엣지 케이스 대응 |

**Step 3: 개선안 제안**

4명의 분석 결과를 종합하여 사용자에게 구체적인 개선안을 제안한다:
- description 개선 (Pushy 전략 적용 — undertrigger 방지)
- 도구 배정 최적화
- R&R 보강
- 프롬프트 정제

개선안을 정리한 후 §A 질문 도구로 묻는다(없으면 번호 블록 폴백). 폴백일 때의 모양:

```text
질문: 분석 결과를 바탕으로 개선안을 만들었어요. 어떻게 할까요?
1. 개선안 적용 (추천) — 제안된 개선안대로 에이전트 파일을 수정해드려요.
2. 일부만 수정 — 어떤 부분을 바꾸고 싶은지 알려주세요.
3. 지금은 유지 — 분석 결과만 참고하고 파일은 그대로 둘게요.
```

**Step 4: 사용자 확인 후 수정**

"개선안 적용" 또는 "일부만 수정" 선택 시 → 에이전트 파일을 수정한다. 덮어쓰기 전 수정 내용을 미리 보여주고 확인 받는다. 수정 후 `python3 "$PLUGIN_ROOT/skills/skillers-suda/scripts/verify_agent.py" <파일>`로 품질 기준을 재확인한다.

---

## 핵심 원칙

스킬을 수백만 번 사용할 사용자를 위해 만든다. 지금 눈앞의 예시만 통과하는 게 아니라, 다양한 상황에서 안정적으로 동작하는 스킬이 목표다.

**인터뷰 먼저, 파일 나중에** — 사용자의 의도를 충분히 파악해야 좋은 스킬이 나온다. 인터뷰를 건너뛰고 바로 파일을 만들면 재작업이 늘어난다.

**4명은 실제로 스폰한다** — 텍스트로 "기획자가 이렇게 말했어요"라고 시뮬레이션하면 다각도 분석이라는 핵심 가치가 사라진다. sub-agent 4개를 한 턴에 동시에 스폰해야 독립적 관점이 나온다. 순차 스폰도 피한다 — 속도가 느려질 뿐 아니라 앞선 에이전트의 결과에 영향받을 수 있다. 스폰이 불가능한 환경에서만 독립 섹션 종합으로 폴백한다.

**eval은 사용자 눈으로** — AI가 자체 판단으로 "잘 됐다"고 결론내면 문제를 놓친다. generate_review.py로 뷰어를 열어서 사용자가 직접 결과를 보고 판단해야 한다.

**일반화** — 특정 eval 케이스를 통과시키려고 하드코딩하면, 그 케이스에만 동작하는 brittle한 스킬이 된다. 개별 실패가 아니라 실패의 패턴을 해결한다.

**쉬운 말** — 이 스킬의 사용자는 바이브코더다. 코딩 지식을 전제하지 않고, 전문 용어에는 항상 쉬운 설명을 붙인다.

**외부 데이터는 검토 후 사용** — api_mcp/rag 결과를 그대로 최종 출력에 넣으면 잘못된 정보가 전달될 수 있다. review 단계를 거쳐야 한다.

**Codex 네이티브** — 만드는 스킬도, 이 스킬 자신도 SKILL.md + references/scripts/assets로 동작한다. 존재하지 않는 도구(다른 하네스 전용 객관식 카드 도구, 슬래시 커맨드 폴더, 에이전트 로스터 폴더)를 가정하지 않는다. 객관식 질문은 §A 질문 도구로 한다.

---

## References

상세 내용은 아래 파일에서 확인하세요 (progressive disclosure):

### 작성 가이드
- **`references/writing-style-guide.md`** — SKILL.md 작성 규칙 (imperative form, description 품질, concise 원칙, 규율형 스킬 합리화 차단)
- **`references/trigger-mechanism.md`** — 스킬 트리거 메커니즘, undertrigger 방지, pushy description 전략
- **`references/improvement-principles.md`** — 반복 개선 원칙 (일반화, lean 유지, why 설명, 반복 코드 번들)

### Eval & 검증
- **`references/eval-guide.md`** — Eval 방법론 (시나리오 정의, 자동 검증, 자동 수정 규칙)
- **`references/schemas.md`** — evals.json, grading.json, benchmark.json 스키마 정의
- **`references/agents/grader.md`** — assertion 채점 에이전트 프롬프트
- **`references/agents/comparator.md`** — 블라인드 A/B 비교 에이전트 프롬프트
- **`references/agents/analyzer.md`** — 벤치마크 분석 에이전트 프롬프트

### 설계 가이드
- **`references/interview-guide.md`** — 인터뷰 방법론 + 페르소나 에이전트 설계 + §A 질문 렌더링 규칙(질문 도구 우선, 번호 블록 폴백)
- **`references/personas.md`** — 4 페르소나 동적 생성 절차 + 참고 예시
- **`references/workflow-step-types.md`** — 6가지 단계 타입 상세 설명과 선택 기준
- **`references/component-type-decision.md`** — 스킬 / 스킬 + 임베드 sub-agent / 플러그인 패키지 판단 기준 트리
- **`references/mcp-catalog.md`** — MCP 서버 카탈로그 (전문가 에이전트 MCP 추천용)
- **`references/agent-templates.md`** — sub-agent 프롬프트 파일 생성 시 품질 기준과 표준 구조 가이드

### 스크립트 & 도구
- **`scripts/`** — verify-skill.py (품질 검증), verify_agent.py (에이전트 파일 검증), aggregate_benchmark.py (벤치마크 집계), package_skill.py (패키징), quick_validate.py (구조 검증, PyYAML 필요), utils.py (SKILL.md 파서)
- **`assets/eval-viewer/`** — eval 결과 브라우저 뷰어 (generate_review.py + viewer.html)
- **`assets/eval_review.html`** — description 최적화용 eval 쿼리 리뷰 템플릿
- **`references/script-templates.md`** — Python/Bash 스크립트 템플릿 모음
- **`references/api-mcp-integration.md`** — API/MCP 연동 가이드와 예시
- **`$PLUGIN_ROOT/scripts/validate-skill.js`** — 플러그인 루트의 Node 기반 SKILL.md 검증기 (verify-skill.py 대안)
