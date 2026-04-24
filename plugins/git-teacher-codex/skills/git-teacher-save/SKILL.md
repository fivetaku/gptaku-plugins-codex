---
name: git-teacher-save
description: Stage and commit changed files with beginner-friendly Korean explanations. Use when the user says "저장해줘", "커밋", "변경 내용 저장", "save", or "commit".
---

# git-teacher-save for Codex

Use this skill to commit local changes safely.

## Workflow

1. Collect status in parallel when possible:
   - `git rev-parse --is-inside-work-tree`
   - `git symbolic-ref --short HEAD`
   - `git status --porcelain`
   - `git diff --stat`
   - `ls .gitignore`
2. Stop if this is not a Git repository.
3. If conflicts exist, show the files and ask in chat which side to keep:
   - `1. 내 변경 유지`
   - `2. 상대방 변경 유지`
4. Stop if there are no changes.
5. Create a basic `.gitignore` if missing:
   - Node.js: `node_modules/`, `.env`, `dist/`
   - Python: `__pycache__/`, `.env`, `venv/`
   - General: `.env`, `.DS_Store`, `*.log`, `thumbs.db`
6. Show a compact changed-file summary.
7. Ask for a commit message in chat only if a good message cannot be inferred.
8. Run:
   - `git add -A`
   - `git commit -m "<message>"`
9. Explain that the work is saved locally and still needs upload to GitHub.

## Commit Message Rules

- Use the user's natural Korean or English phrasing.
- Do not force conventional commits.
- If the user gives an empty or vague message, infer a short message from the diff.

## Safety

- Never run destructive commands such as hard reset.
- Do not rewrite history unless the user explicitly asks.
- Keep unrelated user changes intact.
