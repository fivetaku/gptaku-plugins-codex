# insane-research-codex

Codex marketplace package for the `insane-research` product unit — multi-phase, citation-heavy deep research with durable session state.

Included skills:
- `insane-research-main` — Runs structured, citation-heavy research sessions through a 7-phase pipeline (scoping → retrieval planning → iterative querying → source triangulation → synthesis → QA → packaging) with durable `RESEARCH/` state, a claim-ledger / abstention contract, and source-quality (A-E) tracking.
- `insane-research-query` — Turns a vague research idea into a schema-backed research brief and machine-readable query before full research starts.

Packaging notes:
- The main research workflow and query builder stay together because the original product shipped them as one research suite.
- Active docs are Codex-native and chat-first: there is no `question prompt` widget dependency. Interactive scoping uses the numbered-options chat block from `shared/questioning-policy.md §A`.
