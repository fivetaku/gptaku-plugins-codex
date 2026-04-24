# kkirikkiri Interview Guide for Codex

This file replaces the widget-oriented interview flow with a chat-first approach that works in Codex default mode.

## Core rules

- Ask at most one clarification unless a second question is truly necessary to avoid a wrong team shape.
- Use compact multiple-choice style prompts in chat.
- Each option should explain:
  - what it means
  - why it helps
  - what tradeoff it introduces
- Let the user reply with:
  - a number
  - comma-separated numbers for multi-select
  - a short sentence if none of the choices fit

## Prompt shape

```text
어떤 결과가 필요해요?
1. 추천안 — 무엇인지, 왜 좋은지, 단점
2. 대안 — 무엇인지, 왜 좋은지, 단점
3. 다른 방향 — 한 줄로 적기
```

## When to ask

- Ask only if the answer changes:
  - team composition
  - ownership boundaries
  - acceptance criteria
  - whether delegation is even appropriate

Do not ask if the answer can be safely assumed and recorded in `.kkirikkiri/TEAM_PLAN.md`.

## Good clarification targets

- output depth
- delivery format
- whether code changes are expected
- whether speed or depth matters more

## Bad clarification targets

- model names
- exact agent count unless it changes the plan materially
- implementation trivia that the lead can decide

## Preview pattern

When structure matters, show a short preview first.

```text
현재 팀 초안
- Lead — plan and integration
- Researcher — source gathering
- Reviewer — quality check

이대로 갈까요?
1. 네, 이 구성으로 진행
2. 더 빠르게 — 인원 줄이기
3. 더 깊게 — 조사 역할 강화
```
