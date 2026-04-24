---
slug: porsche
service_name: Porsche
site_url: https://porsche.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#CC0000"
primary_font: Porsche Next
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Porsche (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Porsche처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Porsche Next", "Arial Narrow", Arial, "Heiti SC", SimHei, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #0E0E12; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #CC0000; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순흑 `#000000`으로 두는 것. Porsche의 다크 배경은 `#0E0E12` — 아주 미묘하게 파란 기운이 도는 거의 검정이다. 순흑과 `#0E0E12`는 시각적으로 다르며, 이 미묘한 차이가 프리미엄 feel을 만든다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://porsche.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | N/A |
| Token prefix | N/A |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 플랫폼, React 추정)
- **Design system**: Porsche Design System (PDS) 내부
- **CSS architecture**: BEM-ish + CSS Module 혼합 (`.DatabaseButton__wrapper__0808c` 패턴)
- **Class naming**: CSS Modules + hash suffix (`.ComponentName__element__hash`)
- **Default theme**: dark (bg = `#0E0E12`)
- **Font loading**: 자체 호스트 (`Porsche Next`)
- **Canonical anchor**: `#CC0000` — Porsche 브랜드 레드

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Porsche Next` (Porsche AG 독점)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --porsche-font-family: "Porsche Next", "Arial Narrow", Arial, "Heiti SC", SimHei, sans-serif;
  --porsche-font-weight-normal: 400;
  --porsche-font-weight-bold: 700;
}
body {
  font-family: var(--porsche-font-family);
  font-weight: var(--porsche-font-weight-normal);
}
```

> **라이선스 주의**: `Porsche Next`는 Porsche AG 독점. 외부 프로젝트에서는 `Oswald` 또는 `Bebas Neue`가 narrow sans로 유사한 대체재.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Porsche Red)

| Token | Hex |
|---|---|
| 브랜드 레드 | `#CC0000` |

### 06-2. Brand Dark Variant (UI Dark Backgrounds)

| Token | Hex |
|---|---|
| 다크 배경 (primary) | `#0E0E12` |
| 다크 배경 (hover) | `#1A1A24` |
| 서브 다크 배경 | `#0E1418` |

### 06-3. Neutral Ramp

| Step | Hex | Count |
|---|---|---|
| 흰 텍스트 / 테두리 | `#FFFFFF` | 30회 |
| 다크 배경 | `#0E0E12` | 20회 |
| 순흑 | `#000000` | 2회 |
| hover 다크 배경 | `#1A1A24` | 2회 |
| 중간 회색 | `#555555` | 2회 |
| 밝은 회색 | `#EEEEEE` | 2회 |
| 연한 회청 | `#EEEFF2` | 2회 |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Porsche Red | brand | `#CC0000` |
| Dark surface | primary | `#0E0E12` |
| Dark surface hover | hover | `#1A1A24` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| 배경 primary (다크) | `#0E0E12` | body background (dark theme) |
| 테두리 / 텍스트 on dark | `#FFFFFF` | 흰 텍스트, 테두리 |
| 버튼 hover bg | `#1A1A24` | dark button hover 상태 |
| 브랜드 레드 | `#CC0000` | 포인트 컬러 |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음. `.DatabaseButton__wrapper__0808c`에서 `padding: 6px 10px` 관찰.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| 버튼 | `8px` | `.DatabaseButton__wrapper__0808c` |

---

## 09. Shadows
<!-- SOURCE: auto -->

> N/A — shadow 토큰이 CSS에서 추출되지 않음.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### CTA Button (Dark theme)

```html
<div class="DatabaseButton__wrapper__0808c">
  <button type="button">Configure</button>
</div>
```

| 속성 | 값 |
|---|---|
| background-color | `#0E0E12` |
| border | `1px solid #FFFFFF` |
| border-radius | `8px` |
| padding | `6px 10px` |
| color | `#FFFFFF` |
| width | `185px` |

### Dev Tools Toggle

```html
<button class="DevToolsSidebar__toggleButton__14360">
  <!-- icon -->
</button>
```

| 속성 | 값 |
|---|---|
| background | `#0E0E12` |
| border | `1px solid rgba(255,255,255,.6)` |
| color | `#FFFFFF` |
| hover background | `#1A1A24` |
| hover border-color | `#FFFFFF` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 모델명 + 감성 한 줄 | "The new 911." |
| Primary CTA | 행동 유도, 간결 | "Configure" / "Discover" |
| Secondary CTA | 탐색 유도 | "Find a Dealer" |
| Subheading | 퍼포먼스 수치 | "0–100 km/h in 2.7 s" |
| Tone | 스포티하고 정밀한 독일 감성 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Porsche — copy into your root stylesheet */
:root {
  /* Fonts */
  --porsche-font-family: "Porsche Next", "Arial Narrow", Arial, sans-serif;
  --porsche-font-weight-normal: 400;
  --porsche-font-weight-bold: 700;

  /* Brand */
  --porsche-color-brand-red: #CC0000;

  /* Surfaces (dark theme) */
  --porsche-bg-page: #0E0E12;
  --porsche-bg-hover: #1A1A24;
  --porsche-bg-light: #EEEFF2;
  --porsche-text: #FFFFFF;
  --porsche-text-muted: #555555;

  /* Key spacing observed */
  --porsche-space-btn: 6px 10px;
  --porsche-radius-btn: 8px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Porsche
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          red: '#CC0000',
        },
        surface: {
          dark: '#0E0E12',
          'dark-hover': '#1A1A24',
          light: '#EEEFF2',
        },
        neutral: {
          white: '#FFFFFF',
          mid: '#555555',
          light: '#EEEEEE',
        },
      },
      fontFamily: {
        sans: ['"Porsche Next"', '"Arial Narrow"', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold: '700',
      },
      borderRadius: {
        btn: '8px',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 다크 배경에 `#0E0E12` 사용 (순흑 아님)
- 버튼 테두리에 `1px solid #FFFFFF` 사용
- hover 상태는 `#1A1A24`로 미묘하게 밝게
- Porsche Red `#CC0000`은 포인트 컬러로만 절제 사용
- 버튼 radius `8px` 유지

### ❌ DON'T
- 다크 배경으로 순흑 `#000000` 쓰지 말 것 — `#0E0E12`
- 배경 전체를 빨간색으로 채우지 말 것
- 밝은 테마 배경 쓰지 말 것 — Porsche 마케팅 사이트는 다크 테마 기본
- font-weight 100이나 200 쓰지 말 것 — 400이 기준
