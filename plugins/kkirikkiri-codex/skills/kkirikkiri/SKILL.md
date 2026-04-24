---
name: kkirikkiri
description: Assemble and run a Codex-native agent team from a plain-language request. Use when the user explicitly wants delegation, a research/development/review team, or parallel sub-agent work. Preserves the original kkirikkiri preset, interview, and shared-memory model, but adapts it to Codex with `spawn_agent`, shared files in `.kkirikkiri/`, and concise follow-up questions instead of widget-specific flows.
---

# kkirikkiri for Codex

Read these first:
- `references/presets.md`
- `references/interview-guide.md`
- `references/shared-memory.md`
- `references/team-prompts.md`

Read only when needed:
- `references/pm-frameworks.md` for product, strategy, roadmap, or PRD-heavy requests
- `references/metaphor-guide.md` when you need to translate technical choices into plain Korean
- `references/validation-guide.md` when deciding whether to rebuild or swap team members

Use this skill only when the user is explicitly asking for delegation, parallel help, or an agent-team style workflow. If the user is only asking for a normal answer or a solo code change, do not use this skill.

## Codex Workflow

1. Classify the request with `references/presets.md`.
2. Scan the current environment with:
   `python3 scripts/scan_environment.py --root "$PWD"`
3. Ask at most one short clarification if a missing answer would materially change the team shape. Otherwise proceed with reasonable assumptions and record them.
4. Initialize shared memory with:
   `python3 scripts/init_shared_memory.py --root "$PWD" --task "<task>" --preset "<preset>"`
5. Keep the lead role local. Use `spawn_agent` only for bounded sidecar work or disjoint file ownership.
6. Every spawned agent must receive:
   - a concrete responsibility or file scope
   - a reminder that they are not alone in the codebase
   - instructions to read `.kkirikkiri/TEAM_PLAN.md`, `.kkirikkiri/TEAM_PROGRESS.md`, and `.kkirikkiri/TEAM_FINDINGS.md` first
7. While agents run, do the critical-path work locally and update the shared memory files when the plan or findings change.
8. If one member underperforms, swap only that role first. Reserve full-team rebuilds for genuinely broken first attempts.
9. Finish by writing `.kkirikkiri/TEAM_REPORT.md` with:
   - final output
   - assumptions made
   - what each teammate contributed
   - remaining risks or open questions

## Guardrails

- Prefer 2-4 agents. Larger teams only make sense when work partitions cleanly.
- Do not spawn agents for the immediate blocking task if you can do it locally faster.
- Use the active preset and interview references. Keep the interaction chat-first, concise, and direct.
- Keep `.kkirikkiri/` as the system of record so replacement agents can catch up quickly.
