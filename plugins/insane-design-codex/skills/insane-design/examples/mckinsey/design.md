---
slug: mckinsey
service_name: McKinsey & Company
site_url: https://www.mckinsey.com
fetched_at: 2026-04-15
default_theme: light
brand_color: "#2251FF"
primary_font: McKinsey Sans
font_weight_normal: 400
token_prefix: --mdc-*
---

# DESIGN.md — McKinsey & Company (Codex Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

맥킨지(McKinsey & Company)는 전략 컨설팅 업계의 최상위 브랜드답게 **지적 권위와 신뢰**를 UI 언어로 삼는다. 흰 배경 위에 딥블루 `#051C2C`(deep-blue)가 헤더·섹션 배경으로 등장하고, 일렉트릭 블루 `#2251FF`(electric-blue)가 링크·CTA·인터랙티브 요소에 집중 투입된다. 전통과 혁신의 균형 — 세리프 `Bower` + 산세리프 `McKinsey Sans`의 조합이 이 정체성을 폰트로 표현한다.

색상 전략은 **깊은 네이비 + 브라이트 블루 이중 구조**다. `#051C2C`(딥 네이비)가 권위를 담당하고, `#2251FF`(일렉트릭 블루)가 액션/링크를 맡는다. 이 두 색이 대부분의 UI를 처리한다. `#00A9F4`(사이언)은 악센트, `#FC0D9F`(핫핑크)는 시각적으로 강렬하지만 그라디언트 장식 전용이다. 중성 배경은 순백 `#FFFFFF`이며, 네이비 섹션이 교차해 깊이를 만든다.

폰트는 두 개의 자체 서체다. `McKinsey Sans`가 산세리프 primary body이고, `Bower`(Georgian 계열)가 에디토리얼 헤드라인에 사용된다. MUI 기반으로 `--mdc-font-family-default-primary/secondary` 변수로 다국어 폰트(아랍·일본어·러시아어·베트남어)를 관리한다. 기본 weight는 400이지만 500·600이 강조에 빈번하게 등장한다.

여백은 컨설팅 보고서처럼 체계적이다. 컨테이너 max-width `1179px`, 섹션 패딩은 `.25rem`부터 `2.5rem`까지 규칙적 간격. elevation은 `--mdc-elevation-*` 토큰으로 4단계(2/4/8/16px) 정의된 그림자 시스템이 있다.

인터랙션은 `all .12s linear`로 매우 빠르고 즉각적인 반응을 준다. 비즈니스 효율을 강조하는 듯 군더더기 없는 전환 속도.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 McKinsey처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "McKinsey Sans", "Helvetica Neue", Calibri, Helvetica, Roboto, sans-serif;
  font-weight: 400;
}
h1, h2, h3 {
  font-family: "Bower", Georgia, "Times New Roman", serif;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1B1B19; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #2251FF; --brand-deep: #051C2C; }
```

**절대 하지 말아야 할 것 하나**: 텍스트나 섹션 배경에 `#FC0D9F` 핫핑크를 사용하는 것. 이 색은 CSS 그라디언트 장식에만 사용되며, UI 요소에 적용하면 컨설팅 브랜드의 신뢰감이 완전히 무너진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.mckinsey.com` |
| Fetched | 2026-04-15 |
| Extractor | Playwright MCP (headless Chromium, bot-bypass) |
| HTML size | 649,095 bytes (React/MUI SSR) |
| CSS files | 5개 외부 + 461,889자 인라인, 총 1,430,214자 |
| Token prefix | `--mdc-*` (McKinsey Design Company 토큰 시스템) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React + MUI (Material UI 기반 커스텀)
- **Design system**: MDC (McKinsey Design Company) — prefix `--mdc-*`
- **CSS architecture**: MDC 토큰 + MUI 오버라이드
  ```
  --mdc-color-palette-*   브랜드 팔레트 (electric-blue, deep-blue, cyan)
  --mdc-color-status-*    상태 컬러 시스템 (neutral/blue/yellow/red/green)
  --mdc-elevation-*       그림자 토큰 (2/4/8/16px)
  --mdc-font-family-*     다국어 폰트 패밀리 토큰
  ```
- **Class naming**: MUI 자동 생성 + MDC BEM 클래스
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 CDN (`McKinsey Sans`, `Bower`, `mck-icons`)
- **Canonical anchor**: `#2251FF` (electric-blue) — CTA·링크·활성 인터랙션 전용

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `McKinsey Sans` (자체 커스텀, 유료)
- **Editorial headline**: `Bower` (세리프, Georgian 계열)
- **Icon font**: `mck-icons`
- **Fallback (primary)**: `"Helvetica Neue"`, `Calibri`, `Corbel`, `Helvetica`, `Roboto`, `Droid`, `sans-serif`
- **Fallback (secondary)**: `Georgia`, `"Times New Roman"`, `serif`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --mdc-font-family-default-primary: "McKinsey Sans", "Helvetica Neue", Calibri, Corbel, Helvetica, Roboto, Droid, sans-serif;
  --mdc-font-family-default-secondary: "Bower", Georgia, "Times New Roman", serif;
  --mck-font-weight-normal: 400;
  --mck-font-weight-bold: 600;
}
body {
  font-family: var(--mdc-font-family-default-primary);
  font-weight: var(--mck-font-weight-normal);
}
h1, h2 {
  font-family: var(--mdc-font-family-default-secondary);
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| xs / caption | 0.75rem (12px) | 400 | 1.5 | 0 |
| base / body | 1rem (16px) | 400 | 1.75rem | 0 |
| md | 1.125rem (18px) | 400–500 | 1.5 | 0 |
| lg | 1.5rem (24px) | 400–600 | 1.3 | -0.01em |
| xl / headline | 2rem+ | 400 (Bower) | 1.2 | -0.02em |

> ⚠️ McKinsey 기본 line-height는 `1.75rem`(수치값 아닌 고정 rem). 헤드라인은 Bower 세리프 400, 본문은 McKinsey Sans 400. 혼용 시 line-height 단위 통일에 주의.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Electric Blue)

| Token | Hex |
|---|---|
| --mdc-color-palette-cyan | `#00A9F4` |
| --mdc-color-palette-electric-blue | `#2251FF` |
| --mdc-color-palette-deep-blue | `#051C2C` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| deep-blue | `#051C2C` |
| electric-blue-dark | `#1E32E6` |

### 06-3. Neutral Ramp

| Step | Hex |
|---|---|
| light neutral bg | `#EBEBF6` |
| dark neutral text | `#1B1B19` |
| black | `#000000` |
| white | `#FFFFFF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Cyan | accent | `#00A9F4` |
| Hot Pink (장식용) | gradient only | `#FC0D9F` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --mdc-color-primary | `#2251FF` (electric-blue) | CTA, 링크, 활성 |
| --mdc-color-status-dark-neutral | `#1B1B19` | 기본 텍스트 |
| --mdc-color-status-light-neutral | `#EBEBF6` | 배경 교차 |
| --mdc-color-status-dark-blue | `#1E32E6` | 호버 CTA |
| --mdc-color-status-light-blue | `#E6ECFF` | 선택된 상태 bg |
| --mdc-color-status-red | `#D51F31` | 에러 |
| --mdc-color-status-green | `#007F26` | 성공 |
| --mdc-color-status-yellow | `#FFD048` | 경고 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| --mdc-color-primary | var(--mdc-color-palette-electric-blue) | 모든 기본 액션 |
| --mdc-color-neutral-black | `#000000` | 완전 검정 |
| --mdc-color-neutral-dark-neutral | `#1B1B19` | 거의 검정 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 221 | neutral — 배경 |
| 2 | `#FC0D9F` | 212 | chromatic — 장식 그라디언트 (UI 사용 금지!) |
| 3 | `#000000` | 136 | neutral — 텍스트/아이콘 |
| 4 | `#2251FF` | 126 | chromatic — 브랜드 액션 블루 |
| 5 | `#00000000` | 70 | neutral — 투명 |
| 6 | `#00A9F4` | 40 | chromatic — 시안 악센트 |
| 7 | `#051C2C` | 30 | chromatic — 딥 네이비 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-1 | 0.25rem (4px) | 최소 gap |
| space-2 | 0.5rem (8px) | 인라인 패딩 |
| space-4 | 1rem (16px) | 컴포넌트 패딩 |
| space-6 | 1.5rem (24px) | 섹션 내부 |
| space-8 | 2rem (32px) | 카드 gap |
| space-10 | 2.5rem (40px) | 섹션 패딩 |

**주요 alias**:
- 섹션 패딩: `1.5rem`–`2.5rem` 범위

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | `0` | 인라인 요소 |
| radius-sm | `0.25rem` (4px) | 작은 버튼·태그 |
| radius-md | `0.75rem` (12px) | 카드·모달 |
| radius-full | `17px` | 알약형 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| --mdc-elevation-2 | `0px 2px 4px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)` | 카드 기본 |
| --mdc-elevation-4 | `0px 4px 8px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)` | hover 카드 |
| --mdc-elevation-8 | `0px 8px 16px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)` | 드롭다운 |
| --mdc-elevation-16 | `0px 16px 32px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)` | 모달 |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| duration-fast | `0.12s` | 모든 hover/active 전환 |
| easing-linear | `linear` | 색상 전환 |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1179px` (메인 컨테이너)
- **Grid type**: 12열 그리드 + Flexbox
- **Column count**: 12 (데스크톱), 4 (모바일)
- **Gutter**: 24px

### Hero
- Layout: 2열 (텍스트 좌 + 이미지/카드 우)
- Background: `#FFFFFF` 또는 `#051C2C` (딥 네이비)
- H1: `Bower`, 2rem+, weight 400, color `#1B1B19` 또는 `#FFFFFF`
- Max-width: `1179px`

### Section Rhythm
```css
section {
  padding: 2rem 1.5rem;
  max-width: 1179px;
  margin: 0 auto;
}
```

### Card Patterns
- **Card background**: `#FFFFFF`
- **Card border**: `none`
- **Card radius**: `0.25rem`–`0.75rem`
- **Card padding**: `1.5rem`
- **Card shadow**: `--mdc-elevation-2`

### Navigation Structure
- **Type**: 수평 드롭다운 메뉴
- **Position**: sticky top
- **Height**: 약 64px
- **Background**: `#FFFFFF`
- **Border**: `1px solid #EBEBF6` 하단

### Content Width
- **Prose max-width**: `1179px`
- **Container max-width**: `1179px`
- **Sidebar width**: N/A (없음, 전체 너비 기사형)

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | 479px | 1열, 햄버거 메뉴 |
| Tablet | 767px | 2열 카드 |
| Desktop | 1179px | 3열 카드, 전체 메뉴 |
| Large | 1439px | 최대 레이아웃 |

### Touch Targets
- **Minimum tap size**: 44px
- **Button height (mobile)**: 44px
- **Input height (mobile)**: 44px

### Collapsing Strategy
- **Navigation**: 햄버거 → 전폭 오버레이
- **Grid columns**: 12열 → 4열 → 2열 → 1열
- **Sidebar**: N/A
- **Hero**: 2열 → 1열 스택

### Image Behavior
- **Strategy**: 반응형 `object-fit: cover`
- **Max-width**: 100%
- **Aspect ratio handling**: 16:9 (편집 이미지), 1:1 (저자 사진)

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="mck-btn-primary">Read the report</button>
```

```css
.mck-btn-primary {
  background: #2251FF;
  color: #FFFFFF;
  font-family: "McKinsey Sans", "Helvetica Neue", sans-serif;
  font-size: 1rem;
  font-weight: 500;
  border: none;
  border-radius: 0.25rem;
  padding: 12px 24px;
  min-height: 44px;
  cursor: pointer;
  transition: all 0.12s linear;
}
.mck-btn-primary:hover { background: #1E32E6; }

.mck-btn-outline {
  background: transparent;
  color: #2251FF;
  border: 2px solid #2251FF;
  border-radius: 0.25rem;
  padding: 12px 24px;
  font-family: "McKinsey Sans", sans-serif;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.12s linear;
}
.mck-btn-outline:hover { background: #E6ECFF; }
```

| Spec | Value |
|---|---|
| bg | `#2251FF` |
| text | `#FFFFFF` |
| radius | `0.25rem` (4px) |
| height | `44px` |
| transition | `all 0.12s linear` |

### Badges

```css
.mck-badge {
  background: #E6ECFF;
  color: #2251FF;
  font-family: "McKinsey Sans", sans-serif;
  font-size: 0.75rem;
  font-weight: 500;
  border-radius: 17px;
  padding: 2px 10px;
}
.mck-badge-deep {
  background: #051C2C;
  color: #FFFFFF;
  border-radius: 17px;
}
```

### Cards & Containers

```css
.mck-article-card {
  background: #FFFFFF;
  border: none;
  border-radius: 0.25rem;
  padding: 1.5rem;
  box-shadow: 0px 2px 4px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1);
  transition: box-shadow 0.12s linear;
}
.mck-article-card:hover {
  box-shadow: 0px 4px 8px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1);
}
.mck-article-card-title {
  font-family: "Bower", Georgia, serif;
  font-size: 1.5rem;
  font-weight: 400;
  color: #1B1B19;
  line-height: 1.3;
}
.mck-article-card-topic {
  font-family: "McKinsey Sans", sans-serif;
  font-size: 0.75rem;
  font-weight: 500;
  color: #2251FF;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### Navigation

```css
.mck-nav {
  background: #FFFFFF;
  border-bottom: 1px solid #EBEBF6;
  height: 64px;
  position: sticky;
  top: 0;
  z-index: 100;
}
.mck-nav-logo {
  font-family: "McKinsey Sans", sans-serif;
  font-size: 1rem;
  font-weight: 600;
  color: #1B1B19;
}
.mck-nav-link {
  font-family: "McKinsey Sans", sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  color: #1B1B19;
  text-decoration: none;
}
.mck-nav-link:hover { color: #2251FF; }
```

### Inputs & Forms

```css
.mck-input {
  border: 1px solid #EBEBF6;
  border-radius: 0.25rem;
  height: 44px;
  padding: 0 16px;
  font-family: "McKinsey Sans", sans-serif;
  font-size: 1rem;
  font-weight: 400;
  color: #1B1B19;
  background: #FFFFFF;
  outline: none;
  transition: border-color 0.12s linear;
}
.mck-input:focus { border-color: #2251FF; }
```

### Hero Section

```css
.mck-hero {
  background: #051C2C;
  color: #FFFFFF;
  padding: 4rem 2rem;
  max-width: 100%;
}
.mck-hero-inner {
  max-width: 1179px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}
.mck-hero-headline {
  font-family: "Bower", Georgia, serif;
  font-size: 3rem;
  font-weight: 400;
  color: #FFFFFF;
  line-height: 1.2;
  letter-spacing: -0.02em;
}
.mck-hero-sub {
  font-family: "McKinsey Sans", sans-serif;
  font-size: 1.125rem;
  font-weight: 400;
  color: rgba(255,255,255,0.8);
  line-height: 1.75rem;
  margin-top: 1rem;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 통찰·질문형, Bower 세리프 | "What's your next brilliant move?" |
| Primary CTA | 명확한 행동+목적어 | "Read the report", "Watch the interview" |
| Secondary CTA | 카테고리 이동 | "Our Insights", "Capabilities" |
| Topic label | 대문자 + letter-spacing | "INTERVIEW", "BLOG POST" |
| Tone | 비즈니스 전문가 타겟, 권위 있되 접근 가능 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* McKinsey & Company — copy into your root stylesheet */
:root {
  /* Fonts */
  --mck-font-family: "McKinsey Sans", "Helvetica Neue", Calibri, Helvetica, Roboto, sans-serif;
  --mck-font-family-heading: "Bower", Georgia, "Times New Roman", serif;
  --mck-font-weight-normal: 400;
  --mck-font-weight-bold: 600;

  /* Brand */
  --mck-color-brand: #2251FF;
  --mck-color-brand-dark: #1E32E6;
  --mck-color-deep: #051C2C;
  --mck-color-cyan: #00A9F4;

  /* Surfaces */
  --mck-bg-page: #FFFFFF;
  --mck-bg-dark: #051C2C;
  --mck-text: #1B1B19;
  --mck-text-muted: #7B7B78;

  /* Key spacing */
  --mck-space-sm: 0.5rem;
  --mck-space-md: 1rem;
  --mck-space-lg: 2.5rem;

  /* Radius */
  --mck-radius-sm: 0.25rem;
  --mck-radius-md: 0.75rem;

  /* Elevation */
  --mck-shadow-sm: 0px 2px 4px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1);
  --mck-shadow-md: 0px 4px 8px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — McKinsey & Company
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#2251FF',
          dark: '#1E32E6',
          light: '#E6ECFF',
        },
        deep: '#051C2C',
        cyan: '#00A9F4',
        neutral: {
          50: '#EBEBF6',
          900: '#1B1B19',
        },
        status: {
          red: '#D51F31',
          green: '#007F26',
          yellow: '#FFD048',
        },
      },
      fontFamily: {
        sans: ['"McKinsey Sans"', '"Helvetica Neue"', 'Calibri', 'Helvetica', 'Roboto', 'sans-serif'],
        serif: ['"Bower"', 'Georgia', '"Times New Roman"', 'serif'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        bold: '600',
      },
      borderRadius: {
        sm: '0.25rem',
        DEFAULT: '0.25rem',
        md: '0.75rem',
        full: '17px',
      },
      boxShadow: {
        sm: '0px 2px 4px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)',
        md: '0px 4px 8px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)',
        lg: '0px 8px 16px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)',
        xl: '0px 16px 32px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)',
      },
      maxWidth: {
        content: '1179px',
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
| Brand primary | --mck-color-brand | `#2251FF` |
| Brand deep | --mck-color-deep | `#051C2C` |
| Background | --mck-bg-page | `#FFFFFF` |
| Text primary | --mck-text | `#1B1B19` |
| Text muted | --mck-text-muted | `#7B7B78` |
| Border | N/A | `#EBEBF6` |
| Success | --mdc-color-status-green | `#007F26` |
| Error | --mdc-color-status-red | `#D51F31` |

### Example Component Prompts

#### Hero Section
```
McKinsey 스타일 히어로 섹션을 만들어줘.
- 배경: #051C2C (딥 네이비)
- H1: "Bower" Georgia serif, 3rem, weight 400, color #FFFFFF, letter-spacing -0.02em
- 서브텍스트: "McKinsey Sans", 1.125rem, weight 400, color rgba(255,255,255,0.8)
- CTA 버튼: bg #2251FF, text #FFFFFF, radius 4px, padding 12px 24px
- 레이아웃: 2열 (텍스트 좌, 이미지 우), max-width 1179px
```

#### Card Component
```
McKinsey 스타일 아티클 카드를 만들어줘.
- 배경: #FFFFFF, border: none, radius: 4px
- padding: 1.5rem
- shadow: 0px 2px 4px -1px rgba(5,28,44,0.2), 0px 0px 1px 0px rgba(5,28,44,0.1)
- hover shadow: 0px 4px 8px -1px rgba(5,28,44,0.2)
- 주제 레이블: "McKinsey Sans", 0.75rem, weight 500, color #2251FF, uppercase, letter-spacing 0.05em
- 제목: "Bower" serif, 1.5rem, weight 400, color #1B1B19
- 날짜/메타: 0.875rem, weight 400, color #7B7B78
```

#### Badge
```
McKinsey 스타일 토픽 배지를 만들어줘.
- font: "McKinsey Sans", 0.75rem, weight 500, uppercase, letter-spacing 0.05em
- padding: 2px 10px, radius: 17px
- 기본: bg #E6ECFF, text #2251FF
- 딥: bg #051C2C, text #FFFFFF
```

#### Navigation
```
McKinsey 스타일 상단 네비게이션을 만들어줘.
- 높이: 64px, bg: #FFFFFF, border-bottom: 1px solid #EBEBF6
- 로고: 좌측, "McKinsey Sans", 1rem, weight 600, color #1B1B19
- 링크: "McKinsey Sans", 0.875rem, weight 400, color #1B1B19
- 링크 hover: color #2251FF
- CTA: bg #2251FF, text #FFFFFF, radius 4px
```

### Iteration Guide

- **색상 변경 시**: `#2251FF` 액션 블루와 `#051C2C` 딥 네이비 두 축 유지.
- **폰트 변경 시**: body는 McKinsey Sans 400, 제목은 Bower serif 400.
- **여백 조정 시**: `0.25rem`·`0.5rem`·`1rem`·`1.5rem`·`2.5rem` 단위로만.
- **새 컴포넌트 추가 시**: `--mdc-elevation-*` shadow 패턴 적용, radius 4px.
- **dark 섹션**: `#051C2C` bg + `#FFFFFF` text 조합.
- **반응형**: 479px·767px·1179px 기준.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- CTA 버튼에 `#2251FF` electric-blue 사용
- 다크 섹션에 `#051C2C` deep-blue 배경
- 헤드라인에 Bower 세리프, body에 McKinsey Sans 산세리프 분리
- 카드에 `--mdc-elevation-2` 이중 레이어 그림자 사용
- 토픽 레이블은 uppercase + letter-spacing 0.05em
- max-width `1179px` 컨테이너 고정

### ❌ DON'T
- `#FC0D9F` 핫핑크를 UI 요소에 사용 금지 (그라디언트 장식 전용!)
- 단층 box-shadow 사용 금지 — 반드시 이중 레이어 `rgba(5,28,44,*)` 패턴
- body 폰트에 Bower(세리프) 사용 금지 (헤드라인 전용)
- 컨테이너를 1179px 초과로 키우지 말 것
- `#00A9F4` 사이언을 primary 브랜드 컬러로 쓰지 말 것 (악센트 전용)
- 임의의 transition duration 사용 금지 — `0.12s linear` 유지
