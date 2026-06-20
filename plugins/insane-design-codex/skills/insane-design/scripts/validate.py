#!/usr/bin/env python3
"""
v3.2 design.md validator (validator-spec p1.5 — 8 checks).

Usage:
    python3 validate.py <path/to/design.md>           # single file
    python3 validate.py <directory>                    # all design.md under dir
    python3 validate.py --json <directory>             # JSON output

Exit codes:
    0 = all PASS
    1 = at least one FAIL
    2 = usage error
"""

import re
import sys
import json
import argparse
from pathlib import Path


CHECKS = [
    "schema_version",
    "frontmatter_required",
    "mandatory_sections",
    "craft_floor",
    "negative_space_floor",
    "known_gaps_floor",
    "file_size",
    "direction_summary_format",
]

MANDATORY_SECTIONS = [
    r"^##\s+0?0\.\s",   # Visual Theme & Atmosphere
    r"^##\s+0?1\.\s",   # Quick Start
    r"^##\s+0?2\.\s",   # Provenance
    r"^##\s+0?3\.\s",   # Tech Stack
    r"^##\s+0?4\.\s",   # Font Stack
    r"^##\s+0?5\.\s",   # Typography Scale
    r"^##\s+0?6\.\s",   # Colors
    r"^##\s+0?7\.\s",   # Spacing
    r"^##\s+0?8\.\s",   # Radius
    r"^##\s+11\.\s",    # Layout Patterns
    r"^##\s+13\.\s",    # Components
    r"^##\s+15\.\s",    # Drop-in CSS
    r"^##\s+17\.\s",    # Agent Prompt Guide
    r"^##\s+18\.\s",    # DO / DON'T
    r"^##\s+19\.\s",    # Known Gaps
]

REQUIRED_FRONTMATTER = ["slug", "service_name", "site_url", "archetype",
                       "design_system_level"]

DIRECTION_SUMMARY_KEYS = ["BOLD Direction", "Aesthetic Category",
                         "Signature Element", "Code Complexity"]


def validate(path: Path) -> dict:
    text = path.read_text()
    result = {"path": str(path), "checks": {}, "pass": True}

    # 1. schema_version
    m = re.search(r"^schema_version:\s*([\d.]+)", text, re.M)
    schema_ok = bool(m and m.group(1) == "3.2")
    result["checks"]["schema_version"] = {
        "pass": schema_ok,
        "detail": f"got {m.group(1) if m else 'none'}, expected 3.2"
    }

    # 2. frontmatter required fields
    fm_match = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = fm_match.group(1) if fm_match else ""
    missing = [k for k in REQUIRED_FRONTMATTER if not re.search(rf"^{k}:", fm, re.M)]
    result["checks"]["frontmatter_required"] = {
        "pass": not missing,
        "detail": f"missing: {missing}" if missing else "all present"
    }

    # 3. mandatory sections (15)
    found = sum(1 for pat in MANDATORY_SECTIONS if re.search(pat, text, re.M))
    sections_ok = found == len(MANDATORY_SECTIONS)
    result["checks"]["mandatory_sections"] = {
        "pass": sections_ok,
        "detail": f"{found}/{len(MANDATORY_SECTIONS)} sections found"
    }

    # 4. §13-3 craft >= 5 (yaml block top-level keys)
    m = re.search(
        r"###\s*(?:13-3\.?\s*)?Signature Micro.*?(?=^###\s+1[3-9]-|\n##\s+\d+\.)",
        text, re.M | re.S
    )
    if not m:
        m = re.search(
            r"###\s*13-3\..*?(?=^###\s+1[3-9]-|\n##\s+\d+\.)",
            text, re.M | re.S
        )
    crafts = re.findall(r"^([a-z][a-z0-9_-]+):\s*$", m.group(0), re.M) if m else []
    craft_ok = len(crafts) >= 5
    result["checks"]["craft_floor"] = {
        "pass": craft_ok,
        "detail": f"craft count {len(crafts)}, floor 5"
    }

    # 5. §18 Negative-Space — count "What This Site Doesn't Use" or "absent" items >=5
    s18_match = re.search(
        r"^##\s+18\..*?(?=^##\s+\d+\.|\Z)",
        text, re.M | re.S
    )
    s18 = s18_match.group(0) if s18_match else ""
    # Match either "What This Site Doesn't Use" or "Negative-Space Identity" subsection
    neg_block_match = re.search(
        r"###\s*(?:🚫\s*)?(?:What This Site Doesn'?t Use|Negative-Space Identity).*?(?=^###\s|\Z)",
        s18, re.M | re.S
    )
    if neg_block_match:
        neg_block = neg_block_match.group(0)
    else:
        # Fallback: count all bullet items in §18 (DON'T list often serves as negative-space)
        neg_block = s18
    neg_items = re.findall(r"^[-*]\s+", neg_block, re.M)
    neg_ok = len(neg_items) >= 5
    result["checks"]["negative_space_floor"] = {
        "pass": neg_ok,
        "detail": f"§18 negative items {len(neg_items)}, floor 5"
    }

    # 6. §19 Known Gaps >= 3 items
    s19_match = re.search(r"^##\s+19\..*?(?=^##\s+\d+\.|\Z)", text, re.M | re.S)
    s19 = s19_match.group(0) if s19_match else ""
    gaps = re.findall(r"^[-*]\s+", s19, re.M)
    gaps_ok = len(gaps) >= 3
    result["checks"]["known_gaps_floor"] = {
        "pass": gaps_ok,
        "detail": f"§19 gap items {len(gaps)}, floor 3"
    }

    # 7. file size >= 12KB
    size = len(text.encode("utf-8"))
    size_ok = size >= 12000
    result["checks"]["file_size"] = {
        "pass": size_ok,
        "detail": f"{size/1024:.1f} KB, floor 12 KB"
    }

    # 8. Direction Summary 4-line block (apply Phase 3 regex)
    summary_lines = []
    for key in DIRECTION_SUMMARY_KEYS:
        if re.search(rf">\s*\*\*{re.escape(key)}\*\*:", text, re.M):
            summary_lines.append(key)
    summary_ok = len(summary_lines) == 4
    result["checks"]["direction_summary_format"] = {
        "pass": summary_ok,
        "detail": f"summary keys found: {len(summary_lines)}/4"
    }

    result["pass"] = all(c["pass"] for c in result["checks"].values())
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="design.md file or directory")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--summary-only", action="store_true",
                       help="aggregate counts only")
    args = parser.parse_args()

    target = Path(args.target)
    if not target.exists():
        print(f"ERROR: {target} not found", file=sys.stderr)
        return 2

    if target.is_file():
        files = [target]
    else:
        files = sorted(target.rglob("design.md"))
        if not files:
            print(f"ERROR: no design.md found under {target}", file=sys.stderr)
            return 2

    results = [validate(f) for f in files]

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif args.summary_only:
        total = len(results)
        passed = sum(1 for r in results if r["pass"])
        print(f"PASS: {passed}/{total}")
        for check_name in CHECKS:
            ok = sum(1 for r in results if r["checks"][check_name]["pass"])
            print(f"  {check_name}: {ok}/{total}")
    else:
        for r in results:
            status = "PASS" if r["pass"] else "FAIL"
            print(f"[{status}] {r['path']}")
            if not r["pass"]:
                for check_name, check in r["checks"].items():
                    if not check["pass"]:
                        print(f"  ✗ {check_name}: {check['detail']}")
        total = len(results)
        passed = sum(1 for r in results if r["pass"])
        print(f"\n=== {passed}/{total} PASS ===")

    return 0 if all(r["pass"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
