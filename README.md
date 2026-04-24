English | [한국어](README.ko.md)

# GPTaku Codex Plugins

> **Codex-native plugin marketplace for GPTaku plugins.**

This repository is the Codex marketplace root. It contains Codex plugin manifests, packaged skills, plugin READMEs, validation scripts, and the marketplace manifest.

## Quick Start

Add the marketplace:

```bash
codex plugin marketplace add OWNER/gptaku-plugins-codex
```

If the repository is published under `fivetaku`, use:

```bash
codex plugin marketplace add fivetaku/gptaku-plugins-codex
```

Pin a release or branch when you want reproducible installs:

```bash
codex plugin marketplace add OWNER/gptaku-plugins-codex@v0.1.0
```

After adding the marketplace:
- Restart Codex so the marketplace is reloaded.
- Open the Codex plugin UI and install the plugins you want from `GPTaku Codex`.
- Start a new Codex session before testing newly installed skills.

Use installed plugins by asking naturally in chat. Examples:
- `pumasi-codex` — "Use pumasi to build this app with parallel workers."
- `show-me-the-prd-codex` — "Turn this product idea into a PRD."
- `insane-search-codex` — "Fetch this blocked page and summarize it."
- `kkirikkiri-codex` — "Assemble an agent team to investigate this."
- `docs-guide-codex` — "Explain this using official docs."
- `deep-research-codex` — "Do deep research with citations."
- `nopal-codex` — "Help me work with Google Workspace."
- `git-teacher-codex` — "Teach me this Git workflow step by step."
- `skillers-suda-codex` — "Help me design a Codex skill."
- `vibe-sunsang-codex` — "Review my recent Codex sessions and coach me."

Current Codex CLI exposes marketplace management commands:
- `codex plugin marketplace add <source>` — add a GitHub, Git URL, SSH URL, or local marketplace root.
- `codex plugin marketplace upgrade [gptaku-codex]` — update the marketplace clone.
- `codex plugin marketplace remove gptaku-codex` — remove this marketplace.

## Install From Local Checkout

For local testing before publishing:

```bash
codex plugin marketplace add /absolute/path/to/gptaku-plugins-codex
```

This staging checkout was verified with:

```bash
codex plugin marketplace add /Users/chulrolee/gptaku_plugins/gptaku-plugins-codex
```

Expected result:

```text
Added marketplace `gptaku-codex` from /Users/chulrolee/gptaku_plugins/gptaku-plugins-codex.
Installed marketplace root: /Users/chulrolee/gptaku_plugins/gptaku-plugins-codex
```

## Publish Checklist

- Run `bash scripts/run_package_smoke_tests.sh`.
- Ensure `.agents/plugins/marketplace.json` has `"name": "gptaku-codex"`.
- Ensure every package has `.codex-plugin/plugin.json`, `README.md`, and at least one `skills/<skill-name>/SKILL.md`.
- Publish the contents of this directory as the `gptaku-plugins-codex` GitHub repository root.
- Tag releases, then recommend pinned installs such as `OWNER/REPO@v0.1.0`.
- Tell users to restart Codex after adding or upgrading the marketplace.

## Repository Layout

```text
gptaku-plugins-codex/
  .agents/plugins/marketplace.json   # Codex marketplace manifest
  plugins/
    <plugin-name>/
      .codex-plugin/plugin.json      # plugin manifest
      README.md
      assets/
      skills/
        <skill-name>/
          SKILL.md
          references/
          scripts/
  scripts/
    validate_packages.py
    run_package_smoke_tests.sh
```

Use this repository for:
- Codex marketplace packaging
- plugin manifests
- marketplace manifest maintenance
- packaged plugin README files

Do not publish source-port workspaces, legacy runtime plugin trees, cache directories, or local smoke-test logs in this repository.

## Current Packaged Plugins

- `pumasi-codex`
- `show-me-the-prd-codex`
- `insane-search-codex`
- `kkirikkiri-codex`
- `insane-design-codex`
- `docs-guide-codex`
- `deep-research-codex`
- `nopal-codex`
- `git-teacher-codex`
- `skillers-suda-codex`
- `vibe-sunsang-codex`

## Packaging Flow

1. Edit the packaged plugin under `plugins/<plugin-name>/`.
2. Keep only runtime-safe files in `skills/<skill-name>/`.
3. Fill `.codex-plugin/plugin.json`.
4. Add or update the plugin entry in `.agents/plugins/marketplace.json`.
5. Run the validation and smoke-test commands below.

## Marketplace Manifest

- [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json)

## Validation

Run the package audit from the repository root:

```bash
python3 scripts/validate_packages.py
```

The audit checks marketplace entries, plugin manifests, skill frontmatter, referenced files, legacy-runtime residue, port-note residue, and script syntax.

Run the smoke suite when changing packaged plugin contents:

```bash
bash scripts/run_package_smoke_tests.sh
```

The smoke suite runs the package audit, JSON manifest parsing, available package-level smoke tests, helper-script smoke tests, and the legacy-residue scan.

## License

MIT
