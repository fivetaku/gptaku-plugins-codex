---
slug: lucid
service_name: Lucid
site_url: https://lucid.app
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#D7BE96"
primary_font: GTAmerica
font_weight_normal: 400
token_prefix: --color-primary-colors-*
---

# DESIGN.md — Lucid (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Lucid처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "GTAmerica", "IBM Plex Sans", -apple-system, BlinkMacSystemFont, Helvetica, Roboto, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 다크 배경 + 텍스트 */
:root { --bg: #0F0F0F; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 골드 */
:root { --brand: #D7BE96; }
```

**절대 하지 말아야 할 것 하나**: 골드(#D7BE96)를 노란 CTA로 쓰면서 배경을 밝게 두는 것. Lucid 골드는 다크 배경(#0F0F0F)과의 대비에서만 효과가 살아난다. 라이트 배경 위 골드는 가독성이 없다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://lucid.app` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | `--color-primary-colors-gold`, `--border-brand-gold`, `--surface-brand-gold` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · semantic_vars 추출 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (SSR)
- **Design system**: 인-하우스 — `--color-primary-colors-*`, `--border-brand-*`, `--surface-brand-*` 토큰
- **CSS architecture**: CSS 변수 기반 토큰 시스템 (대규모, 10K줄 이상)
- **Default theme**: dark (#0F0F0F 기반 — frequency top)
- **Font loading**: 자체 호스트 — GTAmerica (마케팅), Lucid Sans VF (앱 내부)
- **Notable**: 마케팅 사이트와 앱 내부가 폰트 스택 다름. 마케팅=GTAmerica, 앱=Lucid Sans VF

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **마케팅 Primary**: `GTAmerica` (Grilli Type, 유료) — 마케팅 사이트
- **App Primary**: `Lucid Sans VF` (Lucid 전용 variable font) — 앱 내부
- **Display**: `SchnyderS`, `SchnyderM` (Grilli Type, 유료) — 대형 헤드라인
- **Serif (editorial)**: `Lucid Serif VF`, `Lucid Serif Italic VF` — 롱폼 콘텐츠
- **Fallback**: `IBM Plex Sans`, `-apple-system`, `Helvetica`
- **Weight**: `300` (light body), `400` (normal), `600` (semibold)

```css
/* 마케팅 사이트 */
body {
  font-family: "GTAmerica", "IBM Plex Sans", -apple-system, BlinkMacSystemFont, Helvetica, Roboto, Arial, sans-serif;
  font-weight: 300; /* Lucid body는 light 300 */
}
.headline-display {
  font-family: "SchnyderS", Georgia, Times, "Times New Roman", serif;
  font-weight: 400;
}
/* 앱 내부 */
.app-body {
  font-family: "Lucid Sans VF", "IBM Plex Sans", -apple-system, sans-serif;
  font-weight: 300;
}
```

> **라이선스 주의**: GTAmerica · Schnyder 유료. 대체재: `Inter` (GTAmerica), `Playfair Display` (Schnyder serif).

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Display | SchnyderS | 64–100px | 400 | 1.0 | -0.02em |
| Section H2 | GTAmerica | 36–56px | 300 | 1.15 | -0.01em |
| Card Title | GTAmerica | 20–28px | 400 | 1.3 | 0 |
| Body | GTAmerica | 16–18px | 300 | 1.7 | 0 |
| App Body | Lucid Sans VF | 14–16px | 300 | 1.5 | 0 |
| Caption | GTAmerica | 12–13px | 300 | 1.4 | 0.02em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Gold Palette (CSS 변수 직접 추출)

| CSS 변수 | Hex | 용도 |
|---|---|---|
| `--color-primary-colors-gold` | `#D7BE96` | **Primary 브랜드 골드** |
| `--border-brand-gold` | `#D7BE96` | 골드 보더 |
| `--surface-brand-gold` | `#D7BE96` | 골드 표면 |
| `--text-brand-gold` | `#D7BE96` | 골드 텍스트 |
| Secondary Gold | `#DBD4C5` | 밝은 골드 variant |
| Muted Gold | `#9D857F` | 어두운 골드/구리 |
| Alt Muted | `#A8918B` | 중간 골드 |

### Dark Neutral Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Page BG | `#0F0F0F` | body 배경 (frequency 1위) |
| Black | `#000000` | 섹션 배경 |
| Dark BG2 | `#1C1C1C` | 카드 배경 |
| Dark BG3 | `#323232` | 차선 배경 |
| Mid Gray | `#4D4D4D` | 경계선 |
| Gray | `#6B6B6B` | muted 텍스트 |
| Light Gray | `#959595` | 부제목 |

### Product Color Palette (앱 내부)

| 이름 | Hex | 용도 |
|---|---|---|
| Blue | `#000A19` → `#041E42` | 딥 네이비 (Lucidchart) |
| Green | `#00AD56` | 성공, 수락 |
| Orange | `#DC8100` | 경고, Lucidspark |
| Red | `#CE0D17` | 에러, 삭제 |
| Cyan | `#00A8F1` | 정보 |

---

## 07. Spacing
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘 간격 |
| sm | 8px | 인라인 요소 |
| md | 16px | 카드 내부 |
| lg | 24px | 섹션 내부 |
| xl | 40px | 섹션 간격 |
| 2xl | 64px | 주요 섹션 |
| 3xl | 96px | hero 패딩 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| sm | 4px | 태그, 배지 |
| md | 8px | 버튼, 카드 |
| lg | 16px | 큰 카드 |
| xl | 24px | hero 배너 |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card-dark | `0 4px 24px rgba(0,0,0,.4)` | 다크 배경 카드 |
| gold-glow | `0 0 24px rgba(215,190,150,.2)` | 골드 글로우 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 150ms | hover 전환 |
| duration-base | 280ms | 카드·패널 |
| duration-slow | 500ms | 섹션 진입 |
| easing | `cubic-bezier(0.4,0,0.2,1)` | 표준 전환 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **최대 너비**: 1440px, 콘텐츠 1200px
- **Hero**: full-viewport dark, 중앙 텍스트 + 골드 accent
- **Feature Alternation**: 텍스트 + 제품 스크린샷 교차 (2-col)
- **Product Tabs**: Lucidchart / Lucidspark / Lucidscale 탭 전환
- **Pricing Grid**: 3-col 비교 카드

---

## 12. Components
<!-- SOURCE: manual -->

### CTA 버튼 (골드 outline)

```css
.btn-gold {
  background: transparent;
  color: #D7BE96;
  border: 1px solid #D7BE96;
  font-family: "GTAmerica", sans-serif;
  font-size: 16px; font-weight: 400;
  padding: 12px 24px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 150ms, color 150ms;
}
.btn-gold:hover {
  background: #D7BE96;
  color: #0F0F0F;
}
```

### 골드 accent 텍스트

```css
/* --text-brand-gold */
.text-gold { color: #D7BE96; }
.border-gold { border-color: #D7BE96; }
.surface-gold { background: #D7BE96; color: #0F0F0F; }
```

### Feature 카드

```css
.feature-card {
  background: #1C1C1C;
  border: 1px solid #323232;
  border-radius: 16px;
  padding: 32px 24px;
  transition: border-color 150ms;
}
.feature-card:hover { border-color: #D7BE96; }
.feature-card__title {
  font-size: 20px; font-weight: 400; color: #FFFFFF;
  margin-bottom: 12px;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: "Visualize together" — 협업 강조
- **서브**: 제품별 핵심 benefit 1문장
- **CTA**: "Get started free" / "Try free" / "See plans"
- **톤**: 현대적·세련된 B2B — 차갑지 않고 우아한

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand Gold Tokens */
  --color-primary-colors-gold: #D7BE96;
  --border-brand-gold: #D7BE96;
  --surface-brand-gold: #D7BE96;
  --text-brand-gold: #D7BE96;

  /* Alias */
  --brand: #D7BE96;
  --bg: #0F0F0F;
  --bg-card: #1C1C1C;
  --fg: #FFFFFF;
  --fg-muted: #959595;

  /* Border */
  --border: #323232;
  --border-strong: #4D4D4D;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 40px;
  --space-2xl: 64px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
}

body {
  font-family: "GTAmerica", "IBM Plex Sans", -apple-system, BlinkMacSystemFont, Helvetica, Roboto, Arial, sans-serif;
  font-weight: 300;
  background: var(--bg);
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
        brand: '#D7BE96',
        'brand-muted': '#9D857F',
        'bg-dark': '#0F0F0F',
        'bg-card': '#1C1C1C',
        'border-dark': '#323232',
        'text-muted': '#959595',
      },
      fontFamily: {
        sans: ['"GTAmerica"', '"IBM Plex Sans"', '-apple-system', 'BlinkMacSystemFont', 'Helvetica', 'sans-serif'],
        display: ['"SchnyderS"', 'Georgia', 'Times', 'serif'],
        app: ['"Lucid Sans VF"', '"IBM Plex Sans"', '-apple-system', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '8px',
        sm: '4px',
        lg: '16px',
        xl: '24px',
      },
      fontWeight: {
        light: '300',
        normal: '400',
        semibold: '600',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- **배경은 #0F0F0F** — 순검정이 아닌 약간 따뜻한 near-black
- **골드(#D7BE96)는 반드시 다크 배경 위에서** — 라이트 배경 위 가독성 불가
- **본문 weight는 300 (light)** — GTAmerica light가 Lucid 세련됨의 핵심
- **CSS 토큰명 `--color-primary-colors-gold` 원본 유지** — 임의 축약 금지
- **Schnyder serif를 display에** — 골드와 세리프의 조합이 고급스러움

### DON'T

- **골드를 라이트 배경에 쓰지 않는다** — 대비 부족으로 읽기 불가
- **body weight를 400으로 올리지 않는다** — 300이 Lucid 마케팅 정체성
- **앱 내부 컬러(#00AD56 green, #DC8100 orange)를 마케팅 사이트에 그대로 쓰지 않는다** — 다른 레이어
- **골드와 흰색만으로 팔레트 구성하지 않는다** — 다크 그레이 계층이 필수
- **Lucid Sans VF (앱 폰트)를 마케팅에 적용하지 않는다** — GTAmerica가 마케팅용
