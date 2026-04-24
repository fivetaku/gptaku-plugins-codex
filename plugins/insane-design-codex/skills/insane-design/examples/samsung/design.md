---
slug: samsung
service_name: Samsung
site_url: https://www.samsung.com/sec/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#212425"
primary_font: Samsung Sharp Sans
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Samsung (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Samsung처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Samsung Sharp Sans", "SamsungOneKorean", "Dotum", "돋움", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #212425; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #212425; }
```

**절대 하지 말아야 할 것 하나**: 버튼을 파랗게 만드는 것. Samsung 웹사이트의 기본 CTA(`.btn-type2`)는 `#212425` — 거의 검정에 가까운 near-black이다. 삼성의 파란색(`.btn-type3` #2189FF)은 보조 액션에만 쓴다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.samsung.com/sec/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다수 외부 CSS |
| Token prefix | N/A (커스텀 프로퍼티 없음, 리터럴 hex 직접 사용) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: 레거시 HTML/CSS (전통적 멀티페이지 사이트)
- **Design system**: 커스텀 CSS — prefix 없는 BEM-유사 클래스
- **CSS architecture**: 플랫 클래스 계층
  ```
  글로벌 리셋 + 공통 컴포넌트 (btn, layer 등)
  페이지별 CSS 개별 로드
  ```
- **Class naming**: 전통 BEM (`.btn`, `.btn-type1`, `.btn-type2`, `.layer-app`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스팅 woff2 (Samsung Sharp Sans, SamsungOneKorean)
- **Canonical anchor**: `#212425` — primary CTA 버튼 색으로 고정

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Samsung Sharp Sans` (Samsung 독점, 유료)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: "Samsung Sharp Sans", "SamsungOneKorean", "Dotum", "돋움", sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스 주의**: `Samsung Sharp Sans`는 삼성 독점 폰트로 외부 사용 불가. 대체재: `Noto Sans KR` 또는 `Pretendard`.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS에 명시적 타이포 스케일 토큰이 없음. 컴포넌트별 리터럴 px 값 직접 적용.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | 14px | 400 | 1.5 | N/A |
| button | 14px | bold | 1 | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (2 steps)

| Token | Hex |
|---|---|
| brand-primary | `#212425` |
| brand-blue | `#2189FF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| disabled | `#8F8F8F` | — |
| text | `#212425` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --btn-primary-bg | `#212425` | 기본 CTA 버튼 배경 |
| --btn-primary-color | `#FFFFFF` | 기본 CTA 버튼 텍스트 |
| --btn-blue-bg | `#2189FF` | 보조 액션 버튼 배경 |
| --btn-disabled | `#8F8F8F` | 비활성 버튼 |
| --border | `#212425` | btn-type1 테두리 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| btn-px | 24px | 버튼 좌우 패딩 |
| btn-mx | 4px | 버튼 간 간격 |
| layer-pb | 24px | 레이어 하단 패딩 |

**주요 alias**:
- 버튼 패딩: 24px (좌우 고정)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn | 0px | 기본 버튼 (각진 모서리) |
| N/A | N/A | 별도 radius 토큰 없음 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Primary (`.btn-type2`)

```html
<button class="btn btn-type2">구매하기</button>
```

| 속성 | 값 |
|---|---|
| background | `#212425` |
| color | `#FFFFFF` |
| border-color | `#212425` |
| padding | 좌우 24px |
| font-weight | bold |

### Button — Outline (`.btn-type1`)

```html
<button class="btn btn-type1">자세히 보기</button>
```

| 속성 | 값 |
|---|---|
| color | `#212425` |
| background | `#FFFFFF` |
| border | 1px solid `#212425` |

### Button — Blue (`.btn-type3`)

```html
<button class="btn btn-type3">다운로드</button>
```

| 속성 | 값 |
|---|---|
| color | `#FFFFFF` |
| background | `#2189FF` |
| border-color | `#2189FF` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 제품명 + 짧은 슬로건 | "Galaxy S25 Ultra" |
| Primary CTA | 동사형 한국어 | "구매하기" |
| Secondary CTA | 더보기 패턴 | "자세히 보기" |
| Tone | 공식적, 간결 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Samsung — copy into your root stylesheet */
:root {
  /* Fonts */
  --samsung-font-family: "Samsung Sharp Sans", "SamsungOneKorean", "Dotum", "돋움", sans-serif;
  --samsung-font-weight-normal: 400;
  --samsung-font-weight-bold: 700;

  /* Brand */
  --samsung-color-brand: #212425;
  --samsung-color-blue: #2189FF;
  --samsung-color-disabled: #8F8F8F;

  /* Surfaces */
  --samsung-bg-page: #FFFFFF;
  --samsung-text: #212425;
  --samsung-text-muted: #8F8F8F;

  /* Key spacing */
  --samsung-space-btn-px: 24px;
  --samsung-space-btn-mx: 4px;

  /* Radius */
  --samsung-radius: 0px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- CTA 버튼은 `#212425` near-black 사용 (삼성의 정체성)
- 한국어 UI는 `SamsungOneKorean` 폰트 사용
- 버튼 모서리는 각지게 (border-radius: 0)
- 보조 액션에만 `#2189FF` 파랑 사용

### ❌ DON'T
- 기본 CTA에 파란색 버튼 넣기 — 삼성 웹은 black CTA가 기본
- 버튼에 둥근 모서리 사용 — 삼성 웹 버튼은 각짐
- `Samsung Sharp Sans`를 라이선스 없이 사용
- 폰트 굵기를 700 이하로 낮추면 "삼성답지 않은" 느낌
