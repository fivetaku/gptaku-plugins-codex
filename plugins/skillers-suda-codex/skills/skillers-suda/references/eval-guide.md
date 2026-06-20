# Eval 가이드 (Codex)

생성된 스킬의 품질을 체계적으로 검증하기 위한 방법론. deepeval의 G-Eval 패턴을 참고. 사람이 읽는 eval부터 시작하고, 기대 동작이 안정화된 뒤에 자동화를 추가한다.

## 1. Eval 기준 정의 (Phase D)

스킬 생성 전에 성공 기준을 먼저 정의한다.

| 기준 | 설명 | 측정 |
|------|------|------|
| 트리거 정확도 | 의도한 입력에 스킬이 활성화되는가 | should-trigger / should-not-trigger 쿼리 |
| 워크플로우 완결성 | 모든 단계가 정상 실행되는가 | 시나리오 end-to-end |
| 출력 품질 | 결과물이 기대에 부합하는가 | 사용자 확인 |
| 엣지 케이스 | 예외 상황을 graceful하게 처리하는가 | 검수자 시나리오 |

### 최소 Eval 세트
- **positive trigger** — 스킬을 써야 하는 요청
- **negative trigger** — 비슷하지만 쓰면 안 되는 요청
- **edge case** — 모호하거나 정보 부족한 입력
- **realistic task** — 실제 사용에 가까운 전체 요청

### 시나리오 수
| 복잡도 | 정상 | 엣지 |
|--------|------|------|
| 단순 (1-3단계) | 2개 | 1개 |
| 보통 (4-6단계) | 3개 | 2개 |
| 복잡 (7+단계) | 3-5개 | 3개 |

### 현실적 프롬프트 철학
실제 사용자가 입력할 법한 구체적 문장으로 작성한다. 파일 경로·개인 상황·약어·오타·캐주얼 표현을 섞는다.
- BAD: `"이 데이터를 포맷해줘"`
- GOOD: `"다운로드 폴더에 'Q4 매출 최종_v2.xlsx' 있는데 C열이 매출이고 D열이 비용이야. 이익률 퍼센트 컬럼 추가해줘"`

## 2. 구조 자동 검증 (Phase E-verify)

파일 생성 직후 `scripts/quick_validate.py`로 구조 품질을 검증한다.

```bash
python3 $PLUGIN_ROOT/skills/skillers-suda/scripts/quick_validate.py <생성된 스킬 디렉토리>
```

검증 항목: frontmatter 존재, name kebab-case, description 존재·1024자 이하, 참조 경로 실재.

| FAIL 항목 | 조치 |
|-----------|------|
| frontmatter 누락 | YAML frontmatter 추가 |
| name kebab-case 위반 | 소문자-하이픈으로 변환 |
| description 누락/과길이 | 보강 또는 1024자 이하로 축약 |
| 참조 경로 없음 | 누락 파일 생성 또는 참조 제거 |

`PASS`까지 수정 후 재검증한다.

## 3. 수동 검증 (Phase F)

자동 검증으로 못 잡는 것: 의미적 정확성(워크플로우가 논리적으로 옳은가), 도메인 적합성, 사용자 경험, 엣지 케이스 대응. eval 시나리오를 직접 실행해 검증한다.

검토 기준: 트리거 정밀도, 첫 행동의 명확성, references/scripts 올바른 사용, 정보 부족 시 안전한 처리, 최종 출력의 유용성.

## 4. with-skill / without-skill 비교 (선택)

엄밀 비교가 필요하면 같은 프롬프트를 스킬 적용/미적용으로 각각 실행해 비교한다. 채점은 `references/agents/grader.md`, 블라인드 A/B는 `references/agents/comparator.md`, 패턴 분석은 `references/agents/analyzer.md`.

## 5. 출력 품질 메트릭 (G-Eval 패턴)

이진 expectations 외에 출력 품질을 0-1로 연속 점수화할 수 있다.

```json
{
  "name": "output_completeness",
  "criteria": "출력물이 요청된 모든 항목을 포함하는가",
  "evaluation_steps": ["요청 항목 추출", "각 항목 존재 확인", "누락 비율로 점수 산출"],
  "threshold": 0.7
}
```

스킬 유형별 권장 메트릭:
| 유형 | 메트릭 | threshold |
|------|--------|-----------|
| 번역 | accuracy / fluency / terminology | 0.8 / 0.7 / 0.7 |
| 요약 | completeness / conciseness / faithfulness | 0.7 / 0.7 / 0.8 |
| 코드 생성 | correctness / style / completeness | 0.9 / 0.6 / 0.8 |
| 분석/리서치 | depth / accuracy / actionability | 0.7 / 0.8 / 0.7 |
| 문서 생성 | structure / completeness / clarity | 0.7 / 0.8 / 0.7 |

작성 원칙: criteria는 한 문장, evaluation_steps 3-5개, threshold는 유형에 맞게(정확성 중요→높게, 창작성 중요→낮게), 점수 0-1.

## 6. Threshold 기반 종합 판정

| 조건 | 판정 |
|------|------|
| 모든 메트릭 PASS + 모든 expectations PASS | 합격 |
| expectations PASS + 일부 메트릭 0.5 이상 threshold 미달 | 조건부 합격 — 개선점 안내 |
| 어떤 expectations FAIL 또는 메트릭 0.5 미만 | 불합격 — 개선 필요 |

스키마 상세는 `references/schemas.md` 참조.
