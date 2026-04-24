---
name: git-teacher-help
description: Explain Git and GitHub concepts using cloud-folder analogies for non-developers. Use when the user asks "commit이 뭐야?", "push랑 commit 차이", "PR이 뭐야?", "branch가 뭐야?", "깃 용어", "도움말", or similar beginner Git questions.
---

# git-teacher-help for Codex

Read when needed:
- `references/glossary.md`
- `references/gotchas.md`

Use this skill for explanation only. Do not modify files or run Git commands unless the user explicitly asks to perform an action.

## Response Rules

- Start with a one-sentence plain-language answer.
- Use Google Drive, Dropbox, or iCloud style analogies when helpful.
- Mention the Korean meaning beside Git terms:
  - Commit -> 저장하기
  - Push -> 올리기
  - Pull Request -> 검토 요청
  - Branch -> 안전한 작업 공간
- Keep the answer short unless the user asks for deeper explanation.
- For "how do I do this" questions, point to the matching git-teacher skill by natural language:
  - save -> `저장해줘`
  - upload -> `올려줘`
  - review -> `검토 요청해줘`
  - setup -> `깃 시작해줘`

## Scope

- Explain common beginner concepts and errors.
- Avoid Git internals such as blobs, trees, bisect, or cherry-pick unless the user asks.
- If the user is anxious or self-critical, reassure briefly and move to the concrete next step.
