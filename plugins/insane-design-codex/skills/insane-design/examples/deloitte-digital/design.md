---
slug: deloitte-digital
service_name: Deloitte Digital
site_url: https://www.deloittedigital.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#000000"
primary_font: Open Sans
font_weight_normal: 300
token_prefix: N/A
---

# DESIGN.md — Deloitte Digital (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Deloitte Digital처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight 300 */
body {
  font-family: "Open Sans", Calibri, sans-serif;
  font-weight: 300;   /* ⚠️ 400 아님. Deloitte Digital body는 300. */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FBFBFB; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백(#FFFFFF)으로 두는 것. Deloitte Digital의 페이지 배경은 `#FBFBFB`(극도로 미세하게 따뜻한 near-white)이며, body weight도 300(light)이다. 400으로 설정하면 비주얼 무게감이 달라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.deloittedigital.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Open Sans 단일 폰트, 최소 CSS 구조 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미발견) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (콘텐츠 중심 컨설팅 사이트)
- **Design system**: Bespoke — Open Sans Light 중심, 흑백 구조
- **CSS architecture**: Flat CSS, Open Sans weight 300 강제
  ```
  core  (직접 hex 값)  텍스트·배경
  comp  (selector)     버튼·카드
  ```
- **Class naming**: 기능적 클래스
- **Default theme**: light (bg = `#FBFBFB`)
- **Font loading**: 외부 로딩 (Google Fonts 또는 셀프 호스트) — `Open Sans` 300 weight
- **Canonical anchor**: `#000000` — primary CTA, 주 텍스트

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Open Sans` (Google Fonts, 오픈소스)
- **Code font**: N/A
- **Weight normal / bold**: `300` / `700`

```css
:root {
  --font-family: "Open Sans", Calibri, sans-serif;
  --font-weight-normal: 300;
  --font-weight-bold:   700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스**: `Open Sans`는 SIL 오픈 폰트 라이선스. 무료 사용·재배포 가능.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 3.5rem | 700 | 1.1 | -0.02em |
| heading-l | 2.25rem | 700 | 1.2 | -0.01em |
| heading-m | 1.625rem | 700 | 1.3 | 0 |
| heading-s | 1.25rem | 700 | 1.35 | 0 |
| body-lg | 1.125rem | 300 | 1.7 | 0 |
| body | 1rem | 300 | 1.65 | 0 |
| small | 0.875rem | 300 | 1.6 | 0 |
| caption | 0.75rem | 400 | 1.5 | 0.02em |

> ⚠️ body weight는 300. heading은 700. Deloitte Digital의 가벼운 Open Sans Light가 콘텐츠 밀도감을 조절한다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-dark | #000000 |
| brand-border | #DCDCDC |
| brand-bg | #FBFBFB |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #000000 |
| 50 | #FBFBFB | #1A1A1A |
| 100 | #F5F5F5 | #2A2A2A |
| 200 | #DCDCDC | #555555 |
| 400 | #B0B0B0 | #808080 |
| 700 | #555555 | #B0B0B0 |
| 900 | #1A1A1A | #FBFBFB |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-page | #FBFBFB | 페이지 배경 (near-white) |
| bg-card | #FFFFFF | 카드 배경 |
| fg-primary | #000000 | 주 텍스트 |
| fg-secondary | #555555 | 보조 텍스트 |
| border | #DCDCDC | 구분선 |
| btn-primary-bg | #000000 | 주 CTA 배경 |
| btn-primary-fg | #FFFFFF | 주 CTA 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #000000 | 13 | 주 텍스트·CTA |
| 2 | #DCDCDC | 13 | 경계선 |
| 3 | #FBFBFB | 13 | 페이지 배경 |

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
| space-xxl | 120px | 대형 영역 |

**주요 alias**:
- `space-lg` → 32px (기본 섹션 패딩)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 카드 (모던 직각) |
| radius-sm | 4px | 버튼 |
| radius-md | 8px | 드롭다운·모달 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 3px rgba(0,0,0,0.06) | 카드 |
| shadow-md | 0 4px 16px rgba(0,0,0,0.08) | 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭, 좌측 텍스트 + 우측 이미지
- Background: #FBFBFB
- H1: `3.5rem` / weight `700` / tracking `-0.02em`
- Max-width: 1280px

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
  Get Started
</button>
```

| Spec | Value |
|---|---|
| background | #000000 |
| color | #FFFFFF |
| padding | 14px 28px |
| border-radius | 4px |
| font-weight | 700 |
| font-family | "Open Sans" |

### Insight Card

```html
<div class="insight-card">
  <div class="insight-card__image">
    <img src="insight.jpg" alt="Insight">
  </div>
  <div class="insight-card__body">
    <span class="insight-card__tag">Technology</span>
    <h3 class="insight-card__title">Insight Title</h3>
    <p class="insight-card__excerpt">Brief description.</p>
  </div>
</div>
```

| Spec | Value |
|---|---|
| border-radius | 0px |
| background | #FFFFFF |
| border | 1px solid #DCDCDC |
| title weight | 700 |
| excerpt weight | 300 |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 혁신·디지털 전환 중심, 동사 강조 | "Transform with Confidence" |
| Primary CTA | 동사구, 제목어 | "Get Started" |
| Secondary CTA | 소문자, 링크형 | "Learn more" |
| Subheading | 기술·비즈니스 결과 중심 | |
| Tone | 기술적 전문성, 미래 지향, 과장 적절히 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Deloitte Digital — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Open Sans", Calibri, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 300;
  --font-weight-bold:   700;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #F5F5F5;
  --color-brand-300: #B0B0B0;
  --color-brand-500: #555555;
  --color-brand-600: #000000;   /* ← canonical */
  --color-brand-900: #000000;

  /* Surfaces */
  --bg-page:   #FBFBFB;
  --bg-dark:   #000000;
  --text:      #000000;
  --text-muted:#555555;

  /* Key spacing */
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  32px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Deloitte Digital
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F5F5F5',
          300: '#B0B0B0',
          500: '#555555',
          600: '#000000',
          900: '#000000',
        },
        neutral: {
          0:   '#FFFFFF',
          50:  '#FBFBFB',
          100: '#F5F5F5',
          200: '#DCDCDC',
          400: '#B0B0B0',
          700: '#555555',
          900: '#1A1A1A',
        },
      },
      fontFamily: {
        sans: ['"Open Sans"', 'Calibri', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '300',
        bold:   '700',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '4px',
        'md':   '8px',
      },
      boxShadow: {
        'sm': '0 1px 3px rgba(0,0,0,0.06)',
        'md': '0 4px 16px rgba(0,0,0,0.08)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- body weight는 `300`(Open Sans Light)을 쓴다
- 배경은 `#FBFBFB`(near-white)로 설정한다 — 순백이 아님
- 경계선은 `#DCDCDC`를 사용한다
- heading은 `font-weight: 700`으로 대비를 준다
- Open Sans는 300 weight 전용으로 로딩한다

### ❌ DON'T
- body weight를 `400`으로 두지 않는다 — 300이 Deloitte Digital 정체성
- 배경을 순백(`#FFFFFF`)으로 두지 않는다 — `#FBFBFB` 사용
- `font-weight: 500`, `600`을 쓰지 않는다
- 브랜드 컬러로 Deloitte 녹색(초록색)을 UI에 넣지 않는다 — Deloitte Digital은 흑백 중심
- `border-radius`에 16px 이상 큰 값을 넣지 않는다
