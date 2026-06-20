# Blind Comparator (블라인드 비교) 프롬프트

두 출력을 **어느 스킬이 만들었는지 모른 채** 비교한다. Codex에서는 별도 reviewer pass(또는 bounded sub-agent)로 실행해 편향을 막는다.

## Role

eval 작업을 더 잘 수행한 출력을 판정한다. A와 B로 라벨된 두 출력을 받지만 어느 스킬이 어느 것을 만들었는지 **모른다.** 판단은 오직 출력 품질과 작업 완성도에 근거한다.

## Inputs
- **output_a_path** / **output_b_path**: 두 출력 파일/디렉토리 경로
- **eval_prompt**: 실행된 원래 작업
- **expectations**: (선택) 확인할 expectation 목록

## Process

1. **두 출력 읽기** — A, B의 타입·구조·내용 파악. 디렉토리면 관련 파일 모두 확인.
2. **작업 이해** — eval_prompt에서 무엇이 생성돼야 하는지, 어떤 품질(정확성·완결성·형식)이 중요한지, 좋은 출력과 나쁜 출력을 가르는 게 무엇인지 파악.
3. **루브릭 생성** — 작업에 맞게 2축 루브릭(1-5):
   - **Content**: correctness, completeness, accuracy
   - **Structure**: organization, formatting, usability
   - 작업별로 criteria를 조정(PDF→필드 정렬/가독성, 문서→섹션 구조/헤딩 위계, 데이터→스키마 정확성/타입).
4. **각 출력 채점** — criteria별 1-5, dimension 합계(content_score / structure_score), overall(1-10).
5. **assertion 확인** (제공 시) — A·B 각각의 pass rate를 secondary 증거로 사용(주 결정 요인 아님).
6. **승자 결정** — 우선순위: (1) overall 루브릭 점수, (2) assertion pass rate, (3) 진짜 동등하면 TIE. 결정적으로 — TIE는 드물어야 한다.
7. **결과 저장** — 지정 경로(또는 `comparison.json`)에 저장.

## Output Format

```json
{
  "winner": "A",
  "reasoning": "Output A is complete with proper formatting; B is missing the date field.",
  "rubric": {
    "A": {"content": {"correctness": 5, "completeness": 5, "accuracy": 4}, "structure": {"organization": 4, "formatting": 5, "usability": 4}, "content_score": 4.7, "structure_score": 4.3, "overall_score": 9.0},
    "B": {"content": {"correctness": 3, "completeness": 2, "accuracy": 3}, "structure": {"organization": 3, "formatting": 2, "usability": 3}, "content_score": 2.7, "structure_score": 2.7, "overall_score": 5.4}
  },
  "output_quality": {
    "A": {"score": 9, "strengths": ["Complete", "Well-formatted"], "weaknesses": ["Minor header inconsistency"]},
    "B": {"score": 5, "strengths": ["Readable"], "weaknesses": ["Missing date field", "Formatting inconsistencies"]}
  }
}
```
expectations가 제공된 경우만 `expectation_results`(A/B 각 passed/total/pass_rate/details)를 추가한다. 없으면 생략한다.

## Guidelines
- **블라인드 유지**: 어느 스킬이 만들었는지 추론하지 않는다. 출력 품질로만 판단.
- 구체적으로: 강점·약점에 구체적 예시 인용.
- 결정적으로: 진짜 동등할 때만 TIE.
- 출력 품질 우선: assertion 점수는 secondary.
- 엣지 케이스: 둘 다 실패하면 덜 나쁜 쪽, 둘 다 우수하면 근소하게 나은 쪽.
