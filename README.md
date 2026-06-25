English | [한국어](README.ko.md)

# gptaku-plugins-codex

> **A Codex plugin marketplace for people who want to become AI Native.**

Being AI Native is not about using AI as a tool. It is about weaving AI naturally into every step from planning to execution. That takes practice, and it takes tools built for people who are learning. These plugins exist to remove specific walls you hit while working with Codex.

[Quick Start](#quick-start) | [Plugins](#available-plugins) | [Why these?](#why-these-plugins) | [Requirements](#requirements)

---

## Quick Start

### 1. Add the marketplace

```bash
codex plugin marketplace add https://github.com/fivetaku/gptaku-plugins-codex.git
```

### 2. Restart Codex

Restart Codex after adding the marketplace so the plugin list is reloaded.

### 3. Install plugins from Codex

Open the Codex plugin UI:

```text
/plugins
```

Choose `GPTaku Codex`, then install the plugins you want.

### 4. Use them naturally

Start a new Codex session and ask in plain language:

```text
Turn this idea into a PRD.
Use pumasi to split this build into parallel workers.
Fetch this blocked page and summarize it.
Teach me this Git workflow step by step.
```

### 5. Update when needed

```bash
codex plugin marketplace upgrade gptaku-codex
```

---

## Why these plugins?

- **Built for learners, not experts** - If you do not know Git, `git-teacher-codex` explains it step by step. If you cannot write a PRD, `show-me-the-prd-codex` interviews you.
- **Codex-native** - These are packaged with `.codex-plugin/plugin.json`, Codex skills, Codex sub-agent patterns, and chat-first interaction rules.
- **Outcomes over features** - Each plugin solves a specific wall: blocked websites, blank PRDs, parallel coding, deep research, docs lookup, workspace orchestration, or growth coaching.
- **Korean-first, English-available** - Built in Korean, with English docs where useful.
- **Composable** - Install only what you need. The plugins are designed to work independently.

---

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [docs-guide-codex](plugins/docs-guide-codex) | Accurate answers grounded in official documentation, using an `llms.txt`-first strategy and official-source fallbacks. |
| [git-teacher-codex](plugins/git-teacher-codex) | Git/GitHub onboarding for non-developers, with cloud-service analogies and safe beginner workflows. |
| [vibe-sunsang-codex](plugins/vibe-sunsang-codex) | AI collaboration mentoring for vibecoders, including session retrospectives, mentoring, and growth reports. |
| [insane-research-codex](plugins/insane-research-codex) | Structured deep research with query design, source triangulation, citations, and quality checks. |
| [pumasi-codex](plugins/pumasi-codex) | Codex-native parallel build orchestration, plus a native image-generation companion skill. |
| [show-me-the-prd-codex](plugins/show-me-the-prd-codex) | Interview-based PRD generation from a rough idea into an actionable document bundle. |
| [kkirikkiri-codex](plugins/kkirikkiri-codex) | Codex-native agent-team assembly from natural language, with shared memory and bounded delegation. |
| [skillers-suda-codex](plugins/skillers-suda-codex) | A workshop for designing, reviewing, and packaging Codex skills or plugin bundles. |
| [nopal-codex](plugins/nopal-codex) | Google Workspace orchestration for Gmail, Calendar, Drive, Docs, Sheets, Slides, Chat, Tasks, and Meet through `gws`. |
| [insane-search-codex](plugins/insane-search-codex) | Adaptive-access workflow for blocked or WAF-heavy pages using generic fetch, public APIs, RSS, Jina, and optional Playwright. |
| [insane-design-codex](plugins/insane-design-codex) | Extract real website CSS into a reusable design system, or reuse the bundled design corpus. |

> More plugins can be added over time. Watch the repository to get release updates.

---

## Requirements

- **Codex CLI** with plugin marketplace support.
- **macOS / Linux**: works out of the box.
- **Windows**: use WSL2 for the best experience.
- Some plugins use optional tools such as `git`, `gh`, `node`, `python3`, `tmux`, or `gws`. The plugin instructions tell you when a tool is needed.

---

## Validate This Marketplace

For maintainers:

```bash
python3 scripts/validate_packages.py
bash scripts/run_package_smoke_tests.sh
```

The validation checks marketplace entries, plugin manifests, skill frontmatter, referenced files, legacy-runtime residue, port-note residue, script syntax, and available smoke tests.

---

## License

MIT

---

<div align="center">

**Become AI Native, one wall at a time.**

</div>
