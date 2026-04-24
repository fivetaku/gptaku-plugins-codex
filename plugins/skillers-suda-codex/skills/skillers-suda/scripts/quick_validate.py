#!/usr/bin/env python3
"""Lightweight Codex skill validator."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML-style frontmatter")

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md not found"]

    text = skill_md.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not name:
        errors.append("missing frontmatter field: name")
    elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("name must be lowercase kebab-case")

    if not description:
        errors.append("missing frontmatter field: description")
    elif len(description) > 1024:
        errors.append("description must be 1024 characters or fewer")

    for ref in re.findall(r"`((?:references|scripts|assets)/[^`]+)`", text):
        if "{" in ref or "*" in ref:
            continue
        if not (skill_dir / ref).exists():
            errors.append(f"referenced path does not exist: {ref}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: quick_validate.py <skill-dir>", file=sys.stderr)
        return 2

    errors = validate(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: skill is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
