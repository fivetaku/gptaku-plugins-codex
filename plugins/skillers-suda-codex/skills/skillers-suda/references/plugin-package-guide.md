# Plugin Package Guide

Use this when the output should be a Codex plugin rather than a standalone skill.

## Required Files

```text
<plugin>/
  .codex-plugin/plugin.json
  README.md
  skills/
  assets/
```

## Manifest Rules

- `name` must match the outer folder name.
- `skills` should point to `./skills/`.
- `interface.displayName` should be human-readable.
- `interface.defaultPrompt` should contain real example prompts.
- `composerIcon` and `logo` should point to package-local assets when present.

## Marketplace Entry

Use this shape when adding to a staging marketplace:

```json
{
  "name": "plugin-name",
  "source": {
    "source": "local",
    "path": "./plugins/plugin-name"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Keep source ports and packaged marketplace plugins separate when a repo contains multiple runtime generations.
