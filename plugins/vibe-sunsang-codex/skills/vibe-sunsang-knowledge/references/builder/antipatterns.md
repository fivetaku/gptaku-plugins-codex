# 비개발자가 빠지기 쉬운 안티패턴

> AI 코딩 도구를 사용할 때 비개발자가 자주 빠지는 함정과 해결법

## The 80% Problem (Addy Osmani)

AI는 빠르게 80%를 만들어 주지만, **나머지 20%가 진짜 어려운 부분**입니다.
80%에서 "거의 다 됐네"라고 느끼지만, 프로덕션 수준까지 가려면
보안, 성능, 에러 처리, 엣지 케이스 등 깊은 지식이 필요합니다.

---

## 안티패턴 목록

### 1. "고쳐줘" 증후군

**증상**: 에러가 나면 에러 메시지를 읽지 않고 "고쳐줘"만 반복
**문제**: AI가 원인이 아닌 증상만 치료하여 문제가 깊어짐
**해결**:
- 에러 메시지의 첫 줄을 직접 읽어보기
- "이 에러가 무슨 뜻인지 설명해줘"를 먼저 요청
- 원인을 이해한 후 "이 원인을 기반으로 수정해줘" 요청

### 2. 모호한 요청 (Vague Prompting)

**증상**: "좋은 웹사이트 만들어줘", "이거 좀 고쳐줘"
**문제**: AI가 자기 맘대로 가정하고 엉뚱한 방향으로 진행
**해결**:
- **무엇을**: 구체적인 기능/변경 사항
- **왜**: 목적과 배경
- **어디에**: 어떤 파일, 어떤 부분
- **제약**: 사용할 기술, 스타일, 제한사항

### 3. 무비판적 수용 (Rubber-Stamping)

**증상**: AI가 만든 코드를 검토 없이 그대로 사용
**문제**: 숨겨진 버그, 보안 취약점, 불필요한 복잡성 누적
**해결**:
- "이 코드를 비개발자도 이해할 수 있게 설명해줘" 요청
- "이 코드에 잠재적 문제가 있는지 리뷰해줘" 요청
- 변경사항이 뭔지 diff를 확인하는 습관

### 4. 컨텍스트 생략 (Missing Context)

**증상**: 프로젝트 구조, 기존 코드, 비즈니스 규칙을 알려주지 않음
**문제**: AI가 프로젝트와 맞지 않는 코드 생성
**해결**:
- 관련 파일을 먼저 읽게 하기
- CLAUDE.md에 프로젝트 컨벤션 정리
- "현재 코드 구조를 파악한 후에 작업해줘" 요청

### 5. 한꺼번에 요청 (Kitchen Sink Request)

**증상**: "로그인, 대시보드, 결제, 알림 기능 다 만들어줘"
**문제**: 각 기능이 대충 만들어지고, 연결 부분에서 문제 발생
**해결**:
- 한 번에 한 기능씩 요청
- 각 기능이 완성되면 테스트 후 다음으로
- 큰 작업은 단계로 나눠서 요청

### 6. 가정 전파 (Assumption Propagation)

**증상**: AI가 초반에 잘못된 가정을 하고 그 위에 계속 쌓아감
**문제**: 나중에 발견하면 전체를 뜯어고쳐야 함
**해결**:
- 첫 구현 후 방향이 맞는지 확인
- "진행하기 전에 네가 이해한 걸 정리해줘" 요청
- 중간중간 검증 포인트 설정

### 7. 이해 부채 (Comprehension Debt)

**증상**: 코드가 잘 돌아가지만 왜 돌아가는지 모름
**문제**: 문제가 생기면 대응 불가, 유지보수 불가
**해결**:
- "이 코드의 핵심 로직을 초보자 수준으로 설명해줘" 요청
- 주요 결정 사항을 메모로 남기기
- 코드 리뷰를 AI에게 요청해서 설명 듣기

### 8. 죽은 코드 방치 (Dead Code Accumulation)

**증상**: 여러 번 수정하면서 사용하지 않는 코드가 쌓임
**문제**: 코드가 점점 복잡해지고, 나중에 뭐가 뭔지 모름
**해결**:
- 주기적으로 "사용하지 않는 코드를 정리해줘" 요청
- 큰 변경 후 "코드 정리(cleanup)해줘" 요청

---

## 위험 신호 체크리스트

아래 항목 중 3개 이상 해당되면 멈추고 회고가 필요합니다:

- [ ] 같은 에러가 3번 이상 반복된다
- [ ] AI 대화가 20턴 이상 지속되는데 해결이 안 된다
- [ ] 코드가 왜 이렇게 생겼는지 설명할 수 없다
- [ ] "일단 돌아가니까" 하고 넘어간 적이 있다
- [ ] AI에게 "전체를 다시 만들어줘"를 요청하고 싶다
- [ ] 에러 메시지를 읽지 않고 바로 붙여넣기 한다
- [ ] 어제 만든 코드를 오늘 이해할 수 없다

## 출처

- [The 80% Problem in Agentic Coding (Addy Osmani)](https://addyo.substack.com/p/the-80-problem-in-agentic-coding)
- [Beyond Vibe Coding (Addy Osmani)](https://beyond.addy.ie/)
- [Newer AI Coding Assistants Are Failing in Insidious Ways (IEEE Spectrum)](https://spectrum.ieee.org/ai-coding-degrades)
- [Debugging AI-Generated Code: 8 Failure Patterns (Augment Code)](https://www.augmentcode.com/guides/debugging-ai-generated-code-8-failure-patterns-and-fixes)
- [The Real Struggle with AI Coding Agents (Smiansh)](https://www.smiansh.com/blogs/the-real-struggle-with-ai-coding-agents-and-how-to-overcome-it/)
