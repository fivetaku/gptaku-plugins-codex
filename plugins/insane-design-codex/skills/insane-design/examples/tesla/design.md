---
schema_version: 3.1
slug: tesla
service_name: Tesla
site_url: https://www.tesla.com
fetched_at: 2026-04-23
default_theme: light
brand_color: "#171a20"
primary_font: Blender TSL
font_weight_normal: 400
token_prefix: --tds-

bold_direction: "Cinematic Tech Minimalism"
aesthetic_category: "Premium EV / Tech"
signature_element: full_bleed_video_hero
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Tesla (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Tesla 웹사이트는 **"시네마틱 전체화면 영상 위에 얹힌 미니멀한 텍스트"**가 정체성이다. 영상이나 사진이 100vw × 100vh로 채우고, 그 위에 헤드라인과 두 개의 CTA만 올려둔다. 사용자는 스크롤할수록 차량이 마치 쇼룸에서 등장하듯 연출된다.

색상 전략은 **"짙은 근-검정 + 순백 + 파랑 CTA"**다. `--tds-color--grey10: #171a20`이 Tesla의 시그니처 다크 베이스다. 이 색은 배경이 아니라 텍스트와 UI에 주로 쓰이고, 실제 히어로 배경은 영상/사진이 100% 채운다. 흰색 텍스트가 어두운 이미지 위에, 검정 텍스트가 밝은 이미지 위에 자동 전환된다. 파란색 `#3e6ae1` 계열은 링크와 포커스 상태에 사용된다.

타이포그래피는 **독점 서체 `Blender TSL` (디스플레이) + `CT Speed` (모노/스피도미터)** 시스템이다. 다국어를 위해 각 언어별 폴백이 CSS 변수로 정밀하게 정의되어 있다 (`--tcl-font-family-korean-blender`, `--tcl-font-family-chinese-simplified-blender` 등). 한국어 폴백은 `"Noto Sans KR"`.

시스템 복잡도는 **952개 CSS custom properties**로 엔터프라이즈급이다. `--tds-size-*` 8px 기반 스페이싱, `--tds-border-radius: 4px` 통일 라디우스, `--tds-box-shadow--small/medium/large` 3단계 그림자 체계가 정밀하게 설계되어 있다.

### Key Characteristics

- 시그니처 다크 `#171a20` — Tesla 고유 near-black (순수 #000이 아님)
- 전체화면 영상/이미지 히어로 — 스크롤 연동 연출
- 독점 서체 Blender TSL + CT Speed (폴백: Helvetica Neue, Noto Sans)
- `--tds-` 네임스페이스 952개 토큰의 완전한 Design System

---

## 01. Quick Start
<!-- SOURCE: css -->

> 5분 안에 Tesla처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + near-black */
body {
  font-family: "Blender TSL", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  color: #171a20;
  background: #fff;
}

/* 2. 히어로: 전체화면 + 텍스트 오버레이 */
.hero {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
}
.hero-text {
  position: absolute;
  bottom: 25%;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  color: #fff;
}

/* 3. 버튼 시스템 */
.btn {
  border-radius: 4px;
  padding: 12px 32px;
  font-weight: 500;
}
.btn-primary { background: #171a20; color: #fff; }
.btn-secondary { background: rgba(255,255,255,0.65); color: #171a20; }
```

---

## 02. Provenance
<!-- SOURCE: auto -->

| 항목 | 값 |
|------|-----|
| Source URL | `https://www.tesla.com` |
| CSS 파일 | `css_8Ql29l2K...css` (756KB), `css_I3wVnI...css` (41KB), `css_SePQCI...css` (18KB) |
| 총 CSS | ~816,775 chars |
| 수집일 | 2026-04-23 |
| 수집 방법 | curl_cffi (chrome impersonation) |

---

## 03. Tech Stack
<!-- SOURCE: html+css -->

| 항목 | 감지 값 |
|------|---------|
| Framework | Drupal (`_flysystem/s3` URL 패턴) |
| CSS 방식 | CSS Custom Properties (`--tds-` prefix, 952개) |
| 토큰 네임스페이스 | `--tds-color-*`, `--tds-size-*`, `--tds-border-radius-*`, `--tds-box-shadow-*` |
| 컴포넌트 prefix | `--tcl-` (Tesla Component Library) |
| 애니메이션 | `--tds-animation-bezier-base: cubic-bezier(0.5,0,0,0.75)` |

---

## 04. Font Stack
<!-- SOURCE: css -->

| 역할 | 폰트 | 폴백 |
|------|------|------|
| Display / UI | `Blender TSL` | `Helvetica Neue`, Helvetica, Arial, sans-serif |
| Monospace / Speedo | `CT Speed` | Noto Sans Mono, monospace |
| 한국어 | `Blender TSL` + `Noto Sans KR` | — |
| 중국어(간체) | `Blender TSL` + `PingFang SC` | Microsoft YaHei |
| 일본어 | `Blender TSL` + `AXIS Font Japanese W55` | — |

```css
:root {
  --tcl-font-family-base-blender: "Blender TSL";
  --tcl-font-family-base-ct-speed: "CT Speed";
  --tcl-font-family-korean-blender: var(--tcl-font-family-base-blender), "Noto Sans KR";
}
```

---

## 05. Typography Scale
<!-- SOURCE: css -->

Tesla의 타이포그래피는 CSS 변수로 완전히 제어된다. 일반적인 h1-h6보다 맥락별 스케일을 사용한다.

| 레벨 | 용도 | 폰트 |
|------|------|------|
| Hero Headline | 차량명, 슬로건 (대형) | Blender TSL, 100 weight |
| Section Title | 섹션 헤딩 | Blender TSL, 500 |
| Body | 설명 텍스트 | Blender TSL, 400 |
| Caption | 법적 고지, 스펙 | Blender TSL, 300 |
| Speed/Mono | 0-100 km/h 수치 등 | CT Speed |

---

## 06. Colors
<!-- SOURCE: css -->

### Near-Black (Tesla Signature)

| 토큰 | 값 |
|------|-----|
| `--tds-color--grey10` | `#171a20` ← Tesla 시그니처 near-black |
| `--tds-color--grey15` | `#222` |
| `--tds-color--grey20` | `#393c41` |
| `--tds-color--grey25` | `#444` |
| `--tds-color--grey30` | `#5c5e62` |

### Gray Ramp

| 토큰 | 값 |
|------|-----|
| `--tds-color--grey35` | `#8e8e8e` |
| `--tds-color--grey40` | `#a2a3a5` |
| `--tds-color--grey45` | `#bbb` |
| `--tds-color--grey50` | `#d0d1d2` |

### White & Background

| 토큰 | 값 |
|------|-----|
| `--tds-color--black` | `#000` |
| `--tds-color-white` | `#fff` (추정) |
| `--tds-color--white` | `#fff` |

### Blue (Link / CTA)

| 토큰 | 값 |
|------|-----|
| `--tds-color--blue10` | `#2e4994` |
| `--tds-color--blue20` | `#3457b1` |
| `--tds-color--blue30` | `#3e6ae1` |

### Semantic

| 토큰 | 값 |
|------|-----|
| `--tds-color--green` | `#12bb00` |
| `--tds-color--error` | `var(--tds-color-red-10)` |

---

## 07. Spacing
<!-- SOURCE: css -->

8px 기반의 `--tds-size-*` 스케일.

| 토큰 | 값 |
|------|-----|
| `--tds-size-half` | `4px` |
| `--tds-size-base` | `8px` |
| `--tds-size-base-plus` | `12px` |
| `--tds-size-2x` | `16px` |
| `--tds-size-3x` | `24px` |
| `--tds-size-4x` | `32px` |
| `--tds-size-5x` | `40px` |
| `--tds-size-6x` | `48px` |
| `--tds-size-7x` | `56px` |
| `--tds-size-8x` | `64px` |
| `--tds-size-9x` | `72px` |

---

## 08. Border Radius
<!-- SOURCE: css -->

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--tds-border-radius` | `4px` | 기본 컴포넌트 |
| `--tds-border-radius--card` | `4px` | 카드 |
| `--tds-border-radius--pill` | `4px` | 버튼 (pill이지만 4px — 미묘한 라운딩) |
| `--tds-border-radius--circle` | `100%` | 아이콘, 아바타 |
| `--tds-modal-border-radius` | `var(--tds-size--1x)` | 모달 |

Tesla는 **4px 통일**을 원칙으로 한다. 대부분의 요소가 동일한 4px 라디우스를 공유한다.

---

## 09. Shadows
<!-- SOURCE: css -->

| 토큰 | 값 |
|------|-----|
| `--tds-box-shadow--small` | `0 4px 8px 0 #00000014` |
| `--tds-box-shadow--medium` | `0 8px 16px 0 #0000001f` |
| `--tds-box-shadow--large` | `0 8px 16px 0 #00000029` |
| `--tds-box-shadow--large-reverse` | `0 -8px 16px 0 #00000029` |
| `--tds-box-shadow--off` | `0 0 0 0 #0000` |

---

## 10. Animation
<!-- SOURCE: css -->

| 토큰 | 값 |
|------|-----|
| `--tds-animation-bezier-base` | `cubic-bezier(0.5,0,0,0.75)` |

Tesla의 트랜지션은 이 single bezier 기반. 부드럽지만 약간 탄력 있는 감.

---

## 11. Grid / Layout
<!-- SOURCE: manual -->

- 전체화면(100vw × 100vh) hero — 영상/이미지 배경
- 스크롤당 1 섹션 구조 (snap scrolling 유사)
- 텍스트는 hero 하단 중앙 정렬
- CTA 버튼 2개: primary(다크) + secondary(반투명 흰색)

---

## 12. Components
<!-- SOURCE: css -->

**버튼**
- Border-radius: 4px (pill보다 각진 느낌)
- Primary: `#171a20` 배경 + 흰색 텍스트
- Secondary: `rgba(255,255,255,0.65)` 배경 + 다크 텍스트 (반투명)
- 패딩: `--tcl-button--padding-inline: unset` (컨텍스트 의존)

**카드**
- `--tds-card--background-color: var(--tds-theme-background-container)`
- `--tds-card--border-radius: 4px`
- shadow: `--tds-box-shadow--small`

**모달**
- `--tds-modal-border-radius: var(--tds-size--1x)` (8px)

---

## 13. Dark/Light Mode
<!-- SOURCE: css -->

Tesla는 `--tds-theme-*` 계열 토큰으로 테마를 지원한다.

| 테마 토큰 | 역할 |
|---------|------|
| `--tds-theme-primary` | 주 컬러 (다크=흰, 라이트=검정) |
| `--tds-theme-foreground` | 전경색 |
| `--tds-theme-foreground-high-contrast` | 고대비 전경 |
| `--tds-theme-background-container` | 컨테이너 배경 |

히어로 섹션은 어두운 배경(영상)에 흰 텍스트, 컨텐츠 섹션은 밝은 배경에 `#171a20` 텍스트.

---

## 14. Drop-in CSS
<!-- SOURCE: css -->

```css
/* Tesla Design System (TDS) — insane-design */
:root {
  /* Near-Black */
  --tds-color--grey10: #171a20;
  --tds-color--grey15: #222;
  --tds-color--grey20: #393c41;
  --tds-color--grey25: #444;
  --tds-color--grey30: #5c5e62;
  --tds-color--grey35: #8e8e8e;
  --tds-color--grey40: #a2a3a5;
  --tds-color--grey45: #bbb;
  --tds-color--grey50: #d0d1d2;
  --tds-color--black: #000;
  --tds-color--white: #fff;

  /* Blue */
  --tds-color--blue10: #2e4994;
  --tds-color--blue20: #3457b1;
  --tds-color--blue30: #3e6ae1;

  /* Semantic */
  --tds-color--green: #12bb00;

  /* Spacing (8px base) */
  --tds-size-half: 4px;
  --tds-size-base: 8px;
  --tds-size-base-plus: 12px;
  --tds-size-2x: 16px;
  --tds-size-3x: 24px;
  --tds-size-4x: 32px;
  --tds-size-5x: 40px;
  --tds-size-6x: 48px;
  --tds-size-7x: 56px;
  --tds-size-8x: 64px;
  --tds-size-9x: 72px;

  /* Border Radius */
  --tds-border-radius: 4px;
  --tds-border-radius--card: 4px;
  --tds-border-radius--pill: 4px;
  --tds-border-radius--circle: 100%;
  --tds-modal-border-radius: 8px;

  /* Shadows */
  --tds-box-shadow--small: 0 4px 8px 0 #00000014;
  --tds-box-shadow--medium: 0 8px 16px 0 #0000001f;
  --tds-box-shadow--large: 0 8px 16px 0 #00000029;
  --tds-box-shadow--off: 0 0 0 0 #0000;

  /* Animation */
  --tds-animation-bezier-base: cubic-bezier(0.5,0,0,0.75);

  /* Opacity */
  --tds-ui-opacity-70: 0.7;
  --tds-ui-opacity-50: 0.5;
  --tds-ui-opacity-30: 0.3;

  /* Font */
  --tcl-font-family-base-blender: "Blender TSL";
  --tcl-font-family-base-ct-speed: "CT Speed";
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
        tesla: {
          dark: '#171a20',
          grey20: '#393c41',
          grey30: '#5c5e62',
          grey40: '#a2a3a5',
          grey50: '#d0d1d2',
          blue: '#3e6ae1',
          green: '#12bb00',
        },
      },
      fontFamily: {
        tesla: ['"Blender TSL"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
        speed: ['"CT Speed"', '"Noto Sans Mono"', 'monospace'],
      },
      borderRadius: {
        tds: '4px',
      },
      spacing: {
        'tds-half': '4px',
        'tds-1': '8px',
        'tds-2': '16px',
        'tds-3': '24px',
        'tds-4': '32px',
        'tds-6': '48px',
        'tds-8': '64px',
      },
      boxShadow: {
        'tds-sm': '0 4px 8px 0 rgba(0,0,0,0.08)',
        'tds-md': '0 8px 16px 0 rgba(0,0,0,0.12)',
        'tds-lg': '0 8px 16px 0 rgba(0,0,0,0.16)',
      },
      transitionTimingFunction: {
        'tesla': 'cubic-bezier(0.5,0,0,0.75)',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

**이 사이트에서 가장 흔한 실수 하나:**

> **DON'T**: Tesla 다크 컬러로 `#000000` 또는 `#1a1a1a` 같은 순수 검정 계열을 쓰는 것.
>
> Tesla의 시그니처 다크는 `#171a20` — 약간의 파랑기가 섞인 near-black이다. 이 0.3% 차이가 Tesla 느낌의 핵심이다.
>
> **DO**: 다크 베이스는 반드시 `#171a20`. Tailwind라면 `bg-[#171a20]`.
