---
slug: coinbase
service_name: Coinbase
site_url: https://www.coinbase.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0052FF"
primary_font: CoinbaseSans
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Coinbase (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Coinbase처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: CoinbaseSans, -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #0A0B0D; }
body { background: var(--bg); color: var(--fg); }

/* 3. Coinbase 블루 */
:root { --brand: #0052FF; }
```

**절대 하지 말아야 할 것 하나**: `#0052FF`를 일반 파랑으로 대체하는 것. 이 값은 Coinbase 고유의 진한 로얄 블루로, CSS 소스에서 OneTrust SDK accept 버튼, 링크 컬러 모두 명시적으로 사용된다. `#0066CC` 같은 소프트 블루나 `#1D9BF0` 트위터 블루와 전혀 다른 포지셔닝이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.coinbase.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes |
| CSS files | 다수 — React/Next.js SSR + OneTrust SDK CSS 포함 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미사용 — 자체 DS 내부 토큰) |
| Method | CSS 주파수 파싱 + selector_role 확인 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React (글로벌 크립토 거래소)
- **Design system**: 자체 DS — Coinbase 폰트 패밀리 (Sans/Display/Condensed/Mono/Text/Icons)
- **CSS architecture**: CSS 모듈 기반 추정, 커스텀 프로퍼티 미사용
- **Default theme**: light (흰 배경, 다크 텍스트, 코발트 블루 CTA)
- **Font loading**: 자체 호스트 `CoinbaseSans`, `CoinbaseDisplay`, `CoinbaseCondensed`, `CoinbaseMono`, `CoinbaseText`
- **Canonical anchor**: `#0052FF` — OneTrust SDK accept/reject 버튼, 링크 등 Coinbase 브랜드 컬러로 명시

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary/Body font**: `CoinbaseSans` (6회 — 주요 UI 텍스트)
- **Display font**: `CoinbaseDisplay` (2회 — 히어로 헤드라인)
- **Condensed**: `CoinbaseCondensed` (2회 — 숫자, 가격 표시)
- **Mono**: `CoinbaseMono` (2회 — 지갑 주소, 코드)
- **Text**: `CoinbaseText` (2회 — 긴 본문)
- **Icon**: `CoinbaseIcons` (3회 — UI 아이콘 폰트)
- **Weight system**: 100, 300, 400, 500, 600, 700, bold, normal

```css
/* 기본 UI */
body {
  font-family: CoinbaseSans, -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  font-weight: 400;
}

/* 히어로 디스플레이 */
h1 {
  font-family: CoinbaseDisplay, CoinbaseSans, sans-serif;
  font-weight: 700;
}
```

> **주의**: Coinbase 폰트 패밀리는 전용 커스텀 폰트. 오픈소스 대체재: `CoinbaseSans` → `Inter`, `CoinbaseDisplay` → `Sora` 또는 `Plus Jakarta Sans`.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight | 폰트 |
|---|---|---|---|
| Hero Display | clamp(40px, 6vw, 72px) | 700 | CoinbaseDisplay |
| Section Heading | 28px–40px | 600–700 | CoinbaseSans |
| Card Title | 18px–22px | 600 | CoinbaseSans |
| Body | 14px–16px | 400 | CoinbaseSans / CoinbaseText |
| Price / Data | 20px–32px | 600–700 | CoinbaseCondensed |
| Wallet Address | 13px–14px | 400 | CoinbaseMono |
| Caption | 12px | 400 | CoinbaseSans |
| Button | 16px | 600 | CoinbaseSans |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand

| Hex | 역할 | 출처 |
|---|---|---|
| `#0052FF` | 브랜드 로얄 블루 — CTA 버튼, 링크 | OneTrust (Coinbase 설정) |

### Neutrals (OneTrust에서 확인)

| Hex | 역할 |
|---|---|
| `#0A0B0D` | 메인 텍스트 (near-black) |
| `#EEF0F3` | 버튼 배경 (보조) |
| `#FFFFFF` | 기본 배경 |

### Neutrals (일반)

| Hex | 역할 |
|---|---|
| `#1B1B1F` | 다크 텍스트 |
| `#F5F8FF` | 라이트 블루 배경 (브랜드 tint) |
| `#3773F5` | 블루 hover |

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
| Button | 8px |
| Card | 12px–16px |
| Input | 8px |
| Modal | 16px |
| Badge | 999px |

> 핀테크/크립토 — 둥글지도 샤프하지도 않은 중립 radius.

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
| Price animation | 200ms | ease |
| Modal open | 250ms | ease-out |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 흰 배경, 큰 헤드라인, 블루 CTA — crypto intro
- **Price 섹션**: 실시간 자산 가격 그리드, condensed 폰트
- **Feature 섹션**: 2-3 column 카드 그리드
- **컨테이너**: `max-width: 1200px; margin: 0 auto; padding: 0 24px`
- **Nav**: 흰 배경 sticky, 블루 "Get started" 버튼

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button

```css
.btn-primary {
  background: #0052FF;
  color: #FFFFFF;
  border: none;
  border-radius: 8px;
  padding: 14px 24px;
  font-family: CoinbaseSans, sans-serif;
  font-weight: 600;
  font-size: 16px;
  transition: all 150ms ease;
}
.btn-primary:hover {
  background: #3773F5;
}
```

### Price Card

```css
.price-card {
  background: #FFFFFF;
  border: 1px solid #EEF0F3;
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 4px 16px rgba(0,0,0,.08);
}
.price-card .price {
  font-family: CoinbaseCondensed, sans-serif;
  font-size: 28px;
  font-weight: 600;
  color: #0A0B0D;
}
.price-card .price--up {
  color: #05B169;  /* 상승 그린 */
}
```

### Wallet Address

```css
.wallet-address {
  font-family: CoinbaseMono, 'SF Mono', monospace;
  font-size: 13px;
  font-weight: 400;
  color: #0A0B0D;
  background: #F5F8FF;
  padding: 8px 12px;
  border-radius: 8px;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 크립토 접근성, 신뢰. "The easiest place to buy and sell crypto."
- **수치**: 자산 가격, 지원 코인 수. "250+ supported assets"
- **CTA**: "Get started", "Buy now", "Trade" — 직접적
- **어조**: 신뢰 + 접근성. 크립토 초보도 진입 가능

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Coinbase Design System — Drop-in */
:root {
  --brand:         #0052FF;
  --brand-hover:   #3773F5;
  --brand-light:   #F5F8FF;

  --color-bg:      #FFFFFF;
  --color-fg:      #0A0B0D;
  --color-border:  #EEF0F3;

  --font-sans:    CoinbaseSans, -apple-system, BlinkMacSystemFont,
                  'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  --font-display: CoinbaseDisplay, CoinbaseSans, sans-serif;
  --font-mono:    CoinbaseMono, 'SF Mono', monospace;
  --font-cond:    CoinbaseCondensed, CoinbaseSans, sans-serif;
}

body {
  font-family: var(--font-sans);
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
        coinbase: {
          blue:  '#0052FF',
          'blue-hover': '#3773F5',
          'blue-light': '#F5F8FF',
          dark:  '#0A0B0D',
          gray:  '#EEF0F3',
        },
      },
      fontFamily: {
        sans:    ['CoinbaseSans', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        display: ['CoinbaseDisplay', 'CoinbaseSans', 'sans-serif'],
        mono:    ['CoinbaseMono', 'SF Mono', 'monospace'],
        cond:    ['CoinbaseCondensed', 'CoinbaseSans', 'sans-serif'],
      },
      borderRadius: {
        btn:  '8px',
        card: '12px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- `#0052FF` 로얄 블루를 메인 CTA에 — 크립토 신뢰 컬러
- `CoinbaseSans`로 UI 텍스트, `CoinbaseDisplay`로 히어로
- 가격 표시에 `CoinbaseCondensed` — 숫자 가독성
- 지갑 주소에 `CoinbaseMono` — 무결성 표시
- 흰 배경 + 블루 CTA — 접근성과 신뢰 동시 전달

### DON'T

- 소프트 블루(`#0066CC` 등)로 `#0052FF` 대체 — 로얄 블루의 강도가 중요
- 다크 배경을 기본으로 — 라이트가 Coinbase의 주 테마
- 가격에 serif 폰트 — Condensed mono 계열 유지

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| Coinbase = 크립토 = 어둡고 화려함 | 라이트 테마 + 로얄 블루 — 신뢰 우선 |
| CSS 토큰 기반 DS | 커스텀 프로퍼티 미사용, 자체 Coinbase 폰트 패밀리 기반 |
| 일반 파랑으로 대체 가능 | `#0052FF`는 Coinbase 고유 로얄 블루 |
