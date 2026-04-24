#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_ROOT="${TMPDIR:-/tmp}/gptaku-codex-smoke-$$"

mkdir -p "$TMP_ROOT"
trap 'rm -rf "$TMP_ROOT"' EXIT

cd "$ROOT"

section() {
  printf '\n== %s ==\n' "$1"
}

section "package audit"
python3 scripts/validate_packages.py

section "json manifests"
python3 - <<'PY'
from __future__ import annotations

import json
from pathlib import Path

root = Path(".")
files = [root / ".agents" / "plugins" / "marketplace.json"]
files.extend(sorted((root / "plugins").glob("*/.codex-plugin/plugin.json")))

for path in files:
    with path.open(encoding="utf-8") as f:
        json.load(f)
    print(f"ok {path}")
PY

section "insane-search smoke"
python3 -m pytest plugins/insane-search-codex/skills/insane-search/engine/tests/test_smoke.py -q

section "skillers-suda quick validate"
python3 plugins/skillers-suda-codex/skills/skillers-suda/scripts/quick_validate.py \
  plugins/skillers-suda-codex/skills/skillers-suda

section "vibe-sunsang converter"
python3 plugins/vibe-sunsang-codex/skills/vibe-sunsang-retro/scripts/convert_sessions.py \
  --limit 1 \
  --output-dir "$TMP_ROOT/vibe-sunsang" \
  --force

section "pumasi workspace init"
python3 plugins/pumasi-codex/skills/pumasi/scripts/init_workspace.py \
  --root "$TMP_ROOT/pumasi" \
  --task "codex marketplace smoke"

section "kkirikkiri shared memory init"
python3 plugins/kkirikkiri-codex/skills/kkirikkiri/scripts/init_shared_memory.py \
  --root "$TMP_ROOT/kkirikkiri" \
  --task "codex marketplace smoke" \
  --preset analysis

section "kkirikkiri environment scan"
python3 plugins/kkirikkiri-codex/skills/kkirikkiri/scripts/scan_environment.py \
  --root "$ROOT"

section "legacy residue scan"
if rg --pcre2 -n "AskUserQuestion|CLAUDE_PLUGIN_ROOT|\\.claude|Claude Code|\\bClaude\\b|(?<![A-Za-z0-9_])Task\\s*\\(|run_in_background|\\.claude-plugin|commands/|(?:references|scripts)/legacy/|pumasi\\.sh|pumasi\\.cmd|pumasi-job|pumasi\\.config\\.yaml|codex /imagen|codex exec|imagen\\.sh|codex-port|-[Cc]odex\\.md|README-codex|workflow-codex|template-codex" \
  plugins .agents; then
  echo "legacy residue found" >&2
  exit 1
fi
echo "clean"

section "done"
echo "package smoke tests passed"
