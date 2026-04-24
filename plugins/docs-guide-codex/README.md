# docs-guide-codex

Codex marketplace package for the `docs-guide` skill.

Included skills:
- `docs-guide` — Fetches and explains official documentation using an `llms.txt`-first strategy and official-source fallbacks.

Packaging notes:
- The package keeps the known-site index and fallback strategy references because they are part of the retrieval logic.
