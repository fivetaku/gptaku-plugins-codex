---
name: vibe-sunsang-growth
description: Generate an AI-collaboration growth report from converted Codex conversations using the v2 level system (6 axes × 7 levels, 0.5 increments), with longitudinal tracking. Offloads heavy analysis to a spawned sub-agent when available, else runs inline. Use when the user says "성장 리포트", "성장 분석", "얼마나 성장했는지", "레벨 체크", "성장 트래킹", or "growth report".
---

# vibe-sunsang-growth for Codex

> AI 활용 세션 데이터를 분석하여 성장 리포트를 자동 생성 (서브에이전트 위임, 유형별 맞춤, v2 6축 분석).

Codex는 skill-first다 (`command-routes/` 없음). 객관식은 Codex CLI에 카드 UI가 없으므로 `shared/questioning-policy.md §A` 번호 블록으로 채팅에서 묻는다.

## 참조 경로

- 대화 로그: `~/vibe-sunsang/conversations/`
- 인덱스: `~/vibe-sunsang/conversations/INDEX.md`
- 지식 베이스: `$PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/`
- 유형 설정: `~/vibe-sunsang/config/workspace_types.json`
- 결과 저장: `~/vibe-sunsang/exports/`
- 종단 로그: `~/vibe-sunsang/growth-log/TIMELINE.md`
- 변환 스크립트: `$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py`

## 실행 방식: sub-agent 분리(선택) 또는 인라인

이 스킬은 대량의 세션 파일을 분석하므로, 가능하면 **메인 컨텍스트 보호**를 위해 Codex의 multi-agent로 sub-agent를 spawn하여 무거운 분석을 분리한다. 이때 **아래 Step 4의 v2 지침 전체를 프롬프트로 직접 전달**한다. (Codex 플러그인 스키마에는 별도 에이전트 로스터 파일이 없으므로, 정의 파일 없이 런타임 spawn에 지침을 그대로 넘긴다.)

> sub-agent spawn이 불가능하거나 사용자가 인라인을 원하면, 이 스킬이 직접 아래 v2 지침대로 분석을 수행한다 — 동작·산출물은 동일하다.

## Step 0: 사전 확인

`~/vibe-sunsang/config/workspace_types.json`이 있는지 확인한다. 없으면:
> "아직 바선생 초기 설정이 안 됐어요. '바선생 시작'(vibe-sunsang-onboard)을 먼저 실행해주세요." → 종료

## Step 1: 범위 선택

사용자가 범위를 명시했으면 그대로 사용한다. 없으면 `shared/questioning-policy.md §A` 번호 블록:

```text
질문: 성장 리포트를 어떤 범위로 생성할까요?
1. 최근 2주 (추천) — 일반 리뷰 주기. 6축 + 레이더 차트 + 안티패턴 + v2 레벨 판정 + 행동 계획 (~2분)
2. 이번 주 — 빠른 주간 리뷰 (최근 7일). 세션 요약 + 6축 + 빠른 피드백 (~1분)
3. 이번 달 — 월간 성장 추이 (최근 30일). 6축 심층 + 레벨 변화 + 정체기/돌파구 (~3분)
4. 특정 프로젝트 — 워크스페이스 전체 기간 심층 분석 (~2분)
(모르면 1번으로 진행하겠습니다)
```

4번 선택 시 → INDEX.md에서 워크스페이스 목록을 §A 번호 블록으로 보여주고 고르게 한다.

## Step 2: 워크스페이스 유형 확인

`~/vibe-sunsang/config/workspace_types.json`을 읽어 분석 대상의 유형을 확인한다:
- 특정 프로젝트 → 해당 워크스페이스 유형
- 기간 기반 → 포함된 워크스페이스들의 유형 목록 수집
- 유형 미등록 워크스페이스 → `default_type` (builder)

## Step 3: 변환 확인

위임 전 최신 데이터가 있는지 확인한다:
1. `~/vibe-sunsang/conversations/INDEX.md` 확인
2. 필요하면 변환을 먼저 실행:
   ```bash
   python3 "$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py" --output-dir "$HOME/vibe-sunsang/conversations" 2>/dev/null || python "$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py" --output-dir "$HOME/vibe-sunsang/conversations"
   ```

## Step 4: 서브에이전트 위임

진행 메시지를 먼저 출력한다:
> "성장 리포트를 생성하고 있습니다. v2 레벨 시스템(6축 기술 차원 분석)으로 세션 데이터를 분석하는 중이니 잠시만 기다려주세요..."

그 다음 sub-agent를 spawn한다 (Codex multi-agent) — 불가 시 인라인으로 직접 수행. 어느 경로든 다음 지침을 **반드시** 분석 프롬프트로 사용한다:

```text
성장 리포트를 생성해주세요.
- 범위: [파악한 범위]
- 워크스페이스 유형: [workspace_types.json에서 파악한 유형 정보]
- 유형별 지식 베이스 경로: $PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/{type}/
- 공통 지식 베이스: $PLUGIN_ROOT/skills/vibe-sunsang-knowledge/references/common/
- 대화 로그 경로: ~/vibe-sunsang/conversations/

[v2 레벨 시스템 지침]
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
- 6축 레이더 차트(텍스트), 레벨 카드, 게이트 상태 테이블 포함
- 승급 시 승급 메시지 포함 (L4→L5는 '80%의 벽' 특별 이벤트)

~/vibe-sunsang/conversations/ 에서 세션 파일을 읽고, 해당 유형의 지식 베이스 기준으로 분석한 후,
~/vibe-sunsang/exports/growth-report-YYYY-MM-DD.md 로 저장해주세요.
```

**중요**: 유형 정보, 경로, v2 지표 지침을 반드시 전달한다.

## Step 5: 결과 전달

서브에이전트가 반환한 결과를 사용자에게 전달한다:
- 저장된 리포트 파일 경로
- 현재 레벨과 6축 점수 요약
- 레이더 차트 (텍스트)
- 주요 성장 포인트
- 다음 단계 제안 (최대 3개, 가장 약한 축 중심)

메인 컨텍스트에는 **요약만** 남기고, 상세는 리포트 파일을 참조하도록 안내한다.

## Step 6: 종단 추적 확인

서브에이전트가 리포트를 저장한 후:
1. `~/vibe-sunsang/growth-log/TIMELINE.md`가 업데이트되었는지 확인.
2. 안 됐으면 수동으로 업데이트 (6축 점수 열 포함):
   ```markdown
   | 날짜 | 레벨 | DECOMP | VERIFY | ORCH | FAIL | CTX | META | 요청품질 | 주요 안티패턴 | 변화 포인트 |
   ```
3. 종단 요약 제공:
   - "N주 전 대비 레벨 LX.X → LY.Y"
   - "가장 크게 성장한 축: [축명] (X.X → Y.Y)"
   - "해소된 안티패턴: [목록]"
   - "다음 레벨까지: [게이트 조건 또는 약한 축]"

## Gotchas

- 서브에이전트가 TIMELINE.md 업데이트에 실패할 수 있다. Step 6에서 반드시 확인하고 보완한다.
- 첫 리포트면 종단 요약 대신 "첫 리포트가 생성되었습니다. 다음 리포트부터 6축 성장 추이를 비교할 수 있어요."라고 안내한다.
- v1.x 이전 리포트와 종단 비교 시 6축 데이터가 없을 수 있다. 이 경우 레벨과 요청 품질만 비교한다.

## 에러 처리

| 상황 | 메시지 |
|------|--------|
| 세션 파일이 없음 | "아직 변환된 대화가 없어요. '변환해줘'(vibe-sunsang-retro)를 먼저 실행해주세요." |
| 변환 스크립트 실패 | "대화 파일 변환에 문제가 생겼어요. `~/.codex/sessions/`가 있는지 확인해주세요." |
| 서브에이전트 실패 | "분석 중 문제가 발생했어요. 다시 한번 시도해볼까요?" (또는 인라인 분석으로 폴백) |
| INDEX.md 없음 | "인덱스 파일이 없어요. '변환해줘'로 먼저 대화를 변환해주세요." |
| 유형 정보 없음 | "워크스페이스 유형이 설정되지 않았어요. '바선생 시작'을 먼저 실행해주세요." |

## Guardrails

- 점수는 객관적 정체성 라벨이 아니라 코칭 신호로 다룬다.
- 세션 3개 미만이면 과적합하지 말고 리포트를 예비(preliminary)로 표시한다.
- 보이는 세션 증거를 인용한다.
- Codex CLI에는 `question prompt` 카드 UI가 없다 → `shared/questioning-policy.md §A` 번호 블록을 쓴다.
