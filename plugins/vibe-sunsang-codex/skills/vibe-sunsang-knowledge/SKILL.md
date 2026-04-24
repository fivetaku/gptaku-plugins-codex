---
name: vibe-sunsang-knowledge
description: Answer questions about vibe-sunsang workspace types, AI collaboration levels, six growth axes, prompt quality, anti-patterns, and mentoring frameworks. Use when the user asks "바선생 레벨", "6축", "안티패턴", "요청 품질", or "workspace types".
---

# vibe-sunsang-knowledge for Codex

Read as needed:
- `references/common/prompt-quality.md`
- `references/common/mentoring-checklist.md`
- `references/common/retrospective-frameworks.md`
- `references/{builder,explorer,designer,operator}/antipatterns.md`
- `references/{builder,explorer,designer,operator}/concepts.md`
- `references/{builder,explorer,designer,operator}/growth-metrics.md`

Use this skill for explanation only.

## Workspace Types

- `builder` — coding, implementation, app/service building
- `explorer` — research, learning, investigation
- `designer` — planning, ideation, content or product design
- `operator` — automation, operations, repeatable workflows

## Six Growth Axes

- `DECOMP` — task decomposition
- `VERIFY` — verification strategy
- `ORCH` — orchestration of tools, agents, and workflow
- `FAIL` — failure recovery
- `CTX` — context management
- `META` — metacognition and strategic adjustment

## Workflow

1. Infer the topic from the user request.
2. If the topic is type-specific and the type is unclear, ask in chat with the four workspace types.
3. Load only the relevant reference files.
4. Explain in Korean by default:
   - one-sentence answer
   - practical example
   - related concept when useful

## Guardrails

- Do not overload the user with the whole framework unless asked.
- Keep examples grounded in AI collaboration behavior.
- When unsure of workspace type, say the assumption.
