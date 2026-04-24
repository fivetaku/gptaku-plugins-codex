---
slug: volvo
service_name: Volvo
site_url: https://volvo.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#1F1F1F"
primary_font: Volvo Novum
font_weight_normal: 400
token_prefix: --ot-btn-*
---

# DESIGN.md — Volvo (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Volvo처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Volvo Novum", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1F1F1F; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #1F1F1F; }
```

**절대 하지 말아야 할 것 하나**: 폰트를 일반 sans-serif로 대체할 때 일반 Regular(400)만 쓰는 것. Volvo Novum은 `SemiLight` 변형이 별도로 있고, weight spectrum이 100~bold까지 광범위하다(9가지). 이 다양한 weight 조합이 Volvo 타이포그래피의 핵심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://volvo.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | N/A |
| Token prefix | `--ot-btn-*` (OneTrust 동의 버튼 레이어) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

> **참고**: Volvo 마케팅 사이트의 CSS 파싱 결과가 대부분 OneTrust 쿠키 동의 UI 컬러이다. 실제 Volvo 브랜드 CSS는 정적 파싱으로 충분히 추출되지 않음. font-family는 `Volvo Novum`이 24회로 가장 많이 감지됨.

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 플랫폼)
- **Design system**: Volvo 내부 디자인 시스템
- **CSS architecture**: N/A (토큰 시스템 미노출, OneTrust 레이어만 파싱됨)
- **Class naming**: N/A
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스트 (`Volvo Novum`, `Volvo Novum SemiLight`, `Volvo Broad`)
- **Canonical anchor**: `#1F1F1F` — `--ot-btn-primary-bg` 값 (다크 버튼 배경)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Volvo Broad` (Volvo 독점, 디스플레이 전용)
- **Body font**: `Volvo Novum` (Volvo 독점, 주요 텍스트)
- **Narrow font**: `Volvo Novum SemiLight` (Volvo 독점)
- **Weight normal / bold**: `400` / `bold`

```css
:root {
  --volvo-font-family: "Volvo Novum", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --volvo-font-family-semi: "Volvo Novum SemiLight", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --volvo-font-weight-normal: 400;
  --volvo-font-weight-bold: 700;
}
body {
  font-family: var(--volvo-font-family);
  font-weight: var(--volvo-font-weight-normal);
}
```

> **라이선스 주의**: Volvo 폰트는 독점. 외부 프로젝트에서는 `Source Sans Pro` 또는 `Noto Sans` + `Narrow` 변형이 유사.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.
> 감지된 weight: 100(1회), 300(13회), 350(2회), 400(17회), 500(16회), 600(7회), 700(12회), bold(21회), normal(6회) — 9가지 weight.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-3. Neutral Ramp (OneTrust 버튼 — Volvo 사이트 적용)

| Step | Light 테마 | Dark 테마 |
|---|---|---|
| primary button bg | `#1F1F1F` | `#E5E7EB` |
| primary button text | `#FFFFFF` | `#0B0F19` |
| primary hover bg | `#3A3A3A` | `#CBD5E1` |
| primary active bg | `#4C4C4C` | `#94A3B8` |
| primary border | `#FFFFFF` | `#0B0F19` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--ot-btn-primary-bg` (dark) | `#1F1F1F` | OneTrust 버튼 배경 (다크 테마) |
| `--ot-btn-primary-text` | `#FFFFFF` | 버튼 텍스트 |
| `--ot-btn-primary-hover` | `#3A3A3A` | 버튼 hover |
| `--ot-btn-primary-bg` (light) | `#E5E7EB` | OneTrust 버튼 배경 (라이트 테마) |

> **주의**: 이 컬러들은 OneTrust 쿠키 동의 UI의 것. Volvo 자체 브랜드 컬러(파란 계열)는 CSS 파싱에서 추출되지 않음.

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — radius 토큰이 CSS에서 추출되지 않음.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary Button (OneTrust 레이어 관찰값)

```html
<button class="volvo-btn volvo-btn--primary" type="button">
  See Models
</button>
```

| 속성 | 값 |
|---|---|
| background-color | `#1F1F1F` |
| color | `#FFFFFF` |
| hover background-color | `#3A3A3A` |
| active background-color | `#4C4C4C` |
| border | `1px solid #FFFFFF` |
| font-family | `Volvo Novum` |

### Hero Section

```html
<section class="hero">
  <div class="hero__media">
    <!-- 차량 전체 폭 사진 -->
  </div>
  <div class="hero__content">
    <h1>Volvo EX90</h1>
    <a href="#" class="btn btn--primary">Explore</a>
  </div>
</section>
```

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 모델명, 스칸디나비아식 간결 | "Volvo EX90" |
| Primary CTA | 발견/탐색 중심 | "Explore" / "Configure" |
| Secondary CTA | 안전·지속가능성 강조 | "Learn about safety" |
| Subheading | 안전, 지속가능성, 전기차 미래 | "Electric. Safe. Sustainable." |
| Tone | 스칸디나비아 미니멀, 안전 강조, 따뜻한 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Volvo — copy into your root stylesheet */
:root {
  /* Fonts */
  --volvo-font-family: "Volvo Novum", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --volvo-font-family-semi: "Volvo Novum SemiLight", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --volvo-font-weight-normal: 400;
  --volvo-font-weight-bold: 700;

  /* Brand (다크 버튼 / OneTrust 레이어에서 관찰) */
  --volvo-color-btn-dark: #1F1F1F;
  --volvo-color-btn-dark-hover: #3A3A3A;
  --volvo-color-btn-dark-active: #4C4C4C;

  /* Surfaces */
  --volvo-bg-page: #FFFFFF;
  --volvo-bg-dark: #1F1F1F;
  --volvo-text: #1F1F1F;
  --volvo-text-muted: #4C4C4C;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 폰트 weight를 다양하게 (100~bold 9단계) — Volvo 타이포그래피의 핵심
- `Volvo Novum SemiLight` 변형 활용
- 버튼은 다크 배경 `#1F1F1F` + 흰 텍스트 패턴
- 스칸디나비아식 미니멀 레이아웃 (여백 충분)
- 안전과 지속가능성 메시지 강조

### ❌ DON'T
- weight를 400 하나로만 쓰지 말 것
- OneTrust 색(`#1C6BBA` 등)을 Volvo 브랜드 색으로 쓰지 말 것
- CSS 파싱에서 미확인된 Volvo 브랜드 블루를 추정으로 채우지 말 것
- 레이아웃을 복잡하게 만들지 말 것
