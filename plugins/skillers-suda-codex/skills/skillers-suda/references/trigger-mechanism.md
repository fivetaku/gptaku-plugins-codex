# Trigger Mechanism (Codex)

> 스킬이 Codex에서 트리거되는 메커니즘과 description 최적화 전략. Phase H에서 참조.

## 트리거 방식

Codex는 사용자 메시지를 받으면 설치된 스킬의 description을 스캔한다. description이 사용자 의도와 매치되면 해당 스킬이 트리거되고 SKILL.md 본문이 로드된다.

```
사용자 메시지 → description 매칭 → SKILL.md 로드 → 실행
```

Codex에는 슬래시 커맨드 진입이 없으므로 **description이 유일한 트리거 표면**이다. 그만큼 description 품질이 중요하다.

## Undertrigger 경향

스킬은 기본적으로 **트리거가 안 되는 쪽으로 편향**된다.
- 정확한 키워드를 안 쓰면 트리거 안 됨.
- 유사 표현·우회 요청을 놓침.
- 한국어/영어 혼용 시 매칭 실패가 잦음.

## Pushy Description 전략

undertrigger 방지를 위해 description을 적극적으로 작성한다.
1. **넓은 트리거 범위** — 핵심 키워드 + 유사 표현·동의어·관련 행동.
2. **구체적 시나리오 나열** — "코드 리뷰"뿐 아니라 "코드 봐줘", "이거 괜찮아?", "버그 있나?".
3. **한/영 혼합**.
4. **행동 동사 중심** — 명사보다 동사로 의도를 매칭.

```
BAD:  "코드 리뷰 도구"
GOOD: "코드 리뷰, 코드 검토, 코드 봐줘, review my code, 버그 찾아줘. Make sure to use this skill whenever the user mentions code review, even if they don't explicitly ask for it."
```

## 복잡한 쿼리만 트리거

단순 질문엔 트리거하지 않고, 스킬이 진짜 필요한 복잡한 요청에만 반응하도록 설계한다.
- 단순: "Python이 뭐야?" → 트리거 X
- 복잡: "Python으로 웹 크롤러 만들어줘" → 트리거 O

복잡성 신호를 description에 포함: 작업 동사("만들어/생성해/설계해/분석해/최적화해") + 규모 명사("프로젝트/시스템/워크플로우").

## should-trigger / should-not-trigger

eval 설계 시 트리거 정확도도 테스트한다.

| 유형 | 설명 | 예시 |
|------|------|------|
| should-trigger | 반드시 트리거되어야 하는 쿼리 | "이 코드 리뷰해줘" |
| should-not-trigger | 트리거되면 안 되는 쿼리 | "Python 문법 알려줘" |

should-trigger 8-10개 + should-not-trigger 8-10개로 약 20개 쿼리를 만들어 트리거율을 측정하고, 가장 정확한 description을 frontmatter에 적용한다. before/after를 사용자에게 보여준다.
