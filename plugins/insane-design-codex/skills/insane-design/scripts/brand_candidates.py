#!/usr/bin/env python3
"""Extract brand color candidates from scraped CSS and HTML snapshots."""

import json
import re
import sys
from collections import Counter
from pathlib import Path


def _normalize_hex(hex_value: str) -> str:
    value = hex_value.lstrip("#")
    if len(value) in (3, 4):
        value = "".join(ch * 2 for ch in value)
    return f"#{value.upper()}"


def _pick_role(name: str) -> str:
    best: tuple[int, int, str] | None = None
    lowered = name.lower()
    for order, keyword in enumerate(("brand", "primary", "accent", "action", "cta")):
        index = lowered.find(keyword)
        if index == -1:
            continue
        candidate = (index, order, keyword)
        if best is None or candidate < best:
            best = candidate
    return "" if best is None else best[2]


def _count_hexes(text: str) -> Counter:
    counts: Counter = Counter()
    for match in re.finditer(r"#[0-9a-fA-F]{3,8}", text):
        counts[_normalize_hex(match.group(0))] += 1
    return counts


def _hex_saturation(hex_value: str) -> float:
    value = _normalize_hex(hex_value)[1:]
    red = int(value[0:2], 16) / 255
    green = int(value[2:4], 16) / 255
    blue = int(value[4:6], 16) / 255
    high = max(red, green, blue)
    low = min(red, green, blue)
    if high == low:
        return 0.0
    lightness = (high + low) / 2
    divisor = 1 - abs(2 * lightness - 1)
    if divisor == 0:
        return 0.0
    return ((high - low) / divisor) * 100


def _extract_svg_counts(html: str) -> Counter:
    counts: Counter = Counter()
    for match in re.finditer(r"<svg\b[\s\S]*?</svg>", html, re.IGNORECASE):
        counts.update(_count_hexes(match.group(0)))
    return counts


def _extract_logo_wall_counts(html: str) -> Counter:
    counts: Counter = Counter()
    blocks: list[str] = []
    for match in re.finditer(
        r"<(?P<tag>section|div|aside)\b(?=[^>]*(?:class|id|data-[\w-]+)=(['\"])[^'\"]*(?:customer|logo-wall|trusted|featured)[^'\"]*\2)[^>]*>[\s\S]*?</(?P=tag)>",
        html,
        re.IGNORECASE,
    ):
        blocks.append(match.group(0))
    if not any("logo-carousel" in block for block in blocks):
        for match in re.finditer(
            r"<ul\b(?=[^>]*(?:class|id|data-[\w-]+)=(['\"])[^'\"]*logo-carousel[^'\"]*\1)[^>]*>[\s\S]*?</ul>",
            html,
            re.IGNORECASE,
        ):
            blocks.append(match.group(0))
    for block in blocks:
        counts.update(_count_hexes(block))
    return counts


def _empty_result(slug: str) -> dict:
    return {
        "slug": slug,
        "semantic_vars": [],
        "selector_role": [],
        "frequency_candidates": [],
        "summary": {"total_candidates": 0, "by_role": {}},
    }


def _build_summary(
    semantic_vars: list[dict], selector_role: list[dict], frequency_candidates: list[dict]
) -> dict:
    by_role: Counter = Counter()
    for item in semantic_vars:
        by_role[item["role"]] += 1
    if selector_role:
        by_role["selector"] += len(selector_role)
    for item in frequency_candidates:
        by_role[item["kind"]] += 1
    return {
        "total_candidates": len(semantic_vars) + len(selector_role) + len(frequency_candidates),
        "by_role": dict(sorted(by_role.items())),
    }


def extract_semantic_brand_vars(css: str) -> list[dict]:
    """Return [{name, value_hex, role}] for CSS vars named --*-brand-* / --*-primary-* / --*-accent-*."""
    results: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    for match in re.finditer(r"--([\w-]+)\s*:\s*#([0-9a-fA-F]{3,8})", css):
        role = _pick_role(match.group(1))
        if not role:
            continue
        name = f"--{match.group(1)}"
        value_hex = _normalize_hex(match.group(2))
        key = (name, value_hex, role)
        if key in seen:
            continue
        seen.add(key)
        results.append({"name": name, "value_hex": value_hex, "role": role})
    return results


def extract_selector_role_hex(css: str) -> list[dict]:
    """Return [{selector, property, hex, rule_snippet}] for hex values inside CSS rules matching primary CTA button/nav patterns."""
    results: list[dict] = []
    seen: set[tuple[str, str, str, str]] = set()
    for rule_match in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        selector = " ".join(rule_match.group(1).split())
        if not selector or not re.search(r"button|btn|cta|primary|action|nav|link", selector, re.IGNORECASE):
            continue
        body = rule_match.group(2)
        rule_snippet = re.sub(r"\s+", " ", f"{selector} {{{body}}}").strip()[:200]
        for decl_match in re.finditer(r"([\w-]+)\s*:\s*([^;{}]*#[0-9a-fA-F]{3,8}[^;{}]*)", body):
            property_name = decl_match.group(1)
            for hex_match in re.finditer(r"#[0-9a-fA-F]{3,8}", decl_match.group(2)):
                hex_value = _normalize_hex(hex_match.group(0))
                key = (selector, property_name, hex_value, rule_snippet)
                if key in seen:
                    continue
                seen.add(key)
                results.append(
                    {
                        "selector": selector,
                        "property": property_name,
                        "hex": hex_value,
                        "rule_snippet": rule_snippet,
                    }
                )
    return results


def extract_frequency_candidates(css: str, html: str) -> list[dict]:
    """Return [{hex, count, kind}] where kind is one of: frequency|svg_pattern|logo_wall|neutral|chromatic."""
    total_counts = _count_hexes(f"{css}\n{html}")
    if not total_counts:
        return []

    svg_counts = _extract_svg_counts(html)
    logo_wall_counts = _extract_logo_wall_counts(html)

    candidates: list[dict] = []
    for hex_value, count in sorted(total_counts.items(), key=lambda item: (-item[1], item[0]))[:30]:
        kind = "frequency"
        logo_wall_count = logo_wall_counts.get(hex_value, 0)
        if logo_wall_count and logo_wall_count * 2 >= count:
            kind = "logo_wall"
        else:
            svg_count = svg_counts.get(hex_value, 0)
            external_count = count - svg_count
            if svg_count and svg_count >= max(1, external_count * 2):
                kind = "svg_pattern"
            elif _hex_saturation(hex_value) < 10:
                kind = "neutral"
            else:
                kind = "chromatic"
        candidates.append({"hex": hex_value, "count": count, "kind": kind})
    return candidates


def extract_all(slug: str) -> dict:
    """Top-level: reads insane-design/{slug}/css/*.css + insane-design/{slug}/index.html, writes insane-design/{slug}/phase1/brand_candidates.json."""
    service_dir = Path.cwd() / "insane-design" / slug
    css_files = sorted(service_dir.glob("css/*.css"))
    output_path = service_dir / "phase1" / "brand_candidates.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not css_files:
        result = _empty_result(slug)
        output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return result

    css = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in css_files)
    html_path = service_dir / "index.html"
    html = html_path.read_text(encoding="utf-8", errors="replace") if html_path.exists() else ""

    semantic_vars = extract_semantic_brand_vars(css)
    selector_role = extract_selector_role_hex(css)
    frequency_candidates = extract_frequency_candidates(css, html)
    result = {
        "slug": slug,
        "semantic_vars": semantic_vars,
        "selector_role": selector_role,
        "frequency_candidates": frequency_candidates,
        "summary": _build_summary(semantic_vars, selector_role, frequency_candidates),
    }
    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> int:
    slug = sys.argv[1] if len(sys.argv) > 1 else "stripe"
    extract_all(slug)
    print(f"wrote insane-design/{slug}/phase1/brand_candidates.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
