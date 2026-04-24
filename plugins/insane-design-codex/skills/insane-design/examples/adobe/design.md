---
slug: adobe
service_name: Adobe
site_url: https://adobe.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#3B63FB"
primary_font: adobe-clean
font_weight_normal: 400
token_prefix: --feds-*
---

# DESIGN.md — Adobe (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Adobe처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "adobe-clean", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #292929; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #3B63FB; }
```

**절대 하지 말아야 할 것 하나**: Adobe 로고의 빨간 `#EB1000`을 UI 버튼 색으로 쓰는 것. 실제 마케팅 사이트의 CTA 버튼은 Spectrum 계열 파란색 `#3B63FB`이다. 빨간색은 로고·브랜드 아이덴티티 전용이고, UI 액션 컬러는 완전히 별개다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://adobe.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다수 외부 CSS (Adobe FEDS + Spectrum) |
| Token prefix | `--feds-*`, `--alias-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (Adobe 자체 마케팅 플랫폼)
- **Design system**: Adobe Spectrum (마케팅 사이트 FEDS 레이어) — prefix `--feds-*`, `--alias-*`
- **CSS architecture**: 2-tier 토큰 계층
  ```
  alias   (--alias-background-semantic-*, --alias-content-*)  semantic 역할 토큰
  feds    (--feds-color-adobeBrand, --feds-cta-*)             마케팅 전용 CTA 토큰
  ```
- **Class naming**: BEM-ish (`.universal-nav-container`, `.feds-*`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스트 (adobe-clean, adobe-clean-serif, adobe-clean-display)
- **Canonical anchor**: `#3B63FB` — `--feds-cta-primary-bg` 및 `--alias-background-semantic-accent-default-spectrum-2` 공통 값

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `adobe-clean-display` (Adobe 독점, 내부 전용)
- **Body font**: `adobe-clean` (Adobe 독점, 내부 전용)
- **Serif font**: `adobe-clean-serif` (Adobe 독점)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --feds-font-family: "adobe-clean", "Helvetica Neue", Arial, sans-serif;
  --feds-font-weight-normal: 400;
  --feds-font-weight-bold: 700;
}
body {
  font-family: var(--feds-font-family);
  font-weight: var(--feds-font-weight-normal);
}
```

> **라이선스 주의**: `adobe-clean` 계열은 Adobe 내부 전용. 외부 프로젝트에서는 `Source Sans 3` 또는 `Inter`가 가장 가까운 오픈소스 대체재.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| heading-xl | 2.5rem | 700 | 1.2 | -0.02em |
| heading-lg | 2rem | 700 | 1.25 | -0.015em |
| heading-md | 1.5rem | 700 | 1.3 | -0.01em |
| body-lg | 1.125rem | 400 | 1.6 | 0 |
| body-md | 1rem | 400 | 1.6 | 0 |
| body-sm | 0.875rem | 400 | 1.5 | 0 |
| label | 0.75rem | 600 | 1.4 | 0.04em |

> ⚠️ Adobe 마케팅 사이트의 heading은 weight 700이 지배적(21회). body는 400이 표준(13회)이나 일부 컴포넌트는 600을 쓴다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (CTA / Spectrum Blue)

| Token | Hex |
|---|---|
| `--feds-cta-primary-bg` | `#3B63FB` |
| `--alias-background-semantic-accent-default-spectrum-2` | `#3B63FB` |
| `--alias-background-semantic-accent-hover-spectrum-2` | `#274DEA` |
| `--alias-background-semantic-accent-default-spectrum` | `#0265DC` |
| `--alias-background-semantic-accent-hover-spectrum` | `#0054B6` |
| `--feds-cta-primary-bg--hover` | `#274DEA` |

### 06-2. Brand Dark Variant (Express Purple)

| Token | Hex |
|---|---|
| `--alias-background-semantic-accent-default-express` (light) | `#5258E4` |
| `--alias-background-semantic-accent-hover-express` (light) | `#4046CA` |
| `--alias-background-semantic-accent-default-express` (dark) | `#A7AAFF` |
| `--alias-background-semantic-accent-hover-express` (dark) | `#BCBEFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| icon/content neutral | `#292929` | `#393939` |
| border | `#E1E1E1` | `#444444` |
| surface hover | `#F5F5F5` | `#333333` |
| CTA secondary border | `#DADADA` | `#393939` |
| focus ring | `#507BFF` | `#507BFF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Adobe Brand (로고) | brand | `#EB1000` |
| Spectrum Blue | default | `#0265DC` |
| Spectrum Blue 2 | default | `#3B63FB` |
| Express Purple | default (light) | `#5258E4` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--feds-color-adobeBrand` | `#EB1000` | 로고 및 브랜드 전용 |
| `--feds-cta-primary-bg` | `#3B63FB` | CTA 버튼 배경 |
| `--alias-icon-neutral-default` | `#292929` | 아이콘 기본 색 |
| `--profile-cta-secondary-border` | `#DADADA` | 보조 CTA 테두리 |
| `--alias-icon-neutral-key-focus` | `#507BFF` | 포커스 링 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--feds-cta-primary-bg` | `#3B63FB` | 마케팅 CTA 주요 버튼 |
| `--feds-cta-primary-bg--hover` | `#274DEA` | CTA hover 상태 |
| `--alias-background-semantic-accent-default-spectrum` | `#0265DC` | Spectrum 앱 accent |
| `--alias-background-semantic-accent-default-express` | `#5258E4` | Express 앱 accent |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| N/A | — | CSS 파싱에서 spacing 토큰 미확인 |

> N/A — spacing 토큰이 CSS에서 추출되지 않음. Adobe FEDS는 Spectrum 스케일을 내부적으로 참조하나 마케팅 레이어에서 직접 노출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| N/A | — | CSS 파싱에서 radius 토큰 미확인 |

> N/A — radius 토큰이 CSS에서 추출되지 않음.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| N/A | — | CSS 파싱에서 shadow 토큰 미확인 |

> N/A — shadow 토큰이 CSS에서 추출되지 않음.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button

```html
<a href="#" class="feds-cta--primary">
  무료로 시작하기
</a>
```

| 속성 | 값 |
|---|---|
| background | `#3B63FB` |
| color | `#FFFFFF` |
| hover background | `#274DEA` |
| font-weight | `700` |
| font-family | `adobe-clean` |

### Secondary CTA Button

```html
<a href="#" class="feds-cta--secondary">
  자세히 알아보기
</a>
```

| 속성 | 값 |
|---|---|
| border | `1px solid #DADADA` |
| color | `#292929` |
| background | `transparent` |

### Navigation

```html
<div class="universal-nav-container">
  <nav id="universal-nav" class="universal-nav-light">
    <!-- nav items -->
  </nav>
</div>
```

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 제품 능력 중심, 능동형 | "Make it. Make it real." |
| Primary CTA | 행동 + 무료 강조 | "무료로 시작하기" |
| Secondary CTA | 방향 유도 | "자세히 알아보기" |
| Subheading | 사용자 베네핏 중심 | "크리에이터를 위한 모든 것" |
| Tone | 창의적이고 역동적, 전문성 강조 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Adobe — copy into your root stylesheet */
:root {
  /* Fonts */
  --feds-font-family: "adobe-clean", "Helvetica Neue", Arial, sans-serif;
  --feds-font-weight-normal: 400;
  --feds-font-weight-bold: 700;

  /* Brand (Spectrum Blue CTA) */
  --feds-color-brand-logo: #EB1000;   /* 로고 전용 — UI에 쓰지 말 것 */
  --feds-color-brand-cta: #3B63FB;    /* CTA 버튼 */
  --feds-color-brand-cta-hover: #274DEA;
  --feds-color-brand-express: #5258E4;

  /* Surfaces */
  --feds-bg-page: #FFFFFF;
  --feds-bg-dark: #292929;
  --feds-text: #292929;
  --feds-text-muted: #6E6E6E;

  /* Focus */
  --feds-focus-ring: #507BFF;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Adobe
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          logo:    '#EB1000',
          cta:     '#3B63FB',
          hover:   '#274DEA',
          express: '#5258E4',
          focus:   '#507BFF',
        },
        neutral: {
          900: '#292929',
          300: '#DADADA',
          200: '#E1E1E1',
          100: '#F5F5F5',
        },
      },
      fontFamily: {
        sans: ['"adobe-clean"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold:   '700',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- CTA 버튼 배경에 `#3B63FB` (Spectrum Blue) 사용
- 본문 색상으로 `#292929` (거의 검정, 순흑 아님) 사용
- Heading에 `font-weight: 700` 적용
- 포커스 링 색으로 `#507BFF` 사용
- adobe-clean 대체재로 `Source Sans 3` 또는 `Inter` 사용

### ❌ DON'T
- Adobe 로고 빨간 `#EB1000`을 UI 버튼에 쓰지 말 것 — 로고 전용
- body에 `font-weight: 300` 또는 `100` 쓰지 말 것 — 400이 기준
- Spectrum Blue와 Express Purple을 같은 화면에 혼합하지 말 것
- CTA 호버 색을 임의로 만들지 말 것 — `#274DEA` 고정
