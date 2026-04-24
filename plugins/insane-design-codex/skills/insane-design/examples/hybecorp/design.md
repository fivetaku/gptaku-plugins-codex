---
slug: hybecorp
service_name: HYBE Corp
site_url: https://hybecorp.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#F5FF00"
primary_font: Big Hit 201110
font_weight_normal: 500
token_prefix: --primary
---

# DESIGN.md — HYBE Corp (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 HYBE처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'Big Hit 201110', 'Noto Sans KR', sans-serif;
  font-weight: 500;   /* ⚠️ 400 아님. HYBE는 500이 기본. */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #111111; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #F5FF00; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백(`#FFFFFF`)으로 두는 것. HYBE 메인 사이트는 짙은 검정(`#111111`)이 기반이다. 밝은 배경에 올리면 K-엔터 감성이 완전히 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://hybecorp.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | ~200KB |
| CSS files | 외부 + 인라인 혼합 |
| Token prefix | `--primary` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: 서버 사이드 렌더링 (Swiper.js 기반 슬라이더)
- **Design system**: 자체 커스텀 — prefix `--primary`
- **CSS architecture**: 단층 커스텀 프로퍼티 (6개 변수)
  ```
  core  (--primary, --swiper-*)  raw hex
  ```
- **Class naming**: BEM-like (`.header .nav`, `.btn_nav`)
- **Default theme**: dark (bg = `#111111`)
- **Font loading**: `@font-face` 셀프 호스트 (`Big Hit 201110`, `Noto Sans KR`)
- **Canonical anchor**: `#10182F` → 딥 네이비 primary 변수; `#F5FF00` → 네온 옐로우 hover accent

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Big Hit 201110` (HYBE 전용 사내 폰트, 유료)
- **Code font**: N/A
- **Weight normal / bold**: `500` / `700`

```css
:root {
  --font-family: 'Big Hit 201110', 'Noto Sans KR', sans-serif;
  --font-weight-normal: 500;
  --font-weight-bold: 700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| nav-link | 2.8rem | 700 | 1.2 | -0.04rem |
| menu-link | 1.8rem | 500 | 2.06 | -0.026rem |
| body-base | 1rem | 500 | 1.6 | 0 |

> ⚠️ rem 기반 폰트 스케일. 네비게이션 타이틀은 `2.8rem`으로 매우 크다. `text-transform: uppercase`가 NAV 레벨에 적용된다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| `--primary` | `#10182F` |
| nav-bg | `#111111` |
| accent-hover | `#F5FF00` ⭐ **canonical 네온** |
| fg | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 100 | `#FFFFFF` | `#111111` |
| 200 | N/A | `#000000` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--primary` | `#10182F` | primary background |
| `--swiper-theme-color` | `#007AFF` | Swiper 컴포넌트 accent |
| nav bg | `#111111` | 헤더 배경 |
| accent hover | `#F5FF00` | 링크 hover, 밑줄 |
| text primary | `#FFFFFF` | 본문 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#111111` | dominant | 배경 (nav, lnb) |
| 2 | `#FFFFFF` | high | 텍스트, 링크 |
| 3 | `#F5FF00` | medium | hover accent |
| 4 | `#10182F` | medium | --primary bg |
| 5 | `#000000` | low | swiper navigation |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| section-pad-v | 7.7rem | 모바일 메뉴 하단 패딩 |
| lnb-pad | 6rem 2rem | 모바일 메뉴 내부 패딩 |
| nav-height | 44px | swiper 네비게이션 |

**주요 alias**:
- `section-pad-v` → 7.7rem (모바일 LNB 바닥 여백)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| default | 0 | 버튼, 카드 모두 각진 디자인 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| nav-transition | `all 0.3s ease-out 0s` | nav bg 슬라이드 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Nav CTA

```html
<button class="btn_nav" type="button" aria-label="메뉴 열기">
  <!-- hamburger icon -->
</button>
```

| Spec | Value |
|---|---|
| bg-before/after | `#111111` |
| width | 2.2rem |
| height | 2px |

### Nav Link

```html
<a class="gnb-link" href="#">메뉴명</a>
```

| Spec | Value |
|---|---|
| font-size | 2.8rem |
| font-family | `Big Hit 201110` |
| font-weight | 700 |
| color | `#111111` |
| text-transform | uppercase |
| letter-spacing | -0.04rem |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 대문자 영문, 임팩트형 | "HYBE" |
| Primary CTA | 짧고 직접적 | "더 보기" |
| Tone | 무게감 있는 공식 어조, 감정 없음 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* HYBE Corp — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: 'Big Hit 201110', 'Noto Sans KR', sans-serif;
  --font-weight-normal: 500;
  --font-weight-bold: 700;

  /* Brand */
  --brand: #F5FF00;    /* ← canonical neon accent */
  --primary: #10182F;

  /* Surfaces */
  --bg-page: #111111;
  --bg-dark: #000000;
  --text: #FFFFFF;
  --text-muted: rgba(255,255,255,0.6);

  /* Key spacing */
  --space-sm: 2rem;
  --space-md: 6rem;
  --space-lg: 7.7rem;

  /* Radius */
  --radius-sm: 0;
  --radius-md: 0;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO
- `Big Hit 201110` 폰트에 `font-weight: 700`을 적극 활용하라 — 굵기 대비가 HYBE 디자인의 핵심이다.
- 배경은 `#111111`(진 검정)으로 유지하라. pure black(`#000`)보다 조금 더 따뜻한 검정이 브랜드 감성이다.
- hover 상태에 `#F5FF00` 네온 옐로우를 정확히 써라 — 이 색이 HYBE의 유일한 강조색이다.
- 네비게이션 텍스트에 `text-transform: uppercase`를 적용하라.
- letter-spacing은 `-0.04rem`(nav), `-0.026rem`(menu)로 미세 조정하라.

### DON'T
- 배경을 `#FFFFFF`(흰색)으로 두지 마라 — HYBE 메인 사이트는 다크 테마다.
- `#F5FF00`을 본문 텍스트에 쓰지 마라 — hover/accent 전용이다.
- `font-weight: 400`으로 두지 마라 — HYBE의 기본은 500이다.
- `#007AFF`(swiper 컬러)를 브랜드 색으로 착각하지 마라 — 라이브러리 기본값일 뿐이다.
- 모서리를 둥글게 만들지 마라 — HYBE UI는 전부 각진(radius: 0) 디자인이다.
