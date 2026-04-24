---
name: insane-design
description: Extract a real design system from a live URL into `design.md` and `report.ko.html`, or reuse the bundled multi-site design corpus as a deterministic design brief. Use when the user wants real CSS tokens, a reusable design reference, or a design pack that can feed apply/build flows.
---

# Insane Design for Codex

Read these first:
- `shared/README.md`
- `references/workflow.md`
- `references/pitfalls.md`
- `references/apply-mode.md`
- `references/build-mode.md`

Load before writing output:
- `references/template.md` for `design.md`
- `references/report-prompt.md` and `references/report.css` for `report.ko.html`

Use `examples/` as the canonical bundled corpus. Do not duplicate or prefer any published mirror.

## Modes

- `analysis` — extract a fresh `design.md` and `report.ko.html` from a live URL
- `apply` — apply an existing `design.md` or bundled example to an existing project
- `build` — generate a new artifact from a `design.md` plus starter components

`apply` and `build` are internal modes of `insane-design`, not separate top-level skills.

## Codex Workflow

1. Validate the URL, derive the slug, and create `insane-design/<slug>/`.
2. Collect HTML, CSS, and screenshots with shell tooling plus the deterministic helper scripts under `scripts/`.
3. Escalate fetch methods according to `references/data-collection.md`; do not hallucinate tokens you can extract.
4. Use the parsing helpers when possible:
   - `scripts/brand_candidates.py`
   - `scripts/var_resolver.py`
   - `scripts/typo_extractor.py`
   - `scripts/alias_layer.py`
5. Write `design.md` with the exact v3.1 frontmatter and `§18 DON'T` contract from `shared/README.md`.
6. Write `report.ko.html` with the canonical report prompt and CSS.
7. Preserve screenshots, CSS captures, and `phase1` artifacts when they support later apply/build work.

## Codex Adaptation

- There is no command-router or widget dependency here. Ask at most one concise clarification if the URL or output root is ambiguous.
- There is no async verifier port. Keep analysis deterministic and synchronous.
- The `apply` and `build` modes depend on the frontmatter and `§18 DON'T` contract staying stable.
