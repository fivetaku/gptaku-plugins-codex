---
slug: gucci
service_name: Gucci
site_url: https://www.gucci.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#000000"
primary_font: Gucci Sans Pro
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Gucci (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Gucci처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Gucci Sans Pro", "Apple SD Gothic Neo", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 컬러로 금색(gold)을 넣는 것. Gucci UI의 primary 버튼과 CTA는 순흑(#000000)이다. 금색은 로고 자수 패턴에만 사용된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.gucci.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다수 외부 + 인라인, Toastify 포함 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미사용) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (전통적 멀티페이지 구조)
- **Design system**: Bespoke — prefix 없음, 커스텀 CSS
- **CSS architecture**: Flat CSS + Toastify 알림 라이브러리
  ```
  core   (직접 hex 값)   페이지 배경·텍스트
  util   (selector 기반) 버튼·링크 상태
  ```
- **Class naming**: BEM 아님, 기능적 클래스 (`.Toastify__close-button` 등)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 셀프 호스트 — `Gucci Sans Pro` (다국어 fallback 포함)
- **Canonical anchor**: `#000000` — primary CTA button bg

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Gucci Sans Pro` (Gucci 독점 라이선스)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: "Gucci Sans Pro", "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold:   700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스 주의**: `Gucci Sans Pro`는 Gucci 독점 폰트. 대체재로 `Helvetica Neue Light` 또는 `Inter` 사용.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 3.5rem | 100 | 1.1 | -0.02em |
| heading-l | 2rem | 400 | 1.2 | -0.01em |
| heading-m | 1.5rem | 400 | 1.3 | 0 |
| heading-s | 1.125rem | 500 | 1.35 | 0 |
| body | 1rem | 400 | 1.6 | 0 |
| caption | 0.75rem | 400 | 1.5 | 0.04em |

> ⚠️ weight 100은 hero 디스플레이 전용. 일반 body에 100을 쓰면 읽기 어렵다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-black | #000000 |
| brand-mid | #555555 |
| brand-light | #F5F5F5 |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #000000 |
| 100 | #F5F5F5 | #1A1A1A |
| 200 | #E5E5E5 | #333333 |
| 400 | #999999 | #666666 |
| 700 | #555555 | #999999 |
| 900 | #1A1A1A | #F5F5F5 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-page | #FFFFFF | 페이지 배경 |
| fg-primary | #000000 | 주 텍스트 |
| fg-secondary | #555555 | 보조 텍스트 |
| border | #E5E5E5 | 구분선 |
| btn-primary-bg | #000000 | 주 CTA 배경 |
| btn-primary-fg | #FFFFFF | 주 CTA 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #FFFFFF | 높음 | 배경·버튼 텍스트 |
| 2 | #000000 | 높음 | 텍스트·primary CTA |
| 3 | #555555 | 중간 | 보조 텍스트 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 아이콘-레이블 간격 |
| space-sm | 8px | 컴포넌트 내부 패딩 |
| space-md | 16px | 섹션 내부 간격 |
| space-lg | 32px | 섹션 간 간격 |
| space-xl | 64px | 페이지 레벨 패딩 |

**주요 alias**:
- `space-md` → 16px (기본 padding)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 버튼, 카드 (럭셔리 직각 스타일) |
| radius-sm | 2px | 입력 필드 |
| radius-full | 999px | 알림 뱃지 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 3px rgba(0,0,0,0.08) | 카드 hover |
| shadow-md | 0 4px 12px rgba(0,0,0,0.12) | 드롭다운 메뉴 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭 이미지 + 중앙 텍스트 오버레이
- Background: #000000 (dark overlay on image)
- H1: `3.5rem` / weight `100` / tracking `-0.02em`
- Max-width: 100vw

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
| mobile | 768px | 1열 그리드 |
| tablet | 1024px | 2열 그리드 |
| desktop | 1440px | 전체 레이아웃 |

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
| background | #000000 |
| color | #FFFFFF |
| padding | 14px 32px |
| border-radius | 0px |
| font-weight | 500 |
| letter-spacing | 0.08em |
| text-transform | uppercase |

### Product Card

```html
<div class="product-card">
  <div class="product-card__image">
    <img src="product.jpg" alt="Product Name">
  </div>
  <div class="product-card__info">
    <p class="product-card__name">Product Name</p>
    <p class="product-card__price">$1,200</p>
  </div>
</div>
```

| Spec | Value |
|---|---|
| border-radius | 0px |
| background | #FFFFFF |
| font-weight (name) | 400 |
| font-weight (price) | 400 |
| gap | 12px |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결, 1인칭 명사형, 이탤릭 강조 없음 | "The Gucci Collection" |
| Primary CTA | 동사 원형, 대문자 | "SHOP NOW" |
| Secondary CTA | 동사 원형, 소문자 | "Discover more" |
| Subheading | 설명적, 간결 | |
| Tone | 절제된 럭셔리, 과잉 수식 금지 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Gucci — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Gucci Sans Pro", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold:   700;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #F5F5F5;
  --color-brand-300: #999999;
  --color-brand-500: #555555;
  --color-brand-600: #000000;   /* ← canonical */
  --color-brand-900: #000000;

  /* Surfaces */
  --bg-page:   #FFFFFF;
  --bg-dark:   #000000;
  --text:      #000000;
  --text-muted:#555555;

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
// tailwind.config.js — Gucci
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F5F5F5',
          300: '#999999',
          500: '#555555',
          600: '#000000',
          900: '#000000',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F5F5F5',
          200: '#E5E5E5',
          400: '#999999',
          700: '#555555',
          900: '#1A1A1A',
        },
      },
      fontFamily: {
        sans: ['"Gucci Sans Pro"', '"Apple SD Gothic Neo"', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '700',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '2px',
        'full': '9999px',
      },
      boxShadow: {
        'sm': '0 1px 3px rgba(0,0,0,0.08)',
        'md': '0 4px 12px rgba(0,0,0,0.12)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- primary CTA는 `background: #000000`, `color: #FFFFFF`로 설정한다
- 버튼과 카드에 `border-radius: 0`을 유지한다 (럭셔리 직각 미학)
- `font-weight: 100`은 hero 디스플레이 텍스트에만 쓴다
- `letter-spacing: 0.08em`을 버튼 텍스트(uppercase)에 적용한다
- 텍스트는 흑백 대비 중심으로 구성한다

### ❌ DON'T
- 브랜드 컬러로 금색(gold)을 UI에 넣지 않는다
- `border-radius`에 큰 값(8px 이상)을 쓰지 않는다
- 본문에 `font-weight: 100`을 쓰지 않는다
- 불필요한 색상 장식을 넣지 않는다 (Gucci UI는 철저하게 흑백)
- 버튼 텍스트를 소문자 혼용(mixed case)으로 쓰지 않는다
