---
slug: kakaocorp
service_name: Kakao
site_url: https://www.kakaocorp.com/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#FEE500"
primary_font: KakaoBig
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Kakao (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Kakao처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: KakaoBig, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #333333; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FEE500; }
```

**절대 하지 말아야 할 것 하나**: 카카오 브랜드 노랑(`#FEE500`)을 텍스트 색으로 쓰는 것. `#FEE500`은 배경색으로만 사용하고 텍스트는 항상 검정(`#000000`)과 함께 쓴다 — 실제 CSS에서 `.btn_play` 배경이 `#FEE500`이고 color가 `#000000`임.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.kakaocorp.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Vue.js scoped CSS (data-v- 해시 포함) |
| Token prefix | N/A (Vue scoped, 리터럴 hex) |
| Method | CSS 셀렉터 역할 분석 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Vue.js (scoped CSS — `[data-v-61c8860e]` 패턴)
- **Design system**: Kakao 전용 커스텀 — `KakaoBig`, `KakaoSmall` 폰트 패밀리
- **CSS architecture**: Vue scoped 컴포넌트 CSS
  ```
  global base (body, button, input 리셋)
  scoped component (data-v-* suffix)
  ```
- **Class naming**: 시맨틱 + 기능 (`.btn_play`, `.btn_stop`, `.btn_more`, `.mo_header`)
- **Default theme**: light (bg = `#FFFFFF`, text = `#333333`)
- **Font loading**: 자체 호스팅 (KakaoBig, KakaoSmall, KakaoDigitLatin)
- **Canonical anchor**: `#FEE500` — 카카오 시그니처 노랑, 배경 전용

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `KakaoBig` (카카오 전용, 대제목용)
- **Body font**: `KakaoSmall` (카카오 전용, 본문용)
- **Digit font**: `KakaoDigitLatin` (숫자/라틴 전용)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --kakao-font-big: KakaoBig, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-small: KakaoSmall, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-weight-normal: 400;
  --kakao-font-weight-bold: 700;
}
body {
  font-family: var(--kakao-font-small);
  font-size: 14px;
  line-height: 1.5;
  font-weight: var(--kakao-font-weight-normal);
  color: #333;
}
```

> 대제목은 KakaoBig(count:108), 본문/UI는 KakaoSmall. `kakaobi`는 아이콘 폰트.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS 리터럴 값 기반 — 체계적 스케일 토큰 없음.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body-base | 14px | 400 | 1.5 | N/A |
| btn_play | 16px | 400 | 1.75 | N/A |
| link-subinfo | 12px | 400 | N/A | -0.2px |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (1 step)

| Token | Hex |
|---|---|
| brand-yellow | `#FEE500` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| text-primary | `#333333` | — |
| text-secondary | `#888888` | — |
| text-tertiary | `#999999` | — |
| text-on-yellow | `#000000` | — |
| border-muted | `#EEEEEE` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| btn_play-bg | `#FEE500` | 재생 버튼 배경 (카카오 노랑) |
| btn_play-color | `#000000` | 재생 버튼 텍스트 |
| btn_stop-border | `#EEEEEE` | 정지 버튼 테두리 |
| direct-link-bg | `#333333` | 스킵 링크 배경 |
| ico_outlink | `#888888` | 외부 링크 아이콘 stroke |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| btn_play-py | 9px 9px 11px | 재생 버튼 패딩 |
| btn_stop-bottom | 40px | 정지 버튼 하단 여백 |
| direct-link-px | 10px | 스킵 링크 패딩 |
| link-subinfo-ls | -0.2px | 서브 링크 자간 |

**주요 alias**:
- 버튼 패딩 비대칭: top 9px, bottom 11px (시각 보정)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn_play | 6px | 재생 버튼 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Play (`.btn_play`)

```html
<button class="btn_play" type="button">재생</button>
```

| 속성 | 값 |
|---|---|
| display | block |
| width | 100% |
| padding | 9px 9px 11px |
| border-radius | 6px |
| font-size | 16px |
| line-height | 1.75 |
| color | `#000000` |
| background | `#FEE500` |

### Navigation Link (`.mo_header .inner_gnb .ico_outlink`)

```html
<span class="ico_outlink"></span>
```

| 속성 | 값 |
|---|---|
| stroke | `#888888` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 카카오 서비스명 중심 | "카카오" |
| Primary CTA | 기능 동사 | "재생" |
| Tone | 친근하고 간결 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Kakao — copy into your root stylesheet */
:root {
  /* Fonts */
  --kakao-font-big: KakaoBig, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-small: KakaoSmall, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-weight-normal: 400;
  --kakao-font-weight-bold: 700;

  /* Brand */
  --kakao-color-brand: #FEE500;
  --kakao-color-brand-text: #000000;

  /* Surfaces */
  --kakao-bg-page: #FFFFFF;
  --kakao-text: #333333;
  --kakao-text-muted: #888888;

  /* Key spacing */
  --kakao-radius-btn: 6px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 카카오 노랑(`#FEE500`) 위에는 항상 검정(`#000000`) 텍스트
- 대제목은 `KakaoBig`, 본문은 `KakaoSmall` 구분 사용
- 버튼 패딩 비대칭 유지: top 9px, bottom 11px
- 아이콘 stroke 색은 `#888888` (회색)

### ❌ DON'T
- `#FEE500` 노랑을 텍스트 색으로 사용 — 배경 전용
- KakaoBig과 KakaoSmall을 하나의 font-family로 통합 — 별도 패밀리
- 카카오 UI에서 border-radius 8px 이상 — 현재 CSS 기준 6px가 최대
