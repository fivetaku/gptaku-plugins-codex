---
slug: daangn
service_name: 당근마켓
site_url: https://www.daangn.com/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#FF6600"
primary_font: Pretendard Variable
font_weight_normal: 400
token_prefix: --seed-
---

# DESIGN.md — 당근마켓 (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 당근마켓처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Pretendard Variable", -apple-system, BlinkMacSystemFont,
               "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FF6600; }
```

**절대 하지 말아야 할 것 하나**: `--seed-*` 토큰을 직접 hex로 교체하는 것. 당근마켓은 Seed Design System의 CSS 변수 계층(`--seed-color-fg-neutral`, `--seed-dimension-x10` 등)을 컴포넌트 전체에서 사용한다. 하드코딩하면 다크 모드와 테마 대응이 전부 깨진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.daangn.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Seed Design System CSS 번들 |
| Token prefix | `--seed-` (Seed Design System) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React (Next.js 추정, 마케팅 사이트)
- **Design system**: Seed Design System — `--seed-*` prefix
- **CSS architecture**: Seed 토큰 계층
  ```
  --seed-color-* (컬러 토큰)
  --seed-dimension-* (크기 토큰, x1~x10 배수 시스템)
  --seed-font-* (타이포 토큰)
  --seed-radius-* (라디우스 토큰)
  --seed-timing-function-* (모션 토큰)
  --seed-duration-* (모션 지속시간)
  ```
- **Class naming**: BEM (`seed-action-button--variant_ghost`, `seed-callout__link`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: Pretendard Variable (CDN)
- **Canonical anchor**: `#FF6600` — 당근마켓 시그니처 오렌지

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Pretendard Variable` (오픈소스, SIL 라이선스)
- **Code font**: `Fira Code` (부분 사용)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --seed-font-family: "Pretendard Variable", -apple-system, BlinkMacSystemFont,
                      "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  --seed-font-weight-regular: 400;
  --seed-font-weight-bold: 700;
}
body {
  font-family: var(--seed-font-family);
  font-weight: var(--seed-font-weight-regular);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ Seed 토큰 참조 구조 (`--seed-font-size-t1`, `--seed-line-height-t4` 등). 실제 px 값은 Seed 변수 해석 필요.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| t2 (callout-link) | var(--seed-font-size-t2) | var(--seed-font-weight-regular) | var(--seed-line-height-t2) | N/A |
| t3 (page-banner) | var(--seed-font-size-t3) | N/A | var(--seed-line-height-t3) | N/A |
| t4 (callout) | var(--seed-font-size-t4) | var(--seed-font-weight-regular) | var(--seed-line-height-t4) | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (2 steps)

| Token | Hex |
|---|---|
| brand-orange | `#FF6600` |
| brand-orange-svg | `#FF6F0F` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| black | `#000000` | — |
| overlay-50 | `#00000080` | — |
| transparent | `#00000000` | — |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| accent-blue | active | `#2299DD` |
| accent-border | ui | `#DCDEE3` |
| text-muted | body | `#868B94` |
| text-secondary | body | `#B0B3BA` |
| bg-muted | surface | `#F3F4F5` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --seed-color-fg-neutral | (Seed 변수) | 기본 전경색 |
| --seed-color-fg-disabled | (Seed 변수) | 비활성 전경색 |
| brand-orange | `#FF6600` | CTA 버튼, 브랜드 강조 |
| yarl-button-active | `#FFFFFF` | 라이트박스 버튼 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| --seed-dimension-x4 | (Seed 변수 × 4) | 버튼 내부 패딩 기준 |
| --seed-dimension-x10 | (Seed 변수 × 10) | 버튼 최소 크기 (touch target) |
| link-text-underline-offset | 2px | 링크 밑줄 offset |

**주요 alias**:
- `x1` 배수 시스템 (Seed dimension 토큰 기반)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| --seed-radius-full | (Seed 변수, 원형) | 원형 버튼, 배지 |
| border-transition | 0.1s | 포커스 테두리 트랜지션 |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| --seed-timing-function-easing | (Seed 변수) | 기본 easing |
| --seed-duration-d3 | (Seed 변수) | 포커스 아웃라인 트랜지션 |
| border-transition | 0.1s | 인풋 테두리 색 전환 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Action Button — Ghost (`.seed-action-button--variant_ghost`)

```html
<button class="seed-action-button seed-action-button--variant_ghost">자세히 보기</button>
```

| 속성 | 값 |
|---|---|
| background | `#FFFFFF00` (투명) |
| color | var(--seed-color-fg-neutral) |
| --seed-box-color | var(--seed-color-fg-neutral) |

### Callout Link (`.seed-callout__link`)

```html
<a class="seed-callout__link" href="#">링크</a>
```

| 속성 | 값 |
|---|---|
| background-color | `#00000000` (투명) |
| font-size | var(--seed-font-size-t4) |
| font-weight | var(--seed-font-weight-regular) |
| text-underline-offset | 2px |

### Input Focus Ring (`.seed-input-button__button:after`)

```html
<div class="seed-input-button__button"></div>
```

| 속성 | 값 |
|---|---|
| border | 2px solid `#0000` |
| border-radius | inherit |
| transition | border-color 0.1s var(--seed-timing-function-easing) |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 지역 커뮤니티 감성 | "당신 근처의 거래" |
| Primary CTA | 행동 유발 간결 동사 | "당근에서 거래하기" |
| Tone | 따뜻하고 친근 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* 당근마켓 — copy into your root stylesheet */
:root {
  /* Fonts */
  --daangn-font-family: "Pretendard Variable", -apple-system, BlinkMacSystemFont,
                        "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --daangn-font-weight-regular: 400;
  --daangn-font-weight-bold: 700;

  /* Brand */
  --daangn-color-brand: #FF6600;
  --daangn-color-accent-blue: #2299DD;

  /* Surfaces */
  --daangn-bg-page: #FFFFFF;
  --daangn-text: #000000;
  --daangn-text-muted: #868B94;

  /* Border */
  --daangn-border: #DCDEE3;

  /* Seed dimension reference */
  --daangn-underline-offset: 2px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- `--seed-*` CSS 변수 계층 유지 — 다크 모드 자동 대응
- Pretendard Variable 사용 (variable font로 단일 파일에서 모든 weight)
- ghost 버튼은 투명 배경(`#00000000`) 유지
- touch target은 `--seed-dimension-x10` 기준 이상 확보

### ❌ DON'T
- `--seed-*` 변수를 하드코딩 hex로 교체 — 테마/다크 모드 깨짐
- `#FF6F0F` SVG 패턴 색을 브랜드 오렌지로 사용 — `#FF6600`이 CTA 기준색
- Seed 토큰 없이 직접 hex 작성 — 컴포넌트 일관성 붕괴
