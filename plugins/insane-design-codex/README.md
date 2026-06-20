# insane-design-codex

Codex marketplace package for the `insane-design` design-system workflow.

Included skills (Codex is skill-first — no `commands/` directory):
- `insane-design` — analysis: extract a real design system from a live URL into a 19-section `design.md` + interactive `report.ko.html`. Also exports `design.md` frontmatter to a W3C DTCG `tokens.json`.
- `insane-apply` — apply an analyzed `design.md` to an existing project while preserving content. Lv1 (token swap) / Lv2 (style rewrite) / Lv3 (full BOLD redesign), with §18 DON'T grep verification.
- `insane-build` — scaffold a new site / deck / card-news / design-system catalog from a `design.md` (or synthesize one), writing deterministic HTML+CSS into `insane-build/{session}/variations/v{N}/`.

Codex adaptations vs the Claude Code plugin:
- `AskUserQuestion` card UI does not exist; every menu/selection uses the numbered-options chat pattern from `shared/questioning-policy.md` §A.
- No async background verifier and no `verify` polling command — verification is synchronous within the same turn (grep first, playwright only when installed).
- All script/asset/reference paths use `$PLUGIN_ROOT`, not `${CLAUDE_PLUGIN_ROOT}`.
- `schema_version: 3.2` is the active `design.md` contract.

Packaging notes:
- The bundled `examples/` corpus is kept because it is part of the product value (apply/build reuse it as deterministic references).
- Canonical references, scripts, the shared contract (`skills/insane-design/shared/README.md`), and starter components live under `skills/insane-design/` and are shared by all three skills.
