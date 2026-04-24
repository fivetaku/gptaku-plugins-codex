---
slug: lg
service_name: LG
site_url: https://www.lg.com/kr/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#B31045"
primary_font: LGSmHaTSB
font_weight_normal: 700
token_prefix: N/A
---

# DESIGN.md — LG (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 LG처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "LGSmHaTSB", sans-serif;
  font-weight: 700;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #B31045; }
```

**절대 하지 말아야 할 것 하나**: LG 브랜드 색을 `#C00000` 빨강으로 기억하는 것. CSS frequency 데이터에서 `#B31045`(2회)와 `#C00000`(2회)가 공존하지만, 실제 버튼(`mainpop .btn.go`)에는 `#DD3C70` 핑크-레드 계열이 쓰인다. LG 전자의 웹 CSS는 체계적 토큰이 없어 컴포넌트마다 다른 레드 계열이 사용된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.lg.com/kr/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다수 외부 CSS (레거시 구조) |
| Token prefix | N/A (커스텀 프로퍼티 없음) |
| Method | CSS hex frequency 분석 · 셀렉터 역할 분석 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: 레거시 HTML/CSS (전통 대기업 사이트)
- **Design system**: 커스텀 CSS — 체계적 토큰 없음
- **CSS architecture**: 페이지별 플랫 CSS
  ```
  global reset
  component CSS (mainpop, btn 등)
  page-specific (rem 기반 모바일 대응)
  ```
- **Class naming**: 전통 시맨틱 (`.mainpop`, `.btn`, `.btn.go`, `.btn.down`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스팅 (`LGSmHaTSB` — LG Smart H ThinSemiBold)
- **Canonical anchor**: `#B31045` — LG 레드 계열 중 가장 순수한 brand red

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `LGSmHaTSB` (LG 전자 전용, 유료)
- **Code font**: N/A
- **Weight normal / bold**: `700` / `bold`

```css
:root {
  --lg-font-family: "LGSmHaTSB", sans-serif;
  --lg-font-weight-normal: 700;
  --lg-font-weight-bold: bold;
}
body {
  font-family: var(--lg-font-family);
  font-weight: var(--lg-font-weight-normal);
}
```

> **주의**: CSS에서 확인된 유일한 LG 전용 폰트는 `LGSmHaTSB`. weight 700과 `bold`가 함께 사용됨.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS에 명시적 타이포 스케일 없음. 레거시 리터럴 px 값 사용.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| btn-go | 14px | N/A | 1.7rem | -0.02em |
| btn-down | 14px | N/A | 1.7rem | N/A |
| body | 0.9rem | N/A | N/A | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (4 steps)

| Token | Hex |
|---|---|
| brand-red | `#B31045` |
| brand-crimson | `#C00000` |
| btn-go | `#DD3C70` |
| btn-down | `#EBB3A4` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| text-body | `#555555` | — |
| text-dark | `#111111` | — |
| mid | `#494949` | — |
| border | `#D9D9D9` | — |
| bg-muted | `#EBEBEB` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| btn-go-bg | `#DD3C70` | 팝업 이동 버튼 배경 |
| btn-down-bg | `#EBB3A4` | 팝업 다운로드 버튼 배경 |
| text-body | `#555555` | 본문 텍스트 |
| text-letter-sp | -0.02em | 버튼 자간 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| btn-px | 14px~46px | 버튼 좌우 패딩 (팝업 버튼) |
| btn-h | 1.7rem | 버튼 높이 |
| body-px | 3rem | 모바일 버튼 좌측 패딩 |

**주요 alias**:
- 레거시 rem 기반 (기준: 폰트 루트 사이즈에 따라 가변)

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — CSS에서 명시적 radius 값 확인 불가

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button — Go (`.mainpop .btn.go`)

```html
<a class="btn go" href="#">이동</a>
```

| 속성 | 값 |
|---|---|
| background | `#DD3C70` (+ 배경 이미지) |
| color | `#FFFFFF` |
| font-size | 14px |
| height | 26px |
| line-height | 26px |
| letter-spacing | -0.02em |

### Button — Download (`.mainpop .btn.down`)

```html
<a class="btn down" href="#">다운로드</a>
```

| 속성 | 값 |
|---|---|
| background | `#EBB3A4` (+ 배경 이미지) |
| font-size | 14px |
| height | 26px |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* LG — copy into your root stylesheet */
:root {
  /* Fonts */
  --lg-font-family: "LGSmHaTSB", sans-serif;
  --lg-font-weight-normal: 700;

  /* Brand */
  --lg-color-brand: #B31045;
  --lg-color-crimson: #C00000;
  --lg-color-btn-go: #DD3C70;
  --lg-color-btn-down: #EBB3A4;

  /* Surfaces */
  --lg-bg-page: #FFFFFF;
  --lg-text: #111111;
  --lg-text-body: #555555;

  /* Radius */
  --lg-radius: 0px;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- LG 폰트는 `LGSmHaTSB` — weight 700이 기본값
- 레드 계열 구분: brand red(`#B31045`), button go(`#DD3C70`), button down(`#EBB3A4`)
- letter-spacing -0.02em 적용 (버튼 텍스트)
- 본문 텍스트 색은 `#555555`

### ❌ DON'T
- 단일 `#FF0000` 순수 빨강 사용 — LG CSS에 없는 색
- 명시적 타이포 스케일 없는 상태에서 임의 사이즈 토큰 생성
- LG 버튼에 `border-radius` 추가 — 각진 직사각형이 기본
