---
schema_version: 3.1
slug: framer
service_name: Framer
site_url: https://www.framer.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#0099FF"
primary_font: Inter
font_weight_normal: 400
token_prefix: --framer-*, --token-*

bold_direction: "Motion-First Dark"
aesthetic_category: "Cool Productivity"
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Framer (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Framer의 마케팅 사이트는 **"캔버스 위에서 살아 움직이는 노코드 디자인 툴"**의 정체성을 시각적으로 증명한다. 전체 페이지는 거의 순흑에 가까운 `#080808`, `#090909`, `#141414` 의 3단 dark 레이어로 깔리고, 그 위에 거의 시그니처처럼 반복되는 **cyan `#0099FF` (#09F)** 점광원이 포인트 악센트로 등장한다. 페이지를 스크롤하면 scene 단위로 전환되는데, 각 scene은 미묘하게 다른 블랙 셰이드(`#171717` / `#1A1A1A` / `#1F1F1F`)로 구분되어 "똑같은 검정 아님"을 느끼게 설계되었다.

색상 전략은 **"모션이 컬러다"**에 가깝다. 정적인 팔레트로는 dark neutral + cyan 단색처럼 보이지만, 히어로와 블록 전환부에서 gradient (`#05f → #60f → #90f`)와 accent (`#FFEEAA` 버터옐로, `#FF7EB0` 핑크, `#ff9e00` 오렌지) 점광이 interaction 시에만 번진다. `#ffffff1a`, `#fffc`, `#fff9`, `#fff6` 같은 white-alpha 토큰을 층층이 겹쳐 glass/surface layering을 만든다 — 이게 Framer 특유의 "유리처럼 겹쳐진 패널" 느낌이다.

타이포그래피는 **Inter + Inter Display + Inter Tight**의 Inter family 3종을 축으로 삼는다. 히어로는 **Inter Display** 큰 타이틀 — 마케팅 hero 클래스 특화 폰트. 본문은 **Inter**, 강조는 **Inter Variable**. 코드 블록만 **JetBrains Mono** 또는 **Geist Mono**. 덤으로 **GT Walsheim Medium** 같은 유료 제품 타이틀용 폰트가 특정 랜딩(Marketing, GT Walsheim Framer Medium)에서 등장한다 — variable 대신 static weight를 선호.

레이아웃은 **canvas 그 자체**를 은유한다. section 간 큰 간격 없이 scroll-snap 류 스크롤링으로 scene을 연결하고, 각 scene은 full-bleed 이미지·비디오를 배경으로 깔고 텍스트는 overlay. hero나 feature 블록은 `border-radius: 24px ~ 32px`로 둥글게 감싸고, shadow 대신 bg layering으로 elevation. 카드 radius는 주로 `16px`·`24px`.

인터랙션이 브랜드다. Framer는 **hover에 motion이 따라오는 것**을 기본으로 설계한다 — transform scale, opacity fade, gradient shimmer. transition은 `.2s–.4s ease-out`이 주류. focus outline은 대개 `--framer-outline-color: #0099FF` cyan 2px ring.

### Key Characteristics

- Dark 3-5단 레이어 (`#080808` / `#090909` / `#141414` / `#171717` / `#1A1A1A`)
- Cyan `#0099FF` (#09F) 단일 시그니처 악센트
- Inter + Inter Display + Inter Tight — family 조합형
- White-alpha layering (`#fff9`, `#fff6`, `#fffc` 등으로 glass 효과)
- border-radius 16–32px — 카드부터 hero까지 둥글둥글
- scroll-snap scene 연결 — section 단절감 없음
- hover에 무조건 motion — scale, opacity, gradient shimmer

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Motion-First Dark
> **Aesthetic Category**: Cool Productivity
> **Signature Element**: 이 사이트는 **near-black 3단 위 cyan `#09F` 단일 악센트 + white-alpha layering + hover-driven motion**으로 기억된다.
> **Code Complexity**: high — variable axis + gradient + scroll-driven transitions 복합

---

## 01. Quick Start

> 5분 안에 Framer처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", "Inter Variable", "SF Pro Display", -apple-system, sans-serif;
  font-weight: 400;
  font-feature-settings: "cv11";
}

/* 2. 배경 + 텍스트 (dark primary) */
:root {
  --framer-bg: #080808;
  --framer-surface: #141414;
  --framer-fg: #FFFFFF;
  --framer-fg-muted: rgba(255,255,255,0.6);
}
body { background: var(--framer-bg); color: var(--framer-fg); }

/* 3. cyan accent */
:root {
  --framer-accent: #0099FF;
  --framer-accent-soft: #ffffff1a;
}
```

**절대 하지 말아야 할 것 하나**: 모든 dark 배경을 동일한 검정으로 두지 마라. Framer는 `#080808 / #090909 / #141414 / #171717` 4-5 단 미세 레이어로 "panel 겹침"을 만든다. 단일 `#000000` 배경은 OLED TV지, Framer가 아니다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.framer.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 추출 완료 (Framer Next.js build) |
| CSS files | 1개 인라인 478KB (`00-inline.css`) |
| Token prefix | `--framer-*`, `--token-{uuid}` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Framer Web Publish (자체 빌드) · React 18
- **Design system**: 내부 토큰 — `--framer-*` semantic + `--token-{uuid}` raw value
- **CSS architecture**: token-uuid + semantic alias 2-tier
  ```
  uuid    (--token-c534b380-e14e-...)       raw hex/value (UUID 네임)
  alias   (--framer-text-color, --framer-bg-color)  semantic 이름
  ```
- **Class naming**: `framer-{hash}` 해시 기반 (`.framer-text` + data-attribute)
- **Default theme**: dark (`#080808` page bg)
- **Font loading**: Framer CDN — Inter family + Inter Display + JetBrains Mono + 유료 GT Walsheim
- **Canonical anchor**: `#0099FF` (`#09F`) — cyan accent, outline color

---

## 04. Font Stack

- **Display**: `Inter Display` (Rasmus Andersson · OFL)
- **Body**: `Inter` / `Inter Variable`
- **Tight variant**: `Inter Tight` (마케팅 title)
- **Code**: `JetBrains Mono` / `Geist Mono`
- **Premium**: `GT Walsheim Framer Medium` (Grilli Type, 유료)
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --framer-font-sans: "Inter","Inter Variable","Inter Display",
    -apple-system,BlinkMacSystemFont,"Segoe UI","Roboto",sans-serif;
  --framer-font-mono: "JetBrains Mono","Geist Mono",
    ui-monospace,"SF Mono","Menlo",monospace;
  --framer-font-weight-normal: 400;
  --framer-font-weight-bold: 600;
}
body { font-family: var(--framer-font-sans); }
```

> **라이선스 주의**: GT Walsheim은 유료. 복제 시 `Inter Display`만으로 충분.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| caption | `12px` | 400 | 1.5 | 0 |
| small | `14px` | 400 | 1.5 | 0 |
| body | `16px` | 400 | 1.6 | -0.005em |
| lead | `18px` | 400 | 1.55 | -0.01em |
| h4 | `20px` | 500 | 1.4 | -0.01em |
| h3 | `24px` | 600 | 1.3 | -0.02em |
| h2 | `32px` | 600 | 1.2 | -0.02em |
| h1 | `48px` | 600 | 1.1 | -0.03em |
| display | `72px` | 600 | 1.05 | -0.04em |
| hero-xxl | `96–128px` | 600 | 1.0 | -0.05em |

> ⚠️ Framer는 Inter Display와 Inter Tight를 혼용한다 — hero는 Inter Display weight 600 letter-spacing `-0.04em`. 본문 `-0.005em` 미세 tracking이 독특.

---

## 06. Colors

### 06-1. Brand Anchor

| Token | Hex |
|---|---|
| `--framer-accent` | `#0099FF` |
| `--framer-accent-short` | `#09F` |
| `--framer-accent-deep` | `#05F` |
| `--framer-accent-purple` | `#60F` |
| `--framer-accent-magenta` | `#90F` |

### 06-3. Neutral Dark Ramp (5-step near-black)

| Step | Hex | Usage |
|---|---|---|
| page | `#080808` | 최상위 페이지 배경 |
| base | `#090909` | alt base |
| surface | `#141414` | 카드/패널 배경 |
| elevated | `#171717` | 호버/포커스 패널 |
| floating | `#1A1A1A` | modal/popover |
| subtle | `#1F1F1F` | section divider |
| border-soft | `#212121` | border 기본 |
| border | `#222222` | strong border |
| border-strong | `#242424` | divider strong |
| tint | `#2B2B2B` | input tint |
| tint-2 | `#2E2E2E` | input hover |
| text-q | `#888888` | text quaternary |
| text-m | `#999999` | text muted |
| text-s | `#666666` | text strong muted |
| text-pri | `#FFFFFF` | text primary |
| ink | `#000000` | dark ink (rare) |

### 06-4. Accent / Highlight

| Family | Hex | Use |
|---|---|---|
| cyan-accent | `#0099FF` | 기본 브랜드 |
| butter | `#FFEEAA` | highlight 포인트 |
| gradient-blue | `#05F` | hero gradient start |
| gradient-purple | `#60F` | gradient middle |
| gradient-magenta | `#90F` | gradient end |

### 06-5. Alpha Layers (Framer 시그니처)

| Token | Hex | Usage |
|---|---|---|
| white-alpha-10 | `#ffffff1a` (10% α) | soft divider, glass layer |
| white-alpha-60 | `#fff6` (40% α) | muted text on dark |
| white-alpha-75 | `#fff9` (56% α) | text secondary on dark |
| white-alpha-80 | `#fffc` (80% α) | text primary on dark alt |

<!-- SOURCE: auto (framer 토큰 시스템은 UUID 기반이므로 alias 레이어가 적음) -->

### 06-6. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--framer-text-color` | `#FFFFFF` (dark) / `#1D1D1D` (light) | 본문 |
| `--framer-link-text-color` | `#0099FF` | 링크 |
| `--framer-link-hover-text-color` | `#09F` brightened | hover 링크 |
| `--framer-blockquote-text-color` | `#FFFFFF` (dark) | 인용 텍스트 |
| `--framer-code-text-color` | `#0099FF` | 코드 인라인 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 근사)

| Rank | Hex | Role |
|---|---|---|
| 1 | `#000000` | neutral ink primary |
| 2 | `#FFFFFF` | text primary on dark |
| 3 | `#1D1D1D` | light-theme text |
| 4 | `#0099FF` | cyan accent (brand) |
| 5 | `#ffffff1a` | white-alpha glass layer |
| 6 | `#141414` | surface |
| 7 | `#666666` | text muted |
| 8 | `#FFEEAA` | butter highlight |

---

## 07. Spacing

Framer는 UUID 토큰 시스템 특성상 spacing scale 이름이 없다. 관찰상 `4px` 배수 체계.

| Token | Value | Use case |
|---|---|---|
| space-1 | `4px` | micro gap |
| space-2 | `8px` | small gap |
| space-3 | `12px` | small padding |
| space-4 | `16px` | 기본 padding |
| space-6 | `24px` | card padding |
| space-8 | `32px` | section inner |
| space-12 | `48px` | section gap |
| space-16 | `64px` | section block padding |
| space-20 | `80px` | large section pad |
| space-24 | `96px` | hero spacing |
| container | `1200px` | content max-width |
| container-wide | `1440px` | full section max |

<!-- SOURCE: template-default 포함 (Framer는 UUID 토큰이라 이름으로 추적 불가) -->

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| radius-sm | `8px` | small chip, badge |
| radius | `12px` | button, input |
| radius-md | `16px` | card |
| radius-lg | `24px` | hero block, feature card |
| radius-xl | `32px` | full-bleed scene block |
| pill | `9999px` | pill button, tag |
| circle | `50%` | avatar |

---

## 09. Shadows

Framer는 shadow 대신 **bg layering**으로 elevation을 만든다. shadow 토큰은 minimal.

| Level | Value | Usage |
|---|---|---|
| none | `none` | 기본 |
| subtle | `0 1px 2px rgba(0,0,0,0.2)` | floating card (template-default) |
| elevated | `0 8px 32px rgba(0,0,0,0.4)` | modal (template-default) |
| glow | `0 0 0 2px #0099FF4D` | focus ring (template-default) |

---

## 10. Motion

Framer는 모션이 브랜드다. Canvas 기반 interaction을 마케팅 사이트에도 재현.

| Token | Value | Usage |
|---|---|---|
| transition-fast | `.15s ease-out` | hover 작은 변화 |
| transition-base | `.2s ease-out` | 기본 transition |
| transition-smooth | `.4s cubic-bezier(0.4,0,0.2,1)` | scene 전환 |
| scroll-snap | `y mandatory` | scene 연결 |
| hover-scale | `scale(1.02)` | card hover |
| gradient-shimmer | `2s infinite` | hero gradient 애니메이션 |

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1200px` (기본) · `1440px` (wide)
- **Grid type**: CSS Grid / Flex hybrid
- **Column count**: 12 (관찰)
- **Gutter**: 24px

### Hero

- **🆕 Pattern Summary**: `~100vh dark bg + 중앙 H1 72–128px + cyan gradient accent + 하단 product canvas video`
- Layout: 1-column 중앙 정렬
- Background: `#080808` + gradient radial `#05F → #60F → #90F` 포인트
- **🆕 Background Treatment**: `near-black + radial gradient + animated canvas overlay`
- H1: `96–128px / weight 600 / ls -0.05em / Inter Display`
- Max-width: `1440px`

### Section Rhythm

```css
section {
  padding-block: 96px;
  padding-inline: 24px;
  max-width: 1440px;
  margin-inline: auto;
}
```

### Card Patterns

- **bg**: `#141414` (surface)
- **border**: `1px solid #ffffff1a` (white-alpha)
- **radius**: `16–24px`
- **padding**: `24–32px`
- **shadow**: 기본 none, hover 시 glow

### Navigation

- **type**: horizontal desktop / hamburger mobile
- **position**: `fixed top 0`
- **height**: `64px`
- **bg**: `rgba(8,8,8,0.8)` + `backdrop-filter: blur(12px)`
- **border**: 하단 `1px solid #ffffff1a`

### Content Width

- **prose**: `680px`
- **container**: `1200px`
- **wide**: `1440px`

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 640px` | 1-column |
| Tablet | `≥ 768px` | 2-col hero |
| Desktop | `≥ 1024px` | full container |
| Large | `≥ 1440px` | wide max |

### Touch Targets

- **min tap**: `44px`
- **button height**: `40–48px`
- **input height**: `40px`

### Collapsing

- **nav**: &lt;768px 햄버거
- **grid**: 12→1 모바일 reset
- **hero**: 1-column 유지, H1 128px → 48px

### Image Behavior

- **strategy**: Framer CDN, responsive srcset, `loading="lazy"`
- **max-width**: `100%`

---

## 13. Components

### Buttons

```html
<button class="framer-button framer-button--primary">Start free</button>
```

| Variant | background | color | radius | padding |
|---|---|---|---|---|
| primary | `#FFFFFF` | `#080808` | `12px` | `12px 24px` |
| accent | `#0099FF` | `#FFFFFF` | `12px` | `12px 24px` |
| ghost | transparent + border `#ffffff1a` | `#FFFFFF` | `12px` | 동일 |
| pill | 좌동 | 좌동 | `9999px` | 동일 |

### Badges

- background: `#ffffff1a`
- color: `#FFFFFF`
- radius: `9999px`
- font-size: `12px`, weight `500`
- padding: `4px 10px`

### Cards

- bg: `#141414`
- border: `1px solid #ffffff1a`
- radius: `24px`
- padding: `32px`
- hover: `transform translateY(-2px)`, border `#ffffff33`

### Navigation

- 로고: 좌측, `Framer` wordmark SVG
- 링크: Inter 14px weight 500, color `#fff9`
- Active: `#FFFFFF` weight 600
- CTA: "Start for free" (white pill) + "Sign in" (ghost)
- Height: `64px` fixed

### Inputs

- height: `40px`
- padding: `0 12px`
- bg: `#171717`
- border: `1px solid #ffffff1a`
- radius: `12px`
- focus: `outline 2px solid #0099FF`

### Hero Section

- bg: `#080808` + radial gradient
- H1: `Inter Display 128px weight 600 ls -0.05em color #FFFFFF`
- sub: `18px color #fff9`
- CTA: primary white pill + secondary ghost
- Canvas: autoplay video or interactive iframe

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 명사형 임팩트 | "The site builder for the AI era." |
| Primary CTA | 2–3 단어, 동사 | "Start for free" / "Try Framer" |
| Secondary CTA | 관찰형 | "See how it works" |
| Subheading | 제품 가치 1문장 | "Design, build, and publish a site in one place." |
| Tone | 쿨하고 확신 있게 | — |

---

## 15. Drop-in CSS

```css
/* Framer — copy into your root stylesheet */
:root {
  --framer-font-sans: "Inter","Inter Display",-apple-system,sans-serif;
  --framer-font-mono: "JetBrains Mono",ui-monospace,Menlo,monospace;
  --framer-font-weight-normal: 400;
  --framer-font-weight-bold: 600;

  /* Dark layers */
  --framer-bg:         #080808;
  --framer-surface:    #141414;
  --framer-elevated:   #171717;
  --framer-floating:   #1A1A1A;
  --framer-border:     #ffffff1a;

  /* Text */
  --framer-text:        #FFFFFF;
  --framer-text-muted:  #fff9;
  --framer-text-subtle: #fff6;

  /* Brand */
  --framer-accent:      #0099FF;
  --framer-accent-deep: #05F;
  --framer-gradient:    linear-gradient(135deg,#05F,#60F,#90F);

  /* Radius */
  --framer-radius-sm: 8px;
  --framer-radius:    12px;
  --framer-radius-md: 16px;
  --framer-radius-lg: 24px;

  /* Motion */
  --framer-transition: .2s ease-out;
}
body { background: var(--framer-bg); color: var(--framer-text); font-family: var(--framer-font-sans); }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Framer
module.exports = {
  theme: {
    extend: {
      colors: {
        framer: {
          bg:       '#080808',
          surface:  '#141414',
          elevated: '#171717',
          floating: '#1A1A1A',
          border:   '#ffffff1a',
          accent:   '#0099FF',
          butter:   '#FFEEAA',
        },
      },
      fontFamily: {
        sans: ['Inter','Inter Display','system-ui'],
        mono: ['JetBrains Mono','ui-monospace'],
      },
      fontWeight: { normal: '400', medium: '500', bold: '600' },
      borderRadius: { sm: '8px', DEFAULT: '12px', md: '16px', lg: '24px', xl: '32px', pill: '9999px' },
      transitionDuration: { DEFAULT: '200ms', fast: '150ms', slow: '400ms' },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand accent | `--framer-accent` | `#0099FF` |
| Page bg | `--framer-bg` | `#080808` |
| Surface | `--framer-surface` | `#141414` |
| Text primary | `--framer-text` | `#FFFFFF` |
| Text muted | `--framer-text-muted` | `#fff9` |
| Border | `--framer-border` | `#ffffff1a` |
| Highlight | butter | `#FFEEAA` |

### Example Component Prompts

#### Hero Section

```
Framer 스타일 히어로 섹션을 만들어줘.
- 배경: #080808 + radial-gradient(circle at 30% 50%, #05F 0%, #60F 40%, transparent 70%)
- H1: Inter Display, 128px, weight 600, ls -0.05em, color #FFFFFF
- sub: 18px, color rgba(255,255,255,0.6)
- CTA primary: bg #FFFFFF, color #080808, radius 12px, padding 12px 24px
- CTA secondary: transparent + border 1px solid #ffffff1a, color #FFFFFF
- 중앙 정렬, max-width 1440px
- 하단 product canvas (autoplay video 또는 iframe, radius 24px)
```

#### Card Component

```
Framer 스타일 카드 컴포넌트를 만들어줘.
- 배경: #141414
- border: 1px solid #ffffff1a
- radius: 24px
- padding: 32px
- hover: translateY(-2px), border #ffffff33, .2s ease-out
- 제목: Inter Display 24px weight 600 color #FFFFFF
- 본문: 16px color rgba(255,255,255,0.6)
```

#### Badge

```
Framer 스타일 배지를 만들어줘.
- bg rgba(255,255,255,0.1) (#ffffff1a)
- color #FFFFFF
- font Inter 12px weight 500
- padding 4px 10px, radius 9999px
- 강조 variant: bg #0099FF, color #FFFFFF
```

#### Navigation

```
Framer 스타일 상단 네비게이션을 만들어줘.
- height 64px, position fixed top 0
- bg rgba(8,8,8,0.8), backdrop-filter blur(12px)
- border-bottom 1px solid #ffffff1a
- 로고: 좌측 Framer wordmark SVG
- 링크: Inter 14px weight 500 color rgba(255,255,255,0.6)
- active: color #FFFFFF weight 600
- CTA 우측: "Sign in" (ghost) + "Start for free" (white pill)
```

### Iteration Guide

- **색상 변경 시** cyan `#0099FF` 고정. 다른 accent는 butter `#FFEEAA` 또는 gradient로만.
- **폰트 변경 시** Inter Display (히어로) + Inter (본문) 고정. weight 400/500/600.
- **여백 조정 시** 4px 배수. 특히 16/24/32/48/64/96 라인.
- **새 컴포넌트** radius는 8/12/16/24/32 중 하나.
- **다크 모드 유일** — light 테마는 보조적. 기본은 dark.
- **반응형** 640/768/1024/1440 4단.
- **모션** hover에 반드시 subtle transform 추가. static element 금지.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 `#080808` 또는 `#090909`. pure black `#000000` 쓰지 말 것.
- 다단 레이어 (page `#080808` → surface `#141414` → elevated `#171717`) 겹쳐 panel 계층 만들기.
- cyan accent `#0099FF`는 link/focus/CTA에만.
- border는 `#ffffff1a` (white 10% α) 소프트. hard border 금지.
- 본문 weight `400`, 타이틀 `600`. Inter family 고정.
- 카드 radius `24px`, 버튼 `12px`.
- hover에 `.2s ease-out transform scale` 추가.

### ❌ DON'T

- pure black `#000000` 배경 금지 — Framer는 `#080808` 3-5 단 레이어.
- 브랜드 cyan `#0099FF`를 넓은 면적에 쓰지 말 것 — accent 전용.
- weight `700` 쓰지 말 것 — `600`이 상한.
- radius `4px` 또는 `6px` 쓰지 말 것 — 최소 `8px`, 주류 `12–24px`.
- `box-shadow 0 4px 12px rgba(0,0,0,0.1)` 같은 light-theme shadow 금지 — dark bg에는 안 맞음.
- hover static 금지 — 반드시 motion 동반.
- light 테마를 기본으로 쓰지 말 것 — Framer 기본은 dark.
