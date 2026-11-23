# skillers-suda-codex

Codex marketplace package for the `skillers-suda` workshop (v1.4.6, tracks the upstream skillers-suda 1.4.5 release).

Included skills:
- `skillers-suda` — Spawns four expert sub-agents in parallel to debate an idea, interviews the user with the Codex question tool, then designs, builds, verifies, evals, tunes the description of, and packages a working Codex skill (or skill + embedded sub-agent prompts, or a plugin bundle).

Packaging notes:
- The four experts are real Codex runtime sub-agents spawned in one turn; the skill falls back to a main-thread synthesis only when delegation is unavailable.
- Choice questions use the Codex question tool (`request_user_input_async`, or `request_user_input` in Plan mode) and fall back to numbered chat options when neither tool is available (see `shared/questioning-policy.md` §A).
- The upstream automated eval runner and description optimizer (`run_eval.py`, `run_loop.py`, `improve_description.py`, `generate_report.py`) are not shipped: they drive a different agent CLI as a subprocess and depend on an external SDK. Phases F and H replace them with sub-agent runs; the grader, comparator, analyzer prompts, benchmark aggregator, review viewer, packager, and validators are shipped unchanged.
- `scripts/quick_validate.py` needs PyYAML (`pip install pyyaml`); `verify-skill.py` and `scripts/validate-skill.js` at the plugin root have no third-party dependencies.
