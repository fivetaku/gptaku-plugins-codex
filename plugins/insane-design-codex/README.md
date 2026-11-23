# insane-design-codex

Codex marketplace package for the `insane-design` design-system workflow (mirrors upstream v0.5.5).

Included skills (Codex is skill-first — the upstream slash-command routers are folded into the skills):
- `insane-design` — smart router (URL → analysis / slug → apply / `build` → build / `export` → DTCG) plus the analysis engine: extract a real design system from a live URL into a 19-section `design.md` (schema 3.2) + interactive `report.ko.html`. Also exports `design.md` frontmatter to a W3C DTCG `tokens.json`.
- `insane-apply` — apply an analyzed `design.md` to an existing project while preserving content. Lv1 (token swap) / Lv2 (style rewrite) / Lv3 (full BOLD redesign), with §18 DON'T grep verification (6-call quota) and an opt-in deeper verifier.
- `insane-build` — scaffold a new site / deck / card-news / design-system catalog from a `design.md` (or synthesize one), writing deterministic HTML+CSS into `insane-build/{session}/variations/v{N}/`.

Codex adaptations vs the upstream plugin:
- Menus/selections use the Codex question tool (`request_user_input_async`, or `request_user_input` in Plan mode) per `shared/questioning-policy.md` §A (recommended option first); only when neither tool exists it falls back to the numbered-options chat pattern ("describe in a sentence" last).
- The upstream opt-in async verifier and its polling command become a Codex runtime `spawn_agent` background sub-agent (agent_type `reviewer`); the main thread reports immediately and the result is collected only when the user asks ("검증 결과 보여줘"). If spawning is unavailable, verification runs inline in the same turn.
- All script/asset/reference paths use `$PLUGIN_ROOT`.
- `schema_version: 3.2` is the active `design.md` contract.
- First-run setup / star prompt / update-notifier hooks are not ported (no plugin hook support in Codex).

Packaging notes:
- The bundled `examples/` corpus (100+ sites) is kept because it is part of the product value (apply/build reuse it as deterministic references).
- Canonical references, scripts, the shared contract (`skills/insane-design/shared/README.md`), and starter components live under `skills/insane-design/` and are shared by all three skills.

Synced from upstream 0.5.4/0.5.5: `brand_candidates.py` now consumes `var_resolver.py`'s real `samples` output (var()-chain brand recovery works), the stripe-only assert in `typo_extractor.py` is gone, the Tier-4 curl_cffi fetch passes its output path via argv, and the example corpus is refreshed.
