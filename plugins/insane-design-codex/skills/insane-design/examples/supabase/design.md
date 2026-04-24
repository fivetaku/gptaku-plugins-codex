---
schema_version: 3.1
slug: supabase
service_name: Supabase
site_url: https://supabase.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#3ECF8E"
primary_font: Ubuntu
font_weight_normal: 400
token_prefix: "Tailwind tokens + Supabase custom (.ch-*, semantic --color-* on dark base)"

bold_direction: "Developer Brutalism"
aesthetic_category: "Developer Brutalism"
signature_element: code_first_terminal
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Supabase (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Supabase의 마케팅 사이트는 `#1C1C1C` near-black 캔버스 위에 **Supabase green `#3ECF8E`** 단 하나의 액센트로 승부하는 **developer-brutalist minimal**이다. Firebase를 대체하는 오픈소스 BaaS라는 포지셔닝이 그대로 시각화되어 — 화려하지 않고, 개발자에게 필요한 것만 명확하게, 터미널 / 코드 블록 / API 스키마를 hero 자리에 둔다. Figma나 Vercel처럼 포장에 신경쓰지 않고, 긱긱한 green/black 조합 하나로 "우리는 infra다"를 말한다.

컬러 시스템은 Tailwind 기반이지만 Supabase 고유의 **dark-first** 의미 layer를 얹었다. 지배색은 `#1C1C1C`(bg-dash), `#191919`(bg-1), `#1E1E1E`(bg-2), `#262626`(border) — 검정 6-8단 계단의 very-dark 스펙트럼이다. 액센트는 `#3ECF8E` 외에 거의 사용되지 않고, Vercel blue `#0070F3`이 link의 일부로 등장할 뿐. `code-hike` 터미널 chrome을 위한 macOS traffic-light 3색(`#ED6B60/#F5BE4F/#62C554`)은 hero에서 오히려 시그니처 역할을 한다.

타이포그래피는 흥미롭게도 **Ubuntu**(오픈소스 시스템 폰트)를 본문에 쓰고, mono로는 **Office Code Pro** + Courier로 터미널 느낌을 살린다. 이는 "우리는 VSCode / DevTools / Linux 생태계"라는 메시지다. weight 200-900 전 범위를 사용하지만 실사용은 400(body) / 500(emphasis) / 600(small heading) / 700(h2-h3) / 800(display). h1은 `clamp(32px, 6vw, 72px)` 스타일의 responsive impact을 준다.

레이아웃은 Next.js + Tailwind 조합이고 `.ch-frame-*` 같은 code-hike 접두어 컴포넌트가 hero의 핵심이다. Terminal chrome card를 centered하게 배치하고 그 위에 실제 SQL/JS 코드를 syntax-highlight로 보여주는 게 Supabase의 signature move — 이게 `pill_cta_impact`가 아니라 `code_first_terminal` 시그니처의 본질이다.

인터랙션은 절제되어 있다. 전체적인 모션 스케일은 Linear와 비슷하지만, Supabase는 micro-interaction에서 scale 대신 `border + glow` 기반 hover를 선호한다. 예: 카드 hover에서 `border-color: rgba(62,207,142,0.4)` + 은은한 green glow.

### Key Characteristics

- Supabase green `#3ECF8E` single-accent
- Dark stack 6단: `#191919` · `#1C1C1C` · `#1E1E1E` · `#262626` · `#3C3C3C` · `#F0F0F0`(inverse)
- Ubuntu body + Office Code Pro mono (개발자 코드 존중)
- code-hike 터미널 chrome (`.ch-frame-*`, traffic-light dots)
- Vercel blue `#0070F3` link accent (subtle)
- weight 200-900 전 범위 (실사용 400/500/600/700/800)
- Hover는 border+glow (scale 없음)
- Hero에 실제 SQL/JS 코드 블록 (marketing copy 대신)

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Developer Brutalism — 화려함 없이 코드블록을 hero에 두는 개발자 중심 미학
> **Aesthetic Category**: Developer Brutalism
> **Signature Element**: code_first_terminal — hero에 syntax-highlighted SQL/JS + macOS chrome
> **Code Complexity**: medium — Tailwind + code-hike + 커스텀 dark layer

---

## 01. Quick Start

```css
:root {
  --supabase-green: #3ECF8E;
  --supabase-green-dark: #24B47E;
  --bg-dash: #1C1C1C;
  --bg-1: #191919;
  --bg-2: #1E1E1E;
  --border: #262626;
  --fg: #EDEDED;
  --fg-muted: #A0A0A0;
  --link-blue: #0070F3;
}
body { background: var(--bg-dash); color: var(--fg); }
```

```css
body {
  font-family: "Ubuntu", "Droid Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  font-size: 16px;
}
code, pre, .mono {
  font-family: "Office Code Pro", "Courier New", monospace;
}
```

```css
/* Signature terminal chrome */
.ch-frame {
  background: #1E1E1E;
  border: 1px solid #262626;
  border-radius: 8px;
}
.ch-frame-dots { display:flex; gap:8px; padding:12px; }
.ch-frame-button-left  { background:#ED6B60; border-color:#CE5347; }
.ch-frame-button-middle{ background:#F5BE4F; border-color:#D6A243; }
.ch-frame-button-right { background:#62C554; border-color:#58A942; }
```

**절대 하지 말 것 하나**: Supabase green을 버튼 배경으로 꽉 채워 쓰지 마라 — Supabase는 초록을 `border-color` + `text-color` + `outline glow`로만 쓴다. solid green fill을 하면 Vercel이나 Cal.com 느낌이 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://supabase.com` |
| Fetched | 2026-04-20 |
| HTML / CSS | Next.js + Tailwind + code-hike |
| Vars total | 788 (resolved 598 · 76%) |
| Signature lib | code-hike (`.ch-frame-*`, `.ch-browser-*`) |

---

## 03. Tech Stack

- **Framework**: Next.js (Vercel hosting)
- **CSS**: Tailwind + custom dark layer + code-hike
- **Typography**: Ubuntu (body) / Office Code Pro (mono)
- **Theme**: dark default, light available
- **Signature**: code-hike terminal chrome at hero
- **Link accent**: Vercel blue `#0070F3`

---

## 04. Font Stack

- **Body/UI**: `Ubuntu`, `Droid Sans`, -apple-system, BlinkMacSystemFont, Segoe WPC, Segoe UI, sans-serif
- **Mono**: `Office Code Pro`, `Courier New`, Courier, monospace
- **Fallback**: system-ui
- **Weights**: 200 · 300 · 400 · 500 · 600 · 700 · 800 · 900 (전 범위 로드, 실사용 400/500/600/700/800)

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `caption` | 12px | 400 | 1.5 | meta / tag |
| `small` | 14px | 400 | 1.5 | small body |
| `body` | 16px | 400 | 1.6 | default |
| `lead` | 18px | 400 | 1.5 | lead paragraph |
| `h3` | 20-24px | 600 | 1.3 | subsection |
| `h2` | 28-36px | 700 | 1.2 | section |
| `h1` | clamp(32px, 6vw, 72px) | 800 | 1.1 | hero |
| `display` | 72-96px | 800 | 1.05 | landing headline |

---

## 06. Colors

> Dark-first 6단 + Supabase green single-accent + Vercel blue link.

### Signature

| Name | Hex | Use |
|---|---|---|
| supabase-green | `#3ECF8E` | single accent (border/text/glow) |
| green-dark | `#24B47E` | hover · focus deeper |
| green-ring | `#1A7A4C` (α=a1) | focus ring (from selector) |

### Dark Stack (neutral)

| Name | Hex | Use |
|---|---|---|
| bg-base | `#1C1C1C` | main background |
| bg-1 | `#191919` | section accent |
| bg-2 | `#1E1E1E` | card / raised |
| bg-3 | `#121516` | deep card |
| border | `#262626` | hairline |
| border-alt | `#1F1F1F` / `#14191B` | subtle inner |
| fg | `#EDEDED` | text primary |
| fg-muted | `#999999` | text secondary |
| neutral-inverse | `#F0F0F0` | light-mode mirror |
| ghost-white | `#FFFFFF` | buttons reverse |

### Link / Accent Pair

| Name | Hex | Use |
|---|---|---|
| vercel-blue | `#0070F3` | link primary |
| deep-ink | `#030A0C` | black text overlay |

### code-hike Terminal Traffic Lights

| Name | Hex | Use |
|---|---|---|
| dot-red | `#ED6B60` (border `#CE5347`) | close |
| dot-amber | `#F5BE4F` (border `#D6A243`) | minimize |
| dot-green | `#62C554` (border `#58A942`) | maximize |

### Translucent Overlays (from CSS)

| Name | Hex | Use |
|---|---|---|
| `#1C1C1C40` | 25% | subtle dim |
| `#1C1C1C80` | 50% | modal scrim |
| `#1C1C1C99` | 60% | dark overlay |
| `#DFFFF1` | — | green glow bg (very pale) |
| `#F4FFFA90` | — | green bg wash |

---

## 07. Spacing

> Tailwind spacing (4px unit). Section padding 64-128px.

| Token | Value |
|---|---|
| `1` | 4px |
| `2` | 8px |
| `3` | 12px |
| `4` | 16px |
| `6` | 24px |
| `8` | 32px |
| `12` | 48px |
| `16` | 64px |
| `24` | 96px |
| `32` | 128px |

---

## 08. Radius

| Name | Value | Use |
|---|---|---|
| `rounded-sm` | 2px | small control |
| `rounded-md` | 6px | input |
| `rounded-lg` | 8px | card / ch-frame |
| `rounded-xl` | 12px | hero card |
| `rounded-full` | 9999px | avatar / pill |

---

## 09. Shadows

| Name | Value | Use |
|---|---|---|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.5)` | subtle raise |
| `shadow-glow-green` | `0 0 20px rgba(62,207,142,0.25)` | signature green aura |
| `shadow-lg` | `0 24px 48px rgba(0,0,0,0.6)` | modal on dark |

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| hover transition | `.15-.2s ease` | border / color |
| link hover | instant color swap | Vercel blue |
| terminal reveal | slide-in + fade | hero code block |
| focus ring | green outline 2px | CTA / input |

---

## 11. Layout Patterns

### Grid
- Max-width: 1280px (content) / 1440px (hero)
- Gutter: 24px
- Columns: 12 (Tailwind default)

### Hero — code_first signature
- Centered 1-column headline
- **code-hike terminal chrome** (`.ch-frame`) centered below
- Traffic-light dots + filename tab + syntax-highlighted SQL/JS
- Primary CTA: green outlined `Start your project` + secondary ghost

### Section Rhythm
- Padding: 96-128px
- Max-width: 1280px
- Alternating `#1C1C1C` / `#191919` for subtle rhythm

### Card
- Bg: `#1E1E1E`
- Border: 1px solid `#262626`
- Radius: 8-12px
- Hover: border → `#3ECF8E40`, subtle green glow

### Navigation
- Horizontal, 64-72px height
- Bg transparent on scroll-top, `#1C1C1CBF` with blur on scroll
- Mobile: hamburger + fullscreen

---

## 12. Responsive Behavior

| Name | Value |
|---|---|
| sm | 640px |
| md | 768px |
| lg | 1024px |
| xl | 1280px |
| 2xl | 1536px |

Mobile: hero 코드 블록 horizontal-scroll로 유지. Headline clamp 축소.

---

## 13. Components

### Terminal Chrome Card (시그니처)
**Spec**: bg `#1E1E1E` · border `#262626` · radius 8px · traffic-light 3dots + filename tab

```css
.ch-frame { background:#1E1E1E; border:1px solid #262626; border-radius:8px; }
.ch-frame-dot { width:12px; height:12px; border-radius:50%; }
.ch-frame-button-left  { background:#ED6B60; border:1px solid #CE5347; }
.ch-frame-button-middle{ background:#F5BE4F; border:1px solid #D6A243; }
.ch-frame-button-right { background:#62C554; border:1px solid #58A942; }
```

### Outlined CTA (Primary)
**Spec**: bg transparent · border 1px solid `#3ECF8E` · color `#3ECF8E` · radius 6px · hover bg `#3ECF8E1A`

```css
.btn-primary {
  background: transparent;
  border: 1px solid #3ECF8E;
  color: #3ECF8E;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 500;
  transition: all .15s ease;
}
.btn-primary:hover {
  background: rgba(62,207,142,0.1);
  box-shadow: 0 0 20px rgba(62,207,142,0.2);
}
```

### Card
**Spec**: bg `#1E1E1E` · border 1px solid `#262626` · radius 8px · hover border `#3ECF8E40`

```css
.card {
  background: #1E1E1E;
  border: 1px solid #262626;
  border-radius: 8px;
  padding: 20px;
  transition: border-color .15s, box-shadow .15s;
}
.card:hover {
  border-color: rgba(62,207,142,0.4);
  box-shadow: 0 0 32px rgba(62,207,142,0.08);
}
```

---

## 14. Content / Copy Voice

| Label | Rule |
|---|---|
| Tone | developer-to-developer, direct, technical |
| Headline | "Build in a weekend · Scale to millions" 류 · 5-8 단어 |
| CTA verb | "Start your project" / "View on GitHub" / "See the docs" |
| Hero proof | code 자체가 hero copy (marketing 문구 대신) |

---

## 15. Drop-in CSS

```css
:root {
  --supabase-green: #3ECF8E;
  --bg-base: #1C1C1C;
  --bg-1: #191919;
  --bg-2: #1E1E1E;
  --border: #262626;
  --fg: #EDEDED;
  --fg-muted: #999999;
  --link: #0070F3;
  --font-body: "Ubuntu","Droid Sans",-apple-system,sans-serif;
  --font-mono: "Office Code Pro","Courier New",monospace;
}
body { background: var(--bg-base); color: var(--fg); font-family: var(--font-body); }
a { color: var(--link); }
.btn-primary {
  background: transparent; border: 1px solid var(--supabase-green);
  color: var(--supabase-green); padding: 10px 20px; border-radius: 6px;
  transition: all .15s ease;
}
.btn-primary:hover { background: rgba(62,207,142,.1); box-shadow: 0 0 20px rgba(62,207,142,.2); }
```

---

## 16. Tailwind Config

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        'supabase-green': { DEFAULT:'#3ECF8E', dark:'#24B47E' },
        'bg-base': '#1C1C1C',
        'bg-1': '#191919',
        'bg-2': '#1E1E1E',
        border: { DEFAULT:'#262626' },
      },
      fontFamily: {
        sans: ['Ubuntu','Droid Sans','sans-serif'],
        mono: ['Office Code Pro','Courier New','monospace'],
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide

| Role | Token | Hex |
|---|---|---|
| Brand | `--supabase-green` | `#3ECF8E` |
| Bg base | `--bg-base` | `#1C1C1C` |
| Card | `--bg-2` | `#1E1E1E` |
| Border | `--border` | `#262626` |
| Text | `--fg` | `#EDEDED` |
| Text muted | `--fg-muted` | `#999999` |
| Link | `--link` | `#0070F3` |

**Prompts**:

- **Hero**: "Supabase hero: bg #1C1C1C, centered headline weight 800 clamp(32px,6vw,72px) color #EDEDED. Below: terminal chrome card (bg #1E1E1E, border 1px solid #262626, radius 8px) with 3 macOS traffic-light dots (#ED6B60/#F5BE4F/#62C554) + syntax-highlighted SQL."
- **CTA**: "Supabase CTA: transparent bg, 1px solid #3ECF8E border, #3ECF8E text, padding 10px 20px, radius 6px. Hover: bg rgba(62,207,142,0.1) + glow 0 0 20px rgba(62,207,142,0.2)."
- **Card**: "Supabase card: bg #1E1E1E, border 1px solid #262626, radius 8px. Hover: border rgba(62,207,142,0.4) + subtle green glow."

---

## 18. DO / DON'T

### DO
- ✅ Dark base `#1C1C1C` 고수 (`#0A0A0A` true black 아님)
- ✅ green `#3ECF8E`는 border / text / glow로만 쓴다
- ✅ Hero에 code block을 주인공으로 (marketing 문구 대신)
- ✅ Ubuntu + Office Code Pro 폰트 조합 유지
- ✅ traffic-light 3색 `#ED6B60/#F5BE4F/#62C554`로 terminal 분위기

### DON'T
- solid green fill 버튼 금지 — border/glow만
- `#000` true black 쓰지 말 것 — `#1C1C1C`가 signature
- sans-serif default로 system font만 쓰지 말 것 — Ubuntu 로드 필수
- hover에 scale(1.04) 쓰지 말 것 — Spotify 시그니처지 Supabase 아님
- Stripe purple / Vercel black 톤 섞지 말 것
