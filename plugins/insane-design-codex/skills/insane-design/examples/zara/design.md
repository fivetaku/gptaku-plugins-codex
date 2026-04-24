---
slug: zara
service_name: Zara
site_url: https://www.zara.com
fetched_at: 2026-04-15
default_theme: light
brand_color: "#000000"
primary_font: Helvetica Now Text
font_weight_normal: 300
token_prefix: --color-*
---

# DESIGN.md — Zara (Codex Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

자라(Zara)는 패스트패션 브랜드임에도 럭셔리에 근접한 **극도의 절제**를 UI 언어로 삼는다. 검정 `#000000`과 흰색 `#FFFFFF`의 이분법적 팔레트 위에 Helvetica Now Text 웨이트 300(Light)을 기본 body 폰트로 쓴다. 색상은 거의 쓰지 않고, 라인과 공간으로 계층을 만든다.

색상 전략은 철저한 흑백 모노크롬이다. `--color-main-000`(#fff)부터 `--color-main-080`(#333)까지 8단계 그레이 스케일이 모든 UI를 처리한다. 유일한 예외는 오류/강조 레드 `#E90D01`·`#FF3B30`과 성공 그린 `#23F444`·`#34C759`이며, 이마저도 상태 피드백 전용이다. 프로모 배지조차 검정 배경 위 흰 텍스트다.

폰트는 사이트의 핵심 정체성이다. `Helvetica Now Text` Light(300)를 primary body로, `Gilroy`와 `Apercu`를 일부 섹션에 혼용하고, `Times New Roman`이 에디토리얼 섹션 헤드라인에 간헐적으로 등장한다. weight 300이 기본값이라 통상 UI보다 현저히 가벼운 획굵기를 갖는다. 700 bold는 강조할 때만 사용.

여백은 관대하고 리듬이 있다. 상품 이미지가 배경 역할을 하며, 텍스트 요소는 이미지 위에 최소한으로 올린다. 섹션 사이는 넓은 padding으로 분리하고, 불필요한 시각 요소는 철저히 제거한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Zara처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Helvetica Now Text", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 300;  /* Light — 400 아님 */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: body font-weight를 `400`으로 설정하는 것. 자라의 정체성은 weight `300` Light에 있다. 400으로 바꾸는 순간 "패스트패션 일반 쇼핑몰" 느낌이 된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.zara.com/kr/` |
| Fetched | 2026-04-15 |
| Extractor | Playwright MCP (headless Chromium, bot-bypass) |
| HTML size | 1,919,528 bytes (Next.js SSR) |
| CSS files | 13개 외부 (`static.zara.net`) + 274,323자 인라인, 총 919,026자 |
| Token prefix | `--color-*` (시맨틱 컬러 시스템), `--color-main-*` (뉴트럴 램프) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (static.zara.net CDN 에셋)
- **Design system**: 커스텀 — prefix `--color-*` (Zara 자체 디자인 토큰)
- **CSS architecture**: CSS 커스텀 프로퍼티 시맨틱 토큰 + 컴포넌트 CSS
  ```
  --color-main-*          뉴트럴 램프 (000=white ~ 080=dark gray)
  --color-background-*    시맨틱 surface 토큰
  --color-content-*       시맨틱 텍스트 토큰
  --color-semantic-*      상태 컬러 (danger/success/warning/info)
  ```
- **Class naming**: BEM 변형 + Zara 커스텀 클래스
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 커스텀 웹폰트 CDN (`Helvetica Now Text`, `Gilroy`, `Apercu`)
- **Canonical anchor**: `#000000` — 자라 UI의 모든 CTA·텍스트·아이콘은 검정

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `Helvetica Now Text` (유료 커스텀, Monotype)
- **Secondary**: `Neue Helvetica for Zara` (자체 커스터마이즈드)
- **Editorial headline**: `Times New Roman` (에디토리얼 섹션)
- **Display accent**: `Gilroy` (캠페인 타이틀)
- **Fallback**: `Helvetica Neue`, `Arial`, `sans-serif`
- **Weight normal / bold**: `300` / `700`

```css
:root {
  --zara-font-family: "Helvetica Now Text", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --zara-font-family-editorial: "Times New Roman", "Helvetica Now Text", Arial, Sans-Serif;
  --zara-font-weight-normal: 300;
  --zara-font-weight-bold: 700;
}
body {
  font-family: var(--zara-font-family);
  font-weight: var(--zara-font-weight-normal);
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| xs | 0.625rem (10px) | 300 | 1.4 | 0.02em |
| sm | 0.6875rem (11px) | 300–500 | 1.5 | 0.01em |
| base / body | 0.8125rem (13px) | 300 | 1.6 | 0 |
| md | 1rem (16px) | 300–500 | 1.5 | 0 |
| lg | 1.5rem (24px) | 300–700 | 1.3 | -0.01em |
| display | 2rem+ | 300 | 1.1 | -0.02em |

> ⚠️ Zara의 모든 텍스트는 weight 300이 기본. 0.8125rem(13px)이 body 표준. 큰 display 폰트도 weight 300으로 쓰는 것이 자라의 정체성이다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Monochrome)

| Token | Hex |
|---|---|
| --color-main-000 | `#FFFFFF` |
| --color-main-005 | `#F2F2F2` |
| --color-main-010 | `#E5E5E5` |
| --color-main-020 | `#CCCCCC` |
| --color-main-040 | `#999999` |
| --color-main-060 | `#666666` |
| --color-main-080 | `#333333` |
| brand / black | `#000000` |

### 06-2. Brand Dark Variant

> N/A — 자라는 흑백 모노크롬. 별도 다크 브랜드 램프 없음.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| surface high | `#FFFFFF` | `#141414` |
| surface alt | `#F2F2F2` | `#262626` |
| mid | `#929292` | `#949494` |
| overlay | `rgba(0,0,0,0.25)` | `rgba(255,255,255,0.75)` |

### 06-4. Accent Families

> N/A — 자라는 상태 컬러 외 채도 있는 브랜드 액센트 없음.

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --color-basic-black | `#000000` | 브랜드 / CTA / 텍스트 |
| --color-basic-white | `#FFFFFF` | 배경 / 반전 텍스트 |
| --color-content-low | `#666666` | 보조 텍스트 |
| --color-content-mid | `#929292` | 비활성 텍스트 |
| --color-emphasis | `#FF3B30` | 강조 / 에러 |
| --color-semantic-danger-high | `#E90D01` | 오류 |
| --color-semantic-success-high | `#0A882A` | 성공 / 재고 있음 |
| --color-semantic-warning-high | `#B66009` | 경고 |
| --color-done | `#34C759` | 완료 상태 |
| --color-sales | `#23F444` | 세일 배지 |
| --color-notification | `#FF9500` | 알림 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| --color-background-low | `#141414` | 다크 surface |
| --color-background-surface | `#ffffffbf` | 반투명 오버레이 |
| --color-background-contrast | `#FFFFFF` | 대비 배경 |
| --color-background-overlay | `rgba(0,0,0,0.25)` | 모달 오버레이 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 865 | neutral — 기본 배경 |
| 2 | `#000000` | 519 | neutral — 텍스트/CTA/아이콘 |
| 3 | `#D8D8D8` | 32 | neutral — 구분선 |
| 4 | `#4C9BEB` | 20 | chromatic — (시스템 UI 기본값, 브랜드 X) |
| 5 | `#C1C1C1` | 20 | neutral — 비활성 |
| 6 | `#999999` | 16 | neutral — 보조 텍스트 |
| 7 | `#333333` | 14 | neutral — 강조 텍스트 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 아이콘 간격 |
| space-sm | 8px | 인라인 요소 |
| space-md | 16px | 컴포넌트 패딩 |
| space-lg | 24px | 카드 gap |
| space-xl | 40px | 섹션 패딩 |
| space-2xl | 80px | 섹션 간 여백 |

**주요 alias**:
- `section padding-top/bottom` → `40px`–`80px` (관대한 여백)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | `0` | 버튼, 입력창, 카드 — 자라는 각진 모서리 |
| radius-xs | `2px` | 일부 내부 요소 |
| radius-round | `17px` | 알림 배지(스크린샷 기준) |

---

## 09. Shadows
<!-- SOURCE: auto -->

> N/A — 자라 CSS에 box-shadow 없음. 계층 구분은 `1px solid #CCCCCC` border와 배경색으로만.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| duration-fast | `0.2s` | hover/active 전환 |
| duration-default | `0.25s` | 메뉴 슬라이드, 이미지 페이드 |
| easing-out | `ease-out` | 기본 |
| easing-linear | `linear` | 배경색 전환 |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: 100% (전폭 패션 이미지 우선)
- **Grid type**: CSS Grid (상품 그리드), Flexbox (네비)
- **Column count**: 4열 (데스크톱), 2열 (모바일)
- **Gutter**: 4px~8px (이미지 밀착 배치)

### Hero
- Layout: 전폭 이미지 + 텍스트 오버레이
- Background: 패션 화보 이미지
- H1: `Helvetica Now Text`, 2rem+, weight 300, color `#FFFFFF`
- Max-width: 100%

### Section Rhythm
```css
section {
  padding: 40px 0;
  max-width: 100%;
}
```

### Card Patterns
- **Card background**: 투명 (이미지가 카드)
- **Card border**: `none`
- **Card radius**: `0`
- **Card padding**: `8px 0` (이미지 아래 텍스트)
- **Card shadow**: 없음

### Navigation Structure
- **Type**: 수평 메가메뉴 (각 카테고리)
- **Position**: sticky top
- **Height**: 약 48px
- **Background**: `#FFFFFF`
- **Border**: `1px solid #000000` 하단

### Content Width
- **Prose max-width**: N/A
- **Container max-width**: `767px` 미만 모바일 전환
- **Sidebar width**: N/A

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | 767px | 2열 그리드, 햄버거 메뉴 |
| Tablet | 768px–1024px | 3열 그리드 |
| Desktop | 1024px+ | 4열 그리드 |
| Large | N/A | 전폭 유지 |

### Touch Targets
- **Minimum tap size**: 44px
- **Button height (mobile)**: 44px
- **Input height (mobile)**: 44px

### Collapsing Strategy
- **Navigation**: 햄버거 → 전폭 오버레이 슬라이드
- **Grid columns**: 4열 → 3열 → 2열
- **Sidebar**: N/A
- **Hero**: 전폭 유지

### Image Behavior
- **Strategy**: CSS `object-fit: cover`, 비율 유지
- **Max-width**: 100%
- **Aspect ratio handling**: 4:5 세로형 (패션 이미지 표준)

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="zara-btn-primary">추가하기</button>
```

```css
.zara-btn-primary {
  background: #000000;
  color: #FFFFFF;
  font-family: "Helvetica Now Text", "Helvetica Neue", sans-serif;
  font-size: 0.8125rem;
  font-weight: 300;
  border: none;
  border-radius: 0;
  padding: 12px 20px;
  min-height: 44px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.2s ease-out;
}
.zara-btn-primary:hover { background: #333333; }
```

| Spec | Value |
|---|---|
| bg | `#000000` |
| text | `#FFFFFF` |
| radius | `0` (각진 모서리) |
| height | `44px` |
| font-size | `0.8125rem` (13px) |
| letter-spacing | `0.05em` |

### Badges

```css
.zara-badge {
  background: #000000;
  color: #FFFFFF;
  font-size: 0.625rem;
  font-weight: 300;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: 0;
}
.zara-badge-sale {
  background: #23F444;
  color: #000000;
}
```

### Cards & Containers

```css
.zara-product-card {
  background: transparent;
  border: none;
  padding: 0;
}
.zara-product-card-info {
  padding: 8px 0;
}
.zara-product-card-title {
  font-size: 0.8125rem;
  font-weight: 300;
  color: #000000;
  line-height: 1.4;
}
.zara-product-card-price {
  font-size: 0.8125rem;
  font-weight: 300;
  color: #000000;
}
```

### Navigation

```css
.zara-nav {
  background: #FFFFFF;
  border-bottom: 1px solid #000000;
  height: 48px;
  position: sticky;
  top: 0;
  z-index: 100;
}
.zara-nav-link {
  font-family: "Helvetica Now Text", sans-serif;
  font-size: 0.8125rem;
  font-weight: 300;
  color: #000000;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  text-decoration: none;
}
```

### Inputs & Forms

```css
.zara-input {
  border: none;
  border-bottom: 1px solid #000000;
  border-radius: 0;
  height: 44px;
  padding: 0 0 8px;
  font-family: "Helvetica Now Text", sans-serif;
  font-size: 0.8125rem;
  font-weight: 300;
  color: #000000;
  background: transparent;
  outline: none;
}
.zara-input:focus { border-bottom-width: 2px; }
```

### Hero Section

```css
.zara-hero {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  overflow: hidden;
}
.zara-hero img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.zara-hero-caption {
  position: absolute;
  bottom: 24px;
  left: 24px;
  color: #FFFFFF;
  font-family: "Helvetica Now Text", sans-serif;
  font-size: 2rem;
  font-weight: 300;
  letter-spacing: -0.01em;
  line-height: 1.1;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결, 대문자, 최소 단어 | "THE ITEM", "NEW IN" |
| Primary CTA | 동사형, 대문자 | "ADD", "SHOP NOW" |
| Secondary CTA | 카테고리명 단순 나열 | "WOMAN", "MAN", "KIDS" |
| Badge | 상태 한 단어 | "SALE", "NEW" |
| Tone | 에디토리얼·미니멀·중립적 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Zara — copy into your root stylesheet */
:root {
  /* Fonts */
  --zara-font-family: "Helvetica Now Text", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --zara-font-weight-normal: 300;
  --zara-font-weight-bold: 700;

  /* Brand — Monochrome */
  --zara-color-brand: #000000;
  --zara-color-brand-light: #333333;

  /* Surfaces */
  --zara-bg-page: #FFFFFF;
  --zara-bg-dark: #141414;
  --zara-text: #000000;
  --zara-text-muted: #666666;

  /* Key spacing */
  --zara-space-sm: 8px;
  --zara-space-md: 16px;
  --zara-space-lg: 40px;

  /* Radius */
  --zara-radius-sm: 0;
  --zara-radius-md: 0;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Zara
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#000000',
          light: '#333333',
        },
        neutral: {
          5:  '#F2F2F2',
          10: '#E5E5E5',
          20: '#CCCCCC',
          40: '#999999',
          60: '#666666',
          80: '#333333',
        },
        sale: '#23F444',
        danger: '#E90D01',
      },
      fontFamily: {
        sans: ['"Helvetica Now Text"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
        editorial: ['"Times New Roman"', '"Helvetica Now Text"', 'Arial', 'Sans-Serif'],
      },
      fontWeight: {
        normal: '300',
        medium: '500',
        bold: '700',
      },
      borderRadius: {
        DEFAULT: '0',
        sm: '0',
        md: '0',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | --zara-color-brand | `#000000` |
| Background | --zara-bg-page | `#FFFFFF` |
| Text primary | --zara-text | `#000000` |
| Text muted | --zara-text-muted | `#666666` |
| Border | N/A | `#000000` |
| Success / Sale | --color-sales | `#23F444` |
| Error | --color-semantic-danger-high | `#E90D01` |

### Example Component Prompts

#### Hero Section
```
Zara 스타일 히어로 섹션을 만들어줘.
- 전폭 패션 화보 이미지 배경 (aspect-ratio: 16/9)
- 텍스트 오버레이: "THE ITEM", Helvetica Now Text, 2rem, weight 300, color #FFFFFF
- 서브: 0.8125rem, weight 300, letter-spacing 0.05em, uppercase
- CTA 버튼: bg #FFFFFF, text #000000, radius 0, padding 12px 20px
- 최대 너비: 100% (전폭)
```

#### Card Component
```
Zara 스타일 상품 카드를 만들어줘.
- 카드 배경: 없음 (이미지가 카드)
- border: none, radius: 0, shadow: 없음
- 이미지: aspect-ratio 4/5, object-fit cover, 전폭
- 제목: Helvetica Now Text, 0.8125rem, weight 300, color #000000
- 가격: 0.8125rem, weight 300, color #000000
- hover: 이미지 살짝 scale(1.02)
```

#### Badge
```
Zara 스타일 배지를 만들어줘.
- font: Helvetica Now Text, 0.625rem, weight 300, letter-spacing 0.05em, uppercase
- padding: 2px 6px, radius: 0
- 기본: bg #000000, text #FFFFFF
- 세일: bg #23F444, text #000000
```

#### Navigation
```
Zara 스타일 상단 네비게이션을 만들어줘.
- 높이: 48px, bg: #FFFFFF, border-bottom: 1px solid #000000
- 로고: 중앙 정렬 "ZARA"
- 링크: Helvetica Now Text, 0.8125rem, weight 300, color #000000, uppercase
- hover: underline
```

### Iteration Guide

- **색상 변경 시**: 흑백 기준. 색을 추가할 때는 상태 컬러(`#E90D01`, `#23F444`)만.
- **폰트 변경 시**: weight 300이 기본. 임의로 400 이상 올리지 말 것.
- **여백 조정 시**: 각 섹션의 padding은 40px~80px 수준. 빠듯하게 주지 말 것.
- **새 컴포넌트 추가 시**: border-radius 0, border 없음 패턴. 그림자 절대 금지.
- **이미지**: 4:5 세로 비율 유지. object-fit: cover.
- **반응형**: 767px 기준으로 2열↔4열 전환.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- body font-weight를 `300`으로 고정 (자라의 정체성)
- 버튼·카드 radius를 `0`으로 (각진 모서리)
- 그림자 대신 `1px solid #000000` border 또는 border 없음
- 상품 이미지에 `aspect-ratio: 4/5` 세로형
- 텍스트는 `uppercase + letter-spacing: 0.05em` 조합
- 색상은 흑백만. 세일만 `#23F444`

### ❌ DON'T
- font-weight `400` 이상 body에 사용 금지
- 버튼에 둥근 radius(8px 이상) 추가 금지
- box-shadow 사용 금지 (자라 CSS에 없음)
- 채도 있는 브랜드 컬러 추가 금지 (자라는 monochrome)
- 배경에 `#F5F5F5` 같은 온화한 회색 금지 (순백 `#FFFFFF`만)
- `Times New Roman`을 body 폰트로 쓰지 말 것 (에디토리얼 헤드라인 전용)
