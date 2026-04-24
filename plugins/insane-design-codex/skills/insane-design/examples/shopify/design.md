---
schema_version: 3.1
slug: shopify
service_name: Shopify
site_url: https://www.shopify.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#008060"
primary_font: ShopifySans
font_weight_normal: 400
token_prefix: --color-shade-*, --color-pistachio-*

bold_direction: "Cinematic Commerce"
aesthetic_category: "Cool Productivity"
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
campaign_active: true
---

# DESIGN.md — Shopify (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Shopify.com 홈페이지는 full-bleed 인물 영상/이미지 배경 + #02090A deep ink 오버레이 + 흰 CTA pill로 구성된 cinematic commerce 톤이다. 'Be the next big thing' 카피 위에 전체 화면 영상이 흐르고, 하단 좌측에 'Dream big, build fast, and grow far on Shopify.' 서브 카피와 2개의 CTA(흰 solid + ghost pill). 오픈 이커머스 브랜드답게 hero가 inspiration 자체가 되도록 설계.

컬러 전략은 rich black + zinc neutral 7단 + green brand accent + campaign 다색이다. 기본 surface는 #02090A rich-black → #061A1C → #000A1E 계열 cinematic dark이고, zinc-style neutral #F4F4F5 / #D4D4D8 / #A1A1AA / #71717A / #52525B이 마케팅 subpage에서 재활용된다. 핵심 브랜드 색은 #008060 Shopify green이지만 홈 hero에서는 거의 보이지 않고, 앱 내부 / pricing에서 primary CTA로 등장한다. campaign_active: true — hero 비주얼은 Shopify Editions마다 회전된다.

타이포그래피는 ShopifySans + PolySans + Trap 트리오. ShopifySans는 custom geometric sans (웹폰트 자체 호스팅, 6회 font-family 등장). 다국어 지원을 위해 Noto Sans JP 등도 번들. hero H1은 weight 700, ~80-96px 스케일. 본문은 PolySans 16-18px.

레이아웃은 1280-1440px + centered text block + full-bleed hero media. hero 바로 아래에 logo parade, feature cards (alternating dark/light bands), 통계 카운터, CTA 재노출의 전형적 commerce 홈 구조. 카드는 rounded 16px + 1px border + subtle gradient 액센트.

인터랙션은 high — hero video loop, scroll-triggered reveal, carousel, hover 3D tilt, accordion 등. transition .3s cubic-bezier(.4,0,.2,1) 기반.

### Key Characteristics

- Hero video
- Rich black #02090A
- ShopifySans geometric
- Zinc neutral 7-step
- Campaign rotating
- Cinematic commerce

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Cinematic Commerce
> **Aesthetic Category**: Cool Productivity
> **Signature Element**: 이 사이트는 **hero video 위 'Be the next big thing'의 cinematic commerce**으로 기억된다.
> **Code Complexity**: high — Shopify 홈페이지의 ShopifySans + rich-black + green brand 디자인 시스템. 캠페인마다 hero 비주얼 회전.

---

## 01. Quick Start

> 5분 안에 Shopify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: "ShopifySans", "PolySans",
    "Inter", -apple-system, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}
.display {
  font-family: "Trap", "ShopifySans", sans-serif;
  font-weight: 700;
}

/* 2. 배경 + 텍스트 (rich black) */
:root {
  --bg:         #02090A; /* rich-black */
  --bg-surface: #061A1C;
  --bg-darker:  #000A1E;
  --fg:         #FFFFFF;
  --fg-muted:   #A1A1AA;
  --border:     #71717A;
}
body { background: var(--bg); color: var(--fg); }

/* 3. Brand green + zinc */
:root {
  --brand:       #008060;
  --brand-soft:  #C1FBD4; /* aloe-10 */
  --accent-mint: #36F4A4;
  --zinc-10:     #F4F4F5;
  --zinc-40:     #A1A1AA;
}

```

**절대 하지 말아야 할 것 하나**: Shopify 홈 hero의 배경을 녹색 #008060로 채우지 마라. home hero는 full-bleed 영상/인물 이미지 + #02090A overlay다. 브랜드 그린은 app 내부 / pricing / success 상태에만 등장한다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://www.shopify.com</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 615,274 bytes (Next.js SSR) |
| CSS files | 1개 번들 (248KB) |
| Token prefix | <code>--color-shade-*</code>, <code>--color-pistachio-*</code>, <code>--color-aloe-*</code> |
| Campaign | <code>campaign_active: true</code> — hero 비주얼 Editions마다 회전 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Liquid (legacy docs)
- **Design system**: Polaris-inspired 자체 토큰 (홈은 별도 마케팅 팀)
- **CSS architecture**: CSS Modules + Tailwind 하이브리드
- **Class naming**: CSS Modules (<code>hero_bg_xxx</code>)
- **Default theme**: <code>dark</code> (bg <code>#02090A</code>) — 섹션마다 변주
- **Font loading**: ShopifySans + PolySans + Trap + Noto Sans JP (multi-lang)
- **Canonical anchor**: <code>#008060</code> Shopify green (marketing hero 외)
- **Campaign hero**: rotating video/image per Editions

---

## 04. Font Stack

- **Primary**: <code>ShopifySans</code> (자체)
- **Display**: <code>Trap</code> (유료)
- **Alt**: <code>PolySans</code> (유료)
- **Multi-lang**: <code>Noto Sans JP</code>
- **Code**: <code>IBMPlexMono</code>
- **Weights**: 400 / 500 / 600 / 700

---

## 05. Typography Scale

> ShopifySans body 16px + Trap display hero 80-96px. Weight 4단.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `caption` | 13px | 400 | 1.4 | 0 |
| `body` | 16px | 400 | 1.5 | 0 |
| `lead` | 18px | 400 | 1.5 | 0 |
| `H3` | 28px | 600 | 1.3 | -0.01em |
| `H2` | 48px | 700 | 1.15 | -0.02em |
| `Hero H1 (Trap)` | 80-96px | 700 | 0.95 | -0.03em |

---

## 06. Colors

> Rich black + zinc 7-step + Shopify green + Editions campaign accent (mint/cyan/purple).

### Rich Black (bg)

| Token | Hex |
|---|---|
| `rich-black ★` | `#02090A` |
| `bg-surface` | `#061A1C` |
| `bg-darker` | `#000A1E` |
| `bg-alt` | `#0A2C30` |
| `bg-forest` | `#11352D` |
| `bg-forest-deep` | `#133B32` |

### Shopify Green

| Token | Hex |
|---|---|
| `brand ★` | `#008060` |
| `aloe-10` | `#C1FBD4` |
| `pistachio-10` | `#D4F9E0` |
| `mint-accent` | `#36F4A4` |

### Zinc Neutral (7-step)

| Token | Hex |
|---|---|
| `shade-10` | `#F4F4F5` |
| `shade-20` | `#E4E4E7` |
| `shade-30` | `#D4D4D8` |
| `shade-40` | `#A1A1AA` |
| `shade-50` | `#71717A` |
| `shade-100` | `#000000` |
| `link-dark` | `#9797A2` |

### Campaign (rotating)

| Token | Hex |
|---|---|
| `cyan` | `#30DEEE` |
| `cyan-vivid` | `#02F0FF` |
| `purple` | `#751BE9` |
| `purple-soft` | `#9A5BFD` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--color-shade-10` | #F4F4F5 — zinc lightest |
| `--color-shade-40` | #A1A1AA — muted text |
| `--color-rich-black` | #02090A — primary bg |
| `--color-link-dark` | #9797A2 — link on dark |
| `--color-link-dark-focus` | #FFFFFF — link focus |
| `--color-aloe-10` | #C1FBD4 — brand soft |
| `--color-pistachio-10` | #D4F9E0 — accent soft |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#D4D4D8` | 17 | zinc 30 |
| 2 | `#71717A` | 16 | zinc 50 muted |
| 3 | `#061A1C` | 16 | surface dark |
| 4 | `#F4F4F5` | 15 | zinc 10 |
| 5 | `#A1A1AA` | 13 | zinc 40 |
| 6 | `#02090A` | 10 | rich-black bg |
| 7 | `#36F4A4` | 8 | campaign mint |
| 8 | `#008060` | 6 | brand green |
| 9 | `#751BE9` | 5 | campaign purple |

---

## 07. Spacing

> 1440px 와이드 + 대형 섹션. Commerce hero답게 여백 공격적.

container: 1440px · hero: full-bleed 100vw · section py: 96-160px

| Token | Value | Use |
|---|---|---|
| `space-2` | 8px | chip |
| `space-4` | 16px | button inner |
| `space-6` | 24px | card |
| `space-8` | 32px | card large |
| `space-16` | 64px | section small |
| `space-24` | 96px | section |
| `space-40` | 160px | hero luxury |
| `container` | 1440px | wide page |

---

## 08. Radius

> 16-24px rounded + pill CTA. Hero media block 24px radius.

| Token | Value | Context |
|---|---|---|
| `radius-sm` | 6px | chip |
| `radius-md` | 12px | card small |
| `radius-lg` | 16px | card |
| `radius-xl` | 24px | hero media |
| `radius-pill` | 9999px | CTA |

---

## 09. Shadows

> 다크 배경 + full-bleed media라 shadow 거의 없음. hover subtle glow만.

| Level | Usage | Value |
|---|---|---|
| `card hover` | lift | `0 8px 16px rgba(0,0,0,0.4)` |
| `cta focus` | a11y | `0 0 0 3px rgba(54,244,164,0.4)` |

---

## 10. Motion

> <code>.3s cubic-bezier(.4,0,.2,1)</code>. hero video + scroll reveal + carousel.

| Pattern | Value | Use |
|---|---|---|
| `hero video` | `loop` | 100% CSS animation |
| `scroll reveal` | `400ms ease-out` | IntersectionObserver |
| `cta hover` | `200ms` | bg/scale 1.02 |
| `carousel` | `600ms ease` | slide snap |

---

## 11. Layout Patterns

> 1440px + full-bleed hero video/image + centered text overlay + alternating sections.

### Grid System

- Container: 1440px max
- Hero: 100vw full-bleed
- Grid type: CSS Grid
- Columns: 12 (or 3-4 카드)
- Gutter: 24-32px

### Hero

- Layout: full-bleed media + 좌측 하단 text block
- Background: autoplay video 또는 static image + rich-black overlay
- H1: Trap 80-96px weight 700 tracking -0.03em color #FFFFFF
- Max-width: ~640px text block
- Pattern: 100vh + 2 CTAs (white solid pill + ghost pill)

### Section Rhythm

- Padding: 96-160px vertical
- Max-width: 1440px
- 섹션 간 dark ↔ light drastic 전환

### Card Patterns

- Background: #061A1C / #FFFFFF (섹션 테마에 따라)
- Border: 1px solid shade-40/50
- Radius: 16-24px
- Padding: 24-40px

### Navigation

- Type: horizontal mega-menu
- Position: sticky + blur
- Height: ~64px
- Background: rgba(2,9,10,0.85) blur on dark

### Content Width

- Prose: 720px
- Container: 1440px
- Hero text: ~640px

---

## 12. Responsive Behavior

> Mobile-first. 640/768/1024/1280/1440 breakpoints.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 640px` | stack + hero text scale |
| Tablet | `≥ 768px` | 2-col |
| Desktop | `≥ 1024px` | full nav |
| Large | `≥ 1280px` | container wider |
| XL | `≥ 1440px` | container max |

### Collapsing Strategy

- **Touch targets**: button 44-48px
- **Nav collapse**: 1024px 이하 햄버거
- **Hero media**: mobile static image (video off)
- **Grid**: 4 → 2 → 1
- **CTA**: stack vertical
- **First-class**: mobile-first

---

## 13. Components

> Hero full-bleed media + 2-CTA pill + zinc logo parade + alternating card bands.

### .btn-primary (white pill)

_Start for free — white pill on dark_

```html
<button style="background:#FFFFFF;color:#02090A;border:0;border-radius:9999px;padding:12px 28px;font-size:15px;font-weight:600;cursor:pointer;">Start for free</button>
```

Spec:

- background: #FFFFFF
- color: #02090A
- radius: 9999px pill
- padding: 12px 28px
- weight: 600

### .btn-ghost (ghost pill)

_Why we build — ghost white pill_

```html
<button style="background:rgba(255,255,255,0.1);color:#FFFFFF;border:1px solid rgba(255,255,255,0.3);border-radius:9999px;padding:12px 28px;font-size:15px;font-weight:500;cursor:pointer;">Why we build Shopify</button>
```

Spec:

- background: rgba(255,255,255,0.1)
- border: 1px solid rgba(255,255,255,0.3)
- radius: 9999px

### .brand-cta (green)

_Shopify app / pricing primary_

```html
<button style="background:#008060;color:#FFFFFF;border:0;border-radius:9999px;padding:12px 28px;font-size:15px;font-weight:600;cursor:pointer;">Get started</button>
```

Spec:

- background: #008060
- color: #FFFFFF
- radius: 9999px
- (app/pricing only, not hero)

---

## 15. Drop-in CSS

```css
/* Shopify — copy into your root */
:root {
  --font-sans: "ShopifySans", "PolySans", "Inter", -apple-system, sans-serif;
  --font-display: "Trap", "ShopifySans", sans-serif;
  --font-mono: "IBMPlexMono", ui-monospace;

  /* Rich black */
  --bg:       #02090A;
  --bg-alt:   #061A1C;
  --bg-deep:  #000A1E;

  /* Zinc */
  --shade-10: #F4F4F5;
  --shade-20: #E4E4E7;
  --shade-30: #D4D4D8;
  --shade-40: #A1A1AA;
  --shade-50: #71717A;

  /* Brand */
  --brand:       #008060;
  --brand-soft:  #C1FBD4;
  --accent-mint: #36F4A4;

  /* Campaign */
  --campaign-cyan:   #30DEEE;
  --campaign-purple: #751BE9;

  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-pill: 9999px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Shopify-like
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: '#008060', soft: '#C1FBD4' },
        bg: { DEFAULT: '#02090A', alt: '#061A1C', deep: '#000A1E' },
        shade: { 10: '#F4F4F5', 20: '#E4E4E7', 30: '#D4D4D8', 40: '#A1A1AA', 50: '#71717A' },
      },
      fontFamily: {
        sans: ['ShopifySans', 'PolySans', 'Inter'],
        display: ['Trap', 'ShopifySans'],
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
| Background (home) | `--bg` | `#02090A` |
| Surface | `--bg-alt` | `#061A1C` |
| Text primary | `white` | `#FFFFFF` |
| Text muted | `--shade-40` | `#A1A1AA` |
| Brand green (app/pricing) | `--brand` | `#008060` |
| Campaign mint | `--accent-mint` | `#36F4A4` |
| Zinc border | `--shade-50` | `#71717A` |

### Example Component Prompts

#### Hero

```
Shopify 스타일 홈 히어로:
- full-bleed autoplay 영상 또는 static image (인물/제품 close-up)
- overlay: linear-gradient(rgba(2,9,10,0.3), rgba(2,9,10,0.85))
- H1: Trap 96px weight 700 color #FFFFFF tracking -0.03em
- Sub: ShopifySans 18px color #E4E4E7
- CTA 1: bg #FFFFFF color #02090A radius 9999px padding 12px 28px
- CTA 2: bg rgba(255,255,255,0.1) border 1px solid rgba(255,255,255,0.3) radius 9999px
```

#### App green CTA

```
Shopify pricing CTA (녹색):
- bg #008060, color #FFFFFF
- radius 9999px, padding 12px 28px
- weight 600
- hover: bg #006B50 (darken)
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- 홈 hero 배경은 full-bleed video/image + rich-black overlay — solid 배경 금지.
- CTA는 홈에서 white pill #FFFFFF, app/pricing에서 green pill #008060으로 구분.
- 모든 CTA radius는 9999px pill.
- display type은 Trap, body는 ShopifySans.
- zinc neutral은 shade-10 #F4F4F5 ~ shade-50 #71717A.
- campaign 활성 시 hero visual + accent 컬러(mint/cyan/purple) 회전 허용.

### ❌ DON'T

- 홈 hero 배경을 solid #008060 녹색으로 두지 말 것 — 반드시 full-bleed media.
- 본문 텍스트를 #FFFFFF로 고정하지 말 것 — shade-40 #A1A1AA 변주.
- CTA radius를 8px, 12px로 두지 말 것 — 9999px pill.
- body weight를 300로 두지 말 것 — 400.
- 카드 bg를 #000000 순흑으로 두지 말 것 — #02090A rich-black 또는 #061A1C.
- 폰트를 Inter로 두지 말 것 — ShopifySans 자체 시그니처.
- Shopify green #008060을 넓은 마케팅 섹션 배경으로 쓰지 말 것 — app/pricing 맥락 전용.
