---
name: vibe-sunsang-mentor
description: Coach AI collaboration quality from recent Codex conversations using workspace type, prompt quality, anti-patterns, and the six growth axes. Use when the user says "멘토링해줘", "코칭해줘", "요청 코칭", "뭘 잘못하고 있는지", or "improve my AI collaboration".
---

# vibe-sunsang-mentor for Codex

Use this skill to coach the user's AI collaboration patterns.

## Inputs

- Converted conversations: `~/vibe-sunsang/conversations/`
- Workspace config: `~/vibe-sunsang/config/workspace_types.json`
- Knowledge references: `../vibe-sunsang-knowledge/references/`

## Modes

- `request` — improve the user's prompt/request quality
- `antipattern` — diagnose repeated bad habits
- `concept` — teach one framework concept
- `overall` — broad coaching across the six axes

## Workflow

1. Ensure conversations exist. If not, run the converter from `vibe-sunsang-retro`.
2. Determine workspace type from config or ask in chat with the four types.
3. Select the mode from the user's wording. Default to `overall`.
4. Load only the relevant knowledge files:
   - request mode: `common/prompt-quality.md`
   - antipattern mode: `{type}/antipatterns.md`
   - concept mode: `{type}/concepts.md`
   - overall mode: `{type}/growth-metrics.md` and `common/mentoring-checklist.md`
5. Inspect the relevant converted sessions.
6. Produce coaching with:
   - observed pattern
   - concrete example from the conversation
   - impact on one or more growth axes
   - better request or behavior example
   - one small practice for the next session

## Guardrails

- Be candid but supportive.
- Do not invent examples that are not visible in the converted logs.
- If there is too little data, say so and give a starter exercise instead.
