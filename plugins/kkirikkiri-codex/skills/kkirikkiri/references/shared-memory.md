# kkirikkiri Shared Memory for Codex

The canonical record lives in `.kkirikkiri/`.

## Required files

- `TEAM_PLAN.md` — current plan, roles, assumptions, acceptance criteria
- `TEAM_PROGRESS.md` — what has started, what is blocked, what changed
- `TEAM_FINDINGS.md` — concrete findings worth handing across agents
- `TEAM_REPORT.md` — final integrated output

## Rules

- The lead updates shared memory whenever the plan materially changes.
- New or replacement agents should read `TEAM_PLAN.md`, `TEAM_PROGRESS.md`, and `TEAM_FINDINGS.md` before doing work.
- Keep entries short and stateful. Prefer bullets over long prose.
- If you make an assumption instead of asking the user, record it in `TEAM_PLAN.md`.

## Replacement workflow

- Replace only the underperforming role first.
- Keep prior findings unless they are clearly wrong.
- Point the replacement agent to the shared files instead of re-explaining the whole task.

## Progress logging

Good progress entries include:

- what finished
- what is still open
- what the next gate is
- which files or outputs are affected
