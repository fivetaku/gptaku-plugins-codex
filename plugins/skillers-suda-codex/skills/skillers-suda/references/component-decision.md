# Component Decision Guide

Choose the smallest artifact that makes the capability reusable.

## Artifact Types

- **Skill** — Best for instruction-heavy workflows, deterministic scripts, and reusable domain knowledge.
- **Plugin** — Best when a product unit needs multiple skills, assets, metadata, MCP config, or marketplace packaging.
- **Reference** — Best for large tables, examples, standards, schemas, or long explanations that should not load every time.
- **Script** — Best for deterministic validation, parsing, file generation, API wrappers, or repeatable transformations.
- **MCP/App** — Best only when the workflow needs live external capabilities that are already exposed as tools.

## Split Rules

- Keep related workflows in one plugin when they ship as one product.
- Split into multiple skills when trigger phrases and user intent are clearly different.
- Do not split only because a document is long; move the long content into `references/`.
- Do not create a script when a short instruction is enough.

## Codex Package Shape

```text
plugin-name/
  .codex-plugin/plugin.json
  README.md
  skills/
    skill-name/
      SKILL.md
      references/
      scripts/
  assets/
```

For migration work, keep temporary source-port notes outside the marketplace repository and publish only the final package shape.
