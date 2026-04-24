#!/usr/bin/env python3
"""Convert Codex JSONL sessions into readable Markdown."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def text_from_content(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""

    parts: list[str] = []
    for item in content:
        if not isinstance(item, dict):
            continue
        text = item.get("text") or item.get("input_text") or item.get("output_text")
        if isinstance(text, str):
            parts.append(text)
    return "\n".join(parts).strip()


def parse_session(path: Path) -> dict[str, Any]:
    meta: dict[str, Any] = {"id": path.stem, "timestamp": "", "cwd": ""}
    messages: list[dict[str, str]] = []

    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue

        event_type = event.get("type")
        payload = event.get("payload") or {}

        if event_type == "session_meta":
            meta_payload = payload or {}
            meta["id"] = meta_payload.get("id") or meta["id"]
            meta["timestamp"] = meta_payload.get("timestamp") or event.get("timestamp") or ""
            meta["cwd"] = meta_payload.get("cwd") or ""
            continue

        if event_type != "response_item" or not isinstance(payload, dict):
            continue

        if payload.get("type") != "message":
            continue

        role = payload.get("role", "unknown")
        text = text_from_content(payload.get("content"))
        if text:
            messages.append({"role": role, "text": text})

    return {"path": path, "meta": meta, "messages": messages}


def title_for(session: dict[str, Any]) -> str:
    timestamp = session["meta"].get("timestamp") or ""
    cwd = session["meta"].get("cwd") or "unknown-workspace"
    workspace = Path(cwd).name if cwd else "unknown-workspace"
    if timestamp:
        return f"{timestamp[:10]} {workspace}"
    return workspace


def write_session(session: dict[str, Any], output_dir: Path) -> Path:
    meta = session["meta"]
    stamp = (meta.get("timestamp") or "unknown-date").replace(":", "-")
    safe_id = str(meta.get("id") or session["path"].stem).replace("/", "-")
    out = output_dir / f"{stamp}-{safe_id}.md"

    lines = [
        f"# {title_for(session)}",
        "",
        f"- Source: `{session['path']}`",
        f"- Workspace: `{meta.get('cwd') or 'unknown'}`",
        f"- Session ID: `{meta.get('id') or session['path'].stem}`",
        "",
        "## Conversation",
        "",
    ]

    for message in session["messages"]:
        role = message["role"].title()
        lines.append(f"### {role}")
        lines.append("")
        lines.append(message["text"].strip())
        lines.append("")

    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert Codex JSONL sessions to Markdown")
    parser.add_argument("--input-dir", default=str(Path.home() / ".codex" / "sessions"))
    parser.add_argument("--output-dir", default=str(Path.home() / "vibe-sunsang" / "conversations"))
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    input_dir = Path(args.input_dir).expanduser()
    output_dir = Path(args.output_dir).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.rglob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    if args.limit > 0:
        files = files[: args.limit]

    converted: list[Path] = []
    for path in files:
        session = parse_session(path)
        if not session["messages"]:
            continue
        out = output_dir / f"{(session['meta'].get('timestamp') or 'unknown-date').replace(':', '-')}-{session['meta'].get('id') or path.stem}.md"
        if out.exists() and not args.force:
            converted.append(out)
            continue
        converted.append(write_session(session, output_dir))

    index_lines = [
        "# vibe-sunsang Conversation Index",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Source: `{input_dir}`",
        "",
    ]
    for out in converted:
        index_lines.append(f"- [{out.stem}]({out.name})")
    (output_dir / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    print(f"converted={len(converted)} output={output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
