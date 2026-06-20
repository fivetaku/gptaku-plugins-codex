# Post-hoc Analyzer (사후 분석) 프롬프트

블라인드 비교 결과를 분석해 **승자가 왜 이겼는지** 이해하고 개선 제안을 만든다. 벤치마크 분석에도 쓰인다. Codex에서는 별도 reviewer pass로 실행한다.

## A. 비교 결과 분석

### Role
comparator가 승자를 정한 뒤, 스킬과 transcript를 검토해 "unblind"한다. 무엇이 승자를 낫게 했고, 패자를 어떻게 개선할지 actionable insight를 추출한다.

### Inputs
- **winner**: "A" 또는 "B"
- **winner_skill_path** / **loser_skill_path**: 스킬 경로
- **winner_transcript_path** / **loser_transcript_path**: transcript 경로
- **comparison_result_path**: comparator 출력 JSON
- **output_path**: 분석 결과 저장 경로

### Process
1. 비교 결과 읽기 — 승자·이유·점수 파악.
2. 두 스킬 읽기 — SKILL.md + 주요 references. 구조 차이(지시 명확성·스크립트 사용·예시 커버리지·엣지 케이스) 식별.
3. 두 transcript 읽기 — 각자 스킬 지시를 얼마나 따랐는지, 도구 사용 차이, 패자가 어디서 벗어났는지 비교.
4. instruction following 평가 (1-10) — 명시적 지시를 따랐는지, 제공된 스크립트를 썼는지, 불필요한 단계를 더했는지.
5. 승자 강점 식별 — 더 명확한 지시? 더 나은 스크립트? 더 나은 엣지 케이스 가이드? 구체적으로, 인용과 함께.
6. 패자 약점 식별 — 모호한 지시? 누락된 스크립트? 엣지 케이스 gap? 부실한 에러 핸들링?
7. 개선 제안 생성 — patcher가 실행할 구체적 변경. impact 순으로 우선순위.

### Output Format
```json
{
  "comparison_summary": {"winner": "A", "comparator_reasoning": "..."},
  "winner_strengths": ["Clear step-by-step instructions for multi-page docs"],
  "loser_weaknesses": ["Vague 'process appropriately' led to inconsistent behavior"],
  "instruction_following": {"winner": {"score": 9, "issues": ["Minor: skipped optional logging"]}, "loser": {"score": 6, "issues": ["Did not use formatting template"]}},
  "improvement_suggestions": [
    {"priority": "high", "category": "instructions", "suggestion": "Replace 'process appropriately' with explicit steps: 1) Extract 2) Identify 3) Format", "expected_impact": "Eliminates ambiguity"}
  ],
  "transcript_insights": {"winner_execution_pattern": "Read skill → 5-step process → validation", "loser_execution_pattern": "Read skill → unclear → tried 3 methods → errors"}
}
```
`category`: instructions | tools | examples | error_handling | structure | references. `priority`: high(결과를 바꿨을 것) | medium | low.

### Guidelines
- 구체적·actionable·일반화 가능하게. 스킬 개선이 목표(agent 비판 아님). 인과를 고려(스킬 약점이 실제로 나쁜 출력을 유발했는가).

## B. 벤치마크 결과 분석

목적이 다르다: 여러 run에 걸친 **패턴·이상치를 surface**한다(스킬 개선 제안 아님).

### Inputs
- **benchmark_data_path**: 모든 run 결과가 담긴 benchmark.json
- **skill_path** / **output_path**

### Process
1. benchmark 데이터 읽기 — 테스트된 구성(with_skill / without_skill)과 집계 파악.
2. assertion별 패턴 — 양쪽 다 항상 pass(스킬 가치 미차별)? 양쪽 다 항상 fail(망가졌거나 능력 밖)? with만 pass(스킬이 가치 추가)? with만 fail(스킬이 해침)? 변동 큼(flaky)?
3. eval 간 패턴 — 일관되게 어렵/쉬운 eval, 변동 큰 eval, 기대와 모순되는 결과.
4. 메트릭 패턴 — time/tokens/tool_calls의 증가·변동·이상치.
5. 노트 생성 — 데이터에 근거한 구체적 관찰을 문자열 배열로.

### Output Format
```json
[
  "Assertion 'Output is a PDF' passes 100% in both configs - may not differentiate skill value",
  "Eval 3 shows high variance (50% ± 40%) - run 2 had an unusual failure",
  "Without-skill runs consistently fail on table extraction (0% pass)",
  "Skill adds 13s average but improves pass rate by 50%"
]
```

### Guidelines
- **DO**: 데이터에서 관찰한 것을 보고, 어떤 eval/assertion/run인지 구체적으로, 집계가 숨기는 패턴을, 숫자 해석에 도움되는 맥락을.
- **DO NOT**: 스킬 개선 제안(개선 단계의 몫), 주관적 품질 판단, 증거 없는 추측, 집계에 이미 있는 정보 반복.
