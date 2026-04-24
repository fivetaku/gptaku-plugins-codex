---
schema_version: 3.1
slug: tailwindcss
service_name: Tailwind CSS
site_url: https://tailwindcss.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#625FFF"
primary_font: Inter
font_weight_normal: 400
token_prefix: "Tailwind utility + CSS custom properties (--font-inter, --font-plex-mono)"

bold_direction: "Code-First Playful"
aesthetic_category: "Utility Brutalism"
signature_element: utility_class_hero
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Tailwind CSS (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Tailwind CSS의 공식 사이트(`tailwindcss.com`)는 본인의 철학 그 자체를 시각화한 **Utility Brutalism** — 페이지가 곧 '튜토리얼이자 라이브 데모'다. dark base `#030712`(slate-950) 위에 **iris/purple `#625FFF`** primary + teal `#00B7D7` secondary 조합으로 시그니처 그라데이션을 만들고, 실제 `class="flex items-center gap-x-4"` 유틸리티 문자열을 hero copy로 쓰는 과감한 개발자 직접 화법.

컬러 시스템은 Tailwind v4.x 공식 팔레트 전체를 사용한다 — 즉 slate 50-950, indigo, sky, emerald, rose 등 수백 개 토큰이 모두 "자기 본사"에 살고 있다. 하지만 마케팅 axis는 좁다: `#625FFF` iris (CTA primary) + `#00B7D7` teal (CTA secondary / accent) + `#3080FF` blue (link) + `#00A5EF` cyan-bright (hero orb) + slate neutrals. frequency candidates에 semi-transparent overlays(`#FFFFFF1A`, `#0307120D`)가 대량 등장하는 이유는 glass-morphism 실험 + dark/light/system 3-mode토글 때문이다.

타이포그래피는 Tailwind 자체 브랜드 폰트 **Inter**(var `--font-inter`)를 body로, **IBM Plex Mono**(`--font-plex-mono`)를 code block과 utility 클래스 문자열 expose 용으로 병행. Ubuntu Mono, Source Sans Pro도 대체 스택에 포함되어 있다. weight는 100/400/500/600/bold 중심 — display에 600을 즐겨 쓴다 (700 heavy가 아니라 600 mid-heavy).

레이아웃은 Tailwind v4 CSS-first 접근의 실례. group/navitem 같은 container-query + variant 조합이 주를 이루고, `.DocSearch-*` (Algolia DocSearch) 컴포넌트가 검색 UI로 통합되어 있다. Hero는 거의 항상 **glowing purple orb** + **animated code/class demo** + **oversized utility-string headline** 구조.

인터랙션은 Tailwind답게 utility class 기반: `group-hover`, `data-[state=...]`, `:where(.dark, .dark *)` pattern이 실제 source에 그대로 드러난다. dark/light/system 3-mode가 `.dark` + `.system` class로 스위칭되고, 각 scope에서 색상이 완전히 다른 ramp를 탄다.

### Key Characteristics

- Iris primary `#625FFF` + Teal `#00B7D7` signature combo
- dark-first `#030712` slate-950 base
- Tailwind 공식 palette 전체 접근 (slate/indigo/sky/rose)
- Inter + IBM Plex Mono (utility class expose용 mono 강조)
- `.dark` + `.system` + `.light` 3-mode 토글
- glassmorphism overlays (`#FFFFFF1A`, `#0307120D`)
- Algolia DocSearch 통합 컴포넌트 (`.DocSearch-*`)
- Hero에 utility class string을 copy로 직접 노출
- weight 600 mid-heavy (700 과감한 heavy 회피)

### BOLD Direction Summary

> **BOLD Direction**: Utility Brutalism — utility class 문자열을 hero copy로 직접 노출하는 개발자 직접 화법
> **Aesthetic Category**: Code-First Playful
> **Signature Element**: utility_class_hero — 실제 `class="..."` 문자열 + purple/teal glow orb
> **Code Complexity**: high — Tailwind v4 container queries + variants + 3-mode theme

---

## 01. Quick Start

```css
:root {
  --iris: #625FFF;
  --teal: #00B7D7;
  --cyan-glow: #00A5EF;
  --blue: #3080FF;
  --bg-base: #030712;
  --bg-elev: #111827;
  --fg: #F8FAFC;
  --fg-muted: #94A3B8;
  --border: #1E293B;
}
```

```css
body {
  font-family: var(--font-inter, "Inter"), system-ui, sans-serif;
  font-weight: 400;
}
code, pre, .utility-string {
  font-family: var(--font-plex-mono, "IBM Plex Mono"), monospace;
}
```

```css
/* Signature glow-CTA */
.btn-iris {
  background: linear-gradient(180deg, #625FFF 0%, #5149E8 100%);
  color: #FFFFFF;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 8px 32px rgba(98,95,255,.4),
              inset 0 1px 0 rgba(255,255,255,.2);
  transition: all .15s ease;
}
.btn-iris:hover { box-shadow: 0 12px 40px rgba(98,95,255,.6); }
```

**절대 하지 말 것 하나**: 유틸리티 클래스 문자열을 hero에 노출하지 않고 평범한 marketing copy만 쓰면 Tailwind가 아니다. 반드시 `class="flex items-center gap-x-4 rounded-full bg-white/5 p-4 shadow-md..."` 같은 live code snippet이 hero에 있어야 한다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://tailwindcss.com` |
| Fetched | 2026-04-20 |
| Framework | Next.js + Tailwind CSS v4 |
| Hosting | Vercel |
| Search | Algolia DocSearch integration |
| Theme | dark (default) / light / system — 3-way |

---

## 03. Tech Stack

- **Framework**: Next.js (Vercel)
- **CSS**: Tailwind CSS v4 (self-host)
- **Typography**: Inter + IBM Plex Mono (CSS variables)
- **Theme mode**: dark / light / system toggle
- **Search**: Algolia DocSearch
- **Container queries**: `@container` + `container-type`
- **Variants**: `data-*`, `:where(.dark, .dark *)`, `group-hover/navitem`

---

## 04. Font Stack

- **Body/UI**: `Inter`, Inter Fallback, system-ui, sans-serif (via `--font-inter`)
- **Mono**: `IBM Plex Mono` (via `--font-plex-mono`), `Ubuntu Mono` 대체
- **Secondary sans**: `Source Sans Pro` (var `--font-source-sans-pro`)
- **Weights**: 100 · 400 · 500 · 600 · bold(700)

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `text-xs` | 12px | 400 | 1.5 | meta |
| `text-sm` | 14px | 400 | 1.5 | small |
| `text-base` | 16px | 400 | 1.6 | body |
| `text-lg` | 18px | 500 | 1.5 | lead |
| `text-xl` | 20px | 500 | 1.4 | subsection |
| `text-2xl` | 24px | 600 | 1.3 | h3 |
| `text-3xl` | 30px | 600 | 1.25 | h2 |
| `text-4xl` | 36px | 600 | 1.15 | large h2 |
| `text-5xl` | 48px | 600 | 1.1 | h1 |
| `text-6xl` | 60px | 600 | 1.05 | hero impact |
| `text-7xl` | 72px | 600 | 1.0 | mega hero |

---

## 06. Colors

### Signature

| Name | Hex | Use |
|---|---|---|
| iris | `#625FFF` | primary CTA · brand |
| teal | `#00B7D7` | secondary CTA · accent |
| cyan-bright | `#00A5EF` | hero orb glow |
| blue | `#3080FF` | link primary |
| blue-alt | `#3080FF80` (50% α) | link soft |

### Dark Stack

| Name | Hex | Use |
|---|---|---|
| bg-base | `#030712` | body bg (slate-950) |
| bg-elev | `#0F172A` | card (slate-900) |
| bg-elev-2 | `#111827` | raised (gray-900) |
| border | `#1E293B` | hairline (slate-800) |
| border-soft | `#E5E7EB0D` | dark mode subtle |
| fg | `#F8FAFC` | text primary (slate-50) |
| fg-muted | `#94A3B8` | text muted (slate-400) |
| fg-subtle | `#71717A` | text subtle (zinc-500) |
| inverse-bg | `#FFFFFF` | light mode body |

### Glass / Overlay (semi-transparent, dark scope)

| Hex | Use |
|---|---|
| `#FFFFFF1A` (10% α) | surface glass |
| `#FFFFFF0D` (5% α) | border glass |
| `#FFFFFF33` (20% α) | divider glass |
| `#FFFFFF80` (50% α) | overlay strong |
| `#0000001A` | light scope divider |
| `#0307120D` | light mode soft border |
| `#03071280` | dark scrim 50% |

### Search UI (Algolia)

| Name | Hex | Use |
|---|---|---|
| docsearch-stroke | `#71717A` | hit action icon |
| docsearch-fav-bg | `#3641534D` (α) | favorite button bg |

---

## 07. Spacing

Standard Tailwind scale:

| Token | Value |
|---|---|
| `px` | 1px |
| `0.5` | 2px |
| `1` | 4px |
| `2` | 8px |
| `3` | 12px |
| `4` | 16px |
| `6` | 24px |
| `8` | 32px |
| `12` | 48px |
| `16` | 64px |
| `20` | 80px |
| `24` | 96px |
| `32` | 128px |

---

## 08. Radius

| Token | Value |
|---|---|
| `rounded-sm` | 2px |
| `rounded` | 4px |
| `rounded-md` | 6px |
| `rounded-lg` | 8px |
| `rounded-xl` | 12px |
| `rounded-2xl` | 16px |
| `rounded-3xl` | 24px |
| `rounded-full` | 9999px |

---

## 09. Shadows

| Name | Value | Use |
|---|---|---|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.5)` | subtle |
| `shadow-glow-iris` | `0 8px 32px rgba(98,95,255,0.4)` | **signature CTA glow** |
| `shadow-glow-teal` | `0 8px 32px rgba(0,183,215,0.3)` | secondary glow |
| `shadow-inner-light` | `inset 0 1px 0 rgba(255,255,255,0.2)` | glass shine |

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| hover transition | `.15s ease` | default |
| theme switch | `.3s ease-in-out` | dark/light swap |
| group-hover | instant | utility class variant |
| nav underline | `.2s ease-out` | link indicator |

---

## 11. Layout Patterns

### Hero — utility_class_hero signature
- bg: slate-950 + radial purple glow orb
- headline: 60-72px weight 600
- **Live utility class demo** (syntax-highlighted `class="..."`)
- CTAs: iris gradient primary + teal ghost secondary

### Section Rhythm
- padding 96-128px
- max-width 1280px
- dark/light 모드 각기 다른 accent ramp

### Card
- bg: glass `rgba(255,255,255,0.03)` + backdrop-blur
- border: 1px solid `rgba(255,255,255,0.08)`
- radius: 16px

### Navigation
- height 64px
- bg transparent → backdrop-blur on scroll
- group/navitem hover → child bg-black/75

---

## 12. Responsive Behavior

| Name | Value |
|---|---|
| sm | 640px |
| md | 768px |
| lg | 1024px |
| xl | 1280px |
| 2xl | 1536px |

Container queries: `@container (width > 768px)` 사용.

---

## 13. Components

### Iris Gradient CTA (Primary)
**Spec**: gradient iris · inner light shine · strong purple glow

```css
.btn-iris {
  background: linear-gradient(180deg, #625FFF 0%, #5149E8 100%);
  color: #FFFFFF;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow:
    0 8px 32px rgba(98,95,255,.4),
    inset 0 1px 0 rgba(255,255,255,.2);
}
```

### Teal Ghost CTA (Secondary)
```css
.btn-teal-ghost {
  background: rgba(0,183,215,.1);
  color: #00B7D7;
  border: 1px solid rgba(0,183,215,.3);
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
}
```

### Glass Card
```css
.card-glass {
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 16px;
  backdrop-filter: blur(12px);
  padding: 24px;
}
```

### Utility String Display
```css
.utility-string {
  font-family: "IBM Plex Mono", monospace;
  font-size: 14px;
  background: rgba(255,255,255,.05);
  padding: 8px 12px;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,.1);
}
```

---

## 14. Content / Copy Voice

| Label | Rule |
|---|---|
| Tone | developer-to-developer, confident, playful |
| Hero copy | utility class string 직접 노출 |
| Headline | "Rapidly build modern websites..." 6-10 단어 |
| CTA verb | "Get started" / "Read the docs" / "Get Tailwind Plus" |

---

## 15. Drop-in CSS

```css
:root {
  --iris: #625FFF;
  --teal: #00B7D7;
  --blue: #3080FF;
  --bg-base: #030712;
  --bg-elev: #0F172A;
  --fg: #F8FAFC;
  --fg-muted: #94A3B8;
  --border: #1E293B;
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", monospace;
}
body {
  background: var(--bg-base);
  color: var(--fg);
  font-family: var(--font-sans);
}
.btn-iris {
  background: linear-gradient(180deg, #625FFF, #5149E8);
  color: #FFFFFF; padding: 12px 24px; border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 8px 32px rgba(98,95,255,.4), inset 0 1px 0 rgba(255,255,255,.2);
}
```

---

## 16. Tailwind Config

```js
module.exports = {
  darkMode: ['class', '.dark, .system'],
  theme: {
    extend: {
      colors: {
        iris: { DEFAULT:'#625FFF', dark:'#5149E8' },
        teal: { DEFAULT:'#00B7D7', glow:'#00A5EF' },
      },
      boxShadow: {
        'glow-iris': '0 8px 32px rgba(98,95,255,0.4), inset 0 1px 0 rgba(255,255,255,0.2)',
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide

| Role | Token | Hex |
|---|---|---|
| Primary CTA | `--iris` | `#625FFF` |
| Secondary | `--teal` | `#00B7D7` |
| Link | `--blue` | `#3080FF` |
| Bg base | `--bg-base` | `#030712` |
| Card | `--bg-elev` | `#0F172A` |
| Text | `--fg` | `#F8FAFC` |
| Border | `--border` | `#1E293B` |

**Prompts**:

- **Hero**: "Tailwind CSS style hero: bg #030712 + radial purple glow orb (from #625FFF fading). Headline 60px weight 600 color #F8FAFC. Below: syntax-highlighted `class=\"flex items-center...\"` utility string demo. Dual CTA: iris gradient primary + teal ghost secondary."
- **CTA**: "Iris gradient CTA: background linear-gradient(180deg, #625FFF, #5149E8), color white, padding 12px 24px, radius 8px, font-weight 600, box-shadow 0 8px 32px rgba(98,95,255,.4) + inset shine."
- **Card**: "Glass card: bg rgba(255,255,255,.03), border 1px solid rgba(255,255,255,.08), radius 16px, backdrop-blur 12px, padding 24px."

---

## 18. DO / DON'T

### DO
- ✅ iris `#625FFF` + teal `#00B7D7` 조합만 primary pair로
- ✅ Hero에 실제 utility class string 노출
- ✅ dark/light/system 3-mode 토글 구현
- ✅ IBM Plex Mono으로 utility string을 monospace로 강조
- ✅ glass overlays (`rgba(255,255,255,.03~.1)`) 사용

### DON'T
- 전통적 gradient (blue→pink)로 시그니처를 대체하지 말 것 — iris+teal이 시그니처
- body font를 Roboto/SFPro로 바꾸지 말 것 — Inter 필수
- hero에 utility class string 없이 평범한 marketing copy만 쓰지 말 것
- radius 9999 pill CTA 쓰지 말 것 — Tailwind은 radius 8이 default CTA
- weight 700 heavy 쓰지 말 것 — 600 mid-heavy가 Tailwind 느낌
