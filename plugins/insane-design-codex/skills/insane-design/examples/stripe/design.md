---
schema_version: 3.1
slug: stripe
service_name: Stripe
site_url: https://stripe.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#635BFF"
primary_font: sohne-var
font_weight_normal: 400
token_prefix: --hds-*

bold_direction: "Refined Fintech"
aesthetic_category: "Refined Fintech"
signature_element: gradient_glow
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Stripe (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Stripe의 마케팅 사이트는 **"금융 인프라를 디자인 언어로 번역한 사이트"**다. 대부분의 결제 SaaS가 파란색과 안전감으로 도배할 때, Stripe는 오히려 **인디고 보라(`#635BFF`)와 그라디언트 글로우**로 "기술이 발전하는 방향"을 시각화한다. hero 섹션 배경은 순백 `#FFFFFF`이지만, 텍스트 제목 뒤로 `#BDB4FF → #643AFD → #533AFD` 가로 그라디언트가 조용히 흐르고, 하단으로 내려갈수록 `#0d1738` 짙은 네이비로 섹션이 전환된다.

색상 전략은 **"brand indigo 한 축 + neutral blue-gray 두 축"**이다. 브랜드는 `#635BFF` (anchor)와 `#533AFD` (brand-600, gradient stop) 한 쌍으로 압축되고, neutral은 light 쪽 `#F8FAFD / #E5EDF5 / #D4DEE9` + dark 쪽 `#1A2C44 / #11273E / #0D253D / #061B31`의 두 계단을 평행 운용한다. 그래서 light 섹션과 dark 섹션이 같은 페이지 안에서 교차해도 어색하지 않다. 이 사이트의 진짜 시그니처는 shadow — `--hds-color-shadow-xs/sm/md/lg/xl` 각 레벨이 **top + bottom 2-layer 원자**로 정의되어 있어서, 모든 카드가 "위에서 내려오는 빛"과 "아래로 떨어지는 그림자"를 동시에 받는다.

타이포그래피는 자체 호스팅한 **`sohne-var`**이 축이다. 이 폰트의 variable axis는 `400 / 425 / 450 / 500 / 550 / 600 / 700`의 미세 weight를 제공하며, 본문은 `16px weight 400`, 헤딩은 `500~600` variable axis 값을 정확히 사용한다. 코드 폰트는 `SourceCodePro`. hds(Home Design System) 네임스페이스 아래 `--hds-font-heading-{xs,sm,md,lg,xl,xxl,hero-sm,hero-lg}` 8단 반응형 scale이 선언되어 있고, breakpoint별로 heading 크기가 독립적으로 성장한다.

레이아웃은 1080-1609px max-width + 반응형 grid. breakpoint가 촘촘하다 — `400/480/600/640/768/840/940/1115/1264/1300px`로 거의 모든 구간에 대응한다. `--hds-space-core-{100,200,300,...}` 토큰 + `--hds-button-padding-block-*`이 반응형 3단 성장으로 설계되어 있어 버튼 하나도 화면이 커지면 크기가 커진다.

인터랙션은 Stripe 특유의 **캐러셀 / case-study carousel / bento grid 애니메이션**이 중심이다. `--carousel-card-scale`, `--carousel-item-progress`, `--bento-right-blob`, `--agentic-box-shadow` 같은 토큰이 존재하며, 이들은 scroll-linked animation의 일부다. transition 자체는 짧지만 연출은 정교하다.

### Key Characteristics

- Brand Indigo 한 축 `#635BFF` + accent gradient `#BDB4FF → #643AFD → #533AFD`
- Light + Dark neutral 이중 ramp (`#F8FAFD` vs `#0D253D`)
- 2-layer dual shadow 원자 (top + bottom, xs~xl 5단계)
- `sohne-var` variable font + SourceCodePro mono
- `--hds-*` Home Design System prefix (수천 토큰)
- 10단 breakpoint (400/480/600/640/768/840/940/1115/1264/1300)
- 반응형 크기 성장 (button padding, heading size가 bp별 자체 scale)
- Scroll-linked carousel / bento grid 시그니처 연출

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Refined Fintech
> **Aesthetic Category**: Refined Fintech
> **Signature Element**: 이 사이트는 **인디고 보라와 그라디언트 글로우 + 2-layer dual shadow**로 기억된다.
> **Code Complexity**: high — HDS variable 수천 개 + sohne-var + reactive padding + scroll animation. 화려하지 않지만 정교.

---

## 01. Quick Start

> 5분 안에 Stripe처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "sohne-var", "SF Pro Display",
    -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 (light default) */
:root {
  --bg: #FFFFFF;
  --fg: #0D1738;
  --surface: #F8FAFD;
  --surface-alt: #F6F9FC;
  --border: #D4DEE9;
  --text-muted: #64748D;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 인디고 + 그라디언트 */
:root {
  --brand:        #635BFF;
  --brand-strong: #533AFD;
  --accent-gradient:
    linear-gradient(90deg,
      #BDB4FF 0%, #643AFD 50%, #533AFD 100%);
}
```

**절대 하지 말아야 할 것 하나**: 브랜드 `#635BFF`를 flat 배경으로 쓰지 마라. Stripe의 인디고는 CTA, focus ring, gradient stop에만 등장한다. Flat indigo 배경은 Discord 또는 Linear인데, Stripe가 아니다. Stripe에서 indigo를 면적으로 쓰는 유일한 방법은 **gradient**다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://stripe.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 573,555 bytes (Next.js SSR) |
| CSS files | 7개 외부, 총 약 428KB minified |
| Token prefix | `--hds-*` (Home Design System), `--accent-*`, `--carousel-*`, `--bento-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (mkt-ssr-statics 번들)
- **Design system**: HDS (Home Design System) — prefix `--hds-color-*`, `--hds-font-*`, `--hds-space-*`, `--hds-button-*`
- **CSS architecture**: core → util → component 3-tier semantic system
  ```
  core   (--hds-color-core-brand-600 : #533afd)      raw hex 원자
  util   (--hds-color-util-accent-lemon-500)         컨텍스트 alias
  comp   (--hds-color-action-bg-disabled)            상호작용 컴포넌트
  ```
- **Class naming**: hashed CSS modules + utility classes
- **Default theme**: light (`<html lang="en-US">`, 배경 `#FFFFFF` / hero 하단 `#0D1738`로 전환)
- **Font loading**: 셀프 호스트 `sohne-var.woff2`, `SourceCodePro.woff2`
- **Canonical anchor**: `#635BFF` — `--hds-canary-color-border-focus`, `--hds-color-core-brand-500` 계열
- **Animation primitives**: `--carousel-*`, `--bento-*`, `--agentic-*`, `--stats-*` (scroll-linked)

---

## 04. Font Stack

- **Display/Body**: `sohne-var` (Klim Type Foundry, 유료)
- **Code**: `SourceCodePro` (Adobe, OFL)
- **Fallback**: `"SF Pro Display", -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Ubuntu, sans-serif`
- **Weight normal / bold**: `400` / `600`
- **Variable weights used**: `400 / 425 / 450 / 500 / 550 / 600 / 700`

```css
:root {
  --hds-font-family:
    "sohne-var", "SF Pro Display", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Ubuntu, sans-serif;
  --hds-font-family-code: SourceCodePro, ui-monospace,
    "SF Mono", Menlo, monospace;
}
body {
  font-family: var(--hds-font-family);
  font-weight: 400;
}
```

> **라이선스 주의**: sohne-var는 Klim Type Foundry 유료 라이선스. 복제 시 `Inter Variable` 또는 `Söhne Buch / Kraftig` 근사 대체. SourceCodePro는 OFL 무료 이므로 그대로 사용 가능.

---

## 05. Typography Scale

> HDS는 heading을 **반응형 3단 scale**로 설계: mobile/tablet/desktop 각각 다른 크기 자동 성장.

| Token | Mobile | Tablet | Desktop | Weight | ls |
|---|---|---|---|---|---|
| `--hds-font-heading-xs-size` | 1rem (16px) | — | — | 500 | -0.01em |
| `--hds-font-heading-sm-size` | 1.125rem (18px) | 1.25rem (20px) | 1.375rem (22px) | 500 | -0.01em |
| `--hds-font-heading-md-size` | 1.25rem (20px) | 1.375rem (22px) | 1.625rem (26px) | 550 | -0.02em |
| `--hds-font-heading-lg-size` | 1.375rem (22px) | 1.75rem (28px) | 2rem (32px) | 550 | -0.02em |
| `--hds-font-heading-xl-size` | 1.75rem (28px) | 2.125rem (34px) | 3rem (48px) | 600 | -0.02em |
| `--hds-font-heading-xxl-size` | 2.125rem (34px) | — | 3.5rem (56px) | 600 | -0.03em |
| `--hds-font-heading-hero-sm-size` | 1.625rem (26px) | 2rem (32px) | 2.25rem (36px) | 600 | -0.02em |
| `--hds-font-heading-hero-lg-size` | 1.75rem (28px) | — | 3rem (48px) | 600 | -0.03em |
| `body` | 1rem (16px) | 1rem | 1rem | 400 | 0 |

> ⚠️ Stripe의 heading은 반응형으로 **크기가 독립 성장**한다. 단일 `clamp()`가 아니라 breakpoint별 `--hds-font-heading-*-size`가 재선언된다.

---

## 06. Colors

### 06-1. Brand (Indigo, core ramp 14 steps)

| Token | Hex |
|---|---|
| `--hds-color-core-brand-25` | `#F5F5FF` |
| `--hds-color-core-brand-50` | `#E8E9FF` |
| `--hds-color-core-brand-75` | `#E2E4FF` |
| `--hds-color-core-brand-100` | `#D6D9FC` |
| `--hds-color-core-brand-200` | `#B9B9F9` |
| `--hds-color-core-brand-300` | `#9A9AFE` |
| `--hds-color-core-brand-400` | `#7F7DFC` |
| `--hds-color-core-brand-500 ★` | `#665EFD` |
| `--hds-color-core-brand-600` | `#533AFD` |
| `--hds-color-core-brand-700` | `#4032C8` |
| `--hds-color-core-brand-800` | `#2E2B8C` |
| `--hds-color-core-brand-900` | `#1C1E54` |
| `--hds-color-core-brand-950` | `#161741` |
| `--hds-color-core-brand-975` | `#0F1137` |

> **Canonical anchor**: `#635BFF` (= `--hds-canary-color-border-focus`, visual brand 500). Core ramp의 500 (`#665EFD`)과 인접 tint.

### 06-2. Accent Gradient (hero)

```css
--accent-gradient-color-stop-1: #BDB4FF;
--accent-gradient-color-stop-2: #643AFD;
--accent-gradient-color-stop-3: #533AFD;
--gradient-color: #533AFD;
```

### 06-3. Neutral Ramp (cool blue-gray, 13 steps)

| Token | Hex | Usage |
|---|---|---|
| `--hds-color-core-neutral-0` | `#FFFFFF` | page bg |
| `--hds-color-core-neutral-25` | `#F8FAFD` | subtle surface |
| `--hds-color-core-neutral-50` | `#E5EDF5` | divider tint |
| `--hds-color-core-neutral-100` | `#D4DEE9` | card border |
| `--hds-color-core-neutral-200` | `#BAC8DA` | input border |
| `--hds-color-core-neutral-300` | `#95A4BA` | placeholder |
| `--hds-color-core-neutral-400` | `#7D8BA4` | text tertiary |
| `--hds-color-core-neutral-500` | `#64748D` | text muted |
| `--hds-color-core-neutral-600` | `#50617A` | text secondary |
| `--hds-color-core-neutral-700` | `#3C4F69` | text body strong |
| `--hds-color-core-neutral-800` | `#273951` | text heading |
| `--hds-color-core-neutral-900` | `#1A2C44` | text deepest |
| `--hds-color-core-neutral-950` | `#11273E` | dark bg panel |
| `--hds-color-core-neutral-975` | `#0D253D` | dark bg strong |
| `--hds-color-core-neutral-990` | `#061B31` | near-black |

### 06-4. Accent Families (product lines + status)

| Family | Hex | Use |
|---|---|---|
| `success-400` | `#00B261` | success state |
| `success-600` | `#006F3A` | success deep |
| `error-400` | `#F3432A` | error |
| `error-500` | `#D8351E` | error strong |
| `error-600` | `#A01400` | error deep |
| `lemon-200` | `#F9B900` | warning / highlight |
| `lemon-300` | `#E8A30B` | warning deep |
| `magenta-350` | `#F44BCC` | bento blob |
| `magenta-600` | `#A51D85` | magenta deep |
| `ruby-600` | `#B51145` | ruby alert |
| `suite-ea2261` | `#EA2261` | suite marker red |
| `suite-ff6118` | `#FF6118` | suite marker orange |
| `suite-fc5` | `#FFCC55` | suite marker yellow |
| `suite-f363f3` | `#F363F3` | suite marker magenta |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--hds-color-input-bg-default` (light) | `#0D17380D` (5% black alpha) | form input 배경 |
| `--hds-color-input-bg-default` (dark) | `#FFFFFF40` (25% white alpha) | dark form input |
| `--hds-color-input-border-default` (light) | `#D4DEE9BF` | form border |
| `--hds-canary-color-border-focus` | `#635BFF` | focus ring |
| `--hds-color-action-bg-disabled` | `#23356EA6` | disabled CTA |
| `--stats-color` (a) | `#0810BF` | stat number blue |
| `--stats-color` (b) | `#4304EA` | stat number indigo |
| `--stats-color` (c) | `#8A35DF` | stat number purple |
| `--stats-color` (d) | `#C42FA5` | stat number magenta |

### 06-6. Shadow Tokens (dual-layer atom)

Stripe shadow는 **top + bottom 두 원자**로 분리. alpha도 light/dark 두 값 병존.

| Token | Light (light theme) | Dark (dark theme) |
|---|---|---|
| `--hds-color-shadow-xs-top` | `#0037700F` | `#0D173826` |
| `--hds-color-shadow-xs-bottom` | `#003B890A` | `#0D173833` |
| `--hds-color-shadow-sm-top` | `#00377014` | `#0D173826` |
| `--hds-color-shadow-sm-bottom` | `#003B890D` | `#0D173833` |
| `--hds-color-shadow-md-top` | `#0037701A` | `#0D173826` |
| `--hds-color-shadow-md-bottom` | `#003B8905` | `#0D173833` |
| `--hds-color-shadow-lg-top` | `#0037701A` | `#0D173826` |
| `--hds-color-shadow-lg-bottom` | `#003B890A` | `#0D173833` |
| `--hds-color-shadow-xl-top` | `#00377024` | `#0D173826` |
| `--hds-color-shadow-xl-bottom` | `#003B890F` | `#0D173833` |

### 06-7. Dominant Colors (실제 CSS 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#0D1738` | 15 | text-heading (deepest ink) |
| 2 | `#F8FAFD` | 11 | neutral-25 surface |
| 3 | `#FFFFFF` | 10 | page bg |
| 4 | `#533AFD` | 10 | brand-600 / gradient |
| 5 | `#FF6118` | 8 | suite orange marker |
| 6 | `#061B31` | 7 | neutral-990 near-black |
| 7 | `#FCFDFE` | 6 | stats-bg option |
| 8 | `#FB76FA` | 6 | stop-color gradient |
| 9 | `#F6F9FC` | 6 | surface alt |
| 10 | `#D4DEE9` | 6 | neutral-100 border |
| 11 | `#7232F1` | 6 | accent magenta-purple |
| 12 | `#1318C1` | 6 | stat deep blue |

---

## 07. Spacing

Stripe는 `--hds-space-core-*` 토큰 시스템 + button padding 반응형 3단을 쓴다.

| Token | Value | Use case |
|---|---|---|
| `--hds-space-core-100` | `4px` | 세밀 gap |
| `--hds-space-core-200` | `8px` | small gutter |
| `--hds-space-core-300` | `12px` | form padding |
| `--hds-space-core-400` | `16px` | card inner |
| `--hds-space-core-500` | `24px` | section vertical |
| `--hds-space-core-600` | `32px` | section generous |
| `--hds-space-core-700` | `48px` | hero block |
| `--hds-space-core-800` | `64px` | mega section |
| `--hds-button-padding-block-start` (sm/md/lg) | `11.5 / 13.5 / 15.5px` | 버튼 상단 padding 3단 |
| `--hds-button-padding-block-end` (sm/md/lg) | `12.5 / 14.5 / 16.5px` | 버튼 하단 padding 3단 |
| `--hds-button-border-width` | `1px` | 모든 버튼 공통 |
| `page-max-width` (관찰) | `1080~1609px` | 섹션별 다름 |
| `carousel-gutter` | `16px` | caro 내부 간격 |
| `divider-height` | `120px` | 섹션 분리자 |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `radius-xs` | `4px` | chip / tag |
| `radius-sm` | `5px` (`--card-radius-inner`) | nested card inner |
| `radius-md` | `8px` | button / input |
| `radius-lg` | `12px` | card 기본 |
| `radius-xl` | `16px` | hero card |
| `radius-2xl` | `20px` | bento block |
| `radius-pill` | `9999px` | pill button |

> 관찰: Stripe는 **nested radius**를 엄격히 — 카드가 16px이면 내부 요소는 `--card-radius-inner: 5px`처럼 명시적으로 작은 값을 가진다.

---

## 09. Shadows

> Stripe의 shadow는 **2-layer dual-shadow 원자**. `shadow-xs` 하나만 해도 top + bottom 2개 색으로 조합됨. light/dark variant 각각 정의.

| Level | Value (light) | Usage |
|---|---|---|
| `shadow-xs` | `0 1px 2px var(--hds-color-shadow-xs-top), 0 2px 4px var(--hds-color-shadow-xs-bottom)` | 얕은 버튼 rest |
| `shadow-sm` | `0 2px 4px var(--shadow-sm-top), 0 4px 8px var(--shadow-sm-bottom)` | 카드 rest |
| `shadow-md` | `0 4px 8px var(--shadow-md-top), 0 8px 16px var(--shadow-md-bottom)` | 드롭다운 |
| `shadow-lg` | `0 8px 16px var(--shadow-lg-top), 0 16px 32px var(--shadow-lg-bottom)` | 모달 |
| `shadow-xl` | `0 16px 32px var(--shadow-xl-top), 0 32px 64px var(--shadow-xl-bottom)` | popup / hero card |
| `agentic-box-shadow` | `0 20.187px 40.374px -20.187px` | AI 에이전틱 카드 signature |
| `hds-canary-ui-shadow` | `0 16px 32px ...` | canary floating UI |

---

## 10. Motion

> Stripe motion은 CSS 토큰으로 덜 노출되어 있고 대부분 JS scroll-linked. 기본 transition은 짧다.

| Pattern | Value | Use |
|---|---|---|
| `transition` (기본) | `200ms cubic-bezier(0.4,0,0.2,1)` | hover / focus |
| `transition-colors` | `150ms ease-out` | 색 전환 |
| `--carousel-item-progress` | `clamp(-1, value, 1)` | scroll-linked progress |
| `--carousel-card-scale` | `calc(1 - max(progress, -1 * progress))` | 카드 scale 연동 |
| bento blob shift | `200-400ms ease-out` | hover 반응 |

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: 1080~1609px (섹션별) — 단일 고정폭 없음
- **Grid type**: CSS Grid + Flex 혼합
- **Column count**: 12 subdivision base + bento custom
- **Gutter**: 16px (`--carousel-gutter`) / 24px (섹션)

### Hero

- **🆕 Pattern Summary**: `~90vh + 순백 bg + 그라디언트 글로우 뒤배 + 좌측 H1 + 우측 product bento/animation`
- Layout: 2-column split (텍스트 + 시각 애셋)
- Background: `#FFFFFF` solid + 뒷면 accent gradient `#BDB4FF → #533AFD`
- H1: `48-56px (desktop) / weight 600 / ls -0.03em`
- Max-width: `1232-1295px`

### Section Rhythm

```css
section {
  padding: 96px 32px;     /* vertical / horizontal */
  max-width: 1295px;
  margin: 0 auto;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` (light) / `#0D253D` (dark 섹션)
- **Card border**: `1px solid #D4DEE9` (light) / none (dark, shadow로 구분)
- **Card radius**: `12-16px` (hero), `8px` (일반)
- **Card padding**: `24-32px`
- **Card shadow**: `shadow-sm` rest → `shadow-md` hover (2-layer dual)

### Navigation Structure

- **Type**: horizontal desktop + mega-dropdown
- **Position**: `position: sticky; top: 0`
- **Height**: `~72px`
- **Background**: `rgba(255,255,255,0.85)` + `backdrop-filter: blur(12px)`
- **Border**: 하단 `1px solid rgba(0,0,0,0.08)` 스크롤 시 나타남

### Content Width

- **Prose max-width**: `~720px`
- **Container max-width**: `1295px` 기본 / `1609px` wide
- **Sidebar width**: docs에서만

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| XS | `≥ 400px` | 모바일 small 보정 |
| SM | `≥ 480px` | 모바일 large |
| MD | `≥ 600px` | 태블릿 portrait |
| LG | `≥ 640px` | 태블릿 land |
| LG+ | `≥ 768px` | small laptop |
| XL | `≥ 840px` | hero 2-col 복원 |
| XXL | `≥ 940px` | full nav |
| Desktop | `≥ 1115px` | container 확장 |
| Wide | `≥ 1264px` | carousel 확장 |
| XWide | `≥ 1300px` | max layout |

*모바일 퍼스트* — 10단계 breakpoint는 Stripe 특유의 정교한 반응형

### Touch Targets

- **Minimum tap size**: `44px` (iOS HIG)
- **Button height**: sm `32px` / md `40px` / lg `48px` (반응형 padding 자동)
- **Input height**: `40-48px`

### Collapsing Strategy

- **Navigation**: 940px 이하에서 햄버거, mega-dropdown 접힘
- **Grid columns**: 3-col → 2-col → 1-col
- **Hero layout**: 2-column → 1-column (840px 이하)
- **Carousel**: card-width `clamp(240px, 30.38cqi, 384px)` container query 사용

### Image Behavior

- **Strategy**: Next.js `<Image>` + CDN (`b.stripecdn.com`)
- **Max-width**: `100%`
- **Aspect ratio**: hero `16/9`, product mockup `3/2`

---

## 13. Components

### Buttons

Stripe 버튼은 `.hds-button-*` 클래스 + `--hds-button-padding-block-*` 반응형 padding.

```html
<button class="hds-button hds-button--primary">Start now</button>
<button class="hds-button hds-button--secondary">Contact sales</button>
```

| Variant | background | color | radius | padding (sm/md/lg) | hover |
|---|---|---|---|---|---|
| primary | `#635BFF` | `#FFFFFF` | `8px` | `11.5/13.5/15.5px` top | `filter: brightness(1.06)` |
| primary-dark | `#0D1738` | `#FFFFFF` | `8px` | 동일 | lighten to `#1A2C44` |
| secondary | `transparent` | `#0D1738` | `8px` | 동일 + `1px solid #D4DEE9` | `bg #F8FAFD` |
| ghost | `transparent` | `#635BFF` | `8px` | 동일 | `bg #F5F5FF` |

### Cards & Containers

```html
<article class="hds-card">
  <h3>Accept payments</h3>
  <p>...</p>
</article>
```

- bg: `#FFFFFF` (light) / `#0D253D` (dark)
- border: `1px solid #D4DEE9` or none
- radius: `12px` 기본 / `16px` hero
- padding: `24px` / `32px`
- shadow: `shadow-sm` (2-layer dual) rest → `shadow-md` hover

### Navigation

- 로고: 좌측 Stripe mark (검정 `#0D1738`)
- 링크: sohne-var 14px weight 400, color `#3C4F69`, hover `#0D1738`
- Active: color `#0D1738`, weight 500
- CTA: 우측 "Sign in" + primary "Contact sales"
- Backdrop: `blur(12px)` on scroll

### Inputs & Forms

- height: `40px`
- padding: `0 12px`
- border: `1px solid #D4DEE9`
- radius: `8px`
- focus: `box-shadow: 0 0 0 3px rgba(99,91,255,0.25); border-color: #635BFF`
- placeholder: `color: #95A4BA`

### Stats / Numbers (signature)

```html
<div class="stats"><span style="color:#0810BF">2.8B+</span></div>
```

- color: `#0810BF / #4304EA / #8A35DF / #C42FA5` 4색 순환
- font: sohne-var `56-72px weight 600 ls -0.03em`
- 개별 stat마다 다른 색 할당

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결한 선언 + 비즈니스 impact | "Financial infrastructure to grow your revenue" |
| Primary CTA | 2단어, 강한 동사 | "Start now" / "Contact sales" |
| Secondary CTA | 관찰형 | "Learn more" |
| Stat copy | 큰 숫자 + 짧은 단위 | "2.8B+ API requests daily" |
| Tone | 신뢰 + 정밀 + 약간의 자신감 | — |

---

## 15. Drop-in CSS

```css
/* Stripe — copy into your root stylesheet */
:root {
  /* Fonts */
  --stripe-font-sans: "sohne-var","SF Pro Display",
    -apple-system,BlinkMacSystemFont,sans-serif;
  --stripe-font-mono: SourceCodePro,ui-monospace,"SF Mono",Menlo,monospace;

  /* Brand */
  --stripe-brand:        #635BFF;
  --stripe-brand-strong: #533AFD;
  --stripe-brand-50:     #E8E9FF;
  --stripe-brand-100:    #D6D9FC;
  --stripe-brand-700:    #4032C8;
  --stripe-brand-900:    #1C1E54;

  /* Gradient */
  --stripe-accent-gradient:
    linear-gradient(90deg, #BDB4FF 0%, #643AFD 50%, #533AFD 100%);

  /* Surfaces (light) */
  --stripe-bg:         #FFFFFF;
  --stripe-surface:    #F8FAFD;
  --stripe-surface-alt:#F6F9FC;
  --stripe-border:     #D4DEE9;
  --stripe-fg:         #0D1738;
  --stripe-fg-muted:   #64748D;
  --stripe-fg-subtle:  #7D8BA4;

  /* Surfaces (dark) */
  --stripe-bg-dark:     #0D253D;
  --stripe-bg-darkest:  #061B31;
  --stripe-fg-on-dark:  #FFFFFF;

  /* Status */
  --stripe-success: #00B261;
  --stripe-error:   #D8351E;
  --stripe-warning: #F9B900;

  /* Spacing */
  --stripe-space-sm:  8px;
  --stripe-space-md:  16px;
  --stripe-space-lg:  32px;
  --stripe-space-xl:  64px;
  --stripe-space-2xl: 96px;

  /* Radius */
  --stripe-radius-sm:  8px;
  --stripe-radius-md:  12px;
  --stripe-radius-lg:  16px;
  --stripe-radius-pill:9999px;

  /* Shadow (2-layer dual) */
  --stripe-shadow-sm:
    0 2px 4px rgba(0,55,112,0.08),
    0 4px 8px rgba(0,59,137,0.05);
  --stripe-shadow-md:
    0 4px 8px rgba(0,55,112,0.10),
    0 8px 16px rgba(0,59,137,0.03);
  --stripe-shadow-lg:
    0 8px 16px rgba(0,55,112,0.10),
    0 16px 32px rgba(0,59,137,0.04);
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Stripe
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#635BFF',
          25:  '#F5F5FF',
          50:  '#E8E9FF',
          100: '#D6D9FC',
          200: '#B9B9F9',
          300: '#9A9AFE',
          400: '#7F7DFC',
          500: '#665EFD',
          600: '#533AFD',
          700: '#4032C8',
          800: '#2E2B8C',
          900: '#1C1E54',
          950: '#161741',
        },
        neutral: {
          0:   '#FFFFFF',
          25:  '#F8FAFD',
          50:  '#E5EDF5',
          100: '#D4DEE9',
          200: '#BAC8DA',
          300: '#95A4BA',
          400: '#7D8BA4',
          500: '#64748D',
          600: '#50617A',
          700: '#3C4F69',
          800: '#273951',
          900: '#1A2C44',
          950: '#11273E',
          975: '#0D253D',
          990: '#061B31',
        },
      },
      fontFamily: {
        sans: ['sohne-var', 'SF Pro Display', 'system-ui'],
        mono: ['SourceCodePro', 'ui-monospace'],
      },
      fontWeight: {
        normal:   '400',
        medium:   '500',
        semibold: '550',
        bold:     '600',
      },
      borderRadius: {
        sm: '4px', DEFAULT: '8px',
        md: '12px', lg: '16px', xl: '20px',
        pill: '9999px',
      },
      screens: {
        xs:  '400px',
        sm:  '480px',
        md:  '600px',
        lg:  '640px',
        xl:  '840px',
        '2xl': '940px',
        '3xl': '1115px',
        '4xl': '1264px',
      },
      backgroundImage: {
        'accent-gradient':
          'linear-gradient(90deg, #BDB4FF 0%, #643AFD 50%, #533AFD 100%)',
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
| Brand primary | `--stripe-brand` | `#635BFF` |
| Brand gradient end | `--stripe-brand-strong` | `#533AFD` |
| Background | `--stripe-bg` | `#FFFFFF` |
| Surface | `--stripe-surface` | `#F8FAFD` |
| Text heading | `--stripe-fg` | `#0D1738` |
| Text muted | `--stripe-fg-muted` | `#64748D` |
| Border | `--stripe-border` | `#D4DEE9` |
| Dark bg | `--stripe-bg-dark` | `#0D253D` |
| Success | `--stripe-success` | `#00B261` |
| Error | `--stripe-error` | `#D8351E` |

### Example Component Prompts

#### Hero Section

```
Stripe 스타일 히어로 섹션.
- 배경: #FFFFFF + 뒷면 accent-gradient
  (linear-gradient(90deg, #BDB4FF, #643AFD, #533AFD))
- H1: sohne-var 48px weight 600, tracking -0.03em, color #0D1738
- Sub: 18px color #50617A line-height 1.5
- Primary CTA: bg #635BFF color #FFF radius 8px
  padding 15.5px 24px 16.5px, font weight 500
- Secondary CTA: transparent border 1px solid #D4DEE9
  color #0D1738
- 2-column split: 좌측 텍스트, 우측 product mockup
- Max-width: 1295px
```

#### Card Component

```
Stripe 스타일 카드.
- bg #FFFFFF, border 1px solid #D4DEE9, radius 12px
- padding 32px
- shadow rest:
    0 2px 4px rgba(0,55,112,0.08),
    0 4px 8px rgba(0,59,137,0.05)
- shadow hover (2-layer dual upgrade):
    0 4px 8px rgba(0,55,112,0.10),
    0 8px 16px rgba(0,59,137,0.03)
- transition 200ms cubic-bezier(0.4,0,0.2,1)
- 제목: sohne-var 22px weight 550 color #0D1738
- 본문: 16px color #3C4F69 line-height 1.6
```

#### Stats Block (signature)

```
Stripe stat number 블록.
- 숫자: sohne-var 72px weight 600, tracking -0.03em
- 색상 순환: #0810BF → #4304EA → #8A35DF → #C42FA5
- 단위/설명: 14px color #64748D, 상단 margin 8px
- 1-row 3-col grid, gap 48px
- 배경: #FFFFFF 또는 #F8FAFD
```

#### Navigation

```
Stripe 상단 네비게이션.
- height 72px, position sticky top 0
- bg rgba(255,255,255,0.85) + backdrop-filter blur(12px)
- 스크롤 시 border-bottom 1px solid rgba(0,0,0,0.08)
- 로고 Stripe mark, 좌측
- 링크 sohne-var 14px weight 400 color #3C4F69 hover #0D1738
- Active: color #0D1738 weight 500
- CTA 우측: "Sign in" 링크 + "Contact sales" primary button
```

### Iteration Guide

- **색상 변경 시**: `--hds-*` 또는 `--stripe-*` semantic token만 사용. raw hex 직접 금지.
- **폰트 변경 시**: `sohne-var`가 기본. 대체 시 `Inter Variable` + weight 400/500/550/600 매핑.
- **여백 조정 시**: `--hds-space-core-*` (4/8/12/16/24/32/48/64) 중에서만.
- **새 컴포넌트 추가 시**: radius `4/8/12/16/20` 중 하나. nested 시 `card-radius-inner: 5px` 패턴.
- **Shadow**: 단층 shadow 금지. 반드시 top + bottom 2-layer dual.
- **반응형**: 10단계 breakpoint 중 적절한 것 선택. 커스텀 breakpoint 금지.
- **Dark 섹션**: 같은 페이지에서 light/dark 교차 가능. dark bg는 `#0D253D` 또는 `#061B31`.
- **transition**: `200ms cubic-bezier(0.4,0,0.2,1)` 기본. 400ms 이상 금지 (scroll animation 제외).

---

## 18. DO / DON'T

### ✅ DO

- 배경은 `#FFFFFF`로 (light) 또는 `#0D253D`로 (dark 섹션). 둘 다 같은 페이지에서 교차 가능.
- CTA primary는 `#635BFF` 배경 + `#FFFFFF` 텍스트 + `border-radius: 8px`.
- 본문은 sohne-var `16px` `weight 400` `color #3C4F69` 또는 `#0D1738`.
- Card radius는 `12px` 기본, `16px` hero.
- Shadow는 반드시 **top + bottom 2-layer dual** — 예: `0 2px 4px rgba(0,55,112,0.08), 0 4px 8px rgba(0,59,137,0.05)`.
- Heading weight는 `500 / 550 / 600` variable axis 값 사용.
- Stat number는 `#0810BF → #4304EA → #8A35DF → #C42FA5` 4색 순환.
- Gradient는 `#BDB4FF → #643AFD → #533AFD` 3-stop.

### ❌ DON'T

- `#635BFF`를 flat 배경으로 쓰지 말 것 — indigo는 CTA, focus, gradient stop에만.
- 본문 텍스트를 `#000000`로 두지 말 것 — 대신 `#0D1738` (heading) 또는 `#3C4F69` (body).
- `box-shadow: 0 2px 4px rgba(0,0,0,0.1)` 같은 단층 shadow 금지 — 반드시 2-layer dual.
- body에 `font-weight: 500`을 쓰지 말 것 — Stripe body는 `400`. Heading만 `500/550/600`.
- radius `10px` 같은 비표준 값 금지 — `4 / 8 / 12 / 16 / 20` 중 하나.
- Single breakpoint 반응형 금지 — Stripe는 10단계. heading size가 bp별 자체 성장.
- `sohne-var` 대신 Söhne non-variable을 쓰지 말 것 — weight 550, 425 같은 중간값을 잃는다.
- transition `400ms` 이상 금지 (scroll animation 제외) — Stripe hover는 `200ms` 고정.
- Gradient를 수직(`linear-gradient(180deg, …)`)으로 쓰지 말 것 — Stripe accent gradient는 `90deg` 수평 고정.
- `--hds-color-brand-100`을 CTA 배경에 쓰지 말 것 — `--hds-color-brand-500/600` 만 primary.
