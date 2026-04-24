---
schema_version: 3.1
slug: figma
service_name: Figma
site_url: https://www.figma.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#000000"
primary_font: figmaSans
font_weight_normal: 400
token_prefix: --f-*

bold_direction: "Playful Precision"
aesthetic_category: "Playful Precision"
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Figma (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Figma의 마케팅 사이트는 **"툴처럼 보이지 않는 툴"**의 시각 언어다. 대부분의 SaaS 홈페이지가 순백 또는 다크 모드를 선택할 때, Figma는 굳이 **파스텔 컬러 블록**을 과감히 면적으로 밀어붙인다. hero 섹션은 `#C7F8FB`(mint), `#00B6FF`(cyan), `#FFC9C1`(peach), `#E4FF97`(lime), `#CB9FD2`(lilac) 같은 크레용 박스 색을 배경 가득 채우고, 그 위에 `#000000` 순흑 타이포와 `#000000` pill button을 얹는다. 배경은 밝고 텍스트는 까만, 제로-모호 대비.

색상 전략은 **"segment 별로 색을 바꿔라"**다. lego block이라고 부르는 섹션마다 `--f-bg-color`가 전환된다 — Design은 mint, Dev Mode는 cyan, Enterprise는 peach. 브랜드 "색"이 없는 게 브랜드 전략이다. 대신 대비는 강박적으로 유지된다: `--f-bg-color` × `--f-text-color` 페어가 항상 선명하고, text-secondary는 `rgba(0,0,0,0.65)` 알파 축소로 일관된 공식을 쓴다. 아주 드문 채도 축: `#972121` 검정-와인(에러), `#4D49FC` 인디고(액센트), `#24CB71`(success) — 면적은 절대 안 준다.

타이포그래피는 자체 호스팅한 가변폰트 **figmaSans**와 **ABCWhytePlusVariable**을 축으로 `320/330/340/400/450/480/520/530/540/550`의 미세 weight 계단을 사용한다. 마치 디자이너가 variable axis slider를 1px씩 움직여본 흔적 그대로. 코드 폰트는 **figmaMono**로 자체 호스팅. body는 `1rem` 기본 · large는 `1.125rem`, ordered list는 `1.25rem`으로 조금 크게 두는 특이한 패턴.

레이아웃은 48열 grid가 핵심이다 — `--f-columns: 48`, `--f-max-content-width: 1680px`. 48열이라는 과도한 해상도 덕에 14/26/8 같은 비정수 폭 조합이 가능하다. 섹션은 `--f-lego-block-padding`으로 리듬을 낸다: 모바일 `5rem`, 960px부터 `7.5rem`, 1920px 이상 `10rem`. 라디우스는 `1rem (--radius)` 고정 — 카드든 버튼이든 뭐든 `16px`. shadow는 거의 없다 — 대신 색면 자체가 섹션 경계다.

인터랙션은 조용하다. outline focus만 깔끔히: `a:focus-visible, button:focus-visible { outline: var(--f-text-color,#000) dashed 2px; outline-offset: 4px }`. transition은 글로벌로 선언하지 않고 필요한 지점에만. 캐러셀(slide) 구조가 있는 걸 봐서 드래그/grab 커서까지 토큰화 (`--f-cursor-grab/grabbing`). 전체적으로 "디자인 툴이니까 과하게 디자인하지 않는다"는 규율.

### Key Characteristics

- 파스텔 컬러 블록 면적 사용 (`#C7F8FB` / `#00B6FF` / `#FFC9C1` / `#E4FF97` / `#CB9FD2`)
- section 단위 `--f-bg-color` 전환 (lego block 시스템)
- 순흑 `#000000` 텍스트 + `#FFFFFF` 보조
- figmaSans + ABCWhytePlusVariable 자체 호스팅 + 미세 weight 계단 (320~550)
- 48열 grid · max-width 1680px
- 라디우스 `1rem (16px)` 단일
- lego block padding 5/7.5/10rem 반응형 계단
- 2px dashed outline focus (figma 특유의 accessibility 시그니처)

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Playful Precision
> **Aesthetic Category**: Playful Precision
> **Signature Element**: 이 사이트는 **파스텔 컬러 블록을 section 단위로 과감히 면적에 쓰고, 순흑 타이포로 제로-모호 대비를 만드는 규율**로 기억된다.
> **Code Complexity**: medium — CSS variable + lego block 토큰 + 48열 grid, 화려한 모션 없음

---

## 01. Quick Start

> 5분 안에 Figma처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "figmaSans", "SF Pro Display", system-ui, helvetica, sans-serif;
  font-weight: 400;
  font-size: 1rem;
}

/* 2. 배경 + 텍스트 (섹션마다 전환) */
:root {
  --f-bg-color: #C7F8FB;       /* mint default */
  --f-text-color: #000000;
  --f-text-secondary-color: rgba(0, 0, 0, 0.65);
}
body { background: var(--f-bg-color); color: var(--f-text-color); }

/* 3. 섹션 블록 (lego 시스템) */
:root { --f-lego-block-padding: 5rem; --radius: 1rem; }
@media (min-width: 960px)  { :root { --f-lego-block-padding: 7.5rem; } }
@media (min-width: 1280px) { :root { --f-lego-block-padding: 10rem; } }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백 `#FFFFFF`로 두지 마라. Figma의 홈은 파스텔 블록이다. `#C7F8FB` / `#00B6FF` / `#FFC9C1` / `#E4FF97` 중 하나를 배경으로 깔고 그 위에 `#000000` 텍스트를 올릴 때 Figma가 된다. 흰 배경에 검은 글자는 Notion 또는 Medium이지, Figma가 아니다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.figma.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 추출 완료 (Next.js/React SSR) |
| CSS files | 1개 외부 + 인라인 (8,238줄 인라인 style) |
| Token prefix | `--f-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: React + 자체 빌드 파이프라인 (figma-web CSS 번들)
- **Design system**: 내부 토큰 — prefix `--f-*` (색상/레이아웃), `--slide-*` (carousel), `--drawers-*` (UI 드로어)
- **CSS architecture**: semantic-direct 1-tier + component alias
  ```
  core    (--f-bg-color, --f-text-color)              직접 hex 값
  comp    (--f-primary-btn-bg-color, --f-badge-*)     컴포넌트 단위 alias
  action  (--f-emphasis-btn-*, --f-form-*)            상호작용 컴포넌트
  ```
- **Class naming**: `fig-{hash}` 해시 기반 CSS-in-JS (emotion/styled 계열)
- **Default theme**: light (`--f-bg-color: #FFFFFF` fallback, 실제 섹션은 파스텔 전환)
- **Font loading**: 자체 호스팅 `figmaSans`, `figmaMono`, `ABCWhytePlusVariable` woff2
- **Canonical anchor**: 고정 브랜드 hex 없음 — section별 `--f-bg-color` 전환이 브랜드 시그니처

---

## 04. Font Stack

- **Display/Body**: `figmaSans` (자체 호스팅, 유료)
- **Display alt**: `ABCWhytePlusVariable` (Dinamo, 유료)
- **Code**: `figmaMono` (자체 호스팅)
- **Weight normal / bold**: `400` / `540`
- **Variable weights used**: `320 / 330 / 340 / 400 / 450 / 480 / 520 / 530 / 540 / 550`

```css
:root {
  --f-font-sans:
    "figmaSans", "figmaSans Fallback",
    "SF Pro Display", system-ui, helvetica, sans-serif;
  --f-font-whyte-variable:
    'ABCWhytePlusVariable', 'ABCWhytePlusVariable Fallback',
    Whyte, sans-serif;
  --f-font-mono:
    "figmaMono", "figmaMono Fallback",
    "SF Mono", menlo, monospace;
}
body {
  font-family: var(--f-font-sans);
  font-weight: 400;
}
```

> **라이선스 주의**: figmaSans/figmaMono는 Figma 내부 폰트. 복제 시 `Inter`, `Söhne`, 또는 `IBM Plex Sans`로 대체하고 Mono는 `JetBrains Mono`로 대체.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| caption | `0.75rem` (12px) | 400 | 1.5 | 0 |
| body-small | `0.875rem` (14px) | 400 | 1.5 | 0 |
| body | `1rem` (16px) | 400 | 1.6 | 0 |
| body-large | `1.125rem` (18px) | 400 | 1.55 | 0 |
| list-ordered | `1.25rem` (20px) | 400 | 1.5 | 0 |
| h3 | `1.5rem` (24px) | 540 | 1.3 | -0.01em |
| h2 | `2rem` (32px) | 540 | 1.2 | -0.02em |
| h1 | `3rem` (48px) | 540 | 1.1 | -0.02em |
| display | `4.5rem` (72px) | 550 | 1.05 | -0.03em |

> ⚠️ Figma의 weight는 일반 `400/500/600/700`이 아니라 `320/330/340/400/450/480/520/530/540/550`의 미세 계단. figmaSans variable axis의 고유 weight 슬라이스다. Inter Variable로 대체할 경우 `400/500/600` 3단계로 단순화.

---

## 06. Colors

### 06-1. Brand (sectional — no single brand color)

Figma는 단일 브랜드 hex가 없다. 섹션마다 `--f-bg-color`를 바꾸는 것이 브랜드 패턴이다.

| Token | Hex | 섹션 |
|---|---|---|
| `--f-bg-color` (hero mint) | `#C7F8FB` | 홈 히어로 기본 |
| `--f-bg-color` (cyan) | `#00B6FF` | Dev Mode lego block |
| `--f-bg-color` (peach) | `#FFC9C1` | 기업 섹션 |
| `--f-bg-color` (lime) | `#E4FF97` | 커뮤니티 섹션 |
| `--f-bg-color` (lilac) | `#CB9FD2` | AI 섹션 |
| `--f-bg-color` (light pink) | `#FFB3B3` | CTA 섹션 |
| `--f-bg-color` (orange) | `#FF7237` | 강조 섹션 |
| `--f-bg-color` (dark) | `#000000` | 푸터/대비 섹션 |

### 06-3. Neutral Ramp

| Step | Hex | Usage |
|---|---|---|
| text-primary | `#000000` | 본문 / 헤드라인 |
| text-secondary | `rgba(0, 0, 0, 0.65)` | 서브 카피 |
| text-placeholder | `rgba(0, 0, 0, 0.5)` | form placeholder |
| surface-inverse | `#FFFFFF` | 브랜드 역상 면 |
| overlay-light | `rgba(255, 255, 255, 0.6)` | list header |
| overlay-icon | `rgba(255, 255, 255, 0.24)` | icon background on dark |
| badge-bg-dim | `rgba(0, 0, 0, 0.08)` | badge light |
| input-hover | `rgba(0, 0, 0, 0.16)` | form hover |
| neutral-light | `#E2E2E2` | divider |
| neutral-med | `#E6E6E6` | sub divider |

### 06-4. Accent Families (product lines + status)

| Family | Hex | Use |
|---|---|---|
| indigo | `#4D49FC` | 액센트, 제품 라인 |
| indigo-tint-15 | `#4D49FC15` | 인디고 soft bg |
| indigo-tint-20 | `#4D49FC20` | 인디고 hover bg |
| cyan | `#00B6FF` | Dev Mode 배경 / 링크 강조 |
| teal | `#33DFDF` | 제품 라인 |
| green | `#24CB71` | success state |
| green-neon | `#67FF7F` | 고채도 success highlight |
| red | `#FF3737` | error strong |
| red-soft | `#FFB3B3` | error soft bg |
| maroon | `#972121` | form error bg |
| maroon-dark | `#721C1C` | error dark |
| orange | `#FF7237` | 강조 · CTA |
| yellow-olive | `#B98E01` | notice |
| lavender | `#C4BAFF` | 서브 ramp |
| lilac | `#CB9FD2` | 서브 ramp |
| peach | `#FFC9C1` | 서브 ramp |
| lime | `#E4FF97` | 서브 ramp |
| lime-soft | `#F3FFE3` | 서브 ramp light |
| mint | `#C7F8FB` | 서브 ramp (hero) |
| sage | `#95B9AC` | neutral accent |
| sand | `#FADCA2` | warm neutral |
| purple-svg | `#874FFF` | svg pattern |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--f-text-color` | `#000000` (light) / `#FFFFFF` (dark block) | 본문 |
| `--f-text-secondary-color` | `rgba(0, 0, 0, 0.65)` | 서브 카피 |
| `--f-primary-btn-bg-color` | `#000000` (light) / `#FFFFFF` (dark) | CTA 배경 |
| `--f-primary-btn-text-color` | `#FFFFFF` (light) / `#000000` (dark) | CTA 텍스트 |
| `--f-emphasis-btn-bg-color` | `#000000` | 강조 CTA |
| `--f-emphasis-btn-text-color` | `#FFFFFF` | 강조 CTA 텍스트 |
| `--f-form-input-bg-color` | `rgba(0, 0, 0, 0.08)` | form 입력 배경 |
| `--f-form-select-hover-bg-color` | `rgba(0, 0, 0, 0.16)` | form hover |
| `--f-form-placeholder-text-color` | `rgba(0, 0, 0, 0.5)` | placeholder |
| `--f-form-error-bg-color` | `#972121` | error state bg |
| `--f-form-error-text-color` | `#FFFFFF` | error text |
| `--f-badge-bg-color` | `rgba(0, 0, 0, 0.08)` | badge |
| `--f-badge-text-color` | `#000000` | badge text |
| `--f-primary-transparent-color` | `rgba(0, 0, 0, 0.16)` | transparent primary |
| `--f-lego-bg-color` | `#C7F8FB` | lego block bg |
| `--f-lego-fg-color` | `#000000` | lego block fg |
| `--f-link-color` | `#000000` | link color (underline 기본) |
| `--f-icon-bg-color` | `rgba(255, 255, 255, 0.24)` | icon bg on dark |
| `--f-list-header-color` | `rgba(255, 255, 255, 0.6)` | list header on dark |
| `--carousel-parent-text-color` | `#FFFFFF` | carousel 텍스트 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--f-lego-bg-color` | `var(--f-bg-color, #FFFFFF)` | lego 섹션 배경 (cascade) |
| `--f-lego-fg-color` | `var(--f-text-color, #000000)` | lego 섹션 전경 |
| `--f-link-color` | `var(--f-text-color, #000000)` | 링크 = 본문색 |

### 06-7. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000` | 542 | neutral ink primary |
| 2 | `#FFFFFF` | 342 | neutral light primary |
| 3 | `#972121` | 50 | form error bg |
| 4 | `#4D49FC` | 10 | indigo accent |
| 5 | `#00B6FF` | 9 | cyan sectional bg |
| 6 | `#24CB71` | 9 | success state |
| 7 | `#697485` | 8 | text tertiary |
| 8 | `#C7F8FB` | 7 | mint sectional bg |
| 9 | `#CB9FD2` | 7 | lilac sectional bg |
| 10 | `#FFC9C1` | 7 | peach sectional bg |

---

## 07. Spacing

Figma는 **lego block padding**을 핵심 리듬 토큰으로 삼는다. spacing scale 이름이 따로 없고 `rem` 기반 raw 값을 직접 쓴다.

| Token | Value | Use case |
|---|---|---|
| `--f-lego-block-padding` (mobile) | `5rem` (80px) | 섹션 상하 |
| `--f-lego-block-padding` (≥960px) | `7.5rem` (120px) | 섹션 상하 |
| `--f-lego-block-padding` (≥1920px) | `10rem` (160px) | 섹션 상하 |
| `--f-max-content-width` | `1680px` | 콘텐츠 최대 폭 |
| `--f-columns` | `48` | grid 열 수 |
| `--f-gutter` | `calc(var(--f-col-width) * 2)` | 열 간격 (2 col) |
| `--f-col-width` | `calc(min(100vw, 1680px) / 48)` | 1 열 폭 |
| `scroll-margin-top` | `5rem` | anchor scroll offset |
| body top padding-block | `5rem 3rem` (h/v) | hero 외곽 |
| carousel slide-gap | `calc(var(--f-col-width) * 1)` | 캐러셀 간격 |
| drawers-img-col-width | `calc(var(--f-col-width) * 26)` | drawer 이미지 폭 |

<!-- SOURCE: auto (inline CSS parsing) -->

**주요 alias**:
- `--f-lego-block-padding` → 5/7.5/10rem (반응형 3단 계단) · 섹션 리듬의 유일한 scale

---

## 08. Radius

Figma는 radius 단일 값 `1rem (16px)`을 모든 컴포넌트에 쓴다. 이것이 "buttons look like cards" 시그니처의 원인이다.

| Token | Value | Context |
|---|---|---|
| `--radius` | `1rem` (16px) | 카드 / 버튼 / 인풋 전체 기본 |
| (computed) | `0.5rem` (8px) | 내부 chip / badge (드물게) |
| (computed) | `9999px` | pill — carousel dots |
| (computed) | `50%` | avatar 원형 |

> Figma의 radius 규율은 "전부 16px로 통일"에 가깝다. 4/6/8/12 같은 세부 scale이 없다.

---

## 09. Shadows

Figma는 shadow를 거의 쓰지 않는다. 섹션 경계는 **색면 자체**로 구분한다.

| Level | Value | Usage |
|---|---|---|
| default | `none` | 대부분 컴포넌트 <!-- SOURCE: auto --> |
| subtle | `0 1px 2px rgba(0,0,0,0.06)` | dropdown menu <!-- SOURCE: template-default --> |
| elevated | `0 8px 24px rgba(0,0,0,0.12)` | modal/popover <!-- SOURCE: template-default --> |

<!-- SOURCE: Figma의 inline CSS에는 box-shadow 토큰이 거의 등장하지 않음. 색면 경계가 shadow 역할을 대체. -->

---

## 10. Motion

CSS 변수로 정의된 duration/easing 토큰은 없음. 주로 `transition: all .2s ease` 수준의 인라인 선언이 관찰된다.

| Token | Value | Usage |
|---|---|---|
| hover-transition | `.2s ease` <!-- SOURCE: template-default --> | 버튼 hover |
| slide-transition | custom transform | carousel slide (variable based on `--slide-width`) |
| focus-outline | `2px dashed` | focus-visible 가시성 (duration 없음) |
| blink | N/A | 적용되지 않음 |

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1680px` (`--f-max-content-width`)
- **Grid type**: 48-column CSS Grid (매우 높은 해상도)
- **Column count**: `48` (`--f-columns`)
- **Gutter**: `calc(var(--f-col-width) * 2)` = 2 열 분량
- **1 col width**: `calc(min(100vw, 1680px) / 48)` ≈ 35px @ max

### Hero

- **🆕 Pattern Summary**: `~100vh mint 배경(#C7F8FB) + 중앙 H1 big + 듀얼 CTA pill + 하단 product mockup`
- Layout: 1-column 중앙 정렬 (데스크톱) / 1-column (모바일)
- Background: `solid #C7F8FB` (mint) 또는 섹션 이동 시 cyan `#00B6FF`
- **🆕 Background Treatment**: `solid color block` (그라데이션 아님, 단일 파스텔)
- H1: `~3rem (48px)` → 데스크톱 `~4.5rem (72px)` / weight `540~550` / tracking `-0.02em`
- Max-width: `1680px`

### Section Rhythm

```css
section {
  padding-block: var(--f-lego-block-padding); /* 5/7.5/10rem */
  max-width: var(--f-max-content-width);      /* 1680px */
  margin-inline: auto;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` 또는 `var(--f-bg-color)` 섹션 색
- **Card border**: 보통 없음 — 색면 자체가 구분
- **Card radius**: `1rem (16px)` (`--radius`)
- **Card padding**: `2rem` 기본, 큰 것은 `3rem`
- **Card shadow**: 기본 `none`

### Navigation Structure

- **Type**: horizontal desktop / hamburger mobile
- **Position**: `position: fixed; top: 0`
- **Height**: `~5rem` (80px) 추정
- **Background**: `rgba(255,255,255,0.9)` + `backdrop-filter: blur` 또는 섹션 배경 상속
- **Border**: 하단 `1px solid rgba(0,0,0,0.08)` 또는 없음

### Content Width

- **Prose max-width**: 본문 `~720px` (관찰상)
- **Container max-width**: `1680px` (`--f-max-content-width`)
- **Homepage max-width**: `1680px`
- **Sidebar width**: N/A — marketing

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 960px` | 1-column, 햄버거 nav, lego block 5rem |
| Desktop | `≥ 960px` | 2-col, lego block 7.5rem |
| Large | `≥ 1280px` | hero 확대 |
| XL | `≥ 1920px` | lego block 10rem |

*모바일 퍼스트* — `min-width` 우세 (960 / 1280 / 1920)

### Touch Targets

- **Minimum tap size**: `~44px` (관찰상)
- **Button height (mobile)**: `~48px` (pill radius 1rem)
- **Input height (mobile)**: `~48px`

### Collapsing Strategy

- **Navigation**: 960px 이하에서 햄버거로 접힘
- **Grid columns**: `48` → 모바일 `12` 수준으로 재배치
- **Sidebar**: N/A
- **Hero layout**: 1-column 유지, 텍스트만 크기 감소

### Image Behavior

- **Strategy**: 자체 CDN, lazy-load, responsive srcset
- **Max-width**: `100%`
- **Aspect ratio handling**: `aspect-ratio` 직접 선언 + `object-fit: cover`

---

## 13. Components

### Buttons

Figma의 버튼은 `--f-primary-btn-*`와 `--f-emphasis-btn-*` 두 종류 + transparent variant로 구성된다.

```html
<button class="fig-primary">Get Figma free</button>
<button class="fig-emphasis">Contact sales</button>
<button class="fig-ghost">Learn more</button>
```

| Variant | background | color | border-radius | padding | hover |
|---|---|---|---|---|---|
| primary (on light) | `#000000` | `#FFFFFF` | `1rem` | `0.75rem 1.5rem` | opacity 0.9 |
| primary (on dark) | `#FFFFFF` | `#000000` | `1rem` | `0.75rem 1.5rem` | opacity 0.9 |
| emphasis | `#000000` | `#FFFFFF` | `1rem` | `0.75rem 1.5rem` | brightness 1.1 |
| ghost | `transparent` + border 1px | `currentColor` | `1rem` | `0.75rem 1.5rem` | bg rgba(0,0,0,0.08) |
| pill | 좌동 | 좌동 | `9999px` | 동일 | 좌동 |

### Badges

```html
<span class="fig-badge">New</span>
```

- background: `rgba(0, 0, 0, 0.08)` (`--f-badge-bg-color`)
- color: `#000000` (`--f-badge-text-color`)
- border-radius: `0.5rem` (8px, 관찰)
- font-size: `12px`, weight 480
- padding: `0.25rem 0.5rem`

### Cards & Containers

```html
<article class="fig-card">
  <h3>Dev Mode</h3>
  <p>Close the gap between design and code.</p>
</article>
```

- bg: `var(--f-bg-color)` 섹션 상속 또는 `#FFFFFF`
- border: 없음 — 색면 경계
- radius: `1rem` (`--radius`)
- padding: `2rem` 기본
- shadow: 기본 none
- hover: 대부분 없음 또는 `transform: translateY(-2px)`

### Navigation

- 로고: 좌측, figma 워드마크 (SVG)
- 링크: `figmaSans` 14-15px weight 450, color `--f-text-color`
- Active: weight 540
- CTA 우측: "Contact sales" + "Log in" + "Get Figma free" 삼각
- Height: `~5rem` fixed
- 모바일: 햄버거

### Inputs & Forms

- height: `~48px`
- padding: `0 1rem`
- background: `rgba(0, 0, 0, 0.08)` (`--f-form-input-bg-color`)
- border: none 기본 / focus 시 `outline 2px dashed currentColor`
- radius: `1rem` (`--radius`)
- placeholder: `rgba(0, 0, 0, 0.5)` (`--f-form-placeholder-text-color`)
- error: bg `#972121` + color `#FFFFFF`

### Hero Section

- 배경: `#C7F8FB` (mint) solid
- 좌상단 eyebrow → H1 (48-72px, weight 540-550) → sub (18-20px) → 듀얼 CTA pill
- 하단: 실제 Figma 제품 스크린샷 (WebP), radius 1rem
- 2-column(데스크톱) → 1-column(모바일)

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 짧고 강하게, 동사 강조 | "Think bigger. Build faster." |
| Primary CTA | 3단어, 제품명 포함 | "Get Figma free" / "Try Dev Mode" |
| Secondary CTA | 대화형 | "Contact sales" |
| Subheading | 제품 가치 1문장 | "One tool for design, prototype, and collaboration." |
| Tone | 활기찬 확신, 디자이너 화법 — 자부심 + 친근함 | — |

---

## 15. Drop-in CSS

```css
/* Figma — copy into your root stylesheet */
:root {
  /* Fonts */
  --f-font-sans: "figmaSans", "SF Pro Display", system-ui, sans-serif;
  --f-font-mono: "figmaMono", ui-monospace, "SF Mono", Menlo, monospace;
  --f-font-weight-normal: 400;
  --f-font-weight-bold: 540;

  /* Surfaces (sectional — pick one per lego block) */
  --f-bg-mint:  #C7F8FB;
  --f-bg-cyan:  #00B6FF;
  --f-bg-peach: #FFC9C1;
  --f-bg-lime:  #E4FF97;
  --f-bg-lilac: #CB9FD2;
  --f-bg-pink:  #FFB3B3;
  --f-bg-black: #000000;
  --f-bg-white: #FFFFFF;

  /* Text */
  --f-text-primary:   #000000;
  --f-text-secondary: rgba(0, 0, 0, 0.65);
  --f-text-inverse:   #FFFFFF;

  /* Accents (point only) */
  --f-indigo: #4D49FC;
  --f-green:  #24CB71;
  --f-orange: #FF7237;
  --f-red:    #FF3737;
  --f-maroon: #972121;

  /* Layout */
  --f-max-content-width: 1680px;
  --f-columns: 48;
  --f-lego-block-padding: 5rem;

  /* Radius */
  --radius: 1rem;
}

@media (min-width: 960px)  { :root { --f-lego-block-padding: 7.5rem; } }
@media (min-width: 1920px) { :root { --f-lego-block-padding: 10rem; } }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Figma
module.exports = {
  theme: {
    extend: {
      colors: {
        figma: {
          mint:  '#C7F8FB',
          cyan:  '#00B6FF',
          peach: '#FFC9C1',
          lime:  '#E4FF97',
          lilac: '#CB9FD2',
          pink:  '#FFB3B3',
          orange:'#FF7237',
          indigo:'#4D49FC',
        },
        ink: {
          DEFAULT: '#000000',
          soft:    'rgba(0,0,0,0.65)',
          placeholder: 'rgba(0,0,0,0.5)',
        },
      },
      fontFamily: {
        sans: ['figmaSans', 'SF Pro Display', 'system-ui'],
        mono: ['figmaMono', 'ui-monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '480',
        bold:   '540',
      },
      borderRadius: {
        DEFAULT: '1rem',
        pill: '9999px',
      },
      maxWidth: {
        content: '1680px',
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
| Sectional bg (hero) | `--f-bg-color` | `#C7F8FB` |
| Text primary | `--f-text-color` | `#000000` |
| Text secondary | `--f-text-secondary-color` | `rgba(0, 0, 0, 0.65)` |
| CTA primary bg | `--f-primary-btn-bg-color` | `#000000` |
| CTA primary text | `--f-primary-btn-text-color` | `#FFFFFF` |
| Success | (accent) | `#24CB71` |
| Error bg | `--f-form-error-bg-color` | `#972121` |
| Accent | (indigo) | `#4D49FC` |

### Example Component Prompts

#### Hero Section

```
Figma 스타일 히어로 섹션을 만들어줘.
- 배경: #C7F8FB (mint) solid block, 전체 화면
- H1: figmaSans, 4.5rem (72px), weight 550, tracking -0.03em, color #000000
- 서브텍스트: 1.25rem (20px), color rgba(0,0,0,0.65)
- CTA primary: 배경 #000000, 텍스트 #FFFFFF, radius 1rem, padding 0.75rem 1.5rem
- CTA secondary: transparent + border 1px solid #000000 + color #000000, 동일 radius
- 최대 너비: 1680px
- 중앙 정렬 텍스트 + 하단 product screenshot(radius 1rem)
```

#### Card Component

```
Figma 스타일 카드 컴포넌트를 만들어줘.
- 배경: var(--f-bg-color) 섹션 상속 또는 #FFFFFF
- border: 없음 (색면 경계)
- radius: 1rem (16px)
- padding: 2rem
- shadow: none
- hover: transform translateY(-2px) .2s ease
- 제목: figmaSans, 1.5rem (24px), weight 540, color #000000
- 본문: 1rem (16px), color rgba(0,0,0,0.65), line-height 1.6
```

#### Badge

```
Figma 스타일 "New" 배지를 만들어줘.
- font: figmaSans, 12px, weight 480
- padding: 0.25rem 0.5rem, radius 0.5rem
- 기본: bg rgba(0,0,0,0.08), color #000000
- 강조: bg #4D49FC, color #FFFFFF
```

#### Navigation

```
Figma 스타일 상단 네비게이션을 만들어줘.
- 높이: 5rem (80px), position fixed, top 0, width 100%
- 배경: rgba(255,255,255,0.9), backdrop-filter blur(12px)
- 로고: 좌측, figma 워드마크 SVG 24px 높이
- 링크: figmaSans 15px weight 450, color #000000
- 활성 링크: weight 540
- CTA 우측 페어: "Log in" (text) + "Contact sales" (ghost) + "Get Figma free" (primary pill, bg #000, color #FFF, radius 1rem)
```

### Iteration Guide

- **색상 변경 시**: 섹션 배경은 `#C7F8FB / #00B6FF / #FFC9C1 / #E4FF97 / #CB9FD2` 5색 팔레트 안에서만. 임의 색상 금지.
- **폰트 변경 시**: weight `400`이 기본. 헤드라인은 `540/550`. 일반 `500/600/700` 쓰지 말 것.
- **여백 조정 시**: `--f-lego-block-padding` 5/7.5/10rem 3단 계단 유지. 임의 여백 금지.
- **새 컴포넌트 추가 시**: radius는 무조건 `1rem` (16px). 4/8/12px 금지.
- **다크 모드**: 별도 테마가 아니라 `--f-bg-color: #000000` 섹션일 때 `--f-text-color: #FFFFFF` swap.
- **반응형**: 960/1280/1920 3단. 커스텀 브레이크포인트 추가 금지.
- **accent 색 사용**: 절대 면적으로 쓰지 말 것. pill · badge · icon accent에만.

---

## 18. DO / DON'T

### ✅ DO

- 섹션 배경은 `#C7F8FB` / `#00B6FF` / `#FFC9C1` / `#E4FF97` / `#CB9FD2` 중 하나. **면적으로 칠해라.**
- CTA는 `#000000` 배경 + `#FFFFFF` 텍스트 + `border-radius: 1rem`.
- 본문은 `figmaSans` `1rem (16px)` `weight 400`.
- 헤드라인 weight는 `540` 또는 `550` (일반 `700` 쓰지 말 것).
- 모든 radius는 `1rem` 통일. 카드·버튼·인풋 전부.
- focus는 `2px dashed currentColor outline + 4px offset` (Figma의 accessibility 시그니처).
- `--f-lego-block-padding` 5/7.5/10rem 3단 계단으로 섹션 리듬 유지.

### ❌ DON'T

- 배경을 순백 `#FFFFFF`로 두지 말 것 — Figma 홈은 파스텔이다. 흰 배경 = Medium/Notion.
- 브랜드 컬러 `#4D49FC` (indigo)를 넓은 면적에 쓰지 말 것 — point accent 전용.
- body weight `500` 또는 `600` 쓰지 말 것 — Figma는 `400/450/480/540/550`.
- radius `8px`, `12px`, `24px` 쓰지 말 것 — 전부 `1rem` (16px).
- shadow `0 4px 12px rgba(0,0,0,0.1)` 같은 기본 shadow 금지 — Figma는 shadow 안 쓰고 색면으로 경계 만듦.
- 폰트를 Inter로 바로 대체 금지 — figmaSans의 weight 480/540 미세 차이가 사라짐. 최소 Inter Variable 사용.
- transition `.3s` 이상 금지 — Figma는 느린 hover 없음.
- 섹션 배경을 그라데이션으로 만들지 말 것 — solid color block이 Figma 시그니처.
