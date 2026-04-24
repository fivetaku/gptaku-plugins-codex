---
slug: uniqlo
service_name: UNIQLO
site_url: https://www.uniqlo.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#FF0000"
primary_font: system-ui
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — UNIQLO (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 UNIQLO처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FF0000; }
```

**절대 하지 말아야 할 것 하나**: 빨간색(#FF0000)을 CTA나 본문 링크에 남용하는 것. UNIQLO의 red는 로고와 특정 promotional 배너에만 사용된다. UI의 기본 동작(버튼, 링크)은 흑백으로 처리된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.uniqlo.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | CSS 최소화, 외부 폰트 없음 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미발견) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (글로벌 e-commerce)
- **Design system**: Bespoke — 시스템 폰트, 흑백 중심, 로고 red 악센트
- **CSS architecture**: Flat CSS, SVG 패턴 (빨간 로고)
  ```
  core  (직접 hex 값)  흑백 UI
  comp  (svg_pattern)  로고·배너 red
  ```
- **Class naming**: 기능적 클래스
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 시스템 폰트 전용 (외부 폰트 없음)
- **Canonical anchor**: `#FF0000` — 로고 빨강 (SVG 패턴에서 검출)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `system-ui` (OS 기본 폰트)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold:   700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **참고**: UNIQLO는 시스템 폰트를 의도적으로 사용한다. 일본어(Hiragino, Yu Gothic), 한국어(Apple SD Gothic Neo), 영어(Helvetica Neue) 모두 OS 기본 폰트로 처리.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 3rem | 700 | 1.1 | -0.02em |
| heading-l | 1.75rem | 700 | 1.2 | -0.01em |
| heading-m | 1.375rem | 700 | 1.3 | 0 |
| heading-s | 1.125rem | 700 | 1.4 | 0 |
| body | 1rem | 400 | 1.6 | 0 |
| small | 0.875rem | 400 | 1.5 | 0 |
| caption | 0.75rem | 400 | 1.4 | 0.02em |
| price | 1.25rem | 700 | 1.2 | 0 |

> ⚠️ heading은 모두 weight 700. body는 400 단일. 중간 weight(500, 600)는 거의 사용하지 않는다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-red | #FF0000 |
| brand-dark | #000000 |
| brand-white | #FFFFFF |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #000000 |
| 100 | #F5F5F5 | #1A1A1A |
| 200 | #E0E0E0 | #333333 |
| 400 | #9E9E9E | #666666 |
| 700 | #424242 | #9E9E9E |
| 900 | #1A1A1A | #F5F5F5 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-page | #FFFFFF | 페이지 배경 |
| fg-primary | #000000 | 주 텍스트 |
| fg-secondary | #424242 | 보조 텍스트 |
| border | #E0E0E0 | 구분선 |
| btn-primary-bg | #000000 | 주 CTA 배경 |
| btn-primary-fg | #FFFFFF | 주 CTA 텍스트 |
| brand-accent | #FF0000 | 로고·프로모션 배너 |
| sale | #FF0000 | 할인가 표시 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #FF0000 | 1 | 로고 SVG (빨간 배경) |
| 2 | #FFFFFF | 1 | 배경 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 미세 간격 |
| space-sm | 8px | 컴포넌트 내부 |
| space-md | 16px | 카드 패딩 |
| space-lg | 32px | 섹션 간 |
| space-xl | 64px | 페이지 패딩 |

**주요 alias**:
- `space-md` → 16px (기본 패딩)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 버튼·카드 (UNIQLO 직각) |
| radius-sm | 2px | 입력 필드 |
| radius-full | 999px | 뱃지·태그 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 3px rgba(0,0,0,0.08) | 카드 hover |
| shadow-md | 0 4px 12px rgba(0,0,0,0.10) | 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭, 상품 이미지 중심
- Background: #FFFFFF
- H1: `3rem` / weight `700` / tracking `-0.02em`
- Max-width: 1440px

### Section Rhythm
```css
section {
  padding: 64px 40px;
  max-width: 1440px;
}
```

### Breakpoints

| Breakpoint | Value | Changes |
|---|---|---|
| mobile | 768px | 1열 상품 그리드 |
| tablet | 1024px | 2열 그리드 |
| desktop | 1440px | 4열 그리드 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary Button

```html
<button class="btn btn--primary">
  Add to Cart
</button>
```

| Spec | Value |
|---|---|
| background | #000000 |
| color | #FFFFFF |
| padding | 14px 24px |
| border-radius | 0px |
| font-weight | 700 |
| text-transform | none |

### Product Card

```html
<div class="product-card">
  <div class="product-card__image">
    <img src="product.jpg" alt="T-Shirt">
    <span class="product-card__badge">Sale</span>
  </div>
  <div class="product-card__info">
    <p class="product-card__name">Ultra Light Down Jacket</p>
    <p class="product-card__price">$99.90</p>
    <p class="product-card__colors">7 Colors</p>
  </div>
</div>
```

| Spec | Value |
|---|---|
| border-radius | 0px |
| background | #FFFFFF |
| sale badge bg | #FF0000 |
| sale badge color | #FFFFFF |
| name weight | 400 |
| price weight | 700 |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결, 소재·기능 직접 서술 | "Made for All" |
| Primary CTA | 동사구, 제목어 | "Add to Cart" |
| Secondary CTA | 소문자, 링크형 | "View all" |
| Subheading | 기능 설명, 명사 중심 | |
| Tone | 실용적, 포용적, 과장 금지 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* UNIQLO — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold:   700;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #FFF5F5;
  --color-brand-300: #FF9999;
  --color-brand-500: #FF3333;
  --color-brand-600: #FF0000;   /* ← canonical (logo/promo only) */
  --color-brand-900: #990000;

  /* Surfaces */
  --bg-page:   #FFFFFF;
  --bg-dark:   #000000;
  --text:      #000000;
  --text-muted:#424242;

  /* Key spacing */
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  32px;

  /* Radius */
  --radius-sm: 0px;
  --radius-md: 2px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — UNIQLO
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#FFF5F5',
          300: '#FF9999',
          500: '#FF3333',
          600: '#FF0000',
          900: '#990000',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F5F5F5',
          200: '#E0E0E0',
          400: '#9E9E9E',
          700: '#424242',
          900: '#1A1A1A',
        },
      },
      fontFamily: {
        sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', '"Helvetica Neue"', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '700',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '2px',
      },
      boxShadow: {
        'sm': '0 1px 3px rgba(0,0,0,0.08)',
        'md': '0 4px 12px rgba(0,0,0,0.10)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- primary CTA는 `background: #000000`으로 유지한다
- `#FF0000`은 로고·sale 배지·프로모션 배너에만 사용한다
- heading은 모두 `font-weight: 700`을 적용한다
- `border-radius: 0`으로 직각 형태를 유지한다
- 상품 그리드는 4열(desktop) 구성을 기본으로 한다

### ❌ DON'T
- `#FF0000`을 CTA 버튼이나 링크 색상으로 쓰지 않는다
- 중간 weight(500, 600)를 heading에 쓰지 않는다 — 400 또는 700만
- `border-radius`에 큰 값을 넣지 않는다
- 배경을 회색(#F5F5F5)으로 두지 않는다 — UNIQLO 기본 배경은 순백
- 불필요한 색상 악센트를 추가하지 않는다
