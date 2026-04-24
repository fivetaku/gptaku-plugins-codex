---
schema_version: 3.1
slug: vercel
service_name: Vercel
site_url: https://vercel.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#000000"
primary_font: Geist
font_weight_normal: 400
token_prefix: --ds-*, --geist-*

bold_direction: "Refined Minimalism"
aesthetic_category: "Refined Minimalism"
signature_element: minimal_extreme
code_complexity: low

medium: web
medium_confidence: high
---

# DESIGN.md — Vercel (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Vercel의 마케팅 홈은 **"흑백 + 한 번의 무지개 스펙트럼"** 이라는 한 줄짜리 디자인 선언에 가깝다. 배경은 `#FFFFFF`, 본문은 `#000000`, CTA도 `#000000` on `#FFFFFF` — UI 자체에는 채도가 없다. 그런데 페이지 중앙의 히어로 아래에 유일하게 **pastel spectrum gradient**가 펼쳐지고, 그 위에 작은 삼각형 로고가 얹혀 이 사이트의 시각적 서명이 된다. "Build and deploy on the AI Cloud"라는 카피는 brutalist하게 큰 사이즈로 놓이지만, 그 주위 공간은 숨이 막힐 만큼 비어 있다. 이것이 Vercel이 말하는 edge: **무채색 타이포그래피와 채도 폭발 한 점의 대비**.

색상 전략은 철저하게 **monochrome-first**다. `--ds-gray-100` ~ `--ds-gray-1000` 10단계 회색 램프가 UI 전체를 지배하고, HSLA 값(`0, 0%, 95%` → `0, 0%, 9%`)은 모두 채도 0%다. 채도 있는 토큰(`--geist-highlight-pink #FF0080`, `--geist-highlight-yellow #FFF500`, `--geist-violet #7928CA`, `--geist-cyan #50E3C2`, `--geist-success #0070F3` "Vercel Blue")은 존재하지만 일반 surface에 쓰지 않는다. 블로그의 카테고리, 차트, 문서 sidebar 같은 **정보 식별 목적**에만 등장한다. 기본 `background-color`는 `#FFFFFF` (light), `#000000` (dark) — 중간 회색 surface를 의도적으로 피한다.

타이포그래피의 축은 **Geist**(Vercel 자체 산스) + **Geist Mono**다. body weight는 `400`, 그러나 실제 통계상 `500 / 600`이 압도적으로 많다 (500: 137회, 600: 106회) — 이는 navigation·card title·button label 등 "조금 더 또렷해야 하는" 자리 때문이다. 계단은 `.875rem (14px)` · `1rem (16px)` · `20/24/32/40/48/56/64px`로 부드럽게 상승하며, 히어로 H1만 `clamp(24px, computed, 72px)`의 fluid 타이포그래피를 쓴다. 특이하게 `GeistPixelSquare/Grid/Circle/Triangle/Line` 같은 **픽셀 아이콘 폰트 5종**을 자체 배포한다 — loading indicator, logo animation에 쓰인다.

레이아웃은 **1200px page-width + 24px gap**이 표준이지만 실제 컨테이너는 `600px` (prose), `960px` (marketing hero) 두 폭이 가장 자주 나타난다. `--geist-space: 4px`를 baseline unit으로 `1x / 2x / 3x / 4x / 6x / 8x / 10x / 16x / 24x / 32x / 48x / 64x` 배수 scale을 공유한다. radius는 `6px` (기본 `--geist-radius`), `12px` (카드), `9999px` (pill) 3단 체계. shadow는 6단계 계단 (`--shadow-smallest` → `--shadow-large`)으로 모두 `#0000001a ~ 1f` 형태의 **균일한 4~6% 검정 오파시티**를 유지해서 "그림자가 있는지 없는지 모를 정도"의 엷은 깊이만 준다.

인터랙션은 `.15s` duration이 압도적(37회) — 거의 모든 hover가 이 한 값으로 통일. easing은 대부분 `ease-out` 또는 생략 (linear). Vercel은 "빠르고 무뚝뚝한" UI를 선택했다.

### Key Characteristics

- Mono-first palette — `#000000` / `#FFFFFF` + 10-step gray ramp (HSL saturation 0%)
- 유일한 채도 point: 히어로 아래 pastel prism gradient + `#0070F3` Vercel Blue
- Geist + Geist Mono self-hosted (+ 5종 GeistPixel 아이콘 폰트)
- `--geist-space: 4px` baseline × `{1x,2x,3x,4x,6x,8x,10x,16x,24x,32x,48x,64x}` scale
- Radius: `6 / 12 / 9999px` 3단
- Shadow: 6단 4-6% opacity — 거의 flat
- `.15s` transition 압도적 — "빠르고 조용함"
- `color_system: monochrome` (함정 #10 대응)

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Refined Minimalism
> **Aesthetic Category**: Refined Minimalism
> **Signature Element**: 이 사이트는 **순백 배경 위 brutalist H1 + 유일한 pastel prism gradient hero art**로 기억된다.
> **Code Complexity**: low — CSS variables + 1-transition + 절제된 hover, 장식적 모션 거의 없음

---

## 01. Quick Start

> 5분 안에 Vercel처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Geist", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 (light default) */
:root {
  --bg: #FFFFFF;
  --fg: #000000;
  --border: hsl(0, 0%, 92%); /* --ds-gray-200 */
}
body { background: var(--bg); color: var(--fg); }

/* 3. CTA는 검정 pill */
:root { --brand: #000000; }
.cta {
  background: var(--brand); color: #FFFFFF;
  border-radius: 9999px; padding: 0 16px; height: 40px;
}
```

**절대 하지 말아야 할 것 하나**: 본문 UI에 채도 있는 색(`#0070F3`, `#FF0080`, `#7928CA` 등)을 쓰지 말 것. Vercel의 정체성은 "컬러가 없다"이다. 채도는 오직 히어로 gradient 아트와 블로그 카테고리 칩처럼 **한 점**에만 허용된다. 면적으로 채도를 쓰면 즉시 다른 사이트가 된다 (함정 #10 monochrome 규칙).

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://vercel.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 910,996 bytes (Next.js SSR) |
| CSS files | 12개 외부, 총 약 868KB minified |
| Token prefix | `--ds-*` (core design system) + `--geist-*` (legacy Geist UI) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (자체 SSR, Vercel hosting)
- **Design system**: Geist DS (`--ds-*` modern + `--geist-*` legacy) + `vercel/geist` 오픈소스 컴포넌트
- **CSS architecture**: 3-tier HSL-based value system
  ```
  core   (--ds-gray-NNN-value: "0, 0%, 95%")       HSL 튜플 (raw)
  alias  (--ds-gray-NNN: hsla(var(--ds-gray-NNN-value), 1))   full color
  comp   (--themed-bg, --menu-bg, --accents-N)      역할 기반 alias
  ```
- **Class naming**: CSS Modules + Tailwind scoped (`.button-module__QyrFCa__invert`, `.tailwind .bg-white`)
- **Default theme**: light (bg = `#FFFFFF`, fg = `#000000`) + `.dark-theme` class 토글
- **Font loading**: 셀프 호스트 `Geist`, `Geist Mono`, `GeistPixelSquare/Grid/Circle/Triangle/Line` (next/font)
- **Canonical anchor**: `#000000` (text) / `#0070F3` Vercel Blue (legacy success color) — UI 자체는 monochrome

---

## 04. Font Stack

- **Display font**: `Geist` (Vercel 자체, OFL 오픈소스)
- **Code font**: `Geist Mono` (OFL)
- **Icon fonts**: `GeistPixelSquare / Grid / Circle / Triangle / Line` (자체, 로고 애니메이션 용)
- **Optional**: `Space Grotesk`, `Space Mono`, `Roboto Mono`, `DSEG7 Classic`, `KaTeX_*` (문서 수식용)
- **Weight normal / bold**: `400` / `700` (실사용 top 3: 500 / 600 / 400)

```css
:root {
  --font-sans: "Geist", Arial, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  --font-sans-fallback: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
  --font-mono: "Geist Mono", ui-monospace, SFMono-Regular, "Roboto Mono", Menlo, Monaco, "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace;
  --font-mono-fallback: "Roboto Mono", Menlo, Monaco, "Lucida Console", "Liberation Mono", "DejaVu Sans Mono", "Bitstream Vera Sans Mono", "Courier New", monospace;
  --font-space-grotesk: "Space Grotesk", var(--font-sans);
}
body {
  font-family: var(--font-sans, var(--font-sans-fallback)), ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}
```

> **라이선스 주의**: `Geist`는 OFL — 재배포 가능 (`vercel.com/font`).

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| small | `.875rem` (14px) | 400 | 1.5 | normal |
| base | `1rem` (16px) | 400 | 1.5 | normal |
| body-l | `18px` | 400 | 1.5 | normal |
| h5 | `20px` | 600 | 1.3 | normal |
| h4 | `24px` | 600 | 1.25 | normal |
| h3 | `32px` | 600 | 1.2 | `-0.01em` |
| h2 | `40px` | 600 | 1.15 | `-0.02em` |
| h1 | `48px / 56px / 64px` | 700 | 1.1 | `-0.02em` |
| hero | `clamp(24px, var(--computed-font-size), 72px)` | 700 | 1.05 | `-0.03em` |

> ⚠️ Vercel의 히어로는 **fluid clamp**다 (`24px → 72px`). viewport에 따라 실시간 보간되므로 고정 px로 재현하면 즉시 다른 사이트가 된다. 일반 H1은 `48/56/64`px, H2는 `40px`, H3는 `32px` — 큰 사이즈에 음수 tracking 필수 (optical compensation, 함정 #13).

---

## 06. Colors

### 06-1. Brand (monochrome — no traditional brand ramp)

Vercel은 `color_system: monochrome`이다. "brand color"는 **black/white** 쌍이며, 채도 있는 "Vercel Blue"는 legacy success 토큰이지 UI 기본색이 아니다.

| Token | Hex | Role |
|---|---|---|
| `--ds-gray-1000` | `hsla(0,0%,9%,1)` ≈ `#171717` | canonical dark anchor |
| `--ds-background-100` | `hsla(0,0%,100%,1)` = `#FFFFFF` | canonical light anchor |
| `--geist-foreground` | `#FFFFFF` (dark theme 내) | — |
| `--geist-background` | `#000000` (dark theme 내) | — |

### 06-3. Neutral Ramp (`--ds-gray-*` + `--ds-background-*`)

| Step | Light Hex | Dark Hex | Note |
|---|---|---|---|
| bg-100 | `#FFFFFF` | `#000000` | page background |
| bg-200 | `#FAFAFA` | `#0A0A0A` | panel subtle |
| gray-100 | `#F2F2F2` (≈95%L) | ≈`#1A1A1A` | hover bg |
| gray-200 | `#EBEBEB` (92%L) | ≈`#1F1F1F` | border subtle |
| gray-300 | `#E6E6E6` (90%L) | ≈`#242424` | border |
| gray-400 | `#EBEBEB` (92%L) | ≈`#2E2E2E` | border strong |
| gray-500 | `#C9C9C9` (79%L) | ≈`#454545` | muted |
| gray-600 | `#A8A8A8` (66%L) | ≈`#666666` | fg-muted |
| gray-700 | `#8F8F8F` (56%L) | ≈`#878787` | fg-secondary |
| gray-800 | `#7D7D7D` (49%L) | ≈`#A1A1A1` | fg-muted-dark |
| gray-900 | `#4D4D4D` (30%L) | ≈`#B8B8B8` | fg-strong |
| gray-1000 | `#171717` (9%L) | ≈`#EDEDED` | fg-primary (anchor) |

> Vercel 회색 램프는 HSL `(0, 0%, L%)` 시리즈 — 전부 채도 0% neutral.

### 06-3b. Accents step scale (legacy Geist, 8-step)

| Token | Hex (light) | Hex (dark) |
|---|---|---|
| `--accents-1` | `#FAFAFA` | `#111111` |
| `--accents-2` | `#EAEAEA` | `#333333` |
| `--accents-3` | `#999999` | `#444444` |
| `--accents-4` | `#888888` | `#666666` |
| `--accents-5` | `#666666` | `#888888` |
| `--accents-6` | `#444444` | `#999999` |
| `--accents-7` | `#333333` | `#EAEAEA` |
| `--accents-8` | `#111111` | `#FAFAFA` |

### 06-4. Accent Families (information / chart use only — NOT for UI surface)

| Family | Key step | Hex |
|---|---|---|
| `--geist-success` ("Vercel Blue") | 500 | `#0070F3` |
| `--geist-success-light` | 400 | `#3291FF` |
| `--geist-success-lighter` | 100 | `#D3E5FF` |
| `--geist-success-dark` | 700 | `#0761D1` |
| `--geist-violet` | 500 | `#7928CA` |
| `--geist-violet-light` | 400 | `#8A63D2` |
| `--geist-violet-lighter` | 100 | `#D8CCF1` |
| `--geist-cyan` | 500 | `#50E3C2` |
| `--geist-cyan-light` | 400 | `#79FFE1` |
| `--geist-cyan-lighter` | 100 | `#AAFFEC` |
| `--geist-warning` | 500 | `#F5A623` |
| `--geist-warning-light` | 400 | `#F7B955` |
| `--geist-warning-lighter` | 100 | `#FFEFCF` |
| `--geist-error` | 500 | `#EE0000` |
| `--geist-error-light` | 400 | `#FF1A1A` |
| `--geist-error-lighter` | 100 | `#F7D4D6` |
| `--geist-highlight-purple` | — | `#F81CE5` |
| `--geist-highlight-pink` | — | `#FF0080` |
| `--geist-highlight-magenta` | — | `#EB367F` |
| `--geist-highlight-yellow` | — | `#FFF500` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--ds-background-100` | `#FFFFFF` | page background (light) |
| `--ds-background-200` | `#FAFAFA` | subtle surface |
| `--ds-gray-1000` | `#171717` | primary text (light) |
| `--ds-gray-700` | `#8F8F8F` | muted text |
| `--ds-gray-alpha-400` | `#00000014` (8% black) | border subtle |
| `--ds-gray-alpha-600` | `#00000057` (34% black) | border strong |

### 06-6. Alias Layer (component-level)

| Alias | Resolves to | Usage |
|---|---|---|
| `--themed-bg` | `var(--ds-gray-1000)` or set at component | CTA button background |
| `--themed-hover-bg` | `#383838` or `var(--ds-gray-alpha-200)` | button hover |
| `--themed-focus-ring` | `#A35200` (brand amber) / varies | focus outline |
| `--menu-bg` | `#FFFFFF` (light) / `#000000` (dark) | dropdown |
| `--light-border-color` | `#FFFFFF1A` | dark overlay border |

### 06-7. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#00000000` | 265 | transparent (utility) |
| 2 | `#FFFFFF` | 70 | light bg / text (dark) |
| 3 | `#000000` | 69 | text / CTA (light) |
| 4 | `#0000000A` | 37 | border alpha 4% |
| 5 | `#FFFFFF00` | 28 | transparent white |
| 6 | `#2C8CE1` | 20 | svg pattern (illustration) |
| 7 | `#00000005` | 16 | border alpha 2% |
| 8 | `#0000001A` | 12 | shadow alpha 10% |
| 9 | `#0000001F` | 12 | shadow alpha 12% |
| 10 | `#333333` | 12 | neutral dark |

---

## 07. Spacing

네이밍: **`--geist-space-Nx` = N × 4px baseline**.

| Token | Value | Use case |
|---|---|---|
| `--geist-space` | `4px` | baseline unit |
| `--geist-space-2x` | `8px` | tight inline gap |
| `--geist-space-3x` | `12px` | gap-half |
| `--geist-space-4x` | `16px` | standard inline padding |
| `--geist-space-6x` | `24px` | `--geist-space-gap` (column gutter) |
| `--geist-space-8x` | `32px` | `--geist-space-small`, section base |
| `--geist-space-10x` | `40px` | `--geist-space-medium` |
| `--geist-space-large` | `48px` | large section padding |
| `--geist-space-16x` | `64px` | hero vertical rhythm |
| `--geist-space-24x` | `96px` | section breathing room |
| `--geist-space-32x` | `128px` | section break |
| `--geist-space-48x` | `192px` | hero vertical (desktop) |
| `--geist-space-64x` | `256px` | oversized hero |

**주요 alias**:

- `--geist-page-margin` → `var(--geist-space-gap)` = `24px`
- `--geist-page-width` → `1200px` (max content)
- `--geist-page-width-with-margin` → `calc(1200px + 48px)` = `1248px`
- `--header-height` → `64px`

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `--geist-radius` | `6px` | 기본 (input, button, chip) |
| — | `12px` | 카드 (compute) |
| — | `9999px` | pill (CTA 주요 형태) |
| — | `4px` | inner chip, code snippet |
| — | `2px` | tag 작은 것 |
| — | `50%` | avatar circle |

> Vercel CTA의 표준 형태는 **pill (9999px radius)** 이 아니라 6px가 기본이다. 홈 hero의 "Start Deploying" 버튼은 square-ish 6px로 관찰된다.

---

## 09. Shadows

Vercel은 shadow를 **4~6% 검정 오파시티**로 통일한다. 단층이 아니라 상태별로 깊이가 바뀐다.

| Level | Value | Usage |
|---|---|---|
| `--shadow-smallest` | `0px 2px 4px #0000001A` | hover tab indicator |
| `--shadow-extra-small` | `0px 4px 8px #0000001F` | popover subtle |
| `--shadow-small` | `0 5px 10px #0000001F` | card resting |
| `--shadow-medium` | `0 8px 30px #0000001F` | card hover |
| `--shadow-large` | `0 30px 60px #0000001F` | modal |
| `--shadow-hover` | `0 30px 60px #0000001F` | large hover |
| `--shadow-sticky` | `0 12px 10px -10px #0000001F` | sticky header shadow |

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| default transition | `.15s` | 절대 다수 (`.15s` 37회 — 전체 transition의 top) |
| color transition | `color .15s` | link hover |
| bg transition | `background .15s ease-out` | button hover |
| opacity transition | `opacity .2s` | modal fade |
| duration popover | `var(--ds-motion-popover-duration)` | popover open/close |
| timing popover | `var(--ds-motion-timing-swift)` | popover easing |

> 패턴: 대부분 `transition: <prop> .15s;` — easing 생략 (browser linear).

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1200px` (`--geist-page-width`)
- **Effective max**: `1248px` (with 2 × 24px margin)
- **Grid type**: CSS Grid + Flexbox 혼합
- **Gutter**: `24px` (`--geist-space-gap`)
- **Typical content width**: `600px` (prose) · `960px` (hero) · `1200px` (grid)

### Hero

- **🆕 Pattern Summary**: `~85vh + 순백 배경 + 대형 serifless H1(clamp 24→72px) + 듀얼 CTA(검정 pill + outline) + 하단 prism pastel gradient 아트 + 중앙 삼각형 로고`
- Layout: **1-column centered** (H1 + sub + CTA 페어), 아래 gradient hero art
- Background: `#FFFFFF` solid
- **🆕 Background Treatment**: `solid #FFFFFF` + 하단 hero art는 별도 SVG/canvas `linear-gradient(90deg, pink 0%, cyan 50%, yellow 100%)` 계열 prism + 삼각형 로고 overlay
- H1: `clamp(24px, var(--computed-font-size), 72px)` / weight `700` / tracking `-0.03em`
- Max-width: `960px` (hero 텍스트 column)

### Section Rhythm

```css
section {
  padding: 96px 24px;           /* --geist-space-24x + --geist-space-6x */
  max-width: 1200px;
  margin: 0 auto;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` (light) / `#0A0A0A` ~ `#111111` (dark)
- **Card border**: `1px solid var(--ds-gray-alpha-400)` (`#00000014` ≈ 8% black)
- **Card radius**: `12px`
- **Card padding**: `24px` (`--geist-space-6x`)
- **Card shadow**: `var(--shadow-small)` 기본, hover `var(--shadow-medium)`

### Navigation Structure

- **Type**: horizontal (`navigation-menu-module__AENi4G__root`)
- **Position**: `position: sticky; top: 0`
- **Height**: `64px` (`--header-height`), `--header-height-expanded: 100px` (hover 시 확장)
- **Background**: `var(--menu-bg)` = `#FFFFFF` (light) / `#000000` (dark)
- **Border**: `--menu-border-width: 1px; --menu-border-color: var(--ds-gray-400)` (하단 1px)

### Content Width

- **Prose max-width**: `600px` 또는 `624px`
- **Container max-width**: `1200px` (`--geist-page-width`)
- **Hero max-width**: `960px`
- **Sidebar width**: docs `280px` 관찰

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 600px` | 1-column, 햄버거 nav |
| Mobile-L | `≥ 600/601px` | tablet portrait |
| Tablet | `≥ 768px` | 2-col grid 시작 |
| Desktop | `≥ 960/961px` | full nav, 3-col grid |
| Large | `≥ 1200px` | sidebar + grid 4-col |

*Mobile-first* (`min-width` 95회 vs `max-width` 소수)

### Touch Targets

- **Minimum tap size**: `32px`
- **Button height (mobile)**: `40px` (`--geist-space-10x`) 기본
- **Input height (mobile)**: `40px`

### Collapsing Strategy

- **Navigation**: 600px 이하에서 햄버거 + full-screen sheet
- **Grid columns**: 3-col → 2-col (768px) → 1-col (600px)
- **Sidebar**: 960px 이하에서 숨김 (docs drawer로 전환)
- **Hero layout**: 그대로 유지 (이미 1-column) — 단 H1 clamp 가 자동으로 축소

### Image Behavior

- **Strategy**: Next.js `<Image>` component + lazy, AVIF/WebP
- **Max-width**: `100%`
- **Aspect ratio handling**: `aspect-ratio` 속성 + `object-fit: cover`

---

## 13. Components

### Buttons

```html
<button data-geist-button class="button-module__QyrFCa__primary">Start Deploying</button>
<button data-geist-button class="button-module__QyrFCa__tertiary">Get a Demo</button>
<button data-geist-button class="button-module__QyrFCa__invert">Documentation</button>
```

| Variant | background | color | border | radius | hover |
|---|---|---|---|---|---|
| primary (light) | `#000000` (or `var(--themed-bg)`) | `#FFFFFF` | none | `6px` | `#383838` (themed-hover-bg) |
| primary (dark) | `#FFFFFF` | `#000000` | none | `6px` | `#CCCCCC` |
| invert (light) | `var(--ds-gray-1000)` | `#FFFFFF` | none | `6px` | `#383838` |
| tertiary | `transparent` | `var(--ds-gray-1000)` | `transparent` | `6px` | `var(--ds-gray-alpha-200)` |
| outline | `transparent` | `#000000` | `1px solid var(--ds-gray-400)` | `6px` | `background: var(--ds-gray-alpha-200)` |

Heights: `24 / 32 / 40 / 48px` slot system.

### Badges

```html
<span class="geist-badge">New</span>
```

- `background: var(--ds-gray-alpha-200)` / `var(--ds-blue-200)` variant
- `color: var(--ds-gray-1000)`
- `border-radius: 9999px`
- `font: var(--font-mono) 12px 500`
- `padding: 2px 8px`

### Cards & Containers

```html
<article class="cmp-card">…</article>
```

- bg: `var(--ds-background-100)` `#FFFFFF`
- border: `1px solid var(--ds-gray-alpha-400)`
- radius: `12px`
- padding: `24px`
- shadow: `--shadow-small` `0 5px 10px #0000001F`
- hover: shadow → `--shadow-medium`, transition `.15s`

### Navigation

- bg: `#FFFFFF` (`--menu-bg`), sticky, height `64px`
- 로고: 좌측, `Geist` 16px weight 600, 삼각형 아이콘(`GeistPixelTriangle`)
- 링크: `Geist` 14px weight 500, color `var(--ds-gray-900)`
- Active: weight 600, color `var(--ds-gray-1000)`
- CTA 페어: "Log In" (text) + "Sign Up" (primary button, `#000000` bg)
- Mobile: 햄버거 → full-screen sheet

### Inputs & Forms

- height: `40px` 기본
- padding: `0 12px`
- border: `1px solid var(--ds-gray-400)`
- radius: `6px`
- focus: `outline: 2px solid var(--themed-focus-ring); outline-offset: 2px`
- placeholder: `color: var(--ds-gray-700)` `#8F8F8F`

### Hero Section

- Layout: 1-column centered, text stack (eyebrow pill → H1 → sub → dual CTA → hero art)
- Eyebrow pill: "Vercel April 2026 security incident" — light gray bg, small text
- H1: "Build and deploy on the AI Cloud." — `clamp(24px,…,72px)`, weight 700, tracking `-0.03em`
- Sub: `.875rem` 14px, color gray-700
- Primary CTA: `#000000` pill (radius `6px` 또는 `9999px`), text `#FFFFFF`
- Secondary CTA: outline, same radius, background transparent
- Hero art: 하단 pastel prism gradient + 삼각형 로고 (SVG + canvas 혼합)

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 동사 주도 선언, 5-8 단어 | "Build and deploy on the AI Cloud." |
| Primary CTA | 2단어, "Start + 동사" 또는 "Get + 명사" | "Start Deploying" / "Get a Demo" |
| Secondary CTA | 명사 기반 | "Request a Demo" / "Documentation" |
| Subheading | 기능 1문장 | "Vercel provides the developer tools and cloud infrastructure to build, scale, and secure a faster, more personalized web." |
| Tone | 기술 자신감 + 친근 (카피라이터가 아닌 엔지니어의 화법) | — |

---

## 15. Drop-in CSS

```css
/* Vercel — copy into your root stylesheet */
:root {
  /* Fonts */
  --v-font-sans:  "Geist", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --v-font-mono:  "Geist Mono", ui-monospace, SFMono-Regular, "Roboto Mono", Menlo, Monaco, monospace;
  --v-font-weight-normal: 400;
  --v-font-weight-medium: 500;
  --v-font-weight-semibold: 600;
  --v-font-weight-bold: 700;

  /* Brand (monochrome) */
  --v-fg:       #000000;
  --v-bg:       #FFFFFF;
  --v-bg-alt:   #FAFAFA;

  /* Neutrals (HSL-based, simplified) */
  --v-gray-200: #EBEBEB;
  --v-gray-400: #EBEBEB;
  --v-gray-500: #C9C9C9;
  --v-gray-700: #8F8F8F;
  --v-gray-900: #4D4D4D;
  --v-gray-1000:#171717;

  --v-border:   rgba(0,0,0,0.08);

  /* Optional accent (legacy) */
  --v-blue:     #0070F3;

  /* Spacing (4px baseline) */
  --v-space:    4px;
  --v-space-2x: 8px;
  --v-space-3x: 12px;
  --v-space-4x: 16px;
  --v-space-6x: 24px;
  --v-space-8x: 32px;
  --v-space-16x:64px;

  /* Radius */
  --v-radius:    6px;
  --v-radius-card: 12px;
  --v-radius-pill: 9999px;

  /* Shadow */
  --v-shadow-small:  0 5px 10px #0000001F;
  --v-shadow-medium: 0 8px 30px #0000001F;
  --v-shadow-large:  0 30px 60px #0000001F;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Vercel (Geist DS)
module.exports = {
  theme: {
    extend: {
      colors: {
        mono: {
          fg: '#000000',
          bg: '#FFFFFF',
          alt:'#FAFAFA',
        },
        gray: {
          100:'#F2F2F2',
          200:'#EBEBEB',
          300:'#E6E6E6',
          500:'#C9C9C9',
          600:'#A8A8A8',
          700:'#8F8F8F',
          800:'#7D7D7D',
          900:'#4D4D4D',
          1000:'#171717',
        },
        geist: {
          blue: '#0070F3',
          violet: '#7928CA',
          cyan: '#50E3C2',
          pink: '#FF0080',
          yellow: '#FFF500',
          warning: '#F5A623',
          error: '#EE0000',
        },
      },
      fontFamily: {
        sans: ['Geist', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['Geist Mono', 'ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal:   '400',
        medium:   '500',
        semibold: '600',
        bold:     '700',
      },
      borderRadius: {
        DEFAULT: '6px',
        card:    '12px',
        pill:    '9999px',
      },
      boxShadow: {
        smallest:    '0px 2px 4px #0000001A',
        'extra-small':'0px 4px 8px #0000001F',
        small:       '0 5px 10px #0000001F',
        medium:      '0 8px 30px #0000001F',
        large:       '0 30px 60px #0000001F',
        sticky:      '0 12px 10px -10px #0000001F',
      },
      transitionDuration: {
        DEFAULT: '150ms',
      },
      spacing: {
        '1x':'4px','2x':'8px','3x':'12px','4x':'16px',
        '6x':'24px','8x':'32px','10x':'40px',
        '16x':'64px','24x':'96px','32x':'128px',
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
| Brand primary | `--v-fg` | `#000000` |
| Background | `--v-bg` | `#FFFFFF` |
| Text primary | `--ds-gray-1000` | `#171717` |
| Text muted | `--ds-gray-700` | `#8F8F8F` |
| Border | `--ds-gray-alpha-400` | `#00000014` (8% black) |
| Success | `--geist-success` | `#0070F3` |
| Error | `--geist-error` | `#EE0000` |

### Example Component Prompts

#### Hero Section

```
Vercel 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF solid
- Eyebrow: 작은 pill, bg #FAFAFA, color #171717, font-size 14px, weight 500, radius 9999px
- H1: Geist, clamp(24px, 6vw, 72px), weight 700, tracking -0.03em, color #000000, 중앙 정렬
- 서브텍스트: Geist 16px, weight 400, color #8F8F8F, 중앙 정렬, max-width 600px
- Primary CTA: 배경 #000000, 텍스트 #FFFFFF, radius 6px, padding 0 20px, height 40px, font-weight 500
- Secondary CTA: transparent + border 1px solid #EBEBEB + color #000000, 동일 radius/height
- CTA 페어 gap: 12px
- 하단 hero art: linear-gradient prism (pink → cyan → yellow) + 삼각형 SVG 로고 overlay
- 섹션 padding: 96px 24px
```

#### Card Component

```
Vercel 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border 1px solid rgba(0,0,0,0.08), radius 12px
- padding: 24px
- shadow: 0 5px 10px #0000001F
- hover 시: shadow 0 8px 30px #0000001F, transition .15s
- 제목: Geist, 20px, weight 600, color #171717
- 본문: Geist, 14px, color #8F8F8F, line-height 1.5
```

#### Badge

```
Vercel 스타일 배지를 만들어줘.
- font: Geist Mono, 12px, weight 500
- padding: 2px 8px, radius 9999px (pill)
- 기본: bg rgba(0,0,0,0.05), color #171717
- 강조: bg #0070F3, color #FFFFFF (사용 지양, 드문 경우만)
```

#### Navigation

```
Vercel 스타일 상단 네비게이션을 만들어줘.
- 높이: 64px, position sticky top 0
- 배경: #FFFFFF, border-bottom 1px solid #EBEBEB
- 로고: 좌측, 삼각형 아이콘 + "Vercel" wordmark (Geist 16px weight 600)
- 링크: Geist 14px weight 500, color #4D4D4D, hover color #171717, transition .15s
- 활성 링크: color #171717, weight 600
- CTA 우측 페어: "Log In"(text link) + "Sign Up"(primary button #000000 bg)
```

### Iteration Guide

- **색상 변경 시**: 본문 UI는 monochrome 유지. 채도는 오직 info chip, 차트, hero art에만 허용.
- **폰트 변경 시**: weight `400`이 기본, `500`이 button/nav, `600`이 제목, `700`이 히어로. `300` 쓰지 말 것.
- **여백 조정 시**: `--geist-space` = `4px` 배수로만 (`4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 / 128 / 192 / 256`). `13px`, `27px` 금지.
- **새 컴포넌트 추가 시**: radius는 `6 / 12 / 9999` 중 하나. shadow는 6단 scale 유지.
- **다크 모드**: `.dark-theme` class 토글로 `--ds-background-100`, `--ds-gray-*` 이 자동 반전.
- **반응형**: 600/768/960/1200 4단. mobile-first로 작성.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 `#FFFFFF`(light) 또는 `#000000`(dark). 중간 회색 surface 쓰지 말 것.
- CTA primary는 `#000000` 배경 + `#FFFFFF` 텍스트 + `border-radius: 6px` (또는 9999px pill).
- 본문은 `Geist` `16px` `weight 400`. 제목은 `weight 600-700`.
- 여백은 `4px` 배수(`--geist-space-Nx`) 시스템으로만.
- Card shadow는 `#0000001F` (약 12% 검정) 오파시티 계단으로만.
- transition은 `.15s` 단일 값 — 다른 duration 쓰지 말 것.
- 히어로 H1은 `clamp(24px, Nvw, 72px)` fluid 타이포그래피로.
- 큰 H1/H2/H3에는 반드시 negative letter-spacing (`-0.01em ~ -0.03em`) 적용.

### ❌ DON'T

- 본문 UI에 채도 색(`#0070F3`, `#FF0080`, `#7928CA` 등)을 넓게 쓰지 말 것 — 대신 `#000000`/`#FFFFFF`와 gray ramp 사용. Vercel의 정체성은 monochrome이다.
- 배경을 중간 회색 (`#F5F5F7`, `#EEEEEE` 등)으로 두지 말 것 — 대신 `#FFFFFF` 또는 `#FAFAFA` (`--ds-background-200`) 사용.
- 텍스트를 `#000000` pure black으로 넓게 쓰지 말 것 — 본문은 `#171717` (`--ds-gray-1000`). pure `#000000`은 버튼 배경/hero H1에만.
- body에 `font-weight: 300` 사용 금지 — Vercel은 `400` 기본이 맞다.
- radius `8px`, `10px` 같은 비표준 값 금지 — `6 / 12 / 9999` 중 하나.
- transition duration `.3s` 이상 금지 — Vercel은 `.15s` 고정.
- `background: #EAEAEA`(`--accents-2` light) 같은 step을 본문 text에 쓰지 말 것 — 그건 border/divider용이다.
- 히어로 H1을 고정 px(예: `60px`)로 쓰지 말 것 — `clamp(24px, Nvw, 72px)` fluid가 맞다.
- 회색 램프를 `0, 0%, X%` 외 채도 있는 HSL로 만들지 말 것 — Vercel gray는 순수 neutral이다.
- `--color-brand` 같은 가상 prefix 금지 — Vercel은 `--ds-*` (modern) 또는 `--geist-*` (legacy) 둘 중 하나.
