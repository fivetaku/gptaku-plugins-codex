#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path


def version_of(cmd: str, args: list[str]) -> str | None:
    if shutil.which(cmd) is None:
        return None
    try:
        out = subprocess.check_output([cmd, *args], stderr=subprocess.STDOUT, text=True, timeout=5)
    except Exception:
        return "unknown"
    return out.strip().splitlines()[0] if out.strip() else "unknown"


def list_skill_dirs() -> list[str]:
    base = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
    if not base.exists():
        return []
    return sorted(p.name for p in base.iterdir() if p.is_dir() and (p / "SKILL.md").exists())


def git_status(root: Path) -> dict[str, str | bool | None]:
    if not (root / ".git").exists():
        return {"is_git_repo": False, "branch": None}
    try:
        branch = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.STDOUT,
            text=True,
            timeout=5,
        ).strip()
    except Exception:
        branch = None
    return {"is_git_repo": True, "branch": branch}


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan the local Codex environment for kkirikkiri.")
    parser.add_argument("--root", default=os.getcwd(), help="Project root to inspect")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    payload = {
        "root": str(root),
        "commands": {
            "codex": version_of("codex", ["--version"]),
            "python3": version_of("python3", ["--version"]),
            "node": version_of("node", ["--version"]),
            "git": version_of("git", ["--version"]),
            "tmux": version_of("tmux", ["-V"]),
            "gh": version_of("gh", ["--version"]),
            "gemini": version_of("gemini", ["--version"]),
        },
        "installed_skills": list_skill_dirs(),
        "git": git_status(root),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
