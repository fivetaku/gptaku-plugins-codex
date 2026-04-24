---
schema_version: 3.1
slug: neon
service_name: Neon
site_url: https://neon.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#00E599"
primary_font: Inter
font_weight_normal: 400
token_prefix: --color-*, --font-*, --tw-*

bold_direction: "Electric Postgres"
aesthetic_category: "Cool Productivity"
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Neon (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Neon은 **"Postgres, but electric"**의 브랜드 서사를 디자인에 정확히 심어 넣는다. 페이지 기본은 dark `#0A0A0A`에 가까운 카본 배경에 neon-green `#00E599` (`lab(80.7954% -61.4598 23.582)` lab color space로도 정의되는 정밀한 bio-electric 그린)이 단일 accent로 번진다. `#38A57D` (focus outline), `#00E599` (hover link), `#AFB1B6` (muted text) 페어가 핵심. 그린은 "electrons that glow"의 은유.

색상 전략은 **"Postgres 로고의 돌고래 코랄 → 전자 녹색으로의 재해석"**. neutral dark 위 단일 neon green spike. `.text-with-links a:hover { color: #00E599; border-color: rgba(0,229,153,0.4) }` 처럼 link hover에 neon green ring. text-secondary `#C9CBCF` · text-muted `#AFB1B6`의 슬레이트 계단. 순백은 거의 안 쓰고 `#FAFAFA` off-white + `#F5F5F5` 톤 다운.

타이포그래피는 **Inter Variable** + **Geist Mono** + **esbuild** (자체 호스팅 특수 폰트 — 일부 코드/기술 강조). Vercel 생태계 동조 — Inter 본문, Geist Mono 코드 블록. `--font-weight-semibold: 600` + `--tw-tracking: .02em` (Tailwind v4 축).

레이아웃은 **wide + dense**. max-width 타이트하지 않고 `1440px+`까지 확장. hero는 animated border (위/아래/좌/우 개별 border glow 애니메이션 `.animated-button` 관찰) + 제품 dashboard live view.

인터랙션이 브랜드 특징. `.animated-button`은 top/side/bottom mask-image로 `#000000 → transparent` radial 그라디언트 animation을 돌린다 — neon "electron moving along edge" 효과.

### Key Characteristics

- Dark carbon base + neon green `#00E599` single accent
- Electron border animation (animated-button)
- Inter + Geist Mono + esbuild (특수 폰트) 3종
- Tailwind v4 `--tw-*` 토큰
- lab() color space로 정밀 그린 정의
- Focus outline `#38A57D` (deeper green)
- text 계단: `#FAFAFA` / `#C9CBCF` / `#AFB1B6` / `#AFB1B666`

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Electric Postgres
> **Aesthetic Category**: Cool Productivity
> **Signature Element**: 이 사이트는 **dark carbon + neon green `#00E599` single spike + animated border electron**으로 기억된다.
> **Code Complexity**: medium — Tailwind v4 + lab() color + border animation

---

## 01. Quick Start

> 5분 안에 Neon처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter","Inter Fallback",
    ui-sans-serif,system-ui,sans-serif;
  font-weight: 400;
}

/* 2. Dark bg + text */
:root {
  --bg:      #0A0A0A;
  --surface: #141414;
  --fg:      #FAFAFA;
  --fg-muted: #C9CBCF;
  --border:  #27272A;
}
body { background: var(--bg); color: var(--fg); }

/* 3. Neon green accent */
:root {
  --color-accent:       #00E599;
  --color-accent-soft:  rgba(0,229,153,0.4);
  --color-focus-ring:   #38A57D;
}
a:hover { color: var(--color-accent); }
:focus-visible { outline: 2px solid var(--color-focus-ring); outline-offset: 2px; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 green을 `#10B981` Tailwind emerald로 대체하지 마라. Neon의 그린은 `#00E599` — 더 높은 saturation, lab color space로 정밀 정의된 "전자처럼 빛나는" 값이다. emerald는 leafy green, neon green은 oscilloscope glow.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://neon.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 추출 완료 (Next.js SSR) |
| CSS files | 2개 외부 (총 ~483KB) |
| Token prefix | `--color-*`, `--font-*`, `--tw-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Tailwind v4 (`--tw-*` system)
- **Design system**: Tailwind v4 theme + 자체 `--color-*` semantic
- **CSS architecture**: Tailwind v4 1-tier
  ```
  theme   (--color-*, --font-*)       semantic + font
  tw      (--tw-translate-x 등)       Tailwind v4 variable
  custom  (.animated-button .top)     component class with mask-image
  ```
- **Class naming**: Tailwind utility + component (`.animated-button`, `.text-with-links`)
- **Default theme**: dark
- **Font loading**: Inter + Geist Mono + esbuild + IBM Plex Sans — 모두 self-host
- **Canonical anchor**: `#00E599` green accent (+ `#38A57D` focus ring)

---

## 04. Font Stack

- **Display/Body**: `Inter` + `Inter Fallback`
- **Code**: `GeistMono` / `Geist Mono` + `var(--font-geist-mono)`
- **Tech highlight**: `esbuild` + `esbuild Fallback` (자체 호스팅 — 제품 테크 섹션용)
- **System serif**: `IBM Plex Sans` (부분 사용)
- **Weight normal / bold**: `400` / `600`
- **`--font-weight-semibold`**: `600`

```css
:root {
  --font-inter: "Inter","Inter Fallback";
  --font-geist-mono: "GeistMono",ui-monospace,SFMono-Regular,
    "Roboto Mono",Menlo,Monaco,"Liberation Mono",
    "DejaVu Sans Mono","Courier New",monospace;
  --font-esbuild: "esbuild","esbuild Fallback";
}
body {
  font-family: var(--font-inter),ui-sans-serif,system-ui,sans-serif,
    "Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
}
```

> **라이선스 주의**: esbuild 폰트는 Neon 자체. 복제 시 `JetBrains Mono` 대체.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height |
|---|---|---|---|
| text-xs | `12px` | 400 | 1.5 |
| text-sm | `14px` | 400 | 1.5 |
| text-base | `16px` | 400 | 1.6 |
| text-lg | `18px` | 500 | 1.55 |
| text-xl | `20px` | 600 | 1.4 |
| text-2xl | `24px` | 600 | 1.3 |
| text-3xl | `30px` | 600 | 1.25 |
| text-4xl | `36px` | 600 | 1.2 |
| text-5xl | `48px` | 600 | 1.1 |
| text-6xl | `64px` | 600 | 1.05 |
| display | `80–112px` | 600 | 1 |

> ⚠️ Neon 히어로는 `--tw-tracking: .02em`로 **positive letter-spacing**을 쓰는 드문 경우. 대부분 사이트는 tight tracking을 쓰지만 Neon은 tech/code 느낌을 위해 `.02em` wide.

---

## 06. Colors

### 06-1. Brand Neon Green

| Token | Hex | Notes |
|---|---|---|
| `--color-accent` (canonical) | `#00E599` | neon green · link hover |
| `--color-focus-ring` | `#38A57D` | deeper green focus ring |
| lab-precise | `lab(80.7954% -61.4598 23.582)` | 동일 그린의 lab 표현 |
| accent-soft | `rgba(0,229,153,0.4)` | `#00E59966` · hover border |

### 06-3. Neutral Carbon Ramp

| Step | Hex | Usage |
|---|---|---|
| deepest | `#000000` | mask image base |
| page | `#0A0A0A` | 기본 페이지 배경 |
| surface | `#141414` | 카드 배경 |
| elevated | `#1A1A1A` | hover bg |
| border | `#27272A` | strong border |
| border-soft | `#AFB1B666` | soft border |
| text | `#FAFAFA` | text primary |
| text-secondary | `#C9CBCF` | `.text-with-links a` text |
| text-muted | `#AFB1B6` | muted |
| white | `#FFFFFF` | animated-button `--color` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--bg` | `#0A0A0A` | 페이지 |
| `--fg` | `#FAFAFA` | 본문 |
| `--color-accent` | `#00E599` | link hover / brand |
| `--color-focus-ring` | `#38A57D` | focus outline |
| `--border` | `#27272A` | border |
| `--text-muted` | `#AFB1B6` | 보조 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to |
|---|---|
| `--animated-button-color` | `#FFFFFF` (outline on dark) |
| `--animated-button-mask` | radial-gradient `#000000 → transparent` |
| `.text-with-links a` | color `#C9CBCF` border `rgba(175,177,182,0.4)` |
| `.text-with-links a:hover` | color `#00E599` border `rgba(0,229,153,0.4)` |

### 06-7. Dominant Colors

| Rank | Hex | Role |
|---|---|---|
| 1 | `#0A0A0A` | page bg |
| 2 | `#FAFAFA` | text primary |
| 3 | `#00E599` | neon green accent |
| 4 | `#141414` | surface |
| 5 | `#C9CBCF` | text-with-links |
| 6 | `#AFB1B6` | text muted |
| 7 | `#38A57D` | focus ring |
| 8 | `#27272A` | border |

---

## 07. Spacing

Tailwind v4 `--spacing` base `0.25rem` (4px) + `--tw-translate-*` micro.

| Token | Value |
|---|---|
| 1 | `4px` |
| 2 | `8px` |
| 3 | `12px` |
| 4 | `16px` |
| 6 | `24px` |
| 8 | `32px` |
| 12 | `48px` |
| 16 | `64px` |
| 24 | `96px` |
| 32 | `128px` |
| container | `1440px` |
| prose | `720px` |
| tw-translate-x (micro) | `-1px` | animated-button offset |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| rounded-sm | `2px` | code token |
| rounded | `4px` | small chip |
| rounded-md | `6px` | button, input |
| rounded-lg | `8px` | card |
| rounded-xl | `12px` | card large |
| rounded-2xl | `16px` | hero block |
| rounded-3xl | `24px` | section |
| rounded-full | `9999px` | pill |

---

## 09. Shadows

dark theme — subtle shadow 또는 glow (border animation이 shadow 역할).

| Level | Value | Usage |
|---|---|---|
| shadow-none | `none` | 기본 |
| shadow-glow | `0 0 0 2px rgba(0,229,153,0.3)` | neon focus ring |
| shadow-card | `0 4px 12px rgba(0,0,0,0.4)` | card on dark (template-default) |

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| transition-base | `200ms ease-out` | hover color/bg |
| animated-button | mask-image + transform | electron border animation (시그니처) |
| transition-colors | `150ms` | text/border color |
| scroll-driven | transform | scroll effects |

---

## 11. Layout Patterns

### Grid

- container `1440px`
- prose `720px`
- grid Tailwind 12-col

### Hero

- Pattern: `dark bg + 큰 H1 + animated-button CTA + product dashboard preview`
- Bg: `#0A0A0A` + subtle radial green glow
- H1: Inter 80–112px weight 600 ls `.02em` color `#FAFAFA`

### Section Rhythm

```css
section { padding-block: 96px; padding-inline: 24px; max-width: 1440px; }
```

### Card

- bg `#141414` + border `1px solid #27272A` + radius `12px` + padding `24px`

### Navigation

- height `64px` fixed
- bg `rgba(10,10,10,0.9)` backdrop blur
- link Inter 14px weight 500 color `#C9CBCF` hover `#00E599`

### Animated Button (시그니처)

```css
.animated-button {
  --color: #fff; --top: 0; --side: 0; --bottom: 0;
  position: relative;
}
.animated-button .top {
  top: calc(var(--top) * -1);
  background-image: linear-gradient(to top, transparent 50%, var(--color) 50%);
  background-position: 0 100%;
  bottom: 50%;
  -webkit-mask-image: radial-gradient(/* ... */);
}
.animated-button .bottom { top: 50%; bottom: calc(var(--bottom) * -1); /* 대칭 */ }
```

---

## 12. Responsive Behavior

### Breakpoints (Tailwind)

| Name | Value |
|---|---|
| sm | `≥ 640px` |
| md | `≥ 768px` |
| lg | `≥ 1024px` |
| xl | `≥ 1280px` |
| 2xl | `≥ 1536px` |

### Touch

- min tap `40px`
- button height `40px`

---

## 13. Components

### Buttons

```html
<a class="animated-button">Get started</a>
```

| Variant | bg | color | radius | padding |
|---|---|---|---|---|
| primary (green) | `#00E599` | `#0A0A0A` | `6px` | `8px 16px` |
| animated-border | transparent + border animation | `#FFFFFF` | `6px` | 동일 |
| ghost | transparent + border `#27272A` | `#FAFAFA` | `6px` | 동일 |

### Badges

- bg `rgba(0,229,153,0.1)`
- color `#00E599`
- radius `9999px`
- font Inter 12px weight 500
- padding `2px 8px`

### Cards

- bg `#141414`, border `1px solid #27272A`, radius `12px`, padding `24px`
- hover `border #3A3A40`

### Navigation

- link 14px weight 500 color `#C9CBCF`
- active: color `#FAFAFA` weight 600
- hover: color `#00E599`

### Inputs

- height `40px`, padding `0 12px`
- bg `#141414`, border `1px solid #27272A`
- radius `6px`
- focus: outline `2px solid #38A57D` offset `2px`

### Hero

- bg `#0A0A0A`
- H1 Inter 96px weight 600 ls .02em color `#FAFAFA`
- sub 18px color `#AFB1B6`
- CTA animated-button + ghost

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | tech + 간결 | "Serverless Postgres. Branch like Git." |
| Primary CTA | 동사 | "Get started" |
| Secondary CTA | "See pricing" / "Read docs" | — |
| Subheading | dev 가치 1문장 | "Build faster with Postgres branching." |
| Tone | engineer 화법 | — |

---

## 15. Drop-in CSS

```css
/* Neon — drop-in */
:root {
  --font-inter: "Inter","Inter Fallback",ui-sans-serif,system-ui,sans-serif;
  --font-geist-mono: "GeistMono",ui-monospace,SFMono-Regular,Menlo,monospace;

  --bg:      #0A0A0A;
  --surface: #141414;
  --elevated:#1A1A1A;
  --fg:      #FAFAFA;
  --fg-muted:#AFB1B6;
  --border:  #27272A;

  --color-accent:     #00E599;
  --color-focus-ring: #38A57D;

  --radius:    6px;
  --radius-lg: 12px;
}
body { background: var(--bg); color: var(--fg); font-family: var(--font-inter); }
a:hover { color: var(--color-accent); }
:focus-visible { outline: 2px solid var(--color-focus-ring); outline-offset: 2px; }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Neon
module.exports = {
  theme: {
    extend: {
      colors: {
        neon: {
          bg:      '#0A0A0A',
          surface: '#141414',
          border:  '#27272A',
          text:    '#FAFAFA',
          'text-muted':'#AFB1B6',
          accent:  '#00E599',
          'accent-soft':'rgba(0,229,153,0.4)',
          focus:   '#38A57D',
        },
      },
      fontFamily: {
        sans: ['Inter','ui-sans-serif','system-ui'],
        mono: ['GeistMono','ui-monospace','SFMono-Regular'],
      },
      letterSpacing: { tight:'-0.02em', wide:'.02em' },
      borderRadius: { sm:'2px', DEFAULT:'4px', md:'6px', lg:'8px', xl:'12px', '2xl':'16px', '3xl':'24px', full:'9999px' },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand accent (neon) | `--color-accent` | `#00E599` |
| Focus ring | `--color-focus-ring` | `#38A57D` |
| Background | `--bg` | `#0A0A0A` |
| Surface | `--surface` | `#141414` |
| Text | `--fg` | `#FAFAFA` |
| Text muted | `--fg-muted` | `#AFB1B6` |
| Text secondary | — | `#C9CBCF` |
| Border | `--border` | `#27272A` |

### Example Component Prompts

#### Hero

```
Neon 스타일 히어로를 만들어줘.
- 배경: #0A0A0A + radial-gradient(circle at 80% 30%, rgba(0,229,153,0.08) 0%, transparent 50%)
- H1: Inter, 96px, weight 600, color #FAFAFA, ls .02em (positive tracking!)
- sub: 18px color #AFB1B6
- CTA animated-button (white outline + electron top/bottom border animation)
- 우측 product dashboard screenshot (radius 12px)
```

#### Card

```
Neon 스타일 카드를 만들어줘.
- bg #141414, border 1px solid #27272A, radius 12px, padding 24px
- hover: border #3A3A40, glow 0 0 0 1px rgba(0,229,153,0.2)
- 제목 Inter 20px weight 600 color #FAFAFA
- 본문 16px color #AFB1B6
```

#### Badge (neon)

```
Neon 스타일 배지를 만들어줘.
- font Inter 12px weight 500
- bg rgba(0,229,153,0.1), color #00E599
- radius 9999px, padding 2px 8px
```

### Iteration Guide

- **색상** neon green `#00E599` 고정 (emerald `#10B981` 대체 금지).
- **폰트** Inter + Geist Mono. esbuild 폰트는 선택.
- **tracking** `.02em` positive (Tailwind `tracking-wide`).
- **focus ring** `#38A57D` (deeper green) 2px.
- **animated-button** electron border는 시그니처 — 복제 유지.

---

## 18. DO / DON'T

### ✅ DO

- 배경 `#0A0A0A` dark carbon. pure black 금지 — 미묘한 warm carbon.
- accent green은 `#00E599` 정밀 neon. tailwind emerald 대체 금지.
- focus outline은 `#38A57D` (deeper green) 2px offset 2px.
- text secondary는 `#C9CBCF`, muted는 `#AFB1B6` 2단 계단.
- tracking `.02em` positive (wide) 히어로에.
- animated-button `.top/.bottom` electron 애니메이션 복제.

### ❌ DON'T

- `#10B981` 또는 `#059669` 같은 Tailwind emerald 쓰지 말 것.
- monochrome tight tracking `-0.02em` 쓰지 말 것 (히어로는 wide).
- focus ring을 blue로 쓰지 말 것 — 반드시 `#38A57D` green.
- 카드에 shadow 강하게 쓰지 말 것 — 미묘한 border가 더 Neon.
- light 테마 기본 금지 — Neon은 dark-first.
