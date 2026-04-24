---
schema_version: 3.1
slug: linear
service_name: Linear
site_url: https://linear.app
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#5E6AD2"
primary_font: Inter Variable
font_weight_normal: 400
token_prefix: --color-*, --radius-*, --font-*

bold_direction: "Cool Productivity"
aesthetic_category: "Cool Productivity"
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Linear (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Linear의 마케팅 사이트는 소프트웨어 엔지니어링의 **고요한 집중력**을 시각적으로 번역한다. 페이지는 거의 순흑에 가까운 `#08090A`로 시작해 `#0F1011`과 `#191D20`의 레이어가 서로 겹치는 패널 구조로 전개된다. 이것은 단순한 다크 모드가 아니라, IDE와 터미널이 늘 배경에 있는 개발자의 환경 자체를 은유한다. 색은 소음이 되지 않도록 철저히 묶여 있고, 유일하게 용납된 악센트는 차가운 인디고 계열 `#5E6AD2`와 링크용 `#7170FF` 한 쌍뿐이다.

색상 전략은 **"채도를 벌어서 써라"**는 원칙으로 요약된다. 넓은 면적은 모두 neutral ink + near-black 배경이 맡고, 브랜드 인디고는 CTA 버튼 배경, focus ring, 링크 활성 상태 등 의미가 필요한 지점에만 등장한다. 서브 컬러로 teal `#00B8CC`, orange `#FF7236`, yellow `#F0BF00`, green `#27A644`, red `#F34F52`가 존재하지만 각각 status·태그·제품 라인(Build/Plan/Security) 식별에만 쓰이며 결코 면적을 차지하지 않는다. light 테마도 존재한다 — `#FFFFFF` 배경에 동일 인디고 계열 `#7070FF` — 하지만 마케팅 홈의 default는 dark다 (`<html data-theme="dark">`).

타이포그래피는 **Inter Variable**을 축으로 하되, 흔한 400/700 대신 **400·450·500·550·600·700**의 7단계를 사용해 미세한 hierarchy를 만든다. `--font-weight-medium: 510`, `--font-weight-semibold: 590` 같은 variable axis 값이 등장하는 것이 특징이며, `--font-settings: "cv01","ss03"`으로 stylistic alternate까지 활성화한다. 디스플레이용 serif로 **Tiempos Headline**을, 코드용으로는 유료 폰트 **Berkeley Mono**를 자체 호스팅한다. 기본 문단은 `0.9375rem (15px)` · `--font-size-regular` 크기로, 조금 작지만 line-height와 letter-spacing으로 정교하게 보정된다.

레이아웃은 **1024px page-max-width + 680px prose-max-width**의 좁은 칼럼 위에서 움직인다. homepage만 `1344px`까지 확장된다 (`--homepage-max-width`). 섹션 간 리듬은 `--page-padding-block: 64px`로 일정하게 유지되고, 헤더는 `65px` 고정에 `backdrop-filter: blur(20px)` glass 효과가 걸려 있다. radius는 `4/6/8/12/16/24/32/9999px`의 배수 시스템으로 설계되어 카드(12/16), 버튼(6/8), pill(9999px)이 명확히 분리된다.

인터랙션은 `.16s` duration을 기본으로 `cubic-bezier(0.25,0.46,0.45,0.94)` (out-quad) ease가 반복된다. hover transition이 느슨해지지 않도록 대부분 `.16s`, 길어도 `.2s`를 넘지 않는다. shadow는 거의 쓰지 않는 대신 `--shadow-stack-low` 같은 다층 dual-shadow 원자로 깊이를 만든다 (Stripe 동일 패턴).

### Key Characteristics

- Near-black 3단 배경 레이어 (`#08090A` / `#0F1011` / `#191D20`)
- 단일 인디고 악센트 `#5E6AD2` — neutral 위에 올려지는 유일한 채도
- Inter Variable 7-weight 계단 (400 / 450 / 500 / 550 / 600 / 700)
- 좁은 prose 칼럼 680px — 가독성 우선
- Radius는 4/6/8/12/16/24/32 배수 체계
- Glass nav: 65px fixed + backdrop-filter blur(20px)
- 16ms duration 고정 — 인터랙션이 "빠르고 조용함"
- Light/Dark 이중 팔레트 존재 — marketing default는 dark

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Cool Productivity
> **Aesthetic Category**: Cool Productivity
> **Signature Element**: 이 사이트는 **채도를 극도로 절제한 near-black 배경 위 단일 인디고 악센트와 미세 weight 계단**으로 기억된다.
> **Code Complexity**: medium — CSS variable + dual-shadow stack + 16ms transitions, 화려한 모션 없음

---

## 01. Quick Start

> 5분 안에 Linear처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter Variable", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  font-size: 0.9375rem; /* 15px — Linear의 regular body */
  font-feature-settings: "cv01","ss03";
}

/* 2. 배경 + 텍스트 (dark default) */
:root {
  --bg: #08090A;
  --fg: #F7F8F8;
  --panel: #0F1011;
  --border: #23252A;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 악센트 */
:root { --brand: #5E6AD2; --link: #7170FF; }
```

**절대 하지 말아야 할 것 하나**: 인디고 `#5E6AD2`를 넓은 면적(배경, 큰 섹션 블록)에 쓰지 마라. Linear의 브랜드는 "인디고가 아니라 neutral 위에 인디고를 **한 점** 올리는 규율"이다. 면적으로 쓰는 순간 Discord가 되고, 포인트로 쓸 때 Linear가 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://linear.app` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 2,298,398 bytes (Next.js SSR) |
| CSS files | 20개 외부, 총 약 500KB minified |
| Token prefix | `--color-*`, `--radius-*`, `--font-*` (DS prefix 없음) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (SSR, React 18)
- **Design system**: 자체 토큰 시스템 — prefix 없이 `--color-*`, `--radius-*`, `--font-*` 직접 사용
- **CSS architecture**: semantic-direct (1-tier)
  ```
  core    (--color-accent, --color-bg-primary, --radius-12)  raw hex / px 직접
  comp    (--btn-highlight-bg, --button-corner-radius)       컴포넌트 alias
  ```
- **Class naming**: CSS Modules (`HeroMultiPanelAsset_primaryPanel__HamkZ`, `Button_variant-invert__ECHZN`)
- **Default theme**: dark (`<html data-theme="dark">`, bg = `#08090A`) · light fallback 존재
- **Font loading**: 셀프 호스트 `InterVariable.woff2`, `Berkeley Mono` (유료, 자체 호스팅), `Tiempos Headline` (유료)
- **Canonical anchor**: `#5E6AD2` — `--color-brand-bg` (dark 테마), CTA 버튼 배경 핵심

---

## 04. Font Stack

- **Display font**: `Inter Variable` (오픈 소스, OFL)
- **Serif display**: `Tiempos Headline` (Klim Type Foundry, 유료 라이선스)
- **Code font**: `Berkeley Mono` (Berkeley Graphics, 유료)
- **Weight normal / bold**: `400` / `700`
- **Variable weights used**: `300 / 400 / 450 / 500 / 510 / 550 / 590 / 600 / 700`

```css
:root {
  --font-regular: "Inter Variable","SF Pro Display",-apple-system,BlinkMacSystemFont,"Segoe UI","Roboto","Oxygen","Ubuntu","Cantarell","Open Sans","Helvetica Neue",sans-serif;
  --font-serif-display: "Tiempos Headline",ui-serif,Georgia,Cambria,"Times New Roman",Times,serif;
  --font-monospace: "Berkeley Mono",ui-monospace,"SF Mono","Menlo",monospace;
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 510;
  --font-weight-semibold: 590;
  --font-weight-bold: 680;
  --font-settings: "cv01","ss03";
  --font-variations: "opsz" auto;
}
body {
  font-family: var(--font-regular);
  font-weight: var(--font-weight-normal);
  font-feature-settings: var(--font-settings);
}
```

> **라이선스 주의**: Berkeley Mono는 상업 라이선스 필수 (`berkeleygraphics.com`). 복제 시 `JetBrains Mono` 또는 `IBM Plex Mono`로 대체.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--font-size-micro` | `0.6875rem` (11px) | 400 | — | — |
| `--font-size-mini` | `0.75rem` (12px) | 400 | — | — |
| `--font-size-small` | `0.8125rem` (13px) | 400 | — | — |
| `--font-size-regular` | `0.9375rem` (15px) | 400 | — | — |
| `--font-size-large` | `1.125rem` (18px) | 450 | — | — |
| `--font-size-title3` | `1.25rem` (20px) | 510 | — | — |
| `--font-size-title2` | `1.5rem` (24px) | 590 | — | — |
| `--font-size-title1` | `2.25rem` (36px) | 680 | tight | `-0.02em` |

> ⚠️ Linear의 본문은 **15px**이 기본이다. `16px`가 아니다. 더 작은 몸집으로 더 높은 정보 밀도를 만들기 위해 `font-settings: cv01,ss03`으로 Inter의 alternate glyph까지 켠다.

---

## 06. Colors

### 06-1. Brand (Indigo, dual-theme)

| Token | Hex |
|---|---|
| `--color-brand-bg` (dark) | `#5E6AD2` |
| `--color-brand-bg` (light) | `#7070FF` |
| `--color-accent` | `#7170FF` |
| `--color-accent-hover` | `#828FFF` |
| `--color-accent-tint` (dark) | `#18182F` |
| `--color-accent-tint` (light) | `#F1F1FF` |
| `--color-link-primary` (dark) | `#828FFF` |
| `--color-link-primary` (light) | `#7070FF` |
| `--color-indigo` | `#5E6AD2` |

### 06-3. Neutral Ramp (dark / light pair)

| Step | Dark | Light |
|---|---|---|
| bg-primary | `#08090A` | `#FFFFFF` |
| bg-marketing | `#010102` | `#FFFFFF` |
| bg-panel | `#0F1011` | `#F9F8F9` |
| bg-shade | `#191D20` | `#F4F2F4` |
| bg-tint | `#141516` | `#F4F4F5` |
| border-primary | `#23252A` | `#E9E8EA` |
| border-secondary | `#2A2E33` | `#E4E2E4` |
| border-tertiary | `#37393A` | `#DCDBDD` |
| text-primary | `#F7F8F8` | `#282A30` |
| text-secondary | `#B4B8BE` | `#3C4149` |
| text-tertiary | `#8A8F98` | `#6F6E77` |
| text-quaternary | `#62666D` | `#86848D` |

### 06-4. Accent Families (product lines + status)

| Family | Hex | Use |
|---|---|---|
| `--color-teal` | `#00B8CC` | cyan highlight, Security product |
| `--color-orange` | `#FC7840` | highlight, Build feature |
| `--color-yellow` | `#F0BF00` | warning, Build tint |
| `--color-green` | `#27A644` | success, Plan product |
| `--color-red` | `#EB5757` | error, destructive |
| `--color-linear-build` | `#D4B144` | Build 제품 식별 |
| `--color-linear-plan` | `#68CC58` | Plan 제품 식별 |
| `--color-linear-security` | `#7A7FAD` | Security 제품 식별 |
| `--bar-color` | `#21B3FF` | progress bar accent |
| `--red` | `#F34F52` | alert shade |
| `--orange` | `#FF7236` | alert shade warm |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-bg-primary` | `#08090A` (dark) / `#FFFFFF` (light) | 페이지 배경 |
| `--color-text-primary` | `#F7F8F8` (dark) / `#282A30` (light) | 본문 텍스트 |
| `--color-brand-bg` | `#5E6AD2` (dark) / `#7070FF` (light) | CTA 버튼 배경 |
| `--color-brand-text` | `#FFFFFF` | CTA 버튼 텍스트 |
| `--color-border-primary` | `#23252A` (dark) / `#E9E8EA` (light) | 카드·섹션 경계 |
| `--kbd-bg` | `#3B3D45` | keyboard 배지 배경 |
| `--color-overlay-primary` | `rgba(255,255,255,0.65)` | 모달 오버레이 (dark) |

### 06-7. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#08090A` | 325 | neutral (dark bg primary) |
| 2 | `#E4E5E9` | 200 | neutral light surface |
| 3 | `#E2E4E7` | 151 | neutral surface alt |
| 4 | `#4354B8` | 124 | svg pattern (illustration) |
| 5 | `#FFFFFF` | 77 | brand-text / light bg |
| 6 | `#E5591D` | 76 | svg pattern (orange art) |
| 7 | `#8A8F98` | 71 | neutral text-tertiary |
| 8 | `#F79CE0` | 51 | svg pattern (pink art) |
| 9 | `#2E2E32` | 43 | neutral dark surface |
| 10 | `#62666D` | 35 | neutral text-quaternary |

---

## 07. Spacing

Linear는 이름 있는 spacing token보다 **page padding + radius scale + raw px**를 직접 쓴다.

| Token | Value | Use case |
|---|---|---|
| `--page-padding-inline` | `24px` | 좌우 페이지 여백 |
| `--page-padding-block` | `64px` | 상하 섹션 여백 |
| `--page-inset` | `32px` | 페이지 inner inset |
| `--page-padding-y` | `48px` | alt vertical padding |
| `--homepage-outer-padding` | `16px` | homepage 외곽 |
| `--homepage-padding-inset` | `8px` | homepage inner |
| `--page-max-width` | `1024px` | 일반 페이지 최대 폭 |
| `--homepage-max-width` | `calc(1344px + var(--homepage-outer-padding)*2)` | 홈 최대 폭 |
| `--prose-max-width` | `680px` (`--font-size-regular`) | 글 읽기 폭 |
| `--header-height` | `65px` | 고정 헤더 높이 |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `--radius-4` | `4px` | 작은 chip, inner input |
| `--radius-6` | `6px` | 버튼 (`--button-corner-radius` 기본) |
| `--radius-8` | `8px` | 카드 small, input |
| `--radius-12` | `12px` | 카드 기본 |
| `--radius-16` | `16px` | 큰 카드, 패널 |
| `--radius-24` | `24px` | 히어로 블록 |
| `--radius-32` | `32px` | 대형 포스터 |
| `--radius-rounded` | `9999px` | pill 버튼, avatar wrapper |
| `--radius-circle` | `50%` | 원형 avatar, dot |
| `--border-hairline` | `0.5px` | retina 1px 대체 |

---

## 09. Shadows

Linear는 shadow를 극도로 절제한다. `--shadow-none` 계열이 기본값이며, 깊이가 필요한 곳에만 `--shadow-stack-low` 같은 **5-layer dual-shadow 원자**가 투입된다 (Stripe 동일 패턴 — 함정 #11).

| Level | Value | Usage |
|---|---|---|
| `--shadow-none` | `0px 0px 0px transparent` | 대부분 컴포넌트의 기본값 |
| `--shadow-tiny` | `var(--shadow-none)` | 아직 미사용 slot |
| `--shadow-low` | `var(--shadow-none)` | 아직 미사용 slot |
| `--shadow-medium` | `var(--shadow-none)` | 아직 미사용 slot |
| `--shadow-high` | `var(--shadow-none)` | 아직 미사용 slot |
| `--shadow-stack-low` | `0px 8px 2px 0px rgba(0,0,0,0), 0px 5px 2px 0px rgba(0,0,0,0.01), 0px 3px 2px 0px rgba(0,0,0,0.04), 0px 1px 1px 0px rgba(0,0,0,0.07), 0px 0px 1px 0px rgba(0,0,0,0.08)` | 카드·팝오버 실사용 5-layer |

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| `--speed-quickTransition` | `.12s` | 가장 빠른 hover |
| `--speed-regularTransition` | `.16s` | 기본 transition (압도적 다수) |
| `--ease-out-quad` | `cubic-bezier(0.25,0.46,0.45,0.94)` | out 기본 |
| `--ease-out-cubic` | `cubic-bezier(0.215,0.61,0.355,1)` | out smooth |
| `--ease-out-quart` | `cubic-bezier(0.165,0.84,0.44,1)` | out 빠르게 |
| `--ease-in-out-quint` | `cubic-bezier(0.86,0,0.07,1)` | 드물게, 히어로 패널 전환 |
| `--blink-duration` | `1.2s` | 커서 깜빡임 |

> 패턴: `transition: filter .16s var(--ease-out-quad), transform .16s var(--ease-out-quad);` — duration 고정, 2-3 프로퍼티 조합.

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1024px` (`--page-max-width`) 일반 / `1344px+32px` (`--homepage-max-width`) 홈
- **Prose max-width**: `680px` (`--prose-max-width`)
- **Grid type**: CSS Grid (4-column 기본, `--grid-columns: 4`)
- **Column count**: `4` (grid-columns token)
- **Gutter**: `24px` (`--page-padding-inline`)

### Hero

- **🆕 Pattern Summary**: `~85vh + near-black 배경 + glass nav(65px fixed) + 좌측 H1 + 좌측 sub-CTA 페어 + 우측 product mockup`
- Layout: 2-column(데스크톱), 1-column(모바일). 우측 column에 `HeroMultiPanelAsset` 다층 UI 캡처
- Background: `#08090A` solid, 서브섹션에서 `linear-gradient(270deg,#09090B 0,transparent 50%)` 페이드 mask
- **🆕 Background Treatment**: `solid #08090A` + 우측 패널에 linear-gradient fade (좌측 텍스트 가독성 확보)
- H1: `~2.25rem (36px)` / weight `590~680` / tracking `-0.02em`
- Max-width: `1344px` (homepage)

### Section Rhythm

```css
section {
  padding: 64px 24px;           /* --page-padding-block --page-padding-inline */
  max-width: 1024px;            /* --page-max-width */
  margin: 0 auto;
}
```

### Card Patterns

- **Card background**: `#0F1011` (dark panel) / `#FFFFFF` (light)
- **Card border**: `1px solid #23252A` (dark) / `1px solid #E9E8EA` (light)
- **Card radius**: `12px` (`--radius-12`) 기본, 큰 것은 `16px` (`--radius-16`)
- **Card padding**: `24px` 기본, 큰 것은 `32px`
- **Card shadow**: 대부분 none, 강조 시 `--shadow-stack-low` 5-layer

### Navigation Structure

- **Type**: horizontal desktop / hamburger mobile
- **Position**: `position: fixed; top: 0`
- **Height**: `65px` (`--header-height`)
- **Background**: `rgba(255,255,255,0.8)` + `backdrop-filter: blur(20px)` (light) / `rgba(10,10,12,0.8)` (dark)
- **Border**: `1px solid rgba(0,0,0,0.08)` 하단

### Content Width

- **Prose max-width**: `680px` (--prose-max-width)
- **Container max-width**: `1024px` (--page-max-width)
- **Homepage max-width**: `1344px` (--homepage-max-width)
- **Sidebar width**: N/A — marketing 사이트엔 없음

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 640px` | 1-column, 햄버거 nav |
| Tablet | `≥ 768px` | 2-col hero, nav inline |
| Desktop | `≥ 1024px` | full page-max-width |
| Large | `≥ 1280px` | homepage 확장 구간 |
| XL | `≥ 1536px` | 초대형 — 추가 여백만 |

*모바일 퍼스트* — `min-width` 우세 (640/768/1024/1280/1536)

### Touch Targets

- **Minimum tap size**: `32px` (pill button min-height 관찰)
- **Button height (mobile)**: ≈ `36-40px`
- **Input height (mobile)**: `--input-height` alias 존재 (구체 값 토큰에 없음, 관찰상 `36px`)

### Collapsing Strategy

- **Navigation**: 1024px 이하에서 햄버거로 접힘, full-screen overlay 나타남
- **Grid columns**: `--grid-columns: 4` → 640px에서 `1`로 reset
- **Sidebar**: N/A (marketing)
- **Hero layout**: 2-column → 1-column (1024px 이하), 우측 mockup은 아래로 이동

### Image Behavior

- **Strategy**: Next.js `<Image>` lazy-load, `webassets.linear.app` CDN (`.png?w=72&q=95&auto=format`)
- **Max-width**: `100%`
- **Aspect ratio handling**: `aspect-ratio: N/M` 수동 선언 + `object-fit: cover`

---

## 13. Components

### Buttons

Linear의 버튼은 `Button_variant-*` CSS module 네이밍 + `--button-*` alias 세트로 정의된다.

```html
<button class="Button_variant-primary__xxx">Get started</button>
<button class="Button_variant-secondary__xxx">Learn more</button>
<button class="Button_variant-invert__xxx">Documentation</button>
```

| Variant | background | color | border-radius | padding | hover |
|---|---|---|---|---|---|
| primary (dark) | `#5E6AD2` | `#FFFFFF` | `6px` | `0 14px; height 32-36px` | `filter: brightness(1.08)` |
| secondary (dark) | `transparent` | `#F7F8F8` | `6px` | 동일 | `background: #1F2024` |
| invert (dark) | `#282A30` (`--color-button-invert-bg`) | `#F7F8F8` | `6px` | 동일 | `#1F2024` |
| pill | 좌동 | 좌동 | `9999px` (`--radius-rounded`) | 동일 | 좌동 |

### Badges / Keyboard keys

```html
<kbd class="kbd">⌘K</kbd>
```

- `background: #3B3D45` (`--kbd-bg`)
- `color: #F7F8F8`
- `border-radius: 4px`
- `font-family: var(--font-monospace)`
- `font-size: 12px`
- padding: `2px 6px`

### Cards & Containers

```html
<article class="card HeroMultiPanelAsset_primaryPanel__x">…</article>
```

- bg: `#0F1011` (dark) / `#FFFFFF` (light)
- border: `1px solid #23252A` (dark) / `1px solid #E9E8EA` (light)
- radius: `12px` 기본 / `16px` 큰 카드
- padding: `24px` / `32px`
- shadow: 기본 none, hover 시 5-layer stack
- hover: `border-color: #2A2E33` (미묘), transition `.16s`

### Navigation

- 로고: 좌측, Inter weight 510 wordmark
- 링크: `Inter Variable` 14px weight 400, color `--color-fg-secondary` = `#3C4149` (light) / `#B4B8BE` (dark 추정)
- Active: weight `510`, color `--color-text-primary`
- CTA: 우측 페어 (Log in 텍스트 + Sign up pill)
- Height: `65px` fixed, backdrop-filter blur
- 모바일: 햄버거 → full-screen drawer

### Inputs & Forms

- height: `36px` 관찰 (토큰화 안됨)
- padding: `0 12px`
- border: `1px solid #E9E8EA` (light) / `#23252A` (dark)
- radius: `6px` (`--radius-6`)
- focus: `outline: 2px solid #7170FF; outline-offset: 1px` 또는 `box-shadow: 0 0 0 3px rgba(94,106,210,0.25)`
- placeholder: `color: #86848D` (text-quaternary)

### Hero Section

- 배경: `#08090A` solid, 하단 섹션으로 내려가며 자연 transition
- 좌측 상단 small-cap eyebrow → H1 (36px, weight 680) → sub (15-18px, text-secondary) → 듀얼 CTA (primary indigo + secondary transparent)
- 우측 product mockup: 실제 Linear 앱 screenshot (WebP), radius 12-16px, 다층 패널 (`HeroMultiPanelAsset`)

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 짧은 선언, 주어-동사 | "Linear is a purpose-built tool for planning and building products" |
| Primary CTA | 2단어, 동사+대상 | "Get started" / "Start building" |
| Secondary CTA | 관찰형 | "See what's new" |
| Subheading | 기능 묘사 1문장 | "Meet the system for modern software development." |
| Tone | 조용한 확신, 과장 지양 — 엔지니어 화법 | — |

---

## 15. Drop-in CSS

```css
/* Linear — copy into your root stylesheet */
:root {
  /* Fonts */
  --ln-font-family: "Inter Variable","SF Pro Display",-apple-system,BlinkMacSystemFont,"Segoe UI","Roboto",sans-serif;
  --ln-font-family-code: "Berkeley Mono",ui-monospace,"SF Mono","Menlo",monospace;
  --ln-font-weight-normal: 400;
  --ln-font-weight-medium: 510;
  --ln-font-weight-semibold: 590;
  --ln-font-weight-bold: 680;
  --ln-font-settings: "cv01","ss03";

  /* Brand */
  --ln-color-brand:          #5E6AD2;   /* canonical anchor */
  --ln-color-accent:         #7170FF;
  --ln-color-accent-hover:   #828FFF;
  --ln-color-accent-tint:    #18182F;
  --ln-color-link:           #7170FF;

  /* Surfaces (dark default) */
  --ln-bg-page:   #08090A;
  --ln-bg-panel:  #0F1011;
  --ln-bg-shade:  #191D20;
  --ln-text:      #F7F8F8;
  --ln-text-muted:#8A8F98;
  --ln-border:    #23252A;

  /* Key spacing */
  --ln-space-sm:  24px;   /* page-padding-inline */
  --ln-space-md:  32px;   /* page-inset */
  --ln-space-lg:  64px;   /* page-padding-block */

  /* Radius */
  --ln-radius-sm: 6px;    /* button */
  --ln-radius-md: 12px;   /* card */
  --ln-radius-lg: 16px;   /* large card */
  --ln-radius-pill: 9999px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Linear
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#5E6AD2',
          light:   '#7070FF',
          accent:  '#7170FF',
          hover:   '#828FFF',
          tint:    '#18182F',
        },
        neutral: {
          page:    '#08090A',
          panel:   '#0F1011',
          shade:   '#191D20',
          border:  '#23252A',
          text:    '#F7F8F8',
          muted:   '#8A8F98',
        },
      },
      fontFamily: {
        sans: ['Inter Variable', 'SF Pro Display', 'system-ui'],
        mono: ['Berkeley Mono', 'ui-monospace'],
      },
      fontWeight: {
        normal:    '400',
        medium:    '510',
        semibold:  '590',
        bold:      '680',
      },
      borderRadius: {
        sm:   '4px',
        DEFAULT: '6px',
        md:   '8px',
        lg:   '12px',
        xl:   '16px',
        '2xl':'24px',
        pill: '9999px',
      },
      boxShadow: {
        stack: '0px 8px 2px 0px rgba(0,0,0,0),0px 5px 2px 0px rgba(0,0,0,0.01),0px 3px 2px 0px rgba(0,0,0,0.04),0px 1px 1px 0px rgba(0,0,0,0.07),0px 0px 1px 0px rgba(0,0,0,0.08)',
      },
      transitionDuration: {
        DEFAULT: '160ms',
        quick:   '120ms',
      },
      transitionTimingFunction: {
        'out-quad':  'cubic-bezier(0.25,0.46,0.45,0.94)',
        'out-cubic': 'cubic-bezier(0.215,0.61,0.355,1)',
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
| Brand primary | `--ln-color-brand` | `#5E6AD2` |
| Background | `--ln-bg-page` | `#08090A` |
| Text primary | `--ln-text` | `#F7F8F8` |
| Text muted | `--ln-text-muted` | `#8A8F98` |
| Border | `--ln-border` | `#23252A` |
| Success | `--color-green` | `#27A644` |
| Error | `--color-red` | `#EB5757` |

### Example Component Prompts

#### Hero Section

```
Linear 스타일 히어로 섹션을 만들어줘.
- 배경: #08090A (near-black, solid)
- H1: Inter Variable, 2.25rem (36px), weight 680, tracking -0.02em, color #F7F8F8
- 서브텍스트: 1rem, color #8A8F98, line-height 1.5
- CTA primary: 배경 #5E6AD2, 텍스트 #FFFFFF, radius 6px, padding 0 14px, height 36px, font-weight 510
- CTA secondary: transparent + color #F7F8F8 + border 1px solid #23252A, 동일 radius
- 최대 너비: 1344px (homepage)
- 좌측 2/3 텍스트 + 우측 1/3 product mockup(webp, radius 12px)
```

#### Card Component

```
Linear 스타일 카드 컴포넌트를 만들어줘.
- 배경: #0F1011 (dark panel), border 1px solid #23252A, radius 12px
- padding: 24px
- shadow: none (기본), hover 시 --shadow-stack-low 5-layer
- hover: border-color #2A2E33, transition .16s cubic-bezier(0.25,0.46,0.45,0.94)
- 제목: Inter Variable, 18px, weight 590, color #F7F8F8
- 본문: 15px, color #B4B8BE, line-height 1.6
```

#### Badge / Kbd

```
Linear 스타일 ⌘K 키 배지를 만들어줘.
- font: Berkeley Mono (fallback monospace), 12px, weight 500
- padding: 2px 6px, radius 4px
- 기본: bg #3B3D45, color #F7F8F8
```

#### Navigation

```
Linear 스타일 상단 네비게이션을 만들어줘.
- 높이: 65px, position fixed, top 0, width 100%
- 배경: rgba(10,10,12,0.8), backdrop-filter blur(20px), 하단 border 1px solid #23252A
- 로고: 좌측, Inter Variable 14px weight 510
- 링크: Inter Variable 14px weight 400, color #B4B8BE, hover color #F7F8F8
- 활성 링크: color #F7F8F8, weight 510
- CTA 우측 페어: "Log in"(text link) + "Sign up"(pill, background #FFFFFF, color #08090A, radius 9999px)
```

### Iteration Guide

- **색상 변경 시**: `--color-*` semantic token만 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight `400`이 기본. `510 / 590 / 680` 3단계로만 계단 구성. 500/600/700 쓰지 말 것.
- **여백 조정 시**: `page-padding-inline 24px` + `page-padding-block 64px` 시스템을 유지. 임의 여백 금지.
- **새 컴포넌트 추가 시**: radius는 `4/6/8/12/16/24/32` 중 하나에서만 선택.
- **다크 모드**: light 토큰에 opacity 얹지 말 것 — 별도 dark variant 값 (`--color-bg-primary` 등)이 이미 정의되어 있음.
- **반응형**: 640/768/1024/1280/1536 5단. 커스텀 브레이크포인트 추가 금지.
- **transition**: `.16s` + `cubic-bezier(0.25,0.46,0.45,0.94)`이 기본. 300ms 이상 쓰지 말 것.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 `#08090A`로 (dark) 또는 `#FFFFFF`(light)로. 둘 중 하나 — 중간 회색 쓰지 말 것.
- CTA는 `#5E6AD2` 배경 + `#FFFFFF` 텍스트 + `border-radius: 6px`.
- 본문은 `Inter Variable` `15px (0.9375rem)` `weight 400`.
- Card radius는 `12px` 또는 `16px` 둘 중 하나만.
- Navigation에 `backdrop-filter: blur(20px)` 적용.
- transition은 `.16s cubic-bezier(0.25,0.46,0.45,0.94)` 고정.
- Weight는 `400 / 510 / 590 / 680` 4단계로만 (일반 500/600/700 쓰지 말 것).

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 (dark 기본일 때) — 대신 `#08090A` 사용. Linear 기본은 dark 테마다.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#282A30` (light) / `#F7F8F8` (dark) 사용.
- 브랜드 인디고 `#5E6AD2`를 넓은 배경에 쓰지 말 것 — 포인트(CTA, focus, link)에만.
- body에 `font-weight: 500` 또는 `600` 사용 금지 — Linear는 `510 / 590`이 맞다.
- 폰트를 `Inter` (비-variable)로 대체하지 말 것 — `Inter Variable`의 variable axis (weight 510, 590, 680)를 쓸 수 없다.
- radius `10px` 같은 비표준 값 금지 — `4 / 6 / 8 / 12 / 16 / 24 / 32` 중 하나.
- transition duration `.3s` 이상 금지 — Linear는 `.16s` 고정.
- `box-shadow: 0 2px 4px rgba(0,0,0,0.1)` 같은 단층 shadow 금지 — `--shadow-stack-low` 5-layer를 써라 (함정 #11).
- `--color-brand` 같은 가상 prefix 금지 — Linear는 prefix 없이 `--color-*` 직접 사용.
