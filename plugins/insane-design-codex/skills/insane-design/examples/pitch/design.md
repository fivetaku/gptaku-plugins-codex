---
slug: pitch
service_name: Pitch
site_url: https://pitch.com
fetched_at: 2026-04-13
default_theme: mixed
brand_color: "#6B53FF"
primary_font: Eina01
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Pitch (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Pitch처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Eina01", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #2B2A35; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 블루퍼플 */
:root { --brand: #6B53FF; }
```

**절대 하지 말아야 할 것 하나**: 단색 purple을 CTA로 쓰고 그라디언트를 생략하는 것. Pitch의 브랜드 핵심은 `linear-gradient(90deg, #8D49F7, #6B53FF)` 그라디언트다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://pitch.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | N/A (CSS Modules hashed classname `.style_*`) |
| Method | selector_role 직접 파싱 · frequency 분석 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (CSS Modules, `.style_navigation__831Nr` 패턴)
- **Design system**: 인-하우스 (CSS Modules 기반)
- **CSS architecture**: CSS Modules — `.style_{컴포넌트}__{해시}` 네이밍
- **Default theme**: mixed (마케팅 페이지 light/dark 교차, 앱 내부는 별개)
- **Font loading**: 자체 호스트 — Eina01 (primary), Mark Pro (display)
- **Notable**: 버튼 그라디언트 3종 (purple, orange, blurple)이 CSS에 직접 노출

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary UI**: `Eina01` (Atipo Foundry, 유료) — body, UI, 대부분의 텍스트
- **Display / Headlines**: `Mark Pro` (Hannes von Döhren, 유료)
- **Weight normal / bold**: `400` / `700–800`

```css
body {
  font-family: "Eina01", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-weight: 400;
}
h1, h2, .headline {
  font-family: "Mark Pro", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 800;
}
```

> **라이선스 주의**: Eina01 유료. 대체재: `Nunito Sans` 또는 `Outfit` (Google Fonts). Mark Pro → `Plus Jakarta Sans`.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero H1 | Mark Pro | 56–80px | 800–950 | 1.05 | -0.02em |
| Section H2 | Mark Pro | 36–48px | 800 | 1.1 | -0.015em |
| Card Title | Eina01 | 20–24px | 700 | 1.25 | -0.01em |
| Body | Eina01 | 16–18px | 400 | 1.65 | 0 |
| Small / Caption | Eina01 | 13–14px | 400 | 1.5 | 0 |
| Label | Eina01 | 12px | 600 | 1 | 0.04em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Palette (CSS selector에서 직접 추출)

| 이름 | Hex | 용도 |
|---|---|---|
| Blurple (CTA) | `#6B53FF` | 주요 CTA 버튼, 링크, 그라디언트 끝 |
| Purple | `#8D49F7` | 그라디언트 시작, 탭 active |
| Purple Deep | `#5318EB` | scrolled nav 배경, prompt 버튼 |
| Ink | `#2B2A35` | 본문 텍스트 (warm near-black) |
| Page BG | `#FFFFFF` | body 기본 배경 |
| Off-Black | `#1E1D28` | 다크 섹션 배경 |
| Muted | `#6F7387` | 비활성 텍스트 |

### 그라디언트 (핵심 브랜드 요소)

| 이름 | 값 | 용도 |
|---|---|---|
| Brand Gradient | `linear-gradient(90deg, #8D49F7, #6B53FF)` | 주요 CTA 버튼, 아웃라인 버튼 |
| Hover Gradient | `linear-gradient(90deg, #6B53FF, #8D49F7, #6B53FF)` | 버튼 hover animation |
| Nav Dark | `background: #8D49F7 linear-gradient(95.14deg, #8D49F7, #6B53FF 103.53%)` | 다크 네비게이션 |

---

## 07. Spacing
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘 간격 |
| sm | 8px | 인라인 요소 |
| md | 16px | 컴포넌트 패딩 |
| lg | 24px | 카드 패딩 |
| xl | 32px | 섹션 간격 |
| 2xl | 56px | 주요 섹션 |
| 3xl | 80px | hero 패딩 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| sm | 4px | 작은 배지 |
| md | 6px | 버튼, 폼 입력 |
| lg | 12px | 카드 |
| xl | 16px | 모달, 큰 카드 |
| pill | 999px | pill CTA |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card | `0 2px 15px rgba(103,110,144,.2), 0 0 0 1px rgba(103,110,144,.08)` | 카드, 드롭다운 |
| nav | `0 1px 0 rgba(0,0,0,.08)` | sticky nav |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 150ms | hover 전환 |
| duration-base | 300ms | 패널, 드롭다운 |
| duration-slow | 500ms | 섹션 진입 |
| easing | `ease-in-out` | 표준 전환 |
| gradient-anim | 10s infinite | 버튼 그라디언트 애니메이션 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **최대 너비**: 1200px, 좌우 패딩 15px (모바일 중심)
- **Hero**: full-viewport, 다크 그라디언트 배경 + 중앙 텍스트
- **Feature grid**: 교차 레이아웃 (텍스트 좌/이미지 우, 또는 반대)
- **Pricing**: 3-col 카드 (월/연간 토글)
- **탭 섹션**: 수평 탭 + 콘텐츠 패널

---

## 12. Components
<!-- SOURCE: manual -->

### CTA 버튼 (그라디언트)

```css
/* CSS에서 직접 추출: style_button__yXCPf.style_blue__d__3k */
.btn-primary {
  position: relative;
  overflow: hidden;
  background-image: linear-gradient(90deg, #8D49F7, #6B53FF);
  color: #FFFFFF;
  font-family: "Eina01", sans-serif;
  font-size: 16px; font-weight: 700;
  padding: 12px 24px;
  border-radius: 6px;
  border: none; cursor: pointer;
}
.btn-primary:hover {
  /* hover 시 그라디언트 반전 animation */
  background-image: linear-gradient(90deg, #6B53FF, #8D49F7, #6B53FF);
}
```

### Blurple 버튼 (solid)

```css
/* style_button__yXCPf.style_blurple__RG4l_ */
.btn-blurple {
  background-color: #6B53FF;
  color: #FFFFFF;
  font-weight: 700;
  padding: 10px 20px;
  border-radius: 6px;
}
```

### 아웃라인 버튼 (그라디언트 보더)

```css
/* style_button__yXCPf.style_outline__uoaH1 */
.btn-outline {
  position: relative;
  background-image: linear-gradient(90deg, #8D49F7, #6B53FF);
  padding: 2px; /* 보더 효과 */
  border-radius: 6px;
}
.btn-outline .inner {
  background: #FFFFFF;
  border-radius: 4px;
  padding: 10px 22px;
  color: #6B53FF;
  font-weight: 700;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: "Make slides people love" — 감성적 benefit 중심
- **서브**: 간결한 feature 설명, 2줄 이내
- **CTA**: "Try Pitch free" / "Get started" — 무료 강조
- **소셜 증명**: 숫자 + 회사명 로고 (trusted by X teams at Y)

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand */
  --brand: #6B53FF;
  --brand-dark: #8D49F7;
  --brand-deep: #5318EB;
  --brand-gradient: linear-gradient(90deg, #8D49F7, #6B53FF);

  /* Surface */
  --bg: #FFFFFF;
  --bg-dark: #1E1D28;
  --fg: #2B2A35;
  --fg-muted: #6F7387;

  /* Border */
  --border: #DDDFE5;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 56px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 12px;
  --radius-pill: 999px;
}

body {
  font-family: "Eina01", -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
  font-weight: 400;
  background: var(--bg);
  color: var(--fg);
  -webkit-font-smoothing: antialiased;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: '#6B53FF',
        'brand-purple': '#8D49F7',
        'brand-deep': '#5318EB',
        ink: '#2B2A35',
        'text-muted': '#6F7387',
        'bg-dark': '#1E1D28',
        'border-default': '#DDDFE5',
      },
      fontFamily: {
        sans: ['"Eina01"', '-apple-system', 'BlinkMacSystemFont', 'Helvetica', 'Arial', 'sans-serif'],
        display: ['"Mark Pro"', '-apple-system', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '6px',
        sm: '4px',
        lg: '12px',
        xl: '16px',
        pill: '999px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- **CTA는 반드시 그라디언트** `linear-gradient(90deg, #8D49F7, #6B53FF)` — 단색 금지
- **텍스트 잉크색은 #2B2A35** — 순흑(#000) 아닌 warm near-black
- **hover 시 그라디언트 반전** — 버튼 상태 표현에 그라디언트 방향 반전 활용
- **다크 hero 섹션에는 Nav 그라디언트** #8D49F7→#6B53FF 배경 사용
- **Eina01 weight 700 이상**으로 헤드라인 강조

### DON'T

- **단색 보라(#8D49F7 또는 #6B53FF) 하나만 쓰지 않는다** — 그라디언트가 핵심
- **주황 그라디언트(#FFD02C→#FF9E2C)를 primary로 쓰지 않는다** — 보조 강조 전용
- **폰트를 Inter로 대체할 때 차이를 모르면 안 된다** — Eina01은 독특한 곡선 있음
- **CSS Modules classname(`.style_*`)을 직접 참조하지 않는다** — 해시로 변경됨
- **배경 흰색에 보라 텍스트만 쓰지 않는다** — 배경과 CTA 그라디언트를 함께 구성
