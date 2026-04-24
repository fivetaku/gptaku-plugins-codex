#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def parse_all_custom_properties(css: str) -> dict[str, str]:
    """Return every custom property declaration as {--name: raw_value}."""
    props: dict[str, str] = {}
    cleaned = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    for match in re.finditer(r"--([\w-]+)\s*:\s*([^;}]+)", cleaned, flags=re.S):
        props[f"--{match.group(1)}"] = match.group(2).strip()
    return props


def detect_alias_tier(props: dict[str, str]) -> dict[str, list[dict]]:
    """Group aliases into the configured tier buckets."""
    tiers: dict[str, list[dict]] = {
        "util": [],
        "semantic": [],
        "action": [],
        "component": [],
        "core": [],
    }

    for alias in sorted(props):
        value = props[alias].strip()
        references: list[str] = []
        for reference in re.findall(r"var\(\s*(--[\w-]+)", value):
            if reference not in references:
                references.append(reference)

        terminal_hint = None
        if re.fullmatch(r"#[0-9a-fA-F]{3,8}", value) or re.fullmatch(
            r"(?:rgba?|hsla?)\(\s*[^()]+\s*\)", value
        ):
            terminal_hint = value
        elif references:
            terminal_hint = references[0]

        entry = {
            "alias": alias,
            "references": references,
            "terminal_hint": terminal_hint,
        }

        if "-util-" in alias:
            tiers["util"].append(entry)
        if "-semantic-" in alias:
            tiers["semantic"].append(entry)
        if any(token in alias for token in ("-action-", "-btn-", "-button-")):
            tiers["action"].append(entry)
        if any(
            token in alias
            for token in ("-input-", "-card-", "-nav-", "-dialog-", "-popover-")
        ):
            tiers["component"].append(entry)
        if "-core-" in alias or re.fullmatch(
            r"#[0-9a-fA-F]{3,8}", value
        ) or re.fullmatch(r"(?:rgba?|hsla?)\(\s*[^()]+\s*\)", value):
            tiers["core"].append(entry)

    return tiers


def extract_slug(slug: str) -> dict:
    """Read CSS for a slug, classify aliases, and write the JSON report."""
    css_dir = Path.cwd() / "insane-design" / slug / "css"
    css = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(css_dir.glob("*.css"))
    )
    props = parse_all_custom_properties(css)
    tiers = detect_alias_tier(props)
    result = {
        "slug": slug,
        "tiers": tiers,
        "stats": {
            "tier_counts": {tier_name: len(entries) for tier_name, entries in tiers.items()}
        },
    }

    output_path = Path.cwd() / "insane-design" / slug / "phase1" / "alias_layer.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    slug = sys.argv[1] if len(sys.argv) > 1 else "stripe"
    sys.stdout.write(json.dumps(extract_slug(slug), indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
