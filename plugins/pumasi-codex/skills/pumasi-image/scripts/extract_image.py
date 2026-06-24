#!/usr/bin/env python3
"""Extract the generated image from `codex exec --json` output (or a session rollout).

codex exec generates images via the `image_generation_call` tool but, unlike the
interactive TUI, does NOT persist them to ~/.codex/generated_images/. The PNG is
returned inline as base64 in the `result` field of `image_generation_call` /
`image_generation_end` events. This decodes that base64 and writes the PNG.

Usage: extract_image.py <source_jsonl> <target_png>
Exit:  0 = wrote target, 1 = no valid image found, 2 = usage error
"""
import sys, json, base64

PNG_SIG = b"\x89PNG\r\n\x1a\n"          # full 8-byte PNG signature
PNG_END = b"IEND\xaeB`\x82"             # IEND chunk + its fixed CRC (PNG must end here)
MIN_PNG = 67                            # smallest real PNG (1x1) is ~67 bytes


def collect_b64(obj, out):
    """Collect candidate base64 result strings, in document order."""
    if isinstance(obj, dict):
        if obj.get("type") in ("image_generation_call", "image_generation_end"):
            r = obj.get("result")
            if isinstance(r, str) and r:
                out.append(r)
        for v in obj.values():
            collect_b64(v, out)
    elif isinstance(obj, list):
        for v in obj:
            collect_b64(v, out)


def decode_valid_png(b64):
    """Return PNG bytes if b64 strictly decodes to a structurally-valid PNG, else None."""
    try:
        raw = base64.b64decode(b64, validate=True)   # reject any non-base64 chars
    except Exception:
        return None
    if (len(raw) >= MIN_PNG
            and raw.startswith(PNG_SIG)
            and raw.endswith(PNG_END)):
        return raw
    return None


def main():
    if len(sys.argv) != 3:
        print("usage: extract_image.py <source_jsonl> <target_png>", file=sys.stderr)
        return 2
    src, target = sys.argv[1], sys.argv[2]
    candidates = []
    try:
        with open(src, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                collect_b64(obj, candidates)
    except OSError as e:
        print(f"cannot read {src}: {e}", file=sys.stderr)
        return 1
    # Prefer the LAST valid image (the final event), not merely the largest —
    # progressive/partial frames can precede the final full image.
    for b64 in reversed(candidates):
        raw = decode_valid_png(b64)
        if raw is not None:
            with open(target, "wb") as out:
                out.write(raw)
            print(f"wrote {len(raw)} bytes to {target}")
            return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
