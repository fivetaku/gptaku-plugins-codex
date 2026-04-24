---
name: vibe-sunsang-growth
description: Generate an AI collaboration growth report from converted Codex conversations using the six-axis level system. Use when the user says "성장 리포트", "바선생 분석", "레벨 평가", "growth report", or asks how their AI collaboration is improving.
---

# vibe-sunsang-growth for Codex

Use this skill for structured growth reports.

## Inputs

- Converted conversations: `~/vibe-sunsang/conversations/`
- Workspace config: `~/vibe-sunsang/config/workspace_types.json`
- Knowledge references: `../vibe-sunsang-knowledge/references/`

## Workflow

1. Ensure converted conversations exist. If not, run `../vibe-sunsang-retro/scripts/convert_sessions.py`.
2. Determine report scope:
   - recent 5 sessions
   - this week
   - named project
   - all converted sessions
3. Determine workspace type from config or ask in chat.
4. Load `{type}/growth-metrics.md` and `common/mentoring-checklist.md`.
5. Score the six axes:
   - `DECOMP`
   - `VERIFY`
   - `ORCH`
   - `FAIL`
   - `CTX`
   - `META`
6. Assign level using the type-specific growth metrics.
7. Save a Markdown report under `~/vibe-sunsang/exports/` when the user asks for a file.

## Report Shape

- Current level and plain-language meaning
- Six-axis score summary
- strongest behavior pattern
- weakest behavior pattern
- evidence from sessions
- next three practice actions

## Guardrails

- Treat scores as coaching signals, not objective identity labels.
- Cite visible session evidence.
- Do not overfit from fewer than three sessions; mark the report as preliminary.
