---
slug: revolut
service_name: Revolut
site_url: https://www.revolut.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#4F55F1"
primary_font: Aeonik Pro
font_weight_normal: 400
token_prefix: --rui-*
---

# DESIGN.md — Revolut (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Revolut처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'Aeonik Pro', Inter, -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #191C1F; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 인디고 */
:root { --rui-color-accent: #4F55F1; }
```

**절대 하지 말아야 할 것 하나**: 요금제별 컬러(보라, 핑크, 골드)를 Revolut의 브랜드 컬러로 착각하는 것. `#4F55F1` 인디고는 기본(Standard) 플랜과 메인 UI에 사용되는 canonical 브랜드 컬러다. 나머지 컬러들은 플랜 구분을 위한 마케팅 레이어다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.revolut.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes |
| CSS files | RUI (Revolut UI) 컴포넌트 라이브러리 |
| Token prefix | `--rui-*` (Revolut UI) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React
- **Design system**: RUI (Revolut UI) — `--rui-color-accent`, `--rui-color-action-*` 토큰 체계
- **CSS architecture**: 다중 테마 — 플랜별 accent 컬러 스위칭 + light/dark 컨텍스트
- **Class naming**: RUI 컴포넌트 클래스 (`rui-button`, `rui-plan-*` 등 추정)
- **Default theme**: light (흰 배경, 다크 그레이 텍스트, 인디고 accent)
- **Font loading**: 자체 호스트 `Aeonik Pro` (커스텀 라이선스) + `Inter` (Google Fonts)
- **Canonical anchor**: `#4F55F1` — `--rui-color-accent` 라이트 모드 첫 번째 값, Standard 플랜 기본

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Brand font**: `Aeonik Pro` (3회 — 헤드라인, UI 강조), `Aeonik Pro Capitalised` (1회 — 특수 타이틀)
- **Body font**: `Inter` (6회 — 본문, 인터페이스)
- **Weight system**: 400, 500, 600, 700, 900

```css
/* 헤드라인 */
h1, h2 {
  font-family: 'Aeonik Pro', Inter, sans-serif;
  font-weight: 700;
}

/* 본문 */
body {
  font-family: Inter, sans-serif;
  font-weight: 400;
}
```

> **주의**: `Aeonik Pro`는 Commercial Type의 유료 라이선스 폰트. 오픈소스 대체재: `Plus Jakarta Sans` 또는 `DM Sans`가 유사한 현대적 feel.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight | 폰트 |
|---|---|---|---|
| Hero Display | clamp(40px, 6vw, 72px) | 700–900 | Aeonik Pro |
| Section Heading | 28px–40px | 700 | Aeonik Pro |
| Card Title | 18px–22px | 600–700 | Aeonik Pro |
| Body | 15px–16px | 400 | Inter |
| Caption | 12px–13px | 400 | Inter |
| Button | 15px | 500–600 | Inter |
| Plan Badge | 11px–13px | 700 | Aeonik Pro Capitalised |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand (Standard / 기본 플랜)

| Token | Hex | 역할 |
|---|---|---|
| --rui-color-accent | `#4F55F1` | 기본 브랜드 인디고 (light 모드) |
| --rui-color-on-accent | `#FFFFFF` | accent 위 텍스트 |
| --rui-color-action-background | `#EDEEFD` | accent 연한 배경 |

### 플랜별 Accent (마케팅 레이어)

| Hex | 플랜 |
|---|---|
| `#9539F2` | Premium (보라) |
| `#F12587` | Metal (핑크) |
| `#DD7904` | Ultra / Gold |
| `#00B88B` | 녹색 계열 플랜 |
| `#667DFF` | 라이트 인디고 variant |

### 다크 모드 Accent

| Hex | 역할 |
|---|---|
| `#7F84F6` | 다크 모드 accent (연한 인디고) |
| `#A04DF4` | 다크 모드 Premium |
| `#F33B94` | 다크 모드 Metal |

### Neutrals

| Hex | 역할 |
|---|---|
| `#FFFFFF` | 기본 배경 |
| `#F4F4F4` | 보조 배경 |
| `#F7F7F7` | 카드 배경 |
| `#191C1F` | 메인 텍스트 |
| `#1C1C1E` | 진한 다크 |

---

## 07. Spacing
<!-- SOURCE: manual -->

| Step | Value |
|---|---|
| xs | 4px |
| sm | 8px |
| md | 16px |
| lg | 24px |
| xl | 32px |
| 2xl | 48px |
| 3xl | 64px |
| 4xl | 96px |

---

## 08. Radius
<!-- SOURCE: manual -->

| 역할 | Radius |
|---|---|
| Button | 8px–12px |
| Card | 12px–16px |
| Input | 8px |
| Plan Card | 16px–20px |
| Modal | 16px |
| Pill / Badge | 999px |

> 핀테크 브랜드 — 날카롭지도 너무 둥글지도 않은 중간 radius. 신뢰감과 현대성의 균형.

---

## 09. Shadows
<!-- SOURCE: manual -->

| 레이어 | CSS |
|---|---|
| Card | `box-shadow: 0 4px 16px rgba(0,0,0,.08)` |
| Dropdown | `box-shadow: 0 8px 24px rgba(0,0,0,.12)` |
| Modal | `box-shadow: 0 16px 48px rgba(0,0,0,.16)` |
| Plan card hover | `box-shadow: 0 8px 32px rgba(79,85,241,.15)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| Button hover | 150ms | ease |
| Card hover | 200ms | ease-out |
| Tab / Plan 전환 | 250ms | ease-in-out |
| Modal open | 300ms | ease-out |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 풀 블리드 + 텍스트 중앙, 흰 배경, 인디고 그라디언트 accent
- **플랜 카드**: 가로 스크롤 또는 그리드, 플랜별 accent 컬러 상단 바
- **Feature 섹션**: 이미지 + 텍스트 2-column, 번갈아 배치
- **컨테이너**: `max-width: 1200px; margin: 0 auto; padding: 0 24px`
- **Nav**: sticky 흰 배경, 인디고 CTA 버튼

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button

```css
.btn-primary {
  background: #4F55F1;
  color: #FFFFFF;
  border: none;
  border-radius: 10px;
  padding: 14px 24px;
  font-family: Inter, sans-serif;
  font-weight: 600;
  font-size: 15px;
  transition: all 150ms ease;
}
.btn-primary:hover {
  background: #3B41D9;
  box-shadow: 0 4px 16px rgba(79,85,241,.3);
}
```

### Plan Card

```css
.plan-card {
  background: #FFFFFF;
  border: 1px solid #EBEBF0;
  border-radius: 16px;
  padding: 24px;
  position: relative;
  overflow: hidden;
}
.plan-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: var(--rui-color-accent, #4F55F1);
}
```

### Accent Badge

```css
.badge-accent {
  background: #EDEEFD;
  color: #4F55F1;
  border-radius: 999px;
  padding: 4px 12px;
  font-size: 12px;
  font-weight: 600;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 자신감, 글로벌 금융. "Money without borders."
- **바디**: 투명성 강조, 수수료 언급. "No hidden fees."
- **CTA**: "Get started", "Open account", "Compare plans"
- **어조**: 모던, 신뢰, 글로벌 — 전통 은행의 반대

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Revolut Design System — Drop-in */
:root {
  --rui-color-accent:            #4F55F1;
  --rui-color-on-accent:         #FFFFFF;
  --rui-color-action-background: #EDEEFD;

  --color-bg:     #FFFFFF;
  --color-bg-alt: #F4F4F4;
  --color-fg:     #191C1F;
  --color-border: #EBEBF0;

  --font-brand: 'Aeonik Pro', Inter, -apple-system, sans-serif;
  --font-body:  Inter, -apple-system, sans-serif;

  --space-xs:  4px;
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  24px;
  --space-xl:  32px;
  --space-2xl: 48px;
}

body {
  font-family: var(--font-body);
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
        revolut: {
          indigo:  '#4F55F1',
          'indigo-dark': '#3B41D9',
          'indigo-bg':   '#EDEEFD',
          purple:  '#9539F2',
          pink:    '#F12587',
          gold:    '#DD7904',
        },
        neutral: {
          900: '#191C1F',
          800: '#1C1C1E',
          200: '#EBEBF0',
          100: '#F4F4F4',
          50:  '#F7F7F7',
        },
      },
      fontFamily: {
        brand: ['Aeonik Pro', 'Inter', '-apple-system', 'sans-serif'],
        sans:  ['Inter', '-apple-system', 'sans-serif'],
      },
      borderRadius: {
        btn:  '10px',
        card: '16px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- `#4F55F1` 인디고를 메인 CTA와 브랜드 accent에 사용
- `Aeonik Pro`로 헤드라인 — 신뢰감 있는 현대적 폰트
- 플랜 카드 상단에 플랜별 accent 컬러 바
- 충분한 white space — 핀테크 청결함
- 수수료 투명성 카피 — Revolut의 핵심 차별점

### DON'T

- 플랜별 컬러(보라, 핑크, 골드)를 메인 브랜드 컬러로 혼용
- 전통 은행처럼 보이는 과도한 그린/블루 — Revolut은 인디고
- 큰 serif 폰트 — Revolut은 sans-serif 현대성
- 다크 배경에 인디고 — light 모드가 primary

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| 요금제 색깔이 브랜드 컬러 | `#4F55F1` 인디고가 canonical 브랜드 |
| Revolut은 보라 브랜드 | 보라는 Premium 플랜 전용 |
| 다크 모드가 기본 | 라이트 모드가 마케팅 기본 |
