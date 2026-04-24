# Schemas

## Skill Brief

```json
{
  "name": "example-skill",
  "artifact_type": "skill",
  "purpose": "What the capability does",
  "triggers": ["example request"],
  "inputs": ["required user input"],
  "outputs": ["files or responses produced"],
  "references": ["references/file.md"],
  "scripts": ["scripts/tool.py"],
  "validation": ["python3 scripts/quick_validate.py path/to/skill"]
}
```

## Plugin Brief

```json
{
  "name": "example-codex",
  "artifact_type": "plugin",
  "display_name": "Example Codex",
  "skills": ["example-skill"],
  "assets": ["assets/example.svg"],
  "category": "Productivity",
  "default_prompts": ["Use example-skill to ..."]
}
```

## Eval Item

```json
{
  "id": "positive-basic",
  "prompt": "User request",
  "should_trigger": true,
  "expected_behavior": "Observable behavior",
  "must_include": ["required output"],
  "must_avoid": ["forbidden behavior"]
}
```
