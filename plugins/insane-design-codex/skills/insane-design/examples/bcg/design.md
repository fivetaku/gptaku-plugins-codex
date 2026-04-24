---
slug: bcg
service_name: BCG
site_url: https://www.bcg.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0E3E1B"
primary_font: henderson-bcg-sans
font_weight_normal: 300
token_prefix: --BCG-*
---

# DESIGN.md — BCG (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 BCG처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight 300 */
body {
  font-family: "henderson-bcg-sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 300;   /* ⚠️ 400 아님. BCG body는 300. */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #212427; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0E3E1B; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 green을 lime-green(`#7EF473`)으로 착각하는 것. BCG의 primary brand color는 딥 포레스트 그린(`#0E3E1B`)이고, `#7EF473`은 검색 필터 버튼 같은 UI 악센트에만 쓰인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.bcg.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | BCG Design System CSS 변수 포함, Flickity + Video.js 라이브러리 |
| Token prefix | `--BCG-*` (예: `--BCG-Greens-green-700`, `--BCG-Neutrals-neutral-300`) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (대규모 콘텐츠 사이트)
- **Design system**: BCG Design System — prefix `--BCG-*`
- **CSS architecture**: 2-tier 토큰 계층 + 라이브러리 CSS
  ```
  semantic  (--BCG-Greens-*, --BCG-Grays-*, --BCG-Neutrals-*)  브랜드 색상
  component (--followOnBanner-accent-color 등)                  컴포넌트별
  ```
- **Class naming**: 기능적 클래스 (Flickity, Video.js 등 라이브러리 혼용)
- **Default theme**: light (bg = `#FFFFFF`, near-white `#F1EEEA`)
- **Font loading**: 셀프 호스트 — `henderson-bcg-sans`, `henderson-bcg-mod`, `henderson-bcg-serif`, `henderson-bcg-headline`
- **Canonical anchor**: `#0E3E1B` — BCG deep forest green (active nav item bg)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `henderson-bcg-headline` (BCG 독점)
- **Body font**: `henderson-bcg-sans` (BCG 독점)
- **Serif font**: `henderson-bcg-serif` (BCG 독점)
- **Code font**: N/A
- **Weight normal / bold**: `300` / `700`

```css
:root {
  --font-body:     "henderson-bcg-sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-headline: "henderson-bcg-headline", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-serif:    "henderson-bcg-serif", Georgia, serif;
  --font-weight-normal: 300;
  --font-weight-bold:   700;
}
body {
  font-family: var(--font-body);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스 주의**: `henderson-bcg-*` 시리즈는 BCG 독점 폰트. 대체재로 `Helvetica Neue Light` 또는 `Source Sans 3 Light` 사용.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 3.5rem | 700 | 1.05 | -0.02em |
| heading-l | 2.25rem | 700 | 1.15 | -0.01em |
| heading-m | 1.5rem | 700 | 1.25 | 0 |
| heading-s | 1.125rem | 700 | 1.35 | 0 |
| body-lg | 1.125rem | 300 | 1.7 | 0 |
| body | 1rem | 300 | 1.65 | 0 |
| small | 0.875rem | 300 | 1.6 | 0 |
| caption | 0.8125rem | 400 | 1.5 | 0.02em |

> ⚠️ body weight는 300. heading은 700. 중간(400, 500, 600)은 UI 레이블 등에 제한적으로 사용.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp — BCG Greens (5 steps)

| Token | Hex |
|---|---|
| --BCG-Greens-green-100 | #DCF9E3 |
| --BCG-Greens-green-200 | #A8F0B8 |
| --BCG-Greens-green-400 | #21BF61 |
| --BCG-Greens-green-700 | #0E3E1B |
| --BCG-Greens-green-900 | #0B3B23 |

### 06-3. Neutral Ramp

| Step | Light (`BCG-Neutrals`) | Dark (`BCG-Grays`) |
|---|---|---|
| white | #FFFFFF | #212427 |
| 100 | #F1EEEA | #2B333F |
| 200 | #DCD5CE | #696969 |
| 300 | #DFD7CD | #898888 |
| 400 | #C8BFB8 | #CCCCCC |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Lime Green (UI) | accent | #7EF473 |
| Lime Green (light) | accent-light | #65D46E |
| Lime Green (200) | --accent-200 | #7EF473 |
| Lime Green (300) | --accent-300 | #71DC68 |
| Red | error | #D82216 |
| Red (dark) | error-dark | #660F09 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --BCG-Greens-green-700 | #0E3E1B | 브랜드 green, 활성 nav |
| --BCG-Grays-white | #FFFFFF | 배경·CTA 텍스트 |
| --followOnBanner-accent-color | #0B3B23 | 배너 악센트 |
| --accent-200 | #7EF473 | 검색 필터 버튼 |
| --black | #212427 | 주 텍스트 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| --BCG-Greens-green-700 | #0E3E1B | 브랜드 primary |
| --neutral-200 | #F1EEEA | 활성 탭 배경 |
| --BCG-Neutrals-neutral-300 | #DFD7CD | 테두리 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #FFFFFF | 58 | 배경·버튼 텍스트 |
| 2 | #000000 | 20 | 텍스트 (라이브러리) |
| 3 | #212427 | 13 | 주 텍스트 |
| 4 | #73859F | 9 | Video.js 컨트롤 |
| 5 | #F1EEEA | 8 | 활성 탭·배경 |
| 6 | #2B333F | 7 | Video.js 다크 |
| 7 | #0E3E1B | 6 | 브랜드 green, 활성 nav |
| 8 | #696969 | 6 | 보조 텍스트 |
| 9 | #D82216 | 6 | 에러·경고 |
| 10 | #7EF473 | 5 | UI 악센트 (검색 필터) |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| --spacing-8 | 8px | 작은 gap |
| --spacing-32b | 20px | 모바일 패딩 |
| space-sm | 8px | 컴포넌트 내부 |
| space-md | 20px | 섹션 내 |
| space-lg | 40px | 섹션 간 |
| space-xl | 80px | 페이지 레벨 |

**주요 alias**:
- `--spacing-8` → 8px (기본 내부 간격)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| --radius-15 | 15px | 탭 바 컨테이너 |
| --Radii-radii-* | N/A | 컴포넌트별 |
| radius-pill | 20px | 검색 필터 버튼 |
| radius-sm | 2px | 일반 버튼 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-focus | 0 0 0 5px #1199FF | 포커스 링 (Flickity) |
| shadow-card | 0 2px 8px rgba(33,36,39,0.10) | 카드 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭, 텍스트 좌측 + 이미지 우측
- Background: #FFFFFF
- H1: `3.5rem` / weight `700` / tracking `-0.02em`
- Max-width: 1440px

### Section Rhythm
```css
section {
  padding: 80px 40px;
  max-width: 1280px;
}
```

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary Button (Dark Green)

```html
<button class="btn btn--primary">
  Explore Insights
</button>
```

| Spec | Value |
|---|---|
| background | #0E3E1B |
| color | #FFFFFF |
| padding | 12px 24px |
| border-radius | 2px |
| font-weight | 400 |
| font-family | henderson-bcg-sans |

### Search Filter Button

```html
<button class="search-facets-button">
  Filter
</button>
```

| Spec | Value |
|---|---|
| background | #7EF473 |
| color | #212427 (--black) |
| padding | 12px 20px |
| border-radius | 20px |
| font-weight | 400 |
| font-size | 13px |

### Active Nav Tab

```html
<li class="active">
  <a class="menu-item" href="#">Topic</a>
</li>
```

| Spec | Value |
|---|---|
| background | var(--BCG-Greens-green-700, #0E3E1B) |
| color | var(--BCG-Grays-white, #FFFFFF) |
| backdrop-filter | blur() |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 전문적, 통찰 중심, 명사구 | "The Future of AI in Business" |
| Primary CTA | 동사 + 목적어 | "Explore Insights" |
| Secondary CTA | 소문자, 링크형 | "Read more" |
| Subheading | 분석적, 데이터 기반 | |
| Tone | 권위적 전문성, 사실 기반, 과장 금지 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* BCG — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "henderson-bcg-sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 300;
  --font-weight-bold:   700;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #DCF9E3;
  --color-brand-300: #A8F0B8;
  --color-brand-500: #21BF61;
  --color-brand-600: #0E3E1B;   /* ← canonical */
  --color-brand-900: #0B3B23;

  /* Surfaces */
  --bg-page:   #FFFFFF;
  --bg-dark:   #212427;
  --text:      #212427;
  --text-muted:#696969;

  /* Key spacing */
  --space-sm:  8px;
  --space-md:  20px;
  --space-lg:  40px;

  /* Radius */
  --radius-sm: 2px;
  --radius-md: 15px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — BCG
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#DCF9E3',
          300: '#A8F0B8',
          500: '#21BF61',
          600: '#0E3E1B',
          900: '#0B3B23',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F1EEEA',
          200: '#DCD5CE',
          400: '#696969',
          700: '#2B333F',
          900: '#212427',
        },
      },
      fontFamily: {
        sans: ['"henderson-bcg-sans"', '"Helvetica Neue"', 'Helvetica', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '300',
        bold:   '700',
      },
      borderRadius: {
        'sm':   '2px',
        'pill': '20px',
        'nav':  '15px',
      },
      boxShadow: {
        'focus': '0 0 0 5px #1199FF',
        'card':  '0 2px 8px rgba(33,36,39,0.10)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- body weight는 `300`을 쓴다 — BCG 타이포그래피의 핵심
- 브랜드 green은 `#0E3E1B`(딥 포레스트)를 primary로 쓴다
- `#7EF473`(lime green)은 UI 악센트(검색 필터 등)에만 쓴다
- heading은 `font-family: henderson-bcg-headline`, weight `700`
- 텍스트 컬러는 `#212427`(cool dark)을 사용한다

### ❌ DON'T
- `#7EF473`을 브랜드 primary color로 쓰지 않는다 — 악센트 전용
- body weight를 400으로 두지 않는다 — BCG body는 300
- `#D82216`(red)을 브랜드 컬러로 쓰지 않는다 — 에러 전용
- Video.js의 `#73859F`를 UI 색상으로 차용하지 않는다 — 라이브러리 전용
- 과도한 green 사용으로 UI를 채우지 않는다 — green은 포인트만
