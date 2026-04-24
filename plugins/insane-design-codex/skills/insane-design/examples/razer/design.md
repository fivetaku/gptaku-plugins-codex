---
slug: razer
service_name: Razer
site_url: https://www.razer.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#44D62C"
primary_font: RazerF5
font_weight_normal: 400
token_prefix: --cx-g-color-*, --primary
---

# DESIGN.md — Razer (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Razer처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: RazerF5, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 레이저 그린 */
:root { --brand: #44D62C; }
```

**절대 하지 말아야 할 것 하나**: 레이저 그린을 다른 그린으로 대체하는 것. `#44D62C`는 전기 네온 그린 — 라임/민트/에메랄드 그린과 전혀 다르다. 일반 `#00FF00` 순수 그린보다 약간 어둡고 황색 기운이 있다. 이 미묘한 차이가 게이밍 브랜드 정체성의 전부다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.razer.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes (Angular SSR / SAP Spartacus) |
| CSS files | 다수 — SAP Cx 기반 + 커스텀 레이어 |
| Token prefix | `--cx-*` (SAP Commerce), `--primary` (Razer 전용) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Angular (SAP Spartacus — SAP Commerce Cloud 기반)
- **Design system**: 하이브리드 — SAP CX 기본 위에 Razer 브랜드 오버레이
- **CSS architecture**: `--cx-*` SAP 토큰 + `--primary` Razer 토큰 중첩
- **Class naming**: `_ngcontent-ng-*` Angular 스코프 + `razer-mega-menu` 커스텀
- **Default theme**: dark (순수 검정 배경, 레이저 그린 액센트)
- **Font loading**: 자체 호스트 `RazerF5` + Google Fonts `Roboto`, `Open Sans`
- **Canonical anchor**: `#44D62C` — `--primary`, `--cx-g-color-primary`, `--cx-color-primary` 세 토큰 모두 동일 값

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary/Brand font**: `RazerF5` (Razer 전용 커스텀 폰트, 30+회 사용)
- **Body font**: `Roboto` (54회 — 본문, UI 텍스트)
- **Secondary**: `Open Sans` (40회)
- **Weight system**: 100, 300, 400, 500, 600, 700, 900

```css
/* 메인 UI */
body {
  font-family: RazerF5, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  font-weight: 400;
}

/* 본문 텍스트 */
.body-text {
  font-family: Roboto, sans-serif;
  font-weight: 400;
}
```

> **주의**: `RazerF5`는 Razer 전용 커스텀 폰트. 대체재로는 `Barlow Condensed` 또는 `Rajdhani`가 유사한 게이밍 feel.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight | 폰트 |
|---|---|---|---|
| Hero / Game Title | clamp(48px, 8vw, 96px) | 700–900 | RazerF5 |
| Product Name | 32px–48px | 700 | RazerF5 |
| Section Heading | 24px–32px | 600–700 | RazerF5 |
| Body | 14px–16px | 400 | Roboto |
| Spec / Tech | 13px–14px | 300–400 | Roboto |
| Caption | 12px | 300 | Open Sans |
| Menu | 16px | 400 | RazerF5 |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand (레이저 그린)

| Token | Hex | 역할 |
|---|---|---|
| --primary | `#44D62C` | Razer 브랜드 그린 (명시) |
| --cx-g-color-primary | `#44D62C` | CX global 브랜드 |
| --cx-color-primary | `#44D62C` | CX 컴포넌트 primary |

### SAP CX 상태 컬러

| Token | Hex | 역할 |
|---|---|---|
| --cx-color-primary (dark context) | `#6BD3FF` | 다크 모드 primary (e-commerce) |
| --cx-color-primary (light) | `#004CCB` | 라이트 컨텍스트 |
| --cx-color-primary (medium) | `#1F7BC0` | 중간 컨텍스트 |

### Neutrals

| Hex | 역할 |
|---|---|
| `#000000` | 기본 배경 |
| `#EEEEEE` | 보조 텍스트, 링크 |
| `#BBBBBB` | 메가메뉴 링크 |
| `#FFFFFF` | 액티브 텍스트 |

---

## 07. Spacing
<!-- SOURCE: manual -->

| Step | Value |
|---|---|
| xs | 4px |
| sm | 8px |
| md | 16px |
| lg | 24px |
| xl | 40px |
| 2xl | 64px |
| 3xl | 96px |

---

## 08. Radius
<!-- SOURCE: manual -->

| 역할 | Radius |
|---|---|
| Button | 2px–4px (샤프) |
| Card | 4px |
| Input | 2px |
| Badge | 999px |

> 게이밍 하드웨어 브랜드 — 각진 엣지가 정체성.

---

## 09. Shadows
<!-- SOURCE: manual -->

| 레이어 | CSS |
|---|---|
| Product card | `box-shadow: 0 0 30px rgba(68,214,44,.15)` (그린 글로우) |
| Button hover | `box-shadow: 0 0 20px rgba(68,214,44,.4)` |
| Modal | `box-shadow: 0 8px 32px rgba(0,0,0,.6)` |

> 레이저 특유의 그린 글로우 효과 — `rgba(68,214,44,*)` 활용.

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| Button hover glow | 200ms | ease |
| Menu open | 250ms | ease-out |
| Image load | 300ms | ease |
| Page transition | 400ms | ease-in-out |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 풀 블리드 제품 이미지, 검정 배경, 레이저 그린 텍스트 포인트
- **메가 메뉴**: `razer-mega-menu` — 검정 배경 + BBB 링크 텍스트 + 그린 active
- **제품 그리드**: 다크 카드, 제품 이미지 중심
- **컨테이너**: `max-width: 1280px; margin: 0 auto`
- **Nav**: 투명 → 스크롤 시 검정 불투명

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button

```css
.btn-primary {
  background: #44D62C;
  color: #000000;
  border: none;
  border-radius: 2px;
  padding: 12px 28px;
  font-family: RazerF5, sans-serif;
  font-weight: 600;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  transition: all 200ms ease;
}
.btn-primary:hover {
  box-shadow: 0 0 20px rgba(68,214,44,.4);
}
```

### Mega Menu Link

```css
.razer-mega-menu > ul > li > a,
.razer-mega-menu > ul > li > button {
  color: #BBB;  /* 비활성 링크 */
  font-family: RazerF5;
  font-size: 16px;
  font-weight: 400;
}
.razer-mega-menu > ul > li.active > a {
  color: #FFFFFF;
}
.razer-mega-menu .submenu li.active > button::after {
  color: #44D62C;  /* 서브메뉴 활성 표시 */
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 파워풀, 기술 우월성. "ULTIMATE PERFORMANCE."
- **스펙**: 수치 강조. "8K UHD Webcam", "4000Hz Polling Rate"
- **CTA**: "SHOP NOW", "CONFIGURE" — 대문자
- **어조**: 게이밍 커뮤니티 언어, 공격적 기술 자신감

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Razer Design System — Drop-in */
:root {
  --primary:             #44D62C;
  --cx-g-color-primary:  #44D62C;
  --cx-color-primary:    #44D62C;

  --color-bg:     #000000;
  --color-fg:     #FFFFFF;
  --color-link:   #EEEEEE;
  --color-muted:  #BBBBBB;

  --font-brand: "RazerF5", "Helvetica Neue", Arial, sans-serif;
  --font-body:  "Roboto", sans-serif;
}

body {
  font-family: var(--font-brand);
  font-weight: 400;
  background: var(--color-bg);
  color: var(--color-fg);
  -webkit-font-smoothing: antialiased;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        razer: {
          green:  '#44D62C',
          black:  '#000000',
          white:  '#FFFFFF',
          link:   '#EEEEEE',
          subtle: '#BBBBBB',
        },
      },
      fontFamily: {
        razer:  ['RazerF5', 'Helvetica Neue', 'Arial', 'sans-serif'],
        roboto: ['Roboto', 'sans-serif'],
      },
      boxShadow: {
        'glow-sm': '0 0 20px rgba(68,214,44,.4)',
        'glow-lg': '0 0 30px rgba(68,214,44,.15)',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- `#44D62C` 레이저 그린을 액센트로 사용
- 버튼 텍스트는 `#000000` — 그린 배경 위 검정
- `RazerF5` 폰트로 헤드라인 — 브랜드 정체성
- 그린 글로우 이펙트: `rgba(68,214,44,.4)` box-shadow
- 대문자 텍스트 "SHOP NOW" — 게이밍 컨벤션
- 검정 배경에 그린 포인트 — 절대 반전시키지 않음

### DON'T

- 라임/민트/에메랄드로 `#44D62C` 대체
- 흰 배경에 레이저 그린 — 다크 배경이 필수 컨텍스트
- 버튼 텍스트를 흰색으로 — 그린 배경 위는 검정
- 큰 border-radius — 게이밍은 샤프 엣지
- 소문자 카피 — Razer는 대문자

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| 일반 그린으로 대체 가능 | `#44D62C`는 전기 네온 — 다른 그린과 전혀 다름 |
| 라이트 테마 존재 | 마케팅 사이트는 순수 다크 |
| 버튼 텍스트 흰색 | 그린 배경에는 검정 텍스트 |
