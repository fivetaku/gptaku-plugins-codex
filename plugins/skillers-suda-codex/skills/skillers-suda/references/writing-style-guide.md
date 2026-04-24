# Writing Style Guide

Write Codex skills as operational instructions, not essays.

## SKILL.md Frontmatter

- `name` must be lowercase kebab-case.
- `description` should say when to use the skill and include likely trigger phrases.
- Keep the description specific enough to avoid over-triggering.

## Body Structure

- Start with what to read first.
- Put optional detail in `references/`.
- Put deterministic work in `scripts/`.
- Keep the main workflow short enough that Codex can act without rereading a large manual.

## Interaction Style

- Use chat-first questions.
- Ask at most one question before acting when a reasonable assumption is safe.
- For choice prompts, show numbered options with one-line tradeoffs.
- Use previews for generated structures before large file creation.

## Anti-Patterns

- Do not mention unavailable tools.
- Do not include command-router assumptions.
- Do not keep duplicate active docs with port-suffix names.
- Do not force a fixed word count if the task is simpler.
- Do not hide critical setup requirements in references only.
