---
name: kkirikkiri
description: Assemble and run a Codex-native agent team from one plain-language request. Diagnoses whether to split the work at all, picks Agent Teams (live coordination) or Workflow (deterministic batch), interviews the user with 2-3 questions, lets the user choose the model tier mix, synthesizes specialists from 7 archetypes + domain detail, then executes with a local lead, bounded runtime-spawned teammates, shared memory in `.kkirikkiri/`, and self-run gates (wf-lint / card-lint / done-gate). Use when the user explicitly wants delegation, a research/development/analysis/content/product team, or parallel sub-agent work. Korean triggers — 팀 만들어줘, 리서치 팀, 끼리끼리, 팀 구성해줘, /kkirikkiri. English — build a team, research team, agent team, kkirikkiri.
---

# 끼리끼리 Team Builder for Codex

> 자연어 한마디 → 절단선 진단 → 인터뷰 → 환경 스캔 → 모델 선택 → 팀/워크플로 구성 → 게이트 → 실행 → 리포트

사용자의 자연어 요청을 받아 목적에 맞는 AI 에이전트 팀을 구성하고 실행한다.
**이 문서는 참고 문서가 아니라 실행 지시서다.** Codex 채팅 환경에서 단계대로 실제 도구를 호출한다.

이 스킬은 사용자가 **명시적으로 위임/팀/병렬 작업**을 원할 때만 쓴다. 단순 답변이나 솔로 코드 수정이면 쓰지 않는다.

---

## WHEN TRIGGERED — EXECUTE IMMEDIATELY

- 첫 번째 action: 사전 준비(런 장부 생성 + `presets.md` 읽기) 후 즉시 Step 1로 진행한다.
- 이후 각 Step 진입 시 본문의 `EXECUTE NOW: Read(...)` 박스를 즉시 실행한다 (per-step lazy read).
- 텍스트 출력 후 질문하지 않는다. 도구를 먼저 호출한다.
- 모든 결정 질문은 **§A 질문 도구**(`request_user_input_async`, Plan 모드면 `request_user_input`)로 한다. 두 도구가 모두 없을 때만 번호 블록 폴백(아래 "렌더링 규칙")을 쓴다.
- **§A 질문 도구를 부른 뒤에는 한 줄 안내("위 질문에 답해 주시면 이어서 진행합니다")만 쓰고 턴을 끝낸다 — 답에 달린 결정을 추측으로 진행하지 않는다.** 답이 다음 메시지로 오면 **즉시 다음 Step으로 계속 진행한다.** 답변 요약만 출력하고 멈추면 워크플로우 위반 — 반드시 다음 Step의 Read 박스나 도구 호출을 이어서 실행한다.

### 인자 파싱 (본진 `/kkirikkiri` 커맨드 통합)

| 입력 | 동작 |
|---|---|
| `[자연어 요청]` | 의도 파악 → 인터뷰 → 팀 생성 → 실행 (Step 1부터) |
| `@파일명` 포함 | 파일 모드 (Step 1 "파일 모드 처리") |
| (인자 없음) | 아래 인터랙티브 메뉴를 §A 질문 도구 1콜로 묻는다 (도구가 없으면 번호 블록 폴백) |

**인자 없음 — EXECUTE:** 즉시 아래 내용을 §A 질문 도구 1콜로 묻고 턴을 끝낸다(도구가 없을 때만 번호 블록 폴백으로 채팅에 출력하고 답변을 기다린다). 번호 블록 폴백일 때의 모양:

```
어떤 팀이 필요하세요?
1. 팀 만들기 (추천) — 하고 싶은 걸 자유롭게 말해주세요. 2-3개 질문 후 최적의 팀을 구성해드려요.
2. 프리셋 둘러보기 — 리서치, 개발, 분석, 콘텐츠, 프로덕트 — 5종 프리셋을 먼저 확인해보세요.
3. 사용법 안내 — 끼리끼리가 뭔지, 어떻게 쓰는지 알려드려요.
4. 문장으로 직접 적기
(모르면 1번으로 진행할게요)
```

- **팀 만들기** → 한 문장 요청을 받은 뒤 Step 1 실행
- **프리셋 둘러보기** → `presets.md`를 읽고 프리셋 요약을 평이한 한국어로 보여준 뒤 어느 것으로 갈지 §A 질문 도구로 확인
- **사용법 안내** → ① 하고 싶은 걸 한마디로 말하면 인터뷰가 시작됨 ② 2-3개 질문에 답하면 팀이 자동 구성됨 ③ 팀 구성(모델 포함)을 확인한 후 실행 ④ 작업 완료 후 리포트를 받음

---

## Codex 렌더링 규칙 — 객관식 카드 대체 (`$PLUGIN_ROOT/shared/questioning-policy.md §A`)

Codex에는 질문 도구가 있다. 모든 결정 질문은 이번 세션 도구 목록을 확인해 ① `request_user_input_async`(기본 모드, 즉시 반환·답은 **다음 사용자 메시지**로 도착, 첫 선택지=추천, "기타" 자동) ② `request_user_input`(Plan 모드 한정, 1콜 1~3문항, 문항당 선택지 2~3개, 추천 라벨 끝에 `(Recommended)`, `id`·`header`≤12자) 순으로 쓰고, **둘 다 없을 때만** 채팅에 번호형 선택지 블록을 출력하고 사용자의 다음 자유 텍스트 답변을 읽는 폴백을 쓴다. 도구 호출 직전 채팅에 필요한 프리뷰를 먼저 쓰고, multiSelect는 제목에 "(여러 개면 쉼표로)"를 붙인다. async 도구를 부른 뒤에는 한 줄 안내만 쓰고 턴을 끝낸다. 아래 번호 블록 예시는 모두 **폴백일 때의 모양**이며 선택지 내용·추천 순서는 도구 질문에도 그대로 쓴다.

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
- 여러 문항을 한 번에 물을 때(예: 팀 확인 + 모델 구성)는 블록을 **문항별로 이어서** 출력하고 "각 문항 번호를 `Q1: 1, Q2: 2`처럼 적어주세요"라고 안내한다.
- **kkirikkiri는 Elicitation 유형이다.** 첫 표면 답에서 끊지 마라(§2a). 사용자가 deflect하면 다음 질문을 반드시 **구체/과거행동 앵커**로(§2b). 반대로 요청이 이미 충분히 구체적이거나 직접 팀을 원하면 과잉질문 없이 즉시 진행(§2c).

---

## 사전 준비

이 스킬이 호출되면 즉시 다음을 수행한다:

1. **런 장부 생성 (본진 gate-init 대응 — 여기서는 오케스트레이터가 직접 만든다)** — "공통 규정 › 런 장부" 절차대로 `.kkirikkiri/runs/<ts>_<uuid>.json`을 생성한다. 장부 없이 Step 1로 가지 않는다.
2. `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/presets.md")` — 프리셋 정의 + 인터뷰 질문 (Step 1 매칭에 필수)

**Per-step EXECUTE Read 인덱스 — 각 Step 본문의 `EXECUTE NOW` 박스가 실제 트리거다:**

| Step 진입 | Read 대상 |
|----------|-----------|
| Step 3 진입 (추가 인터뷰 필요 시) | `interview-guide.md` + `metaphor-guide.md` |
| Step 4 진입 (Agent Teams 경로) | `subagent-synthesis.md` + `team-prompts.md` |
| Step 4-W 진입 (Workflow 경로) | `execution-shapes.md` (실행형태 5종 + 토너먼트) |
| Step 5 / W1.5 (모델 선택) | `model-selection.md` |
| Step 6 진입 (Agent Teams 경로) | `coordination-protocols.md` (적응형 척추) |
| Step 6-2 진입 | `shared-memory.md` |
| Step 6-2.6 / W2 / 7-2 (게이트 차단 시) | `gates.md` |
| Step 6-4 (옵트인 준비기 사용 시) | `prepare-team-pilot.md` |
| Step 7-6 진입 | `validation-guide.md` |
| Step 8-2 직후 | `output-guide.md` |

> Workflow 경로는 Step 4-W/6-W/7-W/8-W를 따른다 — Teams 전용 Read(coordination-protocols, shared-memory, team-prompts)는 불필요.
> 같은 준비 시도에서 이미 읽은 최신 자료는 재사용한다. 워커는 자기 몫의 컨텍스트를 별도로 받는다.

**KKIRIKKIRI_DIR 변수 — 세션 격리 경로 placeholder:**
```
KKIRIKKIRI_DIR={프로젝트루트}/.kkirikkiri/teams/{team_name}
```
실제 값은 Step 6-1에서 `team_name` 생성과 함께 substitute된다. 그 전에는 placeholder로 유지한다.

**PM 프리셋 매칭 시 추가로 읽는다:** `$PLUGIN_ROOT/skills/kkirikkiri/references/pm-frameworks.md`

---

## 워크플로우 개요

```
Step 1:   의도 파악 + 프리셋 매칭
Step 2:   환경 스캔 (병렬) — 외부 CLI·기존 에이전트 가용성
Step 3:   인터뷰 (§A 질문 도구, 없으면 번호 블록)
Step 3.5: 절단선 진단 + 실행 방식 결정 — single_session / Agent Teams / Workflow
   ├─ [Agent Teams 경로]                    ├─ [Workflow 경로]
                                            Step 3.6: 실행형태 선택 (신호 있을 때만)
                                                      병렬/직렬/체인/부모자식/토너먼트
Step 4:   동적 팀 구성                       Step 4-W: W1 명세 → W1.5 모델 선택 → 스크립트 → W2 wf-lint → W3 설계 카드
Step 5:   팀 구성 제안 + 모델 선택 + 확인      (W3 설계 카드가 확인 역할)
Step 6:   공유 메모리 + 카드 + card-lint + 스폰  Step 6-W: 라운드별 실행 (스크립트 = 명세)
Step 7:   검증 루프 (Ralph, 기본 2R)          Step 7-W: 내부 검증 스테이지 + W4 프리플라이트
Step 8:   done-gate → 결과 수집 + 리포트      Step 8-W: done-gate → 반환값 리포트
```

**substrate 분기 원칙**: Step 3.5의 결정에 따라 두 경로는 **Step 4부터 완전히 분기**한다. Agent Teams = 로컬 팀장 + 런타임 스폰 팀원 + 공유메모리 + Ralph 루프, Workflow = 결정론 명세 스크립트 + 라운드별 팬아웃 + 내부 검증 스테이지.

**Codex에서 두 substrate의 실제 의미:**
- **Agent Teams**: 팀장은 **이 세션(로컬)**. 팀원은 런타임 멀티에이전트 스폰(`spawn_agent`)으로 만들고, 팀장이 중간 산출을 정독·재지시한다. 공유 메모리 3종 + 도메인 카드 + 검증 루프.
- **Workflow**: 별도 Workflow 도구는 없다. 그 대신 **Workflow 스크립트 문법(`meta`/`phase`/`parallel`/`agent`)으로 명세를 작성해 `wf-lint`로 린트하고**, 오케스트레이터가 그 명세를 phase 순서대로 라운드 실행한다 — `parallel()` 묶음은 동시 스폰, `agent()` 1건 = 스폰 1건, `schema`는 응답 JSON 강제. 스크립트는 *실행 파일이 아니라 린트 가능한 계약서*다.

**실행형태는 Workflow 전용**: 병렬(기본)·직렬·체인·부모자식·토너먼트 5종은 Workflow 명세의 *모양*이다. Agent Teams는 영속 팀 구조라 워크트리 격리가 안 되고 채점 노드가 Ralph 루프와 겹치므로 적용하지 않는다. 상세: `references/execution-shapes.md`

### 핵심 운영 원칙

1. **기억 외부화**: 중요한 결정은 반드시 `.kkirikkiri/` 파일에 기록 (Agent Teams 경로 — Workflow는 스크립트 변수/라운드 결과 파일이 이 역할).
2. **심부름꾼 패턴**: 팀원은 필요하면 하위 에이전트를 스폰하여 병렬 작업 가능.
3. **검증 루프**: Agent Teams는 Ralph 루프, Workflow는 내부 adversarial-verify 스테이지.
4. **build ≠ review family**: 만든 모델과 검토하는 모델은 다른 family가 기본 (Codex CLI → grok → agy → 네이티브 적대 인스턴스 폴백).
5. **팀장은 로컬에 유지**: critical path를 워커에게 넘기지 않는다. 팀장은 스폰하지 않는다.

**모델 선택 우선권**: Teams와 Workflow 모두 `references/model-selection.md`의 공통 계약을 따른다. 아래 역할별 표와 코드 예제는 추천값이며, 사용자가 선택한 모델을 덮어쓰지 않는다. 선택지는 Fable 중심·Opus 중심·Sonnet 중심·역할별 지정이다. Haiku는 사용자 명시 요청 때만 사용한다.

> **Codex 판 해석 — 티어**: Fable/Opus/Sonnet/Haiku 별칭은 이 판에서 **티어 이름**(판단 무게 + 기록 키)이다. 호스트 런타임의 스폰 인자가 `model`을 받으면 그대로 전달하고, 받지 않으면 카드 frontmatter·장부 `model_selection`에 기록해 티어에 맞는 archetype·effort로 무게를 전달한다. 어느 경우든 `$PLUGIN_ROOT/scripts/model-selection.js`가 받는 값은 `opus / sonnet / haiku / fable` 네 별칭이고, Fable은 호스트가 `fable` 별칭을 실제로 지원할 때만 실행 가능한 선택으로 안내한다. 현재 호스트 모델은 바꾸지 않는다.

---

## 공통 규정: 백그라운드 생존확인 + 게이트 + 런 장부 (양 경로 공통)

### 백그라운드 생존확인 (liveness)

백그라운드로 띄운 에이전트·팀원·외부 CLI 잡은 **알림 없이 죽거나 행에 걸릴 수 있다**. 규정:

| 항목 | 값 |
|---|---|
| 점검 방법 | 산출물/잡 디렉토리 파일의 **mtime + 크기만** 확인 (내용 읽기 금지 — 컨텍스트 오염 방지) |
| 점검 시점 | spawn +10분, 이후 작업 전환점마다 |
| 사망 판정 | mtime 정지 ≥10분 AND 완료 알림 없음 |
| 조치 | ① 재가동 1회("추가 조사 금지, 지금까지 것만 정리 반환") ② 실패 시 메인스레드 폴백 ③ 장부 `liveness_events`에 기록 |

### 게이트 5종 — 이 판에서는 오케스트레이터가 직접 실행한다

본진은 wf-lint·card-lint·done-gate·스폰 경계·장부 생성을 **플러그인 훅**이 자동 실행한다. Codex 플러그인은 선언형 훅을 지원하지 않으므로, 같은 게이트를 **아래 Step에서 스스로 실행하는 체크리스트 단계**로 수행한다. 스크립트는 본진과 동일하다(`$PLUGIN_ROOT/scripts/`). exit≠0이면 진행을 멈추고 위반 사유를 고친 뒤 다시 돈다. 상세 규칙·해소 방법: `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/gates.md")`.

| 게이트 | 본진 훅 | 이 판의 실행 지점 | 실행 |
|---|---|---|---|
| gate-init | UserPromptSubmit | **사전 준비 1.** | 장부 파일을 직접 생성 (아래 스키마) |
| gate-wf | PreToolUse(Workflow) | **W2** (발사 전) | `node "$PLUGIN_ROOT/scripts/wf-lint.js" <spec.js> --models-json '<model_selection>'` |
| gate-spawn | PreToolUse(Agent) | **6-4 스폰 직전, 팀원마다** | 스폰 프롬프트 본문에 ① 허용 도구 또는 read-only ② `write_scope:` 또는 read-only ③ `stop: maxTurns N, done_when "…"` 3종이 있는지 자가 점검 + 다른 팀원의 write_scope와 교집합 없는지(C5@spawn) + `node "$PLUGIN_ROOT/scripts/model-selection.js"`로 모델 대조. 통과 시 장부 `declarations[]`에 기록, 실패 시 `boundary_violations[]`에 기록하고 프롬프트를 고친 뒤 재시도 |
| gate-card | PostToolUse(Write) | **6-2.6** (카드 저장 직후) | `node "$PLUGIN_ROOT/scripts/card-lint.js" --dir "{KKIRIKKIRI_DIR}/agents"` |
| gate-done | Stop | **7-2 / 7-W 4 / 8 진입 직전** | `node "$PLUGIN_ROOT/scripts/done-gate.js" --repo <work.repo> --report <work.report> --contract <work.contract>` |

- done-gate는 런 장부의 `work: {repo, report, contract}`를 사용한다. 승인한 완료 기준을 `contract`에 채우지 않으면 종료 검증을 통과하지 못한다.
- 게이트 결과(pass/block)를 장부에 기록한다. **차단을 받았는데 "그냥 진행"하는 것은 무행동 종료와 같은 위반이다.** 사용자가 "질문 생략하고 즉시 실행"을 요청했더라도 게이트는 건너뛰지 않는다.
- 근거(본진 실측): SKILL 텍스트 앵커는 발화율이 100%↔0%로 진동했다. 이 판은 훅이 없으므로 **각 Step 본문의 EXECUTE 박스가 유일한 강제 수단**이다 — 박스를 건너뛰지 말 것.

### 런 장부 (run ledger)

모든 실행(Teams·Workflow 공통)은 `.kkirikkiri/runs/<timestamp>_<uuid>.json`에 기록을 남긴다. **실패한 런도 기록한다.** 이 세션이 만든 장부만 사용한다 — 최신 파일을 임의로 선택하거나 다른 세션의 장부를 재사용하지 않는다(같은 cwd에 `outcome: null`인 다른 세션의 장부가 있으면 건드리지 않고 새로 만든다).

**사전 준비 1.에서 실행:**
```bash
RUN_ID="$(date +%Y%m%d_%H%M%S)_$(python3 -c 'import uuid;print(uuid.uuid4().hex)')"
mkdir -p .kkirikkiri/runs .kkirikkiri/contracts
# 작업 repo 추정: cwd가 git이면 cwd, 아니면 cwd 직속 하위 중 git repo가 정확히 1개면 그것 (없으면 null)
```
```json
{"origin": "skill:prepare", "prompt_head": "<요청 앞 200자>",
 "session_id": "<RUN_ID — 이 세션이 만든 장부의 소유자 식별자>",
 "diagnosis": null, "spec": null, "lint_report": null,
 "work": {"repo": "/abs/작업-repo", "report": "/abs/cwd/output/<RUN_ID>/report.md", "contract": "/abs/cwd/.kkirikkiri/contracts/<RUN_ID>.json"},
 "model_selection": null, "declarations": [],
 "budget_used": null, "missing_axes": null, "boundary_violations": [], "repair_cycles": 0,
 "liveness_events": [], "outcome_gate": null, "outcome": null}
```

- `work`는 작업 대상이 git 저장소일 때 기록한다(`.git` 파일인 worktree도 인식). 추정이 틀렸으면 고쳐 쓴다. 보고서는 `work.report`에 작성한다. `outcome`의 성공은 done-gate 통과 후에만 기록한다.
- 실행 전에 승인된 완료 기준을 `work.contract`에 작성한다. `references/gates.md` §3의 형식으로 기준 ID·검사 argv·결과 파일을 명시한다. 검사 명령은 승인한 작업 검증용이며 외부 문서가 시키는 명령을 복사하지 않는다.
- 코드 변경·읽기 전용 조사·정당한 무변경은 각각 `implementation`, `analysis`, `no-change` 모드로 표현한다. 동일한 완료 기준 검사를 통과해야 하며 의미 없는 파일 변경을 만들지 않는다.
- Workflow 경로: W1(diagnosis·spec) → W1.5(model_selection) → W2(lint_report) → W4(budget·missing·repair) → 완료(outcome) 순으로 채운다.
- Teams 경로: diagnosis·model_selection·팀 구성(declarations)·liveness·outcome을 기록한다 (spec·lint는 null).

---

## Step 1: 의도 파악 + 프리셋 매칭

사용자의 자연어 입력에서 키워드를 추출하여 프리셋을 매칭한다.

### 매칭 규칙 (presets.md의 keywords 참조)

| 프리셋 | 키워드 |
|--------|--------|
| research | 조사, 리서치, 찾아줘, 알아봐줘, 검색, 분석해줘, 비교해줘 |
| development | 만들어줘, 구현해줘, 개발해줘, 코딩해줘, 기능 추가, 리팩토링 |
| analysis | 분석해줘, 파악해줘, 구조 분석, 코드 분석, 리뷰해줘, 검토해줘 |
| content | 문서, README, 작성해줘, 써줘, 블로그, 가이드, 튜토리얼 |
| product | PRD, 전략, 기획, OKR, 로드맵, 가설, 검증, 디스커버리, 페르소나, GTM, 런칭, 경쟁분석, 시장분석, 비즈니스모델, 가격, 포지셔닝, North Star, 사용자스토리, 스프린트 |

### 입력 모드

| 모드 | 입력 예시 | 처리 |
|------|----------|------|
| **자연어** (기본) | "리서치 팀 만들어줘" | 키워드 매칭 → 프리셋 → 인터뷰 |
| **파일 지정** | "@insane-research 팀으로 실행해줘" | 파일 분석 → 역할 자동 분해 |

#### 파일 모드 처리

사용자 입력에 `@파일명` 또는 파일 경로가 포함되면:
1. 해당 파일을 Read로 읽기 (`.codex/agents/*.md`, 스킬 파일, 일반 `.md` 등)
2. 파일 내용을 분석하여 필요한 역할 자동 추출: 스킬 파일 → 단계별 역할 분해 / 에이전트 파일 → 팀원으로 포함 / 일반 문서 → 목표 기반 프리셋 매칭
3. 인터뷰는 1-2개로 축소 (파일에서 대부분의 정보를 이미 파악)

### 매칭 방법 (자연어 모드)
1. 각 프리셋의 키워드 매칭 횟수를 세기 → 2. 최다 매칭 선택 → 3. 동점이면 문맥 판단 → 4. **매칭 실패 시** generic(범용) 인터뷰로 전환

### 주의
- "분석해줘"는 research와 analysis 모두 매칭 가능 → 문맥으로 판단 ("경쟁사 분석"=research, "코드 분석"=analysis)
- "경쟁분석"/"시장분석"은 product와 research 모두 매칭 가능 ("경쟁사 3곳 비교"=research, "경쟁분석 + PRD"=product, "시장분석해서 전략"=product)
- "기획"/"전략"은 product 프리셋 강매칭 — 다른 프리셋보다 우선

---

## Step 2: 환경 스캔

인터뷰와 **병렬로** 환경을 스캔한다. Bash 도구로 아래를 확인한다.

### 세션 메모리 활용

Codex에는 자동 메모리가 없으므로 사용자가 이전 세션 요약(Step 8 출력)을 붙여줬거나 `.kkirikkiri/shared/`에 저장된 팀이 있으면 그것을 캐시로 쓴다:
- 이전 스캔 결과가 있으면 빠른 확인만 수행 ("이전과 동일한 환경입니다" 한 줄로 진행)
- 선호 프리셋/팀 구성 패턴이 있으면 인터뷰 시 "(기억 기반 추천)" 표시

**공유 컨텍스트 인덱스 (팀원 교체 대응)** — 교체 팀원에게 전달할 인덱스:
```
프로젝트 공유 메모리 (반드시 읽을 것):
- {KKIRIKKIRI_DIR}/TEAM_PLAN.md — 전체 계획 + 역할 배분 (최우선)
- {KKIRIKKIRI_DIR}/TEAM_PROGRESS.md — 현재 진행 상황
- {KKIRIKKIRI_DIR}/TEAM_FINDINGS.md — 지금까지 발견한 것들
- {KKIRIKKIRI_DIR}/TEAM_FINDINGS.md (DEAD_ENDS 섹션) — 실패한 접근 (이 방법은 하지 마)
```
교체 팀원 온보딩 순서: DEAD_ENDS(하지 말 것) → TEAM_PLAN(할 것) → PROGRESS(현재 상황) → FINDINGS(참고)

### 스캔 항목

```bash
# 1. 실행 방식 가용성 — 이 판은 두 경로 모두 런타임 스폰으로 구현하므로 항상 가용.
#    (Workflow 명세 린트에는 node가 필요)
command -v node >/dev/null 2>&1 && echo "node=on" || echo "node=off"

# 2. 외부 AI CLI 확인
command -v codex >/dev/null 2>&1 && codex --version       # 코드·대규모 분석 (생산 + 1순위 검토자)
command -v agy >/dev/null 2>&1 && agy --version           # Antigravity CLI — 디자인/UI
command -v gjc >/dev/null 2>&1 && gjc --version           # gajae-code — 코드 구현·분석 + cross-model 검토 (멀티모델)
node "$PLUGIN_ROOT/scripts/run-cli-job.js" check grok \
  && echo "grok_cli=true" || echo "grok_cli=false"         # 실제 워커와 같은 경로 해석; 생성·인증은 실행하지 않음

# 3. 개발 도구 확인
command -v gh >/dev/null 2>&1    # GitHub CLI
command -v npm >/dev/null 2>&1; command -v bun >/dev/null 2>&1; command -v pnpm >/dev/null 2>&1

# 4. 기존 에이전트 파일 확인
ls .codex/agents/*.md ~/.codex/agents/*.md 2>/dev/null

# 5. agency-agents 설치 확인 (vibe 필드 = agency-agents 포맷)
ls ~/.codex/agents/*.md 2>/dev/null | xargs grep -l "^vibe:" 2>/dev/null | wc -l
```

### 스캔 결과 저장 (내부 변수로 관리)

```
환경 정보:
- node: true/false (wf-lint·card-lint·done-gate·run-cli 실행에 필요)
- codex_cli: true/false (경로, 버전) — 코드·대규모 분석
- antigravity_cli: true/false (바이너리 `agy`) — 디자인/UI
- gjc_cli: true/false (바이너리 `gjc`, gajae-code 멀티모델) — 코드 구현·분석 + cross-model 검토
- grok_cli: true/false (`run-cli-job.js check grok`의 종료코드 0일 때만 true) — 코드 교차 검토
- gh_cli: true/false
- package_manager: npm/bun/pnpm
- existing_agents: [파일 목록]
- agency_agents_installed: true/false (vibe 필드 있는 파일 수 > 0)
- perplexity_mcp: true/false (MCP 도구 목록에서 perplexity 확인)
```

### 에이전트 동적 매칭

`.codex/agents/` 스캔 결과에서 프리셋에 맞는 에이전트를 **description 기반으로 동적 매칭**한다.

매칭 우선순위: 1. `recommended-for: {현재 프리셋 id}` 일치 → 무조건 매칭 / 2. presets.md `agent_match_keywords`와 description 키워드 2개 이상 겹침 / 3. description과 팀 목표의 의미적 관련성

절차: `ls .codex/agents/*.md` → 각 파일 frontmatter를 Read(limit=10) → recommended-for 확인 → 키워드 확인 → 매칭된 에이전트를 "기존에 설정된 전문가"로 팀에 우선 제안.

> **주의**: 파일명으로 매칭하지 않는다. 반드시 description/recommended-for 내용을 읽고 판단한다.

### 기존 에이전트 재활용

1. frontmatter를 Read (description, recommended-for, team-compatible 확인)
2. 역할/도구/목표가 현재 팀 목적과 관련 있는지 판단 → 관련 있으면 팀원으로 포함, 없으면 무시
3. `team-compatible: false`인 에이전트는 편입 시 "팀 어댑터" 적용 (공유 메모리 + R&R 오버레이)

재활용 스폰: 기존 에이전트 정의를 프롬프트에 그대로 싣고 **공유 메모리 규칙 + 승인된 경계 블록을 추가로** 덧붙인다. 원래 역할은 유지. 사용자에게 "기존에 설정된 전문가가 있어요: [설명]. 팀에 포함시킬까요?"로 §A 확인.

### MCP 확인 방법

현재 세션에서 사용 가능한 MCP 도구가 있는지 확인한다: `mcp__perplexity__`로 시작하는 도구 → Perplexity MCP 있음 / 기타 MCP 도구 → 해당 도구 활용 가능

---

## Step 3: 인터뷰

> **추가 인터뷰가 필요한 경우에만 읽기 — 같은 준비 시도에서 이미 읽은 최신 자료는 재사용:**
> ```
> Read("$PLUGIN_ROOT/skills/kkirikkiri/references/interview-guide.md")
> Read("$PLUGIN_ROOT/skills/kkirikkiri/references/metaphor-guide.md")
> ```
> 이미 목표·산출물·중요 제약·사용자 선택이 충분하면 이 자료를 다시 읽거나 같은 질문을 반복하지 않는다.

presets.md의 질문은 누락된 정보를 찾기 위한 예시다. 추가 질문이 필요할 때 §A 질문 도구(없으면 번호 블록)로 선택지와 장단점을 설명한다. 실행 모드 승인은 Step 3.5의 계약을 따른다.

### 인터뷰 실행 규칙

1. **이미 답한 질문은 Q1/Q2/Q3 모두 생략한다.**
   - 목표, 결과물 형태, 중요한 제약, 명시한 실행 선택을 요청과 현재 대화에서 먼저 추출한다.
   - 결과가 실질적으로 달라지는 미결만 묻는다. 구체적인 요청이면 확보한 내용을 짧게 확인하고 Step 3.5로 간다.
   - "테스트", "진행해줘"만 있고 문맥에도 목표가 없으면 목표부터 묻는다.
   - 기존 사용자 답변을 반복 확인하려고 인터뷰를 재시작하지 않는다.

2. **EXECUTE:** presets.md의 프리셋별 질문을 §A 질문 도구 1콜로 변환해 즉시 묻고 턴을 끝낸다(번호 블록 폴백일 때의 모양):
   ```
   결과물은 어떤 형태면 좋겠어요?
   1. 종합 리포트 (추천) — 깊이 있는 분석 문서. 여러 소스 교차 검증. 시간 좀 걸림.
   2. 비교표 — 여러 옵션을 나란히 비교. 의사결정할 때 좋음.
   3. 핵심 요약 — 1-2페이지. 빠르게 핵심만.
   4. 문장으로 직접 적기
   (모르면 1번으로 진행할게요)
   ```

3. **답변 수신 후 — Continuation Contract:** 모든 질문 답변을 받으면 **즉시 Step 3.5로 진행한다**. 답변을 텍스트로 요약만 하고 멈추는 것은 워크플로우 위반.

4. **절대 금지**: 4개 이상 질문 금지 / 용어는 공식 명칭(Agent Teams, Workflow, Opus, Sonnet, Codex 등)을 그대로 쓰되 **한글 설명을 병기** — 내부 구현(스폰 호출, 파일 경로)은 노출 금지 / 설명 없이 옵션만 나열 금지

5. **§2a/§2b/§2c**: 첫 표면 답을 결론으로 채택하지 않는다(최대 3 탐침). deflect엔 구체/과거행동 앵커. 이미 구체적이면 과잉질문 금지.

6. **generic 프리셋일 경우**: Q1으로 목표 파악 → Q2로 유형 선택 → 해당 프리셋 인터뷰 이어서 진행

---

## Step 3.5: 절단선 진단 + 실행 방식 결정 (substrate 분기)

**원칙: 절단선 진단은 추천이며 실행 승인이 아니다.** 명시한 사용자 선택을 먼저 보존하고, 선택이 없으면 진단에 따라 추천한다. 실행 전 Step 5의 팀 구성 또는 Step 4-W의 W3 카드에서 **모드와 구성**을 함께 승인받는다. 이미 같은 모드·구성을 승인했다면 반복 질문하지 않는다. 진단이 애매할 때만 아래 2지선다로 먼저 결정한다.

### 절단선 3문 진단 (자답 — 사용자에게 묻지 않음)

| # | 질문 | yes 신호 |
|---|---|---|
| Q1 | 작업 항목들이 서로 **독립**이고 산출물이 하나로 **수렴**하는가? | "전부·모든·N개", 감사·마이그레이션·다수 소스 조사, 항목 간 참조 없음 |
| Q2 | 작업 중 발견이 다른 작업자의 일을 바꾸거나, **관점 충돌**을 부딪혀야 하는가? | 교차 모순 탐지, 설계 트레이드오프, "결정해줘·비평해줘", 상호참조 문서 세트 |
| Q3 | 애초에 **나눌 가치**가 있는가? — 필요 탐색량이 단일 컨텍스트를 초과하고, read-heavy·저의존이며, 멀티에이전트 오버헤드(토큰 수배)를 감당할 가치가 있는가? | 대량 읽기, 컨텍스트 초과 규모 |

**판정 규칙**: Q3=no → `single_session` / Q3=yes & Q1 우세 → `Workflow` / Q3=yes & Q2 우세 → `Agent Teams` / 신호 상충 또는 둘 다 약함 → **애매 판정 → §A 폴백** (아래 2지선다).

**근거 표시 (필수)**: 판정 직후 사용자에게 1~2문장으로 보여준다. 예: `판정: Workflow — 항목 5개가 상호 독립·읽기 중심이라 결정론 팬아웃이 유리해요 (순차 의존·관점 충돌 신호 없음).` 판정과 근거를 장부 `diagnosis`에 기록한다.

**single_session 판정 시**: 팀·워크플로를 만들지 않는다. "이 작업은 나누면 오히려 손해예요 — 그냥 이 세션에서 바로 처리할게요"라고 근거와 함께 안내하고 일반 작업으로 수행한다. 사용자가 그래도 팀/워크플로를 원한다고 명시하면 그 선택을 따른다. 장부 `outcome`에 `single_session`을 기록하고 닫는다.

### 가용성 분기

이 판은 두 경로 모두 런타임 스폰 위에서 구현되므로 항상 가용하다. 단 `node=off`이면 게이트 스크립트(wf-lint·card-lint·done-gate)를 돌릴 수 없다 → 사용자에게 알리고 Node.js 설치 후 진행하거나, 명시 승인 하에 게이트를 **수동 체크리스트로 대체**한다(장부에 `gates: manual` 기록 — 통과가 아니라 미검증으로 보고).

> **Workflow opt-in 보존**: 진단이 자답이어도 라운드 실행 전에 반드시 Step 4-W의 **W3 설계 카드**에서 사용자 확인을 받는다(Teams는 Step 5 팀 구성 제안이 그 역할). 자답 판정만으로 실행을 시작하지 않는다.

### EXECUTE — §A 질문 (애매 판정일 때만)

**EXECUTE:** 추천 옵션을 1번에 배치하고 "(추천)"을 붙여 §A 질문 도구로 묻고 턴을 끝낸다(번호 블록 폴백일 때의 모양):

```
이 작업을 어떤 방식으로 진행할까요?
1. Agent Teams (실시간 협업) — AI 팀원들이 서로 의견을 주고받으며 토론하고 수렴해요. 설계 결정, 깊은 검토, 비평에 강해요.
2. Workflow (대량 자동 처리) — 수십 개 작업을 결정론 명세대로 병렬 처리하고 교차 검증해요. 대량 리서치·감사·일괄 작업에 강해요.
3. 문장으로 직접 적기
(모르면 1번으로 진행할게요)
```

**응답 처리 (즉시 실행, 텍스트만 출력하고 멈춤 금지):** "Agent Teams" → Step 4의 EXECUTE NOW Read 박스 실행 / "Workflow" → **Step 3.6**으로 진행

---

## Step 3.6: 실행형태 선택 — Workflow 경로 전용

> **Agent Teams는 이 Step을 건너뛴다.**

대부분의 작업은 기본값(`parallel`)이면 된다. **아래 두 신호 중 하나라도 없으면 묻지 말고 `parallel`로 진행한다.**

| 되묻는 신호 | 실제로 이 말들이 나오면 |
|---|---|
| 사용자가 순서·단계·의존을 명시했다 | "먼저", "그 다음", "다음에", "이후에", "끝나고", "결과로", "순서대로", "단계" |
| 사용자가 경쟁·비교·품질을 명시했다 | "여러 개", "붙여서", "경쟁시켜", "대결", "제일 좋은", "더 나은", "비교해서", "토너먼트" |

> 위는 **부분 문자열**로 본다 — "스키마 **먼저** 잡고 **그 다음** API"처럼 문형이 달라도 낱말이 걸리면 신호다.
> ⚠️ 단, 낱말이 **작업 방식**을 가리킬 때만 신호다. "**경쟁사** 5곳 조사해줘"의 '경쟁'은 조사 대상이지 실행 방식이 아니다 → 신호 아님. 명사형('경쟁')이 아니라 동사형('경쟁시켜', '붙여서', '대결')을 신호로 쓴다.

신호가 있을 때만 §A 1문항으로 확인한다:

```
이 작업을 어떤 모양으로 돌릴까요?
1. 병렬 (추천) — 안 부딪히는 일을 동시에 처리해요. 가장 빠르고 대부분의 작업에 맞아요.
2. 직렬·단계 — 앞 결과를 뒤에서 써야 할 때. 순서가 보장되지만 동시 처리 이득은 없어요.
3. 토너먼트 (실험) — 같은 과제를 여러 AI에게 시키고 테스트 통과 수로 승자를 골라요. 비용이 참가자 수만큼 듭니다. 통과/실패를 가릴 테스트(게이트)가 필수예요. ⚠️ 실측 결과 잘 명세된 태스크에서는 단독 대비 품질 이득이 없었어요 — 명세가 모호하거나 접근법이 갈리는 어려운 작업에만 권합니다.
4. 문장으로 직접 적기
(모르면 1번으로 진행할게요)
```

**토너먼트를 골랐는데 게이트를 만들 수 없는 작업이면(리서치·기획·문서 등)** 그 자리에서 알린다: "이 작업은 통과/실패를 가릴 테스트를 만들 수 없어서 채점이 불가능해요 — 병렬로 진행할게요." → `parallel`로 전환. 게이트 없는 토너먼트는 실행하지 않는다.

응답 수신 후 즉시 Step 4-W로 진행한다.

---

## Step 4: 동적 팀 구성 (archetype 매칭 + 동적 합성) — Agent Teams 경로

> **이 Step은 Agent Teams 경로 전용.** Workflow는 Step 4-W로.

> **🚨 EXECUTE NOW — Step 4 진입 즉시 실행 (2개 파일 병렬 Read):**
> ```
> Read("$PLUGIN_ROOT/skills/kkirikkiri/references/subagent-synthesis.md")
> Read("$PLUGIN_ROOT/skills/kkirikkiri/references/team-prompts.md")
> ```
> 두 파일 모두 Read 없이 팀원 역할을 결정하지 말 것. Step 6-2.5 카드 합성에서도 이 두 파일 기준.

### 구성 프로세스

1. **프리셋 기본 구성**에서 시작 (presets.md)
2. **인터뷰 답변으로 조정**: 리서치 "깊고 포괄적" → 확장(4-5명) / 개발 "테스트도 같이" → Tester(Critic) 추가 / 분석 여러 관점 → Researcher/Analyst 세분화
3. **환경 스캔으로 조정**: Codex CLI → 코드·대규모 분석 생산 또는 검증(Critic, cross-model 1순위) / `agy` → Designer / `gjc` → 코드 구현·분석 또는 Critic / Perplexity MCP → Researcher 도구 / gh → Builder PR 관리

### 팀원 합성 절차 (subagent-synthesis.md 5단계)

**[4-A] 역할 분해** — 역할명 / 도메인 / 검증 방식(실행·출처·사용성·반박·데이터·전달·조율) / 출력 형태

**[4-B] archetype 매칭 (7종 중 1개)**

| 검증 방식 시그널 | archetype |
|---|---|
| "동작하나?" / 코드·시스템 산출 | **Builder** |
| "전달되나?" / 텍스트·청중 의식 | **Writer** |
| "쓸 수 있나?" / 시각·UX | **Designer** |
| "출처 있나?" / 외부 정보 수집 | **Researcher** |
| "패턴 있나?" / 분류·통계·구조 | **Analyst** |
| "반박 가능한가?" / 검증·감사 | **Critic** |
| "조율" / 직접 실행 X | **Leader** |

규칙: 한 사람에게 두 archetype 강제 금지(분리 스폰) / 매칭 모호 → Researcher 기본값 / 독립 검증을 맡는 Critic을 둔다 / **Leader 역할은 현재 세션이 맡으며 별도 Leader 워커를 기본 스폰하지 않는다** — 사용자가 별도 조율자를 명시한 경우에만 그 필요와 추가 비용을 팀 구성 승인에 포함 / 흔한 오매칭은 `subagent-synthesis.md` 표 참조

**[4-C] 도메인 살 채집** (6-2.5 카드 합성에 사용) — 살 1 정체성(본질 + 성격 형용사 3-4 + 경험) / 살 2 스택·메서드(표 5-8행) / 살 3 실패 패턴(4-6) / 살 4 KPI 실수치(3-5, 추상 금지). 채집 우선순위: LLM 자체 지식 → 부족하면 심부름꾼 1회 fetch → agency-agents(설치돼 있을 때만 보조)

### 스폰 유형 결정

- **기본값**: 동적 합성 카드 + `agent_type` 매핑 (Researcher/Analyst → `explorer`, Builder/Writer/Designer → `worker`, Critic → `reviewer`, Leader → 로컬·스폰 안 함)
- **외부 자원 보조 활용**: agency-agents 설치됨(`vibe:` 감지) AND 역할이 카탈로그와 정확히 매칭 → 그 외부 정의를 프롬프트에 그대로 싣고 카드는 도메인 정체성·KPI만 보강

### 모델 추천과 사용자 선택

> 다음 표는 추천 조합의 출발점이다. Step 5의 구성 확인에서 `references/model-selection.md`에 따라 모델도 선택받는다. 이미 지정한 모델은 다시 묻지 않고 기록한다.

| 역할 | 모델(티어) | 비고 |
|------|------|------|
| Lead (팀장) | **현재 호스트(로컬)** | 호스트 모델을 바꾸지 않음. 스폰하지 않음 |
| 분석·비평·최종 종합 / 핵심·고난도 구현 | **Opus 추천** | 사용자가 Sonnet 등으로 지정하면 그 선택 보존 |
| 일반 워커 (리서치 수집·쿼리·드래프트·간단 구현·표준 작업) | **Sonnet 추천** | Fable 중심·Opus 중심·직접 지정으로 변경 가능 |
| 기계적 글루 (파일 수집·포맷·추출·진행요약·더미데이터) | **Sonnet 추천** | "전부 Opus"처럼 명시한 선택 우선; Haiku는 사용자 명시 요청 때만 |
| 코드·대규모 분석 (생산 + 검토) | **Codex CLI** | 다른 base 모델. 없으면 Opus 티어 폴백 |
| 디자인/UI | **Antigravity CLI(`agy`)** | 없으면 Sonnet 티어 폴백 |
| 코드 구현·분석 + 교차검토 (멀티모델) | **gajae-code(`gjc`)** | 없으면 Codex/Opus 폴백 |
| 코드 교차 검토 | **Grok CLI(`grok`)** | build를 Codex가 했을 때 1순위 검토자 |

**검토자 추천 순서 (미지정일 때만):** Codex → grok → agy → **네이티브 적대 검토 인스턴스**(별도 컨텍스트 + *"결함을 찾아라(refute)"* 프롬프트. "검토해줘"식 요청 금지 — rubber-stamp 방지). build를 Codex가 했으면 검토는 grok, grok이 했으면 Codex — 같은 family로 자기 산출물을 검토시키지 않는다.

**모델 상속 금지:** 승인한 `model_selection.models[task.id]` 값을 카드와 실제 스폰에 명시한다. 역할 추천값으로 되돌리거나 메인 세션 모델을 상속하지 않는다. 선택 모델/CLI를 사용할 수 없으면 사유와 대안을 묻고 변경 승인 전에는 대체하지 않는다.

### 팀장 R&R (절대 준수)

팀장은 **코드를 짜지 않는다 / 직접 검색하지 않는다 / 직접 문서를 작성하지 않는다**. **계획 수립, 태스크 분배, 결과 검증, 최종 통합**만 수행. 직접 작업하면 R&R 위반.

### CLI 없을 때 폴백

1. 사용자에게 안내(기술 용어 없이): "추가 AI 도구가 있으면 더 전문적인 분석이 가능해요. 설치하시겠어요? (선택사항이에요, 없어도 잘 동작해요)"
2. 거절 → 가능한 네이티브 티어를 제안하고 선택을 확인한 뒤 대체 / 수락 → 설치 명령어 안내 후 재스캔

---

## Step 4-W: 워크플로우 명세 구성 — Workflow 경로

> **이 Step은 Workflow 경로 전용.** Agent Teams는 Step 4로.
> 공유 메모리(6-2)·KKIRIKKIRI_DIR·도메인 카드 합성은 **생성하지 않는다** — 중간 결과는 라운드 결과 파일/변수에 보관된다.

> **🚨 EXECUTE NOW — Step 4-W 진입 즉시 실행:**
> `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/execution-shapes.md")`
> — 실행형태 5종의 스크립트 골격과 토너먼트 가드가 들어 있다. Step 3.6에서 고른 형태의 골격을 그대로 따른다.

오케스트레이터(이 세션)가 인터뷰 답변을 바탕으로 **4단 게이트(W1 명세 → W1.5 모델 선택 → W2 린트 → W3 설계 카드 → 실행 → W4 프리플라이트)** 를 통과시키며 워크플로우를 구성한다. 스크립트보다 명세가 먼저다.

### W1 — WorkflowSpec 선작성 (스크립트 작성 전)

사전 준비에서 만든 이 세션의 런 장부를 불러와 Step 3.5 진단과 명세(`spec`: axes·width·fanin_rule·barrier_reason·models·contract_layers·est_tokens)를 기록한다. 다른 장부를 새로 만들지 않는다. 작업 대상과 완료 계약의 기존 `work` 필드는 보존한다. 필드 의미·설계 결함 기준은 `references/gates.md` §1.

### W1.5 — 공통 모델 선택 (스크립트 생성 전)

`Read("$PLUGIN_ROOT/skills/kkirikkiri/references/model-selection.md")` 후, 단계별 실제 추천 모델을 보여준 뒤(`수집: Sonnet / 검증: Opus / 종합: Opus`) 설계 확인 §A 블록에 모델 선택 문항을 함께 넣는다. 이미 모델을 지정했다면 재질문하지 않는다. 선택한 phase→model 맵을 장부 `model_selection`과 WorkflowSpec에 저장한 뒤 W2로 진행한다.

```
이번 작업의 에이전트 모델을 어떻게 배정할까요? (추천 배정: 수집 Sonnet / 검증 Opus / 종합 Opus)
1. <이번 작업 추천안> (추천) — 생산·분석·검증·종합은 X, 단순 기계적 처리는 Sonnet
2. Fable 중심 — 호스트의 `fable` 별칭 지원을 확인한 뒤 실행
3. Opus 중심 / Sonnet 중심 (원하는 쪽을 적어주세요)
4. 역할별 직접 지정 — 각 단계에 Fable·Opus·Sonnet을 직접 지정 (Haiku는 명시 요청 때만)
(모르면 1번으로 진행할게요)
```

### W2 — wf-lint (본진은 훅 자동 — 이 판은 오케스트레이터가 직접 실행)

> **🚨 EXECUTE NOW — 명세 스크립트를 `{cwd}/.kkirikkiri/runs/<RUN_ID>.workflow.js`로 Write한 직후:**
> ```
> Bash("node \"$PLUGIN_ROOT/scripts/wf-lint.js\" .kkirikkiri/runs/<RUN_ID>.workflow.js --models-json '<장부 model_selection JSON>'")
> ```
> exit≠0이면 **실행 금지** — 돌아온 사유(R1~R7·model-selection)를 고치고 다시 린트한다. 결과 JSON과 checklist C1~C3 자답을 장부 `lint_report`에 기록. 통과 기록 없이 W3로 가지 않는다.

### 스크립트(명세) 구성 규칙

1. **`meta` 블록**: `name`(kebab-case), `description`(한 줄), `phases`(스테이지별 title) — 순수 리터럴.
2. **스테이지 설계**: 기본 순차 phase(pipeline). 배리어는 전체 결과가 필요한 dedup/조기종료에만 `parallel()`.
3. **모델 명시 — 모든 `agent()` 호출에 `model`을 핀한다. 예외 없음.** 핀을 빼면 세션 모델을 그대로 상속한다 — 팬아웃 전체 비용 폭증.

   | 스테이지가 하는 일 | model | 판정 기준 |
   |---|---|---|
   | 수집·조사·드래프트·검증(refute) — 팬아웃되는 본체 작업 | `"sonnet"` 추천 | 선택에 따라 `"opus"` 등으로 변경 가능 |
   | 포맷 변환·필드 추출·목록 정리 — 판단이 없는 기계적 처리 | `"sonnet"` 추천 | 기계적 처리도 Haiku로 자동 배정하지 않음 |
   | 종합·우선순위 판단·최종 합성 — 전체 결과를 한 번에 보는 작업 | `"opus"` 추천 | 사용자 선택 우선; 불필요한 종합 호출은 추가하지 않음 |

   - 실제 `model`과 `phase`는 선택 맵과 일치하는 문자열 리터럴로 쓴다. 사용할 수 없는 모델은 자동으로 낮추지 말고 다시 선택받는다.
4. **adversarial-verify 스테이지 필수 포함**: 팬아웃 결과를 종합하기 전, 독립 검증 에이전트가 *"이 발견을 반박하라(refute)"* 프롬프트로 교차 검증하는 스테이지. `schema`로 구조화 반환 강제.
5. **구조화 출력**: 수집·검증 스테이지는 `{schema}`로 JSON 반환을 강제(빈 스키마 금지 — 필드 1개 이상). 예산 필드(`*_count`) 포함, 폭 ≤6.

### 스크립트 골격 예시

아래 Sonnet/Sonnet/Opus는 추천 조합의 예시다. 실제 생성 시 W1.5의 선택 맵을 각 phase의 model 리터럴에 반영한다.

```javascript
export const meta = {
  name: 'kkirikkiri-research',
  description: '[목표 한 줄]',
  phases: [
    { title: '수집' },     // Sonnet 팬아웃
    { title: '검증' },     // adversarial-verify (refute)
    { title: '종합' },     // Opus
  ],
}
phase('수집')
const found = await parallel(SOURCES.map(s => () =>
  agent(`[조사 지시] ${s}`, {model: 'sonnet', phase: '수집', schema: FINDING_SCHEMA})))
phase('검증')
const verified = await parallel(found.filter(Boolean).map(f => () =>
  agent(`다음 발견을 반박하라(refute). 확신 없으면 refuted=true: ${JSON.stringify(f)}`,
        {model: 'sonnet', phase: '검증', schema: VERDICT_SCHEMA})))
phase('종합')
return await agent(`검증 통과 결과만 종합 리포트로: ...`, {model: 'opus', phase: '종합'})
```

### W3 — 설계 카드 (Continuation, 사용자 확인 지점)

명세가 W2를 통과하면 Step 6-W로 진행하기 전에 선택한 모델을 포함한 설계 요약표를 보여주고 §A로 실행 승인을 받는다. W1.5에서 이미 확인한 모델은 다시 묻지 않는다:

```
Workflow 설계 (wf-lint 통과):
| 축 N개 | 폭 5 | 예산 축당 8회 | 수집 Sonnet / 검증 Opus / 종합 Opus | 견적 ~X만 토큰 |
판정 근거: {Step 3.5 rationale 한 줄}

이대로 실행할까요?
1. 네, 실행해주세요 (추천)
2. 축·폭·모델을 조정하고 싶어요
3. 문장으로 직접 적기
(모르면 1번으로 진행할게요)
```

### W4 — 프리플라이트 (실행 직후 1라운드 검사)

1라운드 결과 수신 즉시 누락 축·예산(`search_count` 합, 캡 80% 초과 시 확장 축소)·계약 위반을 검사하고 장부(`budget_used`·`missing_axes`·`repair_cycles`)에 기록한다. 상세: `references/gates.md` §1 W4. 완료 시 done-gate를 거쳐 `outcome`을 채우면 장부가 닫힌다.

---

## Step 5: 팀 구성 제안 + 모델 선택 + 유저 확인 — Agent Teams 경로

> **이 Step은 Agent Teams 경로 전용.** Workflow는 Step 5를 건너뛴다 (W3 설계 카드가 확인 역할).

이 확인 전에 `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/model-selection.md")`. 기존 확인 블록에 모델 구성 선택을 함께 넣고, 답변 후 task.id별 맵을 런 장부 `model_selection`에 저장한다. 카드와 실제 호출은 그 맵을 따른다. 이미 지정한 모델은 다시 묻지 않는다.

### 제안 형식 (Step 5-1: 일반 텍스트로 출력 — 항상 보이게)

```
이렇게 팀을 구성할게요:

📋 목표: [인터뷰에서 파악한 목표]

팀 구성:
├── 팀장 — 현재 세션 (모델 변경 없음, 로컬)
├── [역할명 1] — [구체적 역할 설명] ([추천 모델] — 한글 설명)
├── [역할명 2] — [구체적 역할 설명] ([추천 모델] — 한글 설명)
└── (선택) [외부 도구] — [역할 설명] (백그라운드)

예상 작업 방식:
1. 팀장이 전체 계획을 세우고 각자 역할을 배분합니다
2. 팀원들이 동시에 작업을 수행합니다
3. 팀장이 결과를 검증하고 통합합니다
4. 최종 리포트를 생성합니다

⏱️ 예상 소요 시간: [기본 3명 10-15분 / 확장 4-5명 15-25분 / 외부 CLI +5-10분]
💡 팁: 빠르게 핵심만 필요하면 팀 규모를 줄일 수 있어요. 대신 깊이가 좀 얕아질 수 있어요.

📁 팀원 역할 파일 (시작 후 생성됩니다):
  {KKIRIKKIRI_DIR}/agents/[역할명1].md
  {KKIRIKKIRI_DIR}/agents/[역할명2].md
```

### 용어 표기 (공식 용어 + 한글 설명 병기)

| 공식 용어 | 병기할 한글 설명 |
|---|---|
| Opus | "가장 똑똑한 모델" — 복잡한 판단, 기획, 통합 |
| Fable | "연결된 Fable 모델" — 호스트 지원을 확인한 뒤 배정 |
| Sonnet | "균형형 모델" — 실행력 좋고 효율적, 워커 기본 |
| Haiku | "경량 모델" — 기본 추천에서 제외, 사용자 명시 요청 때만 |
| Codex CLI | "OpenAI 코드·대규모 분석 도구" |
| Antigravity CLI(agy) | "디자인/UI 도구" |
| gajae-code(gjc) | "멀티모델 코드·교차검토 도구" |
| Grok CLI | "코드 교차 검토 도구" |
| Agent Teams | "실시간 협업 팀" |
| Workflow | "대량 자동 병렬 처리" |

규칙: 공식 용어를 숨기지 않는다(`공식 용어 (한글 설명)`) / 내부 구현(스폰 호출, 내부 파일 경로)은 노출 금지 / 설명 없이 용어만 던지기 금지

### Step 5-2: §A로 확인 + 모델 선택 (2문항 연속)

**EXECUTE:** 텍스트 출력 직후 즉시 아래 블록을 출력한다:

```
Q1. 이 팀 구성으로 시작할까요?
1. 네, 시작해주세요 (추천) — 위 구성대로 팀을 만들고 바로 작업을 시작합니다.
2. 팀원을 조정하고 싶어요 — 역할이나 인원수를 바꿀 수 있어요.
3. 처음부터 다시 — 인터뷰를 다시 진행합니다.

Q2. 에이전트 모델은 어떻게 배정할까요? (추천 배정: [역할1] Sonnet / [역할2] Opus / 검증 Opus)
1. <이번 작업 추천안> (추천) — 위 추천 배정대로
2. Fable 중심 — 생산·분석·검증·종합은 Fable, 단순 기계적 처리는 Sonnet (호스트 지원 확인 후)
3. Opus 중심 / Sonnet 중심 (원하는 쪽을 적어주세요)
4. 역할별 직접 지정 — 각 역할에 Fable·Opus·Sonnet을 직접 지정 (Haiku는 명시 요청 때만)
(각 문항 번호를 "Q1: 1, Q2: 1"처럼 적어주세요. 모르면 둘 다 1번으로 진행할게요)
```

**응답 처리 (즉시 실행, 텍스트만 출력하고 멈춤 금지):**
- "네, 시작해주세요" → 모델 맵을 장부 `model_selection`에 저장 → 즉시 Step 6-1의 team_name 생성 + KKIRIKKIRI_DIR 정의로 진행
- "조정하고 싶어요" → 어떤 부분을 바꿀지 §A로 묻고 Step 4 재실행 (변경분만 재확인)
- "처음부터 다시" → Step 1로 복귀

> **🚨 EXECUTE NOW — "네, 시작해주세요"를 받으면 즉시 다음 도구를 순서대로 호출한다 (Action Vacuum 회귀 방지):**
> ```
> Bash("RAND4=$(openssl rand -hex 2 2>/dev/null || printf '%04x' $((RANDOM % 65536))); echo kkirikkiri-{preset}-$(date +%Y%m%d-%H%M)-${RAND4}")
> Bash("mkdir -p {KKIRIKKIRI_DIR}/{agents,prompts,agent-cache,archive} && mkdir -p {프로젝트루트}/.kkirikkiri/shared/saved-teams")
> ```
> 그 다음 Step 6-2(공유 메모리) → 6-2.5(카드) → 6-2.6(card-lint) → 6-4(스폰). 이 박스가 Step 5→6 경계의 도구 호출 앵커다.

---

## Step 6: 작업 공간 + 공유 메모리 + 카드 + 스폰 + 실행 — Agent Teams 경로

> **이 Step은 Agent Teams 경로 전용.** Workflow는 Step 6-W로.

### 6-0. 적응형 척추 (항상 적용)

Agent Teams는 **항상 능동 코디네이션(적응형 척추)으로 동작한다. 모드 선택은 없다.**

> **🚨 EXECUTE NOW — Step 6 진입 즉시 실행:**
> ```
> Read("$PLUGIN_ROOT/skills/kkirikkiri/references/coordination-protocols.md")
> ```

- 팀장(로컬)은 **능동 구동 루프(drive→inspect→re-inject)**를 따른다. collect-at-end 금지 — 중간 산출을 읽고 그때그때 재지시/재배분/런타임 스폰.
- 6-4 스폰은 매 라운드 보고 의무로 작성한다.
- 비용 주의: 능동 코디네이션은 토큰이 무겁다. **소규모(N≤4) 권장.** 대량·루틴이 섞여 있으면 Workflow 재안내를 고려.

> **🚨 EXECUTE NOW — 이 Step에 진입했다는 것은 Step 5에서 확인을 받았다는 뜻이다. 아래 6-1 / 6-2 / 6-2.5 / 6-2.6 / 6-4의 코드 블록은 예시가 아니라 실제 도구 호출이다. 한 단계도 건너뛰지 말고 순차 실행하며, 각 호출 완료를 확인한 후에만 다음 단계로 진행한다.**

### 6-1. 작업 공간 생성

```bash
RAND4=$(openssl rand -hex 2 2>/dev/null || printf '%04x' $((RANDOM % 65536)))
team_name="kkirikkiri-{preset}-$(date +%Y%m%d-%H%M)-${RAND4}"   # 예: kkirikkiri-research-20260503-1430-a3f2
```
```
KKIRIKKIRI_DIR={프로젝트루트}/.kkirikkiri/teams/{team_name}
```
> **이 변수를 세션 전체에서 일관되게 사용한다.**

**레거시 마이그레이션 시임 (flat → session-scoped)** — `.kkirikkiri/TEAM_PLAN.md`가 루트에 있으면 `mkdir .kkirikkiri/.migration.lock` 락으로 1회만 `teams/legacy-<epoch>/`로 이동한다(TEAM_PLAN/PROGRESS/FINDINGS, agents/, prompts/, agent-cache/). 락 실패 = 다른 세션이 처리 중 → 스킵.

```bash
mkdir -p {KKIRIKKIRI_DIR}/{agents,prompts,agent-cache,archive}
mkdir -p {프로젝트루트}/.kkirikkiri/shared/saved-teams
```

사용자에게 세션 핸들을 알린다. **아직 팀원을 스폰하기 전이므로 "팀이 생성되었습니다"라고 말하지 않는다:**
```
작업 공간을 준비했습니다.
세션 ID: {team_name}
작업 디렉토리: {KKIRIKKIRI_DIR}
```

**팀 형성 확인 (스폰 직후 1회)** — 6-4에서 스폰 호출이 실제로 에이전트 핸들을 반환했는지 확인한 뒤에만 "팀이 생성되었습니다"라고 보고한다. 스폰이 거부되거나 핸들이 없으면 "에이전트 N명이 병렬로 작업 중"이라고 정확히 알리고, Step 8의 종료 절차는 완료 대기로 대체한다.

`{team_name}`은 **작업 디렉토리 이름**이다 — 런타임이 쓰는 내부 팀 식별자와 별개다.

### 6-2. 공유 메모리 초기화 (기억 외부화)

> **기억력을 믿지 마. 중요한 결정은 반드시 파일에 기록.** 대화가 길어지면 오래된 내용이 압축된다.

> **🚨 MANDATORY READ:** `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/shared-memory.md")`

> **🚨 EXECUTE NOW — shared-memory.md를 읽은 직후 즉시 3개 파일을 Write한다 (Read만 하고 6-2.5로 점프 금지):**
> ```
> Write("{KKIRIKKIRI_DIR}/TEAM_PLAN.md", <TEAM_PLAN 템플릿 — 팀 목표, 팀원, 단계별 작업 분배, 태스크 목록>)
> Write("{KKIRIKKIRI_DIR}/TEAM_PROGRESS.md", <TEAM_PROGRESS 템플릿 — 빈 진행 로그>)
> Write("{KKIRIKKIRI_DIR}/TEAM_FINDINGS.md", <TEAM_FINDINGS 템플릿 — 빈 발견 사항 + DEAD_ENDS>)
> ```
> 세 파일 모두 Write 완료를 확인한 후에만 6-2.5로 진행. 미초기화 상태에서 스폰하면 컨텍스트 손실 시 복구 불가.

### 6-2.5. 도메인 카드 합성 (archetype + 4종 살 + 경계 블록)

팀원 스폰 전에 각 팀원의 **도메인 카드**를 `{KKIRIKKIRI_DIR}/agents/{역할명}.md`에 합성 저장한다 (100~150줄).

왜: archetype 본문(team-prompts.md)은 공유 행동 원칙, 카드는 그 사람만의 도메인 디테일 / 컨텍스트 흐려지면 두 파일 다시 읽어 복구 / 카드는 한 번 작성, 스폰 프롬프트에는 경로만.

```markdown
---
name: [역할명]
archetype: [Researcher / Analyst / Builder / Writer / Designer / Critic / Leader]
domain: [도메인 한 줄]
team: [team_name]
model: [model_selection.models[task.id] — opus / sonnet / fable]
tools: [Read, Grep, Write]            # 검증 역할(Critic)은 쓰기 도구 없이
write_scope: [schemas/**, docs/x.md]  # 쓰기 역할 필수; Critic은 [] + review_mode: true
review_mode: false
stop: {maxTurns: 25, done_when: "측정 가능한 완료 기준"}
effort: medium
created: [timestamp]
---

# [역할명]

## 정체성 (도메인 살 1)
- 본질 / 성격(형용사 3-4, generic 회피) / 경험

## 행동 원칙 (archetype 본문 인용)
> archetype: [이름] / 핵심: [Evidence-First 등] / 검증 방식: [한 줄]
→ 상세는 team-prompts.md "# [archetype]" 섹션 참조

## 도메인 R&R
[구체적 작업 범위 5-7행]

## 도메인 스택 / 메서드 (살 2) — 표 5-8행 ("이유" 칼럼 필수)
## 도메인 실패 패턴 (살 3) — 4-6개, 결과까지 명시
## 도메인 KPI (살 4) — 실수치 3-5개, 추상 표현 금지
## 소통 스타일 — 실제 발언 예시 4개
## 결과물 형식
## 공유 메모리
- 계획: {KKIRIKKIRI_DIR}/TEAM_PLAN.md / 진행: TEAM_PROGRESS.md / 발견: TEAM_FINDINGS.md
```

| 길이 가이드 | 목표 |
|---|---|
| 일반적 도메인 (개발자, 리서처) | 100~120줄 |
| 전문 도메인 (Solidity, 임베디드) | 130~150줄 |
| 단순 보조 (포맷팅) | 80~100줄 |

→ few-shot 예시는 `subagent-synthesis.md` 참조. 경계 블록 필드 정의는 `subagent-synthesis.md` [4] + `gates.md` §2.

**팀장 메모(로컬)에 전체 팀원 카드 인덱스 유지:** `{KKIRIKKIRI_DIR}/agents/[팀원].md — [archetype + 도메인 한 줄]` 목록을 TEAM_PLAN.md에 적어 팀원이 역할을 혼동하면 해당 카드 + archetype 섹션을 다시 읽게 지시한다.

### 6-2.6. 카드 게이트 (card-lint — 본진은 훅 자동, 이 판은 직접 실행)

> **🚨 EXECUTE NOW — 카드를 모두 Write한 직후:**
> ```
> Bash("node \"$PLUGIN_ROOT/scripts/card-lint.js\" --dir \"{KKIRIKKIRI_DIR}/agents\"")
> ```
> 위반(C1 필수 필드 / C2 stop 하위 키 / C3 Critic read-only / C4 쓰기 역할 write_scope / **C5 카드 간 write_scope 교집합**)이 하나라도 남은 상태로 스폰하지 않는다. 핵심은 C5: 공유 파일은 소유자 1명 지정 + 나머지는 변경 요청. 결과를 장부 `boundary_violations`에 기록. 통과 기록(exit 0) 없이 6-4로 가지 않는다.

### 6-3. 태스크 목록

팀장이 전체 작업 계획을 TEAM_PLAN.md의 태스크 목록으로 정리한다 (제목 / 구체적 작업 내용·기대 결과물·제약 / 담당 / 상태). 예(리서치 팀): 1. 리서치 계획 수립 — 팀장 / 2. 웹 리서치 — 리서처 1 / 3. 문서 리서치 — 리서처 2 / 4. 결과 통합 + 리포트 — 팀장이 검증·통합, 작성 지시

### 6-4. 팀원 스폰 (런타임 멀티에이전트)

독립 생산자와 검증자로 구성된 작은 Teams 실행에는 `references/prepare-team-pilot.md`의 **옵트인 준비기**(`node "$PLUGIN_ROOT/scripts/prepare-team.js"`)를 사용할 수 있다. 승인받은 계획을 입력하고, 생성된 카드와 요청을 다시 창작하지 말고 사용한다. 이 경로는 준비만 수행하며 에이전트를 자동 발사하지 않는다.

> ⛔ **선행 조건**: 6-2.6 card-lint가 exit 0으로 통과했어야 한다. 사용자가 "질문 생략하고 즉시 실행"을 요청했더라도 이 게이트는 건너뛰지 않는다.

> **🚨 gate-spawn 자가 점검 — 팀원마다 스폰 직전에 실행:**
> 1. 스폰 프롬프트 본문에 **① 허용 도구(또는 read-only) ② `write_scope: [...]`(또는 read-only) ③ `stop: maxTurns N, done_when "…"`** 세 항목이 문자 그대로 들어 있는지 확인. 하나라도 없으면 스폰하지 않고 채운다.
> 2. `write_scope`는 실제 glob 형태로(`schemas/**, CONVENTIONS.md`). 장부 `declarations[]`에 이미 선언된 다른 팀원의 write_scope와 겹치면 **스폰 차단** — 공유 파일은 한 팀원에게만 두고 나머지는 그 팀원에게 변경을 요청하는 방식으로 프롬프트를 고친다(C5@spawn). 장부 `boundary_violations[gate=spawn-overlap]` 기록.
> 3. `Bash("printf '%s' '{\"selection\": <장부 model_selection>, \"id\": \"<task_id>\", \"model\": \"<model>\"}' | node \"$PLUGIN_ROOT/scripts/model-selection.js\"")` — exit≠0이면 선택 맵과 불일치. 맵을 고쳐 통과시키지 말고 스폰 인자를 맵에 맞춘다.
> 4. 통과 → 장부 `declarations[]`에 `{agent, write_scope[], read_only}` 추가 후 스폰.

각 팀원을 런타임 스폰으로 만든다. 프롬프트에는 **archetype 본문 경로 + 도메인 카드 경로 + 승인된 경계 값 + 첫 태스크 + 공유 메모리 경로**를 넣는다 (카드/archetype 본문 자체를 복붙하지 않되, 게이트가 검사할 경계는 경로 참조로 대체하지 않는다):

```
spawn_agent({
  name: task_id,            // 선택 맵의 ID와 일치; 사람이 읽는 역할명은 prompt에 기재
  agent_type: "explorer",   // Researcher/Analyst→explorer, Builder/Writer/Designer→worker, Critic→reviewer
  model: selected_models[task_id],  // 호스트가 model 인자를 받으면 전달("fable"/"opus"/"sonnet"; "haiku"는 명시 요청 때만). 받지 않으면 카드·장부 기록으로 유지
  prompt: `
당신은 [역할명]입니다. ([archetype] archetype + [도메인])

## 승인된 실행 경계 (카드에서 실제 값으로 채움)
- 허용 도구: [승인된 도구 목록]            (검증자면 read-only)
- write_scope: [schemas/**, docs/x.md]   (밖 파일 쓰기 금지 — 필요하면 소유자에게 요청; 검증자면 [] + read-only)
- stop: maxTurns [양의 정수], done_when "[측정 가능한 완료 기준]"
- effort: [승인된 노력 수준]
- 이 경계는 작업 선언이다. 호스트가 실제로 적용한 권한 제한과 구분한다.

## 1. 마스터 행동 원칙 (반드시 먼저 읽기)
Read("$PLUGIN_ROOT/skills/kkirikkiri/references/team-prompts.md") 의
"# [archetype 이름]" 섹션을 읽고 행동 원칙을 내재화하세요.

## 2. 당신의 도메인 카드
Read("{KKIRIKKIRI_DIR}/agents/{역할명}.md") 로
도메인 정체성·스택·실패 패턴·KPI를 확인하세요.

## 3. 첫 태스크
[구체적 지시] — 완료 시 결과·검증 증거를 TEAM_PROGRESS.md에 기록하고 최종 노트로 보고

## 4. 공유 메모리
- {KKIRIKKIRI_DIR}/TEAM_PLAN.md / TEAM_PROGRESS.md / TEAM_FINDINGS.md (DEAD_ENDS 포함)

## 5. 팀 정보
- 작업 디렉토리 키: {team_name}
- 팀장: 현재 호스트 세션 (로컬)
- 다른 팀원: [목록]
- 심부름꾼이 필요하면 하위 에이전트를 스폰해 병렬 위임 (team-prompts.md 참조)
`
})
```

**팀장은 스폰하지 않는다 — 이 세션이 팀장이다.** 팀장 R&R + 능동 코디네이션(coordination-protocols.md)을 내재화하고 직접 구동한다. 팀원 무응답/스폰 실패 시: ① 역할을 다른 팀원에게 재배분 ② 불가하면 팀장이 직접 수행 ③ 핵심 역할이 빠지면 사용자에게 알리고 판단 요청.

### 6-5. 외부 CLI 실행 (가용 프로바이더)

외부 CLI가 배정된 역할은 러너로 실행한다. `--provider`는 `codex`(코드·대규모 분석) | `antigravity`(디자인/UI, 바이너리 `agy`) | `gjc`(코드 구현·분석 + 교차검토) | `grok`(코드 교차 검토) 중 환경 스캔에서 설치 확인된 것.

**검토 역할일 때는 적대적 프롬프트로:** "검토해줘"가 아니라 **"다음 산출물의 결함을 찾아 반박하라(refute)"**. build와 다른 family가 검토한다.

```
1. 프롬프트 파일 작성: Write → {KKIRIKKIRI_DIR}/prompts/{task-id}.md
2. CLI 실행 (백그라운드 — 셸 잡으로 띄우고 JOB_DIR만 받는다):
   Bash: bash "$PLUGIN_ROOT/scripts/run-cli.sh" start --provider codex --prompt-file {KKIRIKKIRI_DIR}/prompts/{task-id}.md
   → 출력되는 JOB_DIR 경로를 저장
   (디자인/UI 역할은 --provider antigravity. agy 1.0.x는 비-TTY에서 stdout이 비는 버그가 있어 results가 빈 경우 네이티브 폴백 권장)
   (build를 codex가 했고 grok_cli=true이면 코드 교차 검토는 --provider grok. grok_cli=false이면 설치 확인된 다른 family의 검토자를 선택.
    다른 family가 없으면 네이티브 독립 에이전트의 적대적 검토로 폴백하고 교차모델 검증은 미실시로 기록. 미설치 CLI를 실행하거나 설치·인증을 강제하지 않는다.)
3. 완료 대기:   Bash: bash "$PLUGIN_ROOT/scripts/run-cli.sh" wait JOB_DIR      (liveness 규정대로 mtime 점검)
4. 결과 확인:   Bash: bash "$PLUGIN_ROOT/scripts/run-cli.sh" results JOB_DIR
5. 결과를 TEAM_FINDINGS.md에 기록
6. 정리:        Bash: bash "$PLUGIN_ROOT/scripts/run-cli.sh" clean JOB_DIR
```

### 6-6. 태스크 배정 + 능동 구동

현재 세션이 승인된 TEAM_PLAN에 따라 각 워커에게 직접 태스크를 배분한다(스폰 프롬프트의 첫 태스크 + 이후 후속 지시). 별도 Leader를 스폰한 뒤 배분을 다시 맡기지 않는다. 팀원 최종 노트가 도착할 때마다 정독 → 검증/모순/공백 판단 → 다음 수(재지시 / 교차검증 위임 / 런타임 전문가 스폰). fire-and-forget 금지. 갈림길(비가역·가치충돌)에서만 게이트(독립 의견 + 심판) 발동 — coordination-protocols.md.

---

## Step 6-W: 워크플로우 실행 — Workflow 경로

> **이 Step은 Workflow 경로 전용.** W2 wf-lint 통과 + W3 승인 없이 진입하지 않는다.

Step 4-W의 명세 스크립트를 **오케스트레이터가 phase 순서대로 라운드 실행**한다:

1. `phase('X')` 하나 = 라운드 하나. `parallel([...])` 안의 `agent()` 호출은 **동시에 스폰**하고(폭 ≤6), 순차 `await agent()`는 순서대로 스폰한다.
2. `agent(prompt, {model, phase, schema})` 1건 = 런타임 스폰 1건. `model`은 선택 맵의 값을 전달(호스트가 받지 않으면 기록), `schema`는 프롬프트에 "다음 JSON 스키마로만 응답" 지시로 강제하고 응답을 파싱 검증한다 — 파싱 실패는 결과 `null`로 처리하고 `filter(Boolean)` 의미를 지킨다.
3. 각 라운드 결과를 `{cwd}/output/<RUN_ID>/round-<phase>.json`에 저장한다(스크립트 변수 대응). 다음 라운드는 이 파일에서 읽는다.
4. 실행 시작 안내:
   ```
   Workflow가 시작됐어요. 라운드가 끝날 때마다 진행 상황을 알려드리고, 완료되면 결과를 정리해서 보여드릴게요.
   ```
5. 공유 메모리·도메인 카드 등 Agent Teams 인프라는 일절 만들지 않는다.
6. 토너먼트 형태면 `execution-shapes.md` §5의 가드(게이트 비면 거부·참가자별 워크트리·기본 2명)와 shim 패턴(외부 CLI는 `run-cli.sh`로)을 그대로 따른다.
7. 1라운드 완료 즉시 **W4 프리플라이트** 실행 → 마지막 라운드 완료 → Step 7-W.

### 6-W 에러 처리
- W3 승인 거부 → "다른 방식(Agent Teams)으로 진행할까요?" §A
- 스테이지 오류 → 명세의 해당 스테이지만 수정 → wf-lint 재실행 → 실패 라운드부터 재실행 (완료된 라운드 결과 파일은 재사용)
- 중도 중단 → 완료된 라운드 파일이 남아 있으므로 그 지점부터 resume 가능함을 안내

---

## Step 7: 검증 루프 (Ralph Pattern) — Agent Teams 경로

> **이 Step은 Agent Teams 경로 전용.** Workflow의 검증은 내부 adversarial-verify 스테이지가 수행 — Step 7-W로.

> **1라운드라도 수용 기준을 전부 통과하면 종료한다.** 부족하면 실패한 기준만 보강한다. 라운드 수를 채우기 위한 반복은 하지 않는다.
> **반복에는 천장이 있다.** 아래 셋 중 하나라도 걸리면 즉시 Step 8로: ① 수용 기준 전부 통과 ② **2라운드를 마쳤다**(3라운드 이상은 사용자 명시 요청 때만) ③ 직전 라운드 대비 실질 개선 없음. 남은 아쉬운 점은 **결과 보고에 "미해결" 항목으로** 적는다.

### 7-1. 진행 상황 모니터링
팀원 최종 노트·TEAM_PROGRESS.md 갱신을 수신하며 진행 상황을 모니터링한다. 백그라운드 잡은 liveness 규정대로 점검.

### 7-2. 1라운드 완료 확인 + done-gate

워커의 완료 보고를 받으면 호스트가: 1. 리포트 파일 확인(Read) 2. TEAM_PLAN.md "검증 결과" 섹션 확인 3. 독립 검증자의 증거와 최종 수용 기준 대조

> **🚨 EXECUTE NOW — 완료 게이트(done-gate, 본진은 Stop 훅 — 이 판은 완료 판정 직전에 직접 실행):**
> ```
> Bash("node \"$PLUGIN_ROOT/scripts/done-gate.js\" --repo \"<work.repo>\" --report \"<work.report>\" --contract \"<work.contract>\"")
> ```
> 장부에 `work{repo,report}`가 있고 `outcome`이 비어 있으면 반드시 돈다. exit≠0(무변경인데 심사 증적 없음 / 완료 계약 검사 실패)이면 **완료 불허** — 팀장이 정비를 지시하거나 보고서에 `## 무변경 종료 심사` 파일별 3열 표(파일/검사 내용/변경 불요 근거)를 채운 뒤 재실행. 결과 JSON을 장부 `outcome_gate`에 기록. 상세: `references/gates.md` §3.

### 7-3. 품질 판정
목표 달성도 / 완성도 / 정확성(출처·근거·테스트) / 일관성(팀원 간 모순)

### 7-4. 품질 충분 → Step 8로

### 7-5. 품질 부족 → 자동 판정 + 2라운드 제안

```
IF 목표_달성도 = FAIL      → 방식 B (전체 재구성)
ELIF 일관성 = FAIL         → 방식 C (부분 교체)
ELIF 완성도/정확성 = FAIL   → 방식 A (팀 유지 + 보강)
ELIF 라운드 >= 승인된_한도(기본 2) → 중단 — 미해결 기준을 명시한 현재 결과로 리포트
```

**EXECUTE:** 판정 결과를 채워 §A 질문 도구로 즉시 묻고 턴을 끝낸다(번호 블록 폴백일 때의 모양):
```
(1라운드 결과 + 부족한 부분 설명). 보강할까요?
1. 네, 보강해주세요 (추천) — 부족한 부분을 집중적으로 보완합니다. 시간이 좀 더 걸려요.
2. 이 정도면 괜찮아요 — 현재 결과를 최종 리포트로 정리합니다.
3. 처음부터 다시 — 팀을 해산하고 새로 구성합니다.
4. 문장으로 직접 적기
(모르면 1번으로 진행할게요)
```
응답 처리(즉시 실행): "보강" → 7-6 Read 박스 → 방식 A/B/C / "괜찮아요" → 8-1 / "처음부터" → Step 1

### 7-6. 2라운드 실행 방식 (3가지)

> **🚨 EXECUTE NOW — 2라운드 진입 즉시:** `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/validation-guide.md")`

교체·추가 팀원 스폰도 6-4의 gate-spawn 자가 점검을 똑같이 거친다. 재구성(방식 B) 시 TEAM_FINDINGS.md 내용을 새 팀에 반드시 전달한다.

### 7-7. 최대 라운드 제한
기본 한도 2라운드. 추가 라운드는 미해결 기준·새 접근·추가 비용을 설명하고 사용자가 명시 승인한 경우에만. 한도에 도달해도 미해결 기준을 통과로 바꾸지 않는다.

---

## Step 7-W: 결과 수신 + 사후 검토 — Workflow 경로

1. **검증은 이미 끝났다** — 내부 adversarial-verify 스테이지가 1차 검증을 수행했다.
2. **cross-model 사후 검토 (선택)**: 결과가 고위험 결정·코드 산출물이고 **Codex CLI가 설치돼 있으면**, 반환값을 `run-cli.sh --provider codex`로 1회 적대 검토("결함을 찾아 반박하라")에 보낸다. 없으면 생략.
3. **결과 미흡 시**: Ralph 루프를 돌리지 않는다. 명세의 해당 스테이지를 수정해 **재실행을 제안**한다(완료된 라운드 파일은 재사용).
4. > **🚨 EXECUTE NOW — done-gate:** `Bash("node \"$PLUGIN_ROOT/scripts/done-gate.js\" --repo \"<work.repo>\" --report \"<work.report>\" --contract \"<work.contract>\"")` — 무변경 종료를 심사 증적 없이 통과시키지 않는다. 차단되면 정비 또는 심사표 작성 후 재실행. 결과를 장부 `outcome_gate`에 기록.
5. 완료 → Step 8-W.

---

## Step 8: 결과 수집 + 리포트

> Agent Teams 경로는 8-1~8-4. **Workflow는 Step 8-W**(이 섹션 끝)로. 어느 경로든 done-gate 통과 기록이 장부에 있어야 진입한다.

### 8-1. 팀 종료
스폰된 팀원이 아직 살아 있으면 종료 지시("작업이 완료되었습니다. 수고하셨습니다.")를 보내고 정리한다. 핸들 없이 서브에이전트로 동작 중이었다면 완료 회수로 대체한다.

> **🚨 산출물이 이미 완성됐는데 대기하지 마라.** 목표 산출물이 디스크에 존재하고 게이트를 통과했다면 남은 에이전트의 보고를 무한정 기다리지 말고 8-2로 진행한다. 미완료 에이전트는 결과 보고에 한 줄로 명시한다.

### 8-2. 유저에게 결과 전달 + 세션 요약

```
끼리끼리 팀 작업이 완료되었어요!

📋 팀: [팀 구성 요약]
🎯 목표: [목표]
📄 결과: [리포트 파일 경로 — work.report]
🔄 라운드: [수행한 라운드 수]
✅ 게이트: card-lint pass / done-gate pass (또는 미해결 항목)

[리포트 핵심 요약 2-3줄]
```

> **🚨 EXECUTE NOW — 결과 전달 직후:** `Read("$PLUGIN_ROOT/skills/kkirikkiri/references/output-guide.md")` — 세션 요약 형식, 팀 저장 파일 형식, 에이전트 저장 절차. 이 Read 없이 8-3으로 진행하지 말 것.

Codex에는 자동 메모리가 없으므로 팀 구성/환경/무엇이 효과적이었고 왜를 자연어로 요약 출력하고 `{KKIRIKKIRI_DIR}/TEAM_REPORT.md`에도 남긴다(다음 세션에 붙여넣어 이어쓰기 가능). 장부 `outcome`을 채워 닫는다.

### 8-3. 팀 저장 (선택)

**EXECUTE:**
```
이 팀 구성을 저장해둘까요? 나중에 비슷한 작업할 때 바로 불러올 수 있어요.
1. 네, 저장해주세요 (추천) — 다음에 인터뷰 없이 바로 시작할 수 있어요.
2. 아니요, 괜찮아요 — 이번만 사용하고 저장하지 않아요.
(모르면 1번으로 진행할게요)
```
"저장" → `Write → {프로젝트루트}/.kkirikkiri/shared/saved-teams/{team_name}.md` 후 8-3-1 / "아니요" → 8-3-1. 형식·불러오기 절차: `output-guide.md`.

### 8-3-1. 팀원 에이전트 저장

**EXECUTE:**
```
잘 동작한 팀원을 에이전트로 저장할까요? 다른 프로젝트에서도 바로 쓸 수 있어요.
1. 네, 저장할게요 — 역할과 능력을 에이전트 파일로 저장해요. 다음 팀 구성 때 자동으로 감지돼요.
2. 괜찮아요 — 이번만 쓰고 저장하지 않아요.
(모르면 2번… 이 질문은 선택이라 답이 없으면 저장하지 않고 넘어갈게요)
```
"저장" → `output-guide.md` 절차대로 팀원 선택(§A, 여러 명이면 "1,3"처럼) → 프롬프트 정제 → `Write → .codex/agents/{역할명}.md`(recommended-for 포함) → 8-4 / "괜찮아요" → 8-4

### 8-4. 공유 메모리 정리
`{KKIRIKKIRI_DIR}/`는 유지한다. 사용자가 원하면 삭제: "이번 세션 작업 기록({KKIRIKKIRI_DIR}/)을 삭제할까요? 남겨두면 나중에 참고할 수 있어요."

### Step 8-W: Workflow 결과 리포트

1. 반환값을 8-2 형식으로 리포트한다(팀 구성 → "처리 규모"):
   ```
   끼리끼리 Workflow 작업이 완료되었어요!
   🏭 처리: [N개 에이전트 / M개 단계]   🎯 목표: [목표]
   📄 결과: [반환값 요약 또는 산출 파일 경로]   ✅ 게이트: wf-lint pass / done-gate pass
   [핵심 요약 2-3줄]
   ```
2. **재사용 안내**: 같은 작업을 반복할 거면 `.kkirikkiri/runs/<RUN_ID>.workflow.js` 명세를 그대로 다시 실행할 수 있다고 안내한다(saved-teams에는 저장하지 않는다).
3. 세션 요약은 8-2와 동일. 장부 `outcome`을 채워 닫는다.

---

## 에러 처리

### 팀원 무응답/오류 (3단계 에스컬레이션)

| 단계 | 상태 | 대응 |
|---|---|---|
| 1회 idle | 정상 | 무시 — 지시 후 응답 대기 중일 수 있음 |
| 2회 연속 idle | 주의 | 진행 확인 지시 |
| 3회 연속 idle | 조치 | 해당 역할만 교체 (kill criteria: 같은 실수 2회 반복도 즉시 교체) |

- 팀원 에러 → 팀장이 판단하여 재시도 또는 다른 팀원에게 재배정

### 심부름꾼 관리
- 응답 없음 → 팀원이 직접 수행 또는 새 심부름꾼 스폰 / 결과 품질 낮음 → 직접 보완 또는 재지시

### CLI 실행 실패
- 선택한 CLI/모델 실행 실패 → 실패를 알리고 재시도·대체 모델·취소를 §A로 선택받는다. 승인 전에 자동 대체하지 않는다.
- 사용자에게 기술적 에러 메시지 그대로 노출 금지 — "외부 도구에서 문제가 생겨서 내부 AI로 대체했어요" 수준

### 게이트 차단
- wf-lint/card-lint/done-gate/gate-spawn 차단 → 사유를 고치고 재실행. 차단 사실과 수정 내용을 장부에 기록. "그냥 진행"은 금지. 3회 이상 같은 게이트에서 막히면 사용자에게 상황과 선택지를 §A로 알린다(종료 허용은 성공이 아니라 미검증으로 보고).

### 인터뷰 중단
- 사용자가 취소 → 즉시 종료, 팀 생성하지 않음. 장부 `outcome: cancelled`. "언제든 다시 시작할 수 있어요"

---

## 절대 하지 마 (전체 워크플로우)

- [ ] 유저 확인 없이 팀을 생성하지 마 (Workflow는 W3 설계 카드 승인이 이 역할)
- [ ] **승인된 실행 방식(substrate)을 임의로 바꾸지 마**
- [ ] **사용자가 "Workflow"를 고르거나 W3를 승인하지 않았는데 라운드 실행을 시작하지 마**
- [ ] 런 장부 없이 Step 1로 가지 마 / 다른 세션의 장부를 재사용하지 마
- [ ] wf-lint·card-lint·gate-spawn 자가 점검·done-gate 통과 기록 없이 다음 단계로 가지 마 — "즉시 실행" 요청에도 게이트는 유지
- [ ] 질문 도구가 있는지 이번 세션 도구 목록으로 확인 — 있으면 §A 질문 도구, 둘 다 없을 때만 번호 블록. 카드 UI가 있는 척하지 마
- [ ] 프리셋을 고정값으로 쓰지 마 — 인터뷰 + 환경스캔으로 동적 조정
- [ ] 공식 용어(Agent Teams/Workflow/Opus/Sonnet/Fable/Codex/agy/gjc/grok)를 메타포로 대체하지 마 — 그대로 쓰고 한글 병기. 내부 구현(스폰 호출/파일 경로)만 비노출
- [ ] 인터뷰 질문 4개 이상 하지 마 / **첫 표면·회피 답을 진짜 니즈로 채택하지 마(§2a)** / 이미 구체적인 요청에 과잉질문하지 마(§2c)
- [ ] 역할 추천을 이유로 사용자가 지정한 모델을 바꾸지 마 — 품질 우려는 설명하고 변경 승인을 받는다
- [ ] Haiku를 자동 추천·자동 대체하지 마 — 사용자 명시 요청 때만
- [ ] 같은 family끼리의 형식적 검토를 기본으로 삼지 마 — Codex→grok→agy→네이티브 적대 인스턴스. 폴백일 땐 refute 프롬프트
- [ ] Workflow 경로에서 공유 메모리·도메인 카드를 만들지 마
- [ ] 팀장에게 코드/검색/문서 작성을 시키지 마 (최종 통합 리포트만 예외) / 팀장을 스폰하지 마 — 로컬이 팀장
- [ ] 에러 메시지를 그대로 보여주지 마
- [ ] 공유 메모리 초기화 없이 팀원을 스폰하지 마 / 팀원 프롬프트에서 공유 메모리 경로·경계 블록을 빠뜨리지 마
- [ ] 두 팀원의 write_scope가 겹치는 상태로 스폰하지 마 — 공유 파일은 소유자 1명
- [ ] 심부름꾼 모델도 선택 맵을 따르고, 미지정 역할을 임의 추가하지 마
- [ ] 검증 없이 결과를 유저에게 전달하지 마 / 기본 2라운드 한도를 승인 없이 넘기지 마
- [ ] 팀 재구성 시 공유 메모리 파일을 삭제하지 마 — 새 팀에 전달
- [ ] 도메인 카드를 archetype 본문 복붙으로 채우지 마 / 도메인 살 4종 중 하나라도 빠뜨리지 마 / 한 팀원에게 두 archetype을 강제하지 마
- [ ] LLM 자체 지식으로 합성 가능한데 외부 fetch부터 하지 마
- [ ] 사이드카를 fire-and-forget 하지 마 — 중간 산출 정독 + 재지시 / 산출물이 완성됐는데 남은 에이전트를 무한정 기다리지 마

## 항상 해 (전체 워크플로우)

- [ ] 사전 준비에서 런 장부 생성 + `work{repo,report,contract}` 기록 (git repo 대상일 때)
- [ ] 모든 §A 블록에 "(추천)" 1번 옵션 + "모르면 1번으로" 안내 + "문장으로 직접 적기" escape
- [ ] Step 3.5 절단선 진단 결과와 근거를 1~2문장으로 표시하고 장부 `diagnosis`에 기록
- [ ] 팀 구성 제안 시 역할을 일상 용어로 설명 + 공식 용어 한글 병기 + 예상 소요시간 + `{KKIRIKKIRI_DIR}/agents/` 경로 목록
- [ ] 구성 확인에 모델 선택 문항을 함께 넣고(`model-selection.md`), 선택 맵을 장부·카드·스폰에 저장 (이미 지정한 모델은 재질문 금지)
- [ ] 팀 실행 전 반드시 유저 확인 (Workflow는 W3 설계 카드)
- [ ] 환경 스캔에서 node + Codex/agy/gjc/grok CLI + 기존 에이전트(`.codex/agents/`) + agency-agents 설치 여부 확인
- [ ] Workflow 명세의 모든 agent()에 선택된 phase별 model 명시 + adversarial-verify 스테이지 + schema + 예산 필드 + 폭 ≤6, 그리고 `wf-lint.js --models-json` 통과
- [ ] 팀 생성 직후 공유 메모리 3종 초기화 (DEAD_ENDS 포함)
- [ ] 팀원 스폰 전 도메인 카드 합성(archetype + 4종 살 + 경계 블록, 100~150줄) → `card-lint.js --dir` exit 0
- [ ] 팀원마다 스폰 직전 gate-spawn 자가 점검(도구/write_scope/stop + C5 교집합 + model-selection.js) → 장부 `declarations[]` 기록
- [ ] 팀원 프롬프트에 archetype 본문(team-prompts.md) + 도메인 카드 경로 + 승인된 경계 값 + 공유 메모리 경로 + 심부름꾼 스폰 방법 포함
- [ ] 팀장(로컬) R&R + 능동 코디네이션 내재화 (collect-at-end 금지), 카드 인덱스를 TEAM_PLAN.md에 유지
- [ ] 백그라운드 잡·팀원은 spawn +10분과 전환점마다 mtime으로 생존 확인, 사망 시 재가동 1회 → 폴백 → `liveness_events` 기록
- [ ] 1라운드 완료 후 반드시 품질 판정 (목표 달성/완성도/정확성/일관성) + `done-gate.js` 실행 → `outcome_gate` 기록
- [ ] 품질 부족 시 유저에게 2라운드 진행 여부 확인 / 팀 재구성 시 TEAM_FINDINGS.md를 새 팀에 전달
- [ ] 팀장의 최종 통합 전 공유 메모리 3개 파일 전부 읽기
- [ ] 기존 에이전트 발견 시 재활용 여부 사용자에게 확인 / 파일 모드(@파일명) 입력 시 파일 분석 → 역할 자동 분해
- [ ] 작업 완료 후 팀 저장 여부 확인 / 저장된 팀 재사용 요청 시 saved-teams에서 불러오기
- [ ] 결과 리포트에 팀 구성(또는 처리 규모) + 작업 과정 + 산출물 + 게이트 결과 + 미해결 항목 포함, 장부 `outcome`을 채워 닫기
