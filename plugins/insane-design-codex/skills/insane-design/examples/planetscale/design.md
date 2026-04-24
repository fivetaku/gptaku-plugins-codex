---
schema_version: 3.1
slug: planetscale
service_name: PlanetScale
site_url: https://planetscale.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#0B6EC5"
primary_font: Inter
font_weight_normal: 400
token_prefix: --gray-*, --blue-*

bold_direction: "Refined SaaS"
aesthetic_category: "Refined SaaS"
signature_element: minimal_extreme
code_complexity: low

medium: web
medium_confidence: high
---

# DESIGN.md — PlanetScale (Codex Edition)

---

## 00. Visual Theme & Atmosphere

PlanetScale 홈페이지는 데이터베이스 인프라 브랜드답게 조용하고 정밀하다. 배경은 순백 #FFFFFF 대신 아주 약간의 웜톤이 섞인 neutral surface로 시작되고, 그 위에 #0B6EC5 블루 한 가지만이 CTA · 링크 · 하이라이트 용도로 제한적으로 등장한다. 장식이 거의 없고 로고 월(Block, Etsy, Intercom, Cursor 등)이 첫 섹션을 차지한다.

컬러 전략은 grayscale 10단 + 단일 블루 악센트의 지극히 보수적인 구조다. Tailwind 스타일의 --gray-50 ~ --gray-900 ramp (#FAFAFA → #111111) 이 전체 UI의 backbone을 이루고, --blue-700 #144EB6이 primary action, --blue-300 #73C7F9이 accent로 쓰인다. Status용으로 --green, --orange, --red ramp가 존재하지만 마케팅 홈에서는 거의 노출되지 않는다.

타이포그래피는 Inter + ui-sans-serif system stack을 축으로 한다. 본문 기본은 16px / weight 400으로 엔터프라이즈 트러스트 톤이며, 디스플레이 제목은 weight 600-700까지 올라간다. 코드 폰트는 ui-monospace / SF Mono / Menlo fallback. Tailwind CSS가 빌드의 중심축이라 utility 클래스가 지배적이다.

레이아웃은 마케팅 사이트 표준인 1200-1280px max-width 중앙 정렬이다. 섹션 리듬은 64-96px vertical padding으로 느슨하고, 로고 월과 feature 카드가 주요 패턴이다. 카드는 얇은 1px border + subtle shadow 조합, radius는 8-12px 범위에 머문다.

인터랙션은 Tailwind 기본 .15s ease-in-out 수준으로 최소한만 움직인다. hover 시 색상 변화 위주이고, 드라마틱한 모션은 없다. 전반적으로 '데이터베이스는 안정이 제1가치'라는 메시지를 시각으로 번역한 느낌.

### Key Characteristics

- Light theme
- Blue-only accent
- Tailwind utility
- Gray ramp 10단
- Logo wall hero
- Enterprise calm

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Refined SaaS
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **하얀 배경 위 절제된 블루 포인트**으로 기억된다.
> **Code Complexity**: low — PlanetScale 홈페이지 CSS 토큰 기반 디자인 시스템 리포트. Tailwind 빌드 산출물에서 실제 사용 중인 색·폰트·여백만 추출.

---

## 01. Quick Start

> 5분 안에 PlanetScale처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Inter + system stack */
body {
  font-family: "Inter", ui-sans-serif,
    system-ui, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 (light default) */
:root {
  --bg: #FFFFFF;
  --fg: #111111;
  --surface: #FAFAFA;
  --border: #E1E1E1;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 블루 */
:root {
  --brand: #0B6EC5;
  --brand-strong: #144EB6;
  --accent: #73C7F9;
}

```

**절대 하지 말아야 할 것 하나**: 파란색을 섹션 배경이나 큰 면적에 쓰지 마라. PlanetScale의 블루는 CTA 버튼과 링크에만 등장하는 포인트 컬러다. 배경으로 쓰면 즉시 Stripe 아류처럼 보인다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://planetscale.com</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 89,808 bytes (Next.js SSR) |
| CSS files | 1개 외부 (81KB minified) |
| Token prefix | <code>--gray-*</code>, <code>--blue-*</code> (Tailwind-style) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (SSR + React)
- **Design system**: Tailwind CSS + 자체 토큰 (<code>--gray-*</code>, <code>--blue-*</code>)
- **CSS architecture**: utility-first, semantic Tailwind 변수
- **Class naming**: Tailwind utilities (<code>bg-white text-gray-900</code>)
- **Default theme**: <code>light</code> (bg <code>#FFFFFF</code>)
- **Font loading**: Inter web font + <code>ui-sans-serif system-ui</code> fallback
- **Canonical anchor**: <code>#0B6EC5</code> / <code>--blue-700</code>
- **Color system**: 10-step gray + 10-step blue/green/orange/red + status

---

## 04. Font Stack

- **Body/Display**: <code>Inter</code> (OFL)
- **Fallback**: <code>ui-sans-serif, system-ui, sans-serif</code>
- **Code**: <code>ui-monospace, SF Mono, Menlo, Consolas</code>
- **Weights**: 400 / 500 / 600 / 700

---

## 05. Typography Scale

> 16px 본문 기준 — 엔터프라이즈 표준. Tailwind 기본 스케일 (text-xs ~ text-6xl) 그대로.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `text-xs` | 12px | 400 | 1.5 | 0 |
| `text-sm` | 14px | 400 | 1.5 | 0 |
| `text-base (body)` | 16px | 400 | 1.5 | 0 |
| `text-lg` | 18px | 400 | 1.5 | 0 |
| `text-2xl` | 24px | 600 | 1.3 | -0.01em |
| `text-4xl` | 36px | 600 | 1.2 | -0.01em |
| `text-6xl (hero H1)` | 60px | 700 | 1.1 | -0.02em |

---

## 06. Colors

> Gray 10단 + Blue 악센트 + status ramp. 가장 단순한 SaaS 팔레트.

### Gray (backbone)

| Token | Hex |
|---|---|
| `gray-50` | `#FAFAFA` |
| `gray-100` | `#EBEBEB` |
| `gray-200` | `#E1E1E1` |
| `gray-300` | `#C1C1C1` |
| `gray-400` | `#A1A1A1` |
| `gray-500` | `#818181` |
| `gray-600` | `#616161` |
| `gray-700` | `#414141` |
| `gray-800` | `#2B2B2B` |
| `gray-900` | `#111111` |

### Blue (brand accent)

| Token | Hex |
|---|---|
| `blue-50` | `#F3FBFF` |
| `blue-100` | `#DDF2FF` |
| `blue-300` | `#73C7F9` |
| `blue-700 ★` | `#144EB6` |
| `blue-950` | `#04122E` |

### Status (rarely surfaced)

| Token | Hex |
|---|---|
| `green-50` | `#EFFFF3` |
| `green-300` | `#75DB8C` |
| `orange-100` | `#FFE8D8` |
| `red (CTA alert)` | `#FF455D` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--bg-primary` | #FFFFFF — page background |
| `--bg-surface` | #FAFAFA — subtle surface (gray-50) |
| `--text-primary` | #111111 — body text (gray-900) |
| `--text-muted` | #737373 — captions (gray-550) |
| `--brand-primary` | #0B6EC5 — primary CTA bg |
| `--border-default` | #E1E1E1 — card/input border (gray-200) |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#0B6EC5` | 7 | brand primary |
| 2 | `#818181` | 7 | gray-500 muted text |
| 3 | `#1E9DE7` | 4 | accent blue lighter |
| 4 | `#A1A1A1` | 3 | gray-400 border |
| 5 | `#336791` | 2 | postgres brand nod |
| 6 | `#EBEBEB` | 1 | gray-100 surface |

---

## 07. Spacing

> Tailwind 기본 4px baseline. p-2, p-4, p-6, p-8, p-12, p-16, p-24 표준.

max-width: 1280px (.container) · py-16 / py-24 섹션 리듬 · gap-4 / gap-6 / gap-8 카드 간격

| Token | Value | Use |
|---|---|---|
| `p-1` | 4px | tight chip padding |
| `p-2` | 8px | small icon button |
| `p-4` | 16px | card inner |
| `p-6` | 24px | card generous |
| `p-8` | 32px | section inner |
| `py-16` | 64px | section vertical |
| `py-24` | 96px | hero vertical |
| `max-w-7xl` | 1280px | page container |

---

## 08. Radius

> Tailwind 기본 radius — 4 / 6 / 8 / 12 / 9999. 카드 8-12px, 버튼 6-8px, pill 9999px.

| Token | Value | Context |
|---|---|---|
| `rounded-sm` | 4px | chip |
| `rounded` | 6px | button default |
| `rounded-md` | 8px | input |
| `rounded-lg` | 12px | card |
| `rounded-full` | 9999px | avatar / pill |

---

## 09. Shadows

> 카드에 1px 테두리 + 얕은 0 1px 3px shadow. 드라마틱한 elevation 없음.

| Level | Usage | Value |
|---|---|---|
| `shadow-sm` | 소형 카드 | `0 1px 2px rgba(0,0,0,0.05)` |
| `shadow` | 기본 카드 | `0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)` |
| `shadow-lg` | dropdown | `0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)` |

---

## 10. Motion

> Tailwind 기본 <code>.15s ease-in-out</code>만 쓴다. 거의 움직이지 않음.

| Pattern | Value | Use |
|---|---|---|
| `transition-colors` | `150ms ease-in-out` | bg/color 변화 |
| `transition-opacity` | `150ms ease-in-out` | 드롭다운 fade |
| `duration-200` | `200ms` | hover lift (사용 빈도 낮음) |

---

## 11. Layout Patterns

> 1280px max-width + 16-24px gutter + 64-96px vertical padding. 매우 보수적.

### Grid System

- Container max-width: 1280px (max-w-7xl)
- Grid type: CSS Grid + Flex (Tailwind utilities)
- Columns: 12 subdivisions (Tailwind col-span-*)
- Gutter: 16-24px (gap-4/gap-6)

### Hero

- Layout: 1-column centered text + 로고 월
- Background: solid white / subtle gradient
- H1: ~60px / weight 700 / tracking -0.02em
- Max-width: ~800px prose
- Pattern: ~60vh + 로고 wall 하단 + dual CTA

### Section Rhythm

- Padding: 64px / 96px vertical
- Max-width: 1280px
- 섹션 간 구분선 없음, 배경만 변함

### Card Patterns

- Background: #FFFFFF / #FAFAFA
- Border: 1px solid #E1E1E1
- Radius: 8-12px
- Padding: 24-32px
- Shadow: shadow-sm 기본

### Navigation

- Type: horizontal + 드롭다운 (Platform, Resources)
- Position: sticky top
- Height: ~64px
- Background: white
- Border: 1px solid #EBEBEB 하단

### Content Width

- Prose: ~720-800px
- Container: 1280px
- Sidebar: docs에서만 사용

---

## 12. Responsive Behavior

> Tailwind 기본 breakpoints 그대로: sm 640 / md 768 / lg 1024 / xl 1280 / 2xl 1536. Mobile-first.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| sm | `≥ 640px` | mobile landscape |
| md | `≥ 768px` | tablet |
| lg | `≥ 1024px` | desktop nav 복원 |
| xl | `≥ 1280px` | full container |
| 2xl | `≥ 1536px` | wide monitors |

### Collapsing Strategy

- **Touch targets**: button height 40-48px (h-10/h-12)
- **Navigation collapse**: lg 이하에서 햄버거
- **Grid columns**: 3-col → 2-col → 1-col
- **Hero layout**: 유지, CTA stack
- **Image strategy**: Next.js Image + srcset
- **First-class**: mobile-first (Tailwind 기본)

---

## 13. Components

> Primary CTA + Secondary CTA + 로고 월 + feature card. Tailwind 유틸 조합.

### .btn-primary

_Primary CTA — 블루 배경_

```html
<button style="background:#0B6EC5;color:#FFF;border:0;border-radius:6px;padding:10px 20px;font-size:14px;font-weight:500;cursor:pointer;">Get in touch</button>
```

Spec:

- background: #0B6EC5
- color: #FFFFFF
- padding: 10px 20px
- border-radius: 6px
- font-weight: 500

### .btn-secondary

_Secondary — ghost with border_

```html
<button style="background:transparent;color:#111;border:1px solid #E1E1E1;border-radius:6px;padding:10px 20px;font-size:14px;font-weight:500;cursor:pointer;">Get started</button>
```

Spec:

- background: transparent
- color: #111111
- border: 1px solid #E1E1E1
- hover: bg #FAFAFA

### .announcement-bar

_상단 공지 bar_

```html
<div style="background:#04122E;color:#FFF;padding:8px 16px;font-size:13px;border-radius:6px;">Introducing Database Traffic Control <a style="color:#73C7F9;margin-left:8px;">Learn more →</a></div>
```

Spec:

- background: #04122E (blue-950)
- color: #FFFFFF
- link color: #73C7F9

---

## 15. Drop-in CSS

```css
/* PlanetScale — copy into your root */
:root {
  /* Fonts */
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;

  /* Grayscale */
  --gray-50:  #FAFAFA;
  --gray-100: #EBEBEB;
  --gray-200: #E1E1E1;
  --gray-500: #818181;
  --gray-900: #111111;

  /* Brand */
  --blue-300: #73C7F9;
  --blue-700: #144EB6;
  --brand:    #0B6EC5;

  /* Surfaces */
  --bg:       #FFFFFF;
  --fg:       #111111;
  --muted-fg: #737373;
  --border:   #E1E1E1;

  /* Scale */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --space-4: 16px;
  --space-8: 32px;
  --space-16: 64px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — PlanetScale-like
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: { 300: '#73C7F9', 700: '#144EB6', DEFAULT: '#0B6EC5' },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui'],
        mono: ['ui-monospace', 'SF Mono', 'Menlo'],
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
| Brand primary | `--brand` | `#0B6EC5` |
| Background | `--bg` | `#FFFFFF` |
| Surface | `--gray-50` | `#FAFAFA` |
| Text primary | `--gray-900` | `#111111` |
| Text muted | `--gray-550` | `#737373` |
| Border | `--gray-200` | `#E1E1E1` |

### Example Component Prompts

#### Hero Section

```
PlanetScale 스타일 히어로를 만들어줘.
- 배경: #FFFFFF
- H1: Inter, 60px, weight 700, tracking -0.02em
- Sub: 18px, color #737373
- CTA: background #0B6EC5, padding 10px 20px, radius 6px
- 하단 로고 월 5개
```

#### Card

```
PlanetScale feature card:
- bg #FFFFFF, border 1px solid #E1E1E1, radius 8px
- padding 24px
- title 16px weight 600
- body 14px color #616161
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 #FFFFFF를 쓰고 surface는 --gray-50 #FAFAFA를 사용한다.
- CTA primary 배경은 반드시 #0B6EC5 (또는 --blue-700 #144EB6) — 다른 블루 금지.
- 카드는 1px solid #E1E1E1 border + 8-12px radius + shadow-sm.
- 본문은 Inter 16px / weight 400 / line-height 1.5로.
- 섹션 vertical padding은 64px-96px (py-16 / py-24)만 사용.

### ❌ DON'T

- 본문 텍스트를 #000000 또는 black으로 두지 말 것 — 대신 #111111 (gray-900) 사용.
- 섹션 배경을 #0B6EC5로 채우지 말 것 — 블루는 포인트용. 대신 #FFFFFF 또는 #FAFAFA.
- Tailwind arbitrary value (text-[13px]) 남용 금지 — text-sm / text-base 표준 스케일만.
- 카드 border를 #000이나 #CCC로 두지 말 것 — #E1E1E1 (gray-200).
- body에 font-weight: 300 쓰지 말 것 — PlanetScale은 400이 기본.
- radius 16px, 20px 같은 외부 값 금지 — 6 / 8 / 12 / 9999만.
