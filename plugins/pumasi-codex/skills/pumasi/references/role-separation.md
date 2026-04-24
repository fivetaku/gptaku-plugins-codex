# lead agent vs Codex 역할 분리

## lead agent가 제공하는 것 (instruction에 포함)

```
✅ 타입/인터페이스 정의 (body 없이)
✅ 함수/클래스 시그니처 (body 없이)
✅ 요구사항 (자연어, 구체적)
✅ 제약사항 (라이브러리명, 스타일 규칙, 금지사항)
✅ 필수 import 라인 (라이브러리 강제용, 1~2줄)
✅ 데이터 모델/스키마 정의
✅ 기존 코드 참조 경로 (reference_files)
✅ 프로젝트 컨텍스트 (기술 스택, 디렉토리 구조)
```

## Codex가 구현하는 것 (lead agent가 작성 금지)

```
❌ 함수/메서드 본문 (body)
❌ 컴포넌트 렌더링 로직 (JSX/HTML)
❌ 비즈니스 로직 구현
❌ CSS/스타일 코드
❌ 이벤트 핸들러 구현
❌ API 호출 로직
❌ 데이터 변환/처리 로직
```

## 경계선 예시

```
lead agent가 주는 것:
  export function generateToken(userId: string, role: string): string
  - jsonwebtoken 사용 (필수 import: import jwt from 'jsonwebtoken')
  - 만료: 7일
  - secret: process.env.JWT_SECRET

Codex가 구현하는 것:
  export function generateToken(userId: string, role: string): string {
    return jwt.sign({ userId, role }, process.env.JWT_SECRET!, { expiresIn: '7d' })
  }
```

lead agent는 **위쪽만** 작성한다. 아래쪽은 Codex가 채운다.
