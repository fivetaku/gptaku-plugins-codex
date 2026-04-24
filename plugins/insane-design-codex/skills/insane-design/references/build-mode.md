# Build Mode

Use build mode when the user wants a new landing page, deck, card, or catalog generated from a `design.md` reference.

## Inputs

- explicit `design.md` path
- bundled example slug from `examples/<slug>/design.md`
- explicit URL only if the user also wants analysis first

## Rules

- Default output root: `insane-build/<session>/variations/v1/`
- Create only `v1` unless the user explicitly asks for multiple variations
- Pick starter components based on the reference medium
- Keep the build tied to the chosen `design.md` so later tweaks stay deterministic
- Validate synchronously with `rg` and basic HTML sanity checks before reporting completion

## Shared Contract

Read `../shared/README.md` before build-mode work. The `design.md` frontmatter and `§18 DON'T` contract must stay compatible with analysis output.
