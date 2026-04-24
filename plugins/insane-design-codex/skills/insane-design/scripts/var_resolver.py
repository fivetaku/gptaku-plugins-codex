from __future__ import annotations

import json
import sys
from pathlib import Path


def parse_all_custom_properties(css: str) -> dict[str, str]:
    """Return {var_name: raw_value} for all --* declarations."""
    import re

    props: dict[str, str] = {}
    for match in re.finditer(r"--([\w-]+)\s*:\s*([^;}]+)", css):
        probe = match.start() - 1
        while probe >= 0 and css[probe].isspace():
            probe -= 1
        if probe >= 0 and css[probe] not in "{;":
            continue
        props[f"--{match.group(1)}"] = match.group(2).strip()
    return props


def _normalize_name(name: str) -> str:
    return name if name.startswith("--") else f"--{name}"


def _unwrap_var_call(value: str) -> str | None:
    stripped = value.strip()
    if not stripped.startswith("var(") or not stripped.endswith(")"):
        return None

    depth = 0
    for index, char in enumerate(stripped):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                return None
            if depth == 0 and index != len(stripped) - 1:
                return None

    if depth != 0:
        return None

    return stripped[4:-1].strip()


def _split_var_arguments(inner: str) -> tuple[str, str | None]:
    depth = 0
    for index, char in enumerate(inner):
        if char == "(":
            depth += 1
        elif char == ")":
            if depth > 0:
                depth -= 1
        elif char == "," and depth == 0:
            fallback = inner[index + 1 :].strip()
            return inner[:index].strip(), fallback or None
    return inner.strip(), None


def _is_terminal_value(value: str) -> bool:
    import re

    stripped = value.strip()
    lowered = stripped.lower()
    return bool(
        re.fullmatch(r"#[0-9a-fA-F]{3,8}", stripped)
        or (
            lowered.startswith(("rgb(", "rgba(", "hsl(", "hsla("))
            and "var(" not in lowered
        )
        or re.fullmatch(r"[-+]?(?:\d+(?:\.\d+)?|\.\d+)(?:[a-zA-Z%]+)?", stripped)
    )


def _prepend_chain(head: str, tail: list[str]) -> list[str]:
    if tail and tail[0] == head:
        return [head, *tail[1:]]
    return [head, *tail]


def _resolve_value(
    value: str, props: dict[str, str], seen: set[str]
) -> tuple[str | None, list[str]]:
    stripped = value.strip()
    if _is_terminal_value(stripped):
        return stripped, [stripped]

    inner = _unwrap_var_call(stripped)
    if inner is None:
        return None, [stripped]

    reference, fallback = _split_var_arguments(inner)
    normalized = _normalize_name(reference)
    if normalized in props:
        return _resolve_var_with_chain(normalized, props, seen)
    if fallback is None:
        return None, [normalized]

    resolved, chain = _resolve_value(fallback, props, seen)
    return resolved, _prepend_chain(normalized, chain)


def _resolve_var_with_chain(
    name: str, props: dict[str, str], seen: set[str] | None = None
) -> tuple[str | None, list[str]]:
    normalized = _normalize_name(name)
    active = set() if seen is None else set(seen)
    if normalized in active:
        return None, [normalized]

    raw = props.get(normalized)
    if raw is None:
        return None, [normalized]

    active.add(normalized)
    resolved, chain = _resolve_value(raw, props, active)
    return resolved, _prepend_chain(normalized, chain)


def resolve_var(name: str, props: dict[str, str], seen: set[str] | None = None) -> str | None:
    """Recursively resolve var(--x, fallback) chains to terminal hex or rgba/hsl string. Returns None for unresolvable, detects cycles via `seen`."""
    resolved, _ = _resolve_var_with_chain(name, props, seen)
    return resolved


def resolve_all(props: dict[str, str]) -> dict[str, dict]:
    """Return {var_name: {raw, resolved_terminal, chain: [str]}} for every var."""
    resolved: dict[str, dict] = {}
    for name, raw in props.items():
        terminal, chain = _resolve_var_with_chain(name, props)
        resolved[name] = {
            "raw": raw,
            "resolved_terminal": terminal,
            "chain": chain,
        }
    return resolved


def resolve_slug(slug: str) -> dict:
    """Top-level: read CSS, parse, resolve, write insane-design/{slug}/phase1/resolved_tokens.json."""
    css_dir = Path.cwd() / "insane-design" / slug / "css"
    output_path = Path.cwd() / "insane-design" / slug / "phase1" / "resolved_tokens.json"

    props: dict[str, str] = {}
    if css_dir.exists():
        for css_file in sorted(css_dir.glob("*.css")):
            props.update(
                parse_all_custom_properties(
                    css_file.read_text(encoding="utf-8", errors="ignore")
                )
            )

    resolved = resolve_all(props)
    resolved_count = sum(
        1 for details in resolved.values() if details["resolved_terminal"] is not None
    )
    samples: dict[str, dict] = {}
    for name, details in list(resolved.items())[:50]:
        samples[name] = {
            "raw": details["raw"],
            "resolved": details["resolved_terminal"],
            "chain": details["chain"],
        }

    result = {
        "slug": slug,
        "total_vars": len(props),
        "resolved_count": resolved_count,
        "unresolved_count": len(props) - resolved_count,
        "samples": samples,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return result


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    slug = args[0] if args else "stripe"
    print(json.dumps(resolve_slug(slug), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
