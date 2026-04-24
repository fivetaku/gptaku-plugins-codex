---
slug: robinhood
service_name: Robinhood
site_url: https://robinhood.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#CCFF00"
primary_font: Phonic
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Robinhood (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Robinhood처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'Capsule Sans Text', Phonic, Helvetica, system-ui, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #110E08; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 네온 옐로우-그린 CTA */
:root { --brand: #CCFF00; }
```

**절대 하지 말아야 할 것 하나**: `#CCFF00` 네온 옐로우-그린을 부드러운 그린이나 라임으로 대체하는 것. 이 컬러는 전기 옐로우에 가까운 극단적 채도의 네온이다. 다크 브라운 배경(`#110E08`) 위에서만 제대로 작동하며, 흰 배경에서는 전혀 다른 브랜드처럼 보인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://robinhood.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes |
| CSS files | 다수 — Emotion/styled-components CSS-in-JS 기반 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미사용, 인라인 해시 클래스) |
| Method | CSS 주파수 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React (Emotion CSS-in-JS)
- **Design system**: 자체 DS — Capsule Design System으로 추정 (Capsule Sans 폰트 패밀리)
- **CSS architecture**: CSS-in-JS 해시 클래스 (`.css-wtcfxq` 등), 커스텀 프로퍼티 미사용
- **Class naming**: Emotion 자동 생성 해시 (`css-*`)
- **Default theme**: dark — 다크 브라운 배경 `#110E08`, 네온 옐로우 accent
- **Font loading**: 자체 호스트 `Phonic`, `Capsule Sans Text/Display`, `Nib Pro Display`
- **Canonical anchor**: `#CCFF00` — CSS 주파수 17회, 유일한 고채도 chromatic 값

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Brand font**: `Phonic` (18회 — 브랜드 전용 커스텀 폰트)
- **Body font**: `Capsule Sans Text` (9회 — 본문 UI)
- **Display**: `Nib Pro Display` (8회 — 히어로 대형 타이틀), `Capsule Sans Display` (4회)
- **Mono**: `Capsule Sans Text Mono` (1회 — 데이터 수치)
- **Legacy/특수**: `Martina Plantijn` (serif, 3회), `ITC Garamond Std` (1회)
- **Weight system**: 300, 400, 500, 600, 700

```css
/* 브랜드 / 헤드라인 */
h1, h2 {
  font-family: 'Nib Pro Display', Phonic, Helvetica, sans-serif;
  font-weight: 400;
}

/* 본문 */
body {
  font-family: 'Capsule Sans Text', Phonic, Helvetica, system-ui, sans-serif;
  font-weight: 400;
}
```

> **주의**: Robinhood의 Capsule Sans 폰트 패밀리(Text/Display/Mono)는 내부 전용 커스텀 폰트. 오픈소스 대체재: `Inter`(Capsule Sans Text용), `Playfair Display`(Nib Pro Display용).

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight | 폰트 |
|---|---|---|---|
| Hero Display | clamp(48px, 8vw, 96px) | 400 | Nib Pro Display |
| Section Heading | 28px–40px | 400–500 | Phonic / Capsule Sans Display |
| Card Title | 16px–20px | 500 | Capsule Sans Text |
| Body | 14px–16px | 400 | Capsule Sans Text |
| Data / Price | 20px–32px | 400 | Capsule Sans Text Mono |
| Caption | 12px | 300–400 | Capsule Sans Text |

> Robinhood 특이점: 헤드라인 weight가 400 — 가늘고 우아한 serif display 폰트로 현대적 핀테크 감성.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand

| Hex | Count | 역할 |
|---|---|---|
| `#CCFF00` | 17 | 브랜드 네온 옐로우-그린 CTA |

### Dark Background

| Hex | Count | 역할 |
|---|---|---|
| `#110E08` | 24 | 메인 다크 브라운 배경 |
| `#35322D` | 22 | 보조 다크 브라운 |
| `#1C180D` | 2 | 카드 다크 배경 |

### Neutrals

| Hex | Count | 역할 |
|---|---|---|
| `#FFFFFF` | 31 | 텍스트, 밝은 배경 |
| `#888784` | 4 | 보조 텍스트 |
| `#4D4A46` | 2 | 구분선, 보더 |

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
| Button | 999px (pill) |
| Card | 12px–16px |
| Input | 8px |
| Badge | 999px |

> Robinhood 버튼은 pill shape — Wise와 같은 완전 rounded 스타일.

---

## 09. Shadows
<!-- SOURCE: manual -->

| 레이어 | CSS |
|---|---|
| Card | `box-shadow: 0 4px 24px rgba(0,0,0,.4)` (다크 배경) |
| Modal | `box-shadow: 0 8px 48px rgba(0,0,0,.6)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| Button hover | 180ms | ease |
| Card hover | 200ms | ease-out |
| Price animation | 300ms | ease |
| Page transition | 400ms | ease-in-out |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 다크 브라운 배경, 대형 serif display 헤드라인, 네온 옐로우 CTA pill
- **차트 섹션**: 실시간 주가 차트, 다크 배경 위 네온 그린 라인
- **Feature 그리드**: 다크 카드, 아이콘 + 텍스트
- **컨테이너**: `max-width: 1200px; margin: 0 auto; padding: 0 24px`
- **Nav**: 다크 배경 고정, 네온 옐로우 CTA

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button (Pill)

```css
.btn-primary {
  background: #CCFF00;
  color: #110E08;        /* 다크 배경 위 밝은 텍스트 아님 — 다크 텍스트 */
  border: none;
  border-radius: 999px;  /* pill */
  padding: 14px 32px;
  font-family: 'Capsule Sans Text', sans-serif;
  font-weight: 500;
  font-size: 16px;
  transition: all 180ms ease;
}
.btn-primary:hover {
  background: #D9FF33;
  box-shadow: 0 0 20px rgba(204,255,0,.3);
}
```

### Price Display

```css
.price-display {
  font-family: 'Capsule Sans Text Mono', monospace;
  font-size: 32px;
  font-weight: 400;
  color: #FFFFFF;
}
.price-display--up {
  color: #CCFF00;  /* 상승 시 네온 그린 */
}
```

### Dark Card

```css
.card {
  background: #1C180D;
  border: 1px solid #35322D;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 24px rgba(0,0,0,.4);
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 대담, 투자 민주화. "Investing for Everyone."
- **수치**: 수익률, 퍼센트 강조. "+12.4% YTD"
- **CTA**: "Get started", "Sign up for free" — 진입 장벽 낮춤 강조
- **어조**: 젊고 대담, 월스트리트 엘리트 반대

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Robinhood Design System — Drop-in */
:root {
  --brand:    #CCFF00;
  --bg-dark:  #110E08;
  --bg-card:  #1C180D;
  --bg-alt:   #35322D;
  --fg:       #FFFFFF;
  --fg-muted: #888784;
  --border:   #4D4A46;

  --font-brand:   'Phonic', Helvetica, system-ui, sans-serif;
  --font-body:    'Capsule Sans Text', Phonic, Helvetica, sans-serif;
  --font-display: 'Nib Pro Display', serif;
  --font-mono:    'Capsule Sans Text Mono', monospace;
}

body {
  font-family: var(--font-body);
  font-weight: 400;
  background: var(--bg-dark);
  color: var(--fg);
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
        robinhood: {
          neon:     '#CCFF00',
          'neon-hover': '#D9FF33',
          dark:     '#110E08',
          'dark-card':  '#1C180D',
          'dark-alt':   '#35322D',
          muted:    '#888784',
          border:   '#4D4A46',
        },
      },
      fontFamily: {
        brand:   ['Phonic', 'Helvetica', 'system-ui', 'sans-serif'],
        body:    ['Capsule Sans Text', 'Phonic', 'Helvetica', 'sans-serif'],
        display: ['Nib Pro Display', 'serif'],
        mono:    ['Capsule Sans Text Mono', 'monospace'],
      },
      borderRadius: {
        btn: '999px',
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

- `#CCFF00` 네온 옐로우-그린을 CTA에 사용 — 다크 배경 위에서만
- 버튼 텍스트는 `#110E08` 다크 브라운 — 네온 배경 위
- `Nib Pro Display` 또는 가벼운 serif로 대형 히어로 타이틀
- 다크 배경(`#110E08`) 필수 — 네온의 컨텍스트
- 주가 상승 표시에 `#CCFF00` 사용 — 브랜드 통일성

### DON'T

- 흰 배경에 `#CCFF00` — 다크 배경이 없으면 의미 없음
- CTA 텍스트를 흰색으로 — 네온 배경 위는 다크 텍스트
- 부드러운 그린으로 대체 — `#CCFF00`은 극단적 채도의 네온
- 과도하게 굵은 헤드라인 — Robinhood는 weight 400 가는 serif

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| Robinhood = 초록 | 브랜드는 `#CCFF00` 네온 옐로우-그린 |
| 흰 배경이 기본 | 다크 브라운 `#110E08`이 primary |
| 버튼 텍스트 흰색 | 네온 배경 위는 다크 `#110E08` 텍스트 |
| CSS 토큰 기반 | Emotion CSS-in-JS, 커스텀 프로퍼티 미사용 |
