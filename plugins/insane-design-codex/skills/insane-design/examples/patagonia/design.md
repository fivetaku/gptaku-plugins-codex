---
slug: patagonia
service_name: Patagonia
site_url: https://www.patagonia.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#020202"
primary_font: Avenir Next W02 Light
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Patagonia (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Patagonia처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Avenir Next W02 Light", Helvetica, Arial, Verdana, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #020202; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #020202; }
```

**절대 하지 말아야 할 것 하나**: 텍스트에 순흑(`#000000`)을 쓰는 것. Patagonia의 기본 텍스트 컬러는 거의 검정이지만 미세하게 더 따뜻한 `#020202`다. 더 중요한 것은 브랜드의 의미 — 환경 운동가 색채를 헷갈려 임의로 초록/파랑을 CTA에 넣지 않는 것이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.patagonia.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Avenir 폰트 중심, 단순 구조 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미발견) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (e-commerce, 서버 렌더링)
- **Design system**: Bespoke — Avenir 폰트 패밀리 중심, 커스텀 CSS
- **CSS architecture**: Flat CSS, font-family 세분화
  ```
  core  (직접 hex 값)  텍스트·배경
  comp  (selector)     버튼·네비게이션
  ```
- **Class naming**: 기능적 클래스
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 셀프 호스트 — `Avenir Next W02 Light`, `Avenir Next LT W02 Bold`, `AvenirNextLTW02-Medium`
- **Canonical anchor**: `#020202` — near-black 텍스트

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Avenir Next W02 Light` (Monotype 라이선스)
- **Bold font**: `Avenir Next LT W02 Bold`
- **Medium font**: `AvenirNextLTW02-Medium`
- **Code font**: N/A
- **Weight normal / bold**: `400` / `bold`

```css
:root {
  --font-body:   "Avenir Next W02 Light", Helvetica, Arial, Verdana, sans-serif;
  --font-bold:   "Avenir Next LT W02 Bold", Helvetica, Arial, Verdana, sans-serif;
  --font-medium: "AvenirNextLTW02-Medium", Helvetica, Arial, Verdana, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold:   bold;
}
body {
  font-family: var(--font-body);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스 주의**: `Avenir Next` 시리즈는 Monotype 유료 폰트. 대체재로 `Nunito Sans Light` 또는 `Source Sans 3 Light` 사용.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 3.5rem | bold | 1.05 | -0.02em |
| heading-l | 2rem | bold | 1.15 | -0.01em |
| heading-m | 1.5rem | bold | 1.25 | 0 |
| heading-s | 1.125rem | bold | 1.35 | 0 |
| body | 1rem | 400 | 1.65 | 0 |
| small | 0.875rem | 400 | 1.6 | 0 |
| caption | 0.75rem | 400 | 1.5 | 0.02em |

> ⚠️ Patagonia는 세 가지 Avenir 변형을 별도 폰트 파일로 분리 로딩한다. `font-weight` 숫자보다 font-family 이름으로 굵기를 제어한다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-dark | #020202 |
| brand-mid | #000000 |
| brand-white | #FFFFFF |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #020202 |
| 100 | #F5F5F5 | #2A2A2A |
| 200 | #E5E5E5 | #404040 |
| 400 | #9E9E9E | #808080 |
| 700 | #4A4A4A | #9E9E9E |
| 900 | #1A1A1A | #F5F5F5 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-page | #FFFFFF | 페이지 배경 |
| fg-primary | #020202 | 주 텍스트 |
| fg-secondary | #4A4A4A | 보조 텍스트 |
| border | #E5E5E5 | 구분선 |
| btn-primary-bg | #020202 | 주 CTA 배경 |
| btn-primary-fg | #FFFFFF | 주 CTA 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #FFFFFF | 3 | 배경 |
| 2 | #000000 | 2 | 텍스트 (CSS 단순화) |
| 3 | #020202 | 2 | 텍스트 (실제 브랜드) |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 미세 간격 |
| space-sm | 8px | 컴포넌트 내부 |
| space-md | 16px | 섹션 내 |
| space-lg | 32px | 섹션 간 |
| space-xl | 64px | 페이지 레벨 |

**주요 alias**:
- `space-lg` → 32px (기본 섹션 패딩)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 기본 버튼·카드 |
| radius-sm | 4px | 입력 필드, 일부 배지 |
| radius-full | 999px | 알림 뱃지 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 3px rgba(2,2,2,0.08) | 카드 hover |
| shadow-md | 0 4px 12px rgba(2,2,2,0.12) | 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭 이미지 + 좌측/중앙 텍스트
- Background: #FFFFFF (텍스트 영역)
- H1: `3.5rem` / weight `bold` / tracking `-0.02em`
- Max-width: 100vw

### Section Rhythm
```css
section {
  padding: 64px 40px;
  max-width: 1440px;
}
```

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary Button

```html
<button class="btn btn--primary">
  Shop Now
</button>
```

| Spec | Value |
|---|---|
| background | #020202 |
| color | #FFFFFF |
| padding | 14px 28px |
| border-radius | 0px |
| font-family | "Avenir Next LT W02 Bold" |
| letter-spacing | 0.04em |
| text-transform | uppercase |

### Product Card

```html
<div class="product-card">
  <div class="product-card__image">
    <img src="jacket.jpg" alt="Product Name">
  </div>
  <div class="product-card__info">
    <h3 class="product-card__name">Nano Puff Jacket</h3>
    <p class="product-card__price">$279</p>
  </div>
</div>
```

| Spec | Value |
|---|---|
| border-radius | 0px |
| background | #FFFFFF |
| gap | 12px |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 직접적, 활동 중심, 감성 없는 실용 | "Better Than New" |
| Primary CTA | 동사 원형, 대문자 | "SHOP" |
| Secondary CTA | 소문자, 링크형 | "Learn more" |
| Subheading | 소재·기능 설명 | |
| Tone | 환경 운동 직접성, 브랜드 가치 중심, 과장 금지 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Patagonia — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Avenir Next W02 Light", Helvetica, Arial, Verdana, sans-serif;
  --font-family-bold: "Avenir Next LT W02 Bold", Helvetica, Arial, Verdana, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold: bold;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #F5F5F5;
  --color-brand-300: #9E9E9E;
  --color-brand-500: #4A4A4A;
  --color-brand-600: #020202;   /* ← canonical */
  --color-brand-900: #000000;

  /* Surfaces */
  --bg-page:   #FFFFFF;
  --bg-dark:   #020202;
  --text:      #020202;
  --text-muted:#4A4A4A;

  /* Key spacing */
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  32px;

  /* Radius */
  --radius-sm: 0px;
  --radius-md: 4px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Patagonia
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F5F5F5',
          300: '#9E9E9E',
          500: '#4A4A4A',
          600: '#020202',
          900: '#000000',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F5F5F5',
          200: '#E5E5E5',
          400: '#9E9E9E',
          700: '#4A4A4A',
          900: '#1A1A1A',
        },
      },
      fontFamily: {
        sans: ['"Avenir Next W02 Light"', 'Helvetica', 'Arial', 'sans-serif'],
        bold: ['"Avenir Next LT W02 Bold"', 'Helvetica', 'Arial', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   'bold',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '4px',
      },
      boxShadow: {
        'sm': '0 1px 3px rgba(2,2,2,0.08)',
        'md': '0 4px 12px rgba(2,2,2,0.12)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 텍스트는 `#020202`(near-black)으로 설정한다
- heading은 `font-family: "Avenir Next LT W02 Bold"`로 별도 지정한다
- 버튼에 `border-radius: 0`을 유지한다
- 환경·활동 가치 중심의 카피 톤을 유지한다

### ❌ DON'T
- 브랜드 컬러로 초록이나 파랑을 CTA에 넣지 않는다 — Patagonia UI는 흑백 중심
- `font-weight: 700`으로 굵기를 제어하지 않는다 — 별도 Bold 폰트 파일 사용
- 텍스트에 순흑(`#000000`)을 쓰지 않는다 — `#020202` 사용
- 불필요한 색상 장식을 넣지 않는다
- 큰 `border-radius`(8px 이상)를 버튼에 쓰지 않는다
