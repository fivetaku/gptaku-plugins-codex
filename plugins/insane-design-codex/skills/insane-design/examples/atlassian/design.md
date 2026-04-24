---
schema_version: 3.1
slug: atlassian
service_name: Atlassian
site_url: https://www.atlassian.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#1868DB"
primary_font: Atlassian Sans
font_weight_normal: 400
token_prefix: --ds-*, --color-*, --space-*

bold_direction: "Refined SaaS"
aesthetic_category: "Refined SaaS"
signature_element: hero_impact
code_complexity: medium
campaign_active: true

medium: web
medium_confidence: high
---

# DESIGN.md — Atlassian (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Atlassian blue + 캠페인 보라·주황 팔레트을(를) 축으로 하는 디자인 시스템. Atlassian 2025 리브랜드 톤 + Team'26 컨퍼런스 캠페인을 동시에 수록. ADG/AtlasKit 토큰 기반.

Atlassian의 마케팅 홈은 refined saas 성격을 유지한다. 브랜드 컬러 `#1868DB`는 CTA, 링크, focus ring 등 의미가 필요한 지점에만 등장하며, 넓은 면적은 light 캔버스(`#FFFFFF` 계열)가 담당한다. 이 구조는 사용자가 "콘텐츠에 집중하게 하고, 색이 개입하는 순간은 결정이 필요한 순간"이라는 일관된 규율로 설계되었다.

색상 전략은 한 점 accent + neutral surface의 고전 SaaS 문법을 따른다. 체감상 가장 넓은 면적은 배경과 텍스트이고, `#1868DB`는 전체 픽셀의 5% 미만이다. 이런 절제가 "Atlassian다움"을 만든다.

타이포그래피는 **Atlassian Sans**를 기본 축으로 한다. body는 `400` weight에 `16px` 전후, H1은 `48~64px` 사이, 섹션 타이틀은 `24~32px` — 전통적인 8단 scale 안에서 움직인다. 글자 간격(letter-spacing)은 큰 사이즈에 음수 tracking을 적용해 시각 보정을 준다.

레이아웃은 1200-1440px content max-width + 8px baseline spacing 시스템 위에 놓인다. 섹션 간 리듬은 80-120px vertical padding으로 정돈되어 있고, 카드/컴포넌트는 12-16px radius를 공유한다. 모션은 `150-200ms` transition에 `ease-out`/`ease-in-out` 기본값을 사용 — 과하게 오래 끌거나 bouncy하지 않다.

### Key Characteristics

- Atlassian blue
- Team'26 campaign
- Atlassian Sans
- enterprise SaaS
- 8px spacing
- 4px-24px radius

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Refined SaaS
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: `hero_impact`
> **Code Complexity**: medium

---

## 01. Quick Start

> 5분 안에 Atlassian처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Atlassian Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 (light default) */
:root {
  --bg: #FFFFFF;
  --fg: #171717;
  --border: #E5E5E5;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 악센트 */
:root {
  --brand: #1868DB;
}
.cta {
  background: var(--brand); color: #FFFFFF;
  border-radius: 8px; padding: 0 16px; height: 40px;
  font-weight: 500;
}
```

**절대 하지 말아야 할 것 하나**: #1868DB를 본문 텍스트 색이나 긴 문단 배경으로 쓰지 말 것. Atlassian의 정체성은 brand accent를 **한 점**에만 올리는 절제다. 넓은 면적으로 가져가면 즉시 다른 제품이 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.atlassian.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |
| Token prefix | `--ds-*, --color-*, --space-*` |
| Screenshot | Jina Reader + PIL crop 1280×800 |

---

## 03. Tech Stack

- **Framework**: Next.js (marketing) + Gatsby fragments
- **Design system**: ADG (Atlassian Design Guidelines) + AtlasKit tokens
- **CSS architecture**: Emotion CSS-in-JS + `--ds-*` CSS variable layer
- **Class naming**: Emotion 해시 (<code>css-1abc23</code>) + BEM
- **Default theme**: light (bg #FFFFFF)
- **Font loading**: self-host Atlassian Sans + Atlassian Sans Display
- **Canonical anchor**: #1868DB (brand.primary) + #803FA5 (team'26 campaign purple)
- **Campaign overlay**: team'26 — indigo #1558BC / purple #803FA5 / orange (Register CTA)

---

## 04. Font Stack

- **Primary**: `Atlassian Sans` — body + display 공용
- **Code**: system mono fallback 또는 `Geist Mono` / `JetBrains Mono`
- **Weight normal / bold**: `400` / `700`
- **자주 쓰는 weight**: 400 / 500 / 600 / 700 4단

```css
:root {
  --font-sans: "Atlassian Sans", -apple-system, BlinkMacSystemFont, "Segoe UI",
               Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco,
               "Cascadia Mono", "Segoe UI Mono", "Roboto Mono", monospace;
}
body {
  font-family: var(--font-sans);
  font-weight: 400;
}
```

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| small | `14px` | 400 | 1.5 | normal |
| base | `16px` | 400 | 1.5 | normal |
| body-l | `18px` | 400 | 1.5 | normal |
| h5 | `20px` | 600 | 1.3 | normal |
| h4 | `24px` | 600 | 1.25 | `-0.01em` |
| h3 | `32px` | 600 | 1.2 | `-0.02em` |
| h2 | `40px` | 700 | 1.15 | `-0.02em` |
| h1 | `48/56/64px` | 700 | 1.1 | `-0.03em` |

> ⚠️ 큰 사이즈(H1~H2)에 음수 tracking 필수 — optical compensation이 없으면 "덜 다듬어진" 느낌이 난다.

---

## 06. Colors

### 06-1. Brand

| Token | Hex | Role |
|---|---|---|
| brand.primary | `#1868DB` | CTA, link, focus ring |
| brand.hover | 약 8% 어두움 | hover state |
| brand.tint | 약 95% light mix | soft bg, badge |

### 06-2. Neutral Ramp (light 기본)

| Step | Hex | Use |
|---|---|---|
| 0 | `#FFFFFF` | page bg |
| 50 | `#FAFAFA` | panel muted |
| 100 | `#F5F5F5` | subtle bg |
| 200 | `#E5E5E5` | border subtle |
| 300 | `#D4D4D4` | border |
| 500 | `#737373` | muted text |
| 700 | `#404040` | secondary text |
| 900 | `#171717` | primary text |

> Atlassian 회색 램프는 Tailwind neutral 계열과 유사 — 채도 0% 기준.

---

## 07. Spacing

8px baseline 시스템.

| Token | Value | Use |
|---|---|---|
| `--space-1` | 4px | hairline, icon gap |
| `--space-2` | 8px | 작은 gap |
| `--space-3` | 12px | inline group |
| `--space-4` | 16px | 기본 card padding |
| `--space-6` | 24px | section inner |
| `--space-8` | 32px | block 간격 |
| `--space-12` | 48px | 섹션 수직 padding (small) |
| `--space-16` | 64px | 섹션 수직 padding (large) |
| `--space-24` | 96px | hero padding |

---

## 08. Radius

| Token | Value | Use |
|---|---|---|
| `--radius-sm` | 4px | chip, badge |
| `--radius-md` | 8px | button 기본 |
| `--radius-lg` | 12px | card |
| `--radius-xl` | 16px | card large |
| `--radius-2xl` | 24px | hero block |
| `--radius-pill` | 9999px | pill CTA |

---

## 09. Shadows

다층 stack 방식. 단층 shadow는 피한다.

| Token | Value | Use |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | button resting |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.07)` | card |
| `--shadow-lg` | `0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)` | dropdown, modal |

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| `--duration-fast` | `150ms` | hover state |
| `--duration-base` | `200ms` | 기본 transition |
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | 기본 ease-out |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | 양방향 |

---

## 11. Layout Patterns

**Grid System**
- Content max-width: 1200-1440px
- Gutter: 24px (desktop) / 16px (mobile)
- Grid type: CSS Grid + Flexbox 하이브리드

**Hero**
- Layout: 1-column centered
- H1: 48-64px / weight 700 / tracking -0.03em
- CTA: 브랜드 primary + 보조 outline

**Section Rhythm**
- Vertical padding: 64-120px
- 섹션 구분은 배경 톤 차이 또는 얇은 border

**Cards**
- Background: #FFFFFF
- Border: 1px solid #E5E5E5
- Radius: 12-16px
- Padding: 24-32px

**Navigation**
- Type: horizontal desktop / hamburger mobile
- Position: sticky top 0 / height 64-72px
- Background: 반투명 + backdrop-filter blur

---

## 12. Responsive Behavior

| Name | Value | Note |
|---|---|---|
| Mobile | `< 640px` | 1-column, hamburger nav |
| Tablet | `≥ 768px` | 2-col hero |
| Desktop | `≥ 1024px` | full nav |
| Large | `≥ 1280px` | content max |
| XL | `≥ 1536px` | 더 큰 여백 |

Mobile-first. 터치 타겟 최소 44px. 네비게이션은 1024px 이하에서 drawer 전환.

---

## 13. Components

### 13-1. Button (primary)

```html
<button class="btn btn--primary">Get started</button>
```

```css
.btn--primary {
  background: #1868DB;
  color: #FFFFFF;
  border: 0;
  border-radius: 8px;
  padding: 0 16px;
  height: 40px;
  font-weight: 500;
  transition: transform 150ms ease-out, filter 150ms ease-out;
}
.btn--primary:hover {
  filter: brightness(1.08);
}
```

### 13-2. Card

```css
.card {
  background: #FFFFFF;
  border: 1px solid #E5E5E5;
  border-radius: 12px;
  padding: 24px;
  transition: border-color 150ms ease-out, box-shadow 150ms ease-out;
}
.card:hover {
  border-color: #1868DB40;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
```

### 13-3. Input

```css
.input {
  background: #FFFFFF;
  border: 1px solid #E5E5E5;
  border-radius: 8px;
  height: 40px;
  padding: 0 12px;
  transition: border-color 150ms, box-shadow 150ms;
}
.input:focus {
  outline: 0;
  border-color: #1868DB;
  box-shadow: 0 0 0 3px #1868DB33;
}
```

### 13-4. Nav

```css
.nav {
  position: sticky; top: 0;
  height: 64px;
  background: rgba(255,255,255,0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid #E5E5E5;
}
```

---

## 14. Content / Copy Voice

- 짧고 단호한 헤드라인 (5-8 단어)
- 서브헤드는 이점 중심, 기능명 나열 지양
- CTA 동사 (Get started, Start building, Book a demo)
- 기술적 정확함 + 친근함 중간 톤

---

## 15. Drop-in CSS

```css
:root {
  --brand: #1868DB;
  --bg: #FFFFFF;
  --fg: #171717;
  --muted: #737373;
  --border: #E5E5E5;
  --card: #FFFFFF;
  --radius: 8px;
  --radius-lg: 12px;
  --font-sans: "Atlassian Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, monospace;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: var(--font-sans);
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
  background: var(--bg);
  color: var(--fg);
}

h1 { font-size: 48px; font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; margin: 0 0 16px; }
h2 { font-size: 32px; font-weight: 600; line-height: 1.2; letter-spacing: -0.02em; margin: 0 0 12px; }
h3 { font-size: 24px; font-weight: 600; line-height: 1.25; letter-spacing: -0.01em; margin: 0 0 8px; }

.btn {
  display: inline-flex; align-items: center; justify-content: center;
  height: 40px; padding: 0 16px;
  border-radius: var(--radius); border: 0;
  font-weight: 500; font-size: 14px;
  cursor: pointer; transition: all 150ms ease-out;
}
.btn--primary { background: var(--brand); color: #FFFFFF; }
.btn--primary:hover { filter: brightness(1.08); }
.btn--outline {
  background: transparent; color: var(--fg);
  border: 1px solid var(--border);
}

.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 24px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Atlassian
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: '#1868DB' },
      },
      fontFamily: {
        sans: ['Atlassian Sans', 'system-ui', 'sans-serif'],
      },
      borderRadius: { DEFAULT: '8px', lg: '12px', xl: '16px' },
      transitionDuration: { DEFAULT: '150ms', base: '200ms' },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `--brand` | `#1868DB` |
| Background | `--bg` | `#FFFFFF` |
| Text primary | `--fg` | `#171717` |
| Text muted | `--muted` | `#737373` |
| Border | `--border` | `#E5E5E5` |

### Example Prompts

**Hero Section**
> Atlassian 스타일 히어로. 배경 `#FFFFFF`, H1 `Atlassian Sans` 56px weight 700 tracking -0.03em color `#171717`. primary CTA `#1868DB` radius 8px padding 0 20px height 44px, secondary outline border `#E5E5E5`.

**Card**
> Atlassian 스타일 카드. bg `#FFFFFF` border 1px solid `#E5E5E5` radius 12px padding 24px. hover border `#1868DB40` shadow `0 4px 6px rgba(0,0,0,0.05)`.

---

## 18. DO / DON'T

### ✅ DO
- 브랜드 색 `#1868DB`는 CTA·링크·focus ring에만 사용
- 배경은 `#FFFFFF` 또는 `#FAFAFA` (panel)
- 본문 텍스트는 `#171717`, muted는 `#737373`
- H1~H3에 음수 letter-spacing 적용 (`-0.01em ~ -0.03em`)
- Radius 4/8/12/16/24/9999px 6단 체계 유지

### ❌ DON'T
- 배경을 `#EEEEEE` 또는 중간 회색으로 두지 말 것 — 대신 `#FAFAFA` 사용
- 텍스트를 `#000000`/`black`으로 두지 말 것 — 대신 `#171717` 사용
- body에 `font-weight: 300` 사용 금지 — Atlassian은 `400`이 기본
- 브랜드 색 `#1868DB`를 긴 문단 배경에 쓰지 말 것
- Radius `20px`, `30px` 등 외부 값 금지 — 토큰 scale만 사용
- 단층 shadow `0 4px 12px rgba(0,0,0,0.1)` 금지 — 2-layer stack 사용
- transition duration `400ms+` 금지 — 150-200ms 유지
