---
name: deep-research-query
description: Structured research-query builder for turning a vague topic into a research brief and machine-readable query before full deep research starts. Use when the user wants help framing a research request.
---

# deep-research-query for Codex

Read these first:
- `references/query_schema.json`

Use this skill when the user wants to shape a vague idea into a research-ready brief before running full deep research.

## Codex Workflow

1. Identify the topic or ask one short chat-first question to pin it down.
2. Clarify only the highest-impact constraints:
   - research type
   - geography or scope
   - source quality
   - intended output
3. Produce:
   - a structured JSON query
   - a human-readable research brief
   - a short execution checklist
4. If the user wants to continue immediately, hand off to `deep-research`.

## Guardrails

- Keep the questions compact and multiple-choice style where possible.
- Use concrete defaults instead of leaving blanks.
- Treat the query schema as the contract for structured output.
- Ask in chat rather than relying on widget-style prompts.
