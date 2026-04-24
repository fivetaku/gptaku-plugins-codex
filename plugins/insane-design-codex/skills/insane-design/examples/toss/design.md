---
schema_version: 3.1
slug: toss
service_name: Toss (토스)
site_url: https://toss.im
fetched_at: 2026-04-20
default_theme: light
brand_color: "#3182F6"
primary_font: Toss Product Sans
font_weight_normal: 400
token_prefix: "Toss Product Sans + Basier Square + Tossface emoji + SD Gothic Neo"

bold_direction: "Korean Fintech Friendly"
aesthetic_category: "Soft-Fintech Minimal"
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Toss (토스)

---

## 00. Visual Theme & Atmosphere

토스(`toss.im`)는 한국 핀테크가 고민하는 "신뢰는 딱딱하지 않게 · 친근함은 가볍지 않게"라는 이중 긴장을 **Toss Blue `#3182F6`** 하나의 컬러 시스템과 **Toss Product Sans** 자체 폰트로 풀어낸 **Soft-Fintech Minimal**이다. 넓은 흰 여백 + big rounded card + 큰 headline + 핵심 CTA 하나 — 금융 UI라기보다 Airbnb/Spotify 류의 B2C lifestyle 앱에 가까운 톤으로 마케팅한다.

컬러 시스템은 Toss Blue `#3182F6`을 중심으로 **Blue ramp 5-6단**(#E8F3FF · #90C2FF · #3182F6 · #2272EB · #1B64DA · #052A56)을 풀로 구축하고, Grey-Mauve 계열 **Greyscale 8-9단**(`#F9FAFB` · `#F2F4F6` · `#D1D6DB` · `#B0B8C1` · `#8B95A1` · `#6B7684` · `#4E5968` · `#333D4B` · `#191F28`)으로 텍스트/보더 계단을 만든다. 상태 컬러는 Red `#F04452`와 그 ramp(`#FFD4D6` · `#FEAFB4` · `#FB8890` · `#F04452` · `#E42939` · `#D22030`)로 error/destructive 표시. 이 둘 외에는 거의 색을 쓰지 않는 엄격한 2-color 금융 규율.

타이포그래피는 **Toss Product Sans**(자체 개발 폰트) 768회 압도적 사용 — 사실상 모든 텍스트가 이 폰트. 여기에 **Tossface**가 emoji/pictogram으로 별도 로드(20회), **Basier Square**는 영문 타이틀 보조, **SD Gothic Neo**는 한글 fallback. weight 300-950 전 범위를 균형 있게 사용 (400 default, 500-700 headings). `font-family: initial!important` 사용도 나타나는데, 이는 특정 widget에서 user agent default로 되돌리는 escape hatch다.

레이아웃은 Toss UI 시스템 기반이고, 모바일-퍼스트 CTA 박스 + large rounded card가 시그니처. section padding 크게 잡고 (80-120px+), headline을 40-72px로 과감하게. 화이트 바닥 + 하나의 Toss Blue 액센트 + 큰 둥근 카드에 그림자 소프트.

인터랙션은 매우 유쾌하다. button hover에 scale transform + subtle shadow elevation, 페이지 전환 fade + slide. Mobile motion이 그대로 웹에 이식되어 UI 전체가 '앱 같다'.

### Key Characteristics

- Toss Blue `#3182F6` single-primary
- Blue ramp 6단 (tint → dark)
- Grey-Mauve ramp 8단 (`#F9FAFB`부터 `#191F28`까지)
- Red state ramp 7단 (error/destructive)
- Toss Product Sans 압도적 (768회)
- Tossface (emoji/pictogram 전용 폰트)
- 2-color discipline (Blue + Grey + Red state)
- Large rounded card · soft shadow
- 앱스러운 motion (scale + fade + slide)

### BOLD Direction Summary

> **BOLD Direction**: Korean Fintech Friendly — 친근하지만 신뢰감 있는 핀테크 톤
> **Aesthetic Category**: Soft-Fintech Minimal
> **Signature Element**: hero_impact — 40-72px headline + 큰 rounded card + Toss Blue CTA 하나
> **Code Complexity**: medium — Toss UI + 자체 폰트 + ramp systems

---

## 01. Quick Start

```css
:root {
  --toss-blue: #3182F6;
  --toss-blue-hover: #1B64DA;
  --toss-blue-soft: #E8F3FF;
  --bg: #FFFFFF;
  --fg: #191F28;
  --fg-muted: #6B7684;
  --border: #E5E8EB;
  --radius-card: 20px;
  --radius-cta: 12px;
}
```

```css
body {
  font-family: "Toss Product Sans", Tossface,
               -apple-system, BlinkMacSystemFont,
               "Apple SD Gothic Neo", "Noto Sans KR",
               Roboto, "Helvetica Neue", sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #191F28;
  background: #FFFFFF;
}
```

```css
.btn-toss {
  background: #3182F6;
  color: #FFFFFF;
  padding: 14px 28px;
  border-radius: 12px;
  font-weight: 700;
  transition: background .15s, transform .1s;
}
.btn-toss:hover { background: #1B64DA; transform: translateY(-1px); }
.btn-toss:active { background: #052A56; transform: translateY(0); }
```

**절대 하지 말 것 하나**: 글자색을 `#000000`으로 두지 마라 — 토스는 `#191F28` (조금 푸른 near-black)을 쓴다. `#000`을 쓰면 딱딱하고 '금융 UI'스러워진다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://toss.im` |
| Fetched | 2026-04-20 |
| Framework | Next.js (추정) + Toss UI |
| Font usage | Toss Product Sans 768회 · Tossface 20회 |
| Theme | light (default) |

---

## 03. Tech Stack

- **Framework**: Next.js + Toss UI (자체 디자인 시스템)
- **Typography**: Toss Product Sans (자체 개발 · 유료/자체 호스팅)
- **Emoji font**: Tossface (pictogram 대체)
- **i18n**: SD Gothic Neo / Noto Sans KR / SF Pro KR
- **Theme**: light default

---

## 04. Font Stack

- **Primary**: `Toss Product Sans` (자체 폰트, 768회 사용)
- **Emoji/Pictogram**: `Tossface` (전용 이모지 폰트)
- **English Title**: `Basier Square` (보조 영문)
- **Korean Fallback**: `Apple SD Gothic Neo`, `Noto Sans KR`, `SF Pro KR`
- **Mono**: `SFMono-Regular`, `Menlo`, `Consolas`, `Monaco`, `Andale Mono`, `Ubuntu Mono`, monospace
- **System fallback**: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif
- **Weights used**: 300 · 400 · 500 · 600 · 700 · 800 · 900 · 950 전 범위

---

## 05. Typography Scale

| Token | Size | Weight | lh | Use |
|---|---|---|---|---|
| caption | 12px | 400 | 1.5 | meta |
| small | 14px | 400 | 1.5 | small body |
| body | 16px | 400 | 1.5 | default |
| lead | 18-20px | 500 | 1.5 | lead paragraph |
| h3 | 22-26px | 600 | 1.3 | subsection |
| h2 | 32-40px | 700 | 1.2 | section |
| h1 | 48-56px | 700 | 1.1 | hero |
| display | 64-72px | 800 | 1.05 | landing impact |

---

## 06. Colors

### Signature Blue (primary · 6 steps)

| Name | Hex | Use |
|---|---|---|
| blue-50 | `#E8F3FF` | button soft bg |
| blue-100 | `#C9E2FF` | chip bg |
| blue-200 | `#90C2FF` | soft border |
| blue-500 (brand) | `#3182F6` | **Toss Blue primary CTA** |
| blue-600 | `#2272EB` | hover |
| blue-700 | `#1B64DA` | active |
| blue-900 | `#052A56` | deepest / press |

### Grey-Mauve (neutral · 9 steps)

| Name | Hex | Use |
|---|---|---|
| grey-50 | `#F9FAFB` | bg alt |
| grey-100 | `#F2F4F6` | section bg / divider |
| grey-200 | `#D1D6DB` | border |
| grey-300 | `#B0B8C1` | disabled |
| grey-400 | `#8B95A1` | placeholder |
| grey-500 | `#6B7684` | **text muted** |
| grey-600 | `#4E5968` | text secondary |
| grey-700 | `#333D4B` | heading-muted |
| grey-900 | `#191F28` | **text primary** (not #000!) |

### Red State (error/destructive · 7 steps)

| Name | Hex | Use |
|---|---|---|
| red-50 | `#FFEEEE` | error bg |
| red-100 | `#FFD4D6` | error chip |
| red-200 | `#FEAFB4` | soft |
| red-300 | `#FB8890` | hover light |
| red-500 (brand-red) | `#F04452` | error primary |
| red-600 | `#E42939` | error hover |
| red-700 | `#D22030` | error active |

---

## 07. Spacing

Toss UI 4px base scale. Section padding 80-120px.

| Token | Value | Use |
|---|---|---|
| `1` | 4px | inline |
| `2` | 8px | icon gap |
| `3` | 12px | button padding-y |
| `4` | 16px | default |
| `6` | 24px | card padding |
| `8` | 32px | section inner |
| `12` | 48px | hero padding-y |
| `20` | 80px | section vertical |
| `30` | 120px | large section / hero |

---

## 08. Radius

| Name | Value | Use |
|---|---|---|
| `radius-sm` | 6px | chip |
| `radius-md` | 8px | input |
| `radius-cta` | 12px | button |
| `radius-lg` | 16px | card small |
| `radius-xl` | 20px | **card standard (Toss 시그니처)** |
| `radius-2xl` | 28px | hero card |
| `radius-full` | 9999px | avatar / tag |

---

## 09. Shadows

Toss의 시그니처는 **soft shadow**. 대비 강하지 않게.

| Name | Value | Use |
|---|---|---|
| shadow-sm | `0 1px 2px rgba(0,0,0,0.04)` | subtle |
| shadow-md | `0 4px 16px rgba(0,0,0,0.06)` | card default |
| shadow-lg | `0 12px 32px rgba(0,0,0,0.08)` | card hover / modal |
| shadow-blue | `0 8px 24px rgba(49,130,246,0.25)` | CTA emphasis |

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| hover transition | `.15s ease` | button |
| button press | `scale(0.98)` on active | tap feedback |
| card hover | `translateY(-2px)` + shadow | elevate |
| page transition | `.3s fade + slide` | 앱스러움 |

---

## 11. Layout Patterns

### Hero — hero_impact
- bg `#FFFFFF` 또는 `#F9FAFB`
- headline 48-72px weight 700-800
- 한 문장 서브카피 (`#6B7684`)
- 단일 Toss Blue CTA (더 큰 12px 패딩)
- 앱 스크린샷 또는 큰 rounded card

### Section Rhythm
- padding 80-120px vertical
- max-width 1200px
- 흰 + `#F9FAFB` alternation

### Card (시그니처)
- bg `#FFFFFF`
- radius **20px** (standard) / 28px (hero)
- shadow soft
- padding 24-32px
- hover: translateY(-2px) + shadow-lg

### Navigation
- height 64-72px
- bg `#FFFFFF` solid 또는 transparent
- Toss Product Sans 500 weight
- mobile: hamburger + fullscreen overlay

---

## 12. Responsive

| Name | Value |
|---|---|
| sm | 640px (mobile) |
| md | 768px (tablet) |
| lg | 1024px (desktop) |
| xl | 1280px (wide) |

Toss는 모바일-first 설계라 mobile view에서 그대로 자연스럽게 stack.

---

## 13. Components

### Toss Blue CTA (Primary)
```css
.btn-toss {
  background: #3182F6;
  color: #FFFFFF;
  padding: 14px 28px;
  border-radius: 12px;
  font-family: "Toss Product Sans", sans-serif;
  font-weight: 700;
  transition: background .15s ease, transform .1s ease;
}
.btn-toss:hover { background: #1B64DA; transform: translateY(-1px); }
.btn-toss:active { background: #052A56; transform: scale(.98); }
```

### Secondary Button (Ghost)
```css
.btn-toss-ghost {
  background: #F2F4F6;
  color: #333D4B;
  padding: 14px 28px;
  border-radius: 12px;
  font-weight: 600;
}
.btn-toss-ghost:hover { background: #D1D6DB; }
```

### Rounded Card (시그니처)
```css
.toss-card {
  background: #FFFFFF;
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  transition: transform .15s, box-shadow .15s;
}
.toss-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.08);
}
```

### Error State Chip
```css
.chip-error {
  background: #FFEEEE;
  color: #D22030;
  padding: 6px 12px;
  border-radius: 9999px;
  font-weight: 500;
}
```

---

## 14. Content / Copy Voice

| Label | Rule | Example |
|---|---|---|
| Tone | 친근한 존댓말 · 짧은 문장 | "금융을 쉽고 간편하게" |
| Headline | 10-15자 한국어 한 문장 | "송금, 투자, 대출까지" |
| Button copy | 2-5자 동사형 | "시작하기" · "확인" |
| Error | 부드러운 존댓말 | "잠시 후 다시 시도해주세요" |

---

## 15. Drop-in CSS

```css
:root {
  --toss-blue: #3182F6;
  --toss-blue-hover: #1B64DA;
  --toss-blue-active: #052A56;
  --toss-blue-soft: #E8F3FF;
  --grey-50: #F9FAFB;
  --grey-100: #F2F4F6;
  --grey-500: #6B7684;
  --grey-900: #191F28;
  --red: #F04452;
  --radius-card: 20px;
  --radius-cta: 12px;
  --font-body: "Toss Product Sans", Tossface, -apple-system, "Apple SD Gothic Neo", sans-serif;
}
body {
  font-family: var(--font-body);
  font-size: 16px; font-weight: 400;
  color: var(--grey-900);
  background: #FFFFFF;
}
.btn-toss {
  background: var(--toss-blue); color: #FFFFFF;
  padding: 14px 28px; border-radius: var(--radius-cta);
  font-weight: 700; transition: all .15s ease;
}
.btn-toss:hover { background: var(--toss-blue-hover); transform: translateY(-1px); }
.toss-card {
  background: #FFFFFF; border-radius: var(--radius-card);
  padding: 24px; box-shadow: 0 4px 16px rgba(0,0,0,.06);
}
```

---

## 16. Tailwind Config

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        toss: {
          blue: { 50:'#E8F3FF', 100:'#C9E2FF', 200:'#90C2FF', 500:'#3182F6', 600:'#2272EB', 700:'#1B64DA', 900:'#052A56' },
          grey: { 50:'#F9FAFB', 100:'#F2F4F6', 200:'#D1D6DB', 300:'#B0B8C1', 400:'#8B95A1', 500:'#6B7684', 600:'#4E5968', 700:'#333D4B', 900:'#191F28' },
          red: { 50:'#FFEEEE', 100:'#FFD4D6', 500:'#F04452', 600:'#E42939', 700:'#D22030' },
        },
      },
      fontFamily: {
        sans: ['"Toss Product Sans"','Tossface','-apple-system','"Apple SD Gothic Neo"','sans-serif'],
      },
      borderRadius: {
        card: '20px',
        cta: '12px',
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide

| Role | Token | Hex |
|---|---|---|
| Brand | `--toss-blue` | `#3182F6` |
| Bg | `--bg` | `#FFFFFF` |
| Bg alt | `--grey-50` | `#F9FAFB` |
| Text primary | `--grey-900` | `#191F28` |
| Text muted | `--grey-500` | `#6B7684` |
| Border | `--grey-200` | `#D1D6DB` |
| Error | `--red` | `#F04452` |

**Prompts**:
- **Hero**: "Toss style hero: bg #FFFFFF, headline 56px weight 700 Toss Product Sans color #191F28. Subheading 18px #6B7684. Single CTA: bg #3182F6 padding 14px 28px radius 12px color white weight 700. Big rounded card radius 28px with soft shadow below."
- **Card**: "Toss rounded card: bg #FFFFFF, radius 20px, padding 24px, shadow 0 4px 16px rgba(0,0,0,.06). Hover translateY(-2px) + shadow-lg."
- **CTA**: "Toss Blue CTA: bg #3182F6, color white, padding 14px 28px, radius 12px, weight 700. Hover bg #1B64DA + translateY(-1px). Active scale(.98)."
- **Error**: "Toss error: bg #FFEEEE, color #D22030, padding 6px 12px, radius 9999 pill."

---

## 18. DO / DON'T

### DO
- ✅ Toss Blue `#3182F6` 한 컬러만 primary로
- ✅ 텍스트는 `#191F28` (not `#000`)
- ✅ 카드 radius **20px** 시그니처 유지
- ✅ Toss Product Sans + Tossface 조합
- ✅ soft shadow (rgba 알파 0.04-0.08)
- ✅ hover에 translateY(-1~-2px) + shadow 증가

### DON'T
- 텍스트를 `#000000` 또는 black으로 쓰지 말 것
- radius를 `4px` `8px`로 작게 쓰지 말 것 — 16-20px이 Toss
- Blue를 진하게 `#1A57D2` 같이 어둡게 쓰지 말 것 — `#3182F6`이 정답
- Tossface 대신 일반 emoji 쓰지 말 것 — 아이콘 전용 폰트로 렌더
- shadow를 `rgba(0,0,0,0.2)` 진하게 쓰지 말 것 — 소프트가 시그니처
- Grey-Mauve ramp를 빠뜨리고 pure-grey `#EEE` 쓰지 말 것 — mauve 끼가 Toss 포인트
