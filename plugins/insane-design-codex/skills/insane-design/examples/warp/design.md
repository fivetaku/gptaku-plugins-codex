---
schema_version: 3.1
slug: warp
service_name: Warp
site_url: https://www.warp.dev
fetched_at: 2026-04-20
default_theme: light
brand_color: "#FAF9F6"
primary_font: Inter
font_weight_normal: 400
token_prefix: "Framer (--framer-*) + custom Matter/Aguzzo display fonts"

bold_direction: "Warm Brutalist Terminal"
aesthetic_category: "Developer Brutalism"
signature_element: warm_cream_terminal
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Warp (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Warp(`www.warp.dev`)는 AI-powered terminal이라는 포지셔닝을 **Warm Brutalist Terminal** 비주얼로 풀어냈다. 가장 특이한 점은 대부분의 dev-tool이 쓰는 검정-아닌 **`#FAF9F6` cream/warm-white** 를 주 bg로 선택했다는 것 — 이는 Kraft paper/Bauhaus 계열에서 영감을 받은 따뜻한 off-white로, "터미널은 검정이어야 한다"는 클리셰를 깨는 전략적 선택이다. 제품 자체 (Warp terminal)는 다크지만, **마케팅 사이트는 cream-first**로 가서 대비를 만든다.

컬러 시스템은 의도적으로 빈약하다 — frequency candidates를 봐도 검정 (`#000` 74회), cream (`#FAF9F6` 33회), 흰색 (`#FFFFFF` 10회)이 압도적이고, 나머지는 거의 alpha-overlay 변형. 중간 gray 계단이 7-8단 (`#232224`, `#2B2B2B`, `#353534`, `#454545`, `#666469`, `#868584`, `#AFAEAC`, `#E3E2E0`) 으로 촘촘하게 제공되어 타이포그래피 hierarchy를 담당. 즉 **컬러로 말하지 않고 warm neutrals + typography로** 말한다.

타이포그래피는 Warp의 진짜 시그니처다. **Inter**(57회)를 body로 쓰면서, display에 **Matter Regular/Medium** (sans serif 브랜드 커스텀), **Aguzzo-TRIAL Medium** (experimental display), **Abel** (condensed)까지 동시에 로드한다. mono는 **Geist Mono** + **Fragment Mono** + **DM Mono** — 3종의 monospace를 맥락별로 swap. weight는 400/500/600/700/900에 집중 (300 없음). `900` heavy는 display 섹션에만.

레이아웃은 Framer 기반 (`--framer-*` custom properties)으로 구성. Framer의 rich text node 시스템이 그대로 드러나 있어 `[data-framer-component-type=DeprecatedRichText]` 같은 selector가 대량 등장. Framer 사이트답게 애니메이션 + scroll-driven interaction이 풍부하게 들어간다.

인터랙션은 Framer 생태계 표준 — hover에서 color transform + smooth opacity/translate. 마케팅 사이트지만 terminal app을 판매하는 만큼 interaction의 "performance feel"을 강조.

### Key Characteristics

- cream/warm-white `#FAF9F6` bg (not true white, not dark)
- true black `#000` text + Warp 다크 `#121212`
- warm gray ramp 8단 (`#E3E2E0` → `#232224`)
- Inter (body) + Matter / Aguzzo / Abel 다중 display
- Geist Mono + Fragment Mono + DM Mono 3종 mono
- weight 400/500/600/700/900 (300 없음)
- Framer `--framer-*` CSS vars + rich text nodes
- 컬러 팔레트 의도적 빈약 (warm neutrals + typography 강조)
- scroll-driven animation (Framer native)

### BOLD Direction Summary

> **BOLD Direction**: Warm Brutalist Terminal — cream bg + typography-first 개발자 도구 미학
> **Aesthetic Category**: Developer Brutalism
> **Signature Element**: warm_cream_terminal — #FAF9F6 bg + Inter/Matter display + mono code
> **Code Complexity**: medium — Framer + 다중 display fonts + rich text nodes

---

## 01. Quick Start

```css
:root {
  --cream: #FAF9F6;
  --cream-alt: #FAF9F5;
  --fg: #000000;
  --fg-alt: #121212;
  --fg-muted: #666469;
  --border: #E3E2E0;
  --dark-bg: #1A1A1A;
  --dark-alt: #2B2B2B;
}
body {
  background: var(--cream);
  color: var(--fg);
}
```

```css
body {
  font-family: "Inter", "Inter Placeholder", sans-serif;
  font-weight: 400;
  font-size: 16px;
}
.display, h1, h2 {
  font-family: "Matter Regular", "Matter Regular Placeholder", sans-serif;
  font-weight: 500;
}
code, pre {
  font-family: "Geist Mono", "Fragment Mono", ui-monospace, monospace;
}
```

```css
.btn-warp {
  background: #000000;
  color: #FAF9F6;
  padding: 12px 24px;
  border-radius: 8px;
  font-family: "Inter", sans-serif;
  font-weight: 500;
  transition: background .2s ease, transform .2s ease;
}
.btn-warp:hover { background: #1A1A1A; transform: translateY(-1px); }
```

**절대 하지 말 것 하나**: bg를 `#FFFFFF` pure white로 두지 마라 — Warp의 정체성은 **`#FAF9F6` warm cream** 이다. pure white로 바꾸면 Stripe/Apple 느낌이 되고 Warp 브랜드가 증발한다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.warp.dev` |
| Fetched | 2026-04-20 |
| Framework | Framer (native site builder) |
| Font vars | `--framer-font-family`, `--framer-link-*-font-family` |
| Theme | light default (product은 dark) |

---

## 03. Tech Stack

- **Framework**: Framer (native)
- **CSS**: Framer custom properties (`--framer-*`) + custom fonts
- **Typography**: Inter + Matter (brand sans) + Geist Mono + Fragment Mono + DM Mono + Aguzzo + Abel
- **Theme**: light default marketing / dark product
- **Interaction**: Framer scroll-driven animations
- **Rich text**: `[data-framer-component-type=DeprecatedRichText]` + `a.framer-text`

---

## 04. Font Stack

- **Primary body**: `Inter` (57회 사용, var `--framer-font-family`)
- **Display sans**: `Matter Regular` / `Matter Medium` / `Matter SQ Medium` / `Matter SQ Regular` (Matter Regular 3회, Matter SQ 2회)
- **Experimental display**: `Aguzzo-TRIAL Medium` (소수)
- **Condensed**: `Abel` (rare)
- **Mono**: `Geist Mono` (6회) / `Fragment Mono` (3회) / `DM Mono` (2회) / `Matter Mono Regular` (2회)
- **Framer Placeholder**: 모든 브랜드 폰트에 `Placeholder` 변형 로드 (FOIT 방지)
- **Weights**: 400 · 500 · 600 · 700 · 900 (300 없음)

---

## 05. Typography Scale

| Token | Size | Weight | lh | Use |
|---|---|---|---|---|
| caption | 12px | 400 | 1.5 | meta |
| small | 14px | 400 | 1.5 | small body |
| body | 16px | 400 | 1.6 | default |
| lead | 18px | 500 | 1.5 | lead |
| h3 | 22-24px | 600 | 1.3 | subsection |
| h2 | 32-40px | 500-600 | 1.2 | section |
| h1 | 48-64px | 500-700 | 1.1 | heading |
| display | 72-96px | 500-900 | 1.05 | hero |
| mega | 120px+ | 900 | 1.0 | oversized hero |

---

## 06. Colors

### Warm Neutrals (signature)

| Name | Hex | Use |
|---|---|---|
| cream | `#FAF9F6` | **primary bg** (warm off-white) |
| cream-alt | `#FAF9F5` | subtle variant |
| white | `#FFFFFF` | used sparingly |
| warm-white-transparent | `#FFFFFFE6` | overlay |

### Dark Stack

| Name | Hex | Use |
|---|---|---|
| black | `#000000` | text primary |
| near-black | `#121212` | text alt / raised dark bg |
| dark-bg | `#1A1A1A` | card bg dark |
| dark-alt | `#2B2B2B` | elevated dark |
| dark-alt-2 | `#232224` | raised |
| border-dark | `#353534` | dark border |
| border-mid | `#454545` | mid border |
| fg-muted-dark | `#666469` | text muted on dark |
| fg-muted | `#868584` | text muted neutral |
| surface-light | `#AFAEAC` | light surface on dark |
| border-light | `#E3E2E0` | light border |

### Overlay / Alpha

| Hex | Use |
|---|---|
| `#FFFFFFE6` | near-white overlay 90% |
| `#FFFFFF99` | white 60% |
| `#FFFFFF29` | white 16% |
| `#FFFFFF0D` | white 5% |
| `#3636321A` | warm black alpha 10% |
| `#87878700` | transparent marker |

### Decorative

| Name | Hex | Use |
|---|---|---|
| svg-pattern-bg | `#FAF9F6` | background illustration |
| teal-svg | `#38555832` (α) | SVG pattern accent |

---

## 07. Spacing

Framer spacing + custom. `0.75rem` / `1rem` / `1.5rem` 주로 사용.

| Token | Value | Use |
|---|---|---|
| xs | 4px | inline |
| sm | 8px | icon gap |
| md | 16px | default |
| lg | 24px | card padding |
| xl | 48px | hero padding |
| 2xl | 96px | section padding |

---

## 08. Radius

| Name | Value | Use |
|---|---|---|
| radius-sm | 4px | input |
| radius-md | 8px | button |
| radius-lg | 12px | card |
| radius-xl | 16px | hero card |
| radius-full | 9999px | pill badge |

---

## 09. Shadows

Warp는 shadow를 거의 쓰지 않는다 — cream bg 위에서 subtle border가 더 적합.

| Name | Value | Use |
|---|---|---|
| border | `1px solid #E3E2E0` | **primary elevation** (border-first) |
| shadow-sm | `0 1px 3px rgba(0,0,0,.04)` | subtle raise |
| shadow-md | `0 8px 24px rgba(0,0,0,.08)` | card hover |

---

## 10. Motion

Framer native animation 기반. scroll-driven + hover transform.

| Pattern | Value | Use |
|---|---|---|
| hover transition | `.2s ease` | color + transform |
| scroll reveal | parallax / fade-in | Framer default |
| button press | `translateY(-1px)` | interactive feedback |

---

## 11. Layout Patterns

### Hero
- bg `#FAF9F6` cream
- oversized headline (Matter 72-96px)
- subcopy Inter muted
- single dark CTA on cream

### Section Rhythm
- padding 96-128px
- max-width 1200-1440px
- alternating cream / `#FFFFFF`

### Card
- bg `#FAF9F6` 또는 `#FFFFFF`
- border 1px solid `#E3E2E0`
- radius 12px
- hover: translateY(-2px) + shadow

### Terminal Screenshot Card (product showcase)
- bg `#1A1A1A` / `#000`
- rounded 16px
- subtle border

### Navigation
- height 72px
- bg cream 또는 transparent
- Inter 500
- single dark CTA "Download"

---

## 12. Responsive

sm 640 / md 768 / lg 1024 / xl 1280.
Framer breakpoint 내부 표기는 `desktop / tablet / phone`.

---

## 13. Components

### Dark CTA on Cream (Primary)
```css
.btn-warp {
  background: #000000;
  color: #FAF9F6;
  padding: 12px 24px;
  border-radius: 8px;
  font-family: "Inter", sans-serif;
  font-weight: 500;
  transition: background .2s ease, transform .2s ease;
}
.btn-warp:hover {
  background: #1A1A1A;
  transform: translateY(-1px);
}
```

### Ghost CTA
```css
.btn-warp-ghost {
  background: transparent;
  color: #000000;
  padding: 12px 24px;
  border-radius: 8px;
  border: 1px solid #E3E2E0;
  font-weight: 500;
}
.btn-warp-ghost:hover { background: #F5F4F0; }
```

### Warm Card
```css
.warp-card {
  background: #FAF9F6;
  border: 1px solid #E3E2E0;
  border-radius: 12px;
  padding: 24px;
  transition: transform .2s ease, box-shadow .2s ease;
}
.warp-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,.08);
}
```

### Terminal Screenshot Frame
```css
.terminal-frame {
  background: #1A1A1A;
  border-radius: 16px;
  padding: 8px;
  border: 1px solid #2B2B2B;
  overflow: hidden;
}
.terminal-frame pre {
  font-family: "Geist Mono", monospace;
  color: #FAF9F6;
  padding: 24px;
}
```

### Oversized Display Headline
```css
.display-xl {
  font-family: "Matter Regular", sans-serif;
  font-size: clamp(48px, 8vw, 120px);
  font-weight: 500;
  line-height: 1.0;
  letter-spacing: -0.03em;
  color: #000000;
}
```

---

## 14. Content / Copy Voice

| Label | Rule |
|---|---|
| Tone | confident, technical, AI-forward |
| Headline | 3-8 단어 bold declarative |
| CTA verb | "Download" / "Get Warp" / "Request Access" |
| Mono usage | code snippets / command examples |

---

## 15. Drop-in CSS

```css
:root {
  --cream: #FAF9F6;
  --fg: #000000;
  --fg-muted: #666469;
  --border: #E3E2E0;
  --dark-bg: #1A1A1A;
  --font-body: "Inter", sans-serif;
  --font-display: "Matter Regular", "Matter Regular Placeholder", sans-serif;
  --font-mono: "Geist Mono", "Fragment Mono", monospace;
}
body {
  background: var(--cream);
  color: var(--fg);
  font-family: var(--font-body);
  font-size: 16px;
  font-weight: 400;
}
h1, h2 { font-family: var(--font-display); font-weight: 500; }
code { font-family: var(--font-mono); }
.btn-warp {
  background: #000; color: var(--cream);
  padding: 12px 24px; border-radius: 8px;
  font-weight: 500; transition: all .2s ease;
}
.btn-warp:hover { background: #1A1A1A; transform: translateY(-1px); }
```

---

## 16. Tailwind Config

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        cream: { DEFAULT:'#FAF9F6', alt:'#FAF9F5' },
        warp: { bg:'#FAF9F6', fg:'#000000', muted:'#666469', border:'#E3E2E0', dark:'#1A1A1A' },
      },
      fontFamily: {
        sans: ['Inter','"Inter Placeholder"','sans-serif'],
        display: ['"Matter Regular"','"Matter Regular Placeholder"','sans-serif'],
        mono: ['"Geist Mono"','"Fragment Mono"','monospace'],
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide

| Role | Token | Hex |
|---|---|---|
| Bg (cream) | `--cream` | `#FAF9F6` |
| Text | `--fg` | `#000000` |
| Text muted | `--fg-muted` | `#666469` |
| Border | `--border` | `#E3E2E0` |
| Dark bg (product) | `--dark-bg` | `#1A1A1A` |

**Prompts**:
- **Hero**: "Warp style hero: bg #FAF9F6 warm cream, oversized headline Matter Regular 96px weight 500 color #000. Subcopy Inter 18px #666469. Dark CTA bg #000 color #FAF9F6 padding 12px 24px radius 8. Optional terminal screenshot card with dark bg #1A1A1A below."
- **CTA**: "Warp dark CTA: bg #000 color #FAF9F6 (cream!), padding 12px 24px, radius 8, Inter 500. Hover: bg #1A1A1A + translateY(-1px)."
- **Warm Card**: "Warp card: bg #FAF9F6, border 1px solid #E3E2E0, radius 12, padding 24. Hover: translateY(-2px) + subtle shadow."
- **Terminal Frame**: "Product terminal frame: bg #1A1A1A, radius 16, padding 8, border 1px #2B2B2B. Inside Geist Mono terminal content."

---

## 18. DO / DON'T

### DO
- ✅ bg는 <code>#FAF9F6</code> cream (pure white 아님)
- ✅ 텍스트는 <code>#000000</code> true black으로 contrast
- ✅ display에 Matter Regular weight 500 · 72-120px
- ✅ 3종 mono 패밀리 (Geist/Fragment/DM) 맥락별 사용
- ✅ border-first elevation (shadow는 거의 없음)
- ✅ cream+black 2-tone으로 충분

### DON'T
- bg를 <code>#FFFFFF</code> 또는 <code>#F5F5F5</code>로 두지 말 것 — cream <code>#FAF9F6</code> 고수
- body에 weight 300 light 쓰지 말 것 — 400부터
- mono를 한 종류만 쓰지 말 것 — Warp는 3종 병행
- shadow로 elevation 표현하지 말 것 — border 사용
- Supabase green 같은 accent color 추가하지 말 것 — warm neutrals only
- hero headline을 serif 폰트로 쓰지 말 것 — Matter/Inter sans 고수
