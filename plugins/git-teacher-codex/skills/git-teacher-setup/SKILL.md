---
name: git-teacher-setup
description: Help non-developers install Git, authenticate GitHub CLI, and create or connect a repository. Use when the user says "깃 시작", "깃 설정", "처음이에요", "git 설치", "GitHub 연결", "프로젝트 만들기", or "git setup".
---

# git-teacher-setup for Codex

Use this skill to prepare Git and GitHub for a beginner.

## Workflow

1. Collect setup status in parallel when possible:
   - `git --version`
   - `gh --version`
   - `git config --global user.name`
   - `git config --global user.email`
   - `gh auth status`
2. Show what is already ready and what is missing.
3. For missing tools, provide the right install command for the user's OS.
4. For missing Git identity, ask in chat for name and email, or infer from GitHub only after authentication exists.
5. For missing GitHub auth, run or show:
   - `gh auth login --web --git-protocol https`
6. For project setup, ask in chat using compact choices:
   - `1. 새 프로젝트 시작`
   - `2. 기존 GitHub 프로젝트 가져오기`
   - `3. 현재 폴더를 Git 프로젝트로 만들기`
7. Run the matching setup command only after the target path and visibility are clear.

## Project Actions

- New project:
  - `mkdir <project-name>`
  - `git init`
  - `gh repo create <project-name> --public|--private --source=. --remote=origin --push`
- Existing project:
  - `gh repo clone owner/repo`
  - or `git clone <url>`
- Current folder:
  - `git init`
  - `gh repo create <folder-name> --public|--private --source=. --remote=origin --push`

## Safety

- Do not pretend interactive browser authentication is complete. Pause after launching or explaining the auth command.
- Do not create public repositories unless the user clearly chose public.
- Explain that GitHub upload is manual: save with commit, then upload with push.
