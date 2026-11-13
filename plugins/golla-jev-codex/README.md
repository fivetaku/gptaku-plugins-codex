# golla-jev-codex

Codex port of the **golla-jev (골라제브)** plugin (v0.1.2). Describe a task and it finds the "pick one" moments, hands them to Jev (TypeSafe System One), and returns a workflow design you can test.

## Triggers

| Trigger | Notes |
|---|---|
| 골라제브 / golla-jev | Name |
| 제브로 뭐 할 수 있어 · 우리 회사에 jev 쓸 데 있어? | Idea mode: 3–5 candidates first |
| 이 업무 jev 워크플로 짜줘 · design a Jev workflow | Design mode: one task end to end |

## What it returns

Flow, step table (Jev / code / LLM / person), draft question JSON, output document preview with per-field source tags, similar public cases, failure points, and a dev/holdout threshold test plan.

## Bundled

- `skills/golla-jev/bench/` — 108-item Korean office benchmark template. Re-measured 2026-11-13 on jev-1.14.0: Korean questions 96.3%, English 93.5%, dev threshold 0.70 → holdout 57/59 auto-handled with 0 errors. The key is read only from `TYPESAFE_API_KEY`.
- `examples/` — three designs produced by the original plugin and reviewed against a checklist.

## Codex differences

- Paths use `$PLUGIN_ROOT`.
- No first-run setup hook (Codex plugins do not run plugin hooks). Updates come from `codex plugin marketplace upgrade`.
- Questions, when needed, are shown as numbered options in chat (see `shared/questioning-policy.md` §A).

## Requirements

Codex CLI. Running the drafted questions needs a TypeSafe API key (paid). Designs alone need no key.

Original plugin: https://github.com/fivetaku/golla-jev · MIT
