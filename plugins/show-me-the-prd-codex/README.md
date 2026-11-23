# show-me-the-prd-codex

Codex marketplace package for the `show-me-the-prd` skill (v0.10.1, aligned with the upstream show-me-the-prd 0.10.1).

Included skills:
- `show-me-the-prd` — Draft-first PRD generator. One open probe for the real problem, one multiple-choice direction round, an immediate five-file PRD bundle (PRD, data model, phases, project spec, README) with an assumption ledger, one confirmation round, then delivery with the remaining assumptions listed.

What's in this version:
- Draft-first interview (0.9.0): question budget = 1 open probe (+1 re-probe) + 2 multiple-choice rounds of up to 4 items; data model and phase split are designed into the draft and confirmed as concrete previews; unconfirmed points become `> ⚠️ 가정:` blocks plus a `## 가정 원장` section in `PRD/01_PRD.md`.
- UI design-reference collection (0.10.0): when the product has a user-facing screen, a `{domain}+{style}` query pulls 6-8 reference images, vision-screens them down to 3-5, and stores them in `PRD/references/` with `sources.json` (local reference only, never republished). Backend/CLI/library plans skip this step entirely. See `skills/show-me-the-prd/references/design-reference-guide.md`.

Packaging notes:
- Choice questions use the Codex question tool (`request_user_input_async`, or `request_user_input` in Plan mode) and fall back to chat numbered choices only when neither tool is available (`shared/questioning-policy.md §A`).
- Upstream first-run setup and update-notifier hooks are not ported (Codex plugins do not support declarative hooks).
