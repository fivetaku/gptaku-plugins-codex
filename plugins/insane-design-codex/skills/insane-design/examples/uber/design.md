---
slug: uber
service_name: Uber
site_url: https://uber.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#276EF1"
primary_font: UberMoveText
font_weight_normal: 500
token_prefix: N/A
---

# DESIGN.md — Uber (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Uber처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: UberMoveText, system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 500;   /* ⚠️ 400 아님. Uber body는 500. */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #276EF1; }
```

**절대 하지 말아야 할 것 하나**: `UberMoveText`와 `UberMove`를 혼용하는 것. `UberMoveText`(count: 53)는 본문용, `UberMove`(count: 34)는 display/heading용이다. 둘을 구분 없이 쓰면 타이포 위계가 무너진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://uber.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | React 기반 SPA |
| CSS files | UberMove 폰트 셀프 호스트 + Base Web CSS |
| Token prefix | N/A (CSS 커스텀 프로퍼티 없음) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React + Base Web (Uber 오픈소스 UI 프레임워크)
- **Design system**: Base Design System — prefix 없음(직접 hex)
- **CSS architecture**: Base Web 인라인 스타일 + 셀프 호스트 폰트
  ```
  직접 hex (no CSS custom property)
  Base Web 컴포넌트 스타일 (inline)
  ```
- **Class naming**: 해시 기반 CSS-in-JS
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: UberMove, UberMoveText 셀프 호스트 + 서브셋 (Book, Medium, Narrow 등)
- **Canonical anchor**: `#276EF1` — frequency_candidates에서 40회 확인된 Uber blue

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `UberMove` (Uber 전용, 헤딩용)
- **Body font**: `UberMoveText` (Uber 전용, 본문용)
- **Code font**: N/A
- **Weight normal / bold**: `500` / `700`

```css
:root {
  --font-family-text: UberMoveText, system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-family-display: UberMove, UberMoveText, system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-weight-normal: 500;
  --font-weight-bold: 700;
}
body {
  font-family: var(--font-family-text);
  font-weight: var(--font-weight-normal);
}
h1, h2, h3 {
  font-family: var(--font-family-display);
}
```

> **참고**: UberMove/UberMoveText는 Dalton Maag이 제작한 Uber 전용 폰트. 재배포 불가. `Aktiv Grotesk`가 근접한 대체재(유료), 무료 대체로는 `Inter`.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | 1rem | 500 | 1.5 | 0 |
| heading-sm | 1.25rem | 700 | 1.3 | 0 |
| heading | 1.5rem | 700 | 1.25 | 0 |
| display | 2.5rem | 700 | 1.1 | -0.01em |
| hero | 3.5rem | 700 | 1.05 | -0.02em |

> ⚠️ `weight: 500`이 Uber body의 기본이다. 400이 아님. CSS에서 weight 500(count: 39)이 400(count: 11)보다 3.5배 더 많이 쓰인다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Uber Blue)

| Token | Hex |
|---|---|
| brand | `#276EF1` ⭐ **canonical** |
| brand-accent | `#ADDEC9` (녹색 보조) |

### 06-3. Neutral Ramp

| Step | Hex |
|---|---|
| bg | `#FFFFFF` |
| bg-secondary | `#F3F3F3` |
| bg-tertiary | `#E8E8E8` |
| border | `#E2E2E2` |
| border-str | `#CBCBCB` |
| fg-muted-3 | `#AFAFAF` |
| fg-muted-2 | `#A6A6A6` |
| fg-muted | `#757575` |
| fg-subtle | `#727272` |
| fg-mid | `#5E5E5E` |
| fg-dark | `#4B4B4B` |
| fg | `#000000` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| brand | `#276EF1` | CTA 버튼, 링크 |
| accent-green | `#ADDEC9` | 드라이버/긍정 상태 |
| fg | `#000000` | 본문 텍스트 |
| bg-secondary | `#F3F3F3` | 카드, 패널 배경 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#E8E8E8` | 504 | 구분선, 테두리 |
| 2 | `#000000` | 126 | 텍스트 |
| 3 | `#FFFFFF` | 121 | 배경 |
| 4 | `#F3F3F3` | 104 | 보조 배경 |
| 5 | `#276EF1` | 40 | 브랜드 블루 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| xs | 4px | 아이콘 간격 |
| sm | 8px | 소형 컴포넌트 |
| md | 16px | 기본 패딩 |
| lg | 24px | 섹션 내 gap |
| xl | 48px | 섹션 간격 |

**주요 alias**:
- Base Web 4px 배수 그리드 기반

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn | 8px | 버튼 |
| card | 8px | 카드 |
| pill | 999px | 배지, 태그 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Primary

```html
<button class="btn-primary" type="button">지금 예약</button>
```

| Spec | Value |
|---|---|
| background | `#276EF1` |
| color | `#FFFFFF` |
| font-weight | 700 |
| font-family | `UberMove` |
| border-radius | 8px |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Uber — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family-text: UberMoveText, system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-family-display: UberMove, UberMoveText, system-ui, sans-serif;
  --font-weight-normal: 500;
  --font-weight-bold: 700;

  /* Brand */
  --brand: #276EF1;   /* ← canonical Uber blue */
  --brand-accent: #ADDEC9;

  /* Surfaces */
  --bg-page: #FFFFFF;
  --bg-secondary: #F3F3F3;
  --bg-tertiary: #E8E8E8;
  --text: #000000;
  --text-muted: #757575;
  --border: #E2E2E2;

  /* Key spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-pill: 999px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO
- `UberMoveText`는 본문에, `UberMove`는 heading에 써라 — 둘을 구분하라.
- 본문 weight는 `500`을 써라 — Uber는 400이 아닌 500이 기본이다.
- 브랜드 블루는 `#276EF1`을 써라.
- 배경 계층을 지켜라 — `#FFFFFF`(main), `#F3F3F3`(secondary), `#E8E8E8`(tertiary).
- 테두리는 `#E8E8E8`(soft) 또는 `#E2E2E2`(standard)를 써라.

### DON'T
- `UberMoveText`를 heading에 쓰지 마라 — heading은 `UberMove`다.
- `font-weight: 400`을 기본으로 두지 마라 — Uber는 500이다.
- `#000000` 순흑을 배경으로 쓰지 마라 — Uber는 라이트 테마다.
- `#ADDEC9`(녹색)를 CTA에 쓰지 마라 — 드라이버 상태 표시 accent다.
- 배경에 `#E8E8E8`을 쓰지 마라 — 그건 테두리/구분선 색이다.
