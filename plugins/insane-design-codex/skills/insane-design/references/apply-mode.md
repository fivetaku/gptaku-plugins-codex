# Apply Mode

Use apply mode when the user wants an existing project restyled with a saved `design.md` or a bundled example slug.

## Inputs

- explicit `design.md` path
- bundled example slug from `examples/<slug>/design.md`
- project-local `insane-design/<slug>/design.md`

## Rules

- Preserve text, links, and user content unless the request explicitly changes them.
- Redesign decisively instead of presenting neutral alternatives.
- Validate synchronously against the `§18 DON'T` contract:
  - at least 2 color checks
  - at least 2 structure checks
  - at least 2 typography checks
- Use `shared/starter-components/` when token swaps are not enough and sections need structural rebuilds.

## Shared Contract

Read `../shared/README.md` before large apply-mode edits. The `design.md` frontmatter and `§18 DON'T` contract are the integration surface between analysis, apply, and build.
