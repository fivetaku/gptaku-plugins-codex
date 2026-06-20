#!/usr/bin/env python3
"""
Export design.md frontmatter to W3C DTCG (Design Tokens Format Module) tokens.json.

Converts the v3.2 frontmatter token graph (colors / typography / rounded / spacing)
into the standard DTCG shape consumed by Figma Tokens Studio, Style Dictionary,
Specify, Cobalt UI, Penpot, Knapsack, Supernova, and @google/design.md.

Usage:
    python3 export_dtcg.py <design.md>                   # stdout
    python3 export_dtcg.py <design.md> -o tokens.json    # file
    python3 export_dtcg.py <design.md> --pretty          # 2-space indent (default)
    python3 export_dtcg.py <design.md> --compact         # no indent

Exit codes:
    0 = success
    1 = parse error / no frontmatter
    2 = usage error

DTCG spec: https://tr.designtokens.org/format/
"""

import argparse
import json
import re
import sys
from pathlib import Path


HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
DIM_RE = re.compile(r"^-?\d*\.?\d+(px|em|rem|%)$")
TOKEN_REF_RE = re.compile(r"^\{([a-zA-Z][\w.-]*)\}$")


def parse_frontmatter(text: str) -> dict | None:
    """Extract YAML frontmatter and parse with PyYAML or a minimal fallback."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    yaml_text = m.group(1)
    try:
        import yaml
        return yaml.safe_load(yaml_text) or {}
    except ImportError:
        return _minimal_yaml_parse(yaml_text)


def _minimal_yaml_parse(text: str) -> dict:
    """Minimal YAML parser sufficient for v3.2 frontmatter shape.

    Only handles the patterns we emit: scalars, quoted strings, nested maps,
    inline-flow maps for components, and inline-flow lists for typography.ladder.
    Used only when PyYAML is unavailable so the script keeps zero-dep portability.
    """
    out: dict = {}
    stack = [(0, out)]
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()
        while stack and indent < stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if line.startswith("- "):
            item = _parse_scalar(line[2:].strip())
            if isinstance(parent, list):
                parent.append(item)
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if not val:
            child: dict | list = {}
            parent[key] = child
            stack.append((indent + 2, child))
        else:
            parent[key] = _parse_scalar(val)
    return out


def _parse_scalar(s: str):
    s = s.strip()
    if not s:
        return None
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    if s.startswith("'") and s.endswith("'"):
        return s[1:-1]
    if s.startswith("{") and s.endswith("}"):
        return _parse_inline_map(s[1:-1])
    if s.startswith("[") and s.endswith("]"):
        return [_parse_scalar(x) for x in s[1:-1].split(",") if x.strip()]
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


def _parse_inline_map(s: str) -> dict:
    """Parse `{ k: v, k2: v2 }` inline maps (depth 1 only — sufficient for v3.2)."""
    out: dict = {}
    depth = 0
    buf = ""
    parts: list[str] = []
    for ch in s:
        if ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(buf)
            buf = ""
        else:
            buf += ch
    if buf:
        parts.append(buf)
    for p in parts:
        if ":" not in p:
            continue
        k, _, v = p.partition(":")
        out[k.strip()] = _parse_scalar(v.strip())
    return out


def _to_dtcg_ref(value: str) -> str:
    """Convert insane-design `{group.token}` to DTCG `{group.token}` (same shape)."""
    return value


def colors_to_dtcg(colors: dict) -> dict:
    out: dict = {}
    for name, value in colors.items():
        if not isinstance(value, str):
            continue
        if HEX_RE.match(value):
            out[name] = {"$value": value.upper(), "$type": "color"}
        elif TOKEN_REF_RE.match(value):
            out[name] = {"$value": _to_dtcg_ref(value), "$type": "color"}
        else:
            out[name] = {"$value": value, "$type": "color"}
    return out


def typography_to_dtcg(typography: dict) -> dict:
    out: dict = {}
    ladder = typography.get("ladder") if isinstance(typography, dict) else None
    if not isinstance(ladder, list):
        return out
    for entry in ladder:
        if not isinstance(entry, dict):
            continue
        token = entry.get("token")
        if not token:
            continue
        composite = {}
        if "size" in entry:
            composite["fontSize"] = entry["size"]
        if "weight" in entry:
            composite["fontWeight"] = entry["weight"]
        if "line-height" in entry:
            composite["lineHeight"] = entry["line-height"]
        if "lineHeight" in entry:
            composite["lineHeight"] = entry["lineHeight"]
        if "tracking" in entry:
            composite["letterSpacing"] = entry["tracking"]
        family = entry.get("family")
        if not family:
            display_prefixes = ("display", "headline", "hero", "h1", "h2", "h3")
            tk = str(token).lower()
            if any(tk.startswith(pref) for pref in display_prefixes):
                family = typography.get("display") or typography.get("body")
            else:
                family = typography.get("body") or typography.get("display")
        if family:
            composite["fontFamily"] = family
        out[str(token)] = {"$value": composite, "$type": "typography"}
    return out


def dimensions_to_dtcg(group: dict, dtcg_type: str) -> dict:
    out: dict = {}
    for name, value in group.items():
        if isinstance(value, (int, float)):
            out[name] = {"$value": f"{value}px", "$type": dtcg_type}
        elif isinstance(value, str):
            out[name] = {"$value": value, "$type": dtcg_type}
    return out


def build_dtcg(fm: dict) -> dict:
    """Map v3.2 frontmatter to DTCG tokens.json structure."""
    name = fm.get("service_name") or fm.get("slug") or "design-system"
    description = (
        f"Generated from insane-design v3.2 frontmatter (slug={fm.get('slug')}, "
        f"fetched={fm.get('fetched_at')}, source={fm.get('site_url')})"
    )
    root: dict = {
        "$schema": "https://schemas.designtokens.org/2025-10/format/",
        "$description": description,
        "$extensions": {
            "com.insane-design": {
                "schema_version": fm.get("schema_version"),
                "slug": fm.get("slug"),
                "service_name": name,
                "site_url": fm.get("site_url"),
                "fetched_at": str(fm.get("fetched_at")) if fm.get("fetched_at") else None,
                "archetype": fm.get("archetype"),
                "design_system_level": fm.get("design_system_level"),
            }
        },
    }
    colors = fm.get("colors")
    if isinstance(colors, dict) and colors:
        root["color"] = colors_to_dtcg(colors)
    typography = fm.get("typography")
    if isinstance(typography, dict) and typography:
        typo_dtcg = typography_to_dtcg(typography)
        if typo_dtcg:
            root["typography"] = typo_dtcg
    spacing = fm.get("spacing")
    if isinstance(spacing, dict) and spacing:
        root["spacing"] = dimensions_to_dtcg(spacing, "dimension")
    rounded = fm.get("rounded")
    if isinstance(rounded, dict) and rounded:
        root["radius"] = dimensions_to_dtcg(rounded, "dimension")
    return root


def main() -> int:
    p = argparse.ArgumentParser(description="design.md → DTCG tokens.json")
    p.add_argument("input", type=Path, help="path to design.md")
    p.add_argument("-o", "--output", type=Path, help="output path (default: stdout)")
    p.add_argument("--compact", action="store_true", help="no indentation")
    args = p.parse_args()

    if not args.input.is_file():
        print(f"error: not a file: {args.input}", file=sys.stderr)
        return 2

    text = args.input.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        print(f"error: no frontmatter in {args.input}", file=sys.stderr)
        return 1

    dtcg = build_dtcg(fm)
    indent = None if args.compact else 2
    payload = json.dumps(dtcg, indent=indent, ensure_ascii=False)

    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
