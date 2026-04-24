---
slug: louisvuitton
service_name: Louis Vuitton
site_url: https://www.louisvuitton.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#19110B"
primary_font: Louis Vuitton Web
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Louis Vuitton (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Louis Vuitton처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Louis Vuitton Web", "Louis Vuitton", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #19110B; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #19110B; }
```

**절대 하지 말아야 할 것 하나**: 텍스트 컬러로 순흑(#000000)을 쓰는 것. Louis Vuitton의 주 텍스트는 따뜻한 거의-검정(#19110B)으로, 차가운 순흑과 브랜드 따뜻함이 완전히 다르다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.louisvuitton.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다국어 전용 font-family 선언 다수 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미사용) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (전통적 멀티페이지 + 국가별 라우팅)
- **Design system**: Bespoke — 전용 폰트 중심, CSS 커스텀 프로퍼티 없음
- **CSS architecture**: 다국어 font-family 분기 + flat CSS
  ```
  core  (직접 hex 값)      배경·텍스트 색상
  comp  (selector 기반)    다국어별 폰트 분기
  ```
- **Class naming**: 기능 중심 클래스
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 셀프 호스트 — `Louis Vuitton Web` (Cyrillic, CJK 등 다국어 변형 포함)
- **Canonical anchor**: `#19110B` — 따뜻한 다크 브라운-블랙

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Louis Vuitton Web` (LV 독점 라이선스)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `400` (normal only)

```css
:root {
  --font-family: "Louis Vuitton Web", "Louis Vuitton", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-family-cjk: "Louis Vuitton Web", "Louis Vuitton", "Droid Sans Fallback",
                     "Malgun Gothic", Dotum, "MS Gothic", Georgia, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold:   400;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스 주의**: `Louis Vuitton Web`은 LV 독점 폰트. 대체재로 `Didot`, `Bodoni Moda`, 또는 `Playfair Display` 사용.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display-xl | 4rem | 400 | 1.0 | -0.02em |
| heading-l | 2.5rem | 400 | 1.1 | -0.01em |
| heading-m | 1.75rem | 400 | 1.2 | 0 |
| heading-s | 1.25rem | 400 | 1.3 | 0.02em |
| body | 1rem | 400 | 1.6 | 0.01em |
| caption | 0.75rem | 400 | 1.5 | 0.04em |

> ⚠️ weight는 400 단일. LV 폰트의 무게감은 font-weight보다 자형(letterform)으로 표현된다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-dark | #19110B |
| brand-mid | #E1E1E1 |
| brand-white | #FFFFFF |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #19110B |
| 100 | #F8F6F3 | #2C2218 |
| 200 | #E1E1E1 | #4A3C2F |
| 400 | #B8B0A6 | #7A6E62 |
| 700 | #6B5E52 | #B8B0A6 |
| 900 | #2C2218 | #F8F6F3 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-page | #FFFFFF | 페이지 배경 |
| fg-primary | #19110B | 주 텍스트 (warm dark) |
| fg-secondary | #6B5E52 | 보조 텍스트 |
| border | #E1E1E1 | 구분선 |
| btn-primary-bg | #19110B | 주 CTA 배경 |
| btn-primary-fg | #FFFFFF | 주 CTA 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #000000 | 6 | 텍스트·UI (CSS 단순화) |
| 2 | #FFFFFF | 5 | 배경 |
| 3 | #E1E1E1 | 2 | 경계선 |
| 4 | #19110B | 1 | 브랜드 따뜻한 다크 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 아이콘-레이블 |
| space-sm | 8px | 컴포넌트 내부 |
| space-md | 16px | 섹션 내부 |
| space-lg | 40px | 섹션 간 |
| space-xl | 80px | 페이지 레벨 |

**주요 alias**:
- `space-md` → 16px (기본 gap)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 버튼·카드 (럭셔리 직각) |
| radius-sm | 2px | 입력 필드 |
| radius-full | 999px | 알림 뱃지 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 4px rgba(25,17,11,0.08) | 카드 hover |
| shadow-md | 0 4px 16px rgba(25,17,11,0.12) | 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭 이미지 + 중앙/좌측 텍스트
- Background: #FFFFFF (텍스트 오버레이)
- H1: `4rem` / weight `400` / tracking `-0.02em`
- Max-width: 100vw

### Section Rhythm
```css
section {
  padding: 80px 48px;
  max-width: 1440px;
}
```

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary Button

```html
<button class="btn btn--primary">
  Discover
</button>
```

| Spec | Value |
|---|---|
| background | #19110B |
| color | #FFFFFF |
| padding | 14px 40px |
| border-radius | 0px |
| font-weight | 400 |
| letter-spacing | 0.12em |
| text-transform | uppercase |

### Product Card

```html
<div class="product-card">
  <div class="product-card__visual">
    <img src="product.jpg" alt="Product">
  </div>
  <div class="product-card__details">
    <h3 class="product-card__name">Neverfull MM</h3>
    <p class="product-card__price">$2,060</p>
  </div>
</div>
```

| Spec | Value |
|---|---|
| border-radius | 0px |
| background | #FFFFFF |
| gap | 16px |
| name weight | 400 |
| price weight | 400 |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결한 명사·형용사, 마침표 없음 | "The Timeless Monogram" |
| Primary CTA | 동사 또는 동사구, 대문자 | "DISCOVER" |
| Secondary CTA | 소문자, 링크형 | "See all" |
| Subheading | 설명적, 간결 | |
| Tone | 격조 있는 절제, 감탄사 금지 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Louis Vuitton — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Louis Vuitton Web", "Louis Vuitton", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold:   400;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #F8F6F3;
  --color-brand-300: #E1E1E1;
  --color-brand-500: #6B5E52;
  --color-brand-600: #19110B;   /* ← canonical */
  --color-brand-900: #0A0704;

  /* Surfaces */
  --bg-page:   #FFFFFF;
  --bg-dark:   #19110B;
  --text:      #19110B;
  --text-muted:#6B5E52;

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
// tailwind.config.js — Louis Vuitton
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F8F6F3',
          300: '#E1E1E1',
          500: '#6B5E52',
          600: '#19110B',
          900: '#0A0704',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F8F6F3',
          200: '#E1E1E1',
          400: '#B8B0A6',
          700: '#6B5E52',
          900: '#2C2218',
        },
      },
      fontFamily: {
        sans: ['"Louis Vuitton Web"', '"Louis Vuitton"', '"Helvetica Neue"', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '400',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '2px',
      },
      boxShadow: {
        'sm': '0 1px 4px rgba(25,17,11,0.08)',
        'md': '0 4px 16px rgba(25,17,11,0.12)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 텍스트 컬러는 `#19110B`(따뜻한 다크)을 쓴다
- 버튼과 카드에 `border-radius: 0`을 유지한다
- 폰트는 weight 단일(400)로 사용한다
- `letter-spacing: 0.12em`을 버튼 uppercase에 적용한다
- 여백을 넉넉하게 (80px 이상) 유지한다

### ❌ DON'T
- 텍스트에 순흑(`#000000`)을 쓰지 않는다 — `#19110B`로 대체
- `border-radius`에 큰 값을 넣지 않는다
- 색상 악센트(파랑, 빨강 등)를 UI에 추가하지 않는다
- body에 `font-weight: 700`을 쓰지 않는다
- 과도한 색상 변화로 호버 효과를 주지 않는다 (언더라인·불투명도 처리만)
