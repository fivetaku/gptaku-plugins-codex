---
name: nopal
description: Codex용 Google Workspace 오케스트레이션 스킬. "nopal", "/nopal", "gws", "gmail", "calendar", "drive", "sheets", "docs", "slides", "chat", "tasks", "meet", "메일 보내줘", "일정 확인", "회의 준비", "문서/시트/드라이브 작업" 같은 요청에 사용됩니다.
---

# nopal for Codex

Read these first:
- `references/gws-shared.md`

Load as needed:
- `references/gws-gmail.md`
- `references/gws-calendar.md`
- `references/gws-drive.md`
- `references/gws-docs.md`
- `references/gws-sheets.md`
- `references/gws-slides.md`
- `references/gws-chat.md`
- `references/gws-tasks.md`
- `references/gws-meet.md`
- `references/recipes.md`
- `references/workflows.md`

Use this skill when the user wants Google Workspace work orchestrated from natural language.

## Codex Workflow

1. Check whether `gws` is installed.
2. If missing, install it with `npm install -g @googleworkspace/cli`.
3. Check authentication status with `gws auth status`.
4. If authentication is missing, stop and show the setup guidance from `nopal-setup`.
5. Parse the user request into:
   - read-only lookup
   - single write action
   - multi-step workflow
6. Read only the service references needed for the current request.
7. For read-only actions, execute directly.
8. For write actions, show a compact execution summary in chat and ask for confirmation before running.

## Guardrails

- Interact with Google Workspace only through `gws`.
- Do not make direct HTTP calls to Google APIs.
- Keep chat clarification minimal.
- When something is safely inferable, prefer defaults over extra questions.
- Read-only checks can run without confirmation.
- Any write, send, create, update, or delete action must be summarized in chat before execution.
