#!/usr/bin/env python3
"""Capture the current OS clipboard (text or image) into a local cache.

The script is intentionally standalone and stdlib-only so a Codex
command can run it without loading large clipboard content into chat first.
It always prints a single valid JSON object to stdout (even on failure), so
the caller can rely on parsing it.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import os
import platform
import re
import shutil
import subprocess
import sys
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable


DEFAULT_CACHE_DIR = "~/dd"            # CCPS §10: user data lives in ~/{plugin-name}/
TEXT_FILE = "content.txt"
IMAGE_FILE = "image.png"
MANIFEST_FILE = "manifest.json"

DEFAULT_RETENTION_DAYS = 7
IMAGE_OVERSIZE_BYTES = 15_000_000     # flag (not reject) images bigger than ~15MB


@dataclass
class CommandResult:
    returncode: int
    stdout: bytes
    stderr: bytes


@dataclass
class ClipboardItem:
    kind: str
    path: Path
    bytes: int
    sha256: str
    chars: int | None = None
    line_count: int | None = None
    estimated_tokens: int | None = None
    size_class: str | None = None
    summary_candidate: bool | None = None
    oversized: bool | None = None
    preview: str | None = None
    source: str | None = None

    def to_json(self) -> dict[str, object]:
        data: dict[str, object] = {
            "kind": self.kind,
            "path": str(self.path),
            "bytes": self.bytes,
            "sha256": self.sha256,
        }
        if self.chars is not None:
            data["chars"] = self.chars
        if self.line_count is not None:
            data["line_count"] = self.line_count
        if self.estimated_tokens is not None:
            data["estimated_tokens"] = self.estimated_tokens
        if self.size_class is not None:
            data["size_class"] = self.size_class
        if self.summary_candidate is not None:
            data["summary_candidate"] = self.summary_candidate
        if self.oversized is not None:
            data["oversized"] = self.oversized
        if self.preview is not None:
            data["preview"] = self.preview
        if self.source:
            data["source"] = self.source
        return data


def run_cmd(
    cmd: list[str],
    *,
    input_bytes: bytes | None = None,
    timeout: int = 12,
) -> CommandResult:
    try:
        proc = subprocess.run(
            cmd,
            input=input_bytes,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
        return CommandResult(proc.returncode, proc.stdout, proc.stderr)
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        return CommandResult(127, b"", str(exc).encode("utf-8", "replace"))


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def detect_platform() -> str:
    if is_wsl():
        return "wsl"
    plat = str(sys.platform)  # widen so platform-narrowing doesn't mark branches dead
    if plat == "darwin":
        return "macos"
    if plat.startswith("win"):
        return "windows"
    return "linux"


def is_wsl() -> bool:
    if os.environ.get("WSL_INTEROP") or os.environ.get("WSL_DISTRO_NAME"):
        return True
    version = Path("/proc/version")
    try:
        return "microsoft" in version.read_text(errors="ignore").lower()
    except OSError:
        return False


def now_local() -> datetime:
    return datetime.now().astimezone()


def env_int(name: str, default: int) -> int:
    """Read an int env var, falling back to default on a bad value.

    Keeps the '--json always prints valid JSON' guarantee: a typo like
    DD_PREVIEW_LINES=abc must not raise ValueError before capture runs.
    """
    try:
        return int(os.environ.get(name, default))
    except (TypeError, ValueError):
        return default


def sha256_file(path: Path) -> str:
    """Hash a file in chunks so a huge capture never loads fully into memory."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def make_entry_dir(cache_dir: Path) -> Path:
    stamp = now_local()
    entry = cache_dir / stamp.strftime("%Y-%m-%d") / (
        stamp.strftime("%H%M%S") + "-" + uuid.uuid4().hex[:12]
    )
    entry.mkdir(parents=True, exist_ok=True)
    return entry


def cleanup_old_entries(cache_dir: Path, retention_days: int) -> None:
    """Delete capture day-folders older than retention_days. Never raises."""
    if retention_days <= 0:
        return
    try:
        cutoff = (now_local() - timedelta(days=retention_days)).date()
        for day_dir in cache_dir.iterdir():
            if not day_dir.is_dir():
                continue
            try:
                day = datetime.strptime(day_dir.name, "%Y-%m-%d").date()
            except ValueError:
                continue  # not a capture day-folder
            if day < cutoff:
                shutil.rmtree(day_dir, ignore_errors=True)
    except OSError:
        return


def decode_text(data: bytes) -> str:
    # PowerShell may emit UTF-16LE if the host encoding is odd; handle that
    # before falling back to UTF-8.
    if data.startswith(b"\xff\xfe") or data.startswith(b"\xfe\xff"):
        return data.decode("utf-16", "replace")
    decoded = data.decode("utf-8", "replace")
    nul_count = decoded.count("\x00")
    if nul_count > max(2, len(decoded) // 20):
        return data.decode("utf-16le", "replace")
    return decoded


def normalize_clipboard_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Strip stray NUL bytes that survive odd UTF-16 decoding so content.txt
    # and previews stay clean.
    text = text.replace("\x00", "")
    return text


SECRET_PATTERNS = [
    re.compile(
        r"(?i)\b(api[_-]?key|secret[_-]?key|client[_-]?secret|access[_-]?token|"
        r"refresh[_-]?token|token|secret|password|passwd|authorization|cookie|"
        r"private[_-]?key)\b(\s*[:=]\s*)(\"?[^\s,;\"]+)"
    ),
    re.compile(r"(?i)\b(bearer\s+)([a-z0-9._~+/=-]{12,})"),
    re.compile(r"\b(sk-[a-zA-Z0-9_-]{12,})"),
    re.compile(r"\b(gh[pousr]_[A-Za-z0-9]{16,})"),
    re.compile(r"\b(xox[baprs]-[A-Za-z0-9-]{10,})"),
    re.compile(r"\b(AKIA[0-9A-Z]{16})\b"),
    re.compile(r"\b(eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{6,})"),
    re.compile(r"\b(AIza[0-9A-Za-z_-]{30,})"),
    re.compile(r"\b(glpat-[A-Za-z0-9_-]{16,})"),
]


def redact_preview(text: str) -> str:
    redacted = text
    redacted = SECRET_PATTERNS[0].sub(r"\1\2[REDACTED]", redacted)
    redacted = SECRET_PATTERNS[1].sub(r"\1[REDACTED]", redacted)
    redacted = SECRET_PATTERNS[2].sub("[REDACTED_KEY]", redacted)
    redacted = SECRET_PATTERNS[3].sub("[REDACTED_TOKEN]", redacted)
    redacted = SECRET_PATTERNS[4].sub("[REDACTED_TOKEN]", redacted)
    redacted = SECRET_PATTERNS[5].sub("[REDACTED_AWS]", redacted)
    redacted = SECRET_PATTERNS[6].sub("[REDACTED_JWT]", redacted)
    redacted = SECRET_PATTERNS[7].sub("[REDACTED_KEY]", redacted)
    redacted = SECRET_PATTERNS[8].sub("[REDACTED_TOKEN]", redacted)
    return redacted


def make_preview(text: str, *, max_chars: int, preview_lines: int) -> str:
    # Redact BEFORE truncating so a secret split at the char boundary can't
    # leak a partial value into the preview.
    preview = redact_preview("\n".join(text.splitlines()[:preview_lines]))
    if len(preview) > max_chars:
        preview = preview[:max_chars].rstrip() + "\n..."
    return preview


def assess_text_size(text: str, byte_count: int) -> dict[str, int | str | bool]:
    chars = len(text)
    line_count = len(text.splitlines())
    estimated_tokens = max(math.ceil(chars / 3), math.ceil(byte_count / 4))

    if estimated_tokens >= 15_000 or chars >= 50_000:
        size_class = "huge"
    elif estimated_tokens >= 6_000:
        size_class = "large"
    elif estimated_tokens >= 2_000:
        size_class = "medium"
    else:
        size_class = "small"

    return {
        "chars": chars,
        "line_count": line_count,
        "estimated_tokens": estimated_tokens,
        "size_class": size_class,
        "summary_candidate": size_class in {"large", "huge"},
    }


def powershell_exe(prefer_windows_exe: bool = False) -> str | None:
    candidates = ["powershell.exe"] if prefer_windows_exe else []
    candidates.extend(["powershell", "pwsh", "powershell.exe"])
    for candidate in candidates:
        if command_exists(candidate):
            return candidate
    return None


def run_powershell(script: str, *, prefer_windows_exe: bool = False) -> CommandResult:
    exe = powershell_exe(prefer_windows_exe=prefer_windows_exe)
    if not exe:
        return CommandResult(127, b"", b"PowerShell executable not found")
    encoded = base64.b64encode(script.encode("utf-16le")).decode("ascii")
    return run_cmd(
        [
            exe,
            "-NoProfile",
            "-NonInteractive",
            "-Sta",
            "-ExecutionPolicy",
            "Bypass",
            "-EncodedCommand",
            encoded,
        ],
        timeout=25,
    )


def wsl_to_windows_path(path: Path) -> str:
    result = run_cmd(["wslpath", "-w", str(path)])
    if result.returncode != 0:
        raise RuntimeError(decode_text(result.stderr or result.stdout).strip())
    return decode_text(result.stdout).strip()


def linux_clipboard_tools() -> list[str]:
    return [t for t in ("wl-paste", "xclip", "xsel") if command_exists(t)]


def get_text(platform_name: str) -> tuple[str | None, str | None]:
    if platform_name == "macos":
        result = run_cmd(["pbpaste"])
        if result.returncode == 0:
            return normalize_clipboard_text(decode_text(result.stdout)), "pbpaste"
        return None, None

    if platform_name in {"windows", "wsl"}:
        script = (
            "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8\n"
            "try { Get-Clipboard -Raw -ErrorAction Stop } catch { exit 2 }\n"
        )
        result = run_powershell(script, prefer_windows_exe=(platform_name == "wsl"))
        if result.returncode == 0:
            return normalize_clipboard_text(decode_text(result.stdout)), "powershell:Get-Clipboard"
        return None, None

    if command_exists("wl-paste"):
        result = run_cmd(["wl-paste", "--no-newline"])
        if result.returncode == 0:
            return normalize_clipboard_text(decode_text(result.stdout)), "wl-paste"

    if command_exists("xclip"):
        result = run_cmd(["xclip", "-selection", "clipboard", "-o"])
        if result.returncode == 0:
            return normalize_clipboard_text(decode_text(result.stdout)), "xclip"

    if command_exists("xsel"):
        result = run_cmd(["xsel", "--clipboard", "--output"])
        if result.returncode == 0:
            return normalize_clipboard_text(decode_text(result.stdout)), "xsel"

    return None, None


MACOS_IMAGE_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp",
    ".tiff", ".tif", ".heic", ".heif", ".bmp",
}


def macos_file_url_image(out_path: Path) -> str | None:
    """Resolve an image FILE reference on the clipboard to the real file.

    Copying a file in Finder puts a file URL (plus the file's *icon*) on the
    clipboard, not the real pixels. Read the file URL and use the actual file
    so '/dd' on a copied image file captures the real image, not the icon.
    """
    result = run_cmd(["osascript", "-e", "POSIX path of (the clipboard as «class furl»)"])
    if result.returncode != 0:
        return None
    src = decode_text(result.stdout).rstrip("\r\n")  # keep filename whitespace
    if not src:
        return None
    src_path = Path(src)
    if not src_path.is_file() or src_path.suffix.lower() not in MACOS_IMAGE_EXTS:
        return None
    try:
        if src_path.suffix.lower() == ".png":
            shutil.copyfile(src_path, out_path)
        else:
            conv = run_cmd(
                ["sips", "-s", "format", "png", str(src_path), "--out", str(out_path)],
                timeout=30,
            )
            if conv.returncode != 0:
                return None
    except OSError:
        return None
    if out_path.exists() and out_path.stat().st_size > 0:
        return f"file:{src_path.name}"
    out_path.unlink(missing_ok=True)
    return None


def save_macos_image(path: Path) -> str | None:
    # 1. Clipboard holds an image FILE reference (e.g. copied in Finder) → use
    #    the real file, not the icon that pngpaste/PNGf would return.
    source = macos_file_url_image(path)
    if source:
        return source

    if command_exists("pngpaste"):
        result = run_cmd(["pngpaste", str(path)], timeout=30)
        if result.returncode == 0 and path.exists() and path.stat().st_size > 0:
            return "pngpaste"
        path.unlink(missing_ok=True)

    png_class = "«class PNGf»"
    tiff_class = "«class TIFF»"

    if save_macos_clipboard_class(path, png_class):
        return "osascript:PNGf"

    tiff_path = path.with_suffix(".tiff")
    if save_macos_clipboard_class(tiff_path, tiff_class):
        result = run_cmd(
            ["sips", "-s", "format", "png", str(tiff_path), "--out", str(path)],
            timeout=30,
        )
        tiff_path.unlink(missing_ok=True)
        if result.returncode == 0 and path.exists() and path.stat().st_size > 0:
            return "osascript:TIFF+sips"
        path.unlink(missing_ok=True)

    return None


def save_macos_clipboard_class(path: Path, apple_class: str) -> bool:
    script = [
        "on run argv",
        "set outPath to item 1 of argv",
        "set outFile to open for access (POSIX file outPath) with write permission",
        "set eof outFile to 0",
        f"write (the clipboard as {apple_class}) to outFile",
        "close access outFile",
        "end run",
    ]
    result = run_cmd(
        ["osascript", *sum((["-e", line] for line in script), []), str(path)],
        timeout=30,
    )
    if result.returncode == 0 and path.exists() and path.stat().st_size > 0:
        return True
    path.unlink(missing_ok=True)
    return False


def save_windows_image(path: Path, platform_name: str) -> str | None:
    target = wsl_to_windows_path(path) if platform_name == "wsl" else str(path)
    escaped_target = target.replace("'", "''")
    script = f"""
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
$path = '{escaped_target}'
$exts = @('.png','.jpg','.jpeg','.gif','.webp','.tiff','.tif','.bmp')
# 1) image FILE copied in Explorer (file drop list) -> use the real file,
#    not the clipboard image (which may be absent or just an icon).
if ([System.Windows.Forms.Clipboard]::ContainsFileDropList()) {{
  foreach ($f in [System.Windows.Forms.Clipboard]::GetFileDropList()) {{
    if (($exts -contains [System.IO.Path]::GetExtension($f).ToLower()) -and (Test-Path -LiteralPath $f)) {{
      $img = [System.Drawing.Image]::FromFile($f)
      $img.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
      $img.Dispose()
      Write-Output ('file:' + [System.IO.Path]::GetFileName($f))
      exit 0
    }}
  }}
}}
# 2) image CONTENT on the clipboard
if (-not [System.Windows.Forms.Clipboard]::ContainsImage()) {{ exit 2 }}
$image = [System.Windows.Forms.Clipboard]::GetImage()
if ($null -eq $image) {{ exit 3 }}
$image.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
exit 0
"""
    result = run_powershell(script, prefer_windows_exe=(platform_name == "wsl"))
    if result.returncode == 0 and path.exists() and path.stat().st_size > 0:
        out = decode_text(result.stdout).strip().splitlines()
        label = next((ln for ln in out if ln.startswith("file:")), None)
        return label or "powershell:ClipboardImage"
    path.unlink(missing_ok=True)
    return None


def save_linux_image(path: Path) -> str | None:
    if command_exists("wl-paste"):
        result = run_cmd(["wl-paste", "--type", "image/png"])
        if result.returncode == 0 and result.stdout:
            path.write_bytes(result.stdout)
            return "wl-paste:image/png"

    if command_exists("xclip"):
        result = run_cmd(["xclip", "-selection", "clipboard", "-t", "image/png", "-o"])
        if result.returncode == 0 and result.stdout:
            path.write_bytes(result.stdout)
            return "xclip:image/png"

    return None


def save_image(platform_name: str, path: Path) -> str | None:
    if platform_name == "macos":
        return save_macos_image(path)
    if platform_name in {"windows", "wsl"}:
        return save_windows_image(path, platform_name)
    return save_linux_image(path)


def item_from_file(
    *,
    kind: str,
    path: Path,
    source: str | None,
    text: str | None = None,
    max_preview_chars: int,
    preview_lines: int,
) -> ClipboardItem:
    byte_count = path.stat().st_size
    digest = sha256_file(path)
    preview = None
    chars = None
    line_count = None
    estimated_tokens = None
    size_class = None
    summary_candidate = None
    oversized = None
    if text is not None:
        assessment = assess_text_size(text, byte_count)
        chars = int(assessment["chars"])
        line_count = int(assessment["line_count"])
        estimated_tokens = int(assessment["estimated_tokens"])
        size_class = str(assessment["size_class"])
        summary_candidate = bool(assessment["summary_candidate"])
        preview = make_preview(
            text,
            max_chars=max_preview_chars,
            preview_lines=preview_lines,
        )
    else:
        # image — flag (do not reject) very large captures so the reader can
        # avoid blowing the context window with a giant PNG.
        oversized = byte_count > IMAGE_OVERSIZE_BYTES
    return ClipboardItem(
        kind=kind,
        path=path,
        bytes=byte_count,
        sha256=digest,
        chars=chars,
        line_count=line_count,
        estimated_tokens=estimated_tokens,
        size_class=size_class,
        summary_candidate=summary_candidate,
        oversized=oversized,
        preview=preview,
        source=source,
    )


def empty_clipboard_message(platform_name: str) -> str:
    if platform_name == "linux" and not linux_clipboard_tools():
        return (
            "No clipboard tool found — install one first "
            "(e.g. `sudo apt install xclip` or `wl-clipboard`), then copy and retry."
        )
    return "Clipboard is empty — copy text or capture an image first, then run /dd again."


def capture_clipboard(args: argparse.Namespace) -> dict[str, object]:
    # Captured clipboard data may contain secrets → restrict new dirs to 0700
    # and new files to 0600 so other local users cannot read the cache.
    os.umask(0o077)
    cache_dir = Path(args.cache_dir).expanduser().resolve()
    entry_dir = make_entry_dir(cache_dir)
    try:
        os.chmod(cache_dir, 0o700)
    except OSError:
        pass
    platform_name = detect_platform()
    items: list[ClipboardItem] = []
    errors: list[str] = []

    if args.prefer in {"auto", "text"}:
        text, source = get_text(platform_name)
        if text:
            text_path = entry_dir / TEXT_FILE
            text_path.write_text(text, encoding="utf-8")
            items.append(
                item_from_file(
                    kind="text",
                    path=text_path,
                    source=source,
                    text=text,
                    max_preview_chars=args.max_preview_chars,
                    preview_lines=args.preview_lines,
                )
            )
        elif args.prefer == "text":
            errors.append(empty_clipboard_message(platform_name))

    if args.prefer in {"auto", "image"}:
        image_path = entry_dir / IMAGE_FILE
        source = save_image(platform_name, image_path)
        if source:
            items.append(
                item_from_file(
                    kind="image",
                    path=image_path,
                    source=source,
                    max_preview_chars=args.max_preview_chars,
                    preview_lines=args.preview_lines,
                )
            )
        elif args.prefer == "image":
            errors.append("No image found in the clipboard — copy or capture an image first.")

    # Auto mode with nothing captured: never report a silent ok:false with
    # an empty errors list. Tell the user what to do.
    if not items and not errors:
        errors.append(empty_clipboard_message(platform_name))

    manifest = build_manifest(
        entry_dir=entry_dir,
        platform_name=platform_name,
        items=items,
        errors=errors,
    )
    # atomic write: a crash mid-write must not leave a truncated manifest.json
    manifest_tmp = entry_dir / (MANIFEST_FILE + ".tmp")
    manifest_tmp.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(manifest_tmp, entry_dir / MANIFEST_FILE)

    cleanup_old_entries(cache_dir, args.retention_days)
    return manifest


def build_manifest(
    *,
    entry_dir: Path,
    platform_name: str,
    items: Iterable[ClipboardItem],
    errors: list[str],
) -> dict[str, object]:
    item_json = [item.to_json() for item in items]
    # tie-break: when a single copy carries both text and image, the image is
    # the primary context (screenshot/reference debugging is the core use case).
    image_items = [i for i in item_json if i.get("kind") == "image"]
    primary = image_items[0] if image_items else (item_json[0] if item_json else None)
    return {
        "ok": bool(item_json),
        "captured_at": now_local().isoformat(timespec="seconds"),
        "platform": platform_name,
        "host": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "entry_dir": str(entry_dir),
        "manifest_path": str(entry_dir / MANIFEST_FILE),
        "primary": primary,
        "items": item_json,
        "errors": errors,
        "usage": "Treat the captured clipboard item(s) as the primary context for the user's /dd request.",
    }


def print_human(manifest: dict[str, object]) -> None:
    if not manifest.get("ok"):
        print("No clipboard content captured.")
        errors = manifest.get("errors") or []
        if isinstance(errors, list):
            for error in errors:
                print(f"- {error}")
        mp = manifest.get("manifest_path")
        if mp:
            print(f"manifest: {mp}")
        return

    primary = manifest.get("primary") or {}
    items = manifest.get("items") or []
    item_count = len(items) if isinstance(items, list) else 0
    print(f"captured: {item_count} item(s)")
    print(f"platform: {manifest['platform']}")
    print(f"entry: {manifest['entry_dir']}")
    if isinstance(primary, dict):
        print(f"primary: {primary.get('kind')} {primary.get('path')}")
        if primary.get("kind") == "text":
            print(f"chars: {primary.get('chars')} | size_class: {primary.get('size_class')}")
            preview = primary.get("preview")
            if preview:
                print("preview:")
                print(preview)
        elif primary.get("kind") == "image":
            size_kb = int(primary.get("bytes", 0)) // 1024
            flag = " (oversized — describe by metadata, avoid full read)" if primary.get("oversized") else ""
            print(f"image: {size_kb} KB{flag}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture the current clipboard into ~/dd (text or image)."
    )
    parser.add_argument(
        "--cache-dir",
        default=os.environ.get("DD_CACHE_DIR", DEFAULT_CACHE_DIR),
        help="Where captured clipboard entries are stored.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the manifest as JSON.",
    )
    parser.add_argument(
        "--prefer",
        choices=["auto", "text", "image"],
        default="auto",
        help="Capture text, image, or both in auto mode.",
    )
    parser.add_argument(
        "--preview-lines",
        type=int,
        default=env_int("DD_PREVIEW_LINES", 20),
        help="Maximum lines to include in the text preview.",
    )
    parser.add_argument(
        "--max-preview-chars",
        type=int,
        default=env_int("DD_MAX_PREVIEW_CHARS", 2000),
        help="Maximum characters to include in the text preview.",
    )
    parser.add_argument(
        "--retention-days",
        type=int,
        default=env_int("DD_RETENTION_DAYS", DEFAULT_RETENTION_DAYS),
        help="Delete cached captures older than this many days (0 disables).",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        manifest = capture_clipboard(args)
    except Exception as exc:  # never leak a traceback into stdout JSON
        manifest = {
            "ok": False,
            "errors": [f"dd capture failed: {exc}"],
            "primary": None,
            "items": [],
        }
        if args.json:
            print(json.dumps(manifest, ensure_ascii=False, indent=2))
        else:
            print_human(manifest)
        return 2

    if args.json:
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
    else:
        print_human(manifest)
    return 0 if manifest["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
