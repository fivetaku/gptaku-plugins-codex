---
schema_version: 3.1
slug: spotify
service_name: Spotify
site_url: https://spotify.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#1ED760"
primary_font: SpotifyMixUI
font_weight_normal: 400
token_prefix: "Encore (--encore-*) + semantic layer (--text-*, --background-*, --essential-*)"

bold_direction: "Vibrant Minimal"
aesthetic_category: "Vibrant Minimal"
signature_element: pill_cta_impact
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Spotify (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Spotify의 마케팅 사이트(`spotify.com`)는 검정 배경 위에 시그니처 `#1ED760` **Spotify green**이 pill-shape 버튼과 헤드라인 액센트에 그룹 지어져 튀어나오는 **Vibrant-on-Dark** 구성이다. 이 초록은 임의의 브랜드 컬러가 아니라 2015년 리브랜딩 이후 10년 넘게 고수해온 audio-first identity — true black (`#000`)과 극명하게 대비되며, 긴 음악 스트리밍 시간 동안 눈의 피로 없이 재생 버튼을 즉시 찾게 만들어주는 기능적 초록이다.

컬러 시스템은 **Encore design system**(Spotify 자체 디자인 시스템)의 semantic token 레이어로 움직인다. `--text-bright-accent` · `--essential-bright-accent` 같은 **의도 기반 이름**이 실제로는 context에 따라 `#1ED760`(default), `#107434`(dark text), `#FFFFFF`, `#159542` 등으로 리맵된다. Campaign별 테마 컬러(빨강 `#590810`, 갈색 `#491E00`, 깊은 녹색 `#073116`, 네이비 `#052A56`) 가 존재해서 각 landing 페이지마다 `--text-bright-accent`를 localize하는 구조다. 결과적으로 Spotify는 "하나의 초록"이 아니라 "초록을 중심으로 하는 6~8개 themeable variant"를 운영한다.

타이포그래피는 Spotify 전용 **SpotifyMixUI** + **SpotifyMixUITitle**(display) 2종을 main stack으로, CircularSp 계열을 다국어(Arab/Cyrl/Deva/Grek/Hebr) fallback으로 병렬 로드한다. weight는 400(body) · 700(bold) · 800(display) · 900(impact)의 4단 계단이고, `--encore-text-size-*` 시스템이 `0.625rem`(10px) → `6rem`(96px)까지 9단 계단을 제공한다. Headline은 `larger-3`~`larger-5` (48-96px)을 즐겨 쓰고 line-height를 1.0~1.1로 타이트하게 조여 impact를 만든다.

레이아웃은 Encore grid + SLDS 없는 자체 Svelte 컴포넌트(`.svelte-164a8y4` 해시)로 조립된다. Hero는 거의 예외없이 **full-bleed dark bg + centered headline + 초록 pill CTA** 구조다. `button-primary` 컴포넌트는 `border-radius: 9999px`의 완전한 pill, `:hover`에 `background-color:#3BE477 + transform:scale(1.04)` — scale 94% 상태에서 4% pop이 Spotify 시그니처 인터랙션이다. `:active`에서는 `#1ABC54`로 살짝 어두워지며 finger press 감각을 준다.

Radius는 pill(9999) 외에도 `--encore-radius-*` 토큰이 있지만 실제 markup에서는 "기본 8px card · 16px modal · 9999 pill"의 3단으로만 리듬을 유지한다. Motion도 `0.15s` transition duration과 `scale(1.04)` hover, 그 외에는 거의 모션이 없다 — 음악이 주인공이라 UI가 배경으로 밀려나는 게 맞는 설계다.

### Key Characteristics

- Spotify green `#1ED760` — 10년 고수한 audio-first identity
- True black `#000` / off-black `#121212` / `#141414` 다크 레이어 3단
- Encore semantic token layer: `--text-bright-accent`, `--essential-*`, `--background-*`
- Campaign theme variants (`#590810` / `#491E00` / `#073116` / `#052A56`)
- SpotifyMixUI + SpotifyMixUITitle + 다국어 CircularSp 병렬 로드
- weight 400/700/800/900 4단 계단 (중간 weight 없음)
- pill CTA 시그니처: radius 9999 + scale(1.04) hover + `#3BE477` light-up
- headline 48-96px, line-height 1.0-1.1 impact

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Vibrant Minimal — black canvas 위 초록 pill의 single-accent 미니멀리즘
> **Aesthetic Category**: Vibrant Minimal
> **Signature Element**: pill_cta_impact — radius 9999 + scale(1.04) hover + `#3BE477` glow
> **Code Complexity**: medium — Encore semantic tokens + Svelte hash class + campaign theme variants

---

## 01. Quick Start

> 5분 안에 Spotify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 다크 + Spotify green 시그니처 */
:root {
  --spotify-green: #1ED760;
  --spotify-green-hover: #3BE477;
  --spotify-green-active: #1ABC54;
  --bg-base: #000000;
  --bg-elevated: #121212;
  --fg: #FFFFFF;
}
body { background: var(--bg-base); color: var(--fg); }
```

```css
/* 2. 폰트 스택 */
body {
  font-family: "SpotifyMixUI", "CircularSp", Helvetica, Arial, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}
h1, .display { font-family: "SpotifyMixUITitle", "SpotifyMixUI", sans-serif; font-weight: 700; }
```

```css
/* 3. 시그니처 pill CTA */
.btn-primary {
  background: #1ED760;
  color: #000;
  padding: 12px 32px;
  border-radius: 9999px;
  font-weight: 700;
  transition: background .15s ease, transform .15s ease;
}
.btn-primary:hover { background: #3BE477; transform: scale(1.04); }
.btn-primary:active { background: #1ABC54; transform: scale(1.0); }
```

**절대 하지 말아야 할 것 하나**: pill CTA 모서리를 `8px`이나 `12px`로 둥글게 하지 마라 — Spotify의 CTA는 `9999px` 완전 pill만 쓴다. `scale(1.04)` hover도 필수. 이 두 개 중 하나라도 빠지면 Spotify가 아니라 Twitch/Discord 느낌이 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://spotify.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA |
| HTML size | ~180KB (hero landing) |
| CSS files | 6개 외부, 총 ~600KB (Encore + campaign themes) |
| Token system | Encore design system (`--encore-*` + `--text-*`, `--background-*`, `--essential-*`) |
| Method | CSS custom properties + Svelte hash selectors |
| Vars resolved | 185 / 221 (84%) |

---

## 03. Tech Stack

- **Framework**: Svelte (hash class `svelte-164a8y4` 등)
- **Design system**: Encore (Spotify 자체, 공개 일부 github.com/spotify/encore-web)
- **CSS architecture**: semantic token layer (`--text-*`, `--essential-*`, `--background-*`, `--decorative-*`)
- **Naming**: `button-primary__inner`, `mh-mobile-menu`, `o-section` 등 BEM-ish
- **Default theme**: dark (black base)
- **Font loading**: 셀프 호스트 SpotifyMixUI + CircularSp 다국어 변형 병렬
- **i18n**: Arab / Cyrl / Deva / Grek / Hebr · 각 언어별 CircularSp-[Script]
- **Campaign variants**: landing별 `--text-bright-accent` 재매핑

---

## 04. Font Stack

- **Body/UI**: `SpotifyMixUI`, `CircularSp`, `Helvetica`, `Arial`, `sans-serif`
- **Display/Title**: `SpotifyMixUITitle`, `SpotifyMixUITitleVariable` (variable font)
- **i18n bodies**: `CircularSp-Arab`, `CircularSp-Cyrl`, `CircularSp-Deva`, `CircularSp-Grek`, `CircularSp-Hebr`
- **i18n aliases**: `circular-spotify-arabic` / `cyrillic` / `deva` / `greek` / `hebrew`
- **Weights used**: 100 · 400 · 700 · 800 · 900 (중간 weight 300/500/600 없음)

---

## 05. Typography Scale

> Encore `--encore-text-size-*` 계단. 400 body + 700/800/900 display. smaller-3(10px) ~ larger-5(96px).

| Token | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `--encore-text-size-smaller-3` | 0.625rem (10px) | 400 | 1.4 | micro caption |
| `--encore-text-size-smaller-2` | 0.75rem (12px) | 400 | 1.5 | caption |
| `--encore-text-size-smaller` | 0.875rem (14px) | 400 | 1.5 | small |
| `--encore-text-size-base` | 1rem (16px) | 400 | 1.5 | body |
| `--encore-text-size-large` | 1.25rem (20px) | 400 | 1.4 | lead |
| `--encore-text-size-larger` | 1.5rem (24px) | 700 | 1.3 | h3 |
| `--encore-text-size-larger-2` | 2rem (32px) | 700 | 1.2 | h2 |
| `--encore-text-size-larger-3` | 3rem (48px) | 800 | 1.1 | h1 |
| `--encore-text-size-larger-4` | 4rem (64px) | 800 | 1.05 | display |
| `--encore-text-size-larger-5` | 6rem (96px) | 900 | 1.0 | hero impact |

---

## 06. Colors

> Black-canvas + Spotify green 축. Campaign별 theme variant 6종. 실제 CSS에서 추출한 ramp.

### Signature

| Name | Hex | Role |
|---|---|---|
| spotify-green | `#1ED760` | primary brand |
| green-hover | `#3BE477` | pill hover |
| green-active | `#1ABC54` | pill press |
| green-dark | `#107434` | text-bright-accent on light |
| green-dark-2 | `#127E38` | alt accent dark |
| green-mid | `#159542` | essential-bright-accent alt |
| green-mid-2 | `#169F47` | alt essential |
| green-tint | `#96F0B6` | chip / pale accent |

### Neutral (dark-first layer)

| Name | Hex | Use |
|---|---|---|
| bg-base | `#000000` | true black canvas |
| bg-elevated | `#121212` | card base |
| bg-elevated-2 | `#141414` | raised card |
| bg-elevated-3 | `#1F1F1F` | popover |
| surface-high | `#343434` | input / divider |
| fg | `#FFFFFF` | primary text |
| fg-muted | `#C7C7C7` | secondary |
| fg-subtle | `#919496` | meta |
| border-alt | `#2A2A2A` | subtle divider |
| off-white | `#F0F0F0` | high contrast surface |

### Campaign Theme Variants

> 각 landing은 `--text-bright-accent`를 자기 테마 hex로 재매핑한다

| Theme | Hex | Context |
|---|---|---|
| Deep-Red | `#590810` | Wrapped / Halloween 계열 |
| Deep-Brown | `#491E00` | Podcast 계열 |
| Deep-Green | `#073116` | Premium Family 계열 |
| Deep-Navy | `#052A56` | Tech / Annual |
| Rose | `#FFD2D7` | Love / Duo |
| Amber | `#FFD97E` | Wrapped Top Artist |
| Sky | `#C8E0FC` | Discover Weekly |
| Violet | `#C4B1D4` | Rap Caviar 계열 |

### Utility Accent

| Name | Hex | Use |
|---|---|---|
| link-blue | `#0D72EA` | external link |
| link-blue-dark | `#0C69D8` | link hover |
| link-blue-deep | `#0951A6` | link active |
| warn-orange | `#FFA42B` / `#FFB656` | warning badge |
| error-red | `#E91429` / `#D81326` | error state |

---

## 07. Spacing

> Encore graphic-size 시스템. 12 → 88px decorative scale + informative 별도 scale.

| Token | Value | Use |
|---|---|---|
| `--encore-graphic-size-decorative-smaller-2` | 12px | chip / badge |
| `--encore-graphic-size-decorative-smaller` | 16px | icon small |
| `--encore-graphic-size-decorative-base` | 24px | icon base |
| `--encore-graphic-size-decorative-larger` | 32px | header icon |
| `--encore-graphic-size-decorative-larger-2` | 40px | avatar |
| `--encore-graphic-size-decorative-larger-3` | 48px | CTA icon |
| `--encore-graphic-size-decorative-larger-4` | 64px | hero mark |
| `--encore-graphic-size-decorative-larger-5` | 88px | feature icon |

### Section Padding

- mobile: 32px vertical (`.mh-mobile-menu nav { padding:32px }` 참조)
- standard: 64-80px
- hero: 96-160px

---

## 08. Radius

> pill(9999)이 시그니처. card/modal은 8/16px.

| Name | Value | Use |
|---|---|---|
| `radius-pill` | 9999px | **CTA 전용 · Spotify 시그니처** |
| `radius-lg` | 16px | modal / hero card |
| `radius-md` | 8px | album cover / card |
| `radius-sm` | 4px | input / small chip |

---

## 09. Shadows

Spotify는 그림자에 의존하지 않는다 — black 배경 위에서 그림자는 거의 보이지 않기 때문에, elevation은 `#121212` → `#141414` → `#1F1F1F` **layered bg** 로 표현한다.

| Name | Value | Use |
|---|---|---|
| `shadow-sm` | `0 2px 4px rgba(0,0,0,0.5)` | 거의 사용 안 함 |
| `shadow-lg` | `0 16px 24px rgba(0,0,0,0.5)` | modal / popover |
| elevation via bg | bg-elevated layering | **실사용 패턴** |

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| pill hover | `background-color, transform 0.15s ease-out` | button-primary |
| pill scale | `scale(1.04)` on hover, `scale(1.0)` on active | 시그니처 |
| link hover | `0.15s ease` color transition | link underline |
| focus ring | border-width 2px + color | `--encore-border-width-focus: 2px` |

---

## 11. Layout Patterns

### Grid

- **Max-width**: 1400px (content container)
- **Gutter**: 24px (base) / 16px (mobile)
- **Columns**: 12 grid + Flexbox mix via Svelte components
- **Breakpoint**: 768 / 1024 / 1280

### Hero

- **Layout**: full-bleed dark bg, centered 1-column headline + dual CTA
- **Bg**: solid `#000` 또는 campaign theme solid
- **H1**: 64-96px (`--encore-text-size-larger-4` ~ `larger-5`) · weight 900
- **CTA**: primary pill `#1ED760` + secondary outline pill

### Section Rhythm

- **Padding**: 96-160px (hero) / 64-80px (feature) / 32px (mobile)
- **Inner max-width**: 1400px
- **Variant**: campaign theme를 section scoped `--text-bright-accent` 재매핑으로 토글

### Card

- **Padding**: 16-24px
- **Radius**: 8px (standard) / 16px (feature)
- **Bg**: `#121212` / `#141414` / `#1F1F1F` 3단 elevation
- **Border**: 1px solid `#2A2A2A` 또는 none

### Navigation

- **Type**: horizontal desktop + hamburger mobile
- **Height**: ~72px
- **Bg**: solid `#000` or transparent on dark hero
- **Mobile menu bg**: `#000` fullscreen overlay, padding 32px

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| `sm` | 768px | mobile stacked |
| `md` | 1024px | tablet 2-col |
| `lg` | 1280px | desktop full |
| `xl` | 1400px | max container cap |

### Collapsing Strategy

- Mobile: 1-column stack · nav → hamburger fullscreen · hero H1 48-56px로 축소
- Tablet: 2-column grid 유지 · feature card 2-wide
- Desktop: 3-4 column feature grid · sticky nav 유지

---

## 13. Components

### Primary Button (Pill CTA) — 시그니처

**Spec**: bg `#1ED760` · color `#000` · radius 9999 · weight 700 · padding 12px 32px · hover `#3BE477` + scale(1.04) · active `#1ABC54`

```css
.button-primary__inner {
  position: relative;
  color: #000;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1ED760;
  border-radius: 9999px;
  font-weight: 700;
  padding: 12px 32px;
  transition-property: background-color, transform;
  transition-duration: 0.15s;
  transition-timing-function: cubic-bezier(0.3, 0, 0, 1);
}
.button-primary:hover .button-primary__inner {
  background-color: #3BE477;
  transform: scale(1.04);
}
.button-primary:active .button-primary__inner {
  background-color: #1ABC54;
}
.button-primary:disabled .button-primary__inner {
  opacity: 0.3;
  color: #000;
  background-color: #1ED760;
}
```

### Secondary Button (Outline Pill)

**Spec**: bg transparent · border 1px solid #FFF · color `#FFF` · radius 9999 · hover border + bg `rgba(255,255,255,0.1)`

```css
.button-secondary {
  background: transparent;
  border: 1px solid #FFFFFF;
  color: #FFFFFF;
  padding: 12px 32px;
  border-radius: 9999px;
  font-weight: 700;
  transition: background .15s ease, transform .15s ease;
}
.button-secondary:hover {
  background: rgba(255,255,255,0.1);
  transform: scale(1.04);
}
```

### Card

앨범/플레이리스트 썸네일 카드

**Spec**: bg `#121212` · radius 8px · padding 16px · hover bg `#1F1F1F`

```css
.card {
  background: #121212;
  border-radius: 8px;
  padding: 16px;
  transition: background .2s ease;
}
.card:hover { background: #1F1F1F; }
```

### Hero Headline

**Spec**: font-size 96px (`--encore-text-size-larger-5`) · weight 900 · line-height 1.0 · letter-spacing -0.04em · color `#FFFFFF`

```css
.hero h1 {
  font-family: "SpotifyMixUITitle", sans-serif;
  font-size: 6rem; /* 96px */
  font-weight: 900;
  line-height: 1.0;
  letter-spacing: -0.04em;
  color: #FFFFFF;
}
```

### Campaign Section Theme Override

**Spec**: section scope에서 accent 재매핑 (e.g. Wrapped는 Deep-Red)

```css
section.theme-wrapped {
  --text-bright-accent: #590810;
  --essential-bright-accent: #590810;
  background: #FFD2D7;
  color: #590810;
}
```

---

## 14. Content / Copy Voice

| Label | Rule | Example |
|---|---|---|
| Tone | confident, music-forward, universal | "Play your favorites" |
| Copy length | Headline 3-6 단어 impact · body 1-2 문장 | — |
| i18n | Arab / Cyrl / Deva / Grek / Hebr 스크립트 병렬 | — |
| CTA verb | "Get Spotify Free" · "Try Premium" · "Play" | — |

---

## 15. Drop-in CSS

```css
:root {
  --spotify-green: #1ED760;
  --spotify-green-hover: #3BE477;
  --spotify-green-active: #1ABC54;
  --spotify-green-dark: #107434;
  --bg-base: #000000;
  --bg-elevated: #121212;
  --bg-elevated-2: #141414;
  --bg-elevated-3: #1F1F1F;
  --fg: #FFFFFF;
  --fg-muted: #C7C7C7;
  --fg-subtle: #919496;
  --border-alt: #2A2A2A;

  --font-body: "SpotifyMixUI", "CircularSp", Helvetica, Arial, sans-serif;
  --font-display: "SpotifyMixUITitle", "SpotifyMixUI", sans-serif;
  --font-weight-body: 400;
  --font-weight-bold: 700;
  --font-weight-display: 900;

  --radius-pill: 9999px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

body {
  font-family: var(--font-body);
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.5;
  color: var(--fg);
  background: var(--bg-base);
}

.hero h1 {
  font-family: var(--font-display);
  font-size: 6rem;
  font-weight: 900;
  line-height: 1.0;
  letter-spacing: -0.04em;
}

.btn-primary {
  background: var(--spotify-green);
  color: #000;
  padding: 12px 32px;
  border-radius: var(--radius-pill);
  font-weight: 700;
  transition: background .15s cubic-bezier(.3,0,0,1), transform .15s cubic-bezier(.3,0,0,1);
}
.btn-primary:hover { background: var(--spotify-green-hover); transform: scale(1.04); }
.btn-primary:active { background: var(--spotify-green-active); transform: scale(1.0); }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'spotify-green': {
          DEFAULT: '#1ED760',
          hover: '#3BE477',
          active: '#1ABC54',
          dark: '#107434',
        },
        'bg-base': '#000000',
        'bg-elev': {
          1: '#121212',
          2: '#141414',
          3: '#1F1F1F',
        },
      },
      fontFamily: {
        sans: ['SpotifyMixUI', 'CircularSp', 'Helvetica', 'Arial', 'sans-serif'],
        display: ['SpotifyMixUITitle', 'SpotifyMixUI', 'sans-serif'],
      },
      fontSize: {
        hero: ['6rem', { lineHeight: '1.0', letterSpacing: '-0.04em' }],
        display: ['4rem', { lineHeight: '1.05', letterSpacing: '-0.03em' }],
      },
      borderRadius: {
        pill: '9999px',
      },
    }
  }
}
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `--spotify-green` | `#1ED760` |
| Brand hover | `--spotify-green-hover` | `#3BE477` |
| Brand active | `--spotify-green-active` | `#1ABC54` |
| Background base | `--bg-base` | `#000000` |
| Background elevated | `--bg-elevated` | `#121212` |
| Text primary | `--fg` | `#FFFFFF` |
| Text muted | `--fg-muted` | `#C7C7C7` |
| Text subtle | `--fg-subtle` | `#919496` |

### Example Component Prompts

**🎯 Hero Section**

> Spotify style hero: black `#000` background full-bleed, headline 96px / weight 900 / line-height 1.0 / color white, 3-6 word impact. Primary CTA: pill bg `#1ED760` color `#000` radius 9999. Secondary CTA: outline white pill.

**🔘 Pill CTA**

> Spotify pill button: bg `#1ED760`, color `#000` (검정 텍스트!), padding 12px 32px, border-radius 9999. Hover: bg `#3BE477` + transform scale(1.04). Active: bg `#1ABC54`. Transition `.15s cubic-bezier(.3,0,0,1)`.

**🎴 Album Card**

> Spotify card: bg `#121212`, radius 8px, padding 16px. Hover: bg `#1F1F1F`. Cover image 1:1 ratio radius 4px. Title 16px weight 700 white. Artist 14px weight 400 `#C7C7C7`.

**🎨 Campaign Theme Variant**

> Spotify campaign section: override `--text-bright-accent` to campaign hex. Wrapped = `#590810` on `#FFD2D7`. Premium = `#073116` on `#96F0B6`. Change brand green to theme pair — but keep pill CTA shape.

### Iteration Tips

- `#1ED760` Spotify green은 CTA/heading-accent 전용. bg fill로는 쓰지 않는다 (너무 튐).
- pill radius는 `9999px` 강제. `12px` 등으로 둥글리면 Spotify 느낌이 증발한다.
- weight는 400/700/800/900만 사용. 300/500/600 absent.
- hover `scale(1.04)` 는 반드시 `transform` 기반이어야 한다 — `padding` 변경 안 됨.
- campaign 변형시 `--text-bright-accent` 재매핑하는 scoped CSS 패턴 권장.

---

## 18. DO / DON'T

### DO

- ✅ true black `#000` 또는 off-black `#121212/#141414/#1F1F1F` 3단 elevation 사용
- ✅ Spotify green `#1ED760`을 CTA + heading accent + 재생버튼 icon에만 제한
- ✅ pill CTA는 `border-radius: 9999px`로 완전 pill
- ✅ hover에 `transform: scale(1.04)` + `background-color: #3BE477` 조합 고수
- ✅ display/title은 SpotifyMixUITitle · weight 900 · line-height 1.0~1.05
- ✅ i18n시 CircularSp-[Script] 서브 폰트 병렬 로드

### DON'T

- 배경을 `#1A1A1A` 같은 어중간한 그레이로 두지 말 것 — `#000` / `#121212` / `#141414` / `#1F1F1F` 중 하나
- `#1ED760` 초록을 body 텍스트 컬러로 쓰지 말 것 — accent 전용
- pill CTA를 `12px`/`8px`/`16px` radius로 둥글리지 말 것 — `9999px`만
- body 폰트를 weight 300/500/600로 두지 말 것 — 400/700만 이원화
- hover에 transform 없이 color만 바꾸지 말 것 — scale(1.04)가 시그니처
- true black 위에 `box-shadow`로 elevation 표현하지 말 것 — bg-layer로 처리
- 초록을 `#00E25A` / `#1DB954` (구 Spotify 로고 컬러) 로 쓰지 말 것 — 2015 리브랜딩 이후 `#1ED760`이 공식
