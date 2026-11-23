# vibe-sunsang-codex

Codex marketplace package for the `vibe-sunsang` AI collaboration mentor (v2.3.0, aligned with the original plugin).

Included skills:
- `vibe-sunsang-onboard` — Self-heals the local workspace, links Codex session projects, classifies workspace types, writes `AGENTS.md`, and runs the first conversion.
- `vibe-sunsang-retro` — Converts Codex session logs into Markdown (per-session metrics in frontmatter, activity-sorted `INDEX.md`) and guides a retrospective.
- `vibe-sunsang-knowledge` — Explains workspace types, anti-patterns, the six growth axes, and the level system.
- `vibe-sunsang-mentor` — Coaches request quality and collaboration habits (4 modes). Also the entry point when the user just says "바선생".
- `vibe-sunsang-growth` — Produces growth reports that open with one level headline and up to three next moves; six-axis scores, weights, and gate arithmetic stay in the report file and are spoken only on request.

Scripts (`scripts/`):
- `ensure_workspace.py` — guarantees the v2 layout under `~/vibe-sunsang/` and migrates v1 numbered folders non-destructively. Every skill runs it first, so there is no "set up first" dead end.
- `convert_sessions.py` — Codex rollout JSONL → Markdown. Groups sessions by working directory (`session_meta.cwd`), emits the same frontmatter contract as the original (tokens, tools, `user_turn_count`, `tool_error_count`, `has_orchestration`, `thinking_turn_ratio`, ...), incremental by default, `--project <display name>` resolution, `--list-projects` for onboarding.
- `analysis_scope.py` — incremental watermark: `--new` lists sessions active since the last review (by frontmatter `end`), `--mark` advances the watermark after a report.

Heavy analysis offload:
- `vibe-sunsang-growth` offloads the v2 analysis to a runtime-spawned Codex sub-agent. Codex plugins don't package an agent-roster file, so the original `growth-analyst` agent instructions live in `skills/vibe-sunsang-growth/references/growth-analyst.md` and the spawn prompt tells the sub-agent to read and follow that file. When spawning isn't available the skill follows the same file inline.

Packaging notes:
- Session source: `~/.codex/sessions/` (or `$CODEX_HOME/sessions`; override with `--sessions-dir`). Converted Markdown goes to `~/vibe-sunsang/conversations/`, config and exports stay in `~/vibe-sunsang/`.
- The workspace instruction file is `AGENTS.md` (what Codex reads), generated from `references/AGENTS-MD-TEMPLATE.md`.
- Choice questions use the Codex question tool (`request_user_input_async`, or `request_user_input` in Plan mode) per `shared/questioning-policy.md` §A, and fall back to numbered options in chat only when neither tool is available. Open coaching questions stay plain chat.
- Not ported (platform-level, per `docs/RE-PORTING-PLAN.md` §2): first-run setup hook, GitHub-star opt-in, update notifier.
