#!/usr/bin/env bash
# /pumasi:image — Codex /imagen 호출 래퍼
# Usage: image helper <prompt_file> <target_image_path>

set -euo pipefail

PROMPT_FILE="${1:-}"
TARGET_PATH="${2:-}"
EXPECTED_ASPECT="${3:-}"   # 선택: "16:9" 처럼 주면 실제 비율과 비교해 경고

if [[ -z "$PROMPT_FILE" || -z "$TARGET_PATH" ]]; then
  echo "Usage: $0 <prompt_file> <target_image_path> [expected_aspect e.g. 16:9]" >&2
  exit 2
fi

# 실제 픽셀 측정 + 요청 비율과 큰 괴리 시 경고 (gpt-image-2는 비율 미보장, 후처리 금지로 보정 불가)
measure_dims() { # echo "W H" (측정 실패 시 빈 출력)
  local f="$1" w="" h=""
  if command -v sips >/dev/null 2>&1; then
    w=$(sips -g pixelWidth  "$f" 2>/dev/null | awk '/pixelWidth/{print $2}')
    h=$(sips -g pixelHeight "$f" 2>/dev/null | awk '/pixelHeight/{print $2}')
  fi
  [[ -n "$w" && -n "$h" ]] && echo "$w $h"
  return 0   # set -e 가드: 측정 실패해도 비0 반환 금지 (DIMS=$(...) 중단 방지)
}
aspect_warn() { # args: W H "ew:eh"
  local w="$1" h="$2" exp="$3" ew eh got expr diff tol
  [[ -z "$exp" || -z "$w" || -z "$h" ]] && return 0
  ew="${exp%%:*}"; eh="${exp##*:}"
  [[ "$ew" =~ ^[0-9]+$ && "$eh" =~ ^[0-9]+$ && "$eh" -ne 0 && "$h" -ne 0 ]] || return 0
  got=$(( w * 1000 / h )); expr=$(( ew * 1000 / eh ))
  diff=$(( got > expr ? got - expr : expr - got )); tol=$(( expr * 15 / 100 ))
  if (( diff > tol )); then
    echo "WARN: aspect mismatch — 요청 ${exp}, 실제 ${w}x${h}. gpt-image-2는 비율을 보장하지 않음(후처리 금지로 보정 불가). 필요하면 비율 힌트를 강화해 재생성하세요." >&2
  fi
  return 0   # set -e 가드: 비율 일치(경고 없음) 시에도 0 반환
}

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "ERROR: prompt file not found: $PROMPT_FILE" >&2
  exit 2
fi

# codex 설치 확인
if ! command -v codex >/dev/null 2>&1; then
  echo "ERROR: codex CLI not found. Install: npm install -g @openai/codex" >&2
  exit 3
fi

# 1) feature flag 확인 + 자동 활성화
FLAG_STATE=$(codex features list 2>&1 | awk '/^image_generation/ {print $NF}' | head -n1)
if [[ "$FLAG_STATE" != "true" ]]; then
  echo "[image helper] enabling image_generation feature flag..."
  codex features enable image_generation >/dev/null 2>&1
fi

# 2) 저장 디렉토리 준비
TARGET_DIR=$(dirname "$TARGET_PATH")
mkdir -p "$TARGET_DIR"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXTRACT="${SCRIPT_DIR}/extract_image.py"

# 3) 프롬프트 본문 + image 도구 즉시 호출 지시
#    핵심: Codex non-interactive run(headless)는 image_generation 도구로 이미지를 생성해서
#    base64(result)로 돌려주지만, TUI와 달리 generated_images/에 파일로 저장하지 않는다.
#    그래서 --json 으로 받아 base64를 우리가 직접 디코딩해 저장한다.
#    "/imagen" 슬래시는 exec에서 inert 텍스트이고, 설치된 codex 스킬을 읽다 도구 호출을
#    놓칠 수 있으므로, 파일/스킬 읽지 말고 도구를 즉시 부르라고 명시한다.
PROMPT_BODY=$(cat "$PROMPT_FILE")

CODEX_PROMPT="Use your image generation tool to generate EXACTLY ONE image now. Call the tool immediately on this turn. Do NOT read any files, skills, references, or AGENTS.md. Do NOT run shell commands. Do NOT copy or save files yourself — just call the image generation tool. Generate the image from this prompt, verbatim:

${PROMPT_BODY}"

# 4) Codex non-interactive run --json 호출 — 이벤트(JSONL)를 stdout으로 받는다.
JSON_OUT=$(mktemp -t imagen-json.XXXXXX)
LOG_FILE=$(mktemp -t imagen-log.XXXXXX)
echo "[image helper] calling Codex non-interactive run --json — target: $TARGET_PATH"
echo "[image helper] json: $JSON_OUT  log: $LOG_FILE"

if ! Codex non-interactive run --json \
    --skip-git-repo-check \
    --dangerously-bypass-approvals-and-sandbox \
    "$CODEX_PROMPT" < /dev/null > "$JSON_OUT" 2> "$LOG_FILE"; then
  echo "ERROR: Codex non-interactive run failed. See log: $LOG_FILE" >&2
  tail -50 "$LOG_FILE" >&2
  exit 4
fi

# 5) 생성 이미지(base64) 추출 → TARGET 저장.
#    1차: stdout(JSONL)에서 image_generation_call.result 디코딩.
#    2차(폴백): 세션 rollout 파일에서 추출(stdout이 result를 안 실어줄 경우).
if python3 "$EXTRACT" "$JSON_OUT" "$TARGET_PATH" >/dev/null 2>&1; then
  SOURCE_DESC="Codex non-interactive run --json (stdout)"
else
  SID=$(grep -hoE '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}' "$LOG_FILE" "$JSON_OUT" 2>/dev/null | head -n1 || true)
  ROLL=""
  [[ -n "$SID" ]] && ROLL=$(find "$HOME/.codex/sessions" -name "rollout-*${SID}.jsonl" 2>/dev/null | head -n1)
  if [[ -n "$ROLL" ]] && python3 "$EXTRACT" "$ROLL" "$TARGET_PATH" >/dev/null 2>&1; then
    SOURCE_DESC="session rollout ($ROLL)"
  else
    echo "ERROR: Codex non-interactive run produced NO image (stdout/rollout에서 base64 이미지 못 찾음)" >&2
    echo "       (생성 실패를 성공으로 보고하지 않기 위해 중단)" >&2
    echo "--- codex log tail ---" >&2
    tail -50 "$LOG_FILE" >&2
    exit 5
  fi
fi

if [[ ! -s "$TARGET_PATH" ]]; then
  echo "ERROR: target file not created or empty: $TARGET_PATH" >&2
  exit 5
fi

# 6) 파일 정보 출력 (실측 해상도 포함 — 감사 가능)
SIZE=$(wc -c < "$TARGET_PATH" | tr -d ' ')
FILE_INFO=$(file "$TARGET_PATH")
SHA1=$(shasum "$TARGET_PATH" | awk '{print $1}')
DIMS=$(measure_dims "$TARGET_PATH")
DIM_STR="${DIMS// /x}"; [[ -z "$DIM_STR" ]] && DIM_STR="(unmeasured)"
if [[ -n "$DIMS" ]]; then
  aspect_warn ${DIMS} "$EXPECTED_ASPECT"
fi

cat <<EOF
[image helper] SUCCESS
  path:    $TARGET_PATH
  source:  $SOURCE_DESC
  size:    $SIZE bytes
  dims:    $DIM_STR
  info:    $FILE_INFO
  sha1:    $SHA1
  log:     $LOG_FILE
EOF
