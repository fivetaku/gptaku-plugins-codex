---
slug: krafton
service_name: Krafton
site_url: https://www.krafton.com/
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#F9423A"
primary_font: system-ui
font_weight_normal: 400
token_prefix: --wp--preset--color--primary
---

# DESIGN.md — Krafton (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Krafton처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #F9423A; }
```

**절대 하지 말아야 할 것 하나**: `#0073A8` (WordPress preset primary)를 Krafton 브랜드 색으로 사용하는 것. `#0073A8`은 WordPress Gutenberg의 기본 preset color이며 실제 Krafton 브랜드와 무관하다. SVG 패턴에서 7회 등장하는 `#F9423A`가 실제 Krafton 레드 브랜드 컬러다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.krafton.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | WordPress (자동 생성 인라인 CSS) |
| Token prefix | `--wp--preset--color--primary` (WordPress preset) |
| Method | CSS hex frequency 분석 · 커스텀 프로퍼티 파싱 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: WordPress (블록 에디터 Gutenberg 사용)
- **Design system**: WordPress 블록 테마 + 크래프톤 커스텀
- **CSS architecture**: WordPress 자동 생성 CSS
  ```
  /*# sourceURL=wp-img-auto-sizes-contain-inline-css */
  --wp--preset--color--* (WordPress 프리셋 토큰)
  .wp-block-button__link (Gutenberg 블록 버튼)
  .wp-block-file__button (파일 다운로드 버튼)
  ```
- **Class naming**: WordPress 블록 (`wp-block-button__link`, `wp-block-file__button`)
- **Default theme**: dark (bg = `#000000`)
- **Font loading**: 시스템 폰트 (전용 폰트 CSS 미확인)
- **Canonical anchor**: `#F9423A` — Krafton 레드, SVG 패턴 7회 등장

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: 시스템 폰트 (CSS에서 전용 폰트 미확인)
- **Code font**: N/A
- **Weight normal / bold**: `400` / N/A

```css
:root {
  --krafton-font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --krafton-font-weight-normal: 400;
}
body {
  font-family: var(--krafton-font-family);
  font-weight: var(--krafton-font-weight-normal);
}
```

> CSS 번들에서 전용 폰트 패밀리 미확인. WordPress 테마 기본 시스템 폰트 사용 추정.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS에서 타이포 스케일 토큰 확인 불가. WordPress 기본값 사용.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | N/A | 400 | N/A | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-red | `#F9423A` |
| brand-teal | `#0073A8` |
| brand-teal-dark | `#005075` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| black | `#000000` | — |
| near-black | `#111111` | — |
| dark-btn | `#32373C` | — |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| wp-green | preset | `#00D084` |
| wp-blue | preset | `#0693E3` |
| wp-purple | preset | `#9B51E0` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --wp--preset--color--primary | `#0073A8` | WordPress 프리셋 (브랜드 아님) |
| brand-red | `#F9423A` | Krafton 브랜드 레드 |
| btn-default-bg | `#32373C` | WordPress 기본 버튼 배경 |
| btn-default-color | `#FFFFFF` | WordPress 기본 버튼 텍스트 |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — CSS에서 스페이싱 토큰 확인 불가

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| wp-block-button | 9999px | Gutenberg 버튼 기본 (pill shape) |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Block Button (`.wp-block-button__link`)

```html
<div class="wp-block-button">
  <a class="wp-block-button__link">게임 보기</a>
</div>
```

| 속성 | 값 |
|---|---|
| color | `#FFFFFF` |
| background-color | `#32373C` |
| border-radius | 9999px |
| box-shadow | none |
| text-decoration | none |

### File Download Button (`.wp-block-file__button`)

```html
<a class="wp-block-file__button" href="#">다운로드</a>
```

| 속성 | 값 |
|---|---|
| background | `#32373C` |
| color | `#FFFFFF` |
| text-decoration | none |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Krafton — copy into your root stylesheet */
:root {
  /* Fonts */
  --krafton-font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --krafton-font-weight-normal: 400;

  /* Brand */
  --krafton-color-brand: #F9423A;
  --krafton-color-teal: #0073A8;
  --krafton-color-teal-dark: #005075;

  /* Surfaces */
  --krafton-bg-page: #000000;
  --krafton-text: #FFFFFF;

  /* Button */
  --krafton-btn-bg: #32373C;
  --krafton-btn-radius: 9999px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 배경은 `#000000` 순수 검정 (다크 테마가 기본)
- Krafton 브랜드 레드는 `#F9423A`
- WordPress 블록 버튼은 pill shape (border-radius: 9999px)
- 텍스트는 `#FFFFFF` 순수 흰색

### ❌ DON'T
- `#0073A8`을 Krafton 브랜드 색으로 사용 — WordPress 프리셋 기본값
- `#32373C` 버튼 배경을 Krafton 브랜드 색으로 혼동 — WordPress 기본 버튼색
- 라이트 테마 기본으로 설정 — Krafton 웹은 다크 테마가 기본
