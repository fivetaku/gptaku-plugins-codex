# kkirikkiri Validation Guide for Codex

Use this file when deciding whether to keep the current team, swap one role, or rebuild the team.

## Decision rules

- Keep the team if the direction is right and only depth or clarity is missing.
- Swap one role if a single contributor is weak but the rest of the team is useful.
- Rebuild the team if the approach is fundamentally wrong or the user explicitly asks to restart.

## Keep-the-team pattern

- Send one focused follow-up to the weakest role.
- Tighten the scope or acceptance criteria.
- Add a verifier only if there is a concrete claim, artifact, or code path to check.

## Partial replacement pattern

- Keep the lead so context stays stable.
- Replace only the weak explorer, worker, or reviewer.
- Point the replacement agent to:
  - `.kkirikkiri/TEAM_PLAN.md`
  - `.kkirikkiri/TEAM_PROGRESS.md`
  - `.kkirikkiri/TEAM_FINDINGS.md`

## Rebuild pattern

- Summarize what failed in `TEAM_PROGRESS.md`.
- Keep any trustworthy findings in `TEAM_FINDINGS.md`.
- Start a fresh team shape from `presets.md` instead of repeating the exact old roster.

## User-facing check

When you need confirmation, ask in chat with a compact choice:

```text
지금 팀을 어떻게 할까요?
1. 그대로 보강 - 방향은 맞고 디테일만 보완
2. 일부 교체 - 특정 역할만 바꾸기
3. 새로 구성 - 접근 자체를 바꿔서 다시 시작
```
