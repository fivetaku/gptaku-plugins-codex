---
name: vibe-sunsang-onboard
description: Initialize vibe-sunsang for Codex by creating local config, choosing a workspace type, and converting recent Codex sessions. Use when the user says "바선생 시작", "vibe-sunsang setup", "온보딩", or wants to start tracking AI collaboration growth.
---

# vibe-sunsang-onboard for Codex

Use this skill to prepare local growth-analysis files.

## Paths

- Config: `~/vibe-sunsang/config/`
- Conversations: `~/vibe-sunsang/conversations/`
- Exports: `~/vibe-sunsang/exports/`
- Source sessions: `~/.codex/sessions/`

## Workflow

1. Create the local directories if missing.
2. Check whether `~/.codex/sessions/` exists and contains JSONL files.
3. If no sessions exist, explain that there is not enough conversation history yet.
4. Ask for workspace type in chat only if `workspace_types.json` is missing:
   - `1. Builder` — coding and app/service building
   - `2. Explorer` — research, learning, and Q&A
   - `3. Designer` — planning, ideation, and content design
   - `4. Operator` — automation, operations, and data processing
5. Write `~/vibe-sunsang/config/workspace_types.json`.
6. Convert recent sessions:
   `python3 ../vibe-sunsang-retro/scripts/convert_sessions.py --output-dir "$HOME/vibe-sunsang/conversations"`
7. Summarize the converted session count and next recommended action.

## Guardrails

- Do not delete old folders automatically.
- Do not claim that analysis is complete during onboarding; conversion only prepares the data.
- Use chat-first choices rather than widget-specific prompts.
