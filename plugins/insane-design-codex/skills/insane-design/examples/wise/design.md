---
slug: wise
service_name: Wise
site_url: https://wise.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#9FE870"
primary_font: Wise Sans
font_weight_normal: 400
token_prefix: --color-*
---

# DESIGN.md — Wise (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Wise처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'Wise Sans', Inter, Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #0E0F0C; }
body { background: var(--bg); color: var(--fg); }

/* 3. 라임 그린 accent */
:root { --color-interactive-accent: #9FE870; }
```

**절대 하지 말아야 할 것 하나**: `VideoJS`를 Wise의 브랜드 폰트로 착각하는 것. VideoJS는 미디어 플레이어 아이콘 폰트로 CSS에서 49회 등장하지만, 실제 브랜드 폰트는 `Wise Sans`이고 본문은 `Inter`다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://wise.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes |
| CSS files | 자체 디자인 시스템 + VideoJS 플레이어 CSS |
| Token prefix | `--color-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React (글로벌 핀테크)
- **Design system**: 자체 DS — `--color-interactive-*`, `--color-content-*`, `--color-sentiment-*` 토큰
- **CSS architecture**: 시맨틱 토큰 체계 — content / interactive / sentiment / background 계층
- **Default theme**: light (흰 배경, near-black 텍스트)
- **Font loading**: 자체 호스트 `Wise Sans` + `Inter` (Google Fonts), `Averta` (레거시)
- **Canonical anchor**: `#9FE870` — `--color-interactive-accent` 다크 모드값, Wise의 시각적 시그니처 라임 그린

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Brand font**: `Wise Sans` (4회 — 헤드라인, 브랜드 텍스트 전용)
- **Body font**: `Inter` (12회 — 본문, UI 텍스트)
- **Legacy**: `Averta` (3회 — 구버전 잔류)
- **Weight system**: 100, 400, 500, 600, 700

```css
/* 헤드라인 */
h1, h2 {
  font-family: 'Wise Sans', Inter, Helvetica, Arial, sans-serif;
  font-weight: 600;
}

/* 본문 */
body {
  font-family: Inter, Helvetica, Arial, sans-serif;
  font-weight: 400;
}
```

> **주의**: `VideoJS`(49회)는 미디어 플레이어 아이콘 폰트로 브랜드 폰트와 무관. `Wise Sans`는 Wise 전용 커스텀 폰트 — 오픈소스 대체재: `Inter` 또는 `DM Sans`.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight | 폰트 |
|---|---|---|---|
| Hero Display | clamp(36px, 5vw, 64px) | 600–700 | Wise Sans |
| Section Heading | 24px–36px | 600 | Wise Sans |
| Card Title | 18px–22px | 600 | Inter |
| Body | 14px–16px | 400 | Inter |
| Caption | 12px–13px | 400 | Inter |
| Button | 15px–16px | 600 | Inter |
| Label | 12px | 600 | Inter |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand (라임 그린 — Wise 시그니처)

| Token | Hex | 역할 |
|---|---|---|
| --color-interactive-accent | `#9FE870` | 라임 그린 CTA (다크 모드 / 브랜드 시그니처) |
| --color-interactive-accent-hover | `#80E142` | hover 상태 |
| --color-interactive-accent-active | `#65CF21` | active 상태 |

### Light Mode Interactive

| Token | Hex | 역할 |
|---|---|---|
| --color-interactive-primary | `#163300` | 라이트 모드 CTA 버튼 (다크 그린) |
| --color-interactive-accent | `#00A2DD` | 라이트 모드 accent (시안 블루) |
| --color-content-accent | `#0097C7` | 콘텐츠 accent 링크 |

### Neutrals

| Hex | 역할 |
|---|---|
| `#0E0F0C` | 메인 텍스트 (near-black, 약간 그린 기운) |
| `#FFFFFF` | 기본 배경 |
| `#37517E` | 보조 텍스트 (slate blue) |

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
| Button | 40px (pill shape — Wise 특유) |
| Card | 12px–16px |
| Input | 8px |
| Badge | 999px |
| Modal | 16px |

> Wise 버튼의 pill radius — 핀테크 브랜드 중 가장 독특한 특징. `border-radius: 40px` 이상의 완전 rounded.

---

## 09. Shadows
<!-- SOURCE: manual -->

| 레이어 | CSS |
|---|---|
| Card | `box-shadow: 0 4px 16px rgba(0,0,0,.08)` |
| Dropdown | `box-shadow: 0 8px 24px rgba(0,0,0,.12)` |
| Modal | `box-shadow: 0 16px 48px rgba(0,0,0,.16)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| Button hover | 150ms | ease |
| Card hover | 200ms | ease-out |
| Page transition | 300ms | ease-in-out |
| Modal open | 250ms | ease-out |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 큰 헤드라인 + 라임 그린 CTA pill 버튼, 흰 배경
- **환율 계산기**: 히어로 내 라이브 환율 위젯 — 브랜드 핵심 기능 노출
- **Feature 섹션**: 이미지 + 텍스트 2-column 교차
- **컨테이너**: `max-width: 1200px; margin: 0 auto; padding: 0 24px`
- **Nav**: sticky 흰 배경, 라임 그린 CTA 버튼 (pill)

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button (Pill)

```css
.btn-primary {
  background: #163300;   /* 라이트 모드 — 다크 그린 */
  color: #9FE870;        /* 라임 그린 텍스트 */
  border: none;
  border-radius: 40px;   /* Wise pill — 완전 rounded */
  padding: 14px 28px;
  font-family: Inter, sans-serif;
  font-weight: 600;
  font-size: 16px;
  transition: all 150ms ease;
}
.btn-primary:hover {
  background: #0D1F00;
}
```

### Dark Mode CTA Button

```css
/* 다크 모드 — 라임 그린 배경 */
.btn-primary--dark {
  background: #9FE870;
  color: #163300;        /* 다크 그린 텍스트 */
  border-radius: 40px;
}
```

### Exchange Rate Widget

```css
.rate-widget {
  background: #FFFFFF;
  border: 1px solid #E0E0E0;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 16px rgba(0,0,0,.08);
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 투명성, 공정함. "Send money abroad, simply."
- **수치**: 환율 실시간 표시, 수수료 명확. "0.42% fee"
- **CTA**: "Send money", "Get started", "See the rate" — 행동 명확
- **어조**: 친근하고 명확, 과장 없음 — 은행에 대한 솔직한 대안

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Wise Design System — Drop-in */
:root {
  --color-interactive-primary:  #163300;   /* 라이트 CTA */
  --color-interactive-accent:   #9FE870;   /* 라임 그린 시그니처 */
  --color-content-accent:       #0097C7;   /* 링크 */

  --color-fg-primary:   #0E0F0C;
  --color-fg-secondary: #37517E;
  --color-bg-page:      #FFFFFF;

  --font-brand: 'Wise Sans', Inter, Helvetica, Arial, sans-serif;
  --font-body:  Inter, Helvetica, Arial, sans-serif;
}

body {
  font-family: var(--font-body);
  font-weight: 400;
  background: var(--color-bg-page);
  color: var(--color-fg-primary);
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
        wise: {
          lime:       '#9FE870',
          'lime-hover': '#80E142',
          green:      '#163300',
          'green-dark': '#0D1F00',
          cyan:       '#00A2DD',
          'cyan-dark': '#0097C7',
          'text-dark': '#0E0F0C',
          'text-slate': '#37517E',
        },
      },
      fontFamily: {
        brand: ['Wise Sans', 'Inter', 'Helvetica', 'Arial', 'sans-serif'],
        sans:  ['Inter', 'Helvetica', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        btn:  '40px',    /* Wise pill 버튼 */
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

- `#9FE870` 라임 그린을 브랜드 시그니처로 사용 — Wise의 시각적 아이덴티티
- 버튼은 반드시 pill shape (`border-radius: 40px`) — Wise만의 차별화 포인트
- `Wise Sans`로 헤드라인 — 브랜드 폰트 (없으면 Inter 대체)
- 환율·수수료 수치를 전면에 — 투명성이 브랜드 가치
- 라이트 모드 CTA: 다크 그린 `#163300` 배경 + 라임 그린 텍스트

### DON'T

- `VideoJS` 폰트를 UI 텍스트에 사용 — 미디어 아이콘 폰트
- 버튼에 작은 radius — Wise의 pill은 정체성
- 일반 그린(`#00FF00` 등)으로 `#9FE870` 대체 — 라임 그린의 절제된 밝기가 핵심
- 수수료를 숨기는 카피 — Wise 브랜드 가치에 반함

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| VideoJS가 주폰트 | VideoJS는 미디어 아이콘 폰트. 브랜드는 Wise Sans |
| 버튼이 일반 rounded | pill `border-radius: 40px` — Wise만의 시그니처 |
| 브랜드가 파랑 | 시안(#00A2DD)은 링크 accent. 브랜드는 라임 그린 |
