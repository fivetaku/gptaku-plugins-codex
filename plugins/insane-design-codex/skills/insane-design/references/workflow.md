# insane-design-codex — Skill Router (v3.2)

This plugin mirrors the Codex CLI `insane-design` plugin as **three Codex skills**
(Codex is skill-first — there is no `command-routes/` directory):

| Skill | Role | Folds in |
|-------|------|----------|
| `insane-design` | analysis — URL → `design.md` + `report.ko.html` | `export` (design.md → DTCG `tokens.json`) |
| `insane-apply` | apply a `design.md` to an existing project (Lv1/Lv2/Lv3) | synchronous `verify` (§18 DON'T grep) |
| `insane-build` | build a new artifact from a `design.md` (or synthesize one) | synchronous `verify` (§18 DON'T grep) |

Canonical assets live under `insane-design/` and are shared by all three skills via
`$PLUGIN_ROOT/skills/insane-design/...`:

- `references/schema.v3.2.md` — frontmatter + section single source of truth
- `references/template.md` — 19-section `design.md` template (v3.2)
- `references/narrative-vocabulary.md` / `report-prompt.md` / `report.css` / `pitfalls.md` / `data-collection.md` / `methodology.md`
- `scripts/` — deterministic extractors + `validate.py` + `export_dtcg.py`
- `shared/README.md` — shared contract (Identity · Contract · Verifier · AI Slop · Starter Components)
- `shared/starter-components/` — per-medium HTML presets
- `examples/` — canonical bundled corpus (read-only)

Apply-specific references live under `$PLUGIN_ROOT/skills/insane-apply/references/`
(`apply-workflow.md`, `redesign-aesthetics.md`).

## Codex adaptations vs Codex CLI

- `question prompt` card UI does not exist → every menu/selection becomes the
  `shared/questioning-policy.md §A` numbered-options-in-chat pattern.
- No async `AgentTask(background execution flag)` verifier and no `verify` polling command →
  all verification is **synchronous** within the same turn (grep first, playwright only if installed).
- All script/asset/reference paths use `$PLUGIN_ROOT`, not `${CODEX_PLUGIN_ROOT}`.
- `schema_version: 3.2` is the active contract (3.1 deprecated).
