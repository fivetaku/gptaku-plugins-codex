# vibe-sunsang-codex

Codex marketplace package for the `vibe-sunsang` AI collaboration mentor.

Included skills:
- `vibe-sunsang-onboard` — Initializes local config and converts recent Codex sessions.
- `vibe-sunsang-retro` — Converts and reviews recent conversation logs.
- `vibe-sunsang-knowledge` — Explains workspace types, anti-patterns, growth axes, and level systems.
- `vibe-sunsang-mentor` — Coaches request quality and collaboration habits.
- `vibe-sunsang-growth` — Produces growth reports from converted conversations.

Heavy analysis offload:
- `vibe-sunsang-growth` offloads the v2 growth-report analysis (6 axes × 7 levels, 0.5 increments) to a runtime-spawned Codex sub-agent with inline instructions — Codex plugins don't package an agent-roster file — and falls back to inline analysis when spawning isn't available.

Packaging notes:
- The packaged runtime reads `~/.codex/sessions/` and writes converted Markdown to `~/vibe-sunsang/conversations/`.
- Config and exports stay in `~/vibe-sunsang/`.
- Codex CLI has no `AskUserQuestion` card UI; all decisions use the numbered-option chat pattern from `shared/questioning-policy.md` §A.
