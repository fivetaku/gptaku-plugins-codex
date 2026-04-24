---
schema_version: 3.1
slug: raycast
service_name: Raycast
site_url: https://www.raycast.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#FF6363"
primary_font: Inter
font_weight_normal: 400
token_prefix: --color-*, --Base-*

bold_direction: "Playful Gradient"
aesthetic_category: "Playful Gradient"
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Raycast (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Raycast 홈페이지는 near-black #0C0D0F 바탕에 vivid red #FF6363 diagonal stripe 그라디언트가 히어로를 압도하는 bold dark 테마다. 'Your shortcut to everything.' 카피와 함께 45도 대각선 red 스트라이프 패턴이 주목도를 최대치로 끌어올린다. 실제로 CSS에서 #FF6363 hex가 26회 등장하는데, 이는 분석한 다른 모든 사이트의 brand accent 빈도를 압도한다.

컬러는 red 브랜드 + #FFFFFF ink + near-black 3단 surface + HSL color space이 특징이다. 일반 사이트와 달리 hsl(202,100%,67%) 같은 HSL 선언이 광범위하게 쓰이고, hsla(0,0%,100%,0.815)처럼 투명도 조절도 HSL 기반. near-black ramp는 #07080A → #0C0D0F → #111214 → #18191A → #313133 → #494B4D의 6단계 깊이.

타이포그래피는 Inter + Geist Mono가 핵심이다. var(--font-geist-mono)가 19회 / var(--monospace-font)가 14회 / var(--font-inter)가 9회 등장하는 걸 보면 기술 product 사이트답게 monospace가 주연급이다. Geist Mono는 terminal hero card에 쓰이고, JetBrains Mono 참조도 6회 있다.

레이아웃은 Raycast extension hero + command palette 모방 UI + alternating dark sections의 패턴이다. command palette를 시뮬레이션한 카드(border hsl(195,5%,15%), bg #111214)가 중앙을 차지한다. 히어로 diagonal stripe는 transform rotate(-45deg) + 복수 red 그라디언트 레이어로 구현.

인터랙션은 high-complexity — stripe의 subtle animation, command palette hover highlight, 탭 전환, 호버 시 색상 lift. transition은 .15s-.3s ease 범위.

### Key Characteristics

- Red diagonal hero
- Near-black 6-layer
- HSL color space
- Geist Mono display
- Command palette UI
- Bold dark

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Playful Gradient
> **Aesthetic Category**: Playful Gradient
> **Signature Element**: 이 사이트는 **강렬한 red 그라디언트와 near-black의 대비**으로 기억된다.
> **Code Complexity**: high — Raycast 홈페이지의 Inter + Geist Mono, red diagonal + near-black 6-step ramp 디자인 시스템.

---

## 01. Quick Start

> 5분 안에 Raycast처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: var(--font-inter),
    "Inter", -apple-system, sans-serif;
  font-weight: 400;
  font-size: 15px;
}
.mono {
  font-family: var(--font-geist-mono),
    "Geist Mono", "JetBrains Mono",
    ui-monospace;
}

/* 2. 배경 + 텍스트 (dark) */
:root {
  --bg: #0C0D0F;
  --bg-layer-2: #111214;
  --bg-layer-3: #18191A;
  --fg: #FFFFFF;
  --border: hsl(195, 5%, 15%);
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. 브랜드 red + gradient */
:root {
  --brand: #FF6363;
  --brand-deep: #FF2136;
  --brand-dark: #452324;
  --hero-stripe: linear-gradient(
    -45deg,
    transparent 40%,
    #FF6363 40%,
    #FF6363 60%,
    transparent 60%
  );
}

```

**절대 하지 말아야 할 것 하나**: Raycast의 red #FF6363는 diagonal stripe 패턴이 signature다. solid 단색 red 배경으로 쓰지 마라. 반드시 -45deg 대각선 반복 스트라이프 + near-black overlay로 구성해야 Raycast 톤이 나온다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://www.raycast.com</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 368,051 bytes (Next.js SSR) |
| CSS files | 12개 외부, 428KB |
| Token prefix | <code>--color-*</code>, <code>--Base-*</code>, <code>--font-*</code> |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (React) + Radix UI 일부
- **Design system**: 자체 토큰 + HSL 채도 제어
- **CSS architecture**: CSS Modules + CSS Variables with HSL
- **Class naming**: CSS Modules (<code>_hero__xxx</code>)
- **Default theme**: <code>dark</code> (bg <code>#0C0D0F</code>)
- **Font loading**: Inter + Geist Mono + JetBrains Mono (self-host)
- **Canonical anchor**: <code>#FF6363</code> red
- **Unique**: HSL color space 광범위 사용, diagonal stripe hero

---

## 04. Font Stack

- **Body**: <code>Inter</code> (OFL, <code>--font-inter</code>)
- **Display mono**: <code>Geist Mono</code> (OFL)
- **Fallback mono**: <code>JetBrains Mono</code>
- **Fallback body**: <code>-apple-system, system-ui</code>
- **Weights**: 400 / 500 / 600 / 700

---

## 05. Typography Scale

> Body 15px Inter + 디스플레이 mono Geist. Hero H1은 48-64px weight 700.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `caption` | 12px | 400 | 1.4 | 0 |
| `body` | 15px | 400 | 1.5 | 0 |
| `lead` | 17px | 400 | 1.5 | 0 |
| `H3 mono` | 20px | 500 | 1.3 | 0 |
| `H2` | 32px | 600 | 1.2 | -0.02em |
| `Hero H1` | 48-64px | 700 | 1.1 | -0.03em |

---

## 06. Colors

> Red diagonal + near-black 6-layer + HSL accent. 가장 bold한 tech dark 팔레트.

### Brand Red (stripe)

| Token | Hex |
|---|---|
| `brand ★` | `#FF6363` |
| `brand-deep` | `#FF2136` |
| `brand-dark` | `#452324` |
| `stripe-dark` | `#833637` |
| `stripe-light` | `#ECA5A7` |

### Near-Black 6-layer

| Token | Hex |
|---|---|
| `Base-Black` | `#000000` |
| `bg-0` | `#07080A` |
| `bg-100` | `#0C0D0F` |
| `bg-200` | `#111214` |
| `bg-300` | `#18191A` |
| `bg-400` | `#313133` |
| `bg-500` | `#494B4D` |

### Accent HSL

| Token | Hex |
|---|---|
| `blue` | `#0294FE` |
| `blue-dark` | `#56C2FF` |
| `green` | `#59D499` |
| `purple` | `#D8ACFF` |
| `blue-electric` | `#052DFF` |

### Neutral White

| Token | Hex |
|---|---|
| `Base-White` | `#FFFFFF` |
| `muted-white` | `#D9D9D9` |
| `button-bg` | `rgba(255,255,255,0.815)` |
| `border` | `hsl(195,5%,15%)` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--Base-Black` | #000000 — absolute black |
| `--Base-White` | #FFFFFF — absolute white |
| `--color-bg-100` | rgb(16,17,17) → #101111 |
| `--color-bg-200` | rgb(24,25,26) → #18191A |
| `--color-border` | hsl(195,5%,15%) — subtle dark border |
| `--color-button-bg` | hsla(0,0%,100%,0.815) — CTA white transparent |
| `--color-blue` | hsl(202,100%,67%) → #56C2FF |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FF6363` | 26 | brand red stripe |
| 2 | `#FFFFFF` | 24 | ink on dark |
| 3 | `#D9D9D9` | 22 | muted white |
| 4 | `#111214` | 13 | bg layer 2 |
| 5 | `#0C0D0F` | 13 | bg primary |
| 6 | `#452324` | 10 | brand dark |
| 7 | `#59D499` | 6 | green accent |
| 8 | `#000000` | 5 | absolute black |

---

## 07. Spacing

> 8px baseline + 1200px container + alternating dark sections.

container: 1200px · section py 96-128px · card padding 24-32px

| Token | Value | Use |
|---|---|---|
| `space-1` | 4px | icon gap |
| `space-2` | 8px | compact |
| `space-3` | 12px | button inner |
| `space-4` | 16px | card inner |
| `space-6` | 24px | card |
| `space-8` | 32px | card large |
| `section-y` | 96px | section vertical |
| `container` | 1200px | page width |

---

## 08. Radius

> 8-12px card + 8px button + 4px input. pill 9999px.

| Token | Value | Context |
|---|---|---|
| `radius-sm` | 4px | input / chip |
| `radius-md` | 8px | button |
| `radius-lg` | 12px | card |
| `radius-xl` | 16px | hero block |
| `radius-full` | 9999px | download button |

---

## 09. Shadows

> 다크 배경이라 shadow 대신 border + glow 사용.

| Level | Usage | Value |
|---|---|---|
| `card inner` | 기본 | `inset 0 0 0 1px hsl(195,5%,15%)` |
| `cta glow` | primary hover | `0 0 20px rgba(255,99,99,0.4)` |
| `dropdown` | menu | `0 10px 24px rgba(0,0,0,0.6)` |

---

## 10. Motion

> <code>.15s-.3s ease</code>. hover highlight + command palette 인터랙션.

| Pattern | Value | Use |
|---|---|---|
| `transition-fast` | `150ms ease-out` | hover bg/color |
| `transition-base` | `200ms ease-out` | 기본 |
| `command palette reveal` | `300ms ease-out` | 스포트라이트 풀업 |
| `stripe drift` | `scroll-linked` | 배경 대각선 이동 |

---

## 11. Layout Patterns

> 1200px + hero stripe + command palette 카드 + alternating section.

### Grid System

- Container max-width: 1200px
- Grid type: CSS Grid + Flex
- Columns: 12 / 6 / 3
- Gutter: 16-24px

### Hero

- Layout: 1-column centered + red diagonal background
- Background: near-black + -45deg red stripes
- H1: 48-64px weight 700 color #FFFFFF
- Max-width: 720px
- Pattern: ~90vh + sub + download CTA pill

### Section Rhythm

- Padding: 96-128px vertical
- Max-width: 1200px
- 섹션 간 bg #0C0D0F ↔ #111214 alternating

### Card Patterns

- Background: #111214
- Border: 1px solid hsl(195,5%,15%)
- Radius: 12px
- Padding: 24px
- Shadow: inner highlight + outer glow hover

### Navigation

- Type: horizontal
- Position: sticky + blur
- Height: ~64px
- Background: rgba(12,13,15,0.8) + backdrop-blur

### Content Width

- Prose: 680px
- Container: 1200px
- Sidebar: N/A (marketing)

---

## 12. Responsive Behavior

> Mobile-first. 640/768/1024/1280 breakpoints.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 640px` | stack |
| Tablet | `≥ 768px` | 2-col |
| Desktop | `≥ 1024px` | full |
| Large | `≥ 1280px` | XL hero |

### Collapsing Strategy

- **Touch targets**: button 40-48px
- **Nav collapse**: 1024px 이하 햄버거
- **Grid columns**: 3 → 2 → 1
- **Hero stripe**: mobile 단순화 (0.5 rotate)
- **Command palette**: mobile 축소 버전
- **First-class**: mobile-first

---

## 13. Components

> Red stripe hero + Download CTA pill + command palette card + feature grid.

### .btn-primary (white transparent)

_Primary CTA — transparent white pill on dark_

```html
<button style="background:rgba(255,255,255,0.815);color:#18191A;border:0;border-radius:9999px;padding:10px 20px;font-size:14px;font-weight:600;cursor:pointer;">Download</button>
```

Spec:

- background: hsla(0,0%,100%,0.815)
- color: #18191A
- radius: 9999px pill
- padding: 10px 20px
- weight: 600

### .command-palette

_Raycast UI 모방 카드_

```html
<div style="background:#111214;border:1px solid hsl(195,5%,15%);border-radius:12px;padding:16px;max-width:320px;font-family:ui-monospace;font-size:13px;color:#D9D9D9;"><div style="opacity:0.5;margin-bottom:8px;">🔍 Search Raycast...</div><div style="padding:8px;background:rgba(255,99,99,0.1);border-radius:6px;color:#FF6363;">→ Open AI Chat</div></div>
```

Spec:

- bg: #111214
- border: 1px solid hsl(195,5%,15%)
- radius: 12px
- highlight: rgba(255,99,99,0.1)

### .stripe-hero

_red diagonal stripe background_

```html
<div style="background:#0C0D0F;padding:40px 20px;border-radius:12px;position:relative;overflow:hidden;color:#FFF;text-align:center;"><div style="position:absolute;inset:0;background:repeating-linear-gradient(-45deg,transparent 0 20px,#FF6363 20px 40px,transparent 40px 60px);opacity:0.7;"></div><div style="position:relative;font-size:20px;font-weight:700;">Your shortcut to everything.</div></div>
```

Spec:

- bg: #0C0D0F
- stripe: repeating-linear-gradient(-45deg, transparent 0, #FF6363 20-40px)
- opacity: 0.7

---

## 15. Drop-in CSS

```css
/* Raycast — copy into your root */
:root {
  --font-inter: "Inter", -apple-system, sans-serif;
  --font-geist-mono: "Geist Mono", "JetBrains Mono", ui-monospace;

  /* Brand */
  --brand:      #FF6363;
  --brand-deep: #FF2136;
  --brand-dark: #452324;

  /* Near-black ramp */
  --bg-0:   #07080A;
  --bg-100: #0C0D0F;
  --bg-200: #111214;
  --bg-300: #18191A;
  --bg-400: #313133;

  /* Accent HSL */
  --color-blue:  hsl(202, 100%, 67%);
  --color-green: #59D499;
  --color-border: hsl(195, 5%, 15%);

  /* Button */
  --color-button-bg:       hsla(0, 0%, 100%, 0.815);
  --color-button-bg-hover: hsl(0, 0%, 100%);
  --color-button-fg:       rgb(24, 25, 26);

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-pill: 9999px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Raycast-like
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: '#FF6363', deep: '#FF2136', dark: '#452324' },
        bg: { 0: '#07080A', 100: '#0C0D0F', 200: '#111214', 300: '#18191A', 400: '#313133' },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif'],
        mono: ['"Geist Mono"', '"JetBrains Mono"', 'ui-monospace'],
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand red | `--brand` | `#FF6363` |
| Background | `--bg-100` | `#0C0D0F` |
| Surface | `--bg-200` | `#111214` |
| Text primary | `--Base-White` | `#FFFFFF` |
| Text muted | `—` | `#D9D9D9` |
| Border | `--color-border` | `hsl(195,5%,15%)` |
| Button bg (CTA) | `--color-button-bg` | `rgba(255,255,255,0.815)` |

### Example Component Prompts

#### Stripe hero

```
Raycast 스타일 히어로:
- bg #0C0D0F
- overlay: repeating-linear-gradient(-45deg, transparent 0 20px, #FF6363 20px 40px, transparent 40px 60px) opacity 0.7
- H1: Inter 56px weight 700 color #FFFFFF
- Sub: 17px color #D9D9D9
- CTA pill: bg rgba(255,255,255,0.815) color #18191A radius 9999px
```

#### Command palette

```
Raycast command palette 카드:
- bg #111214
- border 1px solid hsl(195,5%,15%)
- radius 12px padding 16px
- font Geist Mono 13px color #D9D9D9
- highlight row: bg rgba(255,99,99,0.1) color #FF6363
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 #0C0D0F bg-100 + alternating section #111214 bg-200.
- Red #FF6363는 -45deg diagonal stripe로만 큰 면적에 등장.
- Primary CTA는 흰색 transparent pill rgba(255,255,255,0.815) + radius 9999px.
- border는 반드시 hsl(195,5%,15%) HSL — 일반 hex grey 금지.
- monospace 텍스트는 Geist Mono → JetBrains Mono fallback.

### ❌ DON'T

- Red #FF6363를 solid 배경으로 넓은 면적에 쓰지 말 것 — 반드시 stripe 패턴.
- CTA primary를 solid #FF6363로 두지 말 것 — white transparent pill이 표준.
- 본문 텍스트를 순수 #FFFFFF로 body에 고정하지 말 것 — #D9D9D9 muted 변주.
- border를 solid #333, #444로 두지 말 것 — hsl(195,5%,15%).
- diagonal stripe 각도를 변경하지 말 것 — -45deg 고정.
- body weight를 300로 두지 말 것 — 400.
