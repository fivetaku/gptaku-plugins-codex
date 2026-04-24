---
schema_version: 3.1
slug: prisma
service_name: Prisma
site_url: https://www.prisma.io
fetched_at: 2026-04-20
default_theme: light
brand_color: "#16A394"
primary_font: Inter
font_weight_normal: 400
token_prefix: --color-*, --accent-*

bold_direction: "Refined SaaS"
aesthetic_category: "Refined SaaS"
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Prisma (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Prisma 홈페이지는 연한 민트 cyan 그라디언트가 상단부를 뒤덮는 다소 감성적인 라이트 테마다. 기본 배경은 #FAFAFA 근처에서 시작해 cyan #E0F7F5 톤이 hero 상단에 살짝 섞이고, 브랜드 teal #16A394가 CTA와 로고, 코드 스니펫 키워드에 제한적으로 등장한다. Postgres 커뮤니티 색(#336791)도 살짝 참조된다.

색상 전략은 teal 악센트 + 웜-neutral backbone + accent chart 5색이다. --accent #0D3A38 (deep teal) / --accent-foreground #71E8DF (bright teal) 쌍이 다크 코드 블록에서 쓰이고, chart 컬러로 #7F9CF5 indigo, #805AD5 purple, #D69E2E amber, #319795 teal이 있다. 다크 모드에서는 #131420, #1A202C 딥 블루 neutral 로 전환.

타이포그래피는 Inter + Mona Sans VF 조합이다. Mona Sans VF가 디스플레이 서체로 쓰여 hero H1 Postgres, perfectly managed. 같은 굵은 bold 72px 스케일을 만든다. 본문은 Inter 16px weight 400. 코드는 ui-monospace. weight는 400/500/600/700 표준.

레이아웃은 1280px 컨테이너 + 3-column feature 카드가 핵심 패턴이다. 카드에는 subtle cyan tint 배경 + Prisma 로고 아이콘이 들어간다. 헤더는 80px 정도의 넉넉한 글래스 nav에 GitHub star 카운터가 노출된다. hero CTA는 teal primary + 코드 스니펫 인라인 pill이 병치된다.

인터랙션은 .2s ease-out 기반, hover에서 button scale/color가 변하고 카드에 subtle lift가 있다. 코드 블록은 tabs 전환 인터랙션 포함. 전반적으로 Stripe/Supabase 미학에 더 editorial한 디스플레이 서체를 얹은 느낌.

### Key Characteristics

- Mint cyan hero
- Teal accent
- Mona Sans display
- Inter body
- 3-col feature grid
- GitHub star wall

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Refined SaaS
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **민트 그라디언트 배경 위 굵은 디스플레이**으로 기억된다.
> **Code Complexity**: medium — Prisma 홈페이지의 Inter + Mona Sans 조합, cyan 배경 + teal 악센트 디자인 시스템.

---

## 01. Quick Start

> 5분 안에 Prisma처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: "Inter", "Inter Fallback",
    -apple-system, sans-serif;
  font-weight: 400;
  font-size: 16px;
}
h1, h2, h3 {
  font-family: "Mona Sans VF", "Inter";
  font-weight: 700;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FAFAFA;
  --bg-hero: linear-gradient(
    to bottom,
    #E0F7F5 0%,
    #FAFAFA 60%
  );
  --fg: #111827;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 teal */
:root {
  --brand: #16A394;
  --brand-deep: #0D9488;
  --accent: #71E8DF;
  --accent-bg: #0D3A38;
}

```

**절대 하지 말아야 할 것 하나**: teal #16A394를 다크 배경에 그대로 쓰지 마라. 다크 모드에서는 반드시 #71E8DF (accent-foreground) 로 전환해야 대비가 유지된다. 모든 theme에 단일 teal을 고집하면 접근성이 깨진다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://www.prisma.io</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 437,800 bytes (Next.js SSR) |
| CSS files | 2개 외부, 236KB |
| Token prefix | <code>--color-*</code>, <code>--accent-*</code>, <code>--chart-*</code> |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Fumadocs (docs)
- **Design system**: 자체 토큰 + shadcn 일부 차용
- **CSS architecture**: semantic 2-tier (util + component)
- **Class naming**: Tailwind + CSS Modules
- **Default theme**: <code>light</code> (bg <code>#FAFAFA</code>), dark 지원
- **Font loading**: Inter (self-host) + Mona Sans VF + Inter Fallback
- **Canonical anchor**: <code>#16A394</code> teal primary
- **Color system**: brand teal + chart 5-color + shadcn neutral

---

## 04. Font Stack

- **Body**: <code>Inter</code> (OFL)
- **Display**: <code>Mona Sans VF</code> (OFL, variable)
- **Fallback**: <code>Inter Fallback</code>, system
- **Code**: <code>ui-monospace</code>
- **Weights**: 400 / 500 / 600 / 700

---

## 05. Typography Scale

> Inter body 16px + Mona Sans display hero 72px. 9단 스케일 (Tailwind 기반).

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `text-sm` | 14px | 400 | 1.5 | 0 |
| `text-base` | 16px | 400 | 1.6 | 0 |
| `text-lg` | 18px | 500 | 1.5 | 0 |
| `text-xl` | 20px | 500 | 1.4 | -0.01em |
| `text-3xl` | 30px | 700 | 1.2 | -0.02em |
| `text-5xl` | 48px | 700 | 1.1 | -0.02em |
| `text-7xl (hero H1)` | 72px | 700 | 1 | -0.03em |

---

## 06. Colors

> Teal brand + cyan hero tint + shadcn neutral + chart 5색. 가장 감성적인 light SaaS.

### Brand Teal (dual)

| Token | Hex |
|---|---|
| `teal-300` | `#2DD4BF` |
| `teal-400` | `#14B8A6` |
| `teal-500 ★` | `#16A394` |
| `teal-600` | `#0D9488` |
| `teal-700` | `#319795` |
| `teal-fg` | `#71E8DF` |
| `accent-bg` | `#0D3A38` |

### Neutral Light

| Token | Hex |
|---|---|
| `bg-primary` | `#FAFAFA` |
| `bg-page` | `#F9FAFB` |
| `card` | `#FFFFFF` |
| `border` | `#1D242F` |
| `text-primary` | `#111827` |
| `text-muted` | `#171717` |

### Neutral Dark

| Token | Hex |
|---|---|
| `bg-dark` | `#131420` |
| `card-dark` | `#1A202C` |
| `border-dark` | `#1D242F` |
| `text-dark` | `#F7FAFC` |

### Chart accents

| Token | Hex |
|---|---|
| `chart-1` | `#71E8DF` |
| `chart-2` | `#7F9CF5` |
| `chart-3` | `#319795` |
| `chart-4` | `#805AD5` |
| `chart-5` | `#D69E2E` |

### Status / Extra

| Token | Hex |
|---|---|
| `indigo` | `#4F46E5` |
| `indigo-500` | `#6366F1` |
| `red` | `#DC2626` |
| `orange` | `#EA580C` |
| `green-100` | `#99F6E4` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--background` | #131420 dark / #FAFAFA light |
| `--accent` | #0D3A38 — deep teal bg (dark codes) |
| `--accent-foreground` | #71E8DF — bright teal on dark |
| `--border` | #1D242F — neutral dark border |
| `--card` | #1A202C dark / #FFFFFF light |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#16A394` | 9 | brand teal |
| 2 | `#0D9488` | 8 | brand teal deep |
| 3 | `#14B8A6` | 7 | teal mid |
| 4 | `#2DD4BF` | 6 | teal light |
| 5 | `#1D242F` | 10 | border dark |
| 6 | `#F9FAFB` | 9 | surface light |
| 7 | `#F7FAFC` | 7 | card light |
| 8 | `#111827` | 5 | text primary |

---

## 07. Spacing

> Tailwind 4px baseline + Fumadocs container 1280px.

max-w-7xl: 1280px · py-24 / py-32 hero · gap-6 그리드

| Token | Value | Use |
|---|---|---|
| `p-2` | 8px | chip |
| `p-4` | 16px | button |
| `p-6` | 24px | card inner |
| `p-8` | 32px | card large |
| `py-16` | 64px | section |
| `py-24` | 96px | hero section |
| `max-w-7xl` | 1280px | container |

---

## 08. Radius

> Tailwind 기본 + 카드 12-16px. 버튼은 6-8px 표준.

| Token | Value | Context |
|---|---|---|
| `rounded-md` | 6px | button small |
| `rounded-lg` | 8px | button default |
| `rounded-xl` | 12px | card |
| `rounded-2xl` | 16px | hero block |
| `rounded-full` | 9999px | pill |

---

## 09. Shadows

> light 테마 기본 shadow-sm / md. 다크 테마는 shadow 거의 없음 (border 의존).

| Level | Usage | Value |
|---|---|---|
| `shadow-sm` | 카드 기본 | `0 1px 2px rgba(0,0,0,0.05)` |
| `shadow-md` | elevated | `0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06)` |
| `shadow-lg` | dropdown | `0 10px 15px rgba(0,0,0,0.1)` |

---

## 10. Motion

> <code>.2s ease-out</code> 기본 + tab 전환 <code>.3s</code>.

| Pattern | Value | Use |
|---|---|---|
| `transition-colors` | `200ms ease-out` | hover bg/color |
| `tab indicator` | `300ms ease-out` | 코드 탭 전환 |
| `card hover` | `200ms` | border-color + lift |

---

## 11. Layout Patterns

> 1280px 컨테이너, 3-col feature 그리드 + hero center + 코드 데모.

### Grid System

- Container max-width: 1280px (max-w-7xl)
- Grid type: CSS Grid
- Columns: 3 (feature) / 12 (prose)
- Gutter: 24px (gap-6)

### Hero

- Layout: 1-column centered + code pill
- Background: linear-gradient(to bottom, #E0F7F5, #FAFAFA)
- H1: Mona Sans 72px / weight 700 / tracking -0.03em
- Max-width: ~800px
- Pattern: ~70vh + sub + CTA + npx prisma init code pill

### Section Rhythm

- Padding: 96-128px
- Max-width: 1280px
- 섹션 간 배경 subtle 전환

### Card Patterns

- Background: white + cyan icon tint
- Border: 1px solid #1D242F(dark) or light gray
- Radius: 12-16px
- Padding: 24-32px
- Shadow: shadow-sm

### Navigation

- Type: horizontal + 드롭다운
- Position: sticky + backdrop-blur
- Height: ~64-80px
- Background: rgba(255,255,255,0.8) blur
- Extra: GitHub star counter pill

### Content Width

- Prose (docs): 720px
- Container: 1280px
- Sidebar: 280px Fumadocs ToC

---

## 12. Responsive Behavior

> Tailwind + Fumadocs breakpoints. Mobile-first.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| sm | `≥ 640px` | mobile landscape |
| md | `≥ 768px` | 2-col 카드 |
| lg | `≥ 1024px` | 사이드바 복원 |
| xl | `≥ 1280px` | 3-col 카드 |

### Collapsing Strategy

- **Touch targets**: button 40-48px
- **Nav collapse**: lg 이하 햄버거
- **Grid columns**: 3 → 2 → 1
- **Hero CTA**: stack vertical
- **Code tabs**: 스크롤 가능
- **First-class**: mobile-first

---

## 13. Components

> Teal primary CTA + code pill + 3-col feature + GitHub star counter.

### .btn-primary (teal)

_Primary CTA — teal solid_

```html
<button style="background:#16A394;color:#FFF;border:0;border-radius:8px;padding:12px 24px;font-size:15px;font-weight:600;cursor:pointer;">Create database</button>
```

Spec:

- background: #16A394
- color: white
- padding: 12px 24px
- radius: 8px
- weight: 600

### .code-pill

_Inline 코드 스니펫_

```html
<div style="display:inline-flex;align-items:center;gap:8px;background:#FFF;border:1px solid #1D242F;border-radius:8px;padding:10px 16px;font-family:ui-monospace;font-size:14px;color:#171717;">$ <span style="color:#319795;">npx prisma init</span></div>
```

Spec:

- bg: white
- border: 1px solid #1D242F
- font-family: monospace
- prefix color: #319795

### .feature-card

_cyan icon + title + description_

```html
<div style="background:#FFF;border:1px solid #1D242F22;border-radius:12px;padding:24px;max-width:280px;"><div style="width:40px;height:40px;background:#E0F7F5;border-radius:6px;margin-bottom:12px;"></div><div style="font-weight:700;margin-bottom:6px;">MCP Server</div><div style="color:#616161;font-size:14px;">Use AI to configure and manage databases.</div></div>
```

Spec:

- bg: white
- icon bg: #E0F7F5 cyan tint
- border: subtle
- radius: 12px

---

## 15. Drop-in CSS

```css
/* Prisma — copy into your root */
:root {
  --font-sans: "Inter", "Inter Fallback", -apple-system, sans-serif;
  --font-display: "Mona Sans VF", var(--font-sans);
  --font-mono: ui-monospace, "SF Mono", Menlo;

  /* Brand */
  --brand-teal-500: #16A394;
  --brand-teal-600: #0D9488;
  --accent: #0D3A38;
  --accent-foreground: #71E8DF;

  /* Surfaces light */
  --bg: #FAFAFA;
  --card: #FFFFFF;
  --border: #1D242F1A;
  --fg: #111827;

  /* Surfaces dark */
  --bg-dark: #131420;
  --card-dark: #1A202C;
  --border-dark: #1D242F;
  --fg-dark: #F7FAFC;

  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;

  --space-6: 24px;
  --space-24: 96px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Prisma-like
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          teal: '#16A394',
          DEFAULT: '#16A394',
        },
        accent: { DEFAULT: '#0D3A38', foreground: '#71E8DF' },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui'],
        display: ['"Mona Sans VF"', 'Inter'],
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
| Brand primary | `--brand-teal-500` | `#16A394` |
| Background | `--bg` | `#FAFAFA` |
| Card | `--card` | `#FFFFFF` |
| Text primary | `--fg` | `#111827` |
| Text muted | `—` | `#616161` |
| Border | `--border` | `#1D242F1A` |
| Accent bg | `--accent` | `#0D3A38` |

### Example Component Prompts

#### Hero

```
Prisma 스타일 히어로:
- 배경: linear-gradient(to bottom, #E0F7F5, #FAFAFA)
- H1: Mona Sans VF, 72px, weight 700, tracking -0.03em, color #111827
- Sub: Inter 18px, color #616161
- CTA primary: bg #16A394, color white, padding 12px 24px, radius 8px
- 옆에 code pill: $ npx prisma init
```

#### Feature card

```
Prisma feature card:
- bg #FFFFFF, border 1px solid rgba(29,36,47,0.1), radius 12px
- padding 24px
- icon box 40x40 bg #E0F7F5 radius 6px
- title weight 700, body color #616161
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- Hero 배경은 linear-gradient(to bottom, #E0F7F5, #FAFAFA) — 단색 아님.
- H1은 Mona Sans VF로 — Inter는 body 전용.
- Teal primary #16A394는 light theme, 다크는 #71E8DF로 전환.
- 카드 icon box에 #E0F7F5 cyan tint를 쓴다.
- 코드 스니펫 inline pill은 border 1px solid #1D242F + monospace.

### ❌ DON'T

- 본문 텍스트를 #000000로 두지 말 것 — 대신 #111827.
- Hero 배경을 #FFFFFF 순백으로 두지 말 것 — cyan gradient 필수.
- 다크 모드에서 teal #16A394를 foreground로 쓰지 말 것 — 대신 #71E8DF.
- H1을 Inter로 두지 말 것 — Mona Sans VF 디스플레이만.
- Chart 컬러 5색을 임의로 재배정하지 말 것 — #71E8DF #7F9CF5 #319795 #805AD5 #D69E2E 순서 고정.
