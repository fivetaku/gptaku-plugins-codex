# goaljaby-codex

Codex marketplace package for the `goaljaby` skill — a PRD-to-`/goal` bridge.

Included skills:
- `goaljaby` — Turns a PRD folder into five Korean review documents (VALIDATION/RECOVERY/PLAN/PROGRESS equivalents) plus a `PLANS.md` ExecPlan, then hands off a ready-to-copy Codex `/goal` command after human approval.

## What it does

1. Read a PRD folder (manual or from `show-me-the-prd`).
2. Generate six Korean-first documents: `VALIDATION.md`, `RECOVERY.md`, `PLAN.md`, `PROGRESS.md`, `goal-command.md`, and `PLANS.md` (the Codex ExecPlan with **Progress / Validation / Decision-Log** sections).
3. Enforce a 4,000-character compact on the `/goal` body (file-pointer pattern — the objective references `./PLANS.md`).
4. Show a Korean review summary in chat (no extra file) and prepend a 4-line summary to `PROGRESS.md` and the `PLANS.md` Progress section.
5. After a mandatory approval gate, present a ready-to-copy `/goal` command.

## Codex vs Claude Code

The Claude Code edition emits `/goal` on the assistant's last line to auto-start the goal loop. **Codex cannot auto-emit a slash command** — so this edition ends by presenting a ready-to-copy command instead:

```
/goal Execute ./PLANS.md to completion; keep the Progress section current; stop when <verifiable done condition>
```

Codex has a native `/goal` (the `goals` feature is stable in codex 0.139) plus `/plan` mode and the `PLANS.md`/ExecPlan convention, which this package targets directly.

## Packaging notes

- Chat-first interview model (`shared/questioning-policy.md §A`) instead of any widget-based question flow.
- No hooks. The Claude Code edition's `setup/setup.sh` is intentionally not ported (Codex plugins do not support hooks); the skill needs no bootstrap.
- All paths use `$PLUGIN_ROOT`.

## License

MIT
