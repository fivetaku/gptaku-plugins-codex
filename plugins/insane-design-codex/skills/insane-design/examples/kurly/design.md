---
schema_version: 3.1
slug: kurly
service_name: Market Kurly
site_url: https://www.kurly.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#BD76FF"
primary_font: Pretendard
font_weight_normal: 400
token_prefix: --kpds_*

bold_direction: "Premium Grocery Warmth"
aesthetic_category: "Premium Grocery Warmth"
signature_element: brand_saturation
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Market Kurly (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Market Kurly(마켓컬리)의 마케팅 사이트는 **"새벽배송의 프리미엄 정서"**를 색 하나에 응축한다. 전체 UI는 순백 `#FFFFFF` 바탕 위에 가장 강한 시그니처 하나만을 반복한다 — 브랜드 퍼플 `#BD76FF`와 그 어두운 짝 `#8D4CC4`. 이 두 보라는 페이지 상단 공지, CTA 버튼, 가격 할인 라벨, 카테고리 배지, 페이지네이션 active 등 "구매의 결정적 순간"에만 등장한다. 넓은 면적은 `#F6F4F9` (연보라 tinted neutral)와 `#F2F5F8` (쿨그레이) 두 layer가 나눠서 맡는다.

색상 전략은 **"보라는 아껴쓰고, 회색은 12단으로 쪼개라"**로 요약된다. 보라 1쌍만큼이나 중요한 것이 grayscale 계단이다: `#F2F5F8` → `#DDE2E8` → `#C0C8D0` → `#A7B2BC` → `#848F9A` → `#626C77` → `#505760` → `#464B52` → `#363A40` → `#303337` → `#222222`. 이 12단이 배경, 카드, 구분선, placeholder, body text, title까지 전부 소화하기 때문에 UI가 "조용하지만 분명하게" 읽힌다. 그 외 10여 종의 카테고리 ramp(orange `#EB5522`, red `#AC2728`, green `#028B61`, teal `#48B1C8`, yellow `#F1D902`)는 프로모션·신선식품 라벨·쿠폰 배지 등 의미가 주어진 순간에만 등장하며 면적을 차지하지 않는다.

타이포그래피는 **Pretendard Variable**을 축으로 하되, 한국 웹 표준을 따르는 **'Noto Sans KR'**이 대규모 텍스트 블록(상품 제목, 추천글)에 병행 사용된다. 본문 기본은 `14px / weight 400 / color #333333`이며, 가격은 `18-24px / weight 700`, 상품 타이틀은 `16px / weight 500`으로 상업적 hierarchy가 엄격하다. variable axis는 쓰지 않고 `100 / 200 / 300 / 400 / 500 / 600 / 700 / 800 / 900` 표준 9단 weight를 사용.

레이아웃은 `1050-1200px` 중앙 정렬 고정폭 + 상단 공지 바(announcement) + GNB 네비 + 3-column 배너 슬라이더 + 4/5-card 상품 그리드로 구성된다. 모바일은 별도 라우트로 전환되지만 데스크톱 홈은 "매일 새벽에 바뀌는 카탈로그 디스플레이"라는 원칙하에 정보 밀도가 매우 높다. radius는 4/6/8/10/12/16/24/32px 배수 시스템이며 `--kpds_ldmw17u` 같은 해시 토큰 뒤에 가려져 있다.

인터랙션은 쇼핑 사이트 관습대로 미세하다. 링크 hover는 underline + 색 tone-up, 카드 hover는 `box-shadow: 0 2px 10px rgba(0,0,0,0.06)` 2-layer로 얕게 뜨는 정도. Swiper 라이브러리 기반 캐러셀이 메인 배너와 상품 섹션에 광범위하게 쓰이며 기본 duration `300ms` ease-out.

### Key Characteristics

- 순백 `#FFFFFF` 배경 + 연보라 surface `#F6F4F9`의 2-layer 조합
- 시그니처 퍼플 한 쌍 `#BD76FF` / `#8D4CC4` — 구매 결정 지점에만
- Grayscale 12단 ramp이 UI의 진짜 뼈대
- Pretendard + Noto Sans KR dual Korean font stack
- 14px 본문 · 엄격한 커머스 hierarchy (가격 24px · title 16px · body 14px)
- `--kpds_*` hashed token 시스템 (260+ 변수)
- Swiper.js 기반 캐러셀 도배 (main banner, product carousel)
- 4-column 상품 그리드 + 1200px 고정 페이지 폭

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Premium Grocery Warmth
> **Aesthetic Category**: Premium Grocery Warmth
> **Signature Element**: 이 사이트는 **순백 배경 위 Kurly-퍼플 한 쌍 + 12단 grayscale 뼈대**로 기억된다.
> **Code Complexity**: medium — hashed CSS variable 시스템 + Pretendard/Noto 이중 폰트 스택, 화려한 모션 없음

---

## 01. Quick Start

> 5분 안에 Kurly처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: Pretendard,"Pretendard Variable","Noto Sans KR",
    -apple-system, BlinkMacSystemFont, system-ui,
    "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #333333;
}

/* 2. 배경 + 서피스 (light only) */
:root {
  --bg: #FFFFFF;
  --surface: #F6F4F9;   /* 연보라 tinted surface */
  --neutral-alt: #F2F5F8; /* 쿨그레이 surface */
  --border: #DDE2E8;
  --text: #222222;
  --text-muted: #848F9A;
}
body { background: var(--bg); color: var(--text); }

/* 3. 브랜드 퍼플 (구매의 순간에만) */
:root {
  --brand: #BD76FF;       /* primary purple */
  --brand-strong: #8D4CC4;/* hover/dark pair */
  --brand-soft: #F6F4F9;  /* tinted bg */
}
```

**절대 하지 말아야 할 것 하나**: 브랜드 퍼플 `#BD76FF`를 섹션 배경이나 큰 면적에 쓰지 마라. Kurly의 퍼플은 CTA, 가격 할인, 공지 bar, active pagination에만 등장하는 포인트 컬러다. 면적으로 쓰는 순간 Twitch가 되고, 포인트로 쓸 때 Kurly가 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.kurly.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | ~97KB (Next.js SSR) |
| CSS files | 1개 외부 (138KB) + 인라인 (87KB) |
| Token prefix | `--kpds_*` (hashed), `--base-*`, `--swiper-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (SSR, React)
- **Design system**: 자체 KPDS(Kurly Product Design System) — 해시 prefix `--kpds_ldmw1*`로 난독화된 토큰 260+개
- **CSS architecture**: core-tier 단일층 (200개 core hex/rem 원자 + alias 없음)
  ```
  core    (--kpds_ldmw172b : #f2f5f8, --kpds_ldmw172f : #848f9a)   raw hex 직결
  util    (--base-color #ebebeb, --highlight-color #f5f5f5)        skeleton/loader
  third   (--swiper-theme-color #007aff)                           Swiper 라이브러리
  ```
- **Class naming**: CSS Modules 해시 기반 (`Product_card__xxx`)
- **Default theme**: light only — dark theme 없음
- **Font loading**: Pretendard CDN + Noto Sans KR web font
- **Canonical anchor**: `#BD76FF` — 시그니처 퍼플, 공지 bar/CTA 배경
- **Library deps**: Swiper (캐러셀), react-datepicker (날짜 선택)

---

## 04. Font Stack

- **Display/Body**: `Pretendard` Variable (SIL Open Font License, orioncactus)
- **Secondary Korean**: `Noto Sans KR` (Google, OFL) — 대량 텍스트 블록
- **Code**: `monospace` (OS 기본)
- **Weight normal / bold**: `400` / `700`
- **Weights used (CSS 실측)**: `100 · 200 · 300 · 400 · 500 · 600 · 700 · 800 · 900`

```css
:root {
  --font-sans:
    Pretendard, "Pretendard Variable",
    -apple-system, BlinkMacSystemFont, system-ui, Roboto,
    "Helvetica Neue", "Segoe UI",
    "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic",
    "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol",
    sans-serif;
  --font-noto:
    'Noto Sans KR', 'malgun gothic', 'AppleGothic', 'dotum', sans-serif;
}
body {
  font-family: var(--font-sans);
  font-weight: 400;
  color: #333333;
}
```

> **라이선스 주의**: Pretendard는 OFL (무료). Noto Sans KR도 Google Fonts에서 무료 호스팅. 복제 시 `Inter` + 한국어 폴백만으로도 근접 재현 가능.

---

## 05. Typography Scale

> Kurly는 Pretendard/Noto 기반 커머스 표준 scale. 본문 14px · 가격 24px · hero title 36px.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `caption` | `12px` | 400 | 1.5 | 0 |
| `body-sm` | `13px` | 400 | 1.5 | 0 |
| `body` | `14px` | 400 | 1.5 | 0 |
| `body-lg` | `16px` | 400 | 1.5 | 0 |
| `title-sm` | `18px` | 500 | 1.4 | -0.01em |
| `title-md` | `20px` | 500 | 1.3 | -0.01em |
| `price` | `24px` | 700 | 1.2 | -0.01em |
| `h3` | `28px` | 700 | 1.25 | -0.02em |
| `h2` | `36px` | 700 | 1.15 | -0.02em |
| `hero` | `44px` | 700 | 1.1 | -0.02em |

> ⚠️ 본문은 `14px`가 기본이다. `16px`가 아니다. 한국 커머스 관습 — 정보 밀도가 높은 리스트 페이지에서 `16px`은 과하다.

---

## 06. Colors

### 06-1. Brand (Purple Pair)

| Token | Hex |
|---|---|
| `--brand-primary` | `#BD76FF` |
| `--brand-strong` | `#8D4CC4` |
| `--brand-deeper` | `#7542A1` |
| `--brand-soft-bg` | `#F6F4F9` |
| `--brand-tint` | `#E8DBF3` |
| `--brand-wine` | `#451B6C` |
| `--brand-plum` | `#2B2232` |

### 06-3. Neutral Ramp (12 steps)

| Step | Hex | Use |
|---|---|---|
| neutral-25 | `#F2F5F8` | 쿨그레이 surface (list bg) |
| neutral-50 | `#ECEFF3` | hover background |
| neutral-100 | `#DFE4EB` | divider soft |
| neutral-200 | `#DDE2E8` | card border 기본 |
| neutral-300 | `#C0C8D0` | input border |
| neutral-400 | `#BCC4CC` | disabled text |
| neutral-500 | `#A7B2BC` | placeholder |
| neutral-600 | `#848F9A` | body tertiary |
| neutral-700 | `#626C77` | body secondary |
| neutral-800 | `#505760` | title secondary |
| neutral-850 | `#464B52` | title muted |
| neutral-900 | `#363A40` | title strong |
| neutral-925 | `#303337` | title deepest |
| neutral-950 | `#222222` | text on white (max) |
| text-body | `#333333` | body default |

### 06-4. Accent Families (category / status)

| Family | Hex | Use |
|---|---|---|
| orange | `#EB5522` | 신선식품 카테고리 배지 |
| orange-light | `#FF602B` | 세일 포인트 |
| red | `#E92728` | 할인가/품절 |
| red-alert | `#AC2728` | 시스템 alert |
| green | `#028B61` | 성공/친환경 배지 |
| green-deep | `#019C6C` | 배송 완료 |
| teal | `#48B1C8` | 정보 배지 |
| teal-light | `#45BCD6` | link highlight |
| yellow | `#F1D902` | 쿠폰 배지 |
| yellow-vivid | `#FEE609` | event pop |
| olive | `#B48906` | notice |
| kakao-yellow | `#FEE500` | Kakao 로그인 |
| blue-info | `#076AD3` | notice/info |
| postgres-blue | `#216BA5` | datepicker 기본 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--bg` | `#FFFFFF` | 페이지 배경 |
| `--surface-soft` | `#F6F4F9` | 연보라 tinted surface |
| `--surface-cool` | `#F2F5F8` | 쿨그레이 surface |
| `--text-primary` | `#222222` | 최강조 본문 |
| `--text-body` | `#333333` | body 기본 |
| `--text-muted` | `#848F9A` | 부가 설명 |
| `--text-placeholder` | `#A7B2BC` | input placeholder |
| `--border-default` | `#DDE2E8` | card/input border |
| `--border-strong` | `#C0C8D0` | divider 강조 |
| `--brand-bg` | `#BD76FF` | CTA / 공지 bar |
| `--brand-text` | `#FFFFFF` | CTA 텍스트 |
| `--brand-hover` | `#8D4CC4` | CTA hover |
| `--skeleton-base` | `#EBEBEB` | skeleton loader |
| `--skeleton-highlight` | `#F5F5F5` | skeleton shimmer |

### 06-7. Dominant Colors (실제 CSS 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#BD76FF` | 7 | brand primary purple |
| 2 | `#AEAEAE` | 7 | datepicker neutral |
| 3 | `#F6F4F9` | 6 | brand-soft tinted surface |
| 4 | `#F2F5F8` | 5 | neutral-25 cool surface |
| 5 | `#F0F0F0` | 4 | datepicker today-bg |
| 6 | `#ECEFF3` | 4 | neutral-50 hover |
| 7 | `#DFE4EB` | 4 | neutral-100 divider |
| 8 | `#BCC4CC` | 4 | neutral-400 disabled |
| 9 | `#A7B2BC` | 4 | neutral-500 placeholder |
| 10 | `#8D4CC4` | 4 | brand-strong hover |
| 11 | `#848F9A` | 4 | neutral-600 tertiary |
| 12 | `#303337` | 4 | neutral-925 title |

---

## 07. Spacing

Kurly는 4px baseline grid + 라운드 배수 시스템을 쓴다. `--kpds_ldmw17t ~ ldmw1717` 해시 토큰으로 raw px를 토큰화.

| Token | Value | Use case |
|---|---|---|
| `space-2xs` | `2px` | chip inner hairline |
| `space-xs` | `4px` | 세밀한 gap |
| `space-sm` | `8px` | small gutter |
| `space-md` | `12px` | form padding |
| `space-lg` | `16px` | card inner |
| `space-xl` | `24px` | section vertical |
| `space-2xl` | `32px` | section generous |
| `space-3xl` | `40px` | hero top |
| `space-4xl` | `48px` | block separator |
| `space-5xl` | `64px` | large section |
| `space-6xl` | `80px` | hero bottom |
| `space-7xl` | `96px` | mega section |
| `space-8xl` | `160px` | footer spacing |
| `page-max` | `1050-1200px` | 데스크톱 content 폭 |
| `container` | `320-400px` | 모바일 max (스위퍼 slide) |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `radius-xs` | `4px` | chip / 배지 |
| `radius-sm` | `6px` | 버튼 small |
| `radius-md` | `7px` | input |
| `radius-md-lg` | `8px` | 카드 small |
| `radius-lg` | `10px` | 카드 기본 |
| `radius-xl` | `12px` | 카드 large |
| `radius-2xl` | `13px` | banner slider |
| `radius-3xl` | `14px` | promo card |
| `radius-4xl` | `16px` | hero card |
| `radius-5xl` | `18px` | modal |
| `radius-pill` | `9999px` | pill button |
| `radius-circle` | `50%` | avatar |

---

## 09. Shadows

> 커머스 특성상 shadow 의존도 낮음 — 배경 layering으로 계층 표현. 얕은 2-layer shadow만 제한적 사용.

| Level | Value | Usage |
|---|---|---|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.04)` | 버튼 기본 |
| `shadow` | `0 2px 10px rgba(0,0,0,0.06)` | 카드 hover |
| `shadow-md` | `0 4px 16px rgba(0,0,0,0.08)` | 드롭다운 |
| `shadow-lg` | `0 8px 24px rgba(0,0,0,0.1)` | 모달 |
| `shadow-panel` | `0 2px 4px rgba(0,0,0,0.05), 0 8px 20px rgba(0,0,0,0.04)` | 플로팅 카트 |

---

## 10. Motion

> 쇼핑 기본 — 300ms ease-out. 배너 슬라이더는 Swiper 기본값.

| Token | Value | Usage |
|---|---|---|
| `duration-fast` | `150ms ease-out` | link hover |
| `duration-base` | `300ms ease-out` | card/slider |
| `duration-slow` | `500ms cubic-bezier(0.4,0,0.2,1)` | modal fade |
| `--animation-duration` | `1.5s` | skeleton shimmer |
| `swiper-auto` | `5000ms` | main banner autoplay |

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1050-1200px` 중앙 정렬
- **Grid type**: 4-column product grid + Flex fallback
- **Column count**: 4 (데스크톱 product list) · 2 (태블릿) · 1 (모바일)
- **Gutter**: `16-24px`

### Hero

- **🆕 Pattern Summary**: `상단 공지 bar + GNB + 3-slide main banner + ~420vh total scroll (커머스 관행)`
- Layout: Swiper 메인 배너 (autoplay 5s, fade transition)
- Background: 배너 이미지 full-bleed
- H1: `~36px / weight 700 / tracking -0.02em`
- Max-width: `1200px`

### Section Rhythm

```css
.section {
  padding: 48px 0;       /* vertical */
  max-width: 1200px;
  margin: 0 auto;
  padding-inline: 16px;  /* mobile gutter */
}
```

### Card Patterns

- **Card background**: `#FFFFFF`
- **Card border**: `1px solid #DDE2E8` 또는 border 없음 + subtle shadow
- **Card radius**: `8-12px` (상품 카드 기본 `8px`)
- **Card padding**: `16px`
- **Card shadow**: 기본 none, hover `0 2px 10px rgba(0,0,0,0.06)`

### Navigation Structure

- **Type**: horizontal GNB + 공지 bar (상단)
- **Position**: `position: sticky; top: 0`
- **Height**: 공지 `36px` + GNB `84px` = total `120px`
- **Background**: 공지 `#BD76FF` or `#222222` / GNB `#FFFFFF`
- **Border**: GNB 하단 `1px solid #DDE2E8`

### Content Width

- **Prose max-width**: `~720px`
- **Container max-width**: `1200px`
- **Product grid**: `1050px` (4-col × 250px) 또는 `1200px`
- **Sidebar width**: 없음 (상품 리스트는 full-width grid)

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 640px` | 1-column, 별도 모바일 라우트 |
| Tablet | `≥ 768px` | 2-column product grid |
| Desktop | `≥ 1024px` | 4-column grid 복원 |
| Large | `≥ 1200px` | full page max-width |
| XL | `≥ 1440px` | 추가 여백 |

*데스크톱 퍼스트* — Kurly 홈은 데스크톱 최적화, 모바일은 별도 라우트

### Touch Targets

- **Minimum tap size**: `44px` (iOS HIG 준수)
- **Button height**: `48px` primary · `40px` secondary
- **Input height**: `44px`

### Collapsing Strategy

- **Navigation**: 1024px 이하에서 햄버거 drawer
- **Grid columns**: 4 → 2 → 1
- **Sidebar**: N/A
- **Hero banner**: slide height 축소 (`400px → 280px`)

### Image Behavior

- **Strategy**: Next.js `<Image>` + Kurly CDN (`shop-phinf.pstatic.net` 관련)
- **Max-width**: `100%`
- **Aspect ratio**: 상품 이미지 `1/1`, 배너 `16/9` 또는 `3/1`

---

## 13. Components

### Buttons

Kurly의 버튼은 퍼플 primary + 화이트 ghost + 그레이 secondary 3-variant.

```html
<button class="btn btn-primary">장바구니 담기</button>
<button class="btn btn-secondary">바로구매</button>
<button class="btn btn-ghost">더보기</button>
```

| Variant | background | color | border-radius | padding | hover |
|---|---|---|---|---|---|
| primary | `#BD76FF` | `#FFFFFF` | `6px` | `12px 24px; height 48px` | `background #8D4CC4` |
| secondary | `#FFFFFF` | `#222222` | `6px` | 동일 | `background #F2F5F8` |
| ghost | `transparent` | `#848F9A` | `6px` | 동일 | `color #222222` |
| pill (카테고리) | `#F6F4F9` | `#8D4CC4` | `9999px` | `6px 14px` | `background #E8DBF3` |

### Price Badge

```html
<span class="price">
  <del>₩25,000</del>
  <strong>₩19,900</strong>
  <em>20%</em>
</span>
```

- `del` color: `#A7B2BC`, `font-size: 13px`
- `strong` color: `#222222`, `font-size: 20px`, `font-weight: 700`
- `em` (할인율): color `#BD76FF` (or `#EB5522` for big discount), `font-weight: 700`

### Cards & Containers

```html
<article class="product-card">
  <img ... />
  <div class="product-card__body">…</div>
</article>
```

- bg: `#FFFFFF`
- border: `1px solid #DDE2E8` 또는 border 없음
- radius: `8px`
- padding: `16px` 텍스트 영역만
- shadow: 기본 none, hover `0 2px 10px rgba(0,0,0,0.06)`

### Navigation

- 공지 bar: `height 36px`, bg `#BD76FF`, color `#FFFFFF`, font `13px weight 400`
- GNB: `height 84px`, bg `#FFFFFF`, 로고 좌측 · 카테고리 중앙 · 검색/마이페이지 우측
- 링크: Pretendard `14px weight 400`, color `#222222`, hover color `#8D4CC4`
- Active: underline `2px` color `#BD76FF`

### Inputs & Forms

- height: `44px`
- padding: `0 12px`
- border: `1px solid #DDE2E8`
- radius: `6px`
- focus: `border-color #BD76FF; box-shadow: 0 0 0 3px rgba(189,118,255,0.15)`
- placeholder: `color #A7B2BC`

### Hero Banner (Swiper)

- Swiper.js autoplay `5000ms`
- transition `fade` 300ms
- pagination dot color: default `rgba(0,0,0,0.2)`, active `#BD76FF`

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 혜택 중심 명사구 | "새벽배송 무료 이벤트" |
| Primary CTA | 행동 동사 | "장바구니 담기" / "바로구매" |
| Secondary CTA | 정보성 | "상품 상세보기" |
| Promo copy | 숫자 강조 + 이모지 가끔 | "최대 50% 할인 🎉" |
| Tone | 정중한 친근함 — "~하세요" 경어체 | — |

---

## 15. Drop-in CSS

```css
/* Kurly — copy into your root stylesheet */
:root {
  /* Fonts */
  --k-font-sans:
    Pretendard, "Pretendard Variable",
    -apple-system, BlinkMacSystemFont, system-ui,
    "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;

  /* Brand */
  --k-color-brand:       #BD76FF;
  --k-color-brand-hover: #8D4CC4;
  --k-color-brand-soft:  #F6F4F9;
  --k-color-brand-tint:  #E8DBF3;

  /* Surfaces */
  --k-bg:          #FFFFFF;
  --k-surface:     #F6F4F9;
  --k-surface-cool:#F2F5F8;
  --k-border:      #DDE2E8;
  --k-border-strong:#C0C8D0;
  --k-text:        #222222;
  --k-text-body:   #333333;
  --k-text-muted:  #848F9A;
  --k-placeholder: #A7B2BC;

  /* Status */
  --k-orange: #EB5522;
  --k-red:    #AC2728;
  --k-green:  #028B61;
  --k-teal:   #48B1C8;
  --k-yellow: #F1D902;

  /* Key spacing */
  --k-space-sm:  8px;
  --k-space-md:  16px;
  --k-space-lg:  24px;
  --k-space-xl:  48px;

  /* Radius */
  --k-radius-sm: 6px;
  --k-radius-md: 8px;
  --k-radius-lg: 12px;
  --k-radius-pill: 9999px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Kurly
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#BD76FF',
          hover:   '#8D4CC4',
          soft:    '#F6F4F9',
          tint:    '#E8DBF3',
          wine:    '#451B6C',
        },
        neutral: {
          25:  '#F2F5F8',
          50:  '#ECEFF3',
          100: '#DFE4EB',
          200: '#DDE2E8',
          300: '#C0C8D0',
          400: '#A7B2BC',
          500: '#848F9A',
          600: '#626C77',
          700: '#505760',
          800: '#363A40',
          900: '#222222',
        },
        accent: {
          orange: '#EB5522',
          red:    '#AC2728',
          green:  '#028B61',
          teal:   '#48B1C8',
          yellow: '#F1D902',
        },
      },
      fontFamily: {
        sans: ['Pretendard', 'Pretendard Variable', 'Noto Sans KR', 'system-ui'],
      },
      borderRadius: {
        sm: '4px', DEFAULT: '6px', md: '8px',
        lg: '10px', xl: '12px', '2xl': '16px',
        pill: '9999px',
      },
      maxWidth: {
        container: '1200px',
        product: '1050px',
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
| Brand primary | `--k-color-brand` | `#BD76FF` |
| Brand hover | `--k-color-brand-hover` | `#8D4CC4` |
| Background | `--k-bg` | `#FFFFFF` |
| Surface | `--k-surface` | `#F6F4F9` |
| Text primary | `--k-text` | `#222222` |
| Text body | `--k-text-body` | `#333333` |
| Text muted | `--k-text-muted` | `#848F9A` |
| Border | `--k-border` | `#DDE2E8` |

### Example Component Prompts

#### Hero Banner

```
Kurly 스타일 히어로 배너를 만들어줘.
- Swiper 기반 fade transition, autoplay 5000ms
- 배경: 배너 이미지 full-bleed
- H1: Pretendard 36px weight 700, color #222222, tracking -0.02em
- Sub: 14px color #505760
- Primary CTA: bg #BD76FF, color #FFFFFF, radius 6px, height 48px, padding 12px 24px
- Pagination dot: default rgba(0,0,0,0.2), active #BD76FF
- 최대 너비: 1200px
```

#### Product Card

```
Kurly 스타일 상품 카드를 만들어줘.
- bg #FFFFFF, border none (또는 1px solid #DDE2E8)
- radius 8px, padding 16px (텍스트 영역)
- 이미지 1:1 aspect-ratio, object-fit cover
- 상품명: 14px weight 500 color #222222 line-height 1.4 (2줄 truncate)
- 원가: del color #A7B2BC 13px
- 할인가: 20px weight 700 color #222222
- 할인율: color #BD76FF weight 700
- hover: shadow 0 2px 10px rgba(0,0,0,0.06), transition 200ms
```

#### Top Notice Bar

```
Kurly 상단 공지 bar를 만들어줘.
- height 36px, position sticky top 0
- bg #BD76FF, color #FFFFFF
- font Pretendard 13px weight 400
- 중앙 정렬, 가로 padding 16px
- 닫기 버튼 우측 (color #FFFFFF, opacity 0.8)
```

#### Category Pill

```
Kurly 카테고리 pill 버튼.
- bg #F6F4F9, color #8D4CC4, border none
- radius 9999px, padding 6px 14px
- font Pretendard 13px weight 500
- hover: bg #E8DBF3
```

### Iteration Guide

- **색상 변경 시**: `--k-color-*` semantic token만 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight `400`이 기본. Pretendard가 맞지 않으면 `Inter + Noto Sans KR` 폴백.
- **여백 조정 시**: 4px baseline grid를 유지. 임의 값 금지.
- **새 컴포넌트 추가 시**: radius는 `4/6/8/10/12/16` 중 하나.
- **모바일**: 별도 라우트 권장. 반응형 단일 페이지면 햄버거 nav + 1-col grid.
- **브랜드 퍼플**: CTA, 공지 bar, 가격 할인 이외엔 절대 금지.
- **transition**: `300ms ease-out`이 기본. 500ms 이상 금지.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 `#FFFFFF`로. 서피스는 `#F6F4F9` 또는 `#F2F5F8`로 layer.
- CTA는 `#BD76FF` 배경 + `#FFFFFF` 텍스트 + `border-radius: 6px` + `height 48px`.
- 본문은 Pretendard `14px` `weight 400` `color #333333`.
- 가격 강조는 `20-24px weight 700 color #222222` + 할인율 `#BD76FF`.
- Card radius는 `8px` 기본, `12px` large.
- Navigation에 공지 bar (36px) + GNB (84px) 2-layer 구조.
- transition은 `300ms ease-out` 기본.

### ❌ DON'T

- 배경을 `#BD76FF`(brand)로 채우지 말 것 — 퍼플은 CTA·공지·가격에만.
- 본문 텍스트를 `#000000`로 두지 말 것 — 대신 `#333333` (body) 또는 `#222222` (title).
- Weight `600`을 body에 쓰지 말 것 — Kurly 본문은 `400`. 강조는 `500` 또는 `700`.
- 폰트를 `'맑은 고딕'` (Malgun Gothic)만 쓰지 말 것 — Pretendard 우선, Noto 폴백, 맑은 고딕은 최후 폴백.
- Card radius `16px` 이상 금지 — Kurly는 커머스라 `8-12px`가 표준.
- transition duration `500ms` 이상 금지 — 쇼핑 동선을 느리게 만든다.
- 브랜드 퍼플을 카드 배경에 쓰지 말 것 — Twitch 느낌. 대신 `#F6F4F9` soft tint.
- Dark mode 가정 금지 — Kurly는 light-only. dark variant 토큰 없음.
