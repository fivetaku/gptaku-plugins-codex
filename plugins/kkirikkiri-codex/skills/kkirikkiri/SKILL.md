---
name: kkirikkiri
description: Assemble and run a Codex-native agent team from one plain-language request. Interviews the user with 2-3 questions, proposes specialized agents synthesized from 7 archetypes + domain detail, then executes with a local lead plus bounded sidecar agents and shared memory in `.kkirikkiri/`. Use when the user explicitly wants delegation, a research/development/analysis/content/product team, or parallel sub-agent work. Korean triggers — 팀 만들어줘, 리서치 팀, 끼리끼리, 팀 구성해줘. English — build a team, research team, agent team, kkirikkiri.
---

# 끼리끼리 Team Builder for Codex

> 자연어 한마디 → 인터뷰 → 환경 스캔 → 팀 구성 → 실행 → 리포트

사용자의 자연어 요청을 받아 목적에 맞는 AI 에이전트 팀을 구성하고 실행한다. **이 문서는 참고 문서가 아니라 실행 지시서다.** Codex 채팅 환경에서 단계대로 실제 도구를 호출한다.

이 스킬은 사용자가 **명시적으로 위임/팀/병렬 작업**을 원할 때만 쓴다. 단순 답변이나 솔로 코드 수정이면 이 스킬을 쓰지 않는다.

## 먼저 읽기

- `references/presets.md` — 프리셋 + 인터뷰 질문 (Step 1 매칭에 필수)
- `references/interview-guide.md` — §A 번호 블록 + Elicitation 규칙(§2a/§2b/§2c)
- `references/shared-memory.md` — 공유 메모리 템플릿 + DEAD_ENDS
- `references/team-prompts.md` — archetype 7종 마스터 + Codex 스폰 메커니즘

## 필요할 때 읽기

- `references/subagent-synthesis.md` — 동적 합성 5단계 + 도메인 살 4종 (팀원 카드 합성 시)
- `references/coordination-protocols.md` — 적응형 척추 + 게이트 (대화형 팀 실행 시)
- `references/pm-frameworks.md` — product 프리셋 매칭 시 (PRD/OST/Strategy Canvas 등)
- `references/metaphor-guide.md` — 공식 용어 + 한글 병기 (사용자에게 보여줄 때)
- `references/validation-guide.md` — 방식 A/B/C (2라운드 보강 시)
- `references/output-guide.md` — 세션 요약·팀 저장·에이전트 저장 (Step 8)

---

## Codex 렌더링 규칙 — question prompt 대체 (`shared/questioning-policy.md §A`)

Codex CLI에는 question prompt 같은 객관식 카드 UI가 **없다.** 모든 결정 질문은 **채팅에 번호형 선택지 블록을 출력하고 사용자의 다음 자유 텍스트 답변을 읽는** §A 패턴으로 한다.

```text
(예시 프리뷰 — 구조화 정보를 보여줄 때만. 단순 선호 질문이면 생략)

질문: <한 줄 질문>
1. <추천안> — 무엇인지, 왜 좋은지, 트레이드오프
2. <대안> — 무엇인지, 트레이드오프
3. 문장으로 직접 적기
(여러 개 고를 수 있으면: "여러 개면 1,3처럼 적어주세요")
(모르면 1번으로 진행할게요)
```

- 추천안은 항상 **1번**. 마지막 선택지는 항상 "문장으로 직접 적기"(자유 텍스트 escape).
- "잘 모르겠어요"는 별도 선택지로 만들지 말고 "모르면 1번으로 진행할게요" 문장으로 안내.
- **kkirikkiri는 Elicitation 유형이다.** 첫 표면 답에서 끊지 마라(§2a). 사용자가 deflect하면 다음 질문을 반드시 **구체/과거행동 앵커**로(§2b, 예: "최근에 이걸 직접 해봤다면 그때 뭐가 제일 막혔어요?"). 반대로 요청이 이미 충분히 구체적이거나 직접 팀을 원하면 과잉질문 없이 즉시 진행(§2c).

---

## 워크플로우 개요

```
Step 1:   의도 파악 + 프리셋 매칭
Step 2:   환경 스캔 (병렬)
Step 3:   인터뷰 (§A 번호 블록, Elicitation §2a/§2b)
Step 3.5: 실행 방식 선택 (§A) — 대화형 팀 vs batch(결정론 병렬)
   ├─ [대화형 팀 경로]                       ├─ [batch 경로]
Step 4:   동적 팀 구성 (archetype + 합성)      Step 4-B: 결정론 파이프라인 설계
Step 5:   팀 구성 제안 + 유저 확인              (확인은 실행 직전 한 줄 안내가 대신)
Step 6:   공유 메모리 + 팀원 스폰 + 실행        Step 6-B: 라운드별 병렬 스폰 실행
Step 7:   검증 루프 (방식 A/B/C, 최대 3R)       Step 7-B: 스테이지 내 adversarial-verify
Step 8:   결과 수집 + 리포트                    Step 8-B: 반환값 리포트
```

### 핵심 운영 원칙
1. **기억 외부화**: 중요한 결정은 반드시 `.kkirikkiri/` 파일에 기록 (대화형 팀 경로 — batch는 스크립트 변수가 이 역할).
2. **심부름꾼 패턴**: 팀원은 필요하면 사이드카(`spawn_agent`)를 스폰하여 병렬 작업.
3. **검증 루프**: 대화형 팀은 방식 A/B/C, batch는 스테이지 내 adversarial-verify(refute).
4. **build ≠ review family**: 만든 모델과 검토하는 모델은 다른 family가 기본 (로컬 → Codex CLI → agy → 로컬 Opus 적대 인스턴스 폴백).
5. **팀장은 로컬에 유지**: critical path를 워커에게 넘기지 않는다.

---

## Step 1: 의도 파악 + 프리셋 매칭

`references/presets.md`의 키워드로 프리셋을 매칭한다 (research / development / analysis / content / product / generic).
- 입력에서 각 프리셋 키워드 매칭 횟수를 세고 가장 많이 매칭된 것 선택. 동점이면 문맥 판단. 실패 시 generic.
- 문맥 주의: "경쟁사 분석"=research, "코드 분석"=analysis, "분석+PRD"=product. "기획"/"전략"=product 강매칭.

**파일 모드** (`@파일명` 또는 경로 포함 시): 해당 파일을 Read → 역할 자동 분해 (스킬 파일 → 단계별 역할, 에이전트 파일 → 팀원 포함, 일반 문서 → 목표로 프리셋 매칭). 인터뷰는 1-2개로 축소.

---

## Step 2: 환경 스캔 (병렬)

인터뷰와 병렬로 환경을 스캔한다:
```bash
python3 "$PLUGIN_ROOT/skills/kkirikkiri/scripts/scan_environment.py" --root "$PWD"
```
추가 확인 (스크립트가 못 잡는 항목은 직접):
- 외부 AI CLI: `codex`(코드·대규모 분석, cross-model 검토 1순위) / `agy`(디자인·UI, Gemini CLI 후속) / `gjc`(멀티모델 코드·교차검토)
- 개발 도구: `gh`, `npm`, `bun`, `pnpm`
- 기존 에이전트: `.codex/agents/*.md` 또는 `~/.codex/agents/*.md` — description/recommended-for로 동적 매칭 (파일명으로 매칭 금지)
- MCP: `perplexity` 류 도구 있으면 Researcher에 배정

스캔 결과(내부 변수): `codex_cli`, `antigravity_cli(agy)`, `gjc_cli`, `gh_cli`, `package_manager`, `existing_agents`, `perplexity_mcp`.

### 기존 에이전트 동적 매칭 (우선순위)
1. `recommended-for: {프리셋 id}` 일치 → 무조건 매칭
2. `agent_match_keywords`(presets.md)와 description 키워드 2개 이상 겹침 → 매칭
3. 위 둘 실패 → description과 팀 목표의 의미적 관련성으로 판단
매칭된 에이전트는 "기존에 설정된 전문가"로 팀에 우선 제안하고 사용자 확인.

---

## Step 3: 인터뷰 (§A 번호 블록)

> 진입 즉시: `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/interview-guide.md")` + (PM 매칭 시) `references/pm-frameworks.md`.

presets.md의 프리셋별 인터뷰 질문을 §A 번호 블록으로 채팅에 출력한다 (question prompt 없음).

규칙:
1. **Q1(열린 질문)은 사용자가 이미 자연어로 답했으면 생략 가능.** Q2/Q3는 §2c 신호(이미 구체적/직접 요청)가 없으면 진행.
2. 질문 최대 3개. 4개 초과 금지.
3. **§2a 조기 종료 금지**: 첫 표면/예의/회피성 답을 결론으로 채택하지 마라. 진짜 잡이 본인 발화로 확인될 때까지 이어간다.
4. **§2b 회피 대응**: deflect 감지 시 다음 질문을 반드시 **구체/과거행동 앵커**로 (또 다른 추상 질문 금지). 최대 3 탐침.
5. **§2c 과잉질문 가드**: 요청이 이미 충분히 구체적이거나 직접 팀을 명시적으로 원하면 추가 질문 없이 기본값만 확인하고 진행.
6. 용어는 공식 명칭(Opus, Sonnet, Codex 등)을 그대로 쓰되 한글 설명 병기. 내부 구현(spawn_agent, 파일 경로)은 노출 금지.
7. generic 프리셋이면 Q1으로 목표 파악 → Q2로 유형 선택 → 해당 프리셋 인터뷰 이어서.

답변을 받으면 **즉시 Step 3.5로 진행한다.** 응답 요약만 출력하고 멈추는 것은 워크플로우 위반.

---

## Step 3.5: 실행 방식 선택 (substrate 분기)

**원칙: 임의로 정하지 않는다. 사용자가 §A 번호 블록으로 직접 고른다.**

Codex에서 두 substrate의 실제 의미:
- **대화형 팀**: 로컬 lead(이 Codex 세션)가 적응형 척추로 직접 구동하고, 필요할 때 bounded 사이드카(`spawn_agent`)를 스폰·정독·재지시. 공유 메모리 + 검증 루프(방식 A/B/C). 설계 결정·깊은 검토·비평·수렴에 강함.
- **batch(결정론 병렬)**: 라운드별로 다수의 독립 사이드카를 병렬 스폰해 결정론 파이프라인처럼 돌리고, 스테이지 내 adversarial-verify로 검증. 공유 메모리/도메인 카드 인프라는 만들지 않고 중간 결과는 변수에 보관. 대량·독립·다수 소스 교차검증·감사·마이그레이션에 강함.

추천 휴리스틱:
| 신호 | 추천 |
|---|---|
| 수렴·관점충돌·설계결정·적대적 리뷰·트레이드오프 / "결정해줘"·"검토·비평해줘" / 프리셋 product·analysis | **대화형 팀** |
| 독립·대량·결정론 / "전부·모든·N개" / 감사·마이그레이션·다수 소스 교차검증 / 프리셋 research·대규모 development | **batch** |
| 애매하면 | 대화형 팀 (소규모 안전 기본값). 명백히 대량이면 batch |

§A 블록 (추천 옵션을 1번에):
```
이 작업을 어떤 방식으로 진행할까요?
1. 대화형 팀 (실시간 협업) — 팀원들이 의견을 주고받으며 수렴해요. 설계 결정·깊은 검토·비평에 강해요. (추천: <위 휴리스틱>)
2. batch (대량 자동 병렬 처리) — 수십 개 작업을 병렬로 돌리고 교차 검증해요. 대량 리서치·감사·일괄 작업에 강해요.
(모르면 1번으로 진행할게요)
```
- "대화형 팀" → Step 4 / "batch" → Step 4-B.

---

## Step 4: 동적 팀 구성 (대화형 팀 경로)

> 진입 즉시: `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/subagent-synthesis.md")` + `references/team-prompts.md`.

인터뷰 답변 + 환경 스캔을 종합해 최종 팀을 구성한다.

### 구성 프로세스
1. **프리셋 기본 구성**에서 시작 (presets.md).
2. **인터뷰로 조정**: 리서치 "깊고 포괄적" → 확장(4-5명) / 개발 "테스트도" → Tester(Critic) 추가 / 분석 여러 관점 → Explorer 세분화.
3. **환경으로 조정**: Codex CLI → 코드·대규모 분석 생산 또는 검증(Critic, cross-model 1순위) / agy → Designer / gjc → 코드 구현·분석 또는 Critic / Perplexity MCP → Researcher 도구 / gh → Builder.

### 팀원 합성 절차 (subagent-synthesis.md 5단계)
- **[4-A] 역할 분해**: 역할명 / 도메인 / 검증 방식(실행·출처·사용성·반박·데이터·전달·조율) / 출력 형태.
- **[4-B] archetype 매칭** (team-prompts.md 7종): Builder / Writer / Designer / Researcher / Analyst / Critic / Leader. 한 사람에 두 archetype 금지(분리 스폰). 모호 → Researcher 기본값. Critic 1 + Leader 1 권장.
- **[4-C] 도메인 살 4종 채집**: 정체성 / 스택·메서드(표 5-8행) / 실패 패턴(4-6) / KPI 실수치(3-5, 추상 금지). 채집은 LLM 자체 지식 우선 → 부족하면 1회 fetch 사이드카.

### 모델 티어 규칙 (절대 준수 — Codex 해석)
> "Opus 티어 / Sonnet 티어 / Haiku 티어"는 **역할의 판단 무게 분류**다. Codex 런타임은 `model: opus` 핀을 받지 않으므로, 그 무게를 archetype 본문 + 도메인 카드로 전달한다. (외부 CLI는 실제 모델 분리다.)

| 역할 | 티어 | 비고 |
|------|------|------|
| Lead (팀장) | **Opus 티어** | 무조건. 로컬 유지 |
| 분석·비평·최종 종합 / 핵심·고난도 구현 | **Opus 티어** | 판단이 걸린 역할 전부 |
| 일반 워커 (수집·쿼리·드래프트·간단 구현·표준 작업) | **Sonnet 티어** | 워커 기본값 — 적극 활용 |
| 기계적 글루 (수집·포맷·추출·진행요약·더미데이터) | **Haiku 티어** | 판단 0인 일만 |
| 코드·대규모 분석 (생산 + 검토) | **Codex CLI** | 다른 base 모델. 없으면 로컬 Opus 티어 폴백 |
| 디자인/UI | **Antigravity CLI(agy)** | 없으면 로컬 Sonnet 티어 폴백 |
| 코드 구현·분석 + 교차검토 | **gajae-code(gjc)** | 없으면 Codex/로컬 폴백 |

**검토자 폴백 체인 (build와 다른 family):** Codex 있음 → Codex / 없고 agy 있음 → agy / 둘 다 없음 → 로컬 Opus 적대 검토 인스턴스(별도 컨텍스트 + *"결함을 찾아라(refute)"* 프롬프트, rubber-stamp 금지).

### 팀장 R&R (절대 준수)
팀장은 코드를 짜지 않고 / 직접 검색하지 않고 / 직접 문서를 작성하지 않는다. **계획·태스크 분배·결과 검증·최종 통합**만. 팀장이 직접 작업하면 R&R 위반.

### CLI 없을 때 폴백
외부 CLI가 없으면 사용자에게 안내(기술 용어 없이) → 거절 시 로컬(Opus/Sonnet 티어)로 대체, 수락 시 설치 안내 후 재스캔.

---

## Step 4-B: 결정론 파이프라인 설계 (batch 경로)

> 공유 메모리·도메인 카드는 **만들지 않는다** — 중간 결과는 변수에 보관.

라운드별 병렬 사이드카 파이프라인을 설계한다:
1. **스테이지 설계**: 기본 순차 라운드 (수집 → 검증 → 종합). 각 라운드 안에서는 독립 항목을 병렬 `spawn_agent`.
2. **adversarial-verify 스테이지 필수**: 종합 전, 독립 검증 사이드카가 *"이 발견을 반박하라(refute). 확신 없으면 refuted=true"* 프롬프트로 교차 검증. 구조화 반환(JSON 스키마)을 강제해 파싱 불확실성 제거.
3. **티어 가이드**: 팬아웃되는 수집·드래프트·검증(refute) = Sonnet 티어 / 기계적 포맷·추출 = Haiku 티어 / 종합·우선순위·최종 합성 = Opus 티어 (라운드당 1~2회). 검증 스테이지도 Sonnet 티어 (물량은 팬아웃에 비례).

골격:
```
[수집]  독립 소스마다 spawn_agent("explorer", "[조사 지시] {source} → JSON 스키마")  // 병렬
[검증]  발견마다 spawn_agent("reviewer", "다음 발견을 반박하라(refute)... {finding}")  // 병렬
[종합]  로컬에서 검증 통과 결과만 종합 리포트로
```

설계 완료 → **Step 5를 건너뛰고 즉시 Step 6-B로.** 사용자에게 한 줄 안내:
```
대량 병렬 처리로 구성했어요. 백그라운드로 돌리고 완료되면 정리해서 보여드릴게요.
```

---

## Step 5: 팀 구성 제안 + 유저 확인 (대화형 팀 경로)

최종 팀 구성을 일반 텍스트 트리로 출력하고 §A 번호 블록으로 확인을 받는다.

```
이렇게 팀을 구성할게요:

📋 목표: [인터뷰에서 파악한 목표]

팀 구성:
├── 팀장 — [역할 설명] (Opus — 가장 똑똑한 모델, 로컬)
├── [역할명 1] — [역할 설명] (Sonnet — 균형형 모델)
├── [역할명 2] — [역할 설명] (Sonnet — 균형형 모델)
└── (선택) [외부 CLI] — [역할 설명] (백그라운드)

작업 방식: 팀장이 계획·배분 → 팀원 병렬 작업 → 팀장이 검증·통합 → 최종 리포트
⏱️ 예상 소요: [기본 3명 10-15분 / 확장 4-5명 15-25분 / 외부 CLI +5-10분]

이대로 진행할까요?
1. 네, 시작해주세요 (추천)
2. 팀원을 조정하고 싶어요
3. 처음부터 다시
(모르면 1번으로 진행할게요)
```

표기: 공식 용어 + 한글 설명 병기(`Opus (가장 똑똑한 모델)`). 내부 구현(spawn_agent, 파일 경로)은 비노출. 설명 없이 용어만 던지지 않는다.

응답 처리:
- "네, 시작해주세요" → 즉시 Step 6 (team_name 생성 + 공유 메모리 초기화 + 도메인 카드 + 스폰).
- "조정하고 싶어요" → 어떤 부분을 바꿀지 §A로 묻고 Step 4 재실행.
- "처음부터 다시" → Step 1로 복귀.

---

## Step 6: 공유 메모리 + 팀원 스폰 + 실행 (대화형 팀 경로)

> 진입 즉시: `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/coordination-protocols.md")` (적응형 척추 + 게이트).
> Agent Teams는 항상 능동 코디네이션. 대량·독립·결정론은 Step 3.5에서 이미 batch로 분기됨.

### 6-1. team_name + 디렉토리
```bash
RAND4=$(openssl rand -hex 2 2>/dev/null || printf '%04x' $((RANDOM % 65536)))
team_name="kkirikkiri-{preset}-$(date +%Y%m%d-%H%M)-${RAND4}"   # 예: kkirikkiri-research-20260620-1430-a3f2
mkdir -p ".kkirikkiri/teams/${team_name}/agents" ".kkirikkiri/teams/${team_name}/archive" ".kkirikkiri/shared/saved-teams"
```
사용자에게 세션 핸들(team_name + 작업 디렉토리) 안내.

### 6-2. 공유 메모리 초기화 (기억 외부화)
> 진입 즉시: `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/shared-memory.md")`.

shared-memory.md 템플릿으로 3종 파일을 Write (DEAD_ENDS 섹션 포함). 세 파일 완료 확인 후에만 다음으로. 미초기화 상태에서 스폰 금지(컨텍스트 손실 시 복구 불가).
```
.kkirikkiri/teams/{team_name}/TEAM_PLAN.md      (팀 목표·구성·태스크 분배)
.kkirikkiri/teams/{team_name}/TEAM_PROGRESS.md  (빈 진행 로그)
.kkirikkiri/teams/{team_name}/TEAM_FINDINGS.md  (빈 발견 + DEAD_ENDS)
```

### 6-2.5. 도메인 카드 합성 (archetype + 4종 살)
팀원 스폰 전, 각 팀원의 도메인 카드를 `.kkirikkiri/teams/{team_name}/agents/{역할명}.md`에 합성 저장 (100~150줄). 절차/few-shot은 `subagent-synthesis.md` [3][4]. 도메인 살 4종(정체성·스택·실패패턴·KPI 실수치) 중 하나라도 빠지면 일반론으로 빠진다.

### 6-3. 팀원 스폰
각 팀원을 `spawn_agent`로 스폰한다. 프롬프트에는 **archetype 본문 경로 + 도메인 카드 경로 + 첫 태스크 + 공유 메모리 경로**만 (카드/archetype 본문 자체를 복붙하지 않음). 메커니즘 상세는 team-prompts.md "Codex 스폰 메커니즘".
```
spawn_agent({
  agent_type: "explorer",   // Researcher/Analyst→explorer, Builder/Writer/Designer→worker, Critic→reviewer
  prompt: `
당신은 [역할명]입니다. ([archetype] + [도메인])
## 1. 마스터 행동 원칙
Read("$PLUGIN_ROOT/skills/kkirikkiri/references/team-prompts.md") 의 "# [archetype]" 섹션을 읽고 내재화.
## 2. 도메인 카드
Read(".kkirikkiri/teams/{team_name}/agents/{역할명}.md")
## 3. 첫 태스크
[구체적 지시]
## 4. 공유 메모리
- .kkirikkiri/teams/{team_name}/TEAM_PLAN.md / TEAM_PROGRESS.md / TEAM_FINDINGS.md
## 5. 팀 정보
- 팀장: [leader] (로컬) / 다른 팀원: [목록]
`
})
```
**팀장은 스폰하지 않는다 — 로컬(이 Codex 세션)이 팀장이다.** 팀장 R&R + 능동 코디네이션(coordination-protocols.md)을 내재화하고 직접 구동한다.

### 6-4. 외부 CLI 실행 (Codex/agy/gjc)
외부 CLI가 배정된 역할은 `$PLUGIN_ROOT/skills/kkirikkiri/scripts/`의 러너(있으면)나 직접 CLI 호출로 백그라운드 실행한다. `--provider`는 환경 스캔에서 확인된 것(`codex` | `antigravity` | `gjc`). 검토 역할이면 프롬프트를 **"검토해줘"가 아니라 "다음 산출물의 결함을 찾아 반박하라(refute)"**로. agy 1.0.x는 비-TTY stdout 버그가 있어 results가 비면 로컬 폴백. 결과는 TEAM_FINDINGS.md에 기록.

### 6-5. 능동 구동 (collect-at-end 금지)
팀장(로컬)은 사이드카 최종 노트가 도착할 때마다 정독 → 검증/모순/공백 판단 → 다음 수(재지시 / 교차검증 위임 / 런타임 전문가 스폰)를 결정한다. fire-and-forget 금지. 갈림길(비가역·가치충돌)에서만 게이트(독립 의견 + 심판) 발동 — 상세는 coordination-protocols.md.

---

## Step 6-B: batch 실행 (batch 경로)

Step 4-B 파이프라인을 라운드별로 실행한다.
- 각 라운드: 독립 항목을 병렬 `spawn_agent`. 결과를 변수에 수집.
- adversarial-verify 라운드를 종합 전에 반드시 실행 (refute + JSON 스키마).
- 종합은 로컬에서 검증 통과 결과만으로.
- 스테이지 오류 → 해당 스테이지만 수정 후 재실행. TeamCreate·공유 메모리·도메인 카드는 만들지 않는다.
- 완료 → Step 8-B.

---

## Step 7: 검증 루프 (대화형 팀 경로)

> 1라운드로 끝내지 않는다. 품질이 충분할 때까지 반복(최대 3라운드).

### 7-1. 품질 판정 (1라운드 완료 후 — 항상 수행)
팀장(로컬)이 통합 전 공유 메모리 3개 파일을 전부 읽고 판정:
- 목표 달성도 / 완성도 / 정확성(출처·근거·테스트) / 일관성(팀원 간 모순).

### 7-2. 자동 판정 → 방식 결정
```
목표달성 FAIL → 방식 B (전체 재구성)
일관성 FAIL   → 방식 C (부분 교체)
완성도/정확성 FAIL → 방식 A (팀 유지 + 보강)
라운드 >= 3   → 중단, 최선 결과로 리포트
```

### 7-3. 사용자 확인 (§A)
```
(1라운드 결과 + 부족한 부분 설명) 보강할까요?
1. 네, 보강해주세요 (추천) — 부족한 부분 집중 보완. 시간 더 걸려요.
2. 이 정도면 괜찮아요 — 현재 결과를 최종 리포트로.
3. 처음부터 다시 — 팀 해산 후 새로 구성.
(모르면 1번으로 진행할게요)
```
- "보강" → `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/validation-guide.md")` 후 방식 A/B/C 실행.
- "괜찮아요" → Step 8.
- "처음부터" → Step 1.

### 7-4. 최대 라운드
최대 3라운드. 3라운드 후에도 부족하면 솔직하게 한계를 알리고 최선 결과로 리포트.

---

## Step 8: 결과 수집 + 리포트

### 8-1. 사이드카 정리 + 결과 전달
사이드카가 떠 있으면 종료. 사용자에게:
```
끼리끼리 팀 작업이 완료되었어요!
📋 팀: [구성 요약]  🎯 목표: [목표]  📄 결과: [리포트 경로]  🔄 라운드: [수]
[핵심 요약 2-3줄]
```

### 8-2. 세션 요약 + 저장 (선택)
> `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/output-guide.md")`.

- 세션 요약(무엇이 효과적이었고 왜)을 자연어로 출력 + TEAM_REPORT.md에 함께 남김.
- 팀 저장: §A로 물어 `.kkirikkiri/shared/saved-teams/{team_name}.md` 생성.
- 에이전트 저장: §A로 물어 잘 동작한 팀원을 `.codex/agents/{역할명}.md`로 정제 저장 (recommended-for 포함). 저장 절차/충돌 처리는 output-guide.md.
- 작업 기록(`.kkirikkiri/teams/{team_name}/`)은 유지 (나중에 참조). 사용자가 원하면 삭제.

### Step 8-B: batch 리포트
반환값을 8-1 형식으로 리포트하되 "팀 구성"을 "처리 규모(에이전트 수·스테이지)"로 대체. 같은 작업 반복 예정이면 파이프라인을 재사용할 수 있음을 안내. 세션 요약은 8-2와 동일.

---

## 에러 처리
- **팀원 무응답/저성과**: 1회 → 무시 / 2회 → 진행 확인 / 3회 → 해당 역할만 교체.
- **사이드카 결과 품질 낮음**: 팀원/팀장이 직접 보완 또는 다른 사이드카에 재지시.
- **CLI 실행 실패**: 로컬(Opus 티어)로 대체 (검토 역할이면 로컬 Opus 적대 인스턴스). 사용자에겐 기술 에러 그대로 노출 금지 — "외부 도구 문제로 내부 AI로 대체했어요" 수준.
- **인터뷰 중단**: 즉시 종료, 팀 생성하지 않음. "언제든 다시 시작할 수 있어요."

---

## 절대 하지 마
- [ ] 유저 확인 없이 팀을 생성하지 마 (batch는 실행 직전 한 줄 안내가 이 역할)
- [ ] Step 3.5 사용자 선택 없이 substrate를 임의로 정하지 마
- [ ] 프리셋을 고정값으로 쓰지 마 — 인터뷰 + 환경스캔으로 동적 조정
- [ ] 공식 용어(Opus/Sonnet/Codex/agy/gjc)를 메타포로 대체하지 마 — 그대로 쓰고 한글 병기. 내부 구현(spawn_agent/파일 경로)만 비노출
- [ ] question prompt 카드를 가정하지 마 — Codex엔 없다. §A 번호 블록만
- [ ] **첫 표면/회피 답을 진짜 니즈로 채택하지 마 (§2a). deflect엔 구체/과거행동 앵커로 (§2b)**
- [ ] 이미 구체적인 요청에 과잉질문하지 마 (§2c)
- [ ] 인터뷰 질문 4개 이상 하지 마
- [ ] Haiku 티어를 판단이 필요한 역할에 배정하지 마 — 기계적 글루 한정
- [ ] 같은 family끼리의 형식적 검토를 기본으로 삼지 마 — Codex→agy→로컬 Opus 적대. 폴백일 땐 refute 프롬프트
- [ ] 팀장에게 코드/검색/문서 작성을 시키지 마 (최종 통합 리포트만 예외)
- [ ] 팀장을 스폰하지 마 — 로컬이 팀장
- [ ] 공유 메모리 초기화 없이 팀원을 스폰하지 마
- [ ] 팀원 프롬프트에서 공유 메모리 경로를 빠뜨리지 마
- [ ] 사이드카를 fire-and-forget 하지 마 — 중간 산출 정독 + 재지시
- [ ] 검증 없이 결과를 유저에게 전달하지 마
- [ ] 4라운드 이상 반복하지 마 — 최대 3라운드
- [ ] 도메인 카드를 archetype 본문 복붙으로 채우지 마 — archetype은 team-prompts.md, 카드는 도메인 살 4종
- [ ] 도메인 살 4종 중 하나라도 빠뜨리지 마
- [ ] 한 팀원에게 두 archetype을 강제하지 마 — 분리 스폰
- [ ] LLM 자체 지식으로 합성 가능한데 외부 fetch부터 하지 마

## 항상 해
- [ ] 모든 §A 번호 블록에 "(추천)" 1번 옵션 + "모르면 1번으로" 안내 + "문장으로 직접 적기" escape
- [ ] 팀 구성 제안 시 역할을 일상 용어로 설명 + 공식 용어 한글 병기 + 예상 소요시간
- [ ] 팀 실행 전 유저 확인 (batch는 실행 직전 안내)
- [ ] 환경 스캔에서 실행 substrate 가용성 + Codex/agy/gjc + 기존 에이전트 확인
- [ ] batch 파이프라인에 adversarial-verify(refute) 스테이지 포함
- [ ] 프리셋 매칭 실패 시 generic 인터뷰로 전환
- [ ] 팀 생성 직후 공유 메모리 3종 초기화 (DEAD_ENDS 포함)
- [ ] 팀원 스폰 전 도메인 카드 합성 (archetype + 4종 살, 100~150줄)
- [ ] 팀원 프롬프트에 archetype 본문 경로 + 도메인 카드 경로 둘 다 포함
- [ ] 팀장 R&R + 능동 코디네이션 내재화 (collect-at-end 금지)
- [ ] 1라운드 완료 후 반드시 품질 판정 (목표/완성도/정확성/일관성)
- [ ] 팀장의 최종 통합 전 공유 메모리 3개 파일 전부 읽기
- [ ] 기존 에이전트 발견 시 재활용 여부 사용자에게 확인
- [ ] 파일 모드(@파일명) 입력 시 파일 분석 → 역할 자동 분해
- [ ] 작업 완료 후 팀 저장 여부 사용자에게 확인
