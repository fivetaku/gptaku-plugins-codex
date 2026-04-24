# Eval Guide

Use evals to check whether the generated skill triggers correctly and produces useful output.

## Minimum Eval Set

Create at least:

- positive trigger — a user request that should use the skill
- negative trigger — a nearby request that should not use the skill
- edge case — ambiguous or underspecified input
- realistic task — a full request close to real usage

## Eval Record

```json
{
  "id": "positive-basic",
  "prompt": "User request",
  "should_trigger": true,
  "expected_behavior": "What Codex should do",
  "must_include": ["observable behavior"],
  "must_avoid": ["unsafe or irrelevant behavior"]
}
```

## Review Criteria

- trigger precision
- clarity of first action
- correct use of references or scripts
- safe handling of missing information
- useful final output

Prefer human-readable evals first. Add automation only after the expected behavior is stable.
