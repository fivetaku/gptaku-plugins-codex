---
slug: aesop
service_name: Aesop
site_url: https://www.aesop.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#313131"
primary_font: system-ui
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Aesop (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Aesop처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F5F0E8; --fg: #313131; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #313131; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백(#FFFFFF)으로 두는 것. Aesop의 정체성은 따뜻한 크림-베이지(#F5F0E8) 계열 배경에 있다. 순백 배경은 Aesop 특유의 아포테카리 감성을 즉시 파괴한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.aesop.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | system-ui 기반 단순 구조 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미발견) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (서버 렌더링 e-commerce)
- **Design system**: Bespoke — 시스템 폰트 + 최소 CSS 변수
- **CSS architecture**: Flat CSS, 클래스 기반
  ```
  core  (직접 hex/시스템 값)  텍스트·배경
  comp  (selector)             버튼·카드
  ```
- **Class naming**: 기능적 클래스 (BEM 미적용)
- **Default theme**: light (bg = `#F5F0E8` — 따뜻한 크림)
- **Font loading**: 시스템 폰트 (system-ui) — 외부 폰트 로딩 없음
- **Canonical anchor**: `#313131` — 거의 검정이지만 따뜻한 다크 그레이

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `system-ui` (OS 기본 폰트)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-weight-normal: 400;
  --font-weight-bold:   700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **참고**: Aesop의 브랜드는 폰트 개성이 아닌 색상·질감·여백의 조화로 형성된다. 시스템 폰트를 의도적으로 사용한다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 3rem | 400 | 1.1 | -0.01em |
| heading-l | 1.75rem | 400 | 1.2 | 0 |
| heading-m | 1.375rem | 400 | 1.3 | 0.01em |
| heading-s | 1.125rem | 400 | 1.4 | 0.02em |
| body | 1rem | 400 | 1.7 | 0 |
| caption | 0.8125rem | 400 | 1.5 | 0.04em |

> ⚠️ line-height 1.7은 Aesop 특유의 여유 있는 문단 간격. 1.5로 줄이면 분위기가 완전히 달라진다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-dark | #313131 |
| brand-cream | #F5F0E8 |
| brand-white | #FFFFFF |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #313131 |
| 100 | #F5F0E8 | #3D3D3D |
| 200 | #E8E2D8 | #5A5A5A |
| 400 | #C4BCB0 | #8A8A8A |
| 700 | #7A7468 | #C4BCB0 |
| 900 | #3D3D3D | #F5F0E8 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-page | #F5F0E8 | 페이지 배경 (크림-베이지) |
| bg-card | #FFFFFF | 카드 배경 |
| fg-primary | #313131 | 주 텍스트 |
| fg-secondary | #7A7468 | 보조 텍스트 |
| border | #E8E2D8 | 구분선 |
| btn-primary-bg | #313131 | 주 CTA 배경 |
| btn-primary-fg | #F5F0E8 | 주 CTA 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #313131 | 2 | 주 텍스트·CTA |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 미세 간격 |
| space-sm | 8px | 컴포넌트 내부 |
| space-md | 16px | 섹션 내 |
| space-lg | 40px | 섹션 간 |
| space-xl | 80px | 페이지 레벨 |
| space-xxl | 120px | 대형 여백 |

**주요 alias**:
- `space-xl` → 80px (Aesop의 넉넉한 여백)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 버튼·카드 (약재상 직각 미학) |
| radius-sm | 2px | 입력 필드 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 3px rgba(49,49,49,0.06) | 미세 카드 |
| shadow-md | 0 2px 8px rgba(49,49,49,0.08) | 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭, 이미지 중심 + 하단 텍스트
- Background: #F5F0E8 (크림 배경)
- H1: `3rem` / weight `400` / tracking `-0.01em`
- Max-width: 1440px

### Section Rhythm
```css
section {
  padding: 80px 48px;
  max-width: 1280px;
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
| background | #313131 |
| color | #F5F0E8 |
| padding | 12px 32px |
| border-radius | 0px |
| font-weight | 400 |
| letter-spacing | 0.08em |
| text-transform | uppercase |

### Product Card

```html
<div class="product-card">
  <figure class="product-card__image">
    <img src="product.jpg" alt="Product Name">
  </figure>
  <div class="product-card__content">
    <h3 class="product-card__name">Reverence Aromatique Hand Wash</h3>
    <p class="product-card__volume">500 mL</p>
    <p class="product-card__price">$49</p>
  </div>
</div>
```

| Spec | Value |
|---|---|
| border-radius | 0px |
| background | #FFFFFF |
| gap | 16px |
| name weight | 400 |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결, 명사 중심, 이탤릭 간헐 사용 | "A Ritual of Care" |
| Primary CTA | 동사 원형, 대문자 | "EXPLORE" |
| Secondary CTA | 소문자, 링크형 | "Read more" |
| Subheading | 시적, 설명적 | |
| Tone | 학구적 감성, 자연·과학 용어, 과잉 수식 금지 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Aesop — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold:   700;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #F5F0E8;
  --color-brand-300: #C4BCB0;
  --color-brand-500: #7A7468;
  --color-brand-600: #313131;   /* ← canonical */
  --color-brand-900: #1A1A1A;

  /* Surfaces */
  --bg-page:   #F5F0E8;
  --bg-dark:   #313131;
  --text:      #313131;
  --text-muted:#7A7468;

  /* Key spacing */
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  40px;

  /* Radius */
  --radius-sm: 0px;
  --radius-md: 2px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Aesop
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F5F0E8',
          300: '#C4BCB0',
          500: '#7A7468',
          600: '#313131',
          900: '#1A1A1A',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F5F0E8',
          200: '#E8E2D8',
          400: '#C4BCB0',
          700: '#7A7468',
          900: '#3D3D3D',
        },
      },
      fontFamily: {
        sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'sans-serif'],
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
        'sm': '0 1px 3px rgba(49,49,49,0.06)',
        'md': '0 2px 8px rgba(49,49,49,0.08)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 배경은 `#F5F0E8`(크림-베이지)을 쓴다 — 순백 금지
- primary CTA 텍스트는 `#F5F0E8`(크림)으로, 흰색이 아닌 크림
- `border-radius: 0`으로 직각 미학을 유지한다
- `line-height: 1.7`로 본문 여백을 넉넉하게 준다
- 시스템 폰트를 사용한다 (외부 폰트 불필요)

### ❌ DON'T
- 배경을 순백(`#FFFFFF`)으로 두지 않는다 — 크림 배경이 Aesop의 핵심
- `border-radius`에 8px 이상의 값을 넣지 않는다
- 채도 높은 악센트 색상(빨강, 파랑 등)을 UI에 추가하지 않는다
- 폰트 weight를 100이나 800 등 극단값으로 쓰지 않는다
- 버튼 텍스트를 소문자 혼용으로 쓰지 않는다 (uppercase 통일)
