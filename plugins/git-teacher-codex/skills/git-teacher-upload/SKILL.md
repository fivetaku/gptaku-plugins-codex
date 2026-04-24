---
name: git-teacher-upload
description: Push committed work to GitHub with beginner-friendly explanations. Use when the user says "올려줘", "푸시", "업로드", "GitHub에 올려줘", "push", or "upload".
---

# git-teacher-upload for Codex

Use this skill to push committed work to GitHub.

## Workflow

1. Collect status in parallel when possible:
   - `git rev-parse --is-inside-work-tree`
   - `git symbolic-ref --short HEAD`
   - `git status --porcelain`
   - `git rev-list --count @{u}..HEAD`
   - `git remote get-url origin`
2. Stop if this is not a Git repository.
3. Stop if there is no `origin` remote and point the user to `git-teacher-setup`.
4. Stop if there are uncommitted changes and tell the user to save first.
5. Stop if there is nothing to push.
6. Run `git push origin HEAD`.
7. Convert the remote URL into a browser URL when possible and show it.

## Push Failure Handling

- `non-fast-forward` — Explain that GitHub has newer work. Run `git pull --rebase origin <branch>` only when the working tree is clean, then retry push if rebase succeeds.
- conflict during rebase — Show conflict files and ask in chat which side to keep before continuing.
- permission denied — Ask the user to run setup or authenticate with GitHub CLI.
- remote not found — Ask the user to run setup and reconnect the repository.

## Output

Always explain:
- what was uploaded
- where it is visible on GitHub
- whether a PR is the next likely action
