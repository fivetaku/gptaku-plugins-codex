#!/usr/bin/env python3
"""Extract typography metadata from captured CSS files."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


def group_typography_tokens(props: dict[str, str]) -> dict[str, dict]:
    """Group --*-font-<category>-<variant>-<prop> into {category-variant: {size, weight, lineHeight, letterSpacing}}."""
    grouped: dict[str, dict[str, str]] = {}
    for name, value in props.items():
        match = re.match(
            r"--(.*)font-(heading|text|display|title|label|caption|input|quote|body)-?([a-z0-9]*)-(size|weight|lineHeight|line-height|letterSpacing|letter-spacing)$",
            name,
        )
        if not match:
            continue
        category = match.group(2)
        variant = match.group(3) or "base"
        prop = match.group(4)
        if prop == "line-height":
            prop = "lineHeight"
        elif prop == "letter-spacing":
            prop = "letterSpacing"
        key = f"{category}-{variant}"
        if key not in grouped:
            grouped[key] = {}
        grouped[key][prop] = value.strip()

    category_order = {
        "heading": 0,
        "text": 1,
        "display": 2,
        "title": 3,
        "label": 4,
        "caption": 5,
        "input": 6,
        "quote": 7,
        "body": 8,
    }
    variant_order = {
        "base": 0,
        "xxs": 1,
        "xs": 2,
        "sm": 3,
        "md": 4,
        "lg": 5,
        "xl": 6,
        "xxl": 7,
        "xxxl": 8,
    }

    result: dict[str, dict[str, str]] = {}
    for key in sorted(
        grouped,
        key=lambda item: (
            category_order.get(item.split("-", 1)[0], len(category_order)),
            variant_order.get(item.split("-", 1)[1], len(variant_order)),
            item,
        ),
    ):
        result[key] = {
            prop: grouped[key][prop]
            for prop in ("size", "weight", "lineHeight", "letterSpacing")
            if prop in grouped[key]
        }
    return result


def extract_font_families(css: str) -> list[dict]:
    """Return [{declaration, first_name, count}] from all font-family declarations. Skip var() only."""
    counts = Counter()
    for match in re.finditer(r"font-family\s*:\s*([^;{}]+)", css, re.IGNORECASE):
        declaration = match.group(1).strip()
        parse_target = re.sub(r"\s*!important\s*$", "", declaration, flags=re.IGNORECASE)
        if re.fullmatch(r"var\([^)]*\)", parse_target, re.IGNORECASE):
            continue
        counts[declaration] += 1

    result: list[dict] = []
    for declaration, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        first_name = re.sub(r"\s*!important\s*$", "", declaration, flags=re.IGNORECASE).split(",", 1)[0].strip()
        result.append(
            {
                "declaration": declaration,
                "first_name": first_name.strip("\"'"),
                "count": count,
            }
        )
    return result


def extract_font_weights_used(css: str) -> dict[str, int]:
    """Return {weight_value: count} for font-weight declarations."""
    counts = Counter(
        match.group(1).lower()
        for match in re.finditer(
            r"font-weight\s*:\s*(\d{3}|normal|bold|lighter|bolder)",
            css,
            re.IGNORECASE,
        )
    )
    return {
        weight: counts[weight]
        for weight in sorted(
            counts,
            key=lambda weight: (0, int(weight)) if weight.isdigit() else (1, weight),
        )
    }


def extract_slug(slug: str) -> dict:
    """Read CSS, run all three, write insane-design/{slug}/phase1/typography.json."""
    css_dir = Path.cwd() / "insane-design" / slug / "css"
    output_path = Path.cwd() / "insane-design" / slug / "phase1" / "typography.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    css_files = sorted(css_dir.glob("*.css")) if css_dir.is_dir() else []
    if not css_files:
        # Graceful degradation: CSS 없으면 빈 결과 반환 (CSS-in-JS/인라인 사이트)
        result = {
            "slug": slug,
            "scale": {},
            "families": [],
            "weights_used": {},
            "stats": {"scale_entries": 0, "unique_families": 0, "unique_weights": 0},
            "warning": "No CSS files found — site may use CSS-in-JS or inline styles",
        }
        output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return result

    css = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in css_files)
    props: dict[str, str] = {}
    for name, value in re.findall(r"--([A-Za-z0-9_-]+)\s*:\s*([^;{}]+)", css):
        key = f"--{name}"
        if key not in props:
            props[key] = value.strip()

    scale = group_typography_tokens(props)
    families = extract_font_families(css)
    weights_used = extract_font_weights_used(css)
    result = {
        "slug": slug,
        "scale": scale,
        "families": families,
        "weights_used": weights_used,
        "stats": {
            "scale_entries": len(scale),
            "unique_families": len(families),
            "unique_weights": len(weights_used),
        },
    }

    if slug == "stripe" and result["stats"]["scale_entries"] < 7:
        raise ValueError("stripe must produce at least 7 typography scale entries")

    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> None:
    slug = sys.argv[1] if len(sys.argv) > 1 else "stripe"
    result = extract_slug(slug)
    print(
        json.dumps(
            {
                "slug": slug,
                "output": f"insane-design/{slug}/phase1/typography.json",
                "stats": result["stats"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
