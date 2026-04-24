# kkirikkiri Presets for Codex

Use this file instead of the legacy preset catalog when running inside Codex.

## Preset table

- `research` — For broad topic research, competitor scans, source gathering, and synthesis.
  Use when the user asks to research, compare, investigate, or compile findings.
  Recommended team: lead + 2 explorers.
- `development` — For delegated implementation with clear ownership boundaries.
  Use only when the user explicitly wants delegation or parallel build help.
  Recommended team: lead + 2 workers, optionally 1 verifier.
- `analysis` — For codebase exploration, technical review, audits, and architecture mapping.
  Use when the user wants to understand an existing system rather than change it directly.
  Recommended team: lead + 2 explorers.
- `content` — For writing-heavy tasks such as docs, reports, summaries, or polished deliverables.
  Recommended team: lead + 1 writer + 1 reviewer.
- `product` — For PRD, roadmap, strategy, prioritization, or positioning work.
  Recommended team: lead + 1 researcher + 1 planner.

## Classification rules

- If the user explicitly asks for delegation, a team, multiple agents, parallel help, or to "split this up", use the closest preset above.
- If the request is mostly coding and the user did not ask for delegation, do not use `kkirikkiri`.
- If the request mixes research and implementation, default to `development` when code changes are the end goal, otherwise `research`.

## Team sizing

- Default to 2-4 total agents including the lead.
- Add a verifier only when there is a concrete review or test gate to run.
- Avoid larger teams unless the work partitions cleanly.

## Environment scan interpretation

Read `scripts/scan_environment.py` output like this:

- `codex` present — safe to assume Codex-native execution environment
- `gh` present — PR, issue, and repo workflows are available
- `gemini` present — optional external comparison path, not required
- `installed_skills` — can suggest nearby skills, but do not overfit the team shape to them

Ignore any legacy external-agent file assumptions from older materials.
