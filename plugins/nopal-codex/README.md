# nopal-codex

Codex marketplace package for the `nopal` Google Workspace product unit.

Included skills:
- `nopal` — Orchestrates Gmail, Calendar, Drive, Docs, Sheets, Slides, Chat, Tasks, and Meet requests through `gws`.
- `nopal-setup` — Provides installation and authentication guidance when `gws` is missing or unauthenticated.

Packaging notes:
- The packaged runtime uses `gws` as the only Google Workspace execution surface.
- Read-only checks can run directly; write actions require a compact chat summary before execution.
