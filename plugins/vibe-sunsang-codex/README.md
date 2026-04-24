# vibe-sunsang-codex

Codex marketplace package for the `vibe-sunsang` AI collaboration mentor.

Included skills:
- `vibe-sunsang-onboard` — Initializes local config and converts recent Codex sessions.
- `vibe-sunsang-retro` — Converts and reviews recent conversation logs.
- `vibe-sunsang-knowledge` — Explains workspace types, anti-patterns, growth axes, and level systems.
- `vibe-sunsang-mentor` — Coaches request quality and collaboration habits.
- `vibe-sunsang-growth` — Produces growth reports from converted conversations.

Packaging notes:
- The packaged runtime reads `~/.codex/sessions/` and writes converted Markdown to `~/vibe-sunsang/conversations/`.
- Config and exports stay in `~/vibe-sunsang/`.
