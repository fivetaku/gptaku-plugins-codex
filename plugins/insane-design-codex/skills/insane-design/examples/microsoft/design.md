---
slug: microsoft
service_name: Microsoft
site_url: https://microsoft.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0078D4"
primary_font: Segoe UI
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Microsoft (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Microsoft처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #242424; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0078D4; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 블루로 `#1BA1E2`(Windows 8 시대 구버전)를 쓰는 것. Microsoft는 2019년 이후 Fluent Design으로 전환하며 `#0078D4`를 canonical CTA blue로 고정했다. 구버전 파란색을 쓰면 즉시 구식처럼 보인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://microsoft.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 200,128 bytes (레거시 서버 렌더링) |
| CSS files | 외부 CDN (mwf-west-european-default.min.css 등) |
| Token prefix | N/A (CSS 커스텀 프로퍼티 없음 — 레거시 구조) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · 레거시 페이지 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Microsoft 자체 레거시 CMS (UHF — Universal Header Framework)
- **Design system**: Fluent Design System 2 (Fluent 2) — 마케팅 사이트는 Microsoft Web Framework (MWF) 사용
- **CSS architecture**: 플랫 클래스 (레거시 스타일시트, 토큰 없음)
  ```
  MWF utility classes  (c-uhfh-alert, f-information, theme-light)
  UHF classes          (uhf, uhfc-universal-context)
  ```
- **Class naming**: MWF 유틸리티 (`c-`, `f-`, `x-`, `theme-*`)
- **Default theme**: light
- **Font loading**: CDN 또는 Windows 시스템 폰트 (`Segoe UI` — Windows 기본 탑재)
- **Canonical anchor**: `#0078D4` — Fluent 2 primary blue

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Segoe UI Variable` (Windows 11+ 기본 탑재, 가변 폰트)
- **Body font**: `Segoe UI` (Windows 탑재)
- **Code font**: `Cascadia Code, Consolas, monospace`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --font-family: "Segoe UI Variable", "Segoe UI", system-ui, -apple-system, sans-serif;
  --font-family-code: "Cascadia Code", Consolas, monospace;
  --font-weight-normal: 400;
  --font-weight-bold: 600;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **참고**: Segoe UI Variable은 Windows 11에 탑재. Windows 10 이하는 Segoe UI(고정 폰트)로 fallback. macOS/Linux는 system-ui로 fallback.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| caption | 0.75rem | 400 | 1.33 | 0 |
| body-sm | 0.875rem | 400 | 1.43 | 0 |
| body | 1rem | 400 | 1.5 | 0 |
| subtitle | 1rem | 600 | 1.5 | 0 |
| title-sm | 1.25rem | 600 | 1.4 | -0.005em |
| title | 1.5rem | 600 | 1.33 | -0.01em |
| large-title | 2rem | 600 | 1.25 | -0.015em |
| display | 2.5rem | 600 | 1.2 | -0.02em |

> ⚠️ Fluent 2 타이포 스케일. heading/title 계열은 weight 600이 기본. `Segoe UI Variable`의 가변 폰트 특성 덕분에 400~700 범위가 자연스럽게 렌더된다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Fluent 2 Blue)

| Token | Hex |
|---|---|
| brand-10 | `#EFF6FC` |
| brand-20 | `#DEECF9` |
| brand-30 | `#C7E0F4` |
| brand-40 | `#71AFE5` |
| brand-50 | `#2B88D8` |
| brand-60 | `#0078D4` ⭐ **canonical** |
| brand-70 | `#106EBE` |
| brand-80 | `#005A9E` |
| brand-90 | `#004578` |

### 06-3. Neutral Ramp

| Step | Hex |
|---|---|
| bg | `#FFFFFF` |
| bg-secondary | `#F9F9F9` |
| fg-subtle | `#707070` |
| fg | `#242424` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| primary | `#0078D4` | CTA 버튼, 링크, focus ring |
| text | `#242424` | 본문 텍스트 |
| text-muted | `#707070` | 부가 설명 |
| bg | `#FFFFFF` | 페이지 배경 |
| bg-secondary | `#F9F9F9` | 카드, 섹션 배경 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-2xs | 4px | 아이콘 간격 |
| space-xs | 8px | 소형 컴포넌트 내부 |
| space-sm | 12px | 버튼 패딩 수직 |
| space-md | 16px | 일반 패딩 |
| space-lg | 24px | 섹션 내 간격 |
| space-xl | 48px | 섹션 간격 |

**주요 alias**:
- Fluent 2 → 4px 배수 기반 (Fluent Grid)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-sm | 2px | 소형 (chip) |
| radius-md | 4px | 버튼, 카드 |
| radius-lg | 8px | 대형 카드, 패널 |
| radius-xl | 12px | 모달, 다이얼로그 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Primary (Fluent)

```html
<button class="ms-Button ms-Button--primary" type="button">
  지금 시작
</button>
```

| Spec | Value |
|---|---|
| background | `#0078D4` |
| color | `#FFFFFF` |
| font-weight | 600 |
| border-radius | 4px |
| padding | 8px 20px |
| hover bg | `#106EBE` |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Microsoft — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Segoe UI Variable", "Segoe UI", system-ui, -apple-system, sans-serif;
  --font-family-code: "Cascadia Code", Consolas, monospace;
  --font-weight-normal: 400;
  --font-weight-bold: 600;

  /* Brand (Fluent 2 blue ramp) */
  --brand-10: #EFF6FC;
  --brand-30: #C7E0F4;
  --brand-50: #2B88D8;
  --brand-60: #0078D4;   /* ← canonical */
  --brand-70: #106EBE;
  --brand-90: #004578;

  /* Surfaces */
  --bg-page: #FFFFFF;
  --bg-secondary: #F9F9F9;
  --text: #242424;
  --text-muted: #707070;

  /* Key spacing */
  --space-sm: 12px;
  --space-md: 16px;
  --space-lg: 24px;

  /* Radius */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO
- 브랜드 블루는 `#0078D4`(Fluent 2 brand-60)을 써라.
- 텍스트는 `#242424`를 써라 — 순흑이 아닌 Fluent의 dark gray다.
- 버튼 weight는 600을 써라 — Fluent 2 기준이다.
- border-radius 4px을 기본으로 써라 — Fluent의 기본 radius다.
- 4px 배수 그리드를 지켜라.

### DON'T
- `#1BA1E2`(Windows 8 구버전 파랑)를 쓰지 마라 — Fluent 2는 `#0078D4`로 전환됐다.
- `Arial`을 기본 폰트로 두지 마라 — Windows에서는 `Segoe UI`가 로드된다.
- 버튼 radius를 0으로 두지 마라 — Fluent는 4px이 기본이다.
- 무거운 `font-weight: 700`을 heading에 쓰지 마라 — Fluent heading은 600이다.
- 배경을 진한 회색으로 만들지 마라 — Microsoft 마케팅 사이트 기반은 `#FFFFFF`다.
