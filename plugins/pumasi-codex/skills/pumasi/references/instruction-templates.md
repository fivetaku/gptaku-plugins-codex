# instruction 템플릿

## 기본 템플릿

```
{절대경로}에 다음 파일들을 구현하세요.

## 프로젝트 컨텍스트
- 기술 스택: {언어, 프레임워크, 버전}
- 스타일: {ESM/CJS, strict mode 등}
- 패키지 매니저: {bun/pnpm/npm}

## 생성할 파일 목록
- {경로1} — {역할}
- {경로2} — {역할}

## 공통 타입 (다른 서브태스크와 공유)
```typescript
// 타입/인터페이스만 (body 없이)
interface SharedType { ... }
```

## 파일별 상세

### {경로1}
역할: {이 파일의 역할}

시그니처:
```typescript
export function functionName(param: Type): ReturnType
export class ClassName {
  method(param: Type): ReturnType
}
```

요구사항:
- {구체적 동작 1 — 자연어로}
- {구체적 동작 2 — 자연어로}
- 라이브러리: {이름} (필수 import: {import 문 1줄})

## 금지사항
- 위에 정의되지 않은 파일 생성 금지
- 함수 시그니처 변경 금지
- 지정되지 않은 라이브러리 사용 금지

## 완료 보고
구현 완료 후 다음을 보고하세요:
- 생성된 파일 경로 목록
- 각 함수/클래스의 실제 구현 방식 요약
- 주요 설계 결정사항
```

---

## 좋은 instruction vs 나쁜 instruction

```
❌ 나쁜 instruction (lead agent가 코드를 다 씀):
  instruction: |
    IndexCard.tsx를 구현하세요.
    ```tsx
    export default function IndexCard({ value, change }: Props) {
      const isPositive = change >= 0
      const color = isPositive ? 'text-green-400' : 'text-red-400'
      return (
        <div className="bg-gray-900 rounded-lg p-6">
          <span className="text-4xl">{value.toFixed(1)}</span>
          <span className={color}>{change}</span>
        </div>
      )
    }
    ```
    위 코드를 그대로 작성하세요.

→ lead agent가 이미 토큰을 다 소비함. Codex는 복사만.

✅ 좋은 instruction (Codex가 구현함):
  instruction: |
    src/components/dashboard/IndexCard.tsx를 구현하세요.

    시그니처:
    interface IndexCardProps { value: number; change: number; changePct: number }
    export default function IndexCard(props: IndexCardProps): JSX.Element

    요구사항:
    - 영향력 지수를 크게 표시 (text-4xl 정도)
    - change가 양수면 녹색 ▲, 음수면 빨간색 ▼ 표시
    - changePct를 소수 2자리로 표시
    - Tailwind CSS, 다크 테마 (bg-gray-900 기반)
    - 스케일 안내 텍스트: "0~1000 스케일 | 가중 기하평균 기반"

→ lead agent 토큰 소량. Codex가 실제 구현.
```

---

## instruction 자기 점검 (Phase 2 작성 후)

```
□ instruction에 10줄 이상의 코드 블록이 있는가? → 있으면 삭제
□ "그대로 작성하세요"가 있는가? → 있으면 요구사항으로 변환
□ 함수 본문(body)을 작성했는가? → 시그니처만 남기기
□ tsc/build 게이트가 있는가? → 없으면 추가
□ 제약사항에 라이브러리 강제가 있는가? → 없으면 추가
```
