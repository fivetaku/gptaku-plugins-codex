# 실행 예시

## 예시: Todo 앱 (PM 기획 포함)

```
사용자: "품앗이로 Todo 앱 만들어줘"

[Phase 0] lead agent 기획:
→ 기능 설계 + 데이터 모델 + 기획안 → 사용자 승인

[Phase 1] lead agent 태스크 분해:
Round 1 (병렬):
  - task1: 백엔드 DB + API
    → 시그니처: createTodo(), getTodos(), updateTodo(), deleteTodo()
    → 라이브러리: better-sqlite3, Hono
    → Todo 타입 정의 제공
  - task2: 프론트엔드 컴포넌트
    → 시그니처: TodoItem, AddTodo, FilterBar, StatsBar
    → 요구사항: 인라인 수정, 우선순위 색상, 검색
  - task3: 프론트엔드 설정 + 공통 유틸리티
    → Vite + React 19 + Tailwind 4 설정
    → 공통 fetch 래퍼, 타입 export
Round 2 (후속):
  - task4: 캘린더 뷰 + 드래그 앤 드롭

[Phase 2] 공유 상태 초기화:
python3 scripts/init_workspace.py --root "$PWD" --task "Todo 앱"

[Phase 3] .pumasi/tasks/에 작업 브리프 작성:
- owned files
- required signatures
- constraints
- gate commands

[Phase 4] spawn_agent로 worker를 병렬 실행
[Phase 5] lead agent가 게이트 검증 (tsc -> build -> test)
[Phase 6] 통합 + 완성
```

## 적정 분해 예시 (인증 시스템)

```
Round 1 (병렬):
  task1: JWT 토큰 유틸리티 (auth/token.ts)
  task2: 비밀번호 해싱 유틸리티 (auth/password.ts)
  task3: 사용자 모델 + DB 스키마 (models/user.ts)
Round 2 (후속):
  task4: 인증 API 엔드포인트 (routes/auth.ts) ← task1,2,3 완료 후
```

## .pumasi/tasks 브리프 예시

```markdown
# token-utils

## Owned files

- src/auth/token.ts

## Signatures

- export function generateToken(userId: string, role: string): string
- export function verifyToken(token: string): { userId: string; role: string } | null

## Requirements

- jsonwebtoken 라이브러리 사용 (다른 라이브러리로 대체 금지)
- 필수 import: import jwt from 'jsonwebtoken'
- 만료 시간: 7일
- secret: process.env.JWT_SECRET
- verifyToken은 만료/무효 토큰에 null 반환
- TypeScript strict mode, ESM
- 에러 시 throw 대신 null 반환

## Gates

- npx tsc --noEmit src/auth/token.ts
- grep -q 'jsonwebtoken' src/auth/token.ts
- grep -q 'generateToken' src/auth/token.ts && grep -q 'verifyToken' src/auth/token.ts
```
