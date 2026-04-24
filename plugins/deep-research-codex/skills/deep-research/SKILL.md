---
name: deep-research
description: Comprehensive, citation-heavy research workflow with session state, structured outputs, and source-quality checks. Use when the user explicitly asks for deep research, a long-form report, or citation-backed analysis on a topic.
---

# deep-research for Codex

Read these first:
- `references/phase_contracts.md`
- `references/citation_rules.md`
- `references/quality_rubric.md`

Read as needed:
- `references/query_generator.md`
- `references/tool_strategy.md`
- `references/agent_prompts.md`
- `references/query_schema.json`
- `examples/*.json`

Use this skill when the user explicitly wants deep research, a citation-backed report, or a structured multi-phase investigation.

## Codex Workflow

1. Determine the mode:
   - new research
   - resume existing session
   - status
2. If the request is under-scoped, ask one compact chat-first clarification covering only the biggest unknowns.
3. Create or resume a session under `RESEARCH/` using the local orchestrator helpers.
4. Break the topic into subtopics and generate date-aware search queries.
5. Gather sources with current official or primary references wherever possible.
6. Track source quality and contradictions before synthesis.
7. Write the requested output with citations and clear source provenance.

## Guardrails

- Default to local execution of the research flow.
- Use live browsing for current facts and source verification.
- Prefer primary sources over summaries whenever available.
- Use sub-agents only when the user explicitly asks for team-style or parallel research, and keep each delegated subtopic bounded.
- Every key claim should have at least two supporting sources when feasible.
- If evidence is weak or contradictory, say so plainly.

## Outputs

Expected workspace shape:

```text
RESEARCH/<session_id>/
  state.json
  README.md
  sources/
  outputs/
  artifacts/
```
