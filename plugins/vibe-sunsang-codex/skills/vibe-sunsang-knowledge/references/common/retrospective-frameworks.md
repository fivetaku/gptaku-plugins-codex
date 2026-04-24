# 개인 회고 프레임워크

> "We do not learn from experience. We learn from our reflection on experience." — John Dewey

## 1. WWI (What Went Well / What to Improve / Action Items)

가장 기본적이고 효과적인 회고 프레임워크입니다.

### 구조

| 섹션 | 질문 | 예시 |
|------|------|------|
| What Went Well | 이번에 잘한 것은? | "에러 메시지를 직접 읽고 원인을 파악했다" |
| What to Improve | 개선할 점은? | "요청이 너무 모호해서 AI가 엉뚱한 걸 만들었다" |
| Action Items | 다음에 할 행동은? | "요청 전에 '무엇을, 왜, 어디에' 체크리스트를 쓴다" |

### 실행 방법

1. **빈도**: 주 1회 (금요일 추천), 15~20분
2. **준비**: 지난 주 변환된 대화 로그를 훑어봄
3. **기록**: 각 섹션 2~3개씩
4. **행동**: Action Items는 **1~3개**로 제한 (작은 것이 쌓여 큰 변화)

---

## 2. Start / Stop / Continue

새로운 행동을 시작하고, 나쁜 습관을 멈추고, 좋은 습관을 유지하는 프레임워크.

| 카테고리 | 설명 | 비개발자 예시 |
|----------|------|---------------|
| **Start** | 새로 시작할 것 | "AI에게 요청하기 전에 목적을 한 줄로 적기" |
| **Stop** | 멈출 것 | "에러가 나면 무조건 '고쳐줘'만 말하기" |
| **Continue** | 계속할 것 | "코드 리뷰 요청해서 설명 듣기" |

---

## 3. 4L 프레임워크 (Liked / Learned / Lacked / Longed for)

감정과 학습에 초점을 맞춘 프레임워크. 비개발자에게 특히 유용합니다.

| L | 질문 | 포인트 |
|---|------|--------|
| **Liked** | 즐거웠던 순간은? | 성취감, AI와의 협업이 잘 된 경험 |
| **Learned** | 새로 배운 것은? | 새 개념, 도구 사용법, 패턴 |
| **Lacked** | 부족했던 것은? | 지식 부족, 요청 미흡, 검증 미비 |
| **Longed for** | 있었으면 좋겠는 것은? | 더 나은 가이드, 자동 체크, 학습 자료 |

---

## 4. AI 코딩 세션 전용 회고 템플릿

위 프레임워크들을 AI 코딩에 맞게 커스터마이징한 템플릿입니다.

```markdown
## 회고: [날짜] [프로젝트명]

### 이번 세션 요약
- 목표:
- 결과:
- 소요 시간:

### 요청 품질 평가
- [ ] 목적을 명확하게 전달했는가?
- [ ] 제약 조건을 알려줬는가? (언어, 프레임워크, 스타일)
- [ ] 예시나 참고자료를 제공했는가?
- [ ] 한 번에 한 가지만 요청했는가?

### 검증 & 이해
- [ ] AI가 만든 코드를 설명해달라고 했는가?
- [ ] 에러 메시지를 직접 읽어봤는가?
- [ ] 코드가 왜 이렇게 작성되었는지 이해했는가?
- [ ] 테스트를 요청했는가?

### 새로 배운 것
1.
2.
3.

### 반복된 문제
1.
2.

### 다음 Action Items (최대 3개)
1.
2.
3.
```

---

## 5. 회고 주기 가이드

| 주기 | 범위 | 질문 |
|------|------|------|
| **매 세션** | 방금 끝난 대화 | "이 세션에서 내 요청은 명확했나?" |
| **주간** | 이번 주 전체 | "반복된 실수나 패턴이 있나?" |
| **월간** | 이번 달 전체 | "한 달 전과 비교해서 성장했나?" |
| **분기** | 3개월 | "내 AI 활용 수준이 어떻게 변했나?" |

## 출처

- [Personal Retrospectives for Developers (HackerNoon)](https://hackernoon.com/personal-retrospectives-for-developers-e5d86813d65a)
- [What Went Well Retrospective Template (EasyRetro)](https://easyretro.io/templates/went-well-to-improve-action-items/)
- [Sprint Retrospective (Atlassian)](https://www.atlassian.com/team-playbook/plays/retrospective)
- [54 Retrospective Templates (Echometer)](https://echometerapp.com/en/retrospective-ideas-agile)
