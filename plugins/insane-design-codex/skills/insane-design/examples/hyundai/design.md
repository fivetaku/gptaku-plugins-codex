---
slug: hyundai
service_name: Hyundai
site_url: https://www.hyundai.com/kr/ko/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#007FA8"
primary_font: HyundaiSansTextKR
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Hyundai (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Hyundai처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "HyundaiSansTextKR", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #303133; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #007FA8; }
```

**절대 하지 말아야 할 것 하나**: Element UI(`el-*`) 기본 파랑(`#409EFF`)을 현대 브랜드 색으로 착각하는 것. `#409EFF`는 Element UI 컴포넌트 라이브러리의 기본값이고, 실제 현대 브랜드 액티브 색은 `#007FA8`이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.hyundai.com/kr/ko/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다수 외부 CSS (Element UI 포함) |
| Token prefix | N/A (Element UI 컴포넌트 기반) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Vue.js + Element UI (CSS 클래스 `el-*` 패턴으로 확인)
- **Design system**: Element UI 기반 커스텀 — `el-*` prefix
- **CSS architecture**: Element UI 컴포넌트 CSS + 현대 커스텀 오버라이드
  ```
  element-ui global (--el-color-primary 등)
  hyundai-custom (브랜드 오버라이드)
  page-specific
  ```
- **Class naming**: Element UI 패턴 (`el-pagination`, `el-dialog`, `el-radio-button`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스팅 (`HyundaiSansTextKR`, `HyundaiSansHeadKR`)
- **Canonical anchor**: `#007FA8` — 페이지네이션 액티브 색, 현대 teal 브랜드

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `HyundaiSansHeadKR` (현대 전용 헤드라인용)
- **Body font**: `HyundaiSansTextKR` (현대 전용 본문용)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family-head: "HyundaiSansHeadKR", sans-serif;
  --font-family-text: "HyundaiSansTextKR", sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;
}
body {
  font-family: var(--font-family-text);
  font-weight: var(--font-weight-normal);
}
```

> 한글 전용 폰트로 한국 현대 사이트에서만 사용. 대체재: `Noto Sans KR` (weight 400/700).

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS에 명시적 타이포 스케일 토큰이 없음. Element UI 기본값과 현대 커스텀이 혼재.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | 14px | 400 | 1.5 | N/A |
| heading | N/A | 700 | N/A | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-active | `#007FA8` |
| brand-hover | N/A |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| bg-white | `#FFFFFF` | — |
| bg-muted | `#F4F4F5` | — |
| text-primary | `#303133` | — |
| text-secondary | `#606266` | — |
| text-placeholder | `#909399` | — |
| text-disabled | `#C0C4CC` | — |
| border-base | `#DCDFE6` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| el-color-primary | `#409EFF` | Element UI 기본값 (현대 브랜드 아님) |
| hyundai-active | `#007FA8` | 현대 브랜드 액티브 색 |
| el-color-disabled | `#C0C4CC` | 비활성 |
| el-border | `#DCDFE6` | 기본 테두리 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| pager-item-margin | 5px | 페이지네이션 아이템 간격 |
| pager-item-min-w | 30px | 페이지네이션 최소 너비 |

**주요 alias**:
- Element UI 기본 5px 그리드 기반

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| el-pager | 4px | Element UI 페이지네이션 |
| el-dialog | 4px | 다이얼로그 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Pagination — Active (`.el-pager li.active`)

```html
<ul class="el-pager">
  <li class="active">1</li>
</ul>
```

| 속성 | 값 |
|---|---|
| color | `#007FA8` |
| cursor | default |

### Radio Button — Checked (`.el-radio-button__orig-radio:checked + .el-radio-button__inner`)

```html
<div class="el-radio-button">
  <input class="el-radio-button__orig-radio" type="radio" checked>
  <span class="el-radio-button__inner">선택</span>
</div>
```

| 속성 | 값 |
|---|---|
| color | `#FFFFFF` |
| background-color | `#409EFF` |
| border-color | `#409EFF` |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Hyundai — copy into your root stylesheet */
:root {
  /* Fonts */
  --hyundai-font-head: "HyundaiSansHeadKR", sans-serif;
  --hyundai-font-text: "HyundaiSansTextKR", sans-serif;
  --hyundai-font-weight-normal: 400;
  --hyundai-font-weight-bold: 700;

  /* Brand */
  --hyundai-color-brand: #007FA8;
  --hyundai-color-el-primary: #409EFF;

  /* Surfaces */
  --hyundai-bg-page: #FFFFFF;
  --hyundai-bg-muted: #F4F4F5;
  --hyundai-text: #303133;
  --hyundai-text-muted: #909399;

  /* Borders */
  --hyundai-border: #DCDFE6;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 브랜드 액티브 색으로 `#007FA8` 사용
- 헤드라인에 `HyundaiSansHeadKR`, 본문에 `HyundaiSansTextKR` 구분 사용
- Element UI 기반 컴포넌트 패턴 유지 (`el-*` 클래스)
- 중립 텍스트는 `#303133` (Element UI 기본 텍스트색)

### ❌ DON'T
- `#409EFF`를 현대 브랜드 색으로 사용 — Element UI 기본값이며 현대 브랜드 아님
- 헤드라인 폰트와 본문 폰트를 같은 폰트로 통일 — 현대는 Head/Text 명확히 구분
- 현대 웹 컴포넌트에서 라운드 버튼 남발 — 현대 스타일은 절제된 각도
