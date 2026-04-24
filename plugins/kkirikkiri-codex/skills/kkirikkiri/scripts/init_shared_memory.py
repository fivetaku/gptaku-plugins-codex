#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "TEAM_PLAN.md": "# Team Plan\n\n",
    "TEAM_PROGRESS.md": "# Team Progress\n\n",
    "TEAM_FINDINGS.md": "# Team Findings\n\n",
    "TEAM_REPORT.md": "# Team Report\n\n",
}


def ensure_file(path: Path, initial: str) -> None:
    if not path.exists():
        path.write_text(initial, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize .kkirikkiri shared memory files.")
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument("--task", required=True, help="High-level task description")
    parser.add_argument("--preset", required=True, help="Preset name")
    parser.add_argument("--leader", default="codex-lead", help="Lead identifier")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    shared = root / ".kkirikkiri"
    shared.mkdir(parents=True, exist_ok=True)

    for name, initial in FILES.items():
        ensure_file(shared / name, initial)

    plan = shared / "TEAM_PLAN.md"
    header = (
        f"# Team Plan\n\n"
        f"- Task: {args.task}\n"
        f"- Preset: {args.preset}\n"
        f"- Lead: {args.leader}\n\n"
        f"## Roles\n\n"
        f"## Acceptance Criteria\n\n"
    )
    plan.write_text(header, encoding="utf-8")

    print(shared)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
