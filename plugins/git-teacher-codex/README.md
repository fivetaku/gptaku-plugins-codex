# git-teacher-codex

Codex marketplace package for the `git-teacher` product unit.

Included skills:
- `git-teacher-setup` — Installs or checks Git/GitHub CLI setup and connects a repository.
- `git-teacher-status` — Explains repository status in beginner-friendly Korean.
- `git-teacher-save` — Stages and commits local changes.
- `git-teacher-upload` — Pushes committed work to GitHub.
- `git-teacher-review` — Creates a Pull Request workflow.
- `git-teacher-help` — Explains Git concepts with cloud-folder analogies.

Packaging notes:
- Codex triggers each skill directly from natural language; there is no separate command router.
- Destructive Git history edits are intentionally excluded from the beginner workflow.
