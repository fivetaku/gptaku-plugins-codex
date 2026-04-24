---
slug: dior
service_name: Dior
site_url: https://www.dior.com
fetched_at: 2026-04-15
default_theme: light
brand_color: "#33383C"
primary_font: Hellix
font_weight_normal: 500
token_prefix: --ot-*
---

# DESIGN.md — Dior (Codex Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

디올(Dior)은 럭셔리 패션 하우스의 디지털 표현이다. **근엄한 회색 `#33383C`가 브랜드 앵커**로 작동하고, 흰색 배경 위에 무게감 있는 세리프·산세리프 조합이 클래식한 쿠튀르 톤을 만든다. 밝은 파랑이나 강한 원색은 완전히 배제되며, 절제된 팔레트로 프리미엄 포지셔닝을 강화한다.

색상 전략은 **다크 뉴트럴 모노크롬**이다. 브랜드 앵커 `#33383C`(다크 차콜)와 흰색 `#FFFFFF`·검정 `#000000`이 삼각축을 이루고, `--ot-black-*` 램프(`#ACB2B4`·`#7B8487`·`#5D676C`·`#33383C`)가 그레이 스케일을 4단계로 분리한다. 유일한 포인트는 `#03B2CB`(포커스 링)와 같이 시스템 UI에만 한정된 컬러다.

폰트는 자체 커스텀 서체 `Hellix`를 primary로, `Atacama VAR`를 display headline에 사용한다. font-weight 500(medium)이 기본 body이며, 일반 사이트의 400(regular)보다 한 단계 무겁다. `Century Gothic Std`가 일부 레거시 아이콘·특수 UI에 잔존한다. `ABCDiorIcons` 아이콘 폰트가 별도로 운영된다.

여백은 프리미엄 브랜드 특유의 넉넉함을 갖는다. 컨텐츠는 `max-width: 896px`로 중앙 수렴하고, 상·하 섹션 패딩이 충분하다. 카드 경계는 색상 변화와 미세 border로 표현하며, box-shadow는 없다.

모션은 MUI(Material UI) 기반의 `cubic-bezier(0.4, 0, 0.2, 1)` 250ms 트랜지션을 사용한다. 빠르지도 느리지도 않은 품격 있는 속도감.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Dior처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: Hellix, Arial, sans-serif;
  font-weight: 500;  /* Medium — 400 아님 */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #33383C; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #33383C; }
```

**절대 하지 말아야 할 것 하나**: 텍스트를 `#000000` 순수 검정으로 설정하는 것. 디올의 기본 텍스트는 `#33383C`(다크 차콜)이며, 이 미묘한 차이가 럭셔리 브랜드의 따뜻한 어두움을 만든다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.dior.com/en_us` |
| Fetched | 2026-04-15 |
| Extractor | Playwright MCP (headless Chromium, bot-bypass) |
| HTML size | 545,862 bytes (Next.js SSR, couture-catalog-v2) |
| CSS files | 2개 외부 (`dior.com/couture-catalog-v2-assets`) + 191,381자 인라인, 총 244,454자 |
| Token prefix | `--ot-*` (Dior 자체 디자인 토큰), `--variant-*` (MUI 기반 컴포넌트 변수) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (couture-catalog-v2 빌드)
- **Design system**: MUI(Material UI) + 커스텀 `--ot-*` 토큰 레이어
- **CSS architecture**: MUI 컴포넌트 CSS + Dior 오버라이드 토큰
  ```
  --ot-black-*       Dior 전용 gray 램프 (100~400)
  --ot-white-*       흰 side 램프 (100~200)
  --variant-*        MUI 컴포넌트 상태 변수 (containedBg, outlinedBorder 등)
  ```
- **Class naming**: MUI 자동 생성 (`mui-*`, `.MuiButton-*`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 CDN 서빙 (`Hellix`, `Atacama VAR`, `ABCDiorIcons`)
- **Canonical anchor**: `#33383C` — 모든 텍스트·CTA·버튼 배경이 이 다크 차콜 기반

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `Hellix` (Dior 전용 커스텀, 유료)
- **Display headline**: `Atacama VAR` (가변 폰트)
- **Icon font**: `ABCDiorIcons`
- **Legacy**: `Century Gothic Std`, `DinCondensedBold`
- **Fallback**: `Arial`, `sans-serif`
- **Weight normal / bold**: `500` / `700`

```css
:root {
  --dior-font-family: Hellix, ABCDiorIcons, Arial, sans-serif;
  --dior-font-family-display: "Atacama VAR", ABCDiorIcons, Arial, sans-serif;
  --dior-font-weight-normal: 500;
  --dior-font-weight-bold: 700;
}
body {
  font-family: var(--dior-font-family);
  font-weight: var(--dior-font-weight-normal);
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| xs / caption | 0.75rem (12px) | 500 | 1.5 | 0.02em |
| base / body | 0.875rem (14px) | 500 | 1.6 | 0 |
| md | 1rem (16px) | 500–700 | 1.5 | 0 |
| lg | 1.5rem (24px) | 400–500 | 1.3 | -0.01em |
| display | 2rem+ | 400 | 1.1 | -0.02em |

> ⚠️ Dior body font-weight는 500(medium)이 기본. 0.875rem(14px)이 body 표준. 대형 display 타이틀은 Atacama VAR weight 400으로 가볍게.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Dark Neutral)

| Token | Hex |
|---|---|
| --ot-black-100 | `#ACB2B4` |
| --ot-black-200 | `#7B8487` |
| --ot-black-300 | `#5D676C` |
| --ot-black-400 | `#33383C` |
| brand / black | `#000000` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| --ot-white-100 | `#E5E5E5` |
| --ot-white-200 | `#DADADA` |

### 06-3. Neutral Ramp

| Step | Light |
|---|---|
| 100 | `#ACB2B4` (cool light gray) |
| 200 | `#7B8487` |
| 300 | `#5D676C` |
| 400 | `#33383C` (anchor) |
| max | `#000000` |

### 06-4. Accent Families

> N/A — 디올 UI에 채도 있는 브랜드 액센트 없음.

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --variant-containedBg | `#33383C` | 채워진 버튼 배경 |
| --variant-containedColor | `#FFFFFF` | 채워진 버튼 텍스트 |
| --variant-outlinedColor | `#33383C` | 외곽선 버튼 텍스트/border |
| --variant-textColor | `#33383C` | 텍스트 버튼 |
| --ot-link-text-color | `#7B8487` | 링크 텍스트 |
| focus ring | `#03B2CB` | 접근성 포커스 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| --variant-outlinedBorder | `rgba(51,56,60,0.5)` | 버튼 외곽선 |
| --variant-textBg | `rgba(51,56,60,0.04)` | 텍스트 버튼 hover bg |
| --variant-outlinedBg | `rgba(51,56,60,0.04)` | 외곽선 버튼 hover bg |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#33383CFF` | 114 | neutral — 브랜드 앵커 다크 차콜 |
| 2 | `#FFFFFF` | 97 | neutral — 배경 |
| 3 | `#000000` | 58 | neutral — 강조 텍스트 |
| 4 | `#D8D8D8` | 40 | neutral — 구분선 |
| 5 | `#ACB2B4FF` | 38 | neutral — ot-black-100 (연한 회색) |
| 6 | `#7B8487` | 22 | neutral — ot-black-200 |
| 7 | `#5D676C` | 14 | neutral — ot-black-300 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 아이콘 gap |
| space-sm | 8px | 인라인 패딩 |
| space-md | 16px | 컴포넌트 패딩 |
| space-lg | 24px | 섹션 내부 |
| space-xl | 40px | 섹션 상하 |
| space-2xl | 80px | 대형 섹션 |

**주요 alias**:
- 버튼 패딩: `16px 24px` (중형 CTA 기준)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | `0` | 기본 버튼, 입력창 |
| radius-xs | `2.5px` | 작은 배지 |
| radius-sm | `10px` | 일부 카드 |
| radius-lg | `1.5rem` | 알림 버블 |
| radius-full | `100%` | 아바타, 원형 아이콘 |

---

## 09. Shadows
<!-- SOURCE: auto -->

> N/A — 디올 CSS에 독자적 box-shadow 없음. MUI 기본값만 간헐적으로 존재.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| duration | `250ms` | 모든 MUI 컴포넌트 전환 |
| easing-standard | `cubic-bezier(0.4, 0, 0.2, 1)` | 색상/background 전환 |
| duration-bg | `0.3s` | 배경색 전환 |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `896px` (컨텐츠 영역)
- **Grid type**: CSS Grid + Flexbox
- **Column count**: 3열 (상품), 2열 (컬렉션)
- **Gutter**: 16px–24px

### Hero
- Layout: 전폭 이미지 + 오버레이 텍스트
- Background: 화보 이미지 (어두운 오버레이 포함)
- H1: `Atacama VAR`, 2rem+, weight 400, color `#FFFFFF`
- Max-width: 100%

### Section Rhythm
```css
section {
  padding: 40px 0;
  max-width: 896px;
  margin: 0 auto;
}
```

### Card Patterns
- **Card background**: `#FFFFFF`
- **Card border**: `none` 또는 `1px solid #D8D8D8`
- **Card radius**: `0`–`10px`
- **Card padding**: `16px`
- **Card shadow**: 없음

### Navigation Structure
- **Type**: 수평 카테고리 메뉴
- **Position**: sticky top
- **Height**: 약 60px
- **Background**: `#FFFFFF`
- **Border**: `1px solid #D8D8D8` 하단

### Content Width
- **Prose max-width**: `896px`
- **Container max-width**: `896px`–`100%`
- **Sidebar width**: N/A

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | 600px | 1열, 햄버거 메뉴 |
| Tablet | 600px–900px | 2열 그리드 |
| Desktop | 900px+ | 3열 그리드 |
| Large | 1200px+ | 최대 레이아웃 |

### Touch Targets
- **Minimum tap size**: 44px
- **Button height (mobile)**: 44px
- **Input height (mobile)**: 44px

### Collapsing Strategy
- **Navigation**: 햄버거 → 전폭 오버레이
- **Grid columns**: 3열 → 2열 → 1열
- **Sidebar**: N/A
- **Hero**: 전폭 유지

### Image Behavior
- **Strategy**: 반응형 `object-fit: cover`
- **Max-width**: 100%
- **Aspect ratio handling**: 2:3 세로 (패션 이미지)

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="dior-btn-primary">Shop Now</button>
```

```css
.dior-btn-primary {
  background: #33383C;
  color: #FFFFFF;
  font-family: Hellix, Arial, sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  border: none;
  border-radius: 0;
  padding: 16px 24px;
  min-height: 44px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 250ms cubic-bezier(0.4, 0, 0.2, 1), color 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.dior-btn-primary:hover { background: #000000; }

.dior-btn-outline {
  background: transparent;
  color: #33383C;
  border: 1px solid rgba(51, 56, 60, 0.5);
  border-radius: 0;
  padding: 16px 24px;
  font-family: Hellix, Arial, sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.dior-btn-outline:hover { background: rgba(51, 56, 60, 0.04); }
```

| Spec | Value |
|---|---|
| bg | `#33383C` |
| text | `#FFFFFF` |
| radius | `0` |
| height | `44px` |
| letter-spacing | `0.08em` |
| transition | `250ms cubic-bezier(0.4, 0, 0.2, 1)` |

### Badges

```css
.dior-badge {
  background: #33383C;
  color: #FFFFFF;
  font-family: Hellix, Arial, sans-serif;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 0;
}
```

### Cards & Containers

```css
.dior-product-card {
  background: #FFFFFF;
  border: none;
  padding: 0;
}
.dior-product-card-info {
  padding: 16px 0;
}
.dior-product-card-title {
  font-family: Hellix, Arial, sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  color: #33383C;
  letter-spacing: 0.02em;
}
.dior-product-card-price {
  font-size: 0.875rem;
  font-weight: 500;
  color: #7B8487;
}
```

### Navigation

```css
.dior-nav {
  background: #FFFFFF;
  border-bottom: 1px solid #D8D8D8;
  height: 60px;
  position: sticky;
  top: 0;
  z-index: 100;
}
.dior-nav-link {
  font-family: Hellix, Arial, sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  color: #33383C;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  text-decoration: none;
}
.dior-nav-link:hover { color: #000000; }
```

### Inputs & Forms

```css
.dior-input {
  border: none;
  border-bottom: 1px solid #33383C;
  border-radius: 0;
  height: 44px;
  padding: 0;
  font-family: Hellix, Arial, sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  color: #33383C;
  background: transparent;
  outline: none;
}
.dior-input:focus { border-bottom-color: #000000; outline: 2px solid #03B2CB; }
```

### Hero Section

```css
.dior-hero {
  position: relative;
  width: 100%;
  aspect-ratio: 3/2;
  overflow: hidden;
}
.dior-hero img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.dior-hero-caption {
  position: absolute;
  bottom: 40px;
  left: 40px;
  color: #FFFFFF;
  font-family: "Atacama VAR", Arial, sans-serif;
  font-size: 3rem;
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1.1;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 프랑스어·영어 혼용, 격조 있는 어구 | "Fashion & Accessories", "Fragrance & Beauty" |
| Primary CTA | 동사 + 짧은 명사, 첫글자 대문자 | "Shop Now", "Discover" |
| Secondary CTA | 카테고리명 | "See all" |
| Badge | 없음 (럭셔리 브랜드는 배지 최소화) | |
| Tone | 격조 있는 영어·프랑스어, 과도한 세일 언어 금지 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Dior — copy into your root stylesheet */
:root {
  /* Fonts */
  --dior-font-family: Hellix, ABCDiorIcons, Arial, sans-serif;
  --dior-font-family-display: "Atacama VAR", Arial, sans-serif;
  --dior-font-weight-normal: 500;
  --dior-font-weight-bold: 700;

  /* Brand — Dark Neutral */
  --dior-color-brand: #33383C;
  --dior-color-brand-100: #ACB2B4;
  --dior-color-brand-200: #7B8487;
  --dior-color-brand-300: #5D676C;
  --dior-color-brand-400: #33383C;

  /* Surfaces */
  --dior-bg-page: #FFFFFF;
  --dior-bg-dark: #000000;
  --dior-text: #33383C;
  --dior-text-muted: #7B8487;

  /* Key spacing */
  --dior-space-sm: 8px;
  --dior-space-md: 16px;
  --dior-space-lg: 40px;

  /* Radius */
  --dior-radius-sm: 0;
  --dior-radius-md: 10px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Dior
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          100: '#ACB2B4',
          200: '#7B8487',
          300: '#5D676C',
          400: '#33383C',
          DEFAULT: '#33383C',
          900: '#000000',
        },
        neutral: {
          100: '#E5E5E5',
          200: '#DADADA',
          300: '#D8D8D8',
        },
      },
      fontFamily: {
        sans: ['Hellix', 'Arial', 'sans-serif'],
        display: ['"Atacama VAR"', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '500',
        bold: '700',
      },
      borderRadius: {
        DEFAULT: '0',
        sm: '0',
        md: '10px',
        full: '100%',
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
| Brand primary | --dior-color-brand | `#33383C` |
| Background | --dior-bg-page | `#FFFFFF` |
| Text primary | --dior-text | `#33383C` |
| Text muted | --dior-text-muted | `#7B8487` |
| Border | N/A | `#D8D8D8` |
| Success | N/A | `#2E7D32` |
| Error | N/A | `#D32F2F` |

### Example Component Prompts

#### Hero Section
```
Dior 스타일 히어로 섹션을 만들어줘.
- 전폭 화보 이미지 배경 (aspect-ratio: 3/2)
- 헤드라인: "Atacama VAR", 3rem, weight 400, color #FFFFFF, letter-spacing -0.02em
- 서브텍스트: Hellix, 0.875rem, weight 500, color rgba(255,255,255,0.85), uppercase, letter-spacing 0.08em
- CTA 버튼: bg #FFFFFF, text #33383C, radius 0, padding 16px 24px, uppercase
- 최대 너비: 100%
```

#### Card Component
```
Dior 스타일 상품 카드를 만들어줘.
- 카드 배경: #FFFFFF, border: none, radius: 0, shadow: 없음
- 이미지: aspect-ratio 2/3, object-fit cover
- 제목: Hellix, 0.875rem, weight 500, color #33383C, letter-spacing 0.02em
- 가격: 0.875rem, weight 500, color #7B8487
- hover: 이미지 살짝 scale(1.02), transition 250ms
```

#### Badge
```
Dior 스타일 배지를 만들어줘.
- font: Hellix, 0.75rem, weight 500, letter-spacing 0.08em, uppercase
- padding: 3px 8px, radius: 0
- 기본: bg #33383C, text #FFFFFF
```

#### Navigation
```
Dior 스타일 상단 네비게이션을 만들어줘.
- 높이: 60px, bg: #FFFFFF, border-bottom: 1px solid #D8D8D8
- 로고: 중앙 정렬 "DIOR"
- 링크: Hellix, 0.875rem, weight 500, color #33383C, uppercase, letter-spacing 0.05em
- hover: color #000000
```

### Iteration Guide

- **색상 변경 시**: `#33383C` 기준. 더 밝으면 `#7B8487`, 더 어두우면 `#000000`.
- **폰트 변경 시**: weight 500이 기본. 디스플레이는 Atacama VAR 400.
- **여백 조정 시**: 16px·24px·40px·80px 단계로만.
- **새 컴포넌트 추가 시**: border-radius 0, letter-spacing 0.05em+, uppercase 패턴.
- **transition**: 항상 `250ms cubic-bezier(0.4, 0, 0.2, 1)`.
- **반응형**: 600px·900px·1200px MUI 기준.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 텍스트 기본색을 `#33383C` (순검정 아님)으로 설정
- body font-weight 500으로 고정 (medium)
- 모든 버튼 radius `0` (각진 럭셔리)
- letter-spacing `0.05em` 이상 + uppercase 조합
- transition은 `250ms cubic-bezier(0.4, 0, 0.2, 1)` 유지
- 이미지 비율 2:3 세로형

### ❌ DON'T
- 텍스트를 `#000000` 순검정으로 쓰지 말 것 (앵커는 `#33383C`)
- font-weight 400 body 사용 금지 (500이 기본)
- box-shadow 사용 금지
- 채도 있는 컬러 추가 금지 (포커스 `#03B2CB` 제외)
- 버튼 radius를 8px 이상으로 올리지 말 것
- 배지 남발 금지 — 럭셔리 브랜드는 배지 최소화
