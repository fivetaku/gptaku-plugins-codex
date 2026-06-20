---
name: skillers-suda
description: 스킬러들의 수다 — 4명의 전문가 관점이 수다 떨며 바이브코더의 아이디어를 동작하는 Codex 스킬로 변환한다. Use when the user asks to "스킬 만들어줘", "스킬러들의 수다", "수다", "Codex 스킬 만들어줘", "이 스킬 개선해줘", "skill builder", "make a skill", "create a skill", "build a skill", "improve this skill".
---

# 스킬러들의 수다 (Codex)

> 4명의 전문가 관점으로 아이디어를 다각도로 분석하고, 그 결과로 바이브코더의 아이디어를 동작하는 **Codex 스킬**로 변환한다.

**이 문서는 참고 자료가 아니라 실행 지시서다.** 트리거되면 즉시 워크플로우를 시작한다.

이 스킬은 **Codex 스킬**을 만든다 — 결과물은 `SKILL.md` + 선택적 `references/`·`scripts/`·`assets/`다. Codex에는 `commands/` 슬래시 커맨드 폴더도, `agents/` 폴더도 없다. 진입은 항상 description 트리거로 이뤄진다.

먼저 읽기:
- `references/interview-guide.md` — 인터뷰 방법론 + 4 관점 분석
- `references/personas.md` — 4 관점 동적 생성
- `references/writing-style-guide.md` — Codex SKILL.md 작성 규칙

필요할 때 읽기:
- `references/workflow-step-types.md` — 6가지 단계 타입과 선택 기준
- `references/component-decision.md` — 스킬/플러그인/레퍼런스/스크립트 판단
- `references/trigger-mechanism.md` — description 트리거 최적화
- `references/eval-guide.md` · `references/schemas.md` — eval 설계와 스키마
- `references/improvement-principles.md` — 반복 개선 원칙
- `references/mcp-catalog.md` · `references/api-mcp-integration.md` — 외부 연동
- `references/script-templates.md` — Python/Bash 스크립트 템플릿
- `references/plugin-package-guide.md` — 플러그인 패키지로 묶을 때
- `references/agents/grader.md` · `comparator.md` · `analyzer.md` — eval 채점/비교/분석 프롬프트

## 질문 원칙 (shared/questioning-policy.md)

아이디어를 캐낼 때 가정형 말고 **과거 실제 행동**을 묻는다(§1.3, Mom Test): "이 기능 쓰실래요?"(X) 대신 "지금은 이 문제를 어떻게 해결하세요?"(O). 표면·예의·회피 답을 결론으로 받지 말고 한 번 더 구체 탐침한다(§2a·§2b). 하지만 사용자가 이미 스스로 진단했거나 요청이 이미 충분히 구체적이면 더 캐묻지 말고 즉시 진행한다(§2c). 추론 가능한 건 묻지 않는다(§1.1) — 물어야 하면 "기본값 제시 + 확인" 형태로.

## 질문 렌더링 — §A 번호형 선택지 (Codex 전용)

Codex CLI에는 `AskUserQuestion` 같은 객관식 카드 UI가 **없다.** 모든 선택 질문은 `shared/questioning-policy.md §A`대로 **채팅에 번호형 선택지 블록**을 출력하고 다음 자유 텍스트 답변을 읽는다.

표준 블록 포맷:

```text
예시 프리뷰            ← 구조를 보여줄 때만. 단순 선호 질문이면 생략.
  [User] --1:N--> [Skill]      (매번 인터뷰 결과로 새로 생성, 하드코딩 금지)

질문: <한 줄 질문>
1. <추천안> — 무엇인지, 왜 좋은지, 트레이드오프
2. <대안> — 무엇인지, 트레이드오프
3. 문장으로 직접 수정 요청
(여러 개 고를 수 있으면: "여러 개면 1,3처럼 적어주세요")
```

- 추천안은 항상 **1번**에 둔다.
- "잘 모르겠어요"는 별도 선택지로 만들지 말고 "모르면 1번으로 진행하겠습니다"로 안내한다.
- 핵심 문제 발굴(Phase A 첫 턴)은 번호 블록 대신 **열린 텍스트 질문**으로. 단순 분류/설정 고르기일수록 번호 블록이 적합하다.

## 진입점 판단

사용자가 어디에 있는지 파악하고 거기서 시작한다.

| 상황 | 시작 지점 |
|------|----------|
| 아이디어 없음 | Phase A (아이디어 수집) |
| 아이디어 있음 (요청에 포함) | Phase B (4 관점 분석) |
| 대화에 이미 워크플로우가 있음 ("이걸 스킬로 만들어줘") | 대화에서 추출 → Phase D (워크플로우 확인) |
| 이미 SKILL.md 드래프트가 있음 ("이 스킬 개선해줘") | Phase F (eval 실행) |
| 기존 스킬 분석 요청 ("이 스킬 분석/검토해줘") | 스킬 분석 모드 |

사용자가 "eval 안 해도 돼, 그냥 바이브로 가자"라고 하면 eval을 스킵하고 대화형으로 진행한다.

## 워크플로우

### Phase A: 아이디어 수집

만들고 싶은 스킬의 핵심 아이디어를 파악한다.

**대화 컨텍스트 추출 먼저:** 현재 대화에 이미 워크플로우가 있으면("이걸 스킬로 만들어줘") 대화 히스토리에서 답을 먼저 추출한다 — 사용된 도구, 단계 순서, 사용자가 한 수정, 입출력 형식. 빈 부분만 채우고 확인받는다.

요청에 아이디어가 포함됐으면 그대로 사용한다. 없으면 **열린 텍스트 질문 하나**로 묻는다(번호 블록 아님 — §A·§1.2):

```text
어떤 스킬을 만들고 싶으세요? 한 문장으로 말해주세요.
(예: "유튜브 댓글을 분석해서 인사이트를 뽑아줘", "회의록을 요약하고 액션 아이템 뽑아줘")
```

아이디어가 모호하면(예: "좋은 스킬") **과거 행동 앵커**로 1개 더 묻는다(§2b): "지금은 그걸 어떻게 하고 계세요?". 이미 구체적이면 바로 Phase B로(§2c).

### Phase B: 4 관점 분석 + 토론

**목표:** 아이디어를 4 관점에서 다각도로 분석한다. 검증 다중성을 위해 **인원수 4는 유지**하되, 4명의 정의는 매번 사용자 아이디어의 도메인을 보고 동적 생성한다(`references/personas.md`).

기본 4 관점(도메인 미특정 시):
- **기획자** — 방향·범위·MVP: "누가 쓸 건데? 뭘 해결하는 거야?"
- **사용자** — UX·진입장벽: "나라면 이걸 어떻게 쓸까?"
- **전문가** — 기술 실현성·워크플로우: "이 분야는 이런 점을 조심해야 해"
- **검수자** — 엣지 케이스·실패: "이거 이 경우에도 돼?"

**분석 실행 (Codex 방식):** 기본은 **메인 스레드에서 4 관점을 직접 종합**한다 — 각 관점을 순서대로 적용해 아이디어를 분석한다(`references/interview-guide.md` §2-1의 4개 분석 항목 템플릿 사용). 사용자가 명시적으로 "전문가 팀 불러줘 / 병렬로 깊게 봐줘"라고 요청하고 환경이 sub-agent 위임을 지원할 때만, 최대 4개의 bounded sub-agent로 위임한다. 위임이 불가능하면 조용히 메인 스레드 종합으로 진행한다 — 존재하지 않는 도구를 가정하지 않는다.

**종합 출력 형식:**

```text
4 관점으로 분석했어요:

기획자: "{한줄 요약}"  → {핵심 1-2줄}
사용자: "{한줄 요약}"  → {핵심 1-2줄}
전문가: "{한줄 요약}"  → {핵심 1-2줄}
검수자: "{한줄 요약}"  → {핵심 1-2줄}

종합: {4 관점을 통합한 방향 제안 2-3줄}
```

**의견 충돌은 반드시 노출한다.** 충돌이 있으면 그 충돌 자체를 §A 번호 블록의 질문으로 만든다:

```text
질문: 커맨드 분기가 필요할까요, 단일 스킬이 나을까요?
1. 단일 스킬 (추천) — Codex는 슬래시 커맨드가 없고 트리거가 자연스러움
2. 인수 기반 분기를 SKILL.md 안에서 처리 — 진입 경로가 여러 개일 때
3. 문장으로 직접 수정 요청
```

충돌이 없으면 합의 방향을 짧은 프리뷰(MVP 범위 / 핵심 워크플로우 / 컴포넌트 타입)로 보여주고 §A 블록으로 확인받는다. "다시 토론해줘"를 고르면 추가 정보를 받아 Phase B를 다시 실행한다.

### Phase C: 상세 인터뷰 (0–2개, 필요시만)

팀 분석에서 자동 판단한 항목(purpose / input_type / output_type / trigger_keywords / domain / constraints)은 다시 묻지 않는다. **불확실한 것만** §A 번호 블록으로 최대 2개 묻는다. 충분히 파악됐으면 이 Phase를 스킵하고 Phase D로 간다(§2c).

단순 확인("혹시 이런 뜻인가요?")은 자연 대화로 처리한다 — 굳이 번호 블록을 강제하지 않는다.

### Phase D: 워크플로우 설계 + 확인

팀 분석 + 사용자 답변으로 워크플로우를 설계한다. 6가지 단계 타입을 조합한다(`references/workflow-step-types.md`):

1. **prompt** — Codex가 추론하는 단계 (분석·요약·판단·창작)
2. **script** — 반복/일관성/API 작업용 Python/Bash
3. **api_mcp** — 외부 연동 (API > MCP/App > 직접 구현 우선순위)
4. **rag** — `references/` 참조 검색
5. **review** — 검토 게이트 (api_mcp/rag 뒤에 **반드시** 포함)
6. **generate** — 최종 출력 (파일 생성, 보고서)

**컴포넌트 타입 (Codex):** 기본값은 **스킬**이다. 여러 스킬·자산·메타데이터·MCP 설정을 한 제품으로 묶어야 하면 **플러그인 패키지**(`references/plugin-package-guide.md`). 큰 표·스키마·예시는 **레퍼런스**로, 결정적 작업은 **스크립트**로 분리한다. Claude Code의 command/agent 컴포넌트는 Codex에 없으므로 제안하지 않는다(`references/component-decision.md`).

**자유도(Degrees of Freedom) 식별:** 고정 요소(워크플로우 구조·단계 순서·필수 검증)와 가변 요소(출력 언어·상세도·포맷)를 구분한다. 가변 요소가 있으면 SKILL.md에 **기본값 + 변경 방법**을 명시한다.

**Eval 기준 정의:** 검수자 관점의 엣지 케이스를 활용해 eval 시나리오를 정의한다. should-trigger 2–3개 + should-not-trigger 1–2개. 현실적이고 구체적인 프롬프트로 작성한다(파일 경로·약어·캐주얼 표현을 섞는다). 상세: `references/eval-guide.md`, 스키마: `references/schemas.md`.

**Step D-1:** 단계별 흐름 + eval 시나리오 목록을 보여준다.
**Step D-2:** §A 번호 블록으로 확인받는다 — `1. 이대로 진행 (추천) / 2. 수정할 부분 있어 / 3. 나중에 할게`.

### Phase E: 파일 생성

확인된 워크플로우를 실제 파일로 만든다. **Codex 스킬 파일 구조:**

```text
skills/{skill-name}/
├── SKILL.md              # 워크플로우 (간결하게, references로 분리)
├── scripts/              # script 타입 단계용
├── references/           # rag 타입 + 큰 문서
└── assets/               # 출력에 직접 쓰는 파일 (컨텍스트에 로드 안 함)
```

`commands/`·`agents/` 폴더는 만들지 않는다 — Codex에 없는 컴포넌트다.

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
{명령형 실행 지침}

## References / Scripts / Assets
- **`references/{file}.md`** — {설명}

## Settings (가변 요소가 있을 때만)
| 설정 | 기본값 | 변경 방법 |
```

**경로는 `$PLUGIN_ROOT` 기준으로 작성한다** — 예: `python3 $PLUGIN_ROOT/skills/{skill-name}/scripts/{file}.py`. `$PLUGIN_ROOT`는 Codex가 플러그인 실행 시 플러그인 루트로 설정하는 환경 변수다.

**Description 작성 (`references/trigger-mechanism.md`):**
- **Pushy** — 무엇을 하는지 + 구체적 트리거 상황을 함께. BAD: `"코드 리뷰 도구"` / GOOD: 트리거 문구 + "Make sure to use this skill whenever the user mentions code review."
- **Why** 포함 — "무엇을"뿐 아니라 "왜".
- 한국어 + 영어 트리거 모두.
- 단순 질문이 아닌 복잡한 요청에 반응하도록.

**Writing Style (`references/writing-style-guide.md`):**
- **명령형(imperative)** — "Read the file. Validate the input." / "You should…" 금지.
- description은 **third-person** — "This skill should be used when…".
- **Why 설명 우선** — ALWAYS/NEVER 대신 이유를. Codex는 이유를 이해하면 더 잘 따른다.
- **간결** — 본문은 핵심만, 상세는 `references/`로. 컨텍스트는 공공재다.
- **규율형(Discipline) 스킬이면 합리화 차단 장치 필수** — "X 전에 반드시 Y"를 강제하는 스킬이면 Iron Law + 합리화 차단표 + Red Flags + Spirit vs Letter 4종을 포함한다. 번역·포맷팅 같은 기법형엔 넣지 않는다(토큰 낭비). 판별·템플릿: `references/writing-style-guide.md` §6.

**스크립트:** Python 우선(크로스플랫폼). 에러는 stderr, 결과는 JSON stdout. 표준 라이브러리 우선, 런타임 `pip install` 금지. 템플릿: `references/script-templates.md`.

**파일 덮어쓰기:** 같은 이름 파일이 있으면 사용자에게 확인한다. 동의 없이 덮어쓰지 않는다.

### Phase E-verify: 구조 자동 검증

파일 생성 직후 Codex 스킬 검증 스크립트를 실행한다:

```bash
python3 $PLUGIN_ROOT/skills/skillers-suda/scripts/quick_validate.py <생성된 스킬 디렉토리>
```

`PASS`면 Phase F로. `FAIL`이면 항목별로 수정 후 재검증한다:
- frontmatter 누락 → YAML frontmatter 추가
- name kebab-case 위반 → 소문자-하이픈으로 변환
- description 누락/과길이(>1024자) → 보강 또는 축약
- 참조 경로 없음 → 누락 파일 생성 또는 참조 제거

### Phase F: Eval 실행 + 검토

Phase D에서 정의한 eval 시나리오를 실행한다. 기본은 **사람이 읽는(human-readable) eval**부터 — 각 시나리오를 직접 실행해 트리거 정확도, 첫 행동의 명확성, 출력 유용성을 본다. 안정화된 뒤에만 자동화를 추가한다.

엄밀 비교가 필요하면 with-skill / without-skill 두 실행을 비교한다. 채점은 `references/agents/grader.md`, 블라인드 A/B 비교는 `references/agents/comparator.md`, 패턴 분석은 `references/agents/analyzer.md`의 프롬프트를 사용한다.

**eval은 사용자 눈으로 확인한다.** AI가 자체 판단으로 "잘 됐다"고 결론내면 문제를 놓친다. 결과를 사용자에게 보여주고 §A 블록으로 다음을 정한다 — `1. 다음 단계로 / 2. 개선 필요 / 3. eval 케이스 수정`.

### Phase G: 반복 개선

피드백 기반으로 개선한다(`references/improvement-principles.md`):
1. **일반화** — 특정 eval만 통과하도록 하드코딩하지 않는다. 케이스가 아닌 패턴을 해결한다.
2. **Lean 유지** — 효과 없는 지시를 제거한다.
3. **Why 설명** — 이유를 설명한다.
4. **반복 코드 번들** — 실행에서 같은 스크립트가 반복되면 스킬에 번들한다.

수정 → 재실행 → 비교 → 사용자 리뷰를 만족하거나 의미 있는 개선이 없을 때까지 반복한다.

### Phase H: Description 최적화

should-trigger / should-not-trigger 쿼리로 트리거 정확도를 점검한다. 현실적 프롬프트로 작성하고, best description을 SKILL.md frontmatter에 적용한 뒤 before/after를 사용자에게 보여준다. 상세: `references/trigger-mechanism.md`.

### Phase I: 마무리

변경한 경로, 검증 결과(quick_validate PASS), 남은 리스크를 짧게 보고한다. 플러그인 패키지로 묶었으면 `.codex-plugin/plugin.json`을 JSON 파싱으로 검증한다(`references/plugin-package-guide.md`).

## 스킬 분석 모드

"이 스킬 분석해줘 / 검토해줘" 요청 시:

1. 대상 스킬의 SKILL.md(+ 주요 references)를 읽고 frontmatter·워크플로우를 파싱한다.
2. 4 관점으로 분석한다 — 기획자(목적·트리거), 사용자(쓰기 쉬운가), 전문가(워크플로우·스크립트 적절성), 검수자(엣지 케이스·에러 핸들링).
3. 구체적 개선안을 제안한다 — description(Pushy·undertrigger 방지), 워크플로우 정제, 누락된 review 단계, 엣지 케이스 보강.
4. §A 번호 블록으로 확인받는다 — `1. 개선안 적용 (추천) / 2. 일부만 수정 / 3. 지금은 유지`. 적용 시 Edit로 수정하되, 덮어쓰기 전 변경 내용을 미리 보여주고 확인받는다.

## 핵심 원칙

- **수백만 번 쓸 사용자를 위해 만든다** — 눈앞 예시만 통과하는 게 아니라 다양한 상황에서 안정적으로 동작하는 스킬이 목표다.
- **인터뷰 먼저, 파일 나중** — 의도를 충분히 파악해야 재작업이 줄어든다.
- **4 관점은 진짜로 다르게** — 같은 관점을 4번 반복하면 다각도 검증의 가치가 사라진다. 인원수 4를 유지하되 매번 도메인에 맞게 정의한다.
- **eval은 사용자 눈으로** — 자체 판단으로 통과시키지 않는다.
- **일반화** — 개별 실패가 아니라 실패의 패턴을 해결한다.
- **쉬운 말** — 사용자는 바이브코더다. 전문 용어엔 항상 쉬운 설명을 붙인다.
- **외부 데이터는 검토 후 사용** — api_mcp/rag 결과를 그대로 출력에 넣지 않는다. review 단계를 거친다.
- **Codex 네이티브** — 만드는 스킬도, 이 스킬 자신도 commands/agents 없이 SKILL.md로 동작한다. 존재하지 않는 도구(AskUserQuestion 카드 등)를 가정하지 않는다.
