---
name: pumasi
description: Codex-native parallel build orchestration. Use when the user explicitly wants to delegate a greenfield or large multi-module implementation into parallel Codex worker sessions, while the main agent stays in the PM/architect role. Best for 3 or more independent modules with clear gates and interfaces.
---

# Pumasi for Codex

Read these first:
- `references/anti-patterns.md`
- `references/role-separation.md`
- `references/codex-guide.md`
- `references/instruction-templates.md`
- `references/tech-stack.md`

Read as needed:
- `references/examples.md`

## When To Use

- 3 or more independent new modules or files
- tasks with clear interfaces and bash-verifiable gates
- greenfield implementation or additive work with clean ownership

Do not use for:
- tiny tasks
- bug fixes in tightly coupled existing code
- aesthetic-only UI polish with no meaningful gates

## Codex-Native Workflow

1. Stay in the PM/architect role locally. Do not hand the critical path to a worker.
2. Decompose the request into disjoint tasks and rounds.
3. Initialize shared job state:
   `python3 scripts/init_workspace.py --root "$PWD" --task "<task summary>"`
4. Record the plan in `.pumasi/job.json`, `.pumasi/plan.md`, and `.pumasi/tasks/<task>.md`.
5. Spawn one worker agent per task with explicit file ownership and gate commands.
6. While workers run, keep integration context current in `.pumasi/plan.md`.
7. Validate each task with bash gates after completion.
8. If a task fails, re-delegate only that task with focused correction context.
9. Integrate after all task-level gates pass.

## Worker Rules

- The lead agent writes signatures, types, constraints, and gates.
- Worker agents write the implementation.
- Never paste full function bodies into task briefs.
- Every worker prompt must include:
  - owned files or directories
  - required signatures and imports
  - required libraries and forbidden substitutions
  - exact gate commands
  - reminder that other workers are editing the same repo

## Rounds

- Round 1: shared types, schemas, utilities
- Round 2+: tasks that depend on earlier interfaces
- Final: local integration and verification

Use rounds whenever independent parallel work would otherwise race on shared interfaces.
