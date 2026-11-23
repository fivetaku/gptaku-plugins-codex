# pumasi-codex

Codex marketplace package for the `pumasi` family. Version 1.17.0 (tracks the upstream pumasi plugin 1.17.0).

Included skills:
- `pumasi` — Host-controlled parallel coding orchestration for multi-module greenfield work. The current Codex session stays the host (plans, signatures, gates, verification, integration); implementation is delegated to N parallel CLI workers — Codex workers by default, or `grok`, `cursor-agent` (`--force` required), `gjc`, `agy`, or the `claude` CLI, selectable per task.
- `pumasi-image` — Image-generation companion for posters, thumbnails, logos and other visual deliverables. Uses Codex's native image generation/editing tool (gpt-image-2) by default; the bundled scripts add an optional Grok `image_gen` backend (9:16 / 16:9 / 1:1 only), style-anchor references, proxy bypass and failure-reason surfacing. Never calls image APIs with a raw API key.

Structure:
- `skills/pumasi/` — Parallel build orchestration skill (`scripts/init_workspace.py`, `scripts/codex-output-schema.json`, `references/`).
- `skills/pumasi-image/` — Image-generation skill (`scripts/imagen*.sh`, `scripts/extract_image.py`, `references/`).
- `shared/questioning-policy.md` — Question policy: uses the Codex question tool (`request_user_input_async` / `request_user_input`), with numbered-choice blocks as a fallback when neither tool exists.
- `.codex-plugin/plugin.json` — Codex plugin manifest

Packaging notes:
- The plugin keeps `pumasi` and `pumasi-image` together as one product unit.
- Upstream hooks, first-run setup and update notifier are not ported (no plugin hook support in Codex); the upstream slash-command entry files are merged into the SKILL.md files.
