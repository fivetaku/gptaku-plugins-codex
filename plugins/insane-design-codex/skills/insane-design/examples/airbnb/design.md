---
slug: airbnb
service_name: Airbnb
site_url: https://airbnb.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#FF385C"
primary_font: Airbnb Cereal VF
font_weight_normal: 400
token_prefix: --palette-*
---

# DESIGN.md — Airbnb (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Airbnb처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'Airbnb Cereal VF', 'Circular', -apple-system, BlinkMacSystemFont, Roboto, 'Helvetica Neue', sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #222222; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FF385C; }
```

**절대 하지 말아야 할 것 하나**: 폰트 weight를 `font-weight: 600`으로 통일하는 것. Airbnb는 weight 체계가 세밀하다 — 본문 400(400), 강조 500, 버튼 600, 제목 800(bold)까지 층위가 명확하다. 전부 600으로 뭉개면 Airbnb 특유의 위계가 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://airbnb.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | Next.js SSR |
| CSS files | Airbnb Cereal VF 셀프 호스트 + CSS 변수 |
| Token prefix | `--palette-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (React)
- **Design system**: 자체 DLS — prefix `--palette-*`
- **CSS architecture**: 2-tier 팔레트 + semantic
  ```
  palette   (--palette-bg-primary, --palette-text-primary)  semantic role
  brand     (--palette-bg-primary-core, --palette-bg-primary-luxe)
  ```
- **Class naming**: React + CSS Modules 혼합
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: `Airbnb Cereal VF` 셀프 호스트 (가변 폰트, `Circular`이 fallback)
- **Canonical anchor**: `#FF385C` — `--palette-bg-primary-core`

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Airbnb Cereal VF` (Airbnb 전용 가변 폰트)
- **Code font**: `monospace`
- **Weight normal / bold**: `400` / `bold`

```css
:root {
  --font-family: 'Airbnb Cereal VF', 'Circular', -apple-system, BlinkMacSystemFont, Roboto, 'Helvetica Neue', sans-serif;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 800;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스**: Airbnb Cereal VF는 Airbnb 전용. `Circular`(유료) 또는 `Nunito`(무료)가 근접한 대체재.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| text-micro | ~0.6875rem | 400 | 1.4545 | 0.3px |
| text-small | ~0.875rem | 400 | 1.5 | 0.2px |
| text-regular | 1rem | 400 | 1.4667 | 0.1px |
| text-large | ~1.125rem | 400 | 1.4444 | -0.2px |
| title-4 | ~1.25rem | 600 | 1.25 | -0.4px |
| title-3 | ~1.5rem | 600 | 1.25 | -0.4px |
| title-2 | ~1.875rem | 800 | 1.2667 | -0.6px |
| title-1 | ~2.25rem | 800 | 1.3333 | -0.8px |

> ⚠️ Airbnb 타이포 scale은 CSS에 `text-large`, `text-micro`, `title-1~4`로 정의돼 있다. heading으로 갈수록 letter-spacing이 음수로 커진다 — `-0.4px`(title-3) → `-0.8px`(title-1). 이 negative tracking이 Airbnb 타이포의 핵심이다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Airbnb Core + Variants)

| Token | Hex |
|---|---|
| `--palette-bg-primary-core` | `#FF385C` ⭐ **canonical** |
| `--palette-bg-primary-plus` | `#92174D` |
| `--palette-bg-primary-luxe` | `#460479` |
| error-hover | `#B32505` |
| error | `#C13515` |

### 06-3. Neutral Ramp

| Step | Hex |
|---|---|
| bg | `#FFFFFF` |
| bg-secondary | `#F7F7F7` |
| border | `#DDDDDD` |
| fg | `#222222` |
| fg-muted | `#717171` |
| inverse | `#000000` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--palette-bg-primary` | `#FFFFFF` | 기본 배경 |
| `--palette-bg-primary-core` | `#FF385C` | 브랜드 CTA |
| `--palette-bg-primary-inverse` | `#222222` | 다크 버튼 |
| `--palette-text-primary` | `#222222` | 본문 텍스트 |
| `--palette-bg-primary-error` | `#FFF8F6` | 에러 배경 |
| `--palette-bg-primary-inverse-error` | `#C13515` | 에러 버튼 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | high | 배경 |
| 2 | `#222222` | high | 텍스트, 다크 버튼 |
| 3 | `#FF385C` | medium | 브랜드 CTA |
| 4 | `#F7F7F7` | medium | 보조 배경 |
| 5 | `#DDDDDD` | medium | 테두리 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| letter-tight | -0.8px | title-1 letter-spacing |
| letter-sm | -0.4px | title-3 letter-spacing |

**주요 alias**:
- title-1 → line-height 1.3333, letter-spacing -0.8px

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn | 8px | 일반 버튼 |
| card | 12px | 숙박 카드 |
| pill | 999px | 필터 배지 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Primary (Brand)

```html
<button class="btn-primary" type="button">예약하기</button>
```

| Spec | Value |
|---|---|
| background | `#FF385C` |
| color | `#FFFFFF` |
| font-weight | 600 |
| border-radius | 8px |
| hover bg | `#E31C5F` |

### Button — Inverse (Dark)

```html
<button class="btn-inverse" type="button">더 보기</button>
```

| Spec | Value |
|---|---|
| background | `#222222` |
| color | `#FFFFFF` |
| hover bg | `#000000` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 여행·경험 중심, 감성적 | "어디서든 소속감을" |
| Primary CTA | 행동 유도, 직접적 | "예약하기" |
| Secondary CTA | 탐색 유도 | "자세히 알아보기" |
| Tone | 따뜻하고 포용적. 어디서나 편안함 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Airbnb — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: 'Airbnb Cereal VF', 'Circular', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 800;

  /* Brand */
  --palette-bg-primary-core: #FF385C;   /* ← canonical */
  --palette-bg-primary-plus: #92174D;
  --palette-bg-primary-luxe: #460479;

  /* Surfaces */
  --palette-bg-primary: #FFFFFF;
  --palette-bg-secondary: #F7F7F7;
  --palette-text-primary: #222222;
  --palette-text-muted: #717171;
  --palette-border: #DDDDDD;
  --palette-bg-primary-inverse: #222222;

  /* Key spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-card: 12px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO
- 브랜드 CTA 버튼은 `#FF385C`(--palette-bg-primary-core)을 써라.
- 텍스트는 `#222222`를 써라 — 순흑이 아닌 Airbnb의 따뜻한 dark gray다.
- weight 층위를 지켜라 — 400(본문), 500(강조), 600(버튼), 800(제목).
- 큰 제목에 negative letter-spacing을 써라 — `-0.4px`부터 `-0.8px`까지.
- Airbnb Cereal VF가 없으면 `Circular`를 fallback으로 지정하라.

### DON'T
- `font-weight: 600`으로 모든 텍스트를 통일하지 마라 — 층위가 무너진다.
- 배경을 `#F7F7F7`로 두지 마라 — 그건 hover/secondary 배경이고, 기본은 `#FFFFFF`다.
- `#FF0000`이나 `#FF4466`을 brand red로 쓰지 마라 — 정확히 `#FF385C`를 써야 한다.
- Luxe variant(`#460479`)를 일반 CTA에 쓰지 마라 — Airbnb Luxe 서비스 전용이다.
- 버튼 radius를 0으로 두지 마라 — Airbnb 버튼은 8px이다.
