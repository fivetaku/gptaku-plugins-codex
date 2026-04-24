---
schema_version: 3.1
slug: retool
service_name: Retool
site_url: https://retool.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#151515"
primary_font: Saans
font_weight_normal: 400
token_prefix: --btn-*, --raw-*

bold_direction: "Warm Productivity"
aesthetic_category: "Warm Productivity"
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Retool (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Retool 홈페이지는 #151515 거의-블랙 배경에 #E9EBDF warm cream 텍스트의 warm productivity 팔레트다. 다른 dark SaaS들이 cool grey (#0A0A0A, #F5F5F5)를 쓰는 반면, Retool은 greenish-warm ink + cream ivory 조합으로 '엔터프라이즈인데 따뜻함'을 표현한다. 히어로는 'Build how you want. Ship on a platform you can trust.' 를 Saans 세리프에 가까운 체로 중앙 정렬로 띄운다.

컬러는 warm near-black + cream ivory + PL blue accent + purple gradient의 4축이다. near-black은 #151515 → #242424 → #2E2F2D 3단, cream은 #F7F8F4 → #E9EBDF → #CBCCC4 → #C8BFB5 4단. #518DD2 (PL blue)가 257회 등장하며 CTA/link accent로 가장 빈번하게 쓰인다. #C72844 (red alert)와 pastel accent(#D0C1EA, #B0CCEA, #F5C2B2, #AFD1C6, #E8BAE8, #F6D6A0)는 Retool AppGen BETA 배지에 등장.

타이포그래피는 Saans + Px Grotesk 듀오다. var(--font-saans)가 43회 / var(--font-px-grotesk)가 8회. Saans는 soft warm serif-ish sans이고, Px Grotesk는 좀 더 geometric한 display sans. 본문 16px, Hero는 64-72px까지 확장. weight 400/500/600/700 표준.

레이아웃은 1200-1280px + centered hero + logo wall 패턴. Build how you want H1 아래 prompt input card(rounded, cream bg, orange-ish border)가 중앙에 자리하고, 하단에 Boeing/Adobe/DoorDash/OpenAI/Pernod Ricard 로고 월이 깔린다. 섹션 간 bg가 warm dark ↔ cream으로 drastic하게 전환되기도 한다.

인터랙션은 medium complexity — hover bg 변화, button state 전환, prompt input focus 링. transition은 .2s ease-out.

### Key Characteristics

- Warm ink #151515
- Cream text #E9EBDF
- Saans display
- Prompt input hero
- PL blue accent
- Warm productivity

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Warm Productivity
> **Aesthetic Category**: Warm Productivity
> **Signature Element**: 이 사이트는 **#151515 ink 위 cream serif의 엔터프라이즈 톤**으로 기억된다.
> **Code Complexity**: medium — Retool의 warm ink + cream ivory + Saans/Px Grotesk 듀오 디자인 시스템.

---

## 01. Quick Start

> 5분 안에 Retool처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: var(--font-saans), Saans,
    -apple-system, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}
.display {
  font-family: var(--font-px-grotesk),
    "Px Grotesk", sans-serif;
}

/* 2. 배경 + 텍스트 (warm dark) */
:root {
  --bg:      #151515;
  --bg-mid:  #242424;
  --bg-alt:  #2E2F2D;
  --fg:      #E9EBDF; /* cream ivory */
  --fg-mid:  #CBCCC4;
  --fg-muted:#C8BFB5;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. primary CTA + accent */
:root {
  --btn-primary-bg:       #151515;
  --btn-primary-icon:     #E9EBDF;
  --btn-primary-hover-bg: #2E2F2D;
  --accent-blue:          #518DD2;
  --alert-red:            #C72844;
}

```

**절대 하지 말아야 할 것 하나**: Retool의 포인트는 warm ink다. #000000 순흑이나 #0A0A0A cool black으로 두지 마라. 반드시 #151515 + #E9EBDF cream 쌍이어야 Retool 톤. Notion처럼 #FFFFFF 배경으로 두면 enterprise trust가 사라진다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://retool.com</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 391,416 bytes (Next.js SSR) |
| CSS files | 6개 외부, 656KB |
| Token prefix | <code>--btn-*</code>, <code>--raw-*</code>, <code>--alert-*</code>, <code>--font-*</code> |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (React) + MDX docs
- **Design system**: 자체 토큰 — btn/alert/raw prefix
- **CSS architecture**: semantic 3-tier (raw → btn/alert/etc → component)
- **Class naming**: CSS Modules + BEM
- **Default theme**: <code>dark warm</code> (bg <code>#151515</code>)
- **Font loading**: Saans + Px Grotesk (self-host)
- **Canonical anchor**: <code>#151515</code> (bg ink = brand)
- **Accent system**: PL blue 257회 등장

---

## 04. Font Stack

- **Body/Display**: <code>Saans</code> (유료)
- **Display alt**: <code>Px Grotesk</code> (유료)
- **Fallback**: <code>-apple-system, system-ui</code>
- **Weights**: 400 / 500 / 600 / 700

---

## 05. Typography Scale

> Saans body 16px + Px Grotesk display. Hero 64-72px weight 600-700.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `caption` | 12px | 400 | 1.4 | 0 |
| `body` | 16px | 400 | 1.5 | 0 |
| `lead` | 18px | 400 | 1.5 | 0 |
| `H3` | 24px | 500 | 1.3 | -0.01em |
| `H2` | 40px | 600 | 1.2 | -0.02em |
| `Hero H1 (Saans)` | 64-72px | 600 | 1.05 | -0.03em |

---

## 06. Colors

> Warm #151515 ink + #E9EBDF cream + PL blue #518DD2 + pastel BETA accents.

### Warm Ink (bg)

| Token | Hex |
|---|---|
| `bg-primary ★` | `#151515` |
| `bg-mid` | `#242424` |
| `bg-alt` | `#2E2F2D` |

### Cream Text (fg)

| Token | Hex |
|---|---|
| `fg-primary` | `#E9EBDF` |
| `fg-mid` | `#CBCCC4` |
| `fg-muted` | `#C8BFB5` |
| `fg-surface` | `#F7F8F4` |

### Accent (PL Blue 257x)

| Token | Hex |
|---|---|
| `blue-accent ★` | `#518DD2` |
| `blue-soft` | `#B0CCEA` |
| `red-alert` | `#C72844` |
| `red-soft` | `#E79295` |
| `red-fg` | `#651722` |

### Pastel BETA

| Token | Hex |
|---|---|
| `lavender` | `#D0C1EA` |
| `sky` | `#B0CCEA` |
| `peach` | `#F5C2B2` |
| `mint` | `#AFD1C6` |
| `lilac` | `#E8BAE8` |
| `cream` | `#F6D6A0` |

### Gradient Purple

| Token | Hex |
|---|---|
| `purple-primary` | `#9874D2` |
| `coral` | `#E8765E` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--btn-primary-bg` | #151515 — CTA default bg |
| `--btn-primary-icon` | #E9EBDF — CTA fg |
| `--btn-primary-hover-bg` | #2E2F2D — CTA hover |
| `--alert-default-bg` | #E79295 — alert pastel |
| `--alert-default-stroke` | #C72844 — alert border |
| `--btn-secondary-blue-stroke` | #B0CCEA — secondary blue border |
| `--raw-purple-primary` | gradient anchor |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#151515` | 933 | primary ink/bg |
| 2 | `#E9EBDF` | 908 | primary cream fg |
| 3 | `#518DD2` | 257 | PL blue accent |
| 4 | `#C72844` | 143 | alert red |
| 5 | `#CBCCC4` | 135 | fg-mid |
| 6 | `#C8BFB5` | 120 | fg-muted |
| 7 | `#F7F8F4` | 113 | surface light |
| 8 | `#242424` | 97 | bg-mid |

---

## 07. Spacing

> 1200-1280px 컨테이너 + 96-128px section. Enterprise calm density.

container: 1280px · section py: 96-128px · card padding 24-32px

| Token | Value | Use |
|---|---|---|
| `space-1` | 4px |  |
| `space-2` | 8px | chip |
| `space-4` | 16px | button inner |
| `space-6` | 24px | card inner |
| `space-8` | 32px | card large |
| `space-16` | 64px | section small |
| `space-24` | 96px | section |
| `container` | 1280px | page width |

---

## 08. Radius

> 8-16px card + 8px button. prompt card는 12px.

| Token | Value | Context |
|---|---|---|
| `radius-sm` | 4px | chip |
| `radius-md` | 8px | button |
| `radius-lg` | 12px | prompt card |
| `radius-xl` | 16px | hero card |
| `radius-pill` | 9999px | tag |

---

## 09. Shadows

> 다크 테마라 shadow 거의 없음. prompt card는 subtle border glow.

| Level | Usage | Value |
|---|---|---|
| `card border` | 기본 | `inset 0 0 0 1px #242424` |
| `prompt focus` | input focus | `0 0 0 2px rgba(200,101,77,0.3)` |
| `card hover` | light theme | `0 2px 4px rgba(0,0,0,0.08)` |

---

## 10. Motion

> <code>.2s ease-out</code>. button state 전환 + prompt input focus.

| Pattern | Value | Use |
|---|---|---|
| `transition-colors` | `200ms ease-out` | button bg/icon |
| `fade-in` | `400ms` | logo wall reveal |
| `input focus` | `150ms ease` | ring 확장 |

---

## 11. Layout Patterns

> 1280px + centered hero + prompt input card + logo wall + alternating warm/cream sections.

### Grid System

- Container: 1280px max
- Grid type: CSS Grid + Flex
- Columns: 6 (logo wall)
- Gutter: 16-24px

### Hero

- Layout: 1-column centered + prompt card
- Background: #151515 warm ink
- H1: Saans 64-72px weight 600 color #E9EBDF
- Max-width: ~900px
- Pattern: ~90vh + BETA pill top + prompt input card + logo wall

### Section Rhythm

- Padding: 96-128px
- Max-width: 1280px
- warm dark ↔ cream 섹션 drastic 전환

### Card Patterns

- Background: #242424 (on dark) / #F7F8F4 (on light)
- Border: 1px solid #2E2F2D
- Radius: 8-12px
- Padding: 24-32px

### Navigation

- Type: horizontal + mega menu
- Position: sticky + blur
- Height: ~64px
- Background: rgba(21,21,21,0.85) blur

### Content Width

- Prose: 720px
- Container: 1280px
- Hero max: 900px

---

## 12. Responsive Behavior

> Mobile-first. 640/768/1024/1280 breakpoints.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 640px` | stack |
| Tablet | `≥ 768px` | 2-col |
| Desktop | `≥ 1024px` | full nav |
| Large | `≥ 1280px` | container |

### Collapsing Strategy

- **Touch targets**: button 40-48px
- **Nav collapse**: 1024px 이하 햄버거
- **Logo wall**: 6 → 3 → 2
- **Prompt card**: mobile stack
- **Hero H1**: mobile 40-48px
- **First-class**: mobile-first

---

## 13. Components

> Primary pill CTA + BETA badge + prompt input card + logo wall.

### .btn-primary (pill)

_Start for free — cream pill_

```html
<button style="background:#E9EBDF;color:#151515;border:0;border-radius:9999px;padding:10px 24px;font-size:14px;font-weight:600;cursor:pointer;">Start for free</button>
```

Spec:

- background: #E9EBDF
- color: #151515
- radius: 9999px pill
- padding: 10px 24px
- weight: 600

### .btn-secondary (ghost pill)

_Book a demo — ghost_

```html
<button style="background:transparent;color:#E9EBDF;border:1px solid #E9EBDF;border-radius:9999px;padding:10px 24px;font-size:14px;font-weight:500;cursor:pointer;">Book a demo</button>
```

Spec:

- background: transparent
- border: 1px solid #E9EBDF
- color: #E9EBDF
- radius: 9999px

### .beta-badge

_BETA 배지_

```html
<span style="display:inline-flex;gap:6px;align-items:center;"><span style="background:#B0CCEA;color:#151515;font-size:11px;font-weight:700;padding:2px 6px;border-radius:4px;">BETA</span><span style="color:#E9EBDF;font-size:13px;">Explore Retool&apos;s AppGen →</span></span>
```

Spec:

- BETA bg: #B0CCEA pastel blue
- BETA color: #151515
- radius: 4px

### .prompt-card

_중앙 prompt input_

```html
<div style="background:#242424;border:1px solid #E8765E;border-radius:12px;padding:20px;max-width:420px;color:#E9EBDF;"><div style="color:#CBCCC4;margin-bottom:60px;font-size:14px;">Build me a manufacturing dashboard...</div><button style="float:right;background:#E9EBDF;color:#151515;border:0;border-radius:9999px;padding:6px 14px;font-size:13px;font-weight:600;">Start building</button></div>
```

Spec:

- bg: #242424
- border: 1px solid #E8765E (coral)
- radius: 12px
- CTA radius: 9999px

---

## 15. Drop-in CSS

```css
/* Retool — copy into your root */
:root {
  --font-saans: "Saans", -apple-system, sans-serif;
  --font-px-grotesk: "Px Grotesk", sans-serif;

  /* Warm ink */
  --bg:     #151515;
  --bg-mid: #242424;
  --bg-alt: #2E2F2D;

  /* Cream fg */
  --fg:       #E9EBDF;
  --fg-mid:   #CBCCC4;
  --fg-muted: #C8BFB5;
  --fg-surface: #F7F8F4;

  /* Accent */
  --accent-blue: #518DD2;
  --accent-blue-soft: #B0CCEA;
  --alert-red:  #C72844;
  --alert-red-soft: #E79295;

  /* Button tokens */
  --btn-primary-bg:       var(--fg);       /* cream */
  --btn-primary-fg:       var(--bg);       /* dark */
  --btn-primary-hover-bg: var(--bg-alt);
  --btn-primary-hover-fg: var(--fg);

  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-pill: 9999px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Retool-like
module.exports = {
  theme: {
    extend: {
      colors: {
        bg: { DEFAULT: '#151515', mid: '#242424', alt: '#2E2F2D' },
        fg: { DEFAULT: '#E9EBDF', mid: '#CBCCC4', muted: '#C8BFB5', surface: '#F7F8F4' },
        brand: { blue: '#518DD2', alert: '#C72844' },
      },
      fontFamily: {
        sans: ['Saans', '-apple-system'],
        display: ['"Px Grotesk"', 'Saans'],
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
| Background | `--bg` | `#151515` |
| Surface | `--bg-mid` | `#242424` |
| Text primary | `--fg` | `#E9EBDF` |
| Text muted | `--fg-muted` | `#C8BFB5` |
| Accent blue | `--accent-blue` | `#518DD2` |
| Alert red | `--alert-red` | `#C72844` |
| Border | `--bg-alt` | `#2E2F2D` |

### Example Component Prompts

#### Hero

```
Retool 스타일 히어로:
- bg #151515
- BETA pill: bg #B0CCEA color #151515 radius 4px
- H1: Saans 72px weight 600 tracking -0.03em color #E9EBDF
- Sub: 18px color #CBCCC4
- prompt card: bg #242424 border 1px solid #E8765E radius 12px
- CTA pill: bg #E9EBDF color #151515 radius 9999px
```

#### Logo wall

```
Retool 로고 월:
- bg #242424
- grid 6-col (desktop)
- logo color #E9EBDF (cream monochrome)
- gap 48px
- padding-y 64px
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 #151515 warm ink — #000000 순흑 금지.
- 본문 텍스트는 #E9EBDF cream ivory — #FFFFFF 순백 금지.
- Primary CTA는 cream pill bg #E9EBDF + color #151515 + radius 9999px.
- accent blue #518DD2는 link/icon에만 — 배경 금지.
- BETA 배지는 pastel #B0CCEA / #D0C1EA / #F6D6A0 순환.
- Saans는 body+display 모두, Px Grotesk는 display-only로 병용.

### ❌ DON'T

- 배경을 #000000 순흑으로 두지 말 것 — 반드시 #151515 warm ink.
- 본문 텍스트를 #FFFFFF 순백으로 두지 말 것 — 대신 #E9EBDF cream.
- CTA radius를 6px, 8px로 두지 말 것 — 9999px pill이 표준.
- PL blue #518DD2를 넓은 배경 면적에 쓰지 말 것 — link/icon 전용.
- body weight를 300로 두지 말 것 — 400.
- 카드 bg를 #0A0A0A 같은 cool grey로 두지 말 것 — #242424 warm.
- H1을 Inter로 두지 말 것 — Saans 시그니처.
