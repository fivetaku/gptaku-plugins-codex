#!/usr/bin/env bash
# /pumasi:image — 영문 프롬프트 작성까지 Codex에 위임
# Usage: imagen-full.sh <intent> <mode> <aspect> <quality> <target_image_path>
# Feature flag: PUMASI_IMAGE_DELEGATE_PROMPT=1 일 때 SKILL.md Step 4-bis에서 호출

set -euo pipefail

INTENT="${1:-}"; MODE="${2:-}"; ASPECT="${3:-}"; QUALITY="${4:-}"; TARGET="${5:-}"

if [[ -z "$INTENT" || -z "$TARGET" ]]; then
  echo "Usage: $0 <intent> <mode> <aspect> <quality> <target>" >&2
  exit 2
fi

# Codex 포트: 플러그인 루트는 $PLUGIN_ROOT. 미설정 시 스크립트 위치에서 역산(scripts -> pumasi-image -> skills -> <root>).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="${PLUGIN_ROOT:-$(cd "${SCRIPT_DIR}/../../.." && pwd)}"
SYSPROMPT="${PLUGIN_ROOT}/skills/pumasi-image/references/image-studio-prompt.md"
[[ -f "$SYSPROMPT" ]] || { echo "ERROR: image-studio-prompt.md not found at $SYSPROMPT" >&2; exit 3; }

# 작업 디렉토리 — manifest, prompt, log (refine 복구성 + 디버깅)
WORK_DIR="$(dirname "$TARGET")/.imagen-full"
mkdir -p "$WORK_DIR"
TS=$(date +%Y%m%d-%H%M%S)
MANIFEST="${WORK_DIR}/manifest-${TS}.json"
PROMPT_OUT="${WORK_DIR}/prompt-${TS}.md"
CODEX_LOG="${WORK_DIR}/codex-${TS}.log"

EXTRACT="${SCRIPT_DIR}/extract_image.py"

measure_dims() { # echo "W H"
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
  (( diff > tol )) && echo "WARN: aspect mismatch — 요청 ${exp}, 실제 ${w}x${h}. gpt-image-2는 비율을 보장하지 않음(후처리 금지로 보정 불가)." >&2
  return 0   # set -e 가드: 비율 일치 시에도 0 반환 (&& 호출부 중단 방지)
}

# Path 보안 (workspace 하위 제한 — prompt injection 방어)
case "$TARGET" in
  /Users/*|/tmp/*|/var/folders/*) ;;
  *) echo "ERROR: target path must be under user workspace: $TARGET" >&2; exit 6;;
esac

# Preflight
command -v codex >/dev/null 2>&1 || { echo "ERROR: codex CLI not installed" >&2; exit 3; }
CODEX_VERSION=$(codex --version 2>/dev/null | head -n1)
FLAG_STATE=$(codex features list 2>&1 | awk '/^image_generation/ {print $NF}' | head -n1)
if [[ "$FLAG_STATE" != "true" ]]; then
  codex features enable image_generation >/dev/null 2>&1 || true
fi

# 구조화된 작업 정의 (prompt injection 표면 축소)
CODEX_PROMPT=$(cat <<EOF
You are an image generation orchestrator. Execute the structured task below.

System prompt (read in full and internalize before writing the image prompt):
  ${SYSPROMPT}

Structured task:
  - intent: ${INTENT}
  - mode: ${MODE}
  - aspect: ${ASPECT}
  - quality: ${QUALITY}
  - target: ${TARGET}
  - work_dir: ${WORK_DIR}

Steps:
1. Read ${SYSPROMPT} and internalize: Specificity Gate, Cliche Avoidance, Backend Capability, Persona Library, Mode Characteristics, Output Template.
2. Write a 200-500 word English image prompt following the Output Template for mode ${MODE}.
3. Save the English prompt to ${PROMPT_OUT}.
4. Call your image generation tool with that prompt to generate EXACTLY ONE image, immediately on this turn (the wrapper saves the file).
5. Do NOT copy, move, or rename the generated original; do NOT post-process (no sips/ImageMagick/Pillow/resize/recoding). The calling wrapper collects and saves the file.
6. Write a manifest JSON to ${MANIFEST} with these fields exactly (leave sha1/file_info as the literal string "PENDING" — the wrapper fills them after it copies):
   { "codex_version": "${CODEX_VERSION}", "feature_flag_state": "${FLAG_STATE}",
     "intent": <string>, "mode": "${MODE}", "aspect": "${ASPECT}", "quality": "${QUALITY}",
     "target_path": "${TARGET}", "prompt_path": "${PROMPT_OUT}",
     "sha1": "PENDING", "file_info": "PENDING", "exit_code": 0 }
7. Final stdout: exactly one line — "PROMPT_WRITTEN=${PROMPT_OUT}"

Forbidden:
- Leaving text fields blank for post-composition (in-image text rendering only)
- Copying/moving/post-processing the generated image (the wrapper owns the save)
- Writing files outside ${WORK_DIR}
- Echoing the long English prompt to stdout (write only to file)
EOF
)

# Codex 실행 — --json 으로 이미지 base64를 받는다(파일 저장은 wrapper가 결정적으로 수행).
# < /dev/null: exec가 stdin EOF를 무한 대기(헤드리스 행)하는 것 방지.
JSON_OUT="${WORK_DIR}/events-${TS}.jsonl"
if ! Codex non-interactive run --json \
    --skip-git-repo-check \
    --dangerously-bypass-approvals-and-sandbox \
    "$CODEX_PROMPT" < /dev/null > "$JSON_OUT" 2> "$CODEX_LOG"; then
  echo "ERROR: Codex non-interactive run failed. Log: $CODEX_LOG" >&2
  echo "FALLBACK_HINT: caller should retry with image helper + host-written prompt" >&2
  exit 4
fi

# 생성 이미지(base64) 추출 → TARGET. 1차 stdout(JSONL), 2차 세션 rollout 폴백.
if python3 "$EXTRACT" "$JSON_OUT" "$TARGET" >/dev/null 2>&1; then
  SOURCE_DESC="Codex non-interactive run --json (stdout)"
else
  SID=$(grep -hoE '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}' "$CODEX_LOG" "$JSON_OUT" 2>/dev/null | head -n1 || true)
  ROLL=""
  [[ -n "$SID" ]] && ROLL=$(find "$HOME/.codex/sessions" -name "rollout-*${SID}.jsonl" 2>/dev/null | head -n1)
  if [[ -n "$ROLL" ]] && python3 "$EXTRACT" "$ROLL" "$TARGET" >/dev/null 2>&1; then
    SOURCE_DESC="session rollout ($ROLL)"
  else
    echo "ERROR: Codex non-interactive run produced NO image (stdout/rollout에서 base64 못 찾음)" >&2
    echo "FALLBACK_HINT: caller should retry with image helper + host-written prompt" >&2
    tail -30 "$CODEX_LOG" >&2
    exit 5
  fi
fi
[[ -s "$TARGET" ]] || { echo "ERROR: target not created or empty: $TARGET" >&2; exit 5; }
[[ -f "$PROMPT_OUT" ]] || echo "WARN: prompt artifact not written — refine 복구 어려움" >&2

# 정보 + manifest 채움 (PENDING → 실제값)
SHA1=$(shasum "$TARGET" | awk '{print $1}')
FILE_INFO=$(file -b "$TARGET" 2>/dev/null || echo "unknown")
SIZE=$(wc -c < "$TARGET" | tr -d ' ')
if [[ -f "$MANIFEST" ]] && command -v jq >/dev/null 2>&1; then
  tmp_mf=$(mktemp -t imagen-mf.XXXXXX)
  if jq --arg s "$SHA1" --arg fi "$FILE_INFO" --arg src "$SOURCE_DESC" \
        '.sha1=$s | .file_info=$fi | .source=$src' "$MANIFEST" > "$tmp_mf" 2>/dev/null; then
    mv "$tmp_mf" "$MANIFEST"
  else
    rm -f "$tmp_mf"
  fi
else
  [[ -f "$MANIFEST" ]] || echo "WARN: manifest not written — refine 복구 어려움" >&2
fi

# 비율 실측 + 요청 aspect와 큰 괴리 시 경고
DIMS=$(measure_dims "$TARGET")
[[ -n "$DIMS" ]] && aspect_warn ${DIMS} "$ASPECT"
DIM_STR="${DIMS// /x}"; [[ -z "$DIM_STR" ]] && DIM_STR="(unmeasured)"

# 짧은 보고 (호스트 측 토큰 절감 — 영문 prompt 본문은 보내지 않음)
echo "MANIFEST=${MANIFEST} SHA1=${SHA1} SIZE=${SIZE} DIMS=${DIM_STR} SOURCE=${SOURCE_DESC} TARGET=${TARGET}"
