---
name: show-me-the-prd
description: Turn a rough product idea into a PRD bundle with `PRD/01_PRD.md`, `02_DATA_MODEL.md`, `03_PHASES.md`, `04_PROJECT_SPEC.md`, and `README.md`. Use when the user wants a PRD, planning docs, or an AI-ready build plan from a vague idea or incomplete notes.
---

# Show Me The PRD for Codex

Read these first:
- `references/interview-guide.md`
- `references/research-strategy.md`
- `references/document-templates.md`

Use this skill when the user wants a product plan, PRD, app spec, or a structured build handoff. If the user already provided notes or a partial spec, patch the missing parts instead of starting over.

## Codex Workflow

1. Audit the idea for:
   - problem to solve
   - target users
   - platform
   - MVP scope
   - constraints
2. Ask at most one targeted follow-up if the biggest unknown would materially change the plan.
3. Use live research before recommending features, stacks, vendors, or pricing. Prefer current primary sources when possible.
4. Keep explanations plain-language and production-oriented.
5. Write the preserved five-file bundle under `PRD/`:
   - `01_PRD.md`
   - `02_DATA_MODEL.md`
   - `03_PHASES.md`
   - `04_PROJECT_SPEC.md`
   - `README.md`
6. Put unresolved items into `[NEEDS CLARIFICATION]` instead of blocking the whole draft.
7. End with a short readiness score and next-step handoff.

## Interaction Rules

- Ask in chat with compact multiple-choice style prompts when you truly need a decision.
- Format decision prompts like:
  `1. Recommended option - what it is, why it helps, tradeoff`
  `2. Alternative option - what it is, why it helps, tradeoff`
- When structure matters, show a short fenced preview before the question so the user can react to something concrete.
- Avoid markdown tables in chat, but keep them in the generated docs where the templates expect them.
- If the user supplied an existing spec, preserve its intent and only normalize the structure into the bundled templates.
