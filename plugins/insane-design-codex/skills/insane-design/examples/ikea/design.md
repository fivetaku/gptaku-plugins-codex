---
slug: ikea
service_name: IKEA
site_url: https://www.ikea.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#FFDB00"
primary_font: Noto IKEA
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — IKEA (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 IKEA처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Noto IKEA", "Noto Sans", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFEFB; --fg: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 노랑 */
:root { --brand: #FFDB00; }
```

**절대 하지 말아야 할 것 하나**: IKEA CTA 버튼을 파란색으로 만드는 것. IKEA 마케팅 사이트의 주요 CTA는 노랑(#FFDB00) 배경 + 검정 텍스트다. 파란색(#0058A3)은 정보 링크에만 사용된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.ikea.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | N/A (CSS Modules + Svelte scoped) |
| Method | selector_role 파싱 · frequency 분석 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Svelte / SvelteKit (`.svelte-*` scoped hash 패턴 감지)
- **Design system**: 인-하우스 (`.btn-color-primary`, `.btn-color-secondary` 클래스)
- **CSS architecture**: BEM-like global 클래스 + Svelte scoped
- **Default theme**: light (#FFFEFB 따뜻한 near-white)
- **Font loading**: 자체 호스트 — Noto IKEA (IKEA 커스텀, Noto Sans 기반)
- **Notable**: 버튼 3종 명시적 정의 (primary=검정, secondary=흰, disabled=gray)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary**: `Noto IKEA` (Noto Sans 기반 IKEA 커스텀 폰트)
- **Fallback**: `Noto Sans`, `Helvetica Neue`, `Arial`, sans-serif
- **Weight**: `400` (normal), `700` (bold), `800` (extra bold)

```css
body {
  font-family: "Noto IKEA", "Noto Sans", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}
h1, h2, .headline {
  font-weight: 700;
}
.display {
  font-weight: 800;
}
```

> **라이선스 주의**: Noto IKEA 재배포 불가. 대체재: `Noto Sans` (Google Fonts) — 매우 유사한 모양.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Display | Noto IKEA | 48–72px | 800 | 1.05 | -0.01em |
| Section H2 | Noto IKEA | 28–40px | 700 | 1.2 | -0.005em |
| Card Title | Noto IKEA | 18–22px | 700 | 1.3 | 0 |
| Body | Noto IKEA | 14–16px | 400 | 1.65 | 0 |
| Price | Noto IKEA | 18–24px | 700 | 1 | 0 |
| Caption | Noto IKEA | 12–13px | 400 | 1.4 | 0 |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Palette

| 이름 | Hex | 용도 |
|---|---|---|
| IKEA Yellow | `#FFDB00` | CTA 버튼, 브랜드 identity (frequency top chromatic) |
| Yellow Alt | `#F7DA06` | 미세 variant |
| IKEA Blue | `#0058A3` | 정보 링크, 포커스 상태 |
| Blue Dark | `#003B7D` | 다크 블루 variant |
| Near-Black | `#111111` | 본문 텍스트 (most frequent neutral) |
| Black | `#000000` | 버튼 텍스트, 강조 |

### Surface Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Warm White | `#FFFEFB` | 페이지 배경 (warm near-white) |
| Off-White | `#F5F5F5` | 카드, 버튼 hover |
| Light Gray | `#F1F2F0` | 섹션 배경 |
| Mid Gray | `#DFDFDF` | 경계선, 버튼 secondary hover |
| Text Gray | `#818181` | disabled 텍스트 |
| Light Border | `#CCCCCC` | 모바일 메뉴 경계 |

### Semantic Button Colors (CSS에서 직접 추출)

| 역할 | 배경 | 텍스트 |
|---|---|---|
| Primary (btn-color-primary) | `#111111` (검정) | `#FFFFFF` |
| Primary Hover | `#333333` | `#FFFFFF` |
| Primary Active | `#000000` | `#FFFFFF` |
| Secondary | `#FFFFFF` | `#111111` |
| Secondary Hover | `#F5F5F5` | - |
| Disabled | `#DADADA` | `#818181` |

> **Note**: IKEA.com에서 primary 버튼은 검정, 노랑은 특별 CTA에 사용. 일반 e-commerce 버튼은 검정 우선.

---

## 07. Spacing
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘·배지 |
| sm | 8px | 인라인 요소 |
| md | 16px | 카드 내부 |
| lg | 24px | 섹션 내부 |
| xl | 40px | 섹션 간격 |
| 2xl | 64px | 주요 섹션 |
| 3xl | 80px | hero 패딩 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| none | 0px | 대부분 카드, IKEA 각진 스타일 |
| sm | 2px | 미세 라운딩 |
| md | 4px | 버튼, 폼 |
| lg | 8px | 모달, 드롭다운 |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card | `0 2px 8px rgba(0,0,0,.1)` | 제품 카드 |
| nav | `0 1px 4px rgba(0,0,0,.12)` | 고정 네비게이션 |
| focus | `inset 0 0 0 1px #111, inset 0 0 0 3px #fff, inset 0 0 0 4px #111` | 포커스 링 (접근성) |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 200ms | hover 전환 |
| duration-base | 300ms | 드롭다운, 메뉴 |
| easing | `ease-out` | 요소 등장 |
| box-shadow-transition | `0.2s ease-out` | 포커스 링 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **최대 너비**: 1440px, 콘텐츠 영역 1200px
- **Product Grid**: 4-col desktop, 2-col tablet, 1-col mobile (각진 카드)
- **Hero**: full-width 이미지 + 오버레이 텍스트 또는 2-col 분할
- **Navigation**: 수평 mega menu, 배경 흰색 고정
- **Family Navigation**: 상단 thin strip (0.0625rem 보더)

---

## 12. Components
<!-- SOURCE: manual -->

### 버튼 Primary (검정)

```css
/* .btn-color-primary — CSS에서 직접 추출 */
.btn-primary {
  background: #111111;
  color: #FFFFFF;
  font-family: "Noto IKEA", "Noto Sans", Arial, sans-serif;
  font-size: 14px; font-weight: 700;
  padding: 12px 24px;
  border-radius: 4px;
  border: none; cursor: pointer;
  transition: background 200ms;
}
.btn-primary:hover { background: #333333; }
.btn-primary:active { background: #000000; }
```

### 버튼 Yellow CTA (IKEA 시그니처)

```css
.btn-yellow {
  background: #FFDB00;
  color: #111111;
  font-size: 14px; font-weight: 700;
  padding: 12px 24px;
  border-radius: 4px;
  border: none; cursor: pointer;
  transition: background 200ms;
}
.btn-yellow:hover { background: #F7DA06; }
```

### 제품 카드

```css
.product-card {
  background: #FFFFFF;
  border-radius: 0; /* IKEA 각진 스타일 */
  overflow: hidden;
}
.product-card__name {
  font-size: 16px; font-weight: 700; color: #111111;
  margin-bottom: 4px;
}
.product-card__desc { font-size: 14px; color: #111111; }
.product-card__price { font-size: 20px; font-weight: 700; color: #111111; }
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: "Bring ideas to life" — 제품이 아닌 라이프스타일 중심
- **제품명**: 스웨덴어 고유명사 (KALLAX, BILLY, POÄNG)
- **가격**: 큰 폰트, 세금/할인 명시
- **CTA**: "Add to cart" / "Buy online" / "Find in store"
- **톤**: 실용적·민주적 디자인 ("For the many people")

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand */
  --brand-yellow: #FFDB00;
  --brand-yellow-alt: #F7DA06;
  --brand-blue: #0058A3;
  --brand-blue-dark: #003B7D;

  /* Surface */
  --bg: #FFFEFB;
  --bg-card: #FFFFFF;
  --fg: #111111;
  --fg-muted: #818181;

  /* UI */
  --btn-primary-bg: #111111;
  --btn-primary-hover: #333333;
  --border: #DFDFDF;
  --border-light: #CCCCCC;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 40px;
  --space-2xl: 64px;

  /* Radius */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
}

body {
  font-family: "Noto IKEA", "Noto Sans", "Helvetica Neue", Arial, sans-serif;
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
        'brand-yellow': '#FFDB00',
        'brand-blue': '#0058A3',
        'near-black': '#111111',
        'warm-white': '#FFFEFB',
        'gray-muted': '#818181',
        'border-default': '#DFDFDF',
      },
      fontFamily: {
        sans: ['"Noto IKEA"', '"Noto Sans"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '4px',
        none: '0',
        sm: '2px',
        lg: '8px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- **CTA yellow 버튼은 #FFDB00** + 검정 텍스트 조합 — IKEA 시그니처
- **일반 primary 버튼은 검정(#111111)** — 파란색이 아닌 검정 우선
- **배경은 따뜻한 near-white #FFFEFB** — 순백(#FFFFFF) 대신
- **제품 카드는 border-radius 0** — 각진 디자인이 IKEA 실용성
- **포커스 링은 3중 inset shadow** — 접근성 최우선

### DON'T

- **파란(#0058A3)을 CTA primary로 쓰지 않는다** — 정보 링크 전용
- **노랑(#FFDB00)을 배경으로 전면 사용하지 않는다** — 포인트 컬러 역할
- **border-radius 16px 이상 쓰지 않는다** — IKEA는 실용적 각진 스타일
- **화려한 그라디언트 쓰지 않는다** — 단색, 단순함이 브랜드 원칙
- **Noto IKEA weight 300으로 쓰지 않는다** — 가독성 위해 400 이상
