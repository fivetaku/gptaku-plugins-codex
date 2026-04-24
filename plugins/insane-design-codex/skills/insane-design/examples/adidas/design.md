---
slug: adidas
service_name: adidas
site_url: https://adidas.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#000000"
primary_font: AdihausDIN
font_weight_normal: 400
token_prefix: --gl-*
---

# DESIGN.md — adidas (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 adidas처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: AdihausDIN, Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: adidas 디자인 시스템의 복잡한 토큰명 구조를 무시하고 단순히 `font-family: Arial`로 대체하는 것. adidas는 `--gl-body-font-set-family-functional-*`, `--gl-heading-font-set-family-standard-*` 등 정교한 타이포그래피 토큰 시스템을 사용하며, 각 컨텍스트마다 다른 폰트 변형이 지정되어 있다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://adidas.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 대규모 CSS (Global System + Stripes 컴포넌트 시스템) |
| Token prefix | `--gl-*` (Global Design System) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 마케팅 플랫폼, React 추정)
- **Design system**: adidas Global Design System (GDS) — prefix `--gl-*`
- **CSS architecture**: 다단계 토큰 계층
  ```
  gl-body       (--gl-body-font-set-family-functional-*)  body 타이포그래피
  gl-heading    (--gl-heading-font-set-family-standard-*) heading 타이포그래피
  gl-button     (--gl-button-font-set-family-functional-*)버튼 타이포그래피
  gl-tag        (--gl-tag-font-set-family-functional-*)   태그 타이포그래피
  cardproduct   (--cardproduct-main-onlight-*)            제품 카드
  ```
- **Class naming**: adidas Stripes system (`stripes_v7_gl-cta--*`, `_promo-banner_*_*` 해시 패턴)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스트 (`AdihausDIN`)
- **Canonical anchor**: `#000000` — 658회로 압도적 빈도 (SVG 패턴 포함)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `AdihausDIN` (adidas 독점)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --gl-font-family: AdihausDIN, Helvetica, Arial, sans-serif;
  --gl-font-family-fallback: Helvetica, Arial, sans-serif;
  --gl-font-weight-normal: 400;
  --gl-font-weight-bold: 700;
}
body {
  font-family: var(--gl-body-font-set-family-functional-4), var(--gl-font-family-fallback);
  font-weight: var(--gl-font-weight-normal);
}
```

> **라이선스 주의**: `AdihausDIN`은 adidas 독점. 외부 프로젝트에서는 `DIN Condensed` 또는 `Barlow Condensed`가 유사. `DIN Next LT Pro`가 가장 가깝다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 수치 토큰이 추출되지 않음.
> 타이포그래피 참조 구조: `--gl-body-font-set-family-functional-4` (36회), `--gl-heading-font-set-family-standard-9` (29회), `--gl-heading-font-set-family-standard-4` (15회) 등 16개 이상 변형.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Monochrome)

| Token | Hex |
|---|---|
| 브랜드 블랙 (primary) | `#000000` |
| 흰 배경 / 텍스트 on dark | `#FFFFFF` |

### 06-2. CTA Button States

| Token | Hex |
|---|---|
| primary ondark shadow | `#000000` |
| primary onlight shadow | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Hex | Count |
|---|---|---|
| 순흑 | `#000000` | 658 (SVG 포함) |
| 흰색 | `#FFFFFF` | 71 |
| 대안 배경 | `#ECEFF1` | 30 (SVG 포함) |
| 중간 회색 A | `#A0A0A0` | 6 |
| 중간 회색 B | `#A1A1A1` | 5 |
| 다크 회색 | `#767677` | 4 |
| 연한 배경 | `#F3F3F3` | 4 |
| 보더 회색 | `#D3D7DA` | 3 |
| 다크 회색 2 | `#464545` | 2 |
| 약한 회색 | `#C4C4C4` | 2 |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| 인터랙티브 블루 | focus | `#91C7ED` |
| 에러/경고 | red | `#E32B2B` |
| 프로모 | blue-gray | `#0066FF` |
| 성공 | green | `#408267` |
| 경고 | yellow | `#FFD200` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--icon-primary-color` | `#FFFFFF` | 아이콘 기본 색 (dark bg) |
| primary button shadow | `#FFFFFF` | drop shadow (dark bg) |
| `--backgrounds-gl-color-background-alternative` | `#ECEFF1` | 대안 섹션 배경 |
| focus outline | `#91C7ED` | 접근성 포커스 링 |
| hover CTA color | `#000000` | hover 텍스트 색 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000` | 658 | 브랜드 블랙 (SVG 포함) |
| 2 | `#FFFFFF` | 71 | 흰 배경/텍스트 |
| 3 | `#ECEFF1` | 30 | 대안 배경 (SVG 포함) |
| 4 | `#91C7ED` | 8 | 포커스 링 |
| 5 | `#A0A0A0` | 6 | 보조 텍스트 |
| 6 | `#A1A1A1` | 5 | 보조 텍스트 2 |
| 7 | `#0066FF` | 4 | 프로모 블루 |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 직접 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — radius 토큰이 CSS에서 추출되지 않음. adidas CTA 버튼은 drop shadow 패턴 사용 (border-radius는 미확인).

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| primary CTA (on light) | `var(--offset) var(--offset) 0 0 #FFFFFF, var(--offset) var(--offset) 0 var(--border) #000000` | primary 버튼 (밝은 배경) |
| primary CTA (on dark) | `var(--offset) var(--offset) 0 0 #000000, var(--offset) var(--offset) 0 var(--border) #FFFFFF` | primary 버튼 (어두운 배경) |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button

```html
<a href="#" class="stripes_v7_gl-cta--primary">
  Shop Now
</a>
```

| 속성 | 값 |
|---|---|
| background | `#000000` |
| color | `#FFFFFF` |
| box-shadow | drop shadow (이중 레이어) |
| font-family | `AdihausDIN` |

### Secondary CTA (on dark)

```html
<a href="#" class="stripes_v7_gl-cta--primary-ondark">
  Learn More
</a>
```

| 속성 | 값 |
|---|---|
| box-shadow offset | `var(--button-main-onlight-spacing-all-offset-outerbox) × 2 0 0 #000` |

### Product Card

```html
<div class="cardproduct">
  <img src="product.jpg" alt="adidas Ultraboost" />
  <div class="cardproduct__content">
    <p class="cardproduct__title">Ultraboost 22</p>
    <p class="cardproduct__price">₩189,000</p>
  </div>
</div>
```

### Link Card

```html
<div class="_link-card_516pc_143">
  <!-- row-reverse layout -->
</div>
```

| 속성 | 값 |
|---|---|
| background | `var(--backgrounds-gl-color-background-alternative, #eceff1)` |
| flex-direction | `row-reverse` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 영어 중심, 짧고 강렬 | "Impossible is Nothing" |
| Primary CTA | 행동 직접형 | "Shop Now" / "Add to Bag" |
| Secondary CTA | 탐색형 | "Explore Collection" |
| Subheading | 제품 이름 + 기능 설명 | "Ultraboost 22 — All Terrain" |
| Tone | 스포티, 포용적, 도전적 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* adidas — copy into your root stylesheet */
:root {
  /* Fonts */
  --gl-font-family: AdihausDIN, Helvetica, Arial, sans-serif;
  --gl-font-family-fallback: Helvetica, Arial, sans-serif;
  --gl-font-weight-normal: 400;
  --gl-font-weight-bold: 700;

  /* Brand (monochrome) */
  --gl-color-brand-black: #000000;
  --gl-color-brand-white: #FFFFFF;

  /* Surfaces */
  --gl-bg-page: #FFFFFF;
  --gl-bg-alt: #ECEFF1;
  --gl-bg-dark: #000000;
  --gl-text: #000000;
  --gl-text-muted: #A0A0A0;

  /* Focus */
  --gl-focus-ring: #91C7ED;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — adidas
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          black: '#000000',
          white: '#FFFFFF',
          alt: '#ECEFF1',
          focus: '#91C7ED',
        },
        neutral: {
          900: '#000000',
          600: '#464545',
          400: '#A0A0A0',
          300: '#C4C4C4',
          200: '#D3D7DA',
          100: '#F3F3F3',
          50: '#FFFFFF',
        },
      },
      fontFamily: {
        sans: ['AdihausDIN', 'Helvetica', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold: '700',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 브랜드 컬러는 순흑 `#000000` (회색화 없이)
- CTA 버튼에 drop shadow 이중 레이어 패턴 사용
- 대안 섹션 배경으로 `#ECEFF1` 사용
- 접근성 포커스 링은 `#91C7ED` (연한 파란)
- 폰트 토큰을 컨텍스트별로 세분화 (`body-functional-4`, `heading-standard-9` 등)

### ❌ DON'T
- 순흑을 `#333333` 이나 `#1A1A1A`로 희석하지 말 것 — adidas는 `#000000`
- drop shadow를 단층 box-shadow로 단순화하지 말 것
- SVG 로고의 `#000000` 빈도를 모든 UI 컬러로 해석하지 말 것
- 모든 폰트 컨텍스트를 동일 `AdihausDIN`으로 처리하지 말 것 — 변형별 분리 필요
