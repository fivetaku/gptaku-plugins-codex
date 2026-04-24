# insane-design Workflow for Codex

Use this document instead of the older AI agent-oriented workflow notes.

## Analysis mode

1. Validate the target URL and derive a stable slug.
2. Create `insane-design/<slug>/`.
3. Capture raw evidence:
   - HTML
   - CSS
   - screenshots
   - extracted metadata and tokens
4. Run helper scripts when useful:
   - `scripts/brand_candidates.py`
   - `scripts/var_resolver.py`
   - `scripts/typo_extractor.py`
   - `scripts/alias_layer.py`
5. Synthesize `design.md` using the Codex template.
6. Render `report.ko.html` from the canonical report prompt and CSS.

## Apply mode

- Read `design.md`.
- Preserve the `§18 DON'T` contract.
- Use the design brief to steer edits in an existing project without copying blindly from examples.

## Build mode

- Read `design.md`.
- Pick starter components that match the `medium` field.
- Generate new artifacts that follow the brief rather than cloning the source site.

## Clarification rule

- Ask at most one clarification if the URL or output root is ambiguous.
- Otherwise proceed and record assumptions in the output notes.

## Verification rule

- Prefer synchronous local verification.
- Start with grep or lint checks.
- Only escalate to browser-driven checks when there is a concrete reason.
