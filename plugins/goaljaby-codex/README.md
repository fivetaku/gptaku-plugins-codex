# goaljaby-codex

Codex marketplace package for the `goaljaby` skill — a PRD-to-`/goal` bridge. Current version: **0.8.1**.

Included skills:
- `goaljaby` — Turns a PRD folder into five review documents in the user's language (VALIDATION/RECOVERY/PLAN/PROGRESS/goal-command) plus a `PLANS.md` ExecPlan, then starts the native Codex goal after human approval.

## What it does

1. Read a PRD folder (manual or from `show-me-the-prd`). Detects an assumption ledger and design references (`references/` + `sources.json`) if the PRD carries them.
2. Generate six documents in `output_lang` (the language of the user's request — auto-detected, ko/en first-class with deterministic heading validation, never Korean by default): `VALIDATION.md`, `RECOVERY.md`, `PLAN.md`, `PROGRESS.md`, `goal-command.md`, and `PLANS.md` (the Codex ExecPlan with **Progress / Validation / Decision-Log** sections).
3. Enforce a 4,000-character compact on the `/goal` body (file-pointer pattern — the objective references `./PLANS.md`) with Korean+English OR protected-clause regex enforcement.
4. Show a review summary in chat (no extra file) and prepend a 4-line summary to `PROGRESS.md` and the `PLANS.md` Progress section.
5. After a mandatory approval gate (Codex question tool, numbered-choice chat block as fallback), start the approved objective with `create_goal`.

**Inherited context (0.6.0+ / 0.6.2+)**: if the PRD folder carries `references/` + `sources.json` from `show-me-the-prd` v0.10+, the style keywords and kept images are inherited into PLAN.md/VALIDATION.md (with a copyright guard). If a kkirikkiri plugin is installed in the Codex plugin cache, RECOVERY.md also gets the multi-agent gate rule (boundary blocks for teammates, read-only reviewers, `wf-lint` when the installed kkirikkiri ships it) — silently skipped when kkirikkiri is absent. File names, command identifiers, and shell commands stay as-is.

## Codex vs the original edition

The original edition runs the approved command through its turn-complete hook. Codex passes the reviewed objective to `create_goal` in the current session and begins the first unfinished task. If the tool is unavailable, the saved command remains available for manual execution.

## Packaging notes

- Choice questions use the Codex question tool (`request_user_input_async`; `request_user_input` in Plan mode) per `shared/questioning-policy.md §A`, and fall back to numbered options in chat when neither tool is available.
- No hooks. The original edition's `setup/setup.sh` (first-run prompt, update check) is intentionally not ported; the skill needs no bootstrap.
- Bundled policy excerpt at `skills/goaljaby/references/policy-excerpt.md` mirrors `shared/language-policy.md` and `shared/questioning-policy.md`.
- All paths use `$PLUGIN_ROOT`.

## License

MIT
