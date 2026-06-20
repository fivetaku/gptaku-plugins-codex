# Apply Workflow Reference

## design.md 파싱 규칙

### Frontmatter 필수 필드
| 필드 | 용도 | fallback |
|------|------|----------|
| `brand_color` | 브랜드 컬러 선택지 | `#18181b` |
| `primary_font` | 폰트 선택지 | `system-ui` |
| `font_weight_normal` | weight 선택지 | `400` |
| `default_theme` | light/dark 판단 | `light` |

### §15 Drop-in CSS 추출
1. `## 15.` 또는 `## 15 ` 패턴으로 섹션 시작 찾기
2. 다음 ` ```css ` 블록의 내용 추출
3. `:root { }` 블록과 `body { }` 블록 분리
4. 각 `--변수명: 값;` 쌍을 파싱

### §01 Quick Start 추출
1. `## 01.` 패턴으로 섹션 찾기
2. ` ```css ` 블록에서 `/* 1. */`, `/* 2. */`, `/* 3. */` 기준 3개 스텝 분리
3. 각 스텝의 CSS 속성-값 추출

---

## 프로젝트 스캔 규칙

### CSS 파일 탐색 순서
```
src/app/globals.css
app/globals.css
src/styles/globals.css
styles/global.css
src/index.css
app.css
src/global.css
```

### Tailwind 감지
```
tailwind.config.js
tailwind.config.ts
tailwind.config.mjs
tailwind.config.cjs
```

### 스택 판별
| 발견 | 판정 |
|------|------|
| tailwind.config.* 존재 | Tailwind 프로젝트 |
| package.json에 tailwindcss | Tailwind 프로젝트 |
| CSS 파일만 존재 | Plain CSS 프로젝트 |
| 아무것도 없음 | 사용자에게 경로 입력 요청 |

---

## 토큰 주입 규칙

### CSS 변수 주입 (Edit 도구)
- 기존 `:root { }` 있으면 → 블록 내부에 추가
- 없으면 → 파일 최상단에 새 `:root { }` 생성
- 주석으로 출처 표시: `/* insane-design: {slug} */`

### Tailwind 주입 (Edit 도구)
- `theme.extend.colors` 에 브랜드/neutral 추가
- `theme.extend.fontFamily` 에 폰트 추가
- `theme.extend.borderRadius` 에 라디우스 추가

### 충돌 처리
- 동일 변수명이 이미 있으면 → 값 교체 (old→new)
- 새 변수면 → append
- `/* insane-design */` 주석 블록이 이미 있으면 → 해당 블록 전체 교체 (재적용)
