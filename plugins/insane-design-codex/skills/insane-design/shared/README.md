# insane-design Shared Contract for Codex

This file defines the Codex-native contract that `analysis`, `apply`, and `build` flows depend on.

## Output paths

- `design.md` -> `insane-design/<slug>/design.md`
- `report.ko.html` -> `insane-design/<slug>/report.ko.html`
- screenshots -> `insane-design/<slug>/screenshots/`
- captured CSS and phase artifacts -> keep them under the same slug directory

All paths are project-root relative.

## Core contract

- `design.md` is the canonical design brief.
- `report.ko.html` is the human-facing report artifact.
- `§18 DON'T` is a hard contract that downstream build or apply flows must respect.
- `examples/` is the canonical bundled corpus for deterministic reuse.

## Verification policy

- Default verification is synchronous and local.
- Use grep-based checks first for `§18 DON'T` patterns.
- If richer browser verification is needed, run it explicitly as a normal Codex step, not as a background job contract.

## Starter components

Starter components live under `shared/starter-components/`.

- `web/` — landing and marketing page fragments
- `slide/` — presentation-oriented fragments
- `design-system/` — token and catalog views
- `card-news/` — card-news and social card formats
- `motion/` — motion-oriented stubs

Choose the starter set that matches the `medium` field in `design.md`.

## AI slop policy

The anti-slop rules apply only where `design.md` does not explicitly constrain the design.

- If `design.md` explicitly names a font, color, grid, or layout rule, follow it.
- Otherwise avoid generic AI defaults such as aggressive purple gradients, formulaic hero-card layouts, and filler statistics.

## Required `design.md` fields

The frontmatter must include at least:

- `schema_version: 3.1`
- `slug`
- `service_name`
- `site_url`
- `fetched_at`
- `default_theme`
- `brand_color`
- `primary_font`
- `font_weight_normal`
- `token_prefix`
- `bold_direction`
- `aesthetic_category`
- `signature_element`
- `code_complexity`
- `medium`
- `medium_confidence`

## `§18 DON'T` minimum rule

Include a final section that captures concrete forbidden patterns such as:

- hex colors that must not appear outside narrow roles
- disallowed font weights or pairings
- banned layout motifs
- signature anti-patterns discovered during analysis
