---
slug: mercedes-benz
service_name: Mercedes-Benz
site_url: https://mercedes-benz.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#9F9F9F"
primary_font: MBCorpoSText
font_weight_normal: 100
token_prefix: N/A
---

# DESIGN.md — Mercedes-Benz (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Mercedes-Benz처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight 100 */
body {
  font-family: "MBCorpoSText", "MBCorpoAText", "Helvetica Neue", Arial, sans-serif;
  font-weight: 100;   /* ⚠️ 400 아님. Mercedes는 body가 100. */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #9F9F9F; }
```

**절대 하지 말아야 할 것 하나**: body를 `font-weight: 400`으로 두는 것. Mercedes-Benz의 정체성은 **weight 100** (Ultra Light)에 있다. CSS 전체에서 font-weight 100이 23회 등장하며, 이 초경량 타이포그래피가 럭셔리 브랜드의 핵심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://mercedes-benz.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | N/A |
| Token prefix | N/A — 커스텀 프로퍼티 시스템 미감지 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 플랫폼, Web Components 사용)
- **Design system**: Mercedes-Benz 내부 디자인 시스템
- **CSS architecture**: Web Components 기반 (`brandhub-search-link-list-item` 등)
- **Class naming**: N/A (Web Components 커스텀 엘리먼트)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스트 (MBCorpoSText, MBCorpoAText)
- **Canonical anchor**: `#9F9F9F` — 가장 빈도 높은 비중립 컬러 (12회)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `MBCorpoAText` (Mercedes-Benz 독점, Corporate A — Serif 계열)
- **Body font**: `MBCorpoSText` (Mercedes-Benz 독점, Corporate S — Sans 계열)
- **Weight normal / bold**: `100` / `400`

```css
:root {
  --mb-font-family: "MBCorpoSText", "MBCorpoAText", "Helvetica Neue", Arial, sans-serif;
  --mb-font-weight-normal: 100;   /* ⚠️ Ultra Light = 100. 400 아님. */
  --mb-font-weight-bold: 400;
}
body {
  font-family: var(--mb-font-family);
  font-weight: var(--mb-font-weight-normal);
}
```

> **라이선스 주의**: Mercedes-Benz Corporate 폰트는 독점. 외부 프로젝트에서는 `Cormorant Garamond` (serif) + `Raleway Thin` (sans) 조합이 시각적으로 유사.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음. font-weight 100이 23회로 지배적.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-3. Neutral Ramp

| Step | Hex | Count |
|---|---|---|
| 실버 미드 | `#9F9F9F` | 12회 |
| 순흑 | `#000000` | 2회 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| 링크 / 보조 텍스트 | `#9F9F9F` | 네비게이션 링크, 보조 콘텐츠 |
| 주요 텍스트 / 배경 다크 | `#000000` | 본문, 다크 섹션 배경 |

> **참고**: Mercedes-Benz 마케팅 사이트는 극도로 모노크롬. 실버 `#9F9F9F`가 가장 특징적인 컬러이며, 이는 럭셔리 자동차의 실버 금속감을 UI에 반영한 것.

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음. CSS에서 `1.25rem` 간격이 목격됨.

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — radius 토큰이 CSS에서 추출되지 않음. 주로 sharp corner (0) 사용.

---

## 12. Components
<!-- SOURCE: manual -->

### Navigation Link

```html
<brandhub-search-link-list-item>
  <slot name="link-list-links">
    <ul>
      <li><a href="#">Models</a></li>
    </ul>
  </slot>
</brandhub-search-link-list-item>
```

| 속성 | 값 |
|---|---|
| color | `#9F9F9F` |
| font-size | `1.1428571429rem` |
| gap | `1.25rem` |
| transition | `color .4s ease-in-out` |

### Hero Section

```html
<section class="hero">
  <div class="hero__visual">
    <img src="vehicle.jpg" alt="Mercedes-Benz" />
  </div>
  <div class="hero__text">
    <h1>The new E-Class.</h1>
    <a href="#" class="cta">Discover more</a>
  </div>
</section>
```

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 관사 포함, 품격 있는 단문 | "The new E-Class." |
| Primary CTA | 발견 유도형 | "Discover more" |
| Secondary CTA | 설정/구성 | "Configure" |
| Subheading | 감성적 단문 | "Luxury reimagined." |
| Tone | 절제된 럭셔리, 독일식 정밀성, 정관사 사용 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Mercedes-Benz — copy into your root stylesheet */
:root {
  /* Fonts */
  --mb-font-family: "MBCorpoSText", "MBCorpoAText", "Helvetica Neue", Arial, sans-serif;
  --mb-font-weight-normal: 100;   /* Ultra Light */
  --mb-font-weight-bold: 400;

  /* Brand (monochrome + silver) */
  --mb-color-silver: #9F9F9F;
  --mb-color-black: #000000;
  --mb-color-white: #FFFFFF;

  /* Surfaces */
  --mb-bg-page: #FFFFFF;
  --mb-bg-dark: #000000;
  --mb-text: #000000;
  --mb-text-muted: #9F9F9F;

  /* Spacing observed */
  --mb-space-nav: 1.25rem;
  --mb-font-size-nav: 1.1428571429rem;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- body에 `font-weight: 100` 사용 — 이것이 Mercedes의 핵심
- 네비게이션 링크 색으로 `#9F9F9F` (실버 미드) 사용
- 링크 hover에 `transition: color .4s ease-in-out` 적용
- 레이아웃 최대한 여백 넓게, 미니멀하게
- Web Components 커스텀 엘리먼트 패턴 참고

### ❌ DON'T
- body를 `font-weight: 400` 이상으로 쓰지 말 것
- 컬러풀한 accent 추가하지 말 것 — 모노크롬이 정체성
- 버튼 모서리를 둥글게 만들지 말 것
- `#9F9F9F`를 브랜드 컬러라 착각해 CTA 버튼에 쓰지 말 것 — 보조 텍스트 색
