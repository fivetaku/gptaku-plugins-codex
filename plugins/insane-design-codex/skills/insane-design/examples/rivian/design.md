---
slug: rivian
service_name: Rivian
site_url: https://rivian.com
fetched_at: 2026-04-13
default_theme: mixed
brand_color: "#465243"
primary_font: Adventure
font_weight_normal: 400
token_prefix: --surface-*
---

# DESIGN.md — Rivian (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Rivian처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Adventure", "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #465243; }
```

**절대 하지 말아야 할 것 하나**: Rivian을 테슬라처럼 순흑/순백 모노크롬으로 만드는 것. Rivian의 정체성은 어스 톤(earth tone)이다. `#E6E5DF`(따뜻한 오프화이트)와 `#465243`(어두운 포레스트 그린)이 실제 사이트의 feel을 만든다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://rivian.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Tailwind v4 기반 (CSS custom properties 다수) |
| Token prefix | `--surface-*`, `--text-*`, `--stroke-*`, `--font-adventure` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (Tailwind v4 시그너처 감지)
- **Design system**: Rivian 자체 시스템 — prefix `--surface-*`, `--text-*`, `--stroke-*`
- **CSS architecture**: Tailwind v4 + CSS 커스텀 프로퍼티 semantic layer
  ```
  semantic  (--surface-primary, --text-primary, --stroke-primary)  light/dark 교체
  utility   (--font-adventure, --font-adventure-mono)               폰트 참조
  ```
- **Class naming**: Tailwind utility + `rivian-css-*` 해시 패턴
- **Default theme**: mixed (light 기본, dark 섹션 교차)
- **Font loading**: 자체 호스트 (`Adventure`, `Adventure Mono`)
- **Canonical anchor**: `#465243` — 어스 톤 forest green, chromatic 중 가장 브랜드 정체성에 부합

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Adventure` (Rivian 전용)
- **Mono font**: `Adventure Mono` (Rivian 전용)
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --font-adventure: Adventure;
  --font-adventure-mono: "Adventure Mono";
}
body {
  font-family: var(--font-adventure), ui-sans-serif, system-ui, sans-serif;
  font-weight: 400;
}
```

> **라이선스 주의**: `Adventure` 폰트는 Rivian 전용. 외부 프로젝트에서는 `DM Sans` 또는 `Manrope`가 시각적으로 유사.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Earth Tone)

| Token | Hex |
|---|---|
| forest green (brand) | `#465243` |
| warm off-white | `#E6E5DF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| amber accent | `#FFAC00` |
| red-orange accent | `#E84826` |

### 06-3. Neutral Ramp

| Step | Light (`--surface-primary`) | Dark (`--surface-primary` dark) |
|---|---|---|
| primary surface | `#FFFFFF` | `#000000` |
| primary alt | `#FAFAFA` | `#151515` |
| primary text | `#000000` | `#FFFFFF` |
| invert surface | `#000000` | `#FFFFFF` |
| mid gray | `#CBCBCB` | — |
| dark gray | `#494949` | — |
| off-white | `#F2F2F2` | — |
| near-black | `#151515` | — |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Forest Green | brand | `#465243` |
| Warm Off-white | surface alt | `#E6E5DF` |
| Amber | interior accent | `#FFAC00` |
| Red-Orange | alert/accent | `#E84826` |
| Steel Blue-Gray | video player | `#73859F` |
| Muted Blue | info | `#8BA8BD` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--surface-primary` (light) | `#FFFFFF` | 라이트 테마 배경 |
| `--surface-primaryAlt` (light) | `#FAFAFA` | 라이트 테마 배경 대안 |
| `--surface-primary` (dark) | `#000000` | 다크 테마 배경 |
| `--surface-primaryAlt` (dark) | `#151515` | 다크 테마 배경 대안 |
| `--text-primary` (light) | `#000000` | 라이트 테마 텍스트 |
| `--text-primary` (dark) | `#FFFFFF` | 다크 테마 텍스트 |
| `--stroke-primary` (light) | `#000000` | 라이트 테마 테두리 |
| `--stroke-primary` (dark) | `#FFFFFF` | 다크 테마 테두리 |
| `rivian-css-i5r634:link` | `#151515` | 링크 컬러 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--surface-primary` | `#FFFFFF` / `#000000` | 테마에 따라 교체 |
| `--text-primary` | `#000000` / `#FFFFFF` | 테마에 따라 교체 |
| `--stroke-primary` | `#000000` / `#FFFFFF` | 테마에 따라 교체 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 70 | 라이트 테마 배경/텍스트 |
| 2 | `#000000` | 43 | 다크 배경/텍스트 |
| 3 | `#00000000` | 35 | 투명 |
| 4 | `#F2F2F2` | 20 | 밝은 배경 섹션 |
| 5 | `#151515` | 18 | near-black |
| 6 | `#CBCBCB` | 13 | 중간 회색 |
| 7 | `#494949` | 11 | 다크 회색 |
| 8 | `#E6E5DF` | 11 | warm off-white (earth tone) |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| video player button | `2px` | `.vjs-track-settings-controls button` |

---

## 09. Shadows
<!-- SOURCE: auto -->

> N/A — shadow 토큰이 CSS에서 추출되지 않음.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Navigation

```html
<a class="rivian-css-i5r634" href="/us/en">
  Home
</a>
```

| 속성 | 값 |
|---|---|
| color | `#151515` |
| font-family | `Adventure` |

### Hero (Light + Earth Tone)

```html
<section class="hero" style="background: #E6E5DF;">
  <div class="hero__content">
    <h1>R1T</h1>
    <div class="hero__ctas">
      <a href="#" class="btn btn--primary">주문하기</a>
      <a href="#" class="btn btn--secondary">자세히 보기</a>
    </div>
  </div>
</section>
```

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 모델명 간결, 어드벤처 감성 | "R1T. Go further." |
| Primary CTA | 행동형 | "Order Now" / "주문하기" |
| Secondary CTA | 탐색형 | "Learn More" |
| Subheading | 자연/어드벤처 감성 + 스펙 | "Up to 410+ miles of range" |
| Tone | 어드벤처, 지속가능성, 미래지향 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Rivian — copy into your root stylesheet */
:root {
  /* Fonts */
  --rivian-font-family: Adventure, "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --rivian-font-family-mono: "Adventure Mono", ui-monospace, monospace;
  --rivian-font-weight-normal: 400;
  --rivian-font-weight-bold: 600;

  /* Brand (earth tone) */
  --rivian-color-brand-green: #465243;
  --rivian-color-earth-white: #E6E5DF;
  --rivian-color-amber: #FFAC00;

  /* Surfaces */
  --rivian-bg-page: #FFFFFF;
  --rivian-bg-earth: #E6E5DF;
  --rivian-bg-dark: #000000;
  --rivian-bg-near-black: #151515;
  --rivian-text: #000000;
  --rivian-text-muted: #494949;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Rivian
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          green: '#465243',
          earth: '#E6E5DF',
          amber: '#FFAC00',
        },
        neutral: {
          900: '#000000',
          800: '#151515',
          700: '#494949',
          300: '#CBCBCB',
          100: '#F2F2F2',
          50: '#FAFAFA',
        },
      },
      fontFamily: {
        sans: ['Adventure', '"HelveticaNeue"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
        mono: ['"Adventure Mono"', 'ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold: '600',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 어스 톤 `#E6E5DF`(따뜻한 오프화이트)를 배경 섹션에 사용
- 브랜드 그린 `#465243`을 절제적인 accent로 사용
- light/dark 테마를 `--surface-primary`, `--text-primary` 변수로 교체
- 폰트는 `Adventure` — 없으면 `DM Sans` 또는 `Manrope`

### ❌ DON'T
- 순흑/순백 모노크롬만으로 레이아웃 구성하지 말 것
- Amber `#FFAC00`을 primary CTA에 쓰지 말 것 — 인테리어 조명 accent
- 브랜드 그린을 배경 전체에 깔지 말 것
- 순흑 `#000000` 대신 `#151515`(near-black)를 텍스트/dark 배경에 우선 사용
