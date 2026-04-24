---
name: skillers-suda
description: Design, build, review, and package Codex skills or plugin bundles from a rough idea. Use when the user asks for skill creation, plugin creation, skill improvement, trigger tuning, or a multi-perspective workshop for a new Codex capability.
---

# skillers-suda for Codex

Read these first:
- `references/interview-guide.md`
- `references/component-decision.md`
- `references/writing-style-guide.md`

Read as needed:
- `references/eval-guide.md` when building or improving evals
- `references/plugin-package-guide.md` when the output should be a plugin
- `references/schemas.md` when writing structured metadata

Use this skill when the user wants to create or improve a Codex skill, package a plugin, or turn a vague workflow idea into a reusable capability.

## Codex Workflow

1. Classify the request:
   - new skill
   - plugin package
   - existing skill review
   - trigger or description improvement
   - eval design
2. If the user provided a path, inspect it first before asking questions.
3. If the idea is vague, ask one compact chat question with examples. Keep it multiple-choice style in prose.
4. When the user explicitly wants the full workshop, spawn up to four bounded sub-agents:
   - planner — identifies workflow shape and missing decisions
   - user-advocate — checks usability and trigger language
   - implementer — proposes files, scripts, and package structure
   - reviewer — finds risks, overengineering, and missing validation
5. Keep synthesis local in the main thread. Do not wait on agents before doing context gathering that can be done locally.
6. Produce a short design brief before writing files:
   - skill or plugin name
   - trigger surface
   - required files
   - scripts or references
   - validation plan
7. Create or edit files directly in the workspace.
8. Validate:
   - `python3 scripts/quick_validate.py <skill-dir>` for generated skills
   - JSON parsing for plugin manifests
   - syntax checks for generated scripts
9. Finish with changed paths, validation result, and any remaining risks.

## Output Defaults

- For a single Codex skill, generate:
  - `SKILL.md`
  - `references/` only for content too large for the main skill
  - `scripts/` only when deterministic execution beats prose
- For a Codex plugin package, generate:
  - `.codex-plugin/plugin.json`
  - `README.md`
  - `skills/<skill-name>/SKILL.md`
  - optional `assets/`
  - marketplace entry only when the user asks or the repo already has a marketplace staging file

## Guardrails

- Keep active docs Codex-native. Do not create duplicate port-suffixed documents.
- Use chat-first prompts instead of widget-specific question formats.
- Do not create legacy command-router files or legacy agent files.
- Prefer one strong skill over many tiny skills unless the triggers and ownership are genuinely different.
- If a generated skill needs external credentials or services, document setup and failure behavior explicitly.
