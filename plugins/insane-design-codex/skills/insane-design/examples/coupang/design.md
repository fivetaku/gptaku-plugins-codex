---
slug: coupang
service_name: Coupang
site_url: https://www.coupang.com
fetched_at: 2026-04-15
default_theme: light
brand_color: "#346AFF"
primary_font: Apple SD Gothic Neo
font_weight_normal: 400
token_prefix: --ui-c-*
---

# DESIGN.md — Coupang (Codex Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

쿠팡은 한국 최대 이커머스 플랫폼답게 **기능 밀도 최우선의 실용적 UI**를 구사한다. 흰 배경 `#FFFFFF` 위에 짙은 텍스트 `#212B36`이 촘촘하게 배치되고, 쿠팡 시그니처 블루 `#346AFF`가 CTA·링크·배지 등 모든 능동적 요소에 집중 투입된다. 장식보다 정보 전달이 우선이며 `애플처럼 비워라`는 미감과 정반대다.

색상 전략은 단순하다: 배경은 `#FFFFFF` 순백, 텍스트는 `#212B36`(다크 잉크), 브랜드 블루 `#346AFF`가 CTAㆍ탭ㆍ강조에 독점 사용된다. 빨강 `#CB1400`은 프로모션 가격과 긴급 배지에 한정되고, 중간 회색 `#DDDDDD`~`#888888` 구간이 구분선·보조 텍스트를 담당한다. 채도 있는 색은 파랑과 빨강 두 가지뿐이다.

한국어 UI 최적화를 위해 `Apple SD Gothic Neo`를 1순위 폰트로 세팅하고, 다국어 폴백으로 `Noto Sans KR`·`Roboto`·`Helvetica Neue`를 순서대로 연결한다. 웨이트는 주로 400(body)·700(제목·강조)로 양극화되어 있으며, `Tahoma`가 일부 레거시 컴포넌트에 남아 있다.

여백은 소형 단위 중심(4px·8px·12px·16px)이며 `max-width: 1600px`의 넓은 컨테이너 안에서 촘촘한 그리드로 상품을 가득 채운다. 섹션 간 분리는 `#DDDDDD` 라인이나 배경색 교체(흰색↔`#F5F5F5`)로 처리한다. 그림자(box-shadow)는 CSS에 거의 없고, 카드 구분은 테두리 1px로 한다.

인터랙션은 `.15s` 단일 transition duration 체계이며 부드럽기보다 즉각 반응하는 느낌을 준다. hover 시 색상 변화(파랑 → 짙은 파랑)가 주 피드백 수단이다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 쿠팡처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Apple SD Gothic Neo", "Noto Sans KR", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #212B36; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #346AFF; }
```

**절대 하지 말아야 할 것 하나**: CTA 버튼에 `#0066CC` 같은 임의 파랑을 쓰는 것. 쿠팡의 정확한 브랜드 블루는 `#346AFF`(rgb 52 106 255)이며, 조금만 달라도 즉시 어색해 보인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.coupang.com` |
| Fetched | 2026-04-15 |
| Extractor | Playwright MCP (headless Chromium, bot-bypass) |
| HTML size | 359,122 bytes (Next.js SSR) |
| CSS files | 14개 외부 (`assets.coupangcdn.com`) + 0 인라인, 총 364,760자 |
| Token prefix | `--ui-c-*` (컴포넌트 액션 토큰), `--tw-*` (Tailwind v3 유틸리티) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (assets.coupangcdn.com CDN 서빙)
- **Design system**: 커스텀 — prefix `--ui-c-*` (button, input 등 컴포넌트 토큰)
- **CSS architecture**: Tailwind v3 유틸리티 + 커스텀 컴포넌트 CSS
  ```
  --ui-c-button-*   컴포넌트 사이즈/radius 토큰
  --tw-*            Tailwind 런타임 변수 (border-spacing, translate 등)
  fw-*              커스텀 Tailwind prefix 클래스
  ```
- **Class naming**: `fw-` prefix Tailwind JIT 클래스 (예: `fw-bg-[#346AFF]`, `fw-text-[#346AFF]`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 시스템 폰트 우선 (Apple SD Gothic Neo → Noto Sans KR → Roboto)
- **Canonical anchor**: `#346AFF` — 모든 CTA·링크·강조 요소의 시그니처 블루

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `Apple SD Gothic Neo` (macOS/iOS 시스템 폰트)
- **Fallback chain**: `Noto Sans KR` → `Noto Sans JP` → `Noto Sans TC` → `Roboto` → `Helvetica Neue` → `Arial` → `sans-serif`
- **Legacy**: `Tahoma` (구형 컴포넌트 일부)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --coupang-font-family: "Apple SD Gothic Neo", "Noto Sans KR", "Noto Sans JP", "Noto Sans", Roboto, "Helvetica Neue", Arial, sans-serif;
  --coupang-font-weight-normal: 400;
  --coupang-font-weight-bold: 700;
}
body {
  font-family: var(--coupang-font-family);
  font-weight: var(--coupang-font-weight-normal);
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| xs / caption | 11px | 400 | 1.4 | 0 |
| sm / label | 12px | 400–700 | 1.5 | 0 |
| base / body | 14px | 400 | 1.6 | 0 |
| md | 16px | 400–700 | 1.5 | 0 |
| lg | 18px | 700 | 1.4 | 0 |
| xl | 24px | 700 | 1.3 | -0.01em |

> ⚠️ 12px가 DOM 빈도 최다(96회). 쿠팡은 가격·배지·레이블 텍스트가 극소 사이즈에 집중되어 있다. 14px 이하에서 font-weight:700으로 가독성을 확보한다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (단일 컬러)

| Token | Hex |
|---|---|
| brand-light | `#7A9EFF` |
| brand | `#346AFF` |
| brand-dark | `#2A55CC` |

### 06-2. Brand Dark Variant

> N/A — 쿠팡은 다크 모드 없음. 단일 light 테마.

### 06-3. Neutral Ramp

| Step | Light |
|---|---|
| 0 | `#FFFFFF` |
| 100 | `#F5F5F5` |
| 200 | `#EEEEEE` |
| 300 | `#DDDDDD` |
| 400 | `#CCCCCC` |
| 500 | `#888888` |
| 700 | `#555555` |
| 900 | `#212B36` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Error / Promo | main | `#CB1400` |
| Success | main | `#2E7D32` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| color-brand | `#346AFF` | CTA, 링크, 탭 활성 |
| color-promo | `#CB1400` | 할인 가격, 프로모 배지 |
| color-text | `#212B36` | 기본 텍스트 |
| color-text-muted | `#888888` | 보조 텍스트, 메타 |
| color-border | `#DDDDDD` | 구분선, 카드 테두리 |
| color-bg | `#FFFFFF` | 페이지 배경 |
| color-bg-alt | `#F5F5F5` | 섹션 교차 배경 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| --swiper-theme-color | `#007aff` | Swiper 기본 (브랜드 블루 아님) |
| --tw-ring-offset-color | `#fff` | Tailwind focus ring 오프셋 |
| --ui-c-button-radius-radius | `4px` | 버튼 radius 토큰 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 139 | neutral — 배경/카드 |
| 2 | `#212B36` | 61 | chromatic — 기본 텍스트 |
| 3 | `#346AFF` | 55 | chromatic — 브랜드 블루 |
| 4 | `#CB1400` | 53 | chromatic — 프로모 레드 |
| 5 | `#DDDDDD` | 40 | neutral — 구분선 |
| 6 | `#F5F5F5` | 34 | neutral — 배경 교차 |
| 7 | `#888888` | 28 | neutral — 보조 텍스트 |
| 8 | `#000000` | 22 | neutral — 강조 텍스트 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-1 | 4px | 아이콘-텍스트 간격, 인라인 gap |
| space-2 | 8px | 버튼 내부 padding, 배지 |
| space-3 | 12px | 카드 내부 패딩 |
| space-4 | 16px | 섹션 내부 패딩 |
| space-5 | 20px | 컴포넌트 간격 |
| space-6 | 24px | 카드 외부 gap |
| space-8 | 32px | 섹션 구분 |

**주요 alias**:
- `--ui-c-button-md-px` → `26px` (버튼 수평 패딩)
- `--ui-c-button-md-py` → `5px` (버튼 수직 패딩)
- `--ui-c-button-md-min-height` → `32px` (버튼 최소 높이)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | `0` | 검색창, 구분선 |
| radius-sm | `4px` | 버튼(`--ui-c-button-radius-radius`), 배지 |
| radius-md | `8px` | 카드, 모달 |
| radius-full | `100px` | 알약형 버튼, 태그 |

---

## 09. Shadows
<!-- SOURCE: auto -->

> N/A — 쿠팡 CSS에 box-shadow 토큰이 없음. 카드 구분은 `1px solid #DDDDDD` border 사용.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| duration-fast | `0.15s` | 모든 hover/active 전환 |
| easing-default | `ease` | 기본값 |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1600px` (플랫폼 최대), 일반 컨텐츠 `1024px`
- **Grid type**: CSS Grid + Flexbox 혼용
- **Column count**: 최대 6열 (상품 그리드 기준)
- **Gutter**: 16px

### Hero
- Layout: 배너 슬라이드 (전폭, max-width 없음)
- Background: 이미지/프로모 배경
- H1: N/A — 히어로는 배너 이미지 전용
- Max-width: 100%

### Section Rhythm
```css
section {
  padding: 16px 0;
  max-width: 1600px;
}
```

### Card Patterns
- **Card background**: `#FFFFFF`
- **Card border**: `1px solid #DDDDDD`
- **Card radius**: `4px`–`8px`
- **Card padding**: `12px`
- **Card shadow**: 없음 (border 전용)

### Navigation Structure
- **Type**: 수평 메가메뉴 + 카테고리 사이드바
- **Position**: sticky top
- **Height**: 약 56px
- **Background**: `#FFFFFF`
- **Border**: `1px solid #DDDDDD` 하단

### Content Width
- **Prose max-width**: N/A
- **Container max-width**: `1600px`
- **Sidebar width**: 210px (카테고리)

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | 600px | 1열 상품 리스트, 햄버거 메뉴 |
| Tablet | 768px | 2열 전환 |
| Desktop | 1024px | 4~5열 그리드 |
| Large | 1600px | 최대 컨테이너 너비 |

### Touch Targets
- **Minimum tap size**: 44px
- **Button height (mobile)**: 44px
- **Input height (mobile)**: 40px

### Collapsing Strategy
- **Navigation**: 햄버거 메뉴 → 슬라이드 오버레이
- **Grid columns**: 6열 → 4열 → 2열 → 1열
- **Sidebar**: 숨김 → 오버레이
- **Hero**: 전폭 배너 유지

### Image Behavior
- **Strategy**: 반응형 `<img>` + CDN 리사이즈
- **Max-width**: 100%
- **Aspect ratio handling**: 고정 비율 (상품 이미지 1:1)

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<!-- Primary CTA -->
<button class="coupang-btn-primary">
  로켓배송 구매
</button>
```

```css
.coupang-btn-primary {
  background: #346AFF;
  color: #FFFFFF;
  font-family: "Apple SD Gothic Neo", sans-serif;
  font-size: 14px;
  font-weight: 700;
  border: none;
  border-radius: 4px;
  padding: 5px 26px;
  min-height: 32px;
  cursor: pointer;
  transition: background 0.15s ease;
}
.coupang-btn-primary:hover { background: #2A55CC; }
```

| Spec | Value |
|---|---|
| bg | `#346AFF` |
| text | `#FFFFFF` |
| radius | `4px` |
| height (md) | `32px` |
| px (md) | `26px` |
| hover bg | `#2A55CC` |

### Badges

```css
.coupang-badge {
  background: #CB1400;
  color: #FFFFFF;
  font-size: 11px;
  font-weight: 700;
  border-radius: 2px;
  padding: 1px 4px;
}
.coupang-badge-rocket {
  background: #346AFF;
  color: #FFFFFF;
  border-radius: 2px;
  font-size: 11px;
}
```

### Cards & Containers

```css
.coupang-product-card {
  background: #FFFFFF;
  border: 1px solid #DDDDDD;
  border-radius: 4px;
  padding: 12px;
}
.coupang-product-card:hover {
  border-color: #346AFF;
}
```

### Navigation

```css
.coupang-nav {
  background: #FFFFFF;
  border-bottom: 1px solid #DDDDDD;
  height: 56px;
  position: sticky;
  top: 0;
  z-index: 100;
}
.coupang-nav-link {
  color: #212B36;
  font-size: 14px;
  font-weight: 400;
}
.coupang-nav-link:hover { color: #346AFF; }
```

### Inputs & Forms

```css
.coupang-search-input {
  border: 2px solid #346AFF;
  border-radius: 0;
  height: 40px;
  padding: 0 16px;
  font-size: 14px;
  color: #212B36;
  background: #FFFFFF;
}
```

### Hero Section

```css
.coupang-hero-banner {
  width: 100%;
  background: #346AFF;
  padding: 24px 16px;
  text-align: center;
}
.coupang-hero-headline {
  font-size: 24px;
  font-weight: 700;
  color: #FFFFFF;
  line-height: 1.3;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 혜택 중심, 숫자 강조 | "~30,000원 쿠폰받기" |
| Primary CTA | 동사+목적어, 2~4자 | "구매하기", "쿠폰받기" |
| Secondary CTA | 부드러운 안내 | "자세히 보기" |
| Badge | 핵심 혜택 1~3단어 | "로켓배송", "최저가" |
| Tone | 한국형 세일즈, 숫자·혜택 직접적 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Coupang — copy into your root stylesheet */
:root {
  /* Fonts */
  --coupang-font-family: "Apple SD Gothic Neo", "Noto Sans KR", Roboto, "Helvetica Neue", Arial, sans-serif;
  --coupang-font-weight-normal: 400;
  --coupang-font-weight-bold: 700;

  /* Brand */
  --coupang-color-brand: #346AFF;
  --coupang-color-brand-dark: #2A55CC;
  --coupang-color-promo: #CB1400;

  /* Surfaces */
  --coupang-bg-page: #FFFFFF;
  --coupang-bg-alt: #F5F5F5;
  --coupang-text: #212B36;
  --coupang-text-muted: #888888;

  /* Key spacing */
  --coupang-space-sm: 8px;
  --coupang-space-md: 16px;
  --coupang-space-lg: 24px;

  /* Radius */
  --coupang-radius-sm: 4px;
  --coupang-radius-md: 8px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Coupang
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#346AFF',
          dark: '#2A55CC',
          light: '#7A9EFF',
        },
        promo: '#CB1400',
        neutral: {
          100: '#F5F5F5',
          200: '#EEEEEE',
          300: '#DDDDDD',
          500: '#888888',
          900: '#212B36',
        },
      },
      fontFamily: {
        sans: ['"Apple SD Gothic Neo"', '"Noto Sans KR"', 'Roboto', '"Helvetica Neue"', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold: '700',
      },
      borderRadius: {
        sm: '4px',
        DEFAULT: '4px',
        md: '8px',
        full: '100px',
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
| Brand primary | --coupang-color-brand | `#346AFF` |
| Background | --coupang-bg-page | `#FFFFFF` |
| Text primary | --coupang-text | `#212B36` |
| Text muted | --coupang-text-muted | `#888888` |
| Border | N/A | `#DDDDDD` |
| Promo / Error | --coupang-color-promo | `#CB1400` |
| Success | N/A | `#2E7D32` |

### Example Component Prompts

#### Hero Section
```
쿠팡 스타일 프로모션 배너를 만들어줘.
- 배경: #346AFF
- 제목: "Apple SD Gothic Neo", 24px, weight 700, color #FFFFFF
- 서브: 18px, color rgba(255,255,255,0.85)
- CTA 버튼: bg #FFFFFF, text #346AFF, radius 4px, padding 5px 26px
- 최대 너비: 100% (전폭 배너)
```

#### Card Component
```
쿠팡 스타일 상품 카드를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #DDDDDD, radius: 4px
- padding: 12px
- shadow: 없음
- hover 시: border-color #346AFF
- 가격: 18px, weight 700, color #212B36
- 할인가: 14px, weight 700, color #CB1400
- 배송: 12px, color #346AFF, "로켓배송" 배지
```

#### Badge
```
쿠팡 스타일 배지를 만들어줘.
- font: "Apple SD Gothic Neo", 11px, weight 700
- padding: 1px 4px, radius: 2px
- 로켓배송: bg #346AFF, text #FFFFFF
- 할인: bg #CB1400, text #FFFFFF
- 최저가: bg #212B36, text #FFFFFF
```

#### Navigation
```
쿠팡 스타일 상단 네비게이션을 만들어줘.
- 높이: 56px, bg: #FFFFFF, border-bottom: 1px solid #DDDDDD
- 로고: 좌측, 쿠팡 블루 #346AFF
- 검색창: border 2px solid #346AFF, border-radius 0, 중앙 배치
- 링크: 14px, weight 400, color #212B36
- CTA: bg #346AFF, text #FFFFFF, radius 4px
```

### Iteration Guide

- **색상 변경 시**: `#346AFF` 브랜드 블루 기준. 프로모는 `#CB1400`. 두 색만 사용.
- **폰트 변경 시**: weight 400 기본. 700은 가격·CTA에만.
- **여백 조정 시**: 4의 배수(4/8/12/16/24px) 단위로만.
- **새 컴포넌트 추가 시**: 1px solid `#DDDDDD` border + 4px radius 패턴을 따를 것.
- **반응형**: 768px·1024px·1600px 기준. 그 사이 임의 breakpoint 추가 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- CTA 버튼에 `#346AFF` 정확히 사용
- 한국어 UI에 `Apple SD Gothic Neo` 1순위로 지정
- 할인가·프로모 배지에 `#CB1400` 레드 사용
- 카드 구분은 `1px solid #DDDDDD` 테두리만 (그림자 없음)
- 버튼 radius는 `4px` — 쿠팡 특유의 각진 느낌
- font-weight는 400(body)와 700(강조) 두 단계만

### ❌ DON'T
- `#0066CC` 등 임의 파랑 사용 금지 — 반드시 `#346AFF`
- 배경에 `#F0F0F0` 등 임의 회색 금지 — 교차 배경은 `#F5F5F5`
- 그림자(box-shadow) 남발 금지 — 쿠팡은 border 전용
- 버튼 radius를 `8px` 이상으로 올리지 말 것
- 폰트 크기를 10px 이하로 줄이지 말 것 (접근성)
- 다크 모드 구현 시도 금지 — 쿠팡은 light-only
