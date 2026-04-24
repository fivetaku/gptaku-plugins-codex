---
name: vibe-sunsang-retro
description: Convert and review Codex conversation logs for retrospective analysis. Use when the user says "바선생 회고", "대화 변환", "이번 주 대화", "retro", or asks to inspect recent Codex sessions.
---

# vibe-sunsang-retro for Codex

Use this skill to convert recent Codex sessions into readable Markdown and guide a retrospective.

## Workflow

1. Check `~/.codex/sessions/` for JSONL files.
2. Run the converter:
   `python3 scripts/convert_sessions.py --output-dir "$HOME/vibe-sunsang/conversations"`
3. Read `~/vibe-sunsang/conversations/INDEX.md`.
4. If the user named a project or date, find matching converted files.
5. If multiple plausible matches exist, ask in chat with compact numbered choices.
6. Summarize:
   - main goals
   - repeated friction
   - strong collaboration moves
   - missed verification moments
   - next experiment

## Retrospective Frame

- What did the user ask well?
- Where did the request lack context or acceptance criteria?
- How did the agent respond to uncertainty?
- Were tests, citations, screenshots, or verification used at the right moment?
- What is one behavior to practice next time?

## Output

Write concise Korean by default. If the user asks for an artifact, save it under `~/vibe-sunsang/exports/`.
