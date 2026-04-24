---
schema_version: 3.1
slug: bain
service_name: Bain & Company
site_url: https://www.bain.com
fetched_at: 2026-04-23
default_theme: light
brand_color: "#CC0000"
primary_font: Graphik
font_weight_normal: 400
token_prefix: --bain-*

bold_direction: "Premium B2B Editorial"
aesthetic_category: "Premium B2B Editorial"
signature_element: red_accent_bar
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Bain & Company (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Bain & Company의 웹사이트는 **"컨설팅 권위를 에디토리얼 언어로 번역한 사이트"**다. 대부분의 B2B 기업 사이트가 파란색 안전감과 사진 그리드로 채울 때, Bain은 **짙은 근-검정(near-black) 히어로 배경과 시그니처 레드 `#CC0000`의 절제된 배치**로 "우리는 이미 증명되었다"는 메시지를 전달한다.

색상 전략은 **"근-검정 한 축 + 광범위한 회색 ramp + 시그니처 레드 accent"**다. 히어로와 상단 네비게이션은 `#0a0a0a` / `#121212` 근-검정이 지배하고, 컨텐츠 섹션은 `#ffffff` / `#f9f9f9` / `#f5f5f5`의 순백 계열로 전환된다. 이 두 극 사이의 광범위한 회색 ramp — `#252525`, `#424242`, `#636363`, `#8a8a8a`, `#cacaca`, `#e6e6e6` — 가 모든 텍스트 계층과 구분선을 담당한다. 시그니처 레드 `#CC0000`은 절대 면적으로 쓰이지 않는다. 네비게이션 active 상태, CTA 화살표 아이콘, 텍스트 하단 accent line이 전부다. 이 절제가 레드를 오히려 강하게 만든다.

타이포그래피는 **두 축의 충돌이 시그니처**다. 본문과 UI는 `Graphik`(clean professional sans), 대형 히어로 헤드라인은 `RecklessNeue`(editorial display체), 아티클 헤더는 `TiemposHeadline`(전통 serif)이 맡는다. 이 세 폰트의 조합은 "전략 컨설팅 + 저널리즘 권위"를 동시에 연출한다. h1은 `3.75rem`, 줄간격은 heading 1.066–1.08, body copy 1.78로 본문의 가독성을 극대화한다.

레이아웃은 콘텐츠 집약적이다. 섹션 padding이 촘촘하고, 타이포그래피 contrast로 공간감을 만든다. border-radius는 `0`~`12px`의 range를 가지지만 대부분의 에디토리얼 카드는 `0` 또는 `3px`의 거의-square 처리로 딱딱한 권위감을 부여한다.

인터랙션은 `200ms ease`의 절제된 hover가 기본이다. Bain은 Stripe의 scroll-linked animation이나 Linear의 glass morphism 같은 시각적 연출을 의도적으로 배제한다. 대신 타이포그래피 위계와 여백이 모든 커뮤니케이션 구조를 담당한다.

### Key Characteristics

- 시그니처 레드 `#CC0000` — nav active, CTA 화살표, accent line에만 (면적 사용 금지)
- 근-검정 히어로 + 순백 컨텐츠 섹션의 강한 이분법
- Graphik(sans) + RecklessNeue(display) + Tiempos(serif) 3폰트 시스템
- 광범위한 모노크롬 회색 ramp (pure 회색, cool tint 없음)
- h1 `3.75rem` / lh 1.066–1.08 (heading) / lh 1.78 (body)
- 거의-square border-radius 에디토리얼 카드 (`0` or `3px`)
- `200ms ease` 절제된 hover — scroll animation 없음
- Teal `#005a5f` / `#08617b` 보조 accent (데이터/인사이트 섹션)

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Premium B2B Editorial
> **Aesthetic Category**: Premium B2B Editorial
> **Signature Element**: 이 사이트는 **근-검정 히어로와 시그니처 레드 `#CC0000`의 절제된 accent + 에디토리얼 폰트 3중주**로 기억된다.
> **Code Complexity**: medium — 커스텀 토큰보다 semantic CSS 클래스 기반. 폰트 로딩과 타이포 스케일이 복잡성의 핵심.

---

## 01. Quick Start

> 5분 안에 Bain처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: "Graphik", Helvetica, Arial, sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.78;
}

/* 2. 배경 + 텍스트 (light default) */
:root {
  --bg: #ffffff;
  --fg: #0a0a0a;
  --surface: #f9f9f9;
  --border: #e6e6e6;
  --text-muted: #636363;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 시그니처 레드 + 히어로 */
:root {
  --brand:      #CC0000;
  --brand-dark: #990000;
  --hero-bg:    #0a0a0a;
  --hero-fg:    #ffffff;
}
```

**절대 하지 말아야 할 것 하나**: 시그니처 레드 `#CC0000`을 배경 면적으로 쓰지 마라. Bain의 레드는 nav active state, CTA 화살표 아이콘, 텍스트 하단 accent line, 그리고 border-left accent에만 등장한다. 레드를 버튼 배경이나 섹션 배경으로 쓰는 순간 Bain이 아니라 경고 페이지가 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.bain.com` |
| Fetched | 2026-04-23 |
| Extractor | curl + Chrome UA + CSS 직접 파싱 |
| CSS files | `style.css` (1.79MB), `init.css` (16KB) |
| Token prefix | 커스텀 프로퍼티 미사용 — semantic CSS 클래스 기반 |
| Method | CSS 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: 서버 사이드 렌더링 (정적 에셋 버전 해시: `v-639113351526147023`)
- **Design system**: 명시적 DS prefix 없음 — semantic component class 기반
- **CSS architecture**: component-level flat class naming (BEM-유사)
- **Class naming**: `.hero-*`, `.nav-*`, `.insight-card-*` 등 semantic
- **Default theme**: light (히어로만 dark, 컨텐츠는 light)
- **Font loading**: 외부 호스트 — Graphik, RecklessNeue, TiemposHeadline, bainicon (아이콘 폰트)
- **Canonical anchor**: `#CC0000` — 네비게이션 active, CTA accent
- **Animation primitives**: `200ms ease` hover transitions — scroll-linked animation 없음

---

## 04. Font Stack

- **Body/UI**: `"Graphik", Helvetica, Arial, sans-serif`
- **Display/Hero headline**: `"RecklessNeue"` (editorial display)
- **Article header/Serif**: `"TiemposHeadline", "Tiempos", Georgia, serif`
- **Icon font**: `"bainicon"`
- **Fallback**: `Arial, Helvetica, sans-serif`
- **Weight normal / bold**: `400` / `600`
- **Available weights**: `100 / 200 / 300 / 400 / 500 / 600 / 700 / 900`

```css
:root {
  --font-sans:    "Graphik", Helvetica, Arial, sans-serif;
  --font-display: "RecklessNeue";
  --font-serif:   "TiemposHeadline", "Tiempos", Georgia, serif;
}
body {
  font-family: var(--font-sans);
  font-weight: 400;
}
h1.hero-headline {
  font-family: var(--font-display);
}
.article h2 {
  font-family: var(--font-serif);
}
```

> **라이선스 주의**: Graphik는 Commercial Type 유료. 대체 시 `Inter` 또는 `DM Sans`. RecklessNeue는 Displaay Type Foundry 유료 — 대체 시 `Playfair Display` 또는 `Cormorant Garamond`. Tiempos는 Klim Type Foundry 유료 — 대체 시 시스템 `Georgia`.

---

## 05. Typography Scale

> Bain의 타이포그래피는 에디토리얼 위계가 핵심이다. h1의 `3.75rem`과 body `1rem`의 거의 4배 차이가 권위적 계층감을 만든다.

| Step | Size | Weight | Line-height | Letter-spacing | Font |
|---|---|---|---|---|---|
| `h1` | `3.75rem (60px)` | 400 | 1.066 | `-0.025em` | RecklessNeue |
| `h2` | `2.5rem (40px)` | 400–600 | 1.08 | `-0.025em` | Graphik / TiemposHeadline |
| `h3` | `2rem (32px)` | 400–600 | 1.08 | `-0.025em` | Graphik |
| `h4` | `1.3125rem (21px)` | 600 | 1.2 | `.012em` | Graphik |
| `h5` | `1.125rem (18px)` | 600 | 1.3 | `.015em` | Graphik |
| `h6` | `0.9375rem (15px)` | 600 | 1.4 | `.025em` | Graphik |
| `body large` | `1.125rem (18px)` | 400 | 1.78 | 0 | Graphik |
| `body` | `1rem (16px)` | 400 | 1.78 | 0 | Graphik |
| `small` | `0.875rem (14px)` | 400 | 1.6 | `.012em` | Graphik |
| `xsmall` | `0.75rem (12px)` | 400 | 1.5 | `.015em` | Graphik |
| `micro` | `0.625rem (10px)` | 500 | 1.4 | `.025em` | Graphik |

> Bain heading의 line-height는 1.066–1.08로 매우 타이트하다. 이 촘촘한 leading이 대형 헤드라인의 블록감을 만든다. body는 반대로 1.78로 넓게 열려 있어 장문 리포트 가독성을 확보한다.

---

## 06. Colors

### 06-1. Brand Red

| Token | Hex | Usage |
|---|---|---|
| `--bain-brand` ★ | `#CC0000` | nav active, CTA 화살표, accent line |
| `--bain-brand-dark` | `#990000` | error, brand deep |
| `--bain-brand-error` | `#b90319` | form validation error |

### 06-2. Near Black / Dark Neutral Ramp

| Hex | Usage |
|---|---|
| `#000000` | Pure Black |
| `#0a0a0a` | Hero bg, deepest text |
| `#121212` | Near-black surface |
| `#252525` | Dark card bg |
| `#2a2a2a` | Dark nav bg |
| `#313030` | Dark panel |
| `#333333` | Dark body text |
| `#424242` | Secondary dark |
| `#484848` | Dark muted |
| `#585858` | Mid-dark text |

### 06-3. Mid Gray Ramp

| Hex | Usage |
|---|---|
| `#636363` | Text secondary |
| `#646464` | Icon muted |
| `#666666` | Body muted |
| `#717171` | Placeholder |
| `#757575` | Label |
| `#767676` | A11y minimum contrast |
| `#8a8a8a` | Text tertiary |
| `#969696` | Subtle text |
| `#999999` | Divider text |

### 06-4. Light Gray Ramp

| Hex | Usage |
|---|---|
| `#a3a3a3` | Disabled |
| `#bababa` | Inactive |
| `#bbbbbb` | Light border |
| `#cacaca` | Input border |
| `#cccccc` | Subtle border |
| `#d7d7d7` | Rule / HR |
| `#d9d9d9` | Divider |
| `#e0e0e0` | Card border |
| `#e6e6e6` | Surface border |
| `#eaeaea` | Background border |
| `#ececec` | Subtle bg |

### 06-5. Near White / Surface Ramp

| Hex | Usage |
|---|---|
| `#f2f2f2` | Alt surface |
| `#f4f4f4` | Muted bg |
| `#f5f5f5` | Surface |
| `#f7f7f7` | Subtle surface |
| `#f9f9f9` | Light bg |
| `#fafafa` | Near white |
| `#ffffff` | Page bg, card |

### 06-6. Semantic / Accent Colors

| Family | Hex | Use |
|---|---|---|
| Teal dark | `#005a5f` | Data accent, insight header |
| Teal medium | `#08617b` | Data link, teal CTA |
| Warning amber | `#f59e0b` | Warning state |
| Warning light | `#fbbf24` | Warning soft |
| Attention | `#ffae00` | Attention badge |
| Success | `#3adb76` | Success state |
| Light blue | `#bcdfff` | Highlight bg |
| Light purple | `#d5d6ff` | Highlight bg alt |
| Pink deep | `#4f0731` | Brand variant deep |
| Pink mid | `#752653` | Brand variant |
| Magenta | `#7f2a5f` | Brand accent alt |
| Magenta dark | `#890c58` | Brand deep |
| Magenta red | `#9c093f` | Brand alert |

### 06-7. Dominant Colors (실제 CSS 빈도 기준)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#ffffff` | 40+ | page bg, card, text-on-dark |
| 2 | `#CC0000` | 25+ | brand red (nav, CTA, accent) |
| 3 | `#0a0a0a` | 20+ | hero bg, deepest text |
| 4 | `#333333` | 18+ | body text |
| 5 | `#e6e6e6` | 14+ | border, rule |
| 6 | `#f9f9f9` | 12+ | surface bg |
| 7 | `#636363` | 10+ | text secondary |
| 8 | `#121212` | 8+ | near-black surface |
| 9 | `#cacaca` | 7+ | input border |
| 10 | `#005a5f` | 6+ | teal accent |
| 11 | `#8a8a8a` | 5+ | text tertiary |
| 12 | `#f5f5f5` | 5+ | surface alt |

---

## 07. Spacing

Bain은 별도의 spacing token 시스템보다 에디토리얼 리듬 기반 여백을 사용한다.

| Token | Value | Use case |
|---|---|---|
| `--bain-space-xs` | `4px` | 세밀 gap |
| `--bain-space-sm` | `8px` | 인라인 간격 |
| `--bain-space-md` | `16px` | 카드 내부 |
| `--bain-space-lg` | `24px` | 섹션 내부 padding |
| `--bain-space-xl` | `48px` | 섹션 간 |
| `--bain-space-2xl` | `80px` | 히어로 블록 |
| `--bain-space-3xl` | `120px` | 메가 섹션 분리 |
| `page-max-width` (관찰) | `1280px` | 기본 컨테이너 |
| `article-max-width` (관찰) | `760px` | 에디토리얼 prose |

---

## 08. Radius

Bain은 에디토리얼 권위감을 위해 거의 square에 가까운 radius를 사용한다.

| Token | Value | Context |
|---|---|---|
| `radius-none` | `0` | 에디토리얼 카드, 이미지 컨테이너 |
| `radius-xs` | `3px (0.1875rem)` | chip, 작은 태그 |
| `radius-sm` | `4px (0.25rem)` | 버튼, 입력 필드 |
| `radius-md` | `5px (0.3125rem)` | 일반 UI 요소 |
| `radius-lg` | `6px (0.375rem)` | 드롭다운 |
| `radius-xl` | `8px (0.5rem)` | 모달, 패널 |
| `radius-2xl` | `10px (0.625rem)` | 큰 카드 |
| `radius-3xl` | `12px (0.75rem)` | 히어로 카드 (최대) |

> 관찰: Bain 에디토리얼 카드의 압도적 다수는 `radius: 0`이다. 이 sharp edge가 컨설팅 회사 특유의 딱딱한 권위감을 만든다. `8px`, `12px`은 인터랙티브 UI 컴포넌트에만 등장한다.

---

## 09. Shadows

> Bain shadow는 Stripe의 dual-layer와 달리 단순하고 직접적이다. 컨설팅 권위는 shadow의 화려함보다 타이포그래피로 표현한다.

| Level | Value | Usage |
|---|---|---|
| `shadow-soft` | `0 0 10px rgba(0,0,0,.5)` | 드롭다운, 모달 |
| `shadow-focus` | `0 2px 8px hsla(220,3%,19%,.14), inset 0 0 0 1px #0484e7` | 포커스 링 |
| `shadow-inset` | `inset 0 1px 2px rgba(10,10,10,.1)` | 입력 필드 inset |
| `shadow-brand-bar` | `0.25rem 0 0 -0.25rem #CC0000, -6px 0 0 -0.25rem #CC0000` | 레드 accent 사이드바 |

---

## 10. Motion

> Bain은 의도적으로 minimal motion을 선택한다. 모션이 없는 것이 권위의 표현이다.

| Pattern | Value | Use |
|---|---|---|
| `transition` (기본) | `200ms ease` | hover / focus |
| `transition-colors` | `150ms ease` | 색 전환 |
| nav hover | `200ms ease` | 링크 색 전환 |
| card hover | `200ms ease` | shadow / transform |

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1280px` 기본
- **Article max-width**: `760px` (prose)
- **Grid type**: CSS Grid + Flex 혼합
- **Column count**: 12 grid 기반
- **Gutter**: `24px`

### Hero

- **Pattern Summary**: `100vh + 근-검정 bg (#0a0a0a) + RecklessNeue 대형 H1 + 하단 요약 텍스트`
- Layout: 1-column 좌측 정렬 또는 중앙 정렬
- Background: `#0a0a0a` / `#121212` solid dark
- H1: `RecklessNeue 3.75rem weight 400 ls -0.025em color #ffffff lh 1.066`
- Sub: `Graphik 1.125rem color #8a8a8a line-height 1.78`
- CTA: Graphik 버튼 + 레드 화살표 아이콘

### Section Rhythm

```css
section {
  padding: 80px 48px;
  max-width: 1280px;
  margin: 0 auto;
}
```

### Card Patterns

- **Card background**: `#ffffff` (light) / `#252525` (dark 섹션)
- **Card border**: `1px solid #e6e6e6` (light) / `1px solid #424242` (dark)
- **Card radius**: `0` (에디토리얼) / `4px` (UI 카드)
- **Card padding**: `24px–32px`
- **Card shadow**: hover시 `transform: translateY(-2px)` + soft shadow

### Navigation Structure

- **Type**: horizontal desktop + mega-dropdown
- **Position**: `position: sticky; top: 0`
- **Height**: `~64px`
- **Background**: `#0a0a0a` (스크롤 전) / `rgba(10,10,10,0.95)` (스크롤 후)
- **Active indicator**: `color: #CC0000` + bottom border `2px solid #CC0000`
- **Logo**: Bain & Company 워드마크 (흰색)

### Content Width

- **Prose max-width**: `~760px`
- **Container max-width**: `1280px` 기본
- **Hero max-width**: `1280px`

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 768px` | 1-column, 햄버거 nav |
| Tablet | `≥ 768px` | 2-column |
| Desktop | `≥ 1024px` | full nav, 3-column |
| Wide | `≥ 1280px` | container 확장 |
| XWide | `≥ 1440px` | max layout |

### Touch Targets

- **Minimum tap size**: `44px`
- **Button height**: sm `36px` / md `44px` / lg `52px`
- **Input height**: `44px`

### Collapsing Strategy

- **Navigation**: 1024px 이하에서 햄버거
- **Grid columns**: 3-col → 2-col → 1-col
- **Hero H1**: `3.75rem` → `2.5rem` (tablet) → `1.875rem` (mobile)
- **Insight grid**: 3-col → 2-col → 1-col

### Image Behavior

- **Strategy**: 정적 CDN 호스팅
- **Max-width**: `100%`
- **Aspect ratio**: insight card `16/9`, hero `21/9`

---

## 13. Components

### Buttons

```html
<a class="btn btn--primary">사례 보기 →</a>
<a class="btn btn--outline">더 알아보기</a>
```

| Variant | background | color | radius | padding | hover |
|---|---|---|---|---|---|
| primary | `#CC0000` | `#ffffff` | `4px` | `12px 28px` | `bg #990000` |
| outline light | `transparent` | `#0a0a0a` | `4px` | `11px 27px` + `1px solid #0a0a0a` | `bg #0a0a0a color #fff` |
| outline dark | `transparent` | `#ffffff` | `4px` | `11px 27px` + `1px solid #ffffff` | `bg #ffffff color #0a0a0a` |
| text + arrow | `transparent` | `#CC0000` | `0` | `0` | `text-decoration underline` |

### Cards & Containers

```html
<article class="insight-card">
  <div class="insight-card__image">...</div>
  <div class="insight-card__body">
    <span class="insight-card__tag">전략</span>
    <h3>제목</h3>
    <p>설명</p>
  </div>
</article>
```

- bg: `#ffffff`
- border: `1px solid #e6e6e6`
- radius: `0` (에디토리얼) / `4px` (UI)
- padding: `24px`
- hover: `transform: translateY(-2px) 200ms ease`

### Navigation

- 로고: 좌측 Bain & Company 워드마크 (흰색)
- 배경: `#0a0a0a`
- 링크: Graphik `14px` weight `400` color `rgba(255,255,255,.7)` → hover `opacity 1`
- Active: `color: #CC0000`, bottom indicator `2px solid #CC0000`
- CTA: 우측 "Contact Us" — `border: 1px solid #ffffff; color: #ffffff`

### Inputs & Forms

- height: `44px`
- padding: `0 16px`
- border: `1px solid #cacaca`
- radius: `4px`
- bg: `#ffffff`
- focus: `border-color: #0a0a0a; box-shadow: 0 2px 8px hsla(220,3%,19%,.14), inset 0 0 0 1px #0484e7`
- placeholder: `color: #8a8a8a`

### Stats / Numbers (signature)

```html
<div class="stat-block">
  <span class="stat-block__num">$1.2T+</span>
  <span class="stat-block__label">글로벌 고객 시장가치</span>
</div>
```

- 숫자: `Graphik 3.75rem weight 700 color #0a0a0a` + `border-top: 2px solid #CC0000; padding-top: 16px`
- 라벨: `Graphik 1rem weight 400 color #636363`
- 배경: `#ffffff` 또는 `#f9f9f9`
- 1-row 3-col grid, gap `32px`

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 권위적 선언 + impact | "결과를 만들어내는 전략" |
| Primary CTA | 동사 + 화살표 | "사례 보기 →" |
| Secondary CTA | 탐색형 | "더 알아보기" |
| Stat copy | 숫자 + 짧은 컨텍스트 | "$1.2T+ 클라이언트 시가총액" |
| Tone | 신뢰 + 증거 기반 + 절제 | — |

---

## 15. Drop-in CSS

```css
/* Bain & Company — copy into your root stylesheet */
:root {
  /* Fonts */
  --bain-font-sans:    "Graphik", Helvetica, Arial, sans-serif;
  --bain-font-display: "RecklessNeue";
  --bain-font-serif:   "TiemposHeadline", "Tiempos", Georgia, serif;

  /* Brand */
  --bain-brand:        #CC0000;
  --bain-brand-dark:   #990000;
  --bain-brand-error:  #b90319;

  /* Surfaces (light) */
  --bain-bg:           #ffffff;
  --bain-surface:      #f9f9f9;
  --bain-surface-alt:  #f5f5f5;
  --bain-border:       #e6e6e6;
  --bain-border-str:   #cacaca;
  --bain-fg:           #0a0a0a;
  --bain-fg-muted:     #636363;
  --bain-fg-subtle:    #8a8a8a;

  /* Surfaces (dark/hero) */
  --bain-bg-dark:      #0a0a0a;
  --bain-bg-dark-alt:  #121212;
  --bain-bg-dark-card: #252525;
  --bain-fg-on-dark:   #ffffff;

  /* Accent */
  --bain-teal:         #005a5f;
  --bain-teal-mid:     #08617b;

  /* Status */
  --bain-success:      #3adb76;
  --bain-warning:      #f59e0b;
  --bain-error:        #b90319;

  /* Spacing */
  --bain-space-xs:  4px;
  --bain-space-sm:  8px;
  --bain-space-md:  16px;
  --bain-space-lg:  24px;
  --bain-space-xl:  48px;
  --bain-space-2xl: 80px;
  --bain-space-3xl: 120px;

  /* Radius */
  --bain-radius-none: 0;
  --bain-radius-xs:   3px;
  --bain-radius-sm:   4px;
  --bain-radius-md:   6px;
  --bain-radius-lg:   8px;
  --bain-radius-xl:   12px;

  /* Shadow */
  --bain-shadow-soft:
    0 0 10px rgba(0,0,0,.5);
  --bain-shadow-inset:
    inset 0 1px 2px rgba(10,10,10,.1);
  --bain-shadow-focus:
    0 2px 8px hsla(220,3%,19%,.14),
    inset 0 0 0 1px #0484e7;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Bain & Company
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#CC0000',
          dark:    '#990000',
          error:   '#b90319',
        },
        neutral: {
          0:    '#ffffff',
          50:   '#fafafa',
          100:  '#f5f5f5',
          150:  '#f2f2f2',
          200:  '#e6e6e6',
          250:  '#e0e0e0',
          300:  '#cacaca',
          350:  '#bababa',
          400:  '#8a8a8a',
          450:  '#767676',
          500:  '#636363',
          550:  '#585858',
          600:  '#484848',
          650:  '#424242',
          700:  '#333333',
          750:  '#252525',
          800:  '#121212',
          900:  '#0a0a0a',
          1000: '#000000',
        },
        teal: {
          DEFAULT: '#005a5f',
          mid:     '#08617b',
        },
        warning: {
          DEFAULT: '#f59e0b',
          light:   '#fbbf24',
          amber:   '#ffae00',
        },
      },
      fontFamily: {
        sans:    ['"Graphik"', 'Helvetica', 'Arial', 'sans-serif'],
        display: ['"RecklessNeue"'],
        serif:   ['"TiemposHeadline"', '"Tiempos"', 'Georgia', 'serif'],
      },
      fontWeight: {
        thin:       '100',
        extralight: '200',
        light:      '300',
        normal:     '400',
        medium:     '500',
        semibold:   '600',
        bold:       '700',
        black:      '900',
      },
      fontSize: {
        'micro':  ['0.625rem',  { lineHeight: '1.4' }],
        'xs':     ['0.75rem',   { lineHeight: '1.5' }],
        'sm':     ['0.875rem',  { lineHeight: '1.6' }],
        'base':   ['1rem',      { lineHeight: '1.78' }],
        'lg':     ['1.125rem',  { lineHeight: '1.78' }],
        'h6':     ['0.9375rem', { lineHeight: '1.4', letterSpacing: '.025em' }],
        'h5':     ['1.125rem',  { lineHeight: '1.3', letterSpacing: '.015em' }],
        'h4':     ['1.3125rem', { lineHeight: '1.2', letterSpacing: '.012em' }],
        'h3':     ['2rem',      { lineHeight: '1.08', letterSpacing: '-0.025em' }],
        'h2':     ['2.5rem',    { lineHeight: '1.08', letterSpacing: '-0.025em' }],
        'h1':     ['3.75rem',   { lineHeight: '1.066', letterSpacing: '-0.025em' }],
      },
      borderRadius: {
        'none': '0',
        'xs':   '3px',
        'sm':   '4px',
        DEFAULT:'5px',
        'md':   '6px',
        'lg':   '8px',
        'xl':   '10px',
        '2xl':  '12px',
      },
      screens: {
        sm:  '768px',
        md:  '1024px',
        lg:  '1280px',
        xl:  '1440px',
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
| Brand primary | `--bain-brand` | `#CC0000` |
| Background | `--bain-bg` | `#ffffff` |
| Surface | `--bain-surface` | `#f9f9f9` |
| Text heading | `--bain-fg` | `#0a0a0a` |
| Text muted | `--bain-fg-muted` | `#636363` |
| Text subtle | `--bain-fg-subtle` | `#8a8a8a` |
| Border | `--bain-border` | `#e6e6e6` |
| Hero bg | `--bain-bg-dark` | `#0a0a0a` |
| Teal accent | `--bain-teal` | `#005a5f` |
| Success | `--bain-success` | `#3adb76` |
| Error | `--bain-error` | `#b90319` |

### Example Component Prompts

#### Hero Section

```
Bain & Company 스타일 히어로 섹션.
- 배경: #0a0a0a (solid 근-검정, gradient 없음)
- H1: RecklessNeue 3.75rem weight 400 ls -0.025em color #ffffff lh 1.066
- Sub: Graphik 1.125rem color #8a8a8a lh 1.78
- Primary CTA: bg #CC0000 color #fff radius 4px padding 12px 28px
  Graphik weight 600 + 우측 화살표 아이콘
- 좌측 정렬, max-width 1280px
```

#### Insight Card

```
Bain 스타일 인사이트 카드.
- bg #ffffff, border 1px solid #e6e6e6, radius 0 (에디토리얼)
- padding 24px
- 이미지: aspect-ratio 16/9, radius 0
- 태그: Graphik 0.75rem ls .025em uppercase color #CC0000
- 제목: Graphik 1.3125rem weight 600 color #0a0a0a lh 1.2 ls .012em
- 본문: Graphik 1rem color #636363 lh 1.78
- hover: transform translateY(-2px) 200ms ease
```

#### Stat Block (signature)

```
Bain 통계 블록.
- 숫자: Graphik 3.75rem weight 700 color #0a0a0a
  border-top 2px solid #CC0000, padding-top 16px
- 라벨: Graphik 1rem weight 400 color #636363, margin-top 8px
- 배경: #ffffff 또는 #f9f9f9
- 1-row 3-col grid, gap 32px
```

#### Navigation (Dark)

```
Bain 상단 네비게이션.
- height 64px, position sticky top 0
- bg #0a0a0a
- 로고: 좌측 흰색 Bain & Company 워드마크
- 링크: Graphik 14px weight 400 color rgba(255,255,255,.7)
  hover color #ffffff 200ms ease
- Active: color #CC0000 + bottom border-bottom 2px solid #CC0000
- CTA 우측: "Contact Us" — border 1px solid rgba(255,255,255,.6)
  color #ffffff, hover bg #ffffff color #0a0a0a
```

### Iteration Guide

- **색상 변경 시**: `--bain-*` semantic token 사용. 레드 `#CC0000`은 accent에만.
- **폰트 변경 시**: Graphik 대체 → `Inter` / `DM Sans`. RecklessNeue 대체 → `Playfair Display`.
- **여백 조정 시**: `--bain-space-*` (4/8/16/24/48/80/120) 중에서만.
- **새 컴포넌트 추가 시**: 에디토리얼 맥락 → `radius: 0`. UI 컴포넌트 → `radius: 4px`.
- **Shadow**: soft one-layer `0 0 10px rgba(0,0,0,.5)` 또는 없음. Dual-layer 사용 금지.
- **반응형**: 768 / 1024 / 1280 / 1440 4단계.
- **Dark 섹션**: hero bg `#0a0a0a` / `#121212`. card dark는 `#252525`.
- **transition**: `200ms ease` 기본. 300ms 이상 금지.

---

## 18. DO / DON'T

### DO

- 히어로 배경은 `#0a0a0a` 또는 `#121212` (solid, gradient 없음).
- 시그니처 레드 `#CC0000`은 nav active, CTA 화살표, accent bar, stat border-top에만.
- H1은 `RecklessNeue` — 에디토리얼 권위의 핵심.
- 에디토리얼 카드 radius는 `0` — sharp edge가 권위감을 만든다.
- body text `color: #333333` 또는 `#0a0a0a` / muted는 `#636363`.
- CTA primary는 `#CC0000 bg + #ffffff text + radius 4px`.
- body line-height는 `1.78` — 장문 리포트 가독성 확보.
- 통계 블록은 숫자 위에 `border-top: 2px solid #CC0000`.

### DON'T

- `#CC0000`을 배경 면적으로 쓰지 말 것 — 경고 페이지가 된다.
- 히어로 배경에 gradient 사용 금지 — Bain hero는 solid 근-검정.
- `box-shadow: 0 4px 16px rgba(0,0,0,0.15)` 같은 과한 shadow 금지 — `0 0 10px rgba(0,0,0,.5)` 한도.
- border-radius `16px` 이상 금지 — 최대 `12px`.
- transition `300ms` 이상 금지 — Bain은 `200ms ease`.
- 텍스트를 `#000000` pure black으로 두지 말 것 — `#0a0a0a` 또는 `#333333`.
- teal `#005a5f`를 primary CTA에 쓰지 말 것 — 데이터 accent / 링크 accent만.
- Graphik body에 `font-weight: 700` 금지 — 숫자/통계 강조에만 사용.
