---
name: vibe-sunsang-retro
description: 'Conversation-log converter — transforms Codex session JSONL logs into Markdown (with per-session metrics and an activity-sorted index) and provides an analysis guide. Korean triggers: "변환", "대화 변환", "로그 변환", "회고", "이번 주 대화". English triggers: "retro", "convert conversations", "log conversion".'
---

# vibe-sunsang-retro (Codex)

> Codex 세션 로그를 읽기 좋은 Markdown으로 변환하고 분석 가이드를 제공한다.

Codex는 skill-first다 (별도 커맨드 파일 없음). 객관식은 `$PLUGIN_ROOT/shared/questioning-policy.md §A`의 질문 도구(`request_user_input_async`, Plan 모드는 `request_user_input`)로 묻고, 두 도구가 모두 없을 때만 번호 블록으로 채팅에서 묻는다. async 도구는 부른 뒤 한 줄 안내만 쓰고 턴을 끝낸다(답은 다음 메시지로 온다). 아래 번호 블록 예시는 폴백일 때의 모양이다. 열린 코칭 질문은 도구 없이 평범한 채팅으로 묻는다.

## 데이터 경로

- **원본**: `~/.codex/sessions/**/*.jsonl` (`$CODEX_HOME/sessions`가 있으면 그쪽. 다른 위치는 `--sessions-dir`)
- **변환 결과**: `~/vibe-sunsang/conversations/{프로젝트명}/`
- **인덱스**: `~/vibe-sunsang/conversations/INDEX.md`
- **설정**: `~/vibe-sunsang/config/`
- **리포트 저장**: `~/vibe-sunsang/exports/`
- **변환 스크립트**: `$PLUGIN_ROOT/scripts/convert_sessions.py`

프로젝트 = 세션의 작업 디렉토리(`cwd`). 표시 이름은 폴더명에서 자동 생성되고 `config/project_names.json`(cwd → 이름)으로 바꿀 수 있다. 같은 폴더명이 다른 경로에 있으면 부모 폴더명이 접두로 붙는다.

## 실행: 대화 로그 변환

인자: $ARGUMENTS

### Step 0: 워크스페이스 자동 치유 (dead-end 방지)

파일 존재만 확인하고 튕기지 않는다. 다음을 실행해 워크스페이스를 스스로 준비한다:

```bash
python3 "$PLUGIN_ROOT/scripts/ensure_workspace.py" 2>/dev/null || python "$PLUGIN_ROOT/scripts/ensure_workspace.py"
```

출력 마지막 줄 `STATUS <fresh|v2|v1_migrated>  CONFIG <present|absent>`로 분기한다:

- `v1_migrated` → "이전 버전 데이터를 새 구조로 옮겼어요." 한 줄만 안내하고 계속 진행한다.
- `CONFIG absent` (fresh) → 아직 초기 설정 전이다. "처음이시네요 — 바로 준비할게요!" 안내 후 **vibe-sunsang-onboard로 넘긴다** (자동 이름/기본 유형 lazy 온보딩 가능). 여기서 종료하지 말 것.
- 그 외(`v2`, `CONFIG present`) → 그대로 다음 단계.

### Step 1: 변환 스크립트 실행

인자를 분석하여 적절한 옵션으로 실행합니다:

| 인자 | 동작 |
|------|------|
| (없음) | 증분 변환 (새 세션·이어진 세션만) |
| "전체", "force", "다시" | `--force` 전체 재변환 |
| "상세", "verbose" | `--verbose` 도구 결과 전문 포함 |
| 프로젝트명 | `--project <이름>` 해당 프로젝트만 (INDEX.md 표시 이름 또는 cwd 경로) |

**프로젝트명이 지정된 경우:** `~/vibe-sunsang/conversations/INDEX.md`에서 프로젝트 목록을 읽어 일치하는 프로젝트를 찾습니다. 정확히 일치하는 프로젝트가 없으면 `shared/questioning-policy.md §A` 질문 도구 1콜(`request_user_input_async`, Plan 모드는 `request_user_input`; 둘 다 없으면 번호 블록 폴백)으로 묻는다. 번호 블록 폴백일 때의 모양:

```text
질문: 어떤 프로젝트의 대화를 변환할까요?
1. {프로젝트명1} — {세션 수}개 세션 (가장 활발, 추천)
2. {프로젝트명2} — {세션 수}개 세션
3. 문장으로 직접 알려주세요
(모르면 1번으로 진행하겠습니다)
```

> 선택지는 INDEX.md에서 읽은 프로젝트 목록으로 동적 생성한다. 세션 수가 많은 순으로 정렬한다.

```bash
# 기본: 증분 변환
python3 "$PLUGIN_ROOT/scripts/convert_sessions.py" --names-file "$HOME/vibe-sunsang/config/project_names.json" --output-dir "$HOME/vibe-sunsang/conversations" 2>/dev/null || python "$PLUGIN_ROOT/scripts/convert_sessions.py" --names-file "$HOME/vibe-sunsang/config/project_names.json" --output-dir "$HOME/vibe-sunsang/conversations"

# --force: 인자에 "전체", "force", "다시" 포함 시 위 명령에 --force 추가
# --verbose: 인자에 "상세", "verbose" 포함 시 추가
# --project <이름>: 인자에 프로젝트명 포함 시 추가
```

### 에러 처리

변환 스크립트 실행 중 문제가 발생하면 비개발자가 이해할 수 있게 안내합니다:

| 상황 | 사용자에게 보여줄 메시지 |
|------|------------------------|
| Python 없음 | "Python이 설치되어 있지 않아요. 터미널에서 `python3 --version`을 실행해서 확인해주세요." |
| 세션 폴더 없음 | "Codex 대화 기록을 찾을 수 없어요. Codex로 작업한 적이 있는지, `~/.codex/sessions/`가 있는지 확인해주세요. 다른 위치면 `--sessions-dir <경로>`로 지정할 수 있어요." |
| 권한 오류 | "파일에 접근할 수 없어요. `~/.codex/sessions/` 폴더의 권한을 확인해주세요." |
| 변환 0건 | "새로 변환할 대화가 없어요. 이미 최신 상태입니다!" |

### Step 2: 인덱스 확인

변환 완료 후 인덱스를 읽어 현황을 보여줍니다:

`~/vibe-sunsang/conversations/INDEX.md`를 읽습니다 (프로젝트별 세션 수·기간·**최근 활동** 컬럼, 최근 활동 순 정렬).

변환 결과를 요약합니다:
- 총 프로젝트 수
- 총 세션 수
- 최근 변환된 세션

### Step 3: 분석 템플릿 제안

변환이 완료되면 다음 분석 옵션을 제안합니다:

**사용 가능한 분석:**

1. **프로젝트 패턴 분석**
   > "[프로젝트명] 세션들을 분석해줘. 주요 작업 유형, 반복 에러, 도구 활용 패턴을 정리해줘."

2. **성장 트래커** → "성장 리포트 만들어줘" (vibe-sunsang-growth)
   > 성장 리포트를 생성합니다. (v2: 6축 기술 차원 분석 + 레이더 차트 포함)

3. **멘토링 세션** → "멘토링해줘" (vibe-sunsang-mentor)
   > AI 활용 능력을 코칭 받습니다. (v2: 6축 중심 맞춤 분석)

4. **버그/실수 패턴**
   > "모든 프로젝트에서 내가 겪은 실수 패턴을 찾아줘."

5. **멀티에이전트 리뷰**
   > "서브에이전트를 spawn한 세션을 분석해서 코디네이션 효율을 평가해줘." (frontmatter `has_orchestration: true`)

6. **비용 분석**
   > "프로젝트별 토큰 사용량과 모델 분포를 정리해줘."

7. **6축 분석**
   > "최근 세션을 6축(DECOMP/VERIFY/ORCH/FAIL/CTX/META) 기준으로 분석해줘."

## 회고 프레임

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
- 변환 중 분석이 완료됐다고 말하지 않는다. 변환은 데이터 준비일 뿐이다.
- 선택지 질문은 `shared/questioning-policy.md §A` 질문 도구로 묻고, 도구가 없을 때만 번호 블록을 쓴다.
