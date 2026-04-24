---
slug: gentlemonster
service_name: Gentle Monster
site_url: https://gentlemonster.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#111111"
primary_font: Gentle Monster Serif
font_weight_normal: 350
token_prefix: N/A
---

# DESIGN.md — Gentle Monster (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Gentle Monster처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight 350 */
body {
  font-family: "__gentleSansLightEn_162c6d", Arial, sans-serif;
  font-weight: 350;   /* ⚠️ 400 아님. GM의 Light 계열은 350. */
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #111111; }
```

**절대 하지 말아야 할 것 하나**: `font-weight: 400`을 기본으로 두는 것. Gentle Monster UI의 정체성은 **weight 350의 Light 계열 폰트**다. 400으로 쓰면 럭셔리 감성이 무너진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://gentlemonster.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | Next.js SSR |
| CSS files | next/font 셀프 호스트 (다수의 __gentle* 폰트) |
| Token prefix | N/A (커스텀 프로퍼티 없음) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (next/font 기반 폰트 로딩)
- **Design system**: 자체 커스텀 — CSS 커스텀 프로퍼티 없음, 직접 hex 사용
- **CSS architecture**: 단층 (클래스 직접 스타일, 토큰 계층 없음)
  ```
  직접 hex (no token prefix)
  ```
- **Class naming**: CSS Modules (Next.js `__className_*` 패턴, `Accordion_child_button__GNvrM` 등)
- **Default theme**: 흰 배경(`#FFFFFF`)에 검정 텍스트(`#111111`) — 라이트 기반이지만 전반적으로 미니멀 다크 감성
- **Font loading**: next/font 셀프 호스트 — `__gentleMonsterSerif_*`, `__gentleSansLight*`, `__gentleSansRegular*` 등 언어별 다중 폰트
- **Canonical anchor**: `#111111` — CTA 버튼, 텍스트 primary 전부 이 색

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Gentle Monster Serif` (next/font로 셀프 호스트, `__gentleMonsterSerif_66f77e`)
- **Body font**: `Gentle Sans Light` (언어별 — En: `__gentleSansLightEn_162c6d`, Ko: `__gentleSansLightKo_d1ed49`)
- **Code font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`
- **Weight normal / bold**: `350` / `700`

```css
/* Gentle Monster — font 선언 */
body {
  font-family: "__gentleSansLightEn_162c6d", Arial, sans-serif;
  font-weight: 350;   /* GM Light 계열 비표준 weight */
}
h1, h2 {
  font-family: "__gentleMonsterSerif_66f77e", Arial, sans-serif;
  font-weight: 700;
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | 1rem | 350 | 1.6 | 0 |
| button | 0.875rem | 400 | 1 | 0 |
| caption | 0.6875rem | 400 | 1.36 | 0 |

> ⚠️ GM 폰트는 `350` weight를 비표준으로 지원한다. 일반 Inter나 Arial로 대체하면 weight 350이 무시되어 400으로 렌더된다. 가장 가까운 대체는 `font-weight: 300`(Light)이다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| primary | `#111111` ⭐ **canonical** |
| disabled | `#858585` |
| bg | `#FFFFFF` |
| border | `#D8D8D8` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| text-primary | `#111111` | 모든 텍스트, CTA 버튼 배경 |
| btn-disabled | `#858585` | 비활성화 버튼 배경 + 테두리 |
| btn-text | `#FFFFFF` | CTA 버튼 텍스트 |
| border | `#D8D8D8` | 구분선, Accordion 하단 |
| bg | `#FFFFFF` | 페이지 배경 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#111111` | dominant | 텍스트, CTA, icon |
| 2 | `#FFFFFF` | high | 배경, 버튼 텍스트 |
| 3 | `#858585` | medium | 비활성화 상태 |
| 4 | `#D8D8D8` | medium | 구분선 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| btn-padding | 15px 0 | Accordion 버튼 상하 패딩 |

**주요 alias**:
- `btn-v-pad` → 15px (Accordion 항목 상하 여백)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| cookie-btn | 8px | OneTrust 동의 버튼 |
| default | 0 | 일반 버튼, 카드 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Primary CTA

```html
<button class="btn-common" type="button">구매하기</button>
```

| Spec | Value |
|---|---|
| background | `#111111` |
| color | `#FFFFFF` |
| border | `1px solid #111111` |
| height | 48px |
| border-radius | 8px (OneTrust) / 0 (일반) |

### Accordion — 제품 상세

```html
<button class="Accordion_child_button__GNvrM" type="button">
  상세 정보
</button>
```

| Spec | Value |
|---|---|
| border-bottom | `1px solid #D8D8D8` |
| padding | `15px 0` |
| bg-pseudo | `#000000` (::before, ::after) |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 아트/오브제 중심 서사, 짧고 신비롭게 | "ANOTHER ME" |
| Primary CTA | 동작 중심, 간결 | "Shop Now" |
| Tone | 럭셔리 패션, 감각적이고 절제된 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Gentle Monster — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "__gentleSansLightEn_162c6d", Arial, sans-serif;
  --font-family-serif: "__gentleMonsterSerif_66f77e", Arial, sans-serif;
  --font-weight-normal: 350;
  --font-weight-bold: 700;

  /* Brand */
  --brand: #111111;    /* ← canonical */

  /* Surfaces */
  --bg-page: #FFFFFF;
  --bg-dark: #111111;
  --text: #111111;
  --text-muted: #858585;

  /* Key spacing */
  --space-sm: 15px;
  --space-md: 32px;
  --space-lg: 64px;

  /* Radius */
  --radius-sm: 0;
  --radius-md: 8px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO
- `font-weight: 350`을 정확히 써라 — GM 폰트 전용 비표준 weight이다.
- 배경은 순백(`#FFFFFF`)으로 써라 — GM은 라이트 베이스다.
- 텍스트와 CTA 버튼 배경은 모두 `#111111`으로 통일하라.
- 폰트는 언어별로 구분하라 — 영문은 `__gentleSansLightEn`, 한글은 `__gentleSansLightKo`.
- 미니멀을 유지하라 — 브랜드 색이 없어도 강하다.

### DON'T
- `font-weight: 400`을 기본으로 두지 마라 — GM의 기본은 350이다.
- 밝은 컬러(파랑, 빨강)를 accent로 쓰지 마라 — GM은 흑백 2색 시스템이다.
- 모서리를 과도하게 둥글게 만들지 마라 — 일반 버튼은 radius 0이 기본이다.
- 로고용 이미지 hex를 UI 색으로 착각하지 마라 — GM 아트 이미지의 색은 UI에 적용되지 않는다.
- `#858585`를 일반 텍스트에 쓰지 마라 — 비활성화(disabled) 전용이다.
