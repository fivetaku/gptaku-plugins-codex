# insane-research-codex

Codex marketplace package for the `insane-research` product unit — multi-phase, citation-heavy deep research with durable session state.

Included skills:
- `insane-research-main` — Runs structured, citation-heavy research sessions through a 7-phase pipeline (scoping → retrieval planning → iterative querying → source triangulation → synthesis → QA → packaging) with durable `RESEARCH/` state, a claim-ledger / abstention contract, and source-quality (A-E) tracking. Verification is a code gate, not a suggestion: `snapshot_sources.py` (verbatim source text and SHA-256) → `validate_ledger.py` (quote matching, numeric value presence, claim status, org-level independence, structured counter-search, execution proof) → `verify_report.py` (report body cites verified claims only) → `eval_report.py` (leak / citation / orphan / coverage metrics). Phase 3 can fan out research agents via runtime `spawn_agent` with `merge_agent_returns.py` doing the deterministic merge, and delegates blocked URLs to the insane-search engine when that plugin is installed.
- `insane-research-query` — Turns a vague research idea into a schema-backed research brief and machine-readable query before full research starts.

Packaging notes:
- The main research workflow and query builder stay together because the original product shipped them as one research suite.
- Active docs are Codex-native and chat-first: there is no multiple-choice widget dependency. Interactive scoping uses the numbered-options chat block from `shared/questioning-policy.md §A`.
- Based on upstream insane-research v2.9.0, with the committed v2.10.0 evidence quote gate (`bd4f7ac`, `8171295`) ported in Codex v2.9.1. New sessions use `ledger_schema: 2`; older sessions retain their existing validation rules. Snapshot collection uses the sibling or installed `insane-search-codex` engine (explicit `--engine-dir` and `INSANE_SEARCH_ENGINE_DIR` take priority). Not ported: the upstream first-run setup hook, update notifier, and the strict-mode hand-off to a separate deep-research workflow harness (strict mode re-verifies in the main thread instead).

Regression verification (from the marketplace root):
```bash
python3 -m pytest plugins/insane-research-codex/tests -q
```
