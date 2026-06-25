#!/usr/bin/env bash
# /pumasi:image — generated_images 누적 정리 (선택적, 안전 우선)
#
# Codex /imagen 은 호출마다 ~/.codex/generated_images/ 아래 새 폴더를 쌓는다.
# 정확성은 image helper 의 base64 직접 추출이 보장하므로(스테일 오집음 차단),
# 이 스크립트는 순수 디스크 위생용이다.
#
# 기본은 DRY-RUN — 무엇이 지워질지 보여주기만 한다. 실제 삭제는 --apply 필요.
# 삭제는 가능하면 `trash`(복구 가능)로, 없으면 rm -rf 로 수행한다.
#
# Usage:
#   imagen-cleanup.sh                       # dry-run, 최신 50개 보존
#   imagen-cleanup.sh --keep 30             # 최신 30개만 보존(나머지 후보)
#   imagen-cleanup.sh --older-than-days 14  # 14일 넘은 것만 후보
#   imagen-cleanup.sh --apply               # 실제 삭제 (trash 우선)
set -euo pipefail

KEEP=50
OLDER_DAYS=0
APPLY=0
GEN_DIR="${IMAGEN_GEN_DIR:-$HOME/.codex/generated_images}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --apply) APPLY=1; shift ;;
    --keep) KEEP="${2:-50}"; shift 2 ;;
    --older-than-days) OLDER_DAYS="${2:-0}"; shift 2 ;;
    --gen-dir) GEN_DIR="${2:?}"; shift 2 ;;
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

[[ -d "$GEN_DIR" ]] || { echo "gen dir not found: $GEN_DIR (nothing to do)"; exit 0; }

# mtime 내림차순으로 1-depth 항목(폴더/파일) 나열 (bash 3.2 호환 — mapfile 미사용)
ALL=()
while IFS= read -r line; do
  [[ -n "$line" ]] && ALL+=("$line")
done < <(find "$GEN_DIR" -mindepth 1 -maxdepth 1 ! -name '.DS_Store' -print0 2>/dev/null \
  | xargs -0 stat -f '%m %N' 2>/dev/null | sort -rn | cut -d' ' -f2-)

TOTAL=${#ALL[@]}
echo "gen dir: $GEN_DIR"
echo "total entries: $TOTAL | keep newest: $KEEP | older-than-days: $OLDER_DAYS | mode: $([[ $APPLY -eq 1 ]] && echo APPLY || echo DRY-RUN)"

if (( TOTAL <= KEEP )); then
  echo "nothing to prune (total ${TOTAL} <= keep ${KEEP})"
  exit 0
fi

NOW=$(date +%s)
CANDIDATES=()
for ((i=KEEP; i<TOTAL; i++)); do
  e="${ALL[$i]}"
  if (( OLDER_DAYS > 0 )); then
    mt=$(stat -f '%m' "$e" 2>/dev/null || echo "$NOW")
    age_days=$(( (NOW - mt) / 86400 ))
    (( age_days >= OLDER_DAYS )) || continue
  fi
  CANDIDATES+=("$e")
done

if (( ${#CANDIDATES[@]} == 0 )); then
  echo "no candidates after filters"
  exit 0
fi

echo "candidates (${#CANDIDATES[@]}):"
printf '  %s\n' "${CANDIDATES[@]}"

if (( APPLY == 0 )); then
  echo ""
  echo "DRY-RUN — 삭제하지 않음. 실제로 지우려면 --apply 를 붙이세요."
  exit 0
fi

if command -v trash >/dev/null 2>&1; then
  trash "${CANDIDATES[@]}" && echo "trashed ${#CANDIDATES[@]} entries (복구 가능)"
else
  echo "WARN: 'trash' 미설치 — rm -rf 로 영구 삭제합니다."
  rm -rf "${CANDIDATES[@]}" && echo "removed ${#CANDIDATES[@]} entries"
fi
