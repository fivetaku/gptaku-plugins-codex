---
slug: chanel
service_name: Chanel
site_url: https://www.chanel.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#000000"
primary_font: abchanel-2022
font_weight_normal: 400
token_prefix: --color-*
---

# DESIGN.md — Chanel (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Chanel처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "abchanel-2022", "helvetica-adjusted-abchanel-2022", helvetica, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F9F9F9; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: primary 버튼 배경을 회색(`#767676`)으로 두는 것. Chanel의 기본 CTA는 순흑(#000000)이고, `#767676`은 hover/active 상태 전용이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.chanel.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A (대용량 다국어 CSS) |
| CSS files | 다국어별 font-family 분기, CSS 변수 일부 사용 |
| Token prefix | `--color-*` (시맨틱 변수 사용) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (대규모 다국어 e-commerce)
- **Design system**: Bespoke — `abchanel-*` 전용 폰트 시스템, CSS 변수 일부 도입
- **CSS architecture**: 다국어 font-family 분기 + 부분 CSS 변수
  ```
  semantic  (--color-primary, --color-background 등)   브랜드 색상
  component (--search-primary-button-text 등)           컴포넌트별 변수
  ```
- **Class naming**: `.cc-button--primary`, `.cc-button--black` 등 BEM-ish
- **Default theme**: light (bg = `#F9F9F9`)
- **Font loading**: 셀프 호스트 — `abchanel-2022`, `abchanel-corpo`, `futura-pt` 등 다수
- **Canonical anchor**: `#000000` — primary button background

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `abchanel-2022` (Chanel 독점 라이선스)
- **Body font**: `abchanel-corpo` (Chanel 독점)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --color-primary: #000000;
  --color-background: #FFFFFF;
  --color-background-variant: #F9F9F9;
  --color-secondary-light: #767676;
}
body {
  font-family: "abchanel-2022", "helvetica-adjusted-abchanel-2022", helvetica, sans-serif;
  font-weight: 400;
}
```

> **라이선스 주의**: `abchanel-*` 시리즈는 Chanel 독점 폰트. 대체재로 `Futura PT` 또는 `Helvetica Neue` 사용.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 4rem | 300 | 1.0 | -0.02em |
| heading-l | 2rem | 300 | 1.1 | -0.01em |
| heading-m | 1.5rem | 400 | 1.2 | 0 |
| heading-s | 1.125rem | 500 | 1.3 | 0.02em |
| body | 1rem | 400 | 1.6 | 0.01em |
| caption | 0.75rem | 400 | 1.5 | 0.06em |
| label | 0.6875rem | 600 | 1.4 | 0.1em |

> ⚠️ weight 분포: 300~400이 주류(75%), 600은 레이블·UI 요소 전용. 700은 거의 미사용.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (4 steps)

| Token | Hex |
|---|---|
| brand-black | #000000 |
| brand-near-white | #F9F9F9 |
| brand-mid | #767676 |
| brand-white | #FFFFFF |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #000000 |
| 50 | #F9F9F9 | #1D1D1D |
| 100 | #F0F0F0 | #333333 |
| 400 | #A0A0A0 | #767676 |
| 700 | #767676 | #A0A0A0 |
| 900 | #1D1D1D | #F9F9F9 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --color-primary | #000000 | 주 브랜드, CTA 배경 |
| --color-background | #FFFFFF | 기본 배경 |
| --color-background-variant | #F9F9F9 | 보조 배경, CTA 텍스트 |
| --color-secondary-light | #767676 | hover/active 상태 |
| --color-inverted-background | #FFFFFF | 반전 컨텍스트 배경 |
| --color-inverted-primary-variant | #1D1D1D | 반전 컨텍스트 텍스트 |
| --search-primary-button-text | #F9F9F9 | 검색 버튼 텍스트 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| --color-primary | #000000 | 버튼·링크 주색 |
| --color-background-variant | #F9F9F9 | CTA 텍스트·배경 변형 |
| --color-secondary-light | #767676 | 호버 상태 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #F9F9F9 | 높음 | 배경 변형, CTA 텍스트 |
| 2 | #000000 | 높음 | primary CTA, 텍스트 |
| 3 | #FFFFFF | 높음 | 기본 배경 |
| 4 | #767676 | 중간 | hover/active 상태 |
| 5 | #1D1D1D | 낮음 | 반전 컨텍스트 텍스트 |

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
- `space-lg` → 40px (기본 섹션 패딩)

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
| shadow-sm | 0 1px 4px rgba(0,0,0,0.08) | 카드 float |
| shadow-md | 0 4px 12px rgba(0,0,0,0.10) | 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭 이미지, 텍스트 오버레이 (중앙 또는 좌하단)
- Background: #F9F9F9 (텍스트 섹션)
- H1: `4rem` / weight `300` / tracking `-0.02em`
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

### Primary Button (Black)

```html
<button class="cc-button cc-button--primary cc-button--black">
  Shop Now
</button>
```

| Spec | Value |
|---|---|
| background | var(--color-primary, #000000) |
| color | var(--color-background-variant, #F9F9F9) |
| border | 1px solid #000000 |
| padding | 14px 32px |
| border-radius | 0px |
| font-weight | 400 |
| letter-spacing | 0.06em |

*hover*: background `#767676`, border `#767676`

### Secondary Button (White)

```html
<button class="cc-button cc-button--primary cc-button--white">
  Learn More
</button>
```

| Spec | Value |
|---|---|
| background | #FFFFFF |
| color | #1D1D1D |
| border | 1px solid #FFFFFF |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결, 대문자 강조, 이탤릭 간헐 | "THE ART OF GIVING" |
| Primary CTA | 동사 원형, 대문자 | "SHOP NOW" |
| Secondary CTA | 간결, 소문자 | "Discover" |
| Subheading | 시적, 절제된 묘사 | |
| Tone | 고급 절제, 서사적 스토리텔링, 과장 금지 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Chanel — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "abchanel-2022", "helvetica-adjusted-abchanel-2022", helvetica, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold:   600;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #F9F9F9;
  --color-brand-300: #A0A0A0;
  --color-brand-500: #767676;
  --color-brand-600: #000000;   /* ← canonical */
  --color-brand-900: #000000;

  /* Surfaces */
  --bg-page:   #F9F9F9;
  --bg-dark:   #000000;
  --text:      #000000;
  --text-muted:#767676;

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
// tailwind.config.js — Chanel
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F9F9F9',
          300: '#A0A0A0',
          500: '#767676',
          600: '#000000',
          900: '#000000',
        },
        neutral: {
          0:   '#FFFFFF',
          50:  '#F9F9F9',
          100: '#F0F0F0',
          400: '#A0A0A0',
          700: '#767676',
          900: '#1D1D1D',
        },
      },
      fontFamily: {
        sans: ['"abchanel-2022"', '"helvetica-adjusted-abchanel-2022"', 'helvetica', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '600',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '2px',
      },
      boxShadow: {
        'sm': '0 1px 4px rgba(0,0,0,0.08)',
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
- primary button은 `background: #000000`, `color: #F9F9F9`로 설정한다
- hover 상태는 `background: #767676`으로만 처리한다
- `border-radius: 0`을 모든 버튼·카드에 유지한다
- body weight는 400, heading 디스플레이는 300을 쓴다
- 배경은 #F9F9F9(살짝 따뜻한 near-white)로 설정한다

### ❌ DON'T
- `background: #767676`을 기본 버튼에 쓰지 않는다 — hover 전용
- `border-radius`에 큰 값을 넣지 않는다
- 채도 높은 악센트 색상을 UI에 추가하지 않는다
- `font-weight: 700`을 body나 heading에 쓰지 않는다
- 배경을 순백(`#FFFFFF`)으로 두지 않는다 — `#F9F9F9` 사용
