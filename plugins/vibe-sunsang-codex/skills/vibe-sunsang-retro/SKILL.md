---
name: vibe-sunsang-retro
description: Convert Codex JSONL session logs into readable Markdown and guide a retrospective with analysis templates. Use when the user says "변환", "대화 변환", "로그 변환", "회고", "이번 주 대화", "retro", or "convert conversations".
---

# vibe-sunsang-retro for Codex

> Codex 세션 로그를 읽기 좋은 Markdown으로 변환하고 분석 가이드를 제공한다.

Codex는 skill-first다 (`commands/` 없음). 객관식은 Codex CLI에 카드 UI가 없으므로 `shared/questioning-policy.md §A` 번호 블록으로 채팅에서 묻는다.

## 데이터 경로

- 원본: `~/.codex/sessions/**/*.jsonl`
- 변환 결과: `~/vibe-sunsang/conversations/`
- 인덱스: `~/vibe-sunsang/conversations/INDEX.md`
- 설정: `~/vibe-sunsang/config/`
- 리포트 저장: `~/vibe-sunsang/exports/`
- 변환 스크립트: `scripts/convert_sessions.py` (이 스킬 폴더 안)

## Step 0: 사전 확인

`~/.codex/sessions/`에 JSONL이 있는지 확인한다. 없으면:
> "아직 Codex 대화 기록이 없어요. Codex로 작업한 뒤 다시 와주세요." → 종료

`~/vibe-sunsang/`가 없으면 (미온보딩):
> "아직 바선생 초기 설정이 안 됐어요. '바선생 시작'(vibe-sunsang-onboard)을 먼저 실행해주세요." → 종료

## Step 1: 변환 스크립트 실행

인자를 분석하여 옵션을 정한다:

| 인자 | 동작 |
|------|------|
| (없음) | 증분 변환 (새 세션만 — 이미 있는 파일은 건너뜀) |
| "전체", "force", "다시" | `--force` 전체 재변환 |
| "최근 N개", `--limit N` | `--limit N` 최근 N개 세션만 (기본 30) |

```bash
# 기본: 증분 변환
python3 "$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py" --output-dir "$HOME/vibe-sunsang/conversations" 2>/dev/null || python "$PLUGIN_ROOT/skills/vibe-sunsang-retro/scripts/convert_sessions.py" --output-dir "$HOME/vibe-sunsang/conversations"

# --force: 인자에 "전체", "force", "다시" 포함 시 --force 추가
```

**특정 워크스페이스/날짜를 사용자가 지정했는데** 정확히 일치하는 게 모호하면, INDEX.md에서 후보를 읽어 `shared/questioning-policy.md §A` 번호 블록으로 묻는다:

```text
질문: 어떤 워크스페이스의 대화를 변환/검토할까요?
1. {워크스페이스1} — {세션 수}개 세션 (가장 활발, 추천)
2. {워크스페이스2} — {세션 수}개 세션
3. 문장으로 직접 알려주세요
(모르면 1번으로 진행하겠습니다)
```

> options는 INDEX.md에서 읽은 목록으로 동적 생성, 세션 수 많은 순 정렬.

### 에러 처리 (비개발자 친화)

| 상황 | 메시지 |
|------|--------|
| Python 없음 | "Python이 설치되어 있지 않아요. 터미널에서 `python3 --version`으로 확인해주세요." |
| 세션 폴더 없음 | "Codex 대화 기록을 찾을 수 없어요. `~/.codex/sessions/`가 있는지 확인해주세요." |
| 권한 오류 | "파일에 접근할 수 없어요. `~/.codex/sessions/` 폴더 권한을 확인해주세요." |
| 변환 0건 | "새로 변환할 대화가 없어요. 이미 최신 상태입니다!" |

## Step 2: 인덱스 확인

변환 후 `~/vibe-sunsang/conversations/INDEX.md`를 읽어 현황을 보여준다:
- 총 워크스페이스 수
- 총 세션 수
- 최근 변환된 세션

## Step 3: 분석 템플릿 제안

변환 완료 후 다음 분석 옵션을 제안한다:

1. **워크스페이스 패턴 분석** — "[워크스페이스명] 세션들을 분석해줘. 주요 작업 유형, 반복 에러, 도구 활용 패턴을 정리해줘."
2. **성장 트래커** → "성장 리포트 만들어줘" (vibe-sunsang-growth). v2: 6축 + 레이더 차트.
3. **멘토링 세션** → "멘토링해줘" (vibe-sunsang-mentor). v2: 6축 중심 맞춤 분석.
4. **버그/실수 패턴** — "모든 워크스페이스에서 내가 겪은 실수 패턴을 찾아줘."
5. **비용/모델 분석** — "워크스페이스별 토큰 사용량과 모델 분포를 정리해줘."
6. **6축 분석** — "최근 세션을 6축(DECOMP/VERIFY/ORCH/FAIL/CTX/META) 기준으로 분석해줘."

## Retrospective Frame

회고를 진행할 때 다음 프레임을 쓴다:
- 사용자가 무엇을 잘 요청했는가?
- 요청에 맥락이나 수용 기준(acceptance criteria)이 빠진 곳은 어디였는가?
- 에이전트는 불확실성에 어떻게 반응했는가?
- 테스트·인용·스크린샷·검증이 적절한 순간에 쓰였는가?
- 다음에 연습할 행동 하나는 무엇인가?

## Output

- 기본은 간결한 한국어.
- 사용자가 산출물을 원하면 `~/vibe-sunsang/exports/`에 저장한다.

## Guardrails

- 원본 JSONL 로그를 직접 수정하지 않는다 (읽기 전용).
- 변환된 로그에 보이지 않는 예시를 지어내지 않는다.
- Codex CLI에는 `AskUserQuestion` 카드 UI가 없다 → `shared/questioning-policy.md §A` 번호 블록을 쓴다.
