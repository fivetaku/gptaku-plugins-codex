---
schema_version: 3.1
slug: ferrari
service_name: Ferrari
site_url: https://www.ferrari.com/en-US
fetched_at: 2026-04-23
default_theme: dark
brand_color: "#DA291C"
primary_font: FerrariSans
font_weight_normal: 400
token_prefix: --f-

bold_direction: "Luxury Performance Dark"
aesthetic_category: "Luxury Automotive"
signature_element: gradient_red_accent
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Ferrari (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Ferrari 웹사이트는 **"속도와 럭셔리를 동시에 구현한 다크 시네마틱 사이트"**다. 대부분의 자동차 브랜드가 밝은 배경에 차량 사진을 나열할 때, Ferrari는 `#181818` 근-검정 배경 위에 차량을 올려 **스포트라이트 아래 무대에 선 작품처럼** 연출한다.

색상 전략은 **"근-검정 한 축 + 레드 accent 한 점"**이다. 브랜드 레드 `#DA291C`는 절대 면적으로 쓰이지 않는다. 그라디언트 오버레이(`linear-gradient(180deg, #a00c01, #da291c 64%)`), 포커스 링, 중요 CTA 배경에만 등장한다. 나머지는 `#181818 → #303030 → #666 → #8f8f8f → #d2d2d2 → #f7f7f7`의 7단계 회색 ramp가 모든 계층을 담당한다.

타이포그래피는 **독점 서체 `FerrariSans` 단일 시스템**이다. 외부 구매 불가, 브랜드 아이덴티티 그 자체. 폰트 사이즈는 9px부터 28px까지 픽셀 단위로 정밀하게 제어되고, 줄간격 1.23(헤딩)~1.5(본문)의 빡빡한 라인이 긴장감을 만든다.

시그니처 요소는 **레드 그라디언트**다. `--f-color-gradient-red: linear-gradient(180deg, #a00c01, #da291c 64%)`가 버튼과 accent 요소에 적용되고, 다크 그라디언트 `linear-gradient(180deg, #3c3c3c, #030303 64%)`가 섹션 배경 전환을 담당한다.

### Key Characteristics

- 브랜드 레드 `#DA291C` — 면적 사용 금지, 그라디언트와 포인트에만
- 근-검정 히어로 (`#181818`) + 시네마틱 그라디언트 오버레이
- 독점 서체 FerrariSans — 폴백은 Helvetica Neue
- 노란색 포커스 `#f6e500` — 접근성 색상으로 다크 배경 대비

---

## 01. Quick Start
<!-- SOURCE: css -->

> 5분 안에 Ferrari처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "FerrariSans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  background: #181818;
  color: #f7f7f7;
}

/* 2. 브랜드 레드 그라디언트 버튼 */
.btn-primary {
  background: linear-gradient(180deg, #a00c01, #da291c 64%);
  border: none;
  border-radius: 9999px;
  color: #fff;
  padding: 16px 48px;
}

/* 3. 다크 섹션 그라디언트 */
.section-dark {
  background: linear-gradient(180deg, #3c3c3c, #030303 64%);
}
```

---

## 02. Provenance
<!-- SOURCE: auto -->

| 항목 | 값 |
|------|-----|
| Source URL | `https://www.ferrari.com/en-US` |
| CSS 파일 | `clientlib-site.lc-9c0501eb97f1.min.css` |
| CSS 바이트 | ~14,741 chars (clientlib-site) |
| 수집일 | 2026-04-23 |
| 수집 방법 | curl_cffi (safari impersonation) |

---

## 03. Tech Stack
<!-- SOURCE: html -->

| 항목 | 감지 값 |
|------|---------|
| CMS | Adobe Experience Manager (AEM) — `etc.clientlibs` URL 패턴 |
| CSS 방식 | CSS Custom Properties (`--f-` prefix) |
| 토큰 네임스페이스 | `--f-color-*`, `--f-space-*`, `--f-radius-*`, `--f-shadow-*` |

---

## 04. Font Stack
<!-- SOURCE: css -->

| 역할 | 폰트 | 폴백 |
|------|------|------|
| Primary (전체) | `FerrariSans` | `Helvetica Neue`, Helvetica, Arial, sans-serif |
| CSS 변수 | `var(--f-ferrari-font)` | — |

```css
:root {
  --f-ferrari-font: "FerrariSans";
}
body {
  font-family: var(--f-ferrari-font), "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

---

## 05. Typography Scale
<!-- SOURCE: css -->

| 레벨 | Size | Line Height | 용도 |
|------|------|-------------|------|
| Display | 28px | 1.23 | 대형 헤드라인 |
| Heading | 26px | 1.23 | 섹션 제목 |
| Title | 18px | 1.4 | 카드 제목 |
| Body | 13px | 1.5 | 본문 |
| Caption | 11px | 1.5 | 캡션, 레이블 |
| Micro | 9px | 1.5 | 법적 고지, 메타 |

---

## 06. Colors
<!-- SOURCE: css -->

### Brand Red (Accent)

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--f-color-accent-100` | `#DA291C` | 브랜드 레드 — CTA, 포인트 |
| `--f-color-accent-90` | `#B01E0A` | 레드 다크 — hover |
| `--f-color-accent-80` | `#9D2211` | 레드 딥 |
| `--f-color-gradient-red` | `linear-gradient(180deg, #a00c01, #da291c 64%)` | 버튼 그라디언트 |

### Neutral (Dark → Light)

| 토큰 | 값 |
|------|-----|
| `--f-color-global-black` | `#181818` |
| `--f-color-black-90` | `#303030` |
| `--f-color-black-60` | `#666` |
| `--f-color-black-55` | `#969696` |
| `--f-color-black-50` | `#8F8F8F` |
| `--f-color-black-20` | `#D2D2D2` |
| `--f-color-black-10` | `#F7F7F7` |
| `--f-color-global-white` | `#FFF` |

### Background

| 토큰 | 값 |
|------|-----|
| `--f-color-background-0` | `var(--f-color-global-white)` |
| `--f-color-background-10` | `#EBEBEB` |
| `--f-color-background-darker` | `var(--f-color-black-55)` |

### Accent & Semantic

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--f-color-yellow` | `#F6E500` | 포커스 링 (다크 배경 접근성) |
| `--f-color-yellow-hypersail` | `#FFF200` | Hypersail 에디션 |
| `--f-color-accessible-info` | `#4C98B9` | 정보 상태 |
| `--f-color-accessible-success` | `#03904A` | 성공 상태 |
| `--f-color-accessible-warning` | `#F13A2C` | 경고 상태 |

### Gradients

| 토큰 | 값 |
|------|-----|
| `--f-color-gradient-red` | `linear-gradient(180deg, #a00c01, #da291c 64%)` |
| `--f-color-gradient-dark-grey` | `linear-gradient(180deg, #3c3c3c, #030303 64%)` |
| `--f-color-gradient-shadow-dark` | `linear-gradient(90deg, #121212, #161616)` |
| `--f-color-gradient-shadow-light` | `linear-gradient(180deg, hsla(0,0%,9%,0), hsla(0,0%,9%,.85))` |

---

## 07. Spacing
<!-- SOURCE: css -->

| 토큰 | 값 |
|------|-----|
| `--f-space-xxxs` | `4px` |
| `--f-space-xxs` | `8px` |
| `--f-space-xs` | `16px` |
| `--f-space-s` | `24px` |
| `--f-space-m` | `32px` |
| `--f-space-l` | `48px` |
| `--f-space-xl` | `64px` |
| `--f-space-xxl` | `96px` |
| `--f-space-super` | `128px` |

---

## 08. Border Radius
<!-- SOURCE: css -->

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--f-radius-full` | `9999px` | 버튼, 태그 (pill shape) |
| (inline) | `0` | 카드, 이미지 컨테이너 |

Ferrari는 **pill 버튼 + 0 radius 카드**의 두 극단만 사용한다. 중간값(4px, 8px)은 사용하지 않는다.

---

## 09. Shadows
<!-- SOURCE: css -->

| 토큰 | 값 |
|------|-----|
| `--f-shadow-small` | `0px 4px 8px 0px rgba(0,0,0,.1)` |
| `--f-color-overlay` | `rgba(0,0,0,.3)` |
| `--f-color-overlay-darker` | `hsla(0,0%,7%,.8)` |

---

## 10. Animation
<!-- SOURCE: css -->

| 속성 | 값 |
|------|-----|
| Transition | `200ms ease` (추정) |
| Overlay fade | 오버레이 어둡게 변환 via `--f-color-overlay` |

---

## 11. Grid / Layout
<!-- SOURCE: css -->

- Full-viewport hero (100vw × 100vh)
- 섹션 배경 전환 — 다크/라이트 교차
- 텍스트는 주로 좌측 또는 하단 오버레이 배치

---

## 12. Components
<!-- SOURCE: css -->

**버튼**
- Pill shape (`border-radius: 9999px`)
- Primary: 레드 그라디언트 background
- Secondary: 테두리만
- Focus: 노란색 아웃라인 (`#F6E500`)

**카드 / 이미지**
- 0 border-radius
- 다크 그라디언트 오버레이

**그라디언트 오버레이**
- Hero 이미지 위 `--f-color-gradient-shadow-light` 적용

---

## 13. Dark/Light Mode
<!-- SOURCE: manual -->

Ferrari는 **기본 다크 모드** 사이트다. 라이트 모드 섹션은 `--f-color-background-0` (white)을 배경으로 사용하는 컨텐츠 섹션에서만 등장한다. 토글 없음.

---

## 14. Drop-in CSS
<!-- SOURCE: css -->

```css
/* Ferrari Design System — insane-design */
:root {
  /* Brand */
  --f-color-accent-100: #DA291C;
  --f-color-accent-90: #B01E0A;
  --f-color-accent-80: #9D2211;
  --f-color-gradient-red: linear-gradient(180deg, #a00c01, #da291c 64%);

  /* Neutral */
  --f-color-global-black: #181818;
  --f-color-black-90: #303030;
  --f-color-black-60: #666;
  --f-color-black-55: #969696;
  --f-color-black-50: #8F8F8F;
  --f-color-black-20: #D2D2D2;
  --f-color-black-10: #F7F7F7;
  --f-color-global-white: #FFF;

  /* Background */
  --f-color-background-0: var(--f-color-global-white);
  --f-color-background-10: #EBEBEB;

  /* Accent */
  --f-color-yellow: #F6E500;
  --f-color-focus: var(--f-color-yellow);
  --f-color-accessible-info: #4C98B9;
  --f-color-accessible-success: #03904A;
  --f-color-accessible-warning: #F13A2C;

  /* Gradient */
  --f-color-gradient-dark-grey: linear-gradient(180deg, #3c3c3c, #030303 64%);
  --f-color-gradient-shadow-dark: linear-gradient(90deg, #121212, #161616);
  --f-color-gradient-shadow-light: linear-gradient(180deg, hsla(0,0%,9%,0), hsla(0,0%,9%,.85));

  /* Spacing */
  --f-space-xxxs: 4px;
  --f-space-xxs: 8px;
  --f-space-xs: 16px;
  --f-space-s: 24px;
  --f-space-m: 32px;
  --f-space-l: 48px;
  --f-space-xl: 64px;
  --f-space-xxl: 96px;
  --f-space-super: 128px;

  /* Radius */
  --f-radius-full: 9999px;

  /* Shadow */
  --f-shadow-small: 0px 4px 8px 0px rgba(0,0,0,.1);
  --f-color-overlay: rgba(0,0,0,.3);
  --f-color-overlay-darker: hsla(0,0%,7%,.8);

  /* Font */
  --f-ferrari-font: "FerrariSans";
}
```

---

## 15. Tailwind Config
<!-- SOURCE: css -->

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        ferrari: {
          red: '#DA291C',
          red90: '#B01E0A',
          red80: '#9D2211',
          black: '#181818',
          grey90: '#303030',
          grey60: '#666',
          grey50: '#8F8F8F',
          grey20: '#D2D2D2',
          grey10: '#F7F7F7',
          yellow: '#F6E500',
        },
      },
      fontFamily: {
        ferrari: ['"FerrariSans"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        pill: '9999px',
      },
      spacing: {
        'xxxs': '4px',
        'xxs': '8px',
        'xs': '16px',
        's': '24px',
        'm': '32px',
        'l': '48px',
        'xl': '64px',
        'xxl': '96px',
        'super': '128px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

**이 사이트에서 가장 흔한 실수 하나:**

> **DON'T**: 브랜드 레드 `#DA291C`를 배경색으로 사용하는 것.
>
> Ferrari는 레드를 **그라디언트 포인트와 소형 요소**에만 사용한다. 레드 배경 섹션을 만들면 "싸구려 이탈리아 레스토랑" 느낌이 된다.
>
> **DO**: 레드는 `linear-gradient(180deg, #a00c01, #da291c 64%)` 형태의 그라디언트 버튼과 accent line에만. 배경은 항상 `#181818` 또는 `#fff`.
