---
name: pumasi-image
description: Image-generation companion skill for the pumasi plugin family. Use when the user wants an image, thumbnail, poster, logo, illustration, or related visual artifact. In Codex this maps directly to the native image generation/editing tool.
---

# Pumasi Image for Codex

Read these first:
- `references/clarification-matrix.md`
- `references/keyword-mapping.md`
- `references/image-studio-prompt.md`

Use this skill when the user explicitly wants an image or visual deliverable. Do not use it for code-generation requests.

## Codex Workflow

1. Infer the visual mode from the request.
2. Ask at most one clarification if the request is still ambiguous in a way that would change the output materially.
3. Use the reference files to normalize:
   - aspect ratio hints
   - quality hints
   - mode-specific style/mood/composition slots
4. Convert the normalized request into a single strong prompt.
5. Use the native image generation or editing tool directly.

## Native Contract

- Do not launch background CLI sessions for image generation.
- Do not call external wrapper scripts for image generation.
- Keep prompt construction and clarification policy from the reference files, then call the native image tool directly.
