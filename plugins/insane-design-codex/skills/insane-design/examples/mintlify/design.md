---
schema_version: 3.1
slug: mintlify
service_name: Mintlify
site_url: https://mintlify.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#0C8C5E"
primary_font: inter
font_weight_normal: 400
token_prefix: --color-brand, --font-*, --tw-*

bold_direction: "Documentation Clarity"
aesthetic_category: "Editorial Developer"
signature_element: minimal_extreme
code_complexity: low

medium: web
medium_confidence: high
---

# DESIGN.md — Mintlify (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Mintlify는 **개발자 문서를 위한 플랫폼**이다. 디자인은 이를 그대로 반영해 — **차분한 light 기본 + 녹색 브랜드 + Geist Mono 코드**. 페이지는 `#FFFFFF` 또는 warm neutral `#F7F7F7` 배경에 `#231F20` (warm black) 텍스트가 올려진다. 다크 모드 `#151616` 배경도 존재. 브랜드 green `#0C8C5E` (light) / `#18E299` (dark)가 단일 anchor — 문서 사이트답게 면적을 거의 쓰지 않고 link, CTA, code token color에만 한 점씩.

색상 전략은 **"문서가 읽혀야 한다"**. neutral 위주 팔레트 + 단일 mint green accent + warm neutral gradient. footer CTA 영역에서 `linear-gradient(#F7F7F7 0%, rgba(247,247,247,0.95) 4.7%, rgba(247,247,247,0.89) 8.8%, ... 0%)`처럼 **다중 stop gradient fade**로 섹션 경계를 부드럽게 처리하는 것이 관찰되는 시그니처 기법.

타이포그래피는 **Inter** + **Geist Mono** — Vercel/Next.js 생태계의 default 조합. weight `400 / 500 / 600 / 700 / 800 / 900`까지 사용. 히어로는 `800` 또는 `900`의 full weight로 임팩트.

레이아웃은 **좁은 prose 중앙**. docs 플랫폼답게 `prose max 720px` 기본, 마케팅 페이지는 `container 1200px`. radius는 Tailwind 기본 `--radius 0.5rem`.

인터랙션은 거의 없다 — 문서 사이트는 정적인 게 미덕. hover color 변화 + subtle transition만.

### Key Characteristics

- Light `#FFFFFF` / warm `#F7F7F7` / dark `#151616` 3단
- Brand mint green `#0C8C5E` (light) / `#18E299` (dark) 단일 anchor
- Inter + Geist Mono — Vercel 스택 default
- Multi-stop gradient fade (footer-cta-gradient 시그니처)
- Tailwind v4 + `--color-brand` semantic token
- Docs 중심 — prose 720px 좁은 칼럼

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Documentation Clarity
> **Aesthetic Category**: Editorial Developer
> **Signature Element**: 이 사이트는 **warm neutral + mint green single-accent + 다중 stop gradient fade**로 기억된다.
> **Code Complexity**: low — Tailwind v4 + semantic token 1-tier

---

## 01. Quick Start

> 5분 안에 Mintlify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "inter","Inter Fallback",
    -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 (light) */
:root {
  --bg:         #FFFFFF;
  --bg-warm:    #F7F7F7;
  --fg:         #231F20;
  --fg-muted:   #4A5565;
  --border:     #E5E7EB;
}
body { background: var(--bg); color: var(--fg); }
.dark { --bg: #151616; --fg: #F7F7F7; }

/* 3. Brand mint */
:root {
  --color-brand:       #0C8C5E;
  --color-brand-light: #0C8C5E;
}
.dark {
  --color-brand: #18E299;
}
```

**절대 하지 말아야 할 것 하나**: mint green `#0C8C5E`을 넓은 배경 면적에 쓰지 마라. 문서 사이트 브랜드는 neutral 위에 한 점의 초록이 포인트일 때만 성립한다. 녹색 배경은 Shopify·Duolingo지, Mintlify가 아니다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://mintlify.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 추출 완료 (Next.js SSR) |
| CSS files | 4개 외부 (총 ~225KB) |
| Token prefix | `--color-brand`, `--font-inter`, `--font-geist-mono`, `--tw-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Tailwind v4 (`--tw-*` variable system 감지)
- **Design system**: Tailwind v4 semantic tokens + `--color-brand*`
- **CSS architecture**: Tailwind v4 1-tier
  ```
  theme    (--color-brand, --font-inter)      semantic
  utility  (.text-*, .bg-*, .p-*)             tailwind utility
  custom   (.footer-cta-gradient)             component class
  ```
- **Class naming**: Tailwind utility + occasional component class
- **Default theme**: light (`.dark` class swap)
- **Font loading**: Inter (self-host) + Geist Mono (self-host)
- **Canonical anchor**: `#0C8C5E` (light) / `#18E299` (dark)

---

## 04. Font Stack

- **Display/Body**: `inter` + `inter Fallback`
- **Code**: `Geist Mono` + `Geist Mono Fallback`
- **Fallback**: `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`
- **Weight normal / bold**: `400` / `700`
- **Full weight range**: `100 / 400 / 500 / 600 / 700 / 800 / 900`

```css
:root {
  --font-inter: "inter","inter Fallback",
    -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --font-geist-mono: "Geist Mono","Geist Mono Fallback",
    ui-monospace,SFMono-Regular,Menlo,monospace;
}
body { font-family: var(--font-inter); }
code { font-family: var(--font-geist-mono); }
```

---

## 05. Typography Scale

| Token | Size | Weight | Line-height |
|---|---|---|---|
| text-xs | `12px` | 400 | 1.5 |
| text-sm | `14px` | 400 | 1.5 |
| text-base | `16px` | 400 | 1.6 |
| text-lg | `18px` | 500 | 1.55 |
| text-xl | `20px` | 600 | 1.4 |
| text-2xl | `24px` | 600 | 1.35 |
| text-3xl | `30px` | 700 | 1.25 |
| text-4xl | `36px` | 700 | 1.2 |
| text-5xl | `48px` | 800 | 1.1 |
| text-6xl | `60px` | 900 | 1.05 |
| display | `72–96px` | 900 | 1 |

> ⚠️ Mintlify 히어로 타이틀은 weight `800` 또는 `900`까지 쓴다 — 다른 docs 사이트보다 강한 임팩트.

---

## 06. Colors

### 06-1. Brand Mint (dual-theme)

| Token | Hex |
|---|---|
| `--color-brand` (light) | `#0C8C5E` |
| `--color-brand-light` | `#0C8C5E` |
| `--color-brand` (dark) | `#18E299` |

### 06-3. Neutral Warm Ramp

| Step | Hex | Usage |
|---|---|---|
| white | `#FFFFFF` | page bg |
| bg-warm | `#F7F7F7` | warm bg / section alt |
| bg-warm-2 | `#F5F5F5` | divider warm |
| paper | `#F1EFED` | card bg warm (관찰) |
| border | `#E5E7EB` | standard border |
| border-soft | `#D1D5DC` | soft border |
| text-muted | `#4A5565` | text secondary |
| text | `#231F20` | warm black text |
| black | `#000000` | hard ink |
| dark-bg | `#151616` | dark theme bg |
| dark-2 | `#0A0A0A` | deepest dark |
| slate | `#101828` | accent text dark |

### 06-4. Accent Families (seldom used — status icons only)

| Family | Hex | Use |
|---|---|---|
| royal-blue | `#003087` | accent highlight (rare) |
| sky | `#009CDE` | info |
| orange | `#FF5A00` | warning |
| link-blue | `#0070E0` | link (alt to brand) |
| purple | `#4B73FF` | highlight |
| indigo | `#5984F2` | highlight 2 |
| magenta | `#FF66F4` | accent extreme |
| pink | `#FF7EB0` | accent soft |
| red | `#FF0105` | error |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --bg | `#FFFFFF` (light) / `#151616` (dark) | 페이지 |
| --fg | `#231F20` / `#F7F7F7` | text primary |
| --color-brand | `#0C8C5E` / `#18E299` | link, CTA, code token |
| --border | `#E5E7EB` / `#27272A` | border |
| --bg-muted | `#F7F7F7` / `#0A0A0A` | 보조 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to |
|---|---|
| `--color-brand` | `#0C8C5E` / `#18E299` (theme) |
| `--color-brand-light` | `#0C8C5E` |
| `.footer-cta-gradient` | multi-stop linear-gradient `#F7F7F7` → transparent (light) / `#151616` → transparent (dark) |

### 06-7. Dominant Colors

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 62 | page bg |
| 2 | `#231F20` | 46 | warm black text |
| 3 | `#F1EFED` | 22 | paper bg |
| 4 | `#003087` | 14 | royal blue accent |
| 5 | `#0C8C5E` | 11 | brand mint |
| 6 | `#009CDE` | 10 | sky accent |
| 7 | `#FF5A00` | 10 | orange warn |
| 8 | `#000000` | 7 | hard ink |
| 9 | `#0A0A0A` | 6 | deepest dark |
| 10 | `#101828` | 6 | slate accent |

---

## 07. Spacing

Tailwind v4 — `--spacing` base `0.25rem` (4px).

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
| container | `1200px` |
| prose | `720px` |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| rounded-sm | `2px` | code token highlight |
| rounded | `4px` | badge |
| rounded-md | `6px` | button, input |
| rounded-lg | `8px` | card |
| rounded-xl | `12px` | card large |
| rounded-2xl | `16px` | hero block |
| rounded-full | `9999px` | avatar, pill |

---

## 09. Shadows

| Level | Value | Usage |
|---|---|---|
| shadow-sm | `0 1px 2px 0 rgba(0,0,0,0.05)` | subtle |
| shadow | `0 1px 3px 0 rgba(0,0,0,0.1)` | card rest |
| shadow-md | `0 4px 6px -1px rgba(0,0,0,0.1)` | hover |
| shadow-lg | `0 10px 15px -3px rgba(0,0,0,0.1)` | popover |

<!-- SOURCE: Tailwind default (Mintlify CSS에 custom shadow token 적음) -->

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| transition-base | `150ms cubic-bezier(.4,0,.2,1)` | hover |
| scale-90 | `90%` (scale transform) | press feedback |
| translate-y-2 | `2px` | subtle hover lift |

---

## 11. Layout Patterns

### Grid

- container `1200px`
- prose `720px`
- grid 12-col Tailwind

### Hero

- Pattern: `light bg + H1 display weight 900 + 단일 CTA primary + docs live preview`
- Bg: `#FFFFFF` + subtle warm gradient
- H1: Inter 72–96px weight 900
- Live preview: iframe or docs screenshot

### Section Rhythm

```css
section { padding-block: 96px; padding-inline: 24px; max-width: 1200px; }
```

### Card

- bg `#FFFFFF`, border `1px solid #E5E7EB`, radius `12px`, padding `24px`, shadow-sm

### Navigation

- height `64px` fixed top
- bg `rgba(255,255,255,0.95)` backdrop blur
- 로고 + Links + Docs + GitHub + CTA

### Footer CTA Gradient (시그니처)

```css
.footer-cta-gradient {
  background: linear-gradient(
    #F7F7F7 0%,
    rgba(247,247,247,0.95) 4.7%,
    rgba(247,247,247,0.89) 8.8%,
    rgba(247,247,247,0.827) 12.6%,
    rgba(247,247,247,0.76) 16.3%,
    rgba(247,247,247,0.69) 19.9%,
    rgba(247,247,247,0.615) 23.3%,
    /* ... 계속 세분화된 stop, 수십 개 */
  );
}
.dark .footer-cta-gradient {
  background: linear-gradient(
    #151616 0%,
    rgba(21,22,22,0.95) 4.7%, ...
  );
}
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

### Touch

- min tap `40px`
- button height `36–40px`

---

## 13. Components

### Buttons

```html
<button class="bg-[#0C8C5E] text-white px-4 py-2 rounded-md">Get started</button>
```

| Variant | bg | color | radius | padding |
|---|---|---|---|---|
| primary | `#0C8C5E` | `#FFFFFF` | `6px` | `8px 16px` |
| primary-dark | `#18E299` | `#151616` | `6px` | 동일 |
| ghost | transparent | `#231F20` | `6px` | 동일 |
| outline | border `#E5E7EB` | `#231F20` | `6px` | 동일 |

### Badges

- bg `rgba(12,140,94,0.1)`
- color `#0C8C5E`
- radius `9999px`
- font `Inter 12px weight 500`
- padding `2px 8px`

### Cards

- bg `#FFFFFF` / `#0A0A0A` (dark)
- border `1px solid #E5E7EB` / `#27272A`
- radius `12px`
- padding `24px`
- shadow-sm

### Navigation

- link Inter 14px weight 500 color `#4A5565`
- hover color `#231F20`
- active: color `#0C8C5E` weight 600

### Inputs

- height `40px`, padding `0 12px`
- bg `#FFFFFF`, border `1px solid #E5E7EB`, radius `6px`
- focus `outline 2px solid #0C8C5E`

### Hero

- bg `#FFFFFF`
- H1 Inter 96px weight 900 color `#231F20` ls `-0.04em`
- sub 20px color `#4A5565`
- CTA primary green + secondary ghost

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 가치 서술 | "Meet the modern standard for documentation" |
| Primary CTA | "Get started" | — |
| Secondary CTA | "Request demo" | — |
| Subheading | 기능 + dev focus | "Beautiful docs that scale with your users." |
| Tone | 차분, 신뢰 | — |

---

## 15. Drop-in CSS

```css
/* Mintlify — drop-in */
:root {
  --font-inter: "inter",-apple-system,sans-serif;
  --font-geist-mono: "Geist Mono",ui-monospace,Menlo,monospace;

  --bg: #FFFFFF;
  --bg-warm: #F7F7F7;
  --fg: #231F20;
  --fg-muted: #4A5565;
  --border: #E5E7EB;

  --color-brand: #0C8C5E;
  --color-brand-light: #0C8C5E;

  --radius: 8px;
  --radius-md: 12px;
}
.dark {
  --bg: #151616;
  --fg: #F7F7F7;
  --fg-muted: #9CA3AF;
  --border: #27272A;
  --color-brand: #18E299;
}
body { background: var(--bg); color: var(--fg); font-family: var(--font-inter); }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Mintlify
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: '#0C8C5E', dark: '#18E299' },
        warm: { 0: '#FFFFFF', 100: '#F7F7F7', 200: '#F1EFED' },
        ink: { DEFAULT: '#231F20', muted: '#4A5565' },
        dark: { bg: '#151616', deeper: '#0A0A0A' },
      },
      fontFamily: {
        sans: ['inter','-apple-system','BlinkMacSystemFont'],
        mono: ['Geist Mono','ui-monospace','SFMono-Regular'],
      },
      fontWeight: { normal:'400', medium:'500', semibold:'600', bold:'700', extrabold:'800', black:'900' },
      borderRadius: { sm:'2px', DEFAULT:'4px', md:'6px', lg:'8px', xl:'12px', '2xl':'16px', full:'9999px' },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand (light) | `--color-brand` | `#0C8C5E` |
| Brand (dark) | `--color-brand` | `#18E299` |
| Background | `--bg` | `#FFFFFF` |
| Warm bg | `--bg-warm` | `#F7F7F7` |
| Text | `--fg` | `#231F20` |
| Text muted | `--fg-muted` | `#4A5565` |
| Border | `--border` | `#E5E7EB` |

### Example Component Prompts

#### Hero

```
Mintlify 스타일 히어로를 만들어줘.
- 배경: #FFFFFF
- H1: Inter, 96px, weight 900, color #231F20, ls -0.04em
- sub: 20px color #4A5565
- CTA primary: bg #0C8C5E, color #FFFFFF, radius 6px, padding 8px 16px
- CTA ghost: bg transparent, color #231F20
- 중앙 또는 좌측 정렬, 하단 docs live preview iframe (radius 12px)
```

#### Card

```
Mintlify 스타일 문서 카드를 만들어줘.
- bg #FFFFFF, border 1px solid #E5E7EB, radius 12px, padding 24px
- shadow 0 1px 3px 0 rgba(0,0,0,0.08)
- 아이콘 좌상단 #0C8C5E (SVG)
- 제목 Inter 20px weight 600
- 본문 16px color #4A5565
```

#### Badge

```
Mintlify 스타일 배지를 만들어줘.
- font Inter 12px weight 500
- bg rgba(12,140,94,0.1), color #0C8C5E, radius 9999px
- padding 2px 8px
```

### Iteration Guide

- **색상** brand `#0C8C5E`을 면적으로 쓰지 말 것 — point accent.
- **폰트** Inter + Geist Mono 고정 (Vercel 계열).
- **다크 mode** `.dark` class로 `--bg/--fg/--color-brand` swap.
- **footer gradient** multi-stop fade가 Mintlify 시그니처 — 복제 시 유지.
- **docs 중심** prose max 720px 지키기.

---

## 18. DO / DON'T

### ✅ DO

- light 기본 `#FFFFFF` · 텍스트 `#231F20` warm black.
- 브랜드 mint green `#0C8C5E`은 link/CTA/code-token-color에만.
- Inter weight `400/600/900` 3단 계단.
- 카드 radius `12px`, 버튼 `6px`.
- footer-cta-gradient 다중 stop fade로 섹션 경계 부드럽게.
- 다크 모드는 `--color-brand: #18E299` bright mint로 swap.

### ❌ DON'T

- mint green을 넓은 배경에 쓰지 말 것 — Duolingo 됨.
- weight `800–900`을 본문에 쓰지 말 것 — display/hero 전용.
- monochrome 엄격히 가지 말 것 — warm `#F7F7F7` + paper `#F1EFED` 레이어.
- 단일 stop linear-gradient 금지 — Mintlify는 multi-stop fade.
- prose max-width `1024px` 이상 금지.
