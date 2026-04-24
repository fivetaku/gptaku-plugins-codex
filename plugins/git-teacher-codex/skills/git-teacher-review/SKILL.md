---
name: git-teacher-review
description: Create a beginner-friendly GitHub Pull Request workflow. Use when the user says "PR 만들어줘", "검토 요청", "리뷰 요청", "팀원한테 보여주고 싶어", "create PR", or "pull request".
---

# git-teacher-review for Codex

Use this skill to create a Pull Request while explaining it as a safe review request.

## Workflow

1. Collect status in parallel when possible:
   - `git rev-parse --is-inside-work-tree`
   - `git symbolic-ref --short HEAD`
   - `git status --porcelain`
   - `git rev-list --count @{u}..HEAD`
   - `git remote get-url origin`
   - `gh auth status`
2. Stop if this is not a Git repository.
3. Stop if there is no `origin` remote or GitHub CLI is not authenticated.
4. Stop and explain if conflicts exist.
5. Determine whether there are uncommitted changes or unpushed commits.
6. Ask for a short work description in chat only when it cannot be inferred from the diff or recent commits.
7. If currently on `main` or `master`, create a review branch with a readable slug and date.
8. Commit changes when needed:
   - `git add -A`
   - `git commit -m "<description>"`
9. Push:
   - `git push origin HEAD`
10. Create the PR:
    - `gh pr create --title "<description>" --body "<summary>"`
11. Return to `main` or `master` only when it is safe and the branch existed before.
12. Show the PR URL and explain what the teammate sees.

## Branch Naming

- Use a short English slug when possible.
- Add a date suffix such as `0424`.
- Example: `main-page-design/0424`.

## Safety

- Do not use `git reset --hard`.
- Do not rewrite committed history unless the user explicitly asks.
- If a PR already exists for the branch, show the existing PR URL instead of creating another.
