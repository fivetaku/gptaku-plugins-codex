---
schema_version: 3.1
slug: github
service_name: GitHub
site_url: https://github.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#1F6FEB"
primary_font: Mona Sans
font_weight_normal: 400
token_prefix: --fgColor-*, --bgColor-*, --borderColor-*, --button-*

bold_direction: "Industrial Engineering"
aesthetic_category: "Cool Productivity"
signature_element: minimal_extreme
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — GitHub (Codex Edition)

---

## 00. Visual Theme & Atmosphere

GitHub의 랜딩/홈 디자인은 **Primer Design System**의 산물이다. 20개가 넘는 테마 CSS 파일(`dark`, `dark_colorblind`, `dark_dimmed`, `dark_high_contrast`, `dark_tritanopia`, 그리고 light 동일 계열)이 각각 독립된 팔레트로 분리돼 있는 점 자체가 시그니처 — GitHub은 **접근성(WCAG)을 디자인 시스템의 1급 시민**으로 대우한다. 기본은 dark `#0D1117` 페이지 배경에 순백에 가까운 텍스트.

색상 전략은 **"의미론적 semantic token이 전부"**다. `--fgColor-*`, `--bgColor-*`, `--borderColor-*`, `--button-*`, `--reactionButton-*` 같은 role 이름의 alias만 UI 코드에 쓰이고, raw hex는 `--base-color-*` 1-tier에만 존재한다. 브랜드 green `#2DA44E` (정확히는 dark에서 `#2E9A40` active · `#29903B` hover) + accent blue `#1F6FEB`가 핵심. 파란색은 주로 link/focus/accent, 초록은 primary CTA + success.

타이포그래피는 **Mona Sans** (GitHub 자체 variable font, OFL) + **Hubot Sans** 일부 + `system-ui` fallback이 기본. 코드는 당연히 **SF Mono** 또는 **Consolas**. variable axis로 `400 / 500 / 600` 주류에 hero 타이틀은 `700`. body `16px` 기준.

레이아웃은 **좁은 content 중앙 + 양옆 여백** — max-width `1280px`. hero는 dark gradient 위에 cyan accent 빛이 번지는 패턴 (`#388BFD` soft glow). 카드는 `border-radius: 6–12px` 소박하게. shadow는 정교한 dual-layer (`--shadow-small`, `--shadow-medium`, `--shadow-large`).

인터랙션은 **절제된 즉시성**. button hover는 `background-color` 변화만 (`#2E9A40 → #29903B`). 긴 transition 없음.

### Key Characteristics

- 멀티 테마 (light/dark × colorblind/tritanopia × high-contrast/dimmed) 8–10 분기
- Primer semantic alias layer (`--fgColor-*` / `--bgColor-*`)
- Brand green primary `#2DA44E` + blue accent `#1F6FEB`
- Mona Sans variable font + system-ui fallback
- Content max 1280px
- Radius 6–12px 소박
- 접근성 1급 — colorblind / tritanopia / high-contrast variant 존재

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Industrial Engineering
> **Aesthetic Category**: Cool Productivity
> **Signature Element**: 이 사이트는 **Primer의 semantic token 2-tier + 다중 테마 분기 (colorblind/tritanopia/high-contrast)**로 기억된다.
> **Code Complexity**: high — semantic alias 수백 개, theme 분기, variable font

---

## 01. Quick Start

> 5분 안에 GitHub처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Mona Sans","Hubot Sans",-apple-system,BlinkMacSystemFont,
    "Segoe UI","Noto Sans","Helvetica","Arial",sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 (dark default) */
:root {
  --bgColor-default: #0D1117;
  --bgColor-muted:   #010409;
  --fgColor-default: #E6EDF3;
  --fgColor-muted:   #8B949E;
  --borderColor-default: #30363D;
}
body { background: var(--bgColor-default); color: var(--fgColor-default); }

/* 3. Primary CTA green */
:root {
  --button-primary-bgColor-rest:   #2DA44E;
  --button-primary-bgColor-hover:  #29903B;
  --button-primary-bgColor-active: #2E9A40;
  --fgColor-accent: #4493F8;
}
```

**절대 하지 말아야 할 것 하나**: raw hex `#0D1117`, `#2DA44E` 등을 컴포넌트 CSS에 직접 쓰지 마라. GitHub은 **무조건 semantic alias (`--bgColor-default`, `--button-primary-bgColor-rest`)로만** 참조한다. raw hex 사용은 테마 분기를 불가능하게 만든다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://github.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 추출 완료 |
| CSS files | 25개 외부 (테마 variant 포함) |
| Token prefix | `--fgColor-*`, `--bgColor-*`, `--borderColor-*`, `--button-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Rails + React view hydration
- **Design system**: **Primer Design System** — prefix `--fgColor-*`, `--bgColor-*`, `--button-*`
- **CSS architecture**: 2-tier (base + semantic)
  ```
  base    (--base-color-{hue}-{step})     raw hex values
  semantic(--fgColor-*, --bgColor-*)       semantic alias (컴포넌트 사용)
  ```
- **Theme variants**: `dark`, `dark_colorblind`, `dark_colorblind_high_contrast`, `dark_dimmed`, `dark_dimmed_high_contrast`, `dark_high_contrast`, `dark_tritanopia`, `dark_tritanopia_high_contrast`, `light`, `light_colorblind`, `light_colorblind_high_contrast`, `light_high_contrast`, `light_tritanopia`, `light_tritanopia_high_contrast`
- **Class naming**: BEM + utility (`primer-react-css__xxx`)
- **Default theme**: dark (`#0D1117`)
- **Font loading**: Mona Sans (variable) + Hubot Sans + system-ui
- **Canonical anchor**: `#2DA44E` button primary + `#1F6FEB` accent emphasis

---

## 04. Font Stack

- **Display/Body**: `Mona Sans` (GitHub OFL variable font)
- **Display alt**: `Hubot Sans` (GitHub variable)
- **Code**: `ui-monospace`, `SFMono-Regular`, `SF Mono`, `Menlo`, `Consolas`, `Liberation Mono`, `monospace`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --fontStack-sansSerif: "Mona Sans","Hubot Sans",-apple-system,BlinkMacSystemFont,
    "Segoe UI","Noto Sans","Helvetica","Arial",sans-serif,
    "Apple Color Emoji","Segoe UI Emoji";
  --fontStack-monospace: ui-monospace,SFMono-Regular,"SF Mono",Menlo,
    Consolas,"Liberation Mono",monospace;
}
```

---

## 05. Typography Scale

| Token | Size | Weight | Line-height |
|---|---|---|---|
| `--text-caption-size` | `12px` | 400 | 1.5 |
| `--text-body-size-small` | `12px` | 400 | 1.4 |
| `--text-body-size-medium` | `14px` | 400 | 1.5 |
| `--text-body-size-large` | `16px` | 400 | 1.6 |
| `--text-subtitle-size-large` | `20px` | 500 | 1.4 |
| `--text-title-size-small` | `24px` | 600 | 1.3 |
| `--text-title-size-medium` | `32px` | 600 | 1.25 |
| `--text-title-size-large` | `40px` | 600 | 1.15 |
| `--text-display-size` | `48–72px` | 700 | 1.1 |

> ⚠️ GitHub body는 `14px` (small) 기반 · 마케팅 home은 `16px` (large). 섹션마다 base 폰트 크기가 다르니 주의.

---

## 06. Colors

### 06-1. Brand Green (primary CTA)

| Token | Hex |
|---|---|
| `--button-primary-bgColor-rest` | `#2DA44E` (light) / `#238636` (dark) |
| `--button-primary-bgColor-hover` | `#29903B` |
| `--button-primary-bgColor-active` | `#2E9A40` |
| `--button-primary-bgColor-disabled` | `#105823` |
| `--button-primary-fgColor-rest` | `#FFFFFF` |
| `--button-primary-fgColor-disabled` | `rgba(255,255,255,0.4)` (`#FFFFFF66`) |
| `--button-primary-borderColor-disabled` | `#105823` |

### 06-2. Accent Blue

| Token | Hex |
|---|---|
| `--fgColor-accent` | `#4493F8` |
| `--bgColor-accent-emphasis` | `#1F6FEB` |
| `--bgColor-accent-muted` | `rgba(56,139,253,0.1)` (`#388BFD1A`) |
| `--borderColor-accent-emphasis` | `#1F6FEB` |
| `--borderColor-accent-muted` | `rgba(56,139,253,0.4)` (`#388BFD66`) |

### 06-3. Neutral Dark (page + surface)

| Step | Hex | Usage |
|---|---|---|
| `--bgColor-default` | `#0D1117` | 페이지 배경 |
| `--bgColor-muted` | `#010409` | subtle secondary bg |
| `--bgColor-subtle` | `#161B22` | card bg |
| `--bgColor-inset` | `#161B22` | inner bg |
| `--bgColor-emphasis` | `#6E7681` | emphasis bg |
| `--borderColor-default` | `#30363D` | 기본 border |
| `--borderColor-muted` | `#21262D` | soft border |
| `--fgColor-default` | `#E6EDF3` | text primary |
| `--fgColor-muted` | `#8B949E` | text muted |
| `--fgColor-subtle` | `#6E7681` | text subtle |

### 06-4. Neutral Light

| Step | Hex |
|---|---|
| `--bgColor-default` (light) | `#FFFFFF` |
| `--bgColor-muted` (light) | `#F6F8FA` |
| `--bgColor-subtle` (light) | `#F6F8FA` |
| `--fgColor-default` (light) | `#1F2328` |
| `--fgColor-muted` (light) | `#59636E` |
| `--borderColor-default` (light) | `#D1D9E0` |

### 06-4b. Accent Families (status)

| Family | Hex | Use |
|---|---|---|
| open (green) | `#2DA44E` | primary action, success |
| closed (red) | `#CF222E` | danger, closed |
| merged (purple) | `#8250DF` | merged PR |
| attention (yellow) | `#9A6700` | attention, warning |
| sponsors (pink) | `#BF3989` | sponsors |
| done (purple) | `#8250DF` | done state |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--fgColor-default` | `#E6EDF3` (dark) / `#1F2328` (light) | text primary |
| `--bgColor-default` | `#0D1117` (dark) / `#FFFFFF` (light) | bg primary |
| `--button-primary-bgColor-rest` | `#2DA44E` | CTA primary |
| `--fgColor-accent` | `#4493F8` | link, accent text |
| `--bgColor-accent-emphasis` | `#1F6FEB` | accent bg |
| `--borderColor-default` | `#30363D` (dark) / `#D1D9E0` (light) | border |
| `--reactionButton-selected-bgColor-rest` | `rgba(56,139,253,0.2)` | 이모지 반응 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to |
|---|---|
| `--fgColor-*` | `--base-color-{hue}-{step}` |
| `--button-primary-bgColor-rest` | `--base-color-green-5` (대략) |
| `--reactionButton-selected-fgColor-hover` | `#79C0FF` |
| `--topicTag-borderColor` | `transparent` |

### 06-7. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Role |
|---|---|---|
| 1 | `#0D1117` | dark page bg |
| 2 | `#FFFFFF` | light bg / text on dark |
| 3 | `#E6EDF3` | text primary dark |
| 4 | `#2DA44E` | button primary |
| 5 | `#30363D` | border dark |
| 6 | `#1F6FEB` | accent emphasis |
| 7 | `#161B22` | card bg |
| 8 | `#8B949E` | text muted dark |
| 9 | `#4493F8` | link accent |
| 10 | `#CF222E` | closed/danger red |

---

## 07. Spacing

Primer spacing scale — 4px 배수.

| Token | Value | Use |
|---|---|---|
| `--base-size-4` | `4px` | micro gap |
| `--base-size-8` | `8px` | small gap |
| `--base-size-12` | `12px` | form gap |
| `--base-size-16` | `16px` | 기본 padding |
| `--base-size-24` | `24px` | card padding |
| `--base-size-32` | `32px` | section inner |
| `--base-size-40` | `40px` | large gap |
| `--base-size-48` | `48px` | hero spacing |
| `--base-size-64` | `64px` | section block |
| content-max | `1280px` | content wrapper |
| container-narrow | `768px` | narrow prose |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `--borderRadius-small` | `4px` | inner chip |
| `--borderRadius-medium` | `6px` | button, input, card |
| `--borderRadius-large` | `12px` | large card, modal |
| `--borderRadius-full` | `9999px` | avatar, label pill |

---

## 09. Shadows

| Level | Value | Usage |
|---|---|---|
| `--shadow-resting-small` | `0 1px 0 rgba(31,35,40,0.04)` | button rest (light) |
| `--shadow-resting-medium` | `0 3px 6px rgba(140,149,159,0.15)` | card (light) |
| `--shadow-floating-small` | `0 8px 24px rgba(140,149,159,0.2)` | popover |
| `--shadow-floating-large` | `0 16px 32px rgba(31,35,40,0.15)` | modal |
| dark variant | shadow opacity ↑ | dark theme |

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| transition-short | `80ms ease-out` | button hover |
| transition-base | `160ms ease-out` | color/bg change |
| ease-default | `cubic-bezier(0.33,1,0.68,1)` | 기본 easing |

---

## 11. Layout Patterns

### Grid System

- **max-width**: `1280px` (full-width-container)
- **narrow**: `768px`
- **gutter**: `24px`
- **grid type**: 12-col CSS Grid

### Hero

- **Pattern Summary**: `~70vh dark bg + 중앙 H1 48–72px + cyan glow accent + 듀얼 CTA primary green / ghost`
- Layout: 1-col 중앙 + 우측 product mockup (opt)
- Background: `#0D1117` + radial blue glow
- **Background Treatment**: `solid near-black + radial blue accent glow`
- H1: `48–72px / weight 700 / ls -0.02em`
- Max-width: `1280px`

### Section Rhythm

```css
section { padding-block: 64px; padding-inline: 24px; max-width: 1280px; }
```

### Card Patterns

- bg: `#161B22` (dark) / `#FFFFFF` (light)
- border: `1px solid #30363D` (dark) / `#D1D9E0` (light)
- radius: `6–12px`
- padding: `16–24px`
- hover: `border #8B949E`

### Navigation

- type: horizontal desktop / hamburger mobile
- position: fixed top 0
- height: `64px`
- bg: `#0D1117` dark / `#FFFFFF` light
- border: 하단 `1px solid #30363D`

### Content Width

- prose: `768px`
- container: `1280px`

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value |
|---|---|
| Mobile | `< 768px` |
| Tablet | `≥ 768px` |
| Desktop | `≥ 1012px` |
| Large | `≥ 1280px` |
| XL | `≥ 1400px` |

### Touch Targets

- min tap: `32px` (primer)
- button height: `32–40px`
- input height: `32–40px`

### Collapsing

- nav: &lt;768px 햄버거
- grid: 12→1 reset
- hero: 2-col → 1-col

### Image Behavior

- strategy: img srcset + `loading="lazy"`
- max-width: `100%`

---

## 13. Components

### Buttons

```html
<button class="Button Button--primary">Sign up</button>
```

| Variant | bg | color | radius | padding |
|---|---|---|---|---|
| primary (green) | `#2DA44E` | `#FFFFFF` | `6px` | `5px 16px` |
| default | `#21262D` (dark) | `#C9D1D9` | `6px` | 동일 |
| outline | transparent + border | accent | `6px` | 동일 |
| danger | `#CF222E` | `#FFFFFF` | `6px` | 동일 |

### Badges (Label)

- bg: `--bgColor-accent-muted` 또는 status 계열
- color: accent text
- radius: `9999px`
- font-size: `12px` weight 500
- padding: `0 8px` · height `20px`

### Cards

- bg: `#161B22` / `#FFFFFF`
- border: `1px solid #30363D`
- radius: `6px` 기본 / `12px` 큰 것
- padding: `16–24px`
- shadow: `--shadow-resting-small`

### Navigation

- 로고: octocat SVG 좌측
- 링크: Mona Sans 14px weight 500
- CTA 우측: "Sign in" + "Sign up" (green primary)
- Height: `64px`
- 모바일: 햄버거

### Inputs

- height: `32px`
- padding: `5px 12px`
- bg: `#0D1117` + border `#30363D`
- radius: `6px`
- focus: `outline 2px solid #1F6FEB`

### Hero

- bg: `#0D1117` + radial gradient
- H1: Mona Sans 72px weight 700
- sub: 20px `#8B949E`
- CTA: primary green + secondary ghost

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 기술적 확신 | "Let's build from here" |
| Primary CTA | "Sign up for GitHub" 류 | "Sign up for GitHub" |
| Secondary CTA | Try / Start 동사 | "Start a free trial" |
| Subheading | 가치 명시 1문장 | — |
| Tone | 개발자 화법 — 차분, 실용 | — |

---

## 15. Drop-in CSS

```css
/* GitHub (Primer) — drop-in */
:root {
  --fontStack-sansSerif: "Mona Sans","Hubot Sans",-apple-system,sans-serif;
  --fontStack-monospace: ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;

  /* Dark default */
  --bgColor-default:  #0D1117;
  --bgColor-muted:    #010409;
  --bgColor-subtle:   #161B22;
  --fgColor-default:  #E6EDF3;
  --fgColor-muted:    #8B949E;
  --borderColor-default: #30363D;

  /* Brand */
  --button-primary-bgColor-rest:  #2DA44E;
  --button-primary-bgColor-hover: #29903B;
  --fgColor-accent:               #4493F8;
  --bgColor-accent-emphasis:      #1F6FEB;

  /* Danger */
  --fgColor-danger: #F85149;
  --bgColor-danger-emphasis: #CF222E;

  /* Radius */
  --borderRadius-small:  4px;
  --borderRadius-medium: 6px;
  --borderRadius-large:  12px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — GitHub Primer
module.exports = {
  theme: {
    extend: {
      colors: {
        primer: {
          bg:      '#0D1117',
          muted:   '#010409',
          subtle:  '#161B22',
          border:  '#30363D',
          text:    '#E6EDF3',
          'text-muted': '#8B949E',
          accent:  '#1F6FEB',
          link:    '#4493F8',
          green:   '#2DA44E',
          red:     '#CF222E',
          purple:  '#8250DF',
          yellow:  '#9A6700',
        },
      },
      fontFamily: {
        sans: ['Mona Sans','Hubot Sans','system-ui'],
        mono: ['ui-monospace','SF Mono','Menlo'],
      },
      borderRadius: { sm:'4px', DEFAULT:'6px', lg:'12px', full:'9999px' },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary (green) | `--button-primary-bgColor-rest` | `#2DA44E` |
| Accent (blue) | `--bgColor-accent-emphasis` | `#1F6FEB` |
| Background | `--bgColor-default` | `#0D1117` |
| Text primary | `--fgColor-default` | `#E6EDF3` |
| Text muted | `--fgColor-muted` | `#8B949E` |
| Border | `--borderColor-default` | `#30363D` |
| Link | `--fgColor-accent` | `#4493F8` |
| Danger | `--fgColor-danger` | `#F85149` |

### Example Component Prompts

#### Hero Section

```
GitHub 스타일 히어로 섹션을 만들어줘.
- 배경: #0D1117 + radial-gradient(circle at center, rgba(31,111,235,0.15) 0%, transparent 60%)
- H1: Mona Sans, 72px, weight 700, color #E6EDF3, ls -0.02em
- sub: 20px, color #8B949E
- CTA primary: bg #2DA44E, color #FFFFFF, radius 6px, padding 5px 16px
- CTA secondary: bg transparent, border 1px solid #30363D, color #E6EDF3
```

#### Card Component

```
GitHub (Primer) 스타일 카드를 만들어줘.
- bg #161B22, border 1px solid #30363D, radius 6px
- padding 24px
- shadow 0 1px 0 rgba(0,0,0,0.1)
- hover border-color #8B949E
- 제목 Mona Sans 20px weight 600
- 본문 14px color #8B949E
```

#### Badge (Label)

```
GitHub 스타일 라벨 배지를 만들어줘.
- font Mona Sans 12px weight 500
- padding 0 8px height 20px radius 9999px
- bg #388BFD1A (accent muted), color #4493F8, border none
```

#### Navigation

```
GitHub 스타일 상단 네비를 만들어줘.
- height 64px, position fixed top 0
- bg #0D1117 (dark), border-bottom 1px solid #30363D
- 로고 좌측 octocat SVG
- 링크 Mona Sans 14px weight 500 color #E6EDF3
- CTA 우측: Sign in (ghost) + Sign up (green primary)
```

### Iteration Guide

- **색상** raw hex 직접 사용 금지 — 반드시 `--fgColor-*` / `--bgColor-*` / `--button-*` alias.
- **폰트** Mona Sans weight 400/500/600/700 4단.
- **여백** 4px 배수 (4/8/12/16/24/32/48/64).
- **radius** 4/6/12/9999 중 하나.
- **테마** light/dark × colorblind/tritanopia/high-contrast — token swap만으로 대응.

---

## 18. DO / DON'T

### ✅ DO

- 컴포넌트 CSS는 `--bgColor-*` / `--fgColor-*` / `--button-*` semantic alias로만.
- primary CTA는 `#2DA44E` green, hover `#29903B`, active `#2E9A40`.
- 본문은 Mona Sans, body `14px` (small ui) 또는 `16px` (marketing hero).
- 카드 radius `6px` (기본), `12px` (큰 것).
- border는 `#30363D` (dark) / `#D1D9E0` (light).
- 접근성 테마 분기: `data-theme="dark_colorblind"` 처럼 HTML attribute로 스왑.

### ❌ DON'T

- raw hex `#0D1117` 같은 값을 컴포넌트 CSS에 직접 쓰지 말 것 — 테마 분기 깨짐.
- primary bg에 파랑 `#1F6FEB` 쓰지 말 것 — primary는 green, blue는 accent/link 전용.
- radius `8px` 쓰지 말 것 — Primer scale은 `4/6/12`.
- weight `800`, `900` 쓰지 말 것 — Mona Sans는 최대 `700`.
- 카드 shadow를 강하게 쓰지 말 것 — Primer shadow는 subtle dual-layer.
