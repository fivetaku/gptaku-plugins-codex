# Codex 특성 및 instruction 작성 가이드

> **Codex는 lead agent와 달리 맥락 추론이 약하다. 하지만 구현력은 충분하다.**
> **핵심: 무엇을(시그니처)과 어떻게(제약사항)를 명확히 주면 잘 구현한다.**

## lead agent vs Codex 비교

| 항목 | lead agent | Codex |
|------|--------|-------|
| 맥락 추론 | 잘함 | 약함 |
| 코드 구현 | 할 수 있지만 토큰 비쌈 | **빠르고 사용량 넉넉** |
| 파일 경로 | 상대경로 OK | **절대경로 필수** |
| 라이브러리 | 추천 가능 | **지정 필수** (안 하면 대체함) |
| 함수 시그니처 | 자유 설계 | **정확히 지정 필수** |

## Codex가 라이브러리를 대체하는 문제

"better-sqlite3 사용"이라고만 쓰면 Codex가 더 쉬운 방법(JSON 파일 등)으로 대체할 수 있다.

**해결 방법 (코드 전체를 주지 않고):**

```
❌ 나쁜 해결 (코드 전체 제공 — 안티패턴):
  instruction에 DB 초기화 코드 30줄을 그대로 작성

✅ 좋은 해결 (제약사항 + 게이트 강화):
  instruction:
    - 라이브러리: better-sqlite3 (JSON/fs 등 다른 방식 사용 절대 금지)
    - 필수 import: import Database from 'better-sqlite3'
    - DB 파일: ./data.db

  gates:
    - name: "better-sqlite3 사용 확인"
      command: "grep -q 'better-sqlite3' src/db.ts && ! grep -q 'readFileSync' src/db.ts"
    - name: "타입 체크"
      command: "npx tsc --noEmit src/db.ts"
```

**원칙: 코드를 주지 말고, 제약사항을 주고 게이트로 검증하라.**

## Codex에게 효과적인 instruction 규칙

```
✅ DO (lead agent가 instruction에 포함할 것):
- 절대 경로로 파일 위치 명시
- 함수/클래스 시그니처 (body 없이)
- 타입/인터페이스 정의
- 사용할 라이브러리명 + 필수 import 1줄
- 자연어 요구사항 (구체적으로)
- 금지사항 (다른 라이브러리 대체 금지 등)
- 생성할 파일 목록
- 코딩 스타일 (ESM/CJS, strict mode 등)

❌ DON'T (lead agent가 instruction에 포함하지 말 것):
- 함수/컴포넌트의 본문(body) 코드
- JSX/HTML 렌더링 마크업
- 비즈니스 로직 구현 코드
- CSS/스타일 구현 코드
- "위 코드를 그대로 작성하세요" 지시
- 10줄 이상의 코드 블록
- 설정 파일 전체 내용 (핵심 설정값만 전달)
```
