# Schemas (Codex)

skillers-suda가 사용하는 구조화 메타데이터 스키마.

## Skill Brief

파일 생성 전 보여주는 설계 브리프.

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
  "validation": ["python3 $PLUGIN_ROOT/skills/example-skill/scripts/quick_validate.py path/to/skill"]
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

## evals.json

스킬의 eval을 정의한다. `evals/evals.json`에 위치.

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": "positive-basic",
      "prompt": "User's example prompt",
      "should_trigger": true,
      "expected_behavior": "What Codex should do",
      "files": [],
      "must_include": ["observable behavior"],
      "must_avoid": ["unsafe or irrelevant behavior"],
      "expectations": ["The output includes X", "The skill used script Y"],
      "quality_metrics": [
        {
          "name": "completeness",
          "criteria": "출력물이 요청된 모든 항목을 포함하는가",
          "evaluation_steps": ["항목 목록 추출", "존재 여부 확인", "비율 산출"],
          "threshold": 0.7
        }
      ]
    }
  ]
}
```

**Fields:**
- `skill_name`: 스킬 frontmatter name과 일치.
- `evals[].id`: 고유 식별자.
- `evals[].prompt`: 실행할 작업.
- `evals[].should_trigger`: 이 프롬프트에 스킬이 트리거되어야 하는지.
- `evals[].expected_behavior`: 성공의 human-readable 설명.
- `evals[].files`: (선택) 입력 파일 경로.
- `evals[].must_include` / `must_avoid`: 관찰 가능한 포함/금지 행동.
- `evals[].expectations`: 검증 가능한 진술 목록.
- `evals[].quality_metrics`: (선택) 연속 품질 메트릭. 각각 `name`, `criteria`(한 문장), `evaluation_steps`(3-5개), `threshold`(0-1).

## grading.json

채점기(grader) 출력. `<run-dir>/grading.json`.

```json
{
  "expectations": [
    {"text": "The output includes 'John Smith'", "passed": true, "evidence": "Found in Step 3"}
  ],
  "summary": {"passed": 2, "failed": 1, "total": 3, "pass_rate": 0.67},
  "claims": [
    {"claim": "The form has 12 fields", "type": "factual", "verified": true, "evidence": "Counted 12 fields"}
  ],
  "quality_metrics": [
    {"name": "completeness", "score": 0.85, "threshold": 0.7, "status": "PASS"}
  ],
  "overall_verdict": "pass",
  "verdict_reason": "All expectations passed. Quality metrics: 3/3 PASS."
}
```

**Fields:**
- `expectations[]`: 채점된 expectation (text / passed / evidence).
- `summary`: 집계 (passed / failed / total / pass_rate).
- `claims`: 출력에서 추출·검증한 주장 (claim / type=factual|process|quality / verified / evidence).
- `quality_metrics`: (선택) 연속 메트릭 결과 (name / score / threshold / status=PASS|WARN|FAIL).
- `overall_verdict`: (선택) `pass` | `conditional_pass` | `fail`.
- `verdict_reason`: (선택) 판정 설명.

## comparison.json

블라인드 비교기(comparator) 출력. `<grading-dir>/comparison-N.json`.

```json
{
  "winner": "A",
  "reasoning": "Output A is complete; B is missing the date field.",
  "rubric": {
    "A": {"content_score": 4.7, "structure_score": 4.3, "overall_score": 9.0},
    "B": {"content_score": 2.7, "structure_score": 2.7, "overall_score": 5.4}
  },
  "output_quality": {
    "A": {"score": 9, "strengths": ["..."], "weaknesses": ["..."]},
    "B": {"score": 5, "strengths": ["..."], "weaknesses": ["..."]}
  }
}
```
`winner`는 "A" | "B" | "TIE". expectations가 제공된 경우만 `expectation_results`를 포함한다.

## analysis.json

사후 분석기(analyzer) 출력. `<grading-dir>/analysis.json`.

```json
{
  "comparison_summary": {"winner": "A", "comparator_reasoning": "..."},
  "winner_strengths": ["Clear step-by-step instructions"],
  "loser_weaknesses": ["Vague instruction led to inconsistent behavior"],
  "improvement_suggestions": [
    {"priority": "high", "category": "instructions", "suggestion": "Replace vague step with explicit steps", "expected_impact": "Eliminates ambiguity"}
  ]
}
```
`category`: instructions | tools | examples | error_handling | structure | references. `priority`: high | medium | low.
