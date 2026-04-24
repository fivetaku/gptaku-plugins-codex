#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    out = []
    prev_dash = False
    for ch in lowered:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    return slug or "task"


def ensure(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a Codex-native pumasi workspace.")
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument("--task", required=True, help="Top-level task summary")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    pumasi = root / ".pumasi"
    tasks_dir = pumasi / "tasks"
    reports_dir = pumasi / "reports"

    ensure(tasks_dir)
    ensure(reports_dir)

    created_at = datetime.now(timezone.utc).isoformat()
    job = {
      "task": args.task,
      "created_at": created_at,
      "root": str(root),
      "status": "planning",
      "tasks": [],
      "rounds": [],
    }
    (pumasi / "job.json").write_text(json.dumps(job, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (pumasi / "plan.md").write_text(
        "# Pumasi Plan\n\n"
        f"- Task: {args.task}\n"
        f"- Created: {created_at}\n\n"
        "## Rounds\n\n"
        "## Tasks\n\n",
        encoding="utf-8",
    )
    (tasks_dir / f"{slugify(args.task)}.md").write_text(
        "# Seed Task\n\n"
        f"{args.task}\n",
        encoding="utf-8",
    )
    print(pumasi)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
