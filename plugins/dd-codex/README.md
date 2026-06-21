# dd-codex

Codex port of the **dd** plugin (v0.3.1) — drop the OS clipboard (text or image) into context and act on it, with no pasting and no boilerplate.

## Triggers

| Trigger | Notes |
|---|---|
| `/dd` | Primary English trigger |
| `/ㅇㅇ` | Korean IME alias — typing `dd` in a Korean IME produces `ㅇㅇ` |
| 클립보드 보내줘 | Korean natural-language |
| 이거 분석해줘 | Korean natural-language |
| 방금 캡처한 거 | Korean natural-language |
| 이 레퍼런스로 | Korean natural-language |
| 스크린샷 드롭 | Korean natural-language |
| drop clipboard | English natural-language |
| use what I copied | English natural-language |
| this screenshot | English natural-language |
| this reference | English natural-language |

## How it works

1. **Capture** — runs `skills/dd/scripts/dd_clipboard.py --json` as its first action. The script writes the clipboard to `~/dd/<date>/<id>/` and prints a JSON manifest.
2. **Gate** — if `ok` is false, surfaces the error and stops.
3. **Preview** — shows one line of what was captured so you can catch a stale grab.
4. **Route** — large or analysis-only captures go to a sub-agent (model pinned to sonnet); small or implementation-needed captures stay in the main session.
5. **Read lazily** — text is read by `size_class` (small/medium/large/huge); images are Read to see them visually.

## Cache

Captures are stored in `~/dd/` (override with `DD_CACHE_DIR`). Old entries are purged automatically after `DD_RETENTION_DAYS` days (default 7).

## Security

Secret patterns (`api_key`, `Bearer`, `sk-`, `ghp_`, `xoxb-`, JWT, AWS AKIA, etc.) are redacted from the preview before it enters context. The raw file on disk is not redacted.

## Platform support

macOS (pbpaste / pngpaste / osascript), Windows, WSL, Linux (wl-paste / xclip / xsel).

## Source

Ported from [`plugins/dd`](../../plugins/dd) in the gptaku_plugins monorepo.
