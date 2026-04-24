---
schema_version: 3.1
slug: lemon-squeezy
service_name: Lemon Squeezy
site_url: https://www.lemonsqueezy.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#5423E7"
primary_font: Circularpro book
font_weight_normal: 400
token_prefix: --ls-*, --purple-*, --gray-*

bold_direction: "Playful Commerce"
aesthetic_category: "Playful Precision"
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Lemon Squeezy (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Lemon Squeezy의 마케팅 사이트는 "Merchant of Record를 재미있게 판다"는 브랜드 정신을 시각화한다. 페이지는 dark `#121217` (`--black-2`) 기반에 핵심 브랜드 **purple `#5423E7`** (`--ls-purple`)가 hero·CTA·스크롤 하이라이트에 반복된다. 보색으로 **yellow `#FFC233`** (`--ls-color-yellow`)이 citrus accent처럼 hero 피그·레몬 일러스트에 등장. purple과 yellow의 대비가 "Lemon × Squeezy"의 바로 그 톤이다.

색상 전략은 **"purple × yellow + hot accent"**의 3축이다. `--ls-purple #5423E7` (primary) · `--purple-500 #7047EB` (hover tint) · `--purple-600 #5423E7` (base) · yellow `#FFC233` (accent) · yellow-lighter `#FFD266` (accent soft). 거기에 hot pink `#DB0BB9` (`--pink-700`) 포인트가 hero CTA나 badge로 한두 번 등장. 텍스트 계층은 `#121217` (black-2 on light) / `#FFFFFF` (white on dark) + `#6C6C89` (`--gray-500`) muted.

타이포그래피는 **Circularpro book** (Lineto, 유료, 1st choice) + **Circularxx** (variant) + fallback으로 **Inter**. circular 계열은 둥근 o/a 글리프가 시그니처 — Airbnb, Spotify도 쓰는 라인. 코드는 **JetBrains Mono** (`Jetbrainsmono`).

레이아웃은 **스토리텔링형 스크롤** — dark hero → 제품 설명 → pricing → CTA 연결. Webflow로 제작되어 `.w-button`, `.w-slider-*`, `.w-dropdown-*` 등 Webflow util class가 DOM에 노출된다. max-width `1280px` 기본, hero는 full-bleed.

인터랙션은 Webflow interactions로 scroll-driven reveal + hover scale. transition `.2s ease-out` 표준.

### Key Characteristics

- Purple `#5423E7` (--ls-purple) 브랜드 primary + yellow `#FFC233` citrus accent
- Dark `#121217` 기반 (black-2)
- Circularpro book 폰트 — 라운드 글리프
- Webflow 빌드 (`.w-button`, `.w-slider` 등 util)
- Hot pink `#DB0BB9` 소량 포인트
- purple hover tint `#7047EB`로 layering

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Playful Commerce
> **Aesthetic Category**: Playful Precision
> **Signature Element**: 이 사이트는 **dark `#121217` 위 purple `#5423E7` × yellow `#FFC233` 대비와 Webflow 스토리텔링 스크롤**로 기억된다.
> **Code Complexity**: medium — Webflow util + CSS variable purple/yellow swap

---

## 01. Quick Start

> 5분 안에 Lemon Squeezy처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Circularpro book","Circularxx",Inter,
    -apple-system,BlinkMacSystemFont,sans-serif;
  font-weight: 400;
}

/* 2. Dark bg + text */
:root {
  --black-2: #121217;
  --ls-white: #FFFFFF;
  --gray-500: #6C6C89;
}
body { background: var(--black-2); color: var(--ls-white); }

/* 3. Brand purple × yellow */
:root {
  --ls-purple:   #5423E7;
  --purple-500:  #7047EB;
  --ls-color-yellow: #FFC233;
  --pink-700:    #DB0BB9;
}
```

**절대 하지 말아야 할 것 하나**: purple을 다른 purple hex로 바꾸지 마라. `#5423E7`이 canonical anchor. `#6D28D9` 같은 tailwind violet으로 대체하면 "Lemon Squeezy다움"이 사라진다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.lemonsqueezy.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 추출 완료 (Webflow build) |
| CSS files | 2개 (inline 6KB + Webflow shared 304KB) |
| Token prefix | `--ls-*`, `--purple-*`, `--gray-*`, Webflow `.w-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: **Webflow** (`lemon-squeezy-staging.shared.d81ccb696.min.css`)
- **Design system**: `--ls-*` (색) + `--purple-*` (브랜드 ramp) + `--gray-*` (neutral) + Webflow util
- **CSS architecture**: flat semantic + utility
  ```
  brand   (--ls-purple, --ls-color-yellow)    canonical hex
  ramp    (--purple-500, --purple-600, --gray-500, --pink-700)
  webflow (.w-button, .w-slider-*)            util class
  ```
- **Class naming**: Webflow BEM (`.nav_menu`, `.nav_dropdown-link`, `.w-button`)
- **Default theme**: dark (`#121217`) + light blocks 혼용
- **Font loading**: Circularpro (자체 호스팅) + Inter fallback + JetBrains Mono
- **Canonical anchor**: `#5423E7` (`--ls-purple`) + `#FFC233` (yellow) 페어

---

## 04. Font Stack

- **Display/Body**: `Circularpro book` (Lineto, 유료)
- **Display alt**: `Circularxx`
- **Fallback**: `Inter`, `Arial`, `Helvetica Neue`, `Helvetica`, `Ubuntu`, `Segoe UI`, `Verdana`, `sans-serif`
- **Code**: `Jetbrainsmono` (JetBrains Mono)
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --ls-font-sans: "Circularpro book","Circularxx",Inter,
    "Helvetica Neue",Helvetica,Ubuntu,"Segoe UI",Verdana,sans-serif;
  --ls-font-mono: "Jetbrainsmono",ui-monospace,"SF Mono",Menlo,monospace;
}
body { font-family: var(--ls-font-sans); }
```

> **라이선스 주의**: Circularpro는 유료. 복제 시 `Nunito` 또는 `Poppins` 대체 (라운드 글리프 유지).

---

## 05. Typography Scale

| Token | Size | Weight | Line-height |
|---|---|---|---|
| caption | `12px` | 400 | 1.5 |
| small | `14px` | 400 | 1.5 |
| body | `16px` | 400 | 1.6 |
| lead | `18px` | 400 | 1.55 |
| h4 | `20px` | 500 | 1.4 |
| h3 | `24px` | 600 | 1.3 |
| h2 | `36px` | 600 | 1.2 |
| h1 | `48px` | 600 | 1.1 |
| display | `72–96px` | 600 | 1.05 |

> ⚠️ Circular 계열은 rounded glyph 덕에 같은 size에서도 Inter보다 약간 커 보인다. body `16px`가 충분.

---

## 06. Colors

### 06-1. Brand Purple Ramp

| Token | Hex |
|---|---|
| `--purple-500` (light hover) | `#7047EB` |
| `--purple-600` (brand base) | `#5423E7` |
| `--ls-purple` (canonical) | `#5423E7` |

### 06-2. Citrus Accent (Yellow)

| Token | Hex |
|---|---|
| `--ls-color-yellow` | `#FFC233` |
| `--ls-color-yellow-lighter` | `#FFD266` |

### 06-3. Neutral

| Step | Hex | Usage |
|---|---|---|
| `--black-2` | `#121217` | dark page bg |
| `--ls-white` | `#FFFFFF` | light bg / text on dark |
| `--gray-500` | `#6C6C89` | text muted |
| `--bullet-point-color` | `#6C6C89` | list marker |
| `--light-white` | `#fff9` (56% α) | overlay text on dark |

### 06-4. Accent Families

| Family | Hex | Use |
|---|---|---|
| pink-700 | `#DB0BB9` | hot accent (rare) |
| webflow-blue | `#3898EC` | Webflow default button (before override) |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| body-bg | `#121217` | dark primary |
| body-fg | `#FFFFFF` | text on dark |
| primary-btn-bg | `#5423E7` | CTA bg |
| primary-btn-fg | `#FFFFFF` | CTA text |
| accent-yellow | `#FFC233` | highlight, illustration |
| muted-fg | `#6C6C89` | meta text |
| input-bg | `#FAFAFA` (light) | form bg |
| input-border | `#CCCCCC` | form border |

### 06-6. Semantic Alias Layer

| Alias | Resolves to |
|---|---|
| `--button-primary-light` | `#FFFFFFE6` · light-on-dark button |
| `--ls-purple` | `#5423E7` |
| `--gray-500` | `#6C6C89` |

### 06-7. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Role |
|---|---|---|
| 1 | `#FFFFFF` | text on dark |
| 2 | `#121217` | dark page |
| 3 | `#5423E7` | brand purple |
| 4 | `#FFC233` | yellow accent |
| 5 | `#6C6C89` | gray muted |
| 6 | `#7047EB` | purple hover |
| 7 | `#DB0BB9` | hot pink accent |
| 8 | `#222222` | webflow slider nav bg (override) |

---

## 07. Spacing

Webflow spacing + 4–8px 배수.

| Token | Value |
|---|---|
| space-2 | `8px` |
| space-3 | `12px` |
| space-4 | `16px` |
| space-6 | `24px` |
| space-8 | `32px` |
| space-12 | `48px` |
| space-16 | `64px` |
| section-pad | `96px` |
| container | `1280px` |
| prose | `680px` |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| radius-sm | `8px` | chip/badge |
| radius | `12px` | button, input |
| radius-md | `16px` | card |
| radius-lg | `24px` | hero block |
| pill | `100px` (scrollbar thumb 관찰 — 실제 `100px`이 scrollbar에 쓰임) | |
| full | `9999px` | avatar, pill |

---

## 09. Shadows

| Level | Value | Usage |
|---|---|---|
| subtle | `0 0 3px #3336` | slider nav (Webflow util) |
| card | `0 4px 12px rgba(0,0,0,0.08)` | card rest (template-default) |
| elevated | `0 8px 24px rgba(0,0,0,0.12)` | modal (template-default) |

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| transition-base | `.2s ease-out` | hover |
| webflow-scroll | scroll-driven | section reveal |
| dropdown-toggle | `.2s` | `.w-dropdown` |

---

## 11. Layout Patterns

### Grid

- container `1280px`, hero full-bleed
- `.w-*` Webflow grid util

### Hero

- Pattern: `dark bg + 큰 H1 purple × yellow illustration + 듀얼 CTA`
- Bg: `#121217` + radial purple glow
- H1: `Circularpro book 72–96px weight 600 color #FFFFFF`
- Illustration: 레몬 + 스크러빙 모션 (SVG/Lottie)

### Section Rhythm

```css
section { padding-block: 96px; padding-inline: 24px; max-width: 1280px; }
```

### Card

- bg `#1C1C24` (dark surface, 관찰)
- border `1px solid rgba(255,255,255,0.1)`
- radius `16px`
- padding `24px`
- shadow none

### Navigation

- height `72px` fixed top
- bg `rgba(18,18,23,0.9)` backdrop blur
- 로고 + 링크 + Sign in + Sign up (yellow CTA)

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value |
|---|---|
| Mobile | `< 768px` |
| Tablet | `≥ 768px` |
| Desktop | `≥ 1024px` |
| Large | `≥ 1280px` |

### Touch/Collapsing

- min tap `44px`
- nav 햄버거 &lt;768px
- 2-col hero → 1-col mobile

---

## 13. Components

### Buttons

```html
<a class="w-button ls-cta-primary">Start for free</a>
```

| Variant | bg | color | radius | padding |
|---|---|---|---|---|
| primary (yellow) | `#FFC233` | `#121217` | `12px` | `12px 24px` |
| primary (purple) | `#5423E7` | `#FFFFFF` | `12px` | `12px 24px` |
| ghost | transparent + border | `#FFFFFF` | `12px` | 동일 |
| pill | 좌동 | 좌동 | `9999px` | 동일 |

### Badges

- bg `rgba(84,35,231,0.2)` (`--ls-purple` 20α)
- color `#FFFFFF` or `#FFC233`
- radius `9999px`
- font `Circularpro 12px weight 500`
- padding `4px 10px`

### Cards

- bg `#1C1C24`, border `1px solid rgba(255,255,255,0.08)`, radius `16px`, padding `24px`
- hover: `transform translateY(-2px)` + border `rgba(255,255,255,0.2)`

### Navigation

- `.nav_menu` container
- link Circular 14px weight 500 color `rgba(255,255,255,0.8)`
- hover color `#FFFFFF`
- active: underline purple

### Inputs

- height `48px`, padding `0 16px`
- bg `#FAFAFA` (light) or `#1C1C24` (dark)
- border `1px solid #CCCCCC` (light) / `rgba(255,255,255,0.1)` (dark)
- radius `12px`
- focus: `outline 2px solid #5423E7`

### Hero

- bg `#121217` + purple radial gradient
- H1 96px weight 600 color `#FFFFFF`
- sub 18px color `rgba(255,255,255,0.7)`
- CTA primary (yellow pill) + secondary (ghost)
- SVG illustration 레몬 + 스크러버

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 위트 + 직설 | "Sell anything, anywhere in the world." |
| Primary CTA | 2–3 단어 | "Start for free" / "Get started" |
| Secondary CTA | 정보형 | "Learn how it works" |
| Subheading | MoR 강조 | "Merchant of Record for digital products." |
| Tone | 가볍고 친근 + pro | — |

---

## 15. Drop-in CSS

```css
/* Lemon Squeezy — drop-in */
:root {
  --ls-font-sans: "Circularpro book",Inter,-apple-system,sans-serif;
  --ls-font-mono: "Jetbrainsmono",ui-monospace,Menlo,monospace;

  --black-2: #121217;
  --ls-white: #FFFFFF;
  --gray-500: #6C6C89;
  --light-white: #fff9;

  --ls-purple:   #5423E7;
  --purple-500:  #7047EB;
  --purple-600:  #5423E7;

  --ls-color-yellow: #FFC233;
  --ls-color-yellow-lighter: #FFD266;

  --pink-700: #DB0BB9;

  --radius-sm: 8px;
  --radius:    12px;
  --radius-md: 16px;
  --radius-lg: 24px;
}
body { background: var(--black-2); color: var(--ls-white); font-family: var(--ls-font-sans); }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Lemon Squeezy
module.exports = {
  theme: {
    extend: {
      colors: {
        ls: {
          bg:     '#121217',
          white:  '#FFFFFF',
          purple: '#5423E7',
          'purple-hover': '#7047EB',
          yellow: '#FFC233',
          'yellow-soft': '#FFD266',
          pink:   '#DB0BB9',
          gray:   '#6C6C89',
        },
      },
      fontFamily: {
        sans: ['Circularpro book','Inter','system-ui'],
        mono: ['Jetbrainsmono','ui-monospace'],
      },
      borderRadius: { sm:'8px', DEFAULT:'12px', md:'16px', lg:'24px', full:'9999px' },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary (purple) | `--ls-purple` | `#5423E7` |
| Brand accent (yellow) | `--ls-color-yellow` | `#FFC233` |
| Background | `--black-2` | `#121217` |
| Text primary | `--ls-white` | `#FFFFFF` |
| Text muted | `--gray-500` | `#6C6C89` |
| Hot accent | `--pink-700` | `#DB0BB9` |

### Example Component Prompts

#### Hero

```
Lemon Squeezy 스타일 히어로를 만들어줘.
- 배경: #121217 + radial-gradient(#5423E7 0%, transparent 60%)
- H1: Circularpro book, 96px, weight 600, color #FFFFFF
- sub: 18px color rgba(255,255,255,0.7)
- CTA primary: bg #FFC233, color #121217, radius 9999px, padding 14px 28px
- CTA secondary: bg transparent border 1px solid rgba(255,255,255,0.2)
- 좌측 텍스트 + 우측 SVG 레몬 일러스트
```

#### Card

```
Lemon Squeezy 스타일 카드를 만들어줘.
- bg #1C1C24, border 1px solid rgba(255,255,255,0.08), radius 16px, padding 24px
- 제목 Circular 20px weight 500
- 본문 16px color rgba(255,255,255,0.7)
- hover: translateY(-2px), border rgba(255,255,255,0.2)
```

#### Badge

```
Lemon Squeezy 스타일 배지를 만들어줘.
- font Circular 12px weight 500
- bg rgba(84,35,231,0.2), color #FFC233
- radius 9999px padding 4px 10px
```

### Iteration Guide

- **색상** purple `#5423E7` × yellow `#FFC233` 페어 유지. 한 쌍이 브랜드.
- **폰트** Circular 대체 시 Nunito/Poppins (라운드 글리프).
- **다크 기본** `#121217` 고정.
- **pill CTA** yellow primary는 pill (radius 9999px)로 쓰는 게 시그니처.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 `#121217` dark primary. pure black 금지.
- primary CTA는 yellow `#FFC233` 배경 + `#121217` 텍스트 + pill radius.
- purple `#5423E7`은 secondary CTA, link, accent에만.
- 본문 Circular `16px` weight `400`.
- 카드 bg `#1C1C24` (slightly lighter than page).

### ❌ DON'T

- purple을 `#6D28D9` 같은 Tailwind violet으로 대체 금지.
- yellow를 `#F59E0B` 같은 amber로 바꾸지 말 것 — `#FFC233` citrus 고유.
- body weight `500` 이상 금지.
- 카드에 강한 shadow 금지.
- monochrome dark 레이아웃 금지 — yellow 포인트 하나는 반드시 넣기.
