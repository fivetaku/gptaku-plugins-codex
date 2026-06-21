---
name: dd
description: Use this skill when the user runs /dd or /ㅇㅇ (Hangul IME alias — typing "dd" in Korean IME produces "ㅇㅇ") to act on the current OS clipboard (text or image) without pasting it into chat. Captures the live clipboard into a local cache and uses only the manifest plus a short preview as context. Korean triggers — /dd, /ㅇㅇ, 클립보드 보내줘, 이거 분석해줘, 방금 캡처한 거, 이 레퍼런스로, 스크린샷 드롭. English triggers — /dd, drop clipboard, use what I copied, this screenshot, this reference.
---

# dd — Drop Clipboard into Context

> Capture the current OS clipboard and act on it, without pasting raw content into chat.

The user copied or screenshotted something — usually a design reference or screenshot, sometimes an error log, code, or URL — and wants it used as the reference for their request. `/dd` and `/ㅇㅇ` capture the live clipboard into `~/dd/` and inject only a manifest summary, keeping the conversation clean.

## Workflow

### Step 1 — Capture (always first)

Run this as your VERY FIRST action, before anything else:

```
python3 "$PLUGIN_ROOT/skills/dd/scripts/dd_clipboard.py" --json
```

The script writes the clipboard to `~/dd/<date>/<id>/` and prints a JSON manifest with fields: `ok`, `primary` (`kind`, `path`, `size_class`, `preview`, `oversized`), `items`, `errors`, `captured_at`, `platform`.

### Step 2 — Empty / failure gate

Check `ok` first. If it is false, show the `errors[]` to the user verbatim and STOP. The clipboard is empty or unsupported — do not proceed with empty context or invent content.

Example reply: "클립보드가 비어있어요. 복사하고 다시 /dd 해주세요."

This matters because the clipboard usually holds *something*; a true `ok:false` is rare and worth surfacing.

### Step 3 — Identify the capture and the task

Show one short line of what was captured:
- text — `kind`, `size_class`, first ~2 lines of `preview`
- image — `image, <KB>, saved to <path>`

This gives the user a chance to catch a wrong or stale grab. The clipboard keeps only the most recent copy with no timestamp — something copied long ago can still be sitting there.

Then settle the task from the user's request (passed as the skill argument). If that is empty, infer intent from the content AND the ongoing conversation, and say the inferred intent in one line before acting (e.g. "📋 에러 로그 감지 → 원인부터 볼게요"). Mapping heuristics: error/traceback → debug; code → explain/review; broken-UI image → diagnose; URL/doc → summarize. If intent stays ambiguous, fall back to the Step 4 confirm gate rather than guessing.

### Step 4 — Confirm gate (only when it looks wrong)

Judge whether the captured item matches intent:
- Request is non-empty but the clipboard is clearly unrelated → ask "클립보드에 <요약> 있는데, 이거 맞아요?" before acting.
- No request and you cannot tell from the ongoing conversation what to do → ask the same.
- Otherwise (clipboard clearly fits the request, or fits what the conversation is already doing) → act directly, do not ask.

Confirm with a normal question in your reply, not a tool call. Do not over-ask — gate only on a real mismatch. Per `shared/questioning-policy.md §2c`: if the request is concrete and the clipboard fits, proceed immediately.

### Step 5 — Context routing gate

Decide whether the captured item should be handled in the main session or delegated to a background sub-agent. The goal is to keep the active conversation light.

**Delegate to a sub-agent when:**
- the request is mainly analysis, summary, extraction, explanation, or diagnosis
- captured text is `large` or `huge`
- image is one-off reference material and the user only asks what it means, why it looks wrong, or what should change
- the task can be answered with a compact conclusion, checklist, error cause, or visual brief

The sub-agent reads `content.txt` or `image.png`, analyzes it, and returns only the useful result to the main session. Do not copy the full raw content back into the main conversation.

**Model pin:** always spawn dd sub-agents with `model: sonnet`. Never let the sub-agent inherit the main session model — dd's delegated work (summaries, error triage, visual briefs) does not need an expensive model.

**Diagnosis guidance:** when delegating error/log diagnosis, include this instruction in the sub-agent prompt: locate the FIRST anomaly in the timeline, then look at what changed immediately BEFORE it (deploys, config reloads, version changes, flag flips); treat the error flood at the tail as a consequence, not the cause. Without this, the sub-agent tends to stop at the surface mechanism and prescribe symptom-level fixes.

**Stay in main session when:**
- the captured item is small enough to answer from the `preview`
- the user wants the repo edited based on the capture
- the capture is referenced repeatedly during implementation
- exact code, exact lines, or exact visual details are needed while modifying files

**Hybrid rule:** if the task needs implementation but the capture is large, first have a sub-agent write a compact brief (`dd_brief.md`, `error_summary.md`, or `visual_reference.md`). Then the main session works from that brief and only reads focused slices of the original when necessary.

Never read a large or huge capture into the main session just because it exists. Read only what the current task needs.

### Step 6 — Read by size (text)

Lead with the manifest `preview`. Read the file only as needed so a huge paste never floods context:
- `small` → answer from `preview`; do not open the file.
- `medium` → use `rg`/`head`/`tail` on `content.txt`; avoid a full read.
- `large` → read focused ranges; write `summary.md` only if the request truly needs a summary or the same capture is reused.
- `huge` → never read the whole file; search with `rg` for error keywords and read head/tail only.

Never paste the full content into chat.

### Step 7 — Images

For `kind: image`, Read the saved `image.png` to actually see it, then act on the request (e.g. "이런 느낌으로 만들어줘", "왜 깨져?"). Do not create an automatic summary for images. If `oversized` is true, avoid a full read — describe from metadata or ask the user to crop the area that matters.

## Language

Reply in the user's language, decided fresh each time — nothing is stored:
- The request has text → reply in that text's language (`/dd what is this` → English; `/dd 이거 뭐야` → Korean).
- No request → reply in the language the user has been using in this conversation (it is already in context).
- A fresh session whose first message is a bare `/dd` (no request text and no prior conversation) → reply in English, or ask once which language to use.

Never default to Korean just because the plugin was authored in Korea.

## Why this shape

The clipboard is a single most-recent slot with no timestamp, so freshness cannot be measured — only judged by whether the content fits the intent (Steps 3–4). Reading lazily by `size_class` (Step 6) keeps token cost low, which is a side benefit; the main job is simply handing the clipboard to Codex — and, for heavy items, handing it to a sub-agent and keeping only the conclusion (Step 5).

## Security

- The script redacts `api_key`/`token`/`password`/`Bearer`/`sk-`/`ghp_`/`xoxb-` patterns in the preview. The raw file on disk is not redacted, so do not echo full raw content back unnecessarily.
- The cache lives in `~/dd/` and auto-deletes captures older than `DD_RETENTION_DAYS` (default 7) on each run. Nothing is uploaded anywhere.

## Scripts

- **`scripts/dd_clipboard.py`** — captures the clipboard, writes the cache and manifest, computes the text size class, redacts the preview, flags oversized images, and cleans up old captures. Run with `--json`. Uses `$PLUGIN_ROOT` for self-referencing the script path. Environment: `DD_CACHE_DIR` (default `~/dd`), `DD_RETENTION_DAYS`, `DD_PREVIEW_LINES`, `DD_MAX_PREVIEW_CHARS`.
