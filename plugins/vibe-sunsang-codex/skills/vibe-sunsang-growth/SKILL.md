---
name: vibe-sunsang-growth
description: 'Growth report generator — analyzes converted Codex conversations and produces a progression report using the v2 level system (6 axes × 7 levels, 0.5 increments), leading with one level headline and up to three next moves. Offloads heavy analysis to a runtime-spawned sub-agent when available, else runs inline. Korean triggers: "성장 리포트", "성장 분석", "얼마나 성장했는지", "레벨 체크", "성장 트래킹". English triggers: "growth report", "growth tracking", "level check".'
---

# Growth - 성장 리포트 생성 스킬 (Codex)

> AI 활용 세션 데이터를 분석하여 성장 리포트를 자동 생성 (서브에이전트 위임, 유형별 맞춤, v2 6축 분석)

Codex는 skill-first다 (별도 커맨드 파일 없음). 객관식은 `$PLUGIN_ROOT/shared/questioning-policy.md §A`의 질문 도구(`request_user_input_async`, Plan 모드는 `request_user_input`)로 묻고, 두 도구가 모두 없을 때만 번호 블록으로 채팅에서 묻는다. async 도구는 부른 뒤 한 줄 안내만 쓰고 턴을 끝낸다(답은 다음 메시지로 온다). 아래 번호 블록 예시는 폴백일 때의 모양이다. 열린 코칭 질문은 도구 없이 평범한 채팅으로 묻는다.

async 호출 형식: `{"questions":[{"title":"헤더 — 질문","options":["추천안 (추천) — 설명","대안 — 설명"]}]}`. 문항에는 `title`·`options`(문자열 배열)만 넣는다. `question`·`header`·`id`는 Plan 모드 `request_user_input` 전용이라 async에 넣으면 파싱 오류가 난다. "기타·직접 적기" 선택지는 넣지 않는다(자유 입력 칸이 자동으로 붙는다).

## 참조 경로

- **대화 로그**: `~/vibe-sunsang/conversations/`
- **인덱스**: `~/vibe-sunsang/conversations/INDEX.md`
- **지식 베이스**: `$PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/`
- **유형 설정**: `~/vibe-sunsang/config/workspace_types.json`
- **결과 저장**: `~/vibe-sunsang/exports/`
- **종단 로그**: `~/vibe-sunsang/growth-log/TIMELINE.md`
- **분석 지침(서브에이전트용)**: `$PLUGIN_ROOT/skills/vibe-sunsang-growth/references/growth-analyst.md`
- **스크립트**: `$PLUGIN_ROOT/scripts/ensure_workspace.py`, `analysis_scope.py`, `convert_sessions.py`

## 실행 방식: sub-agent 분리(선택) 또는 인라인

이 스킬은 대량의 세션 파일을 분석하므로, 가능하면 **메인 컨텍스트 보호**를 위해 Codex의 multi-agent로 sub-agent를 spawn하여 무거운 분석을 분리한다. Codex 플러그인 스키마에는 별도 에이전트 로스터 파일이 없으므로, 본진 `growth-analyst` 에이전트의 지침은 `references/growth-analyst.md`에 임베드되어 있고, 런타임 spawn 프롬프트에서 **그 파일을 읽고 따르라**고 지시한다.

> sub-agent spawn이 불가능하거나 사용자가 인라인을 원하면, 이 스킬이 직접 `references/growth-analyst.md`를 읽고 그대로 분석을 수행한다 — 동작·산출물은 동일하다.

### Step 0: 워크스페이스 자동 치유 (dead-end 방지)

파일 존재만 확인하고 튕기지 않는다. 다음으로 워크스페이스를 스스로 준비한다:

```bash
python3 "$PLUGIN_ROOT/scripts/ensure_workspace.py" 2>/dev/null || python "$PLUGIN_ROOT/scripts/ensure_workspace.py"
```

출력 마지막 줄 `STATUS ...  CONFIG <present|absent>`로 분기:

- `v1_migrated` → "이전 버전 데이터를 새 구조로 옮겼어요." 한 줄 안내 후 계속.
- `CONFIG absent` (fresh) → "처음이시네요 — 바로 준비할게요!" 후 **vibe-sunsang-onboard로 넘긴다**. 여기서 종료하지 말 것.
- 그 외 → 다음 단계.

### Step 1: 범위 선택

**기본은 "지난 리뷰 이후"다.** 먼저 증분 범위를 계산해 사용자에게 무엇이 새로 생겼는지 보여준다:

```bash
python3 "$PLUGIN_ROOT/scripts/analysis_scope.py" --new 2>/dev/null || python "$PLUGIN_ROOT/scripts/analysis_scope.py" --new
```

마지막 줄 `SUMMARY total=.. matched=.. new=.. continued=.. watermark=..`를 읽는다.

- `watermark=none`(첫 리뷰)이거나 사용자가 명시적으로 범위를 말한 경우 → 아래 §A 질문 도구로 범위를 고르게 한다(폴백은 번호 블록).
- 그 외 → "지난 리뷰({watermark}) 이후 **새 세션 {new}개, 이어서 진행한 세션 {continued}개**가 있어요. 이걸 바로 분석할까요, 아니면 다른 범위로 볼까요?" 라고 안내한 뒤, 사용자가 다른 범위를 원하지 않으면 **증분 범위(analysis_scope가 출력한 md 경로 목록)를 그대로 분석 대상으로 삼는다.** `matched=0`이면 "지난 리뷰 이후 새로 이어간 대화가 없어요. 전체 기간으로 볼까요?"로 안내.

**사용자가 다른 범위를 원하거나 첫 리뷰면** `shared/questioning-policy.md §A` 질문 도구 1콜(`request_user_input_async`, Plan 모드는 `request_user_input`; 둘 다 없으면 번호 블록 폴백). 번호 블록 폴백일 때의 모양:

```text
질문: 성장 리포트를 어떤 범위로 생성할까요?
1. 최근 2주 (추천) — 일반 리뷰 주기. 세션 트렌드 + 6축 레이더 + 안티패턴 + v2 레벨 판정(Fit Score·게이트) + 행동 계획 (~2분)
2. 이번 주 — 빠른 주간 리뷰 (최근 7일). 세션 요약 + 6축 + 빠른 피드백 (~1분)
3. 이번 달 — 월간 성장 추이 (최근 30일). 6축 심층 + 레벨 변화 + 정체기/돌파구 + 상세 행동 계획 (~3분)
4. 특정 프로젝트 — 선택한 프로젝트의 전체 기간, 해당 유형 맞춤 6축 평가 + 프로젝트별 성장 곡선 (~2분)
(모르면 1번으로 진행하겠습니다)
```

- 1~3번 → `analysis_scope.py --window-days 14|7|30`으로 대상 md 목록을 뽑는다.
- 4번 → `~/vibe-sunsang/conversations/INDEX.md`에서 프로젝트 목록을 §A 질문 도구(없으면 번호 블록)로 보여주고 고르게 한다.

### Step 2: 워크스페이스 유형 확인

`~/vibe-sunsang/config/workspace_types.json`을 읽어 분석 대상 프로젝트의 유형을 확인합니다.

- 특정 프로젝트 분석 → 해당 프로젝트의 유형 사용
- 기간 기반 분석 → 포함된 프로젝트들의 유형 목록 수집
- 유형이 등록되지 않은 프로젝트 → `default_type` (builder) 사용

### Step 3: 증분 변환 (항상 자동 선행)

별도 `변환` 실행을 요구하지 않는다. 위임 직전 **항상** 증분 변환을 돌려 이어서 진행한 대화까지 최신화한다(증분이라 이미 최신이면 즉시 끝난다):

```bash
python3 "$PLUGIN_ROOT/scripts/convert_sessions.py" --names-file "$HOME/vibe-sunsang/config/project_names.json" --output-dir "$HOME/vibe-sunsang/conversations" 2>/dev/null || python "$PLUGIN_ROOT/scripts/convert_sessions.py" --names-file "$HOME/vibe-sunsang/config/project_names.json" --output-dir "$HOME/vibe-sunsang/conversations"
```

> Step 1에서 증분 범위를 이미 계산했다면, 변환 후 새로 이어진 세션이 반영됐을 수 있으니 `analysis_scope.py --new`를 한 번 더 돌려 최종 대상 목록을 확정한다.

### Step 4: 서브에이전트 위임

사용자에게 진행 상황을 알린 후 sub-agent를 spawn합니다 (Codex multi-agent) — 불가 시 인라인으로 직접 수행.

**진행 메시지 (spawn 전 반드시 출력):**
> "성장 리포트를 생성하고 있습니다. v2 레벨 시스템(6축 기술 차원 분석)으로 세션 데이터를 분석하는 중이니 잠시만 기다려주세요..."

어느 경로든 다음 지침을 **반드시** 분석 프롬프트로 사용한다:

```text
먼저 $PLUGIN_ROOT/skills/vibe-sunsang-growth/references/growth-analyst.md 를 읽고, 그 지침(Execution Flow 0~8, Output, Language)을 그대로 따라 성장 리포트를 생성해주세요.

- 범위: [파악한 범위]
- [증분 분석인 경우] 분석 대상 세션 파일 목록(analysis_scope --new 출력): [md 경로 목록을 그대로 전달]. 이 목록에 있는 세션만 읽어 분석하세요.
- 워크스페이스 유형: [workspace_types.json에서 파악한 유형 정보]
- 유형별 지식 베이스 경로: $PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/{type}/
- 공통 지식 베이스: $PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/common/
- 대화 로그 경로: ~/vibe-sunsang/conversations/

[v2 레벨 시스템 요약 — 상세는 growth-analyst.md]
- 6대 기술 차원(DECOMP/VERIFY/ORCH/FAIL/CTX/META)별로 행동 신호를 감지하세요.
- 유형별 동적 가중치를 적용하세요:
    Builder:  DECOMP 25%, VERIFY 25%, ORCH 15%, FAIL 15%, CTX 10%, META 10%
    Explorer: DECOMP 15%, VERIFY 15%, ORCH 10%, FAIL 20%, CTX 20%, META 20%
    Designer: DECOMP 20%, VERIFY 15%, ORCH 10%, FAIL 10%, CTX 25%, META 20%
    Operator: DECOMP 15%, VERIFY 20%, ORCH 25%, FAIL 20%, CTX 10%, META 10%
- Fit Score 공식: F_L = SUM(w_i * S_i)
- 바닥 효과 보정: 첫 세션 ≥ L1.5, 3세션 + 도구 2종 ≥ L2.0
- 게이트 조건 확인: L3(구체성>0.5), L4(검증>0.15 & 수정>0.05), L5(도구>8 또는 오케스트레이션 & 전략>0.05), L6(멀티에이전트), L7(외부기여)
- 내부 소수점 2자리, 공식 0.5 단위 반올림
- 리포트 파일에는 6축 레이더 차트(텍스트), 레벨 카드, 게이트 상태 테이블 포함
- 승급 시 승급 메시지 포함 (L4→L5는 '80%의 벽' 특별 이벤트)

~/vibe-sunsang/conversations/ 에서 세션 파일을 읽고, 해당 유형의 지식 베이스 기준으로 분석한 후,
~/vibe-sunsang/exports/growth-report-YYYY-MM-DD.md 로 저장해주세요.
대화창 회신은 레벨 헤드라인 1줄 + '다음 한 수' 최대 3개 + 저장 경로만으로 끝내세요.
```

**중요**: 유형 정보, 경로, v2 지표 지침을 반드시 전달한다.

### Step 5: 결과 전달

서브에이전트가 반환한 결과를 **판정 하나 + 할 일 + 경로** 순서로 전달합니다:

1. 레벨 헤드라인 한 줄 (`## L[X.X] [레벨명]`, 직전 리포트가 있으면 `L[이전] → L[현재]`)
2. `다음 한 수` — 가장 약한 축부터 최대 3개, 한 줄에 하나
3. 저장된 리포트 파일 경로

**대화창에 쓰지 않는 것**: 6축 개별 점수, 내부 점수, 가중치, Fit Score·게이트 산식, 레이더 차트, 리포트 본문 재출력. 사용자가 "왜 그 레벨이야", "6축 보여줘", "레이더 보여줘"라고 물으면 그때 답합니다 — 근거는 리포트 파일에 전부 있습니다.

메인 컨텍스트에는 **요약만** 남기고, 상세 분석은 리포트 파일을 참조하도록 안내합니다.

### Step 6: 종단 추적 확인

서브에이전트가 리포트를 저장한 후:

1. `~/vibe-sunsang/growth-log/TIMELINE.md`가 업데이트되었는지 확인
2. 업데이트되지 않았으면 수동으로 업데이트 (6축 점수 열 포함):

```markdown
| 날짜 | 레벨 | DECOMP | VERIFY | ORCH | FAIL | CTX | META | 요청품질 | 주요 안티패턴 | 변화 포인트 |
```

3. 종단 정보는 Step 5의 헤드라인에 흡수한다 — 별도 요약 블록을 새로 만들지 않는다:
   - 레벨 변화는 헤드라인의 `L[이전] → L[현재]`로 표현
   - 가장 크게 성장한 축, 해소된 안티패턴은 **변화가 있을 때만** 한 줄로 덧붙인다
   - "다음 레벨까지"는 `다음 한 수` 목록이 이미 답한다. 중복해서 쓰지 않는다.

### Step 7: 분석 워터마크 갱신

리포트가 정상 저장되면 **반드시** 워터마크를 전진시켜, 다음 리뷰가 "이번에 본 것 이후"만 잡도록 한다:

```bash
python3 "$PLUGIN_ROOT/scripts/analysis_scope.py" --new --mark 2>/dev/null || python "$PLUGIN_ROOT/scripts/analysis_scope.py" --new --mark
```

> 리포트 저장에 실패했다면 갱신하지 않는다(다음 실행에서 다시 잡히도록). 사용자가 "전체" 등 임의 범위를 강제한 경우에도 워터마크는 최신 활동 기준으로 전진한다.

### Gotchas

- 서브에이전트가 TIMELINE.md 업데이트에 실패할 수 있다. Step 6에서 반드시 확인하고 보완한다.
- 첫 리포트일 경우 종단 요약 대신 "첫 리포트가 생성되었습니다. 다음 리포트부터 6축 성장 추이를 비교할 수 있어요."라고 안내한다.
- v1.x 이전 리포트와의 종단 비교 시 6축 데이터가 없을 수 있다. 이 경우 레벨과 요청 품질만 비교한다.
- 세션 3개 미만이면 과적합하지 말고 리포트를 예비(preliminary)로 표시한다.

### 에러 처리

문제 발생 시 비개발자가 이해할 수 있게 안내합니다:

| 상황 | 사용자에게 보여줄 메시지 |
|------|------------------------|
| 세션 파일이 없음 | "아직 변환된 대화가 없어요. Codex로 작업한 기록(`~/.codex/sessions/`)이 있는지 확인해주세요." |
| 변환 스크립트 실패 | "대화 파일 변환에 문제가 생겼어요. `~/.codex/sessions/`가 있는지 확인해주세요. 다른 위치면 `--sessions-dir`로 지정할 수 있어요." |
| 서브에이전트 실패 | "분석 중 문제가 발생했어요. 다시 한번 시도해볼까요?" (또는 인라인 분석으로 폴백) |
| INDEX.md 없음 | "인덱스 파일이 없어요. '변환해줘'(vibe-sunsang-retro)로 먼저 대화를 변환해주세요." |
| 유형 정보 없음 | "워크스페이스 유형이 설정되지 않았어요. '바선생 시작'(vibe-sunsang-onboard)을 먼저 실행해주세요." |

## Guardrails

- 점수는 객관적 정체성 라벨이 아니라 코칭 신호로 다룬다.
- 보이는 세션 증거를 인용한다. 변환된 로그에 없는 예시를 지어내지 않는다.
- 선택지 질문은 `shared/questioning-policy.md §A` 질문 도구로 묻고, 도구가 없을 때만 번호 블록을 쓴다.
