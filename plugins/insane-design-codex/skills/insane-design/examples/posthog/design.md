---
schema_version: 3.1
slug: posthog
service_name: PostHog
site_url: https://posthog.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#F54E00"
primary_font: IBM Plex Sans Variable
font_weight_normal: 400
token_prefix: --tw-*, --swiper-*

bold_direction: "Warm Productivity"
aesthetic_category: "Editorial Magazine"
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — PostHog (Codex Edition)

---

## 00. Visual Theme & Atmosphere

PostHog 홈페이지는 개발자 제품 사이트 중에서도 유독 warm하고 playful한 에디토리얼 톤을 고수한다. 배경은 순백이 아니라 #EEEFE9 크림/paper 톤이고, 오렌지 #F54E00 브랜드 컬러가 CTA·헤드라인 밑줄·뱃지에 자유롭게 등장한다. 히어로는 약간의 하드보드 질감과 함께 커다란 브랜드 일러스트가 중앙을 차지한다.

컬러는 크림 paper + 오렌지 + 보조 yellow/teal/red의 에디토리얼 팔레트다. --bg가 RGB 채널 변수로 되어 있고(rgb(var(--bg))), 라이트 모드는 크림, 다크 모드는 #1E1F23 near-black으로 전환된다. accent는 #F54E00 (orange), #29DBBB (teal), #F7A501 (yellow), #E92F2F (red) — 모두 status/태그·강조로 쓴다.

타이포그래피는 IBM Plex Sans Variable을 body로 쓰고, 디스플레이용으로 Open Runde 같은 rounded geometric sans를 섞는다. 코드 폰트는 Source Code Pro. weight는 400/500/600/700의 표준 4단이지만, variable axis를 활용해 얇은 450/550 같은 중간값도 등장한다. 본문은 16px 기준.

레이아웃은 docs 중심 사이트답게 넓은 prose + 사이드바 ToC 패턴이 지배적이다. 홈에는 swiper carousel, 카드 리스트, big text section이 번갈아 나오고 Tailwind가 전체 CSS 뼈대다. 카드는 두꺼운 1px outline + pill 태그 + 짙은 shadow로 종이 카드처럼 보이는 질감을 만든다.

인터랙션은 Tailwind 기본 위에 swiper slide transition, hover lift, 유머러스한 이모지/아이콘이 얹혀있다. 속도는 .2s-.3s ease 중심으로 조금 느린 편이다. 전반적으로 '오픈소스 docs 사이트지만 브랜드가 또렷하다'는 입장.

### Key Characteristics

- Warm paper bg
- Orange accent
- Editorial magazine
- Open source docs
- Big illustration hero
- Swiper carousel

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Warm Productivity
> **Aesthetic Category**: Editorial Magazine
> **Signature Element**: 이 사이트는 **손글씨 느낌 + 오렌지 악센트의 Warm Docs**으로 기억된다.
> **Code Complexity**: medium — PostHog 홈페이지의 Tailwind + IBM Plex + 크림 paper 팔레트. 실제 CSS 추출로 만든 리포트.

---

## 01. Quick Start

> 5분 안에 PostHog처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: "IBM Plex Sans Variable",
    Arial, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: 238 239 233; /* #EEEFE9 cream */
  --fg: 30 31 35;    /* #1E1F23 ink */
  --accent: 245 78 0; /* orange */
}
body {
  background: rgb(var(--bg));
  color: rgb(var(--fg));
}

/* 3. 브랜드 오렌지 */
:root {
  --orange: #F54E00;
  --teal:   #29DBBB;
  --yellow: #F7A501;
  --red:    #E92F2F;
}

```

**절대 하지 말아야 할 것 하나**: PostHog의 bg를 #FFFFFF 순백으로 두지 마라. 반드시 #EEEFE9 cream paper. 순백으로 바꾸는 순간 워밍/에디토리얼 톤이 사라지고 일반 tech docs가 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://posthog.com</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 1,054,702 bytes (Gatsby/static) |
| CSS files | 1개 번들 (604KB minified) |
| Token prefix | <code>--tw-*</code> (Tailwind) + <code>--swiper-*</code> |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Gatsby (static site, MDX docs)
- **Design system**: Tailwind CSS + 자체 rgb() 토큰
- **CSS architecture**: utility-first + rgb(var(--x)) opacity 패턴
- **Class naming**: Tailwind + BEM hybrid
- **Default theme**: <code>light (cream)</code> + dark 전환 지원
- **Font loading**: IBM Plex Sans Variable (self-host), Open Runde, Source Code Pro
- **Canonical anchor**: <code>#F54E00</code> orange primary
- **Carousel**: swiper (v10+) with custom pagination colors

---

## 04. Font Stack

- **Body**: <code>IBM Plex Sans Variable</code> (OFL)
- **Display**: <code>Open Runde</code> (OFL)
- **Fallback**: <code>Arial, sans-serif</code>
- **Code**: <code>Source Code Pro</code> (OFL)
- **Weights**: 400 / 500 / 600 / 700 + variable axis 중간값

---

## 05. Typography Scale

> IBM Plex Sans + Open Runde 조합. 본문 16px, 헤드라인 36-72px 드라마틱 스케일.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `text-sm` | 14px | 400 | 1.5 | 0 |
| `text-base (body)` | 16px | 400 | 1.6 | 0 |
| `text-lg` | 18px | 500 | 1.5 | 0 |
| `text-2xl` | 24px | 600 | 1.3 | -0.01em |
| `text-4xl` | 36px | 700 | 1.2 | -0.02em |
| `text-6xl` | 60px | 700 | 1.05 | -0.03em |
| `text-7xl (hero)` | 72px | 700 | 1 | -0.03em |

---

## 06. Colors

> 크림 paper + 오렌지 + 4종 accent (teal/yellow/red/green). 에디토리얼 톤.

### Brand & Accents

| Token | Hex |
|---|---|
| `orange ★` | `#F54E00` |
| `orange-warm` | `#F7A501` |
| `teal` | `#29DBBB` |
| `red` | `#E92F2F` |
| `green` | `#6AA84F` |
| `green-vivid` | `#00FF00` |

### Neutral Paper (light)

| Token | Hex |
|---|---|
| `bg-cream` | `#EEEFE9` |
| `bg-white` | `#FFFFFF` |
| `surface` | `#F5E2B2` |
| `ink-primary` | `#1E1F23` |
| `ink-mid` | `#151515` |
| `ink-muted` | `#8D8D8D` |

### Neutral Dark

| Token | Hex |
|---|---|
| `bg-dark` | `#1E1F23` |
| `bg-darker` | `#161616` |
| `border-dark` | `#26292E` |
| `text-dark` | `#FFFFFF` |

### Tag / Highlight

| Token | Hex |
|---|---|
| `brand-orange-deep` | `#C23D00` |
| `brand-orange-shadow` | `#802700` |
| `yellow-highlight` | `#F1A82C` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--bg (light)` | 238 239 233 → #EEEFE9 cream paper |
| `--bg (dark)` | 30 31 35 → #1E1F23 near-black |
| `--accent` | #F54E00 — CTA, headline underline |
| `--swiper-pagination-color` | #F7A501 — carousel active dot |
| `--swiper-theme-color` | #007AFF — default (재정의됨) |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#F5E2B2` | 18 | warm tag bg |
| 2 | `#1E1F23` | 15 | dark ink/bg |
| 3 | `#F54E00` | 14 | brand orange |
| 4 | `#161616` | 10 | deep dark bg |
| 5 | `#8D8D8D` | 10 | muted text |
| 6 | `#FFFFFF` | 8 | card bg |
| 7 | `#29DBBB` | 8 | teal accent |
| 8 | `#E92F2F` | 8 | red alert |
| 9 | `#F7A501` | 8 | yellow swiper |

---

## 07. Spacing

> Tailwind 4px baseline + 자체 큰 섹션 여백 (py-24, py-32).

max-w-screen-2xl: 1536px · py-24 / py-32 섹션 · gap-6 / gap-8 카드

| Token | Value | Use |
|---|---|---|
| `p-2` | 8px | tag |
| `p-4` | 16px | button |
| `p-6` | 24px | card inner |
| `p-8` | 32px | card generous |
| `py-16` | 64px | section small |
| `py-24` | 96px | section standard |
| `py-32` | 128px | hero |
| `max-w-screen-2xl` | 1536px | page container |

---

## 08. Radius

> 둥글둥글한 rounded 철학 — 6/8/12/16/full 표준.

| Token | Value | Context |
|---|---|---|
| `rounded` | 4px | input |
| `rounded-md` | 6px | button |
| `rounded-lg` | 8px | card |
| `rounded-xl` | 12px | card large |
| `rounded-2xl` | 16px | hero card |
| `rounded-full` | 9999px | pill |

---

## 09. Shadows

> 두꺼운 1px border + 무거운 다크 shadow — 종이카드 질감.

| Level | Usage | Value |
|---|---|---|
| `shadow-sm` | 기본 카드 | `0 1px 2px rgba(0,0,0,0.1)` |
| `shadow-md` | feature card | `0 4px 8px rgba(0,0,0,0.12)` |
| `shadow-paper` | 종이 질감 | `0 6px 0 0 rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.08)` |

---

## 10. Motion

> swiper slide + hover lift. <code>.2s-.3s</code> ease out.

| Pattern | Value | Use |
|---|---|---|
| `slide transition` | `300ms ease` | swiper carousel |
| `hover lift` | `200ms ease` | card -translate-y-1 |
| `theme switch` | `200ms` | light↔dark |

---

## 11. Layout Patterns

> 1536px max + 사이드바 ToC(docs) + 카드 그리드. 홈은 carousel 중심.

### Grid System

- Container max-width: 1536px (max-w-screen-2xl)
- Grid type: CSS Grid (Tailwind)
- Columns: 2-3 카드 그리드
- Gutter: 24-32px (gap-6/gap-8)

### Hero

- Layout: 1-column centered + big illustration
- Background: #EEEFE9 cream paper
- H1: ~60-72px / weight 700 / tracking -0.03em
- Max-width: ~1000px
- Pattern: ~80vh + hero art + dual CTA

### Section Rhythm

- Padding: 96-128px vertical
- Max-width: 1536px
- 섹션 간 배경 톤 전환

### Card Patterns

- Background: white 또는 cream surface
- Border: 1-2px solid dark
- Radius: 12-16px
- Padding: 24-32px
- Shadow: 종이 paper offset

### Navigation

- Type: horizontal + mega menu
- Position: sticky top
- Height: ~64px
- Background: #EEEFE9 cream + blur

### Content Width

- Prose (docs): 720px
- Container: 1536px
- Sidebar: 280px (docs ToC)

---

## 12. Responsive Behavior

> Tailwind breakpoints (sm/md/lg/xl/2xl) + mobile-first. 사이드바는 lg부터 노출.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| sm | `≥ 640px` |  |
| md | `≥ 768px` | 2-col 그리드 |
| lg | `≥ 1024px` | 사이드바 복원 |
| xl | `≥ 1280px` | 3-col 그리드 |
| 2xl | `≥ 1536px` | 최대 너비 |

### Collapsing Strategy

- **Touch targets**: button 44px (h-11)
- **Nav collapse**: lg 이하 햄버거
- **Grid columns**: 3 → 2 → 1
- **Hero layout**: stack + 그림 압축
- **Swiper**: mobile slides-per-view 1.2
- **First-class**: mobile-first Tailwind

---

## 13. Components

> Primary CTA (orange) + swiper slide + badge tag + big hero illustration.

### .btn-primary

_오렌지 CTA — pill shape_

```html
<button style="background:#F54E00;color:#FFF;border:0;border-radius:6px;padding:12px 24px;font-size:15px;font-weight:600;cursor:pointer;">Get started - free</button>
```

Spec:

- background: #F54E00
- color: white
- radius: 6px
- padding: 12px 24px
- weight: 600

### .badge

_status/카테고리 태그_

```html
<span style="display:inline-flex;padding:4px 10px;background:#F5E2B2;color:#151515;border-radius:9999px;font-size:12px;font-weight:500;border:1px solid #1E1F23;">Product</span>
```

Spec:

- background: #F5E2B2
- border: 1px solid #1E1F23
- radius: 9999px
- font-size: 12px

### .paper-card

_종이 카드_

```html
<div style="background:#FFF;border:1px solid #1E1F23;border-radius:12px;padding:24px;box-shadow:4px 4px 0 0 #1E1F23;max-width:300px;"><div style="font-weight:700;margin-bottom:8px;">Session Replay</div><div style="color:#8D8D8D;font-size:14px;">Watch every user session</div></div>
```

Spec:

- bg: white
- border: 1px solid #1E1F23
- radius: 12px
- shadow: offset 4px 4px 0 dark

---

## 15. Drop-in CSS

```css
/* PostHog — copy into your root */
:root {
  --font-sans: "IBM Plex Sans Variable", Arial, sans-serif;
  --font-display: "Open Runde", var(--font-sans);
  --font-mono: "Source Code Pro", ui-monospace;

  /* Brand */
  --orange: #F54E00;
  --teal:   #29DBBB;
  --yellow: #F7A501;
  --red:    #E92F2F;

  /* Surfaces (light) */
  --bg: 238 239 233;   /* #EEEFE9 cream */
  --fg: 30 31 35;      /* #1E1F23 ink */
  --surface: #FFFFFF;
  --border: #1E1F23;

  /* Surfaces (dark) */
  --bg-dark: #1E1F23;
  --fg-dark: #FFFFFF;

  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-pill: 9999px;

  --space-6: 24px;
  --space-8: 32px;
  --space-24: 96px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — PostHog-like
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: { orange: '#F54E00', teal: '#29DBBB', yellow: '#F7A501', red: '#E92F2F' },
        bg: 'rgb(var(--bg) / <alpha-value>)',
        fg: 'rgb(var(--fg) / <alpha-value>)',
      },
      fontFamily: {
        sans: ['"IBM Plex Sans Variable"', 'Arial', 'sans-serif'],
        display: ['"Open Runde"', 'sans-serif'],
        mono: ['"Source Code Pro"', 'ui-monospace'],
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
| Brand primary | `--orange` | `#F54E00` |
| Background | `--bg (cream)` | `#EEEFE9` |
| Ink primary | `--fg` | `#1E1F23` |
| Surface | `--surface` | `#FFFFFF` |
| Text muted | `--muted` | `#8D8D8D` |
| Border dark | `--border` | `#1E1F23` |
| Accent teal | `--teal` | `#29DBBB` |

### Example Component Prompts

#### Hero Section

```
PostHog 스타일 히어로:
- 배경: #EEEFE9 cream paper
- H1: Open Runde, 72px, weight 700, tracking -0.03em
- Sub: 18px, #1E1F23
- CTA: bg #F54E00, radius 6px, padding 12px 24px, weight 600
- 중앙 히어로 일러스트
```

#### Paper card

```
PostHog 종이 카드:
- bg white, border 1px solid #1E1F23, radius 12px
- offset shadow: 4px 4px 0 0 #1E1F23
- padding 24px
- title weight 700, body color #8D8D8D
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 #EEEFE9 cream paper — 순백 절대 금지.
- 카드 border는 두꺼운 1-2px solid #1E1F23로 — 에디토리얼 톤.
- 종이 질감은 offset shadow 4px 4px 0 0 #1E1F23로 표현.
- 오렌지 #F54E00는 CTA와 headline 악센트에만.
- 헤드라인은 Open Runde rounded geometric을 쓴다 — body는 IBM Plex Sans.

### ❌ DON'T

- 배경을 #FFFFFF 또는 white로 두지 말 것 — 대신 #EEEFE9 (cream) 사용.
- 본문 텍스트를 #000000로 두지 말 것 — 대신 #1E1F23.
- 카드 border를 #E5E7EB 같은 light gray로 두지 말 것 — 반드시 dark #1E1F23.
- box-shadow를 0 1px 3px rgba(0,0,0,0.1) 표준으로 두지 말 것 — offset 4px 4px 0 0 paper 질감 필수.
- body weight를 300으로 두지 말 것 — PostHog는 400이 기본.
- 오렌지를 넓은 섹션 배경으로 쓰지 말 것 — CTA/강조 악센트 전용.
