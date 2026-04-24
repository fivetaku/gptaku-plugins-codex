---
name: git-teacher-status
description: Explain the current Git status in plain Korean for non-developers. Use when the user asks "상태 확인", "뭐가 바뀌었어?", "git status", "what changed", or wants to know whether work is saved or uploaded.
---

# git-teacher-status for Codex

Use this skill to translate repository state into beginner-friendly language.

## Workflow

1. Collect status in parallel when possible:
   - `git rev-parse --is-inside-work-tree`
   - `git symbolic-ref --short HEAD`
   - `git status --porcelain`
   - `git log --oneline -3`
   - `git remote -v`
   - `git stash list`
2. Stop with a clear explanation if this is not a Git repository.
3. If the repository is in detached `HEAD`, explain the risk and recover to `main` or `master` only when that target branch exists.
4. If conflicts exist, show the conflict files and ask in chat which side to keep:
   - `1. 내 변경 유지`
   - `2. 상대방 변경 유지`
5. Translate porcelain codes into simple Korean:
   - `M` -> `수정됨`
   - `A` -> `새로 추가됨`
   - `D` -> `삭제됨`
   - `R` -> `이름 바뀜`
   - `??` -> `새 파일`
6. Explain whether the work is:
   - changed but not committed
   - committed but not pushed
   - clean
   - connected or not connected to GitHub

## Tone

- Use cloud-folder analogies only when they make the answer clearer.
- Keep it concrete: what changed, what it means, and what the next safe action is.
- Avoid advanced Git jargon unless the user asks.
