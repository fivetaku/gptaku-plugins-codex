---
schema_version: 3.1
slug: resend
service_name: Resend
site_url: https://resend.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#FFFFFF"
primary_font: Inter
font_weight_normal: 400
token_prefix: --color-*, --font-*
color_system: monochrome

bold_direction: "Monochrome Luxury"
aesthetic_category: "Monochrome Luxury"
signature_element: minimal_extreme
code_complexity: low

medium: web
medium_confidence: high
---

# DESIGN.md — Resend (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Resend 홈페이지는 #05050A 완전 블랙 + #FFFFFF ink의 monochrome luxury 톤이다. 다른 모든 SaaS가 브랜드 컬러 싸움을 할 때, Resend는 유일하게 'Email for developers'라는 카피와 함께 색 없이 승부한다. 히어로는 full-bleed black 배경에 도메인 식 H1 + 두 개의 ghost CTA + 상단 'Launch Week 6 is here' 라벨만 떠 있다.

컬러 전략은 블랙/화이트 + 9단 gray ramp + 희귀한 accent다. light-gray ramp는 #191919 → #333 → #656565 → #989898 → #BEBEBE → #D7D7D7 → #EEE → #F0F0F0 → #FFF의 9단계. chromatic accent는 CSS에 존재하지만(mint #62FFB3, cyan #2BF2FF, lime #FFFF92) 홈페이지 surface에는 거의 노출되지 않고 Launch Week 이미지나 캠페인에서만 쓰인다.

타이포그래피는 Inter + ABC Favorit + domaine (유료 세리프) 트리오다. body는 Inter 16px 400. 디스플레이용 Domaine 세리프가 hero H1 'Email for developers'에 쓰여 luxury editorial 감성을 만든다. 코드는 mono. weight scale은 400/500/600 3단으로 극도로 단순.

레이아웃은 1200px + full-bleed hero + 중앙 정렬 prose 패턴. 섹션 간 배경은 #05050A ↔ #14151799로 미세하게 변주된다. 카드는 거의 사용하지 않고, 대신 긴 텍스트 block과 code snippet block이 교대로 나온다. 네비게이션은 60px 정도 sticky + 간결한 링크 7개.

인터랙션은 extreme minimalism — hover 시 색상 약한 변화, 거의 모든 transition이 .15s ease. Launch Week 배너에서만 subtle gradient animation. code complexity 자체가 low로 판단될 만큼 마크업도 깔끔.

### Key Characteristics

- Full-bleed black
- Domaine serif
- 9-step gray
- Monochrome luxury
- Editorial H1
- Minimal extreme

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: Monochrome Luxury
> **Signature Element**: 이 사이트는 **검정 위 세리프 디스플레이의 절제된 자신감**으로 기억된다.
> **Code Complexity**: low — Resend의 monochrome luxury 팔레트 — 색 대신 세리프와 여백으로 브랜드를 세운다.

---

## 01. Quick Start

> 5분 안에 Resend처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: "Inter", ui-sans-serif, sans-serif;
  font-weight: 400;
  font-size: 16px;
}
h1, h2 {
  font-family: "Domaine Display",
    "ABC Favorit", Georgia, serif;
  font-weight: 500;
  letter-spacing: -0.02em;
}

/* 2. 배경 + 텍스트 (monochrome) */
:root {
  --bg: #05050A;
  --canvas: #14151799;
  --fg: #FDFDFD;
  --border: #323232;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. grayscale ramp (9단) */
:root {
  --gray-1: #F0F0F0;
  --gray-3: #D7D7D7;
  --gray-5: #989898;
  --gray-7: #656565;
  --gray-9: #333333;
  --gray-10: #191919;
}

```

**절대 하지 말아야 할 것 하나**: Resend에 brand color를 만들지 마라. 이 사이트의 정체성은 색이 없는 것이다. primary hex를 blue/orange/green으로 지어내면 다른 SaaS 클론이 된다. 반드시 black + Domaine serif로만 시그니처를 표현.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://resend.com</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 448,792 bytes (Next.js SSR) |
| CSS files | 6개 외부, 764KB |
| Token prefix | <code>--color-light-*</code>, <code>--color-gray-*</code>, <code>--font-*</code> |
| Color system | <code>monochrome</code> |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (React 18)
- **Design system**: 자체 토큰 + TipTap 에디터(docs)
- **CSS architecture**: CSS Modules + CSS Variables
- **Class naming**: CSS Modules
- **Default theme**: <code>dark</code> (bg <code>#05050A</code>)
- **Font loading**: Inter + ABC Favorit + Domaine (유료 self-host)
- **Canonical anchor**: <code>#FFFFFF</code> (monochrome — no chromatic brand)
- **Color system**: monochrome — brand은 tonality

---

## 04. Font Stack

- **Body**: <code>Inter</code> (OFL)
- **Display serif**: <code>Domaine Display</code> (유료)
- **Alt sans**: <code>ABC Favorit</code> (유료)
- **Fallback**: <code>ui-sans-serif, system-ui</code>
- **Weights**: 400 / 500 / 600

---

## 05. Typography Scale

> Inter 16px body + Domaine serif H1. Weight는 극도로 단순 (400/500/600).

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `caption` | 13px | 400 | 1.4 | 0 |
| `body` | 16px | 400 | 1.6 | 0 |
| `lead` | 18px | 400 | 1.5 | 0 |
| `H3` | 24px | 500 | 1.3 | -0.01em |
| `H2 (Domaine)` | 40px | 500 | 1.2 | -0.02em |
| `Hero H1 (Domaine)` | 64-80px | 500 | 1.05 | -0.02em |

---

## 06. Colors

> 오직 black + white + 9-step gray. chromatic accent는 캠페인 전용이며 일반 surface에 미노출.

### Grayscale 9-step

| Token | Hex |
|---|---|
| `gray-1` | `#F0F0F0` |
| `gray-2` | `#EEEEEE` |
| `gray-3` | `#D7D7D7` |
| `gray-4` | `#BEBEBE` |
| `gray-5` | `#989898` |
| `gray-7` | `#656565` |
| `gray-9` | `#333333` |
| `gray-10` | `#191919` |

### Ink Absolute

| Token | Hex |
|---|---|
| `black` | `#000000` |
| `bg-primary` | `#05050A` |
| `canvas` | `#141517` |
| `ink-mid` | `#1D1C1B` |
| `surface-dark` | `#26292E` |
| `border` | `#323232` |
| `border-strong` | `#2A2A2A` |

### White / Light surfaces

| Token | Hex |
|---|---|
| `white` | `#FFFFFF` |
| `fg-primary` | `#FDFDFD` |
| `slate-3` | `#0000330F` |
| `slate-7` | `#00062E32` |

### Campaign accent (rare)

| Token | Hex |
|---|---|
| `mint` | `#62FFB3` |
| `cyan` | `#2BF2FF` |
| `lime` | `#FFFF92` |
| `coral` | `#F76004` |
| `lavender` | `#9281F7` |
| `amber` | `#FFC446` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--background` | #000 — body background |
| `--canvas` | #14151799 — subtle surface tint |
| `--color-black` | #000 |
| `--color-light-gray-10` | #191919 — deepest surface |
| `--color-light-gray-7` | #656565 — muted text |
| `--color-light-gray-1` | #F0F0F0 — subtle light surface |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FDFDFD` | 9 | ink on dark |
| 2 | `#323232` | 12 | border |
| 3 | `#2A2A2A` | 10 | border strong |
| 4 | `#1D1C1B` | 8 | ink mid |
| 5 | `#05050A` | 8 | primary bg |
| 6 | `#26292E` | 8 | surface dark |
| 7 | `#62FFB3` | 20 | Launch Week mint (campaign) |
| 8 | `#22C55E` | 14 | status success |

---

## 07. Spacing

> 매우 넉넉한 여백 — 160px hero padding, 96-128px section. Luxury editorial rhythm.

container: 1200px · section py: 96-128px · hero py: 160px+

| Token | Value | Use |
|---|---|---|
| `space-2` | 8px | chip |
| `space-4` | 16px | button inner |
| `space-6` | 24px | card inner |
| `space-8` | 32px | card |
| `space-16` | 64px | section small |
| `space-24` | 96px | section standard |
| `space-32` | 128px | section luxury |
| `container` | 1200px | page width |

---

## 08. Radius

> 절제 — 4 / 6 / 8 / 12 / full. Hero CTA pill, 나머지는 square-ish.

| Token | Value | Context |
|---|---|---|
| `radius-sm` | 4px | chip |
| `radius-md` | 6px | input |
| `radius-lg` | 8px | button |
| `radius-xl` | 12px | card |
| `radius-full` | 9999px | tag / CTA pill |

---

## 09. Shadows

> 거의 없음. 있다면 1px border만.

| Level | Usage | Value |
|---|---|---|
| `border-only` | 기본 | `inset 0 0 0 1px #323232` |
| `cta hover` | subtle | `0 0 0 1px rgba(255,255,255,0.1)` |

---

## 10. Motion

> <code>.15s ease</code> 매우 빠른 색 전환만. 극도의 미니멀.

| Pattern | Value | Use |
|---|---|---|
| `transition-colors` | `150ms ease` | hover color/bg |
| `fade-in` | `300ms ease-out` | 섹션 페이드 인 |

---

## 11. Layout Patterns

> 1200px + 넉넉한 여백 + 중앙 텍스트 block 중심. 카드 거의 없음.

### Grid System

- Container: 1200px max
- Type: Flex + CSS Grid 혼합
- Columns: 12 (소수만 사용)
- Gutter: 16-24px

### Hero

- Layout: 1-column centered
- Background: full-bleed #05050A
- H1: Domaine 64-80px weight 500 tracking -0.02em
- Max-width: 800px
- Pattern: ~85vh + small top label + dual ghost CTA

### Section Rhythm

- Padding: 96-160px vertical
- Max-width: 1200px
- 섹션 간 bg tint 미세 변주

### Card Patterns

- 거의 사용 안 함. 대신 text block 위주
- 쓴다면 bg #14151799, border 1px solid #323232
- Radius: 8-12px

### Navigation

- Type: horizontal 8 links
- Position: sticky + blur
- Height: ~60px
- Background: rgba(5,5,10,0.8)

### Content Width

- Prose: 680px max
- Container: 1200px
- Hero max: 800px

---

## 12. Responsive Behavior

> Mobile-first. 768/1024/1280 3단 breakpoint — 단순.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 640px` | stack |
| Tablet | `≥ 768px` | 2-col if needed |
| Desktop | `≥ 1024px` | full layout |
| Large | `≥ 1280px` | container max |

### Collapsing Strategy

- **Touch targets**: button 44-48px
- **Nav collapse**: 768px 이하 햄버거
- **Grid**: 거의 stack
- **Hero**: 그대로 centered
- **CTA**: stack vertical
- **First-class**: mobile-first

---

## 13. Components

> Ghost CTA 2개 + small label pill + 텍스트 block. 카드 거의 없음.

### .btn-ghost

_monochrome CTA — ghost with border_

```html
<button style="background:transparent;color:#FDFDFD;border:1px solid #323232;border-radius:8px;padding:10px 20px;font-size:14px;font-weight:500;cursor:pointer;">Get Started</button>
```

Spec:

- background: transparent
- border: 1px solid #323232
- color: #FDFDFD
- radius: 8px
- weight: 500

### .btn-solid (light on dark)

_Primary CTA — white solid pill_

```html
<button style="background:#FDFDFD;color:#05050A;border:0;border-radius:8px;padding:10px 20px;font-size:14px;font-weight:600;cursor:pointer;">Get Started</button>
```

Spec:

- background: #FDFDFD
- color: #05050A
- radius: 8px
- padding: 10px 20px
- weight: 600

### .label-pill

_Launch Week 상단 배지_

```html
<span style="display:inline-flex;gap:6px;align-items:center;background:#14151799;color:#FDFDFD;border:1px solid #323232;border-radius:9999px;padding:4px 12px;font-size:12px;">🚀 Launch Week 6 is here</span>
```

Spec:

- bg: #14151799 subtle tint
- border: 1px solid #323232
- radius: 9999px pill
- font: 12px

---

## 15. Drop-in CSS

```css
/* Resend — copy into your root */
:root {
  --font-sans: "Inter", ui-sans-serif, sans-serif;
  --font-serif: "Domaine Display", "ABC Favorit", Georgia, serif;

  /* Monochrome (brand = absence of chromatic) */
  --bg:       #05050A;
  --canvas:   #14151799;
  --fg:       #FDFDFD;
  --fg-muted: #989898;
  --border:   #323232;

  /* Gray ramp */
  --gray-1:  #F0F0F0;
  --gray-3:  #D7D7D7;
  --gray-5:  #989898;
  --gray-7:  #656565;
  --gray-9:  #333333;
  --gray-10: #191919;

  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  --space-16: 64px;
  --space-24: 96px;
  --space-32: 128px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Resend-like (monochrome)
module.exports = {
  theme: {
    extend: {
      colors: {
        bg: '#05050A', canvas: '#14151799', fg: '#FDFDFD',
        gray: { 1:'#F0F0F0', 3:'#D7D7D7', 5:'#989898', 7:'#656565', 9:'#333333', 10:'#191919' },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif'],
        serif: ['"Domaine Display"', 'Georgia'],
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
| Background | `--bg` | `#05050A` |
| Surface | `--canvas` | `#14151799` |
| Text primary | `--fg` | `#FDFDFD` |
| Text muted | `--gray-5` | `#989898` |
| Border | `--border` | `#323232` |
| CTA solid | `--fg` | `#FDFDFD` |
| Accent (rare) | `campaign` | `#62FFB3` |

### Example Component Prompts

#### Hero

```
Resend 스타일 히어로:
- bg full-bleed #05050A
- 상단 label pill: 🚀 Launch Week 6 is here (border #323232, radius 9999px)
- H1: Domaine Display 72px weight 500 tracking -0.02em color #FDFDFD — 'Email for developers'
- Sub: Inter 18px color #989898
- CTA: 2개 (solid white + ghost dark border)
```

#### Ghost CTA

```
Resend ghost 버튼:
- bg transparent
- border 1px solid #323232
- color #FDFDFD
- radius 8px padding 10px 20px weight 500
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 #05050A near-absolute black — 순흑보다 0.01 warmer.
- H1은 반드시 Domaine 또는 세리프 디스플레이로 — Inter는 body 전용.
- primary CTA는 흰색 solid #FDFDFD, secondary는 ghost with border #323232.
- text muted는 #989898 (gray-5) — 너무 어두운 #656565은 hint/caption 전용.
- chromatic accent는 캠페인에만 예외적으로 허용.

### ❌ DON'T

- 임의의 brand color를 지어내지 말 것 — 이 사이트의 정체성은 색이 아니라 톤/타이포.
- 배경을 #000000 순흑으로 두지 말 것 — 대신 #05050A (미세 warmer).
- H1을 Inter로 두지 말 것 — Domaine 세리프가 시그니처.
- 본문 텍스트를 #FFFFFF 순백으로 두지 말 것 — #FDFDFD near-white.
- 카드를 남용하지 말 것 — Resend는 텍스트 block + 여백이 구조.
- body weight를 300로 두지 말 것 — 400.
- 색을 쓰고 싶으면 Launch Week 캠페인 스타일로만 (mint #62FFB3 등).
