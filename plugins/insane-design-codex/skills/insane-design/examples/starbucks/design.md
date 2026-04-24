---
slug: starbucks
service_name: Starbucks
site_url: https://www.starbucks.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#006242"
primary_font: SoDoSans
font_weight_normal: 400
token_prefix: --colorGreenAccent
---

# DESIGN.md — Starbucks (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Starbucks처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SoDoSans", "Lander Tall", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F5F1EB; --fg: #1E3932; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 그린 */
:root { --brand: #006242; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백(#FFFFFF)으로 두는 것. Starbucks 배경은 따뜻한 크림(#F5F1EB)이다. 흰 배경으로 바꾸면 브랜드 따뜻함이 완전히 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.starbucks.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | `--colorGreenAccent: #00754A` (CSS 변수 1개 노출) |
| Method | CSS 커스텀 프로퍼티 파싱 · frequency 분석 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React (인하우스 빌드)
- **Design system**: 인-하우스 (공개 DS 없음, 토큰 1개만 노출)
- **CSS architecture**: 인라인 스타일 + CSS Modules 혼용 추정
- **Default theme**: light (크림 배경 #F5F1EB)
- **Font loading**: 자체 호스트 — SoDoSans (custom), Lander Tall (display)
- **Notable**: CSS 추출 결과에서 그린 계열 컬러가 다수 — #006242, #006241, #00754A

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary**: `SoDoSans` (Starbucks 전용 custom sans, 재배포 불가)
- **Display/Headline**: `Lander Tall` (Starbucks 전용 display 폰트)
- **Fallback**: `Helvetica Neue, Helvetica, Arial, sans-serif`
- **Weight normal / bold**: `400` / `600–700`

```css
body {
  font-family: "SoDoSans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}
.headline {
  font-family: "Lander Tall", "SoDoSans", "Helvetica Neue", sans-serif;
  font-weight: 700;
}
```

> **라이선스 주의**: SoDoSans · Lander Tall 모두 Starbucks 전용 폰트. 대체재: `Montserrat` (bold 헤드라인) + `Source Sans 3` (본문).

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Display | Lander Tall | 56–80px | 700 | 1.05 | -0.01em |
| Section H2 | SoDoSans | 32–40px | 700 | 1.15 | -0.01em |
| Card Title | SoDoSans | 20–24px | 600 | 1.3 | 0 |
| Body | SoDoSans | 16px | 400 | 1.65 | 0 |
| Small / Caption | SoDoSans | 13–14px | 400 | 1.5 | 0 |
| Button | SoDoSans | 14–16px | 700 | 1 | 0.02em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Green Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Brand Green (Primary) | `#006242` | CTA 버튼, 헤더, 브랜드 강조 |
| Green Alt | `#006241` | 미세 variant |
| Green Accent (CSS var) | `#00754A` | --colorGreenAccent (accent 역할) |
| Green Accent Alt | `#008046` | 밝은 그린 hover |
| Forest (Body Text BG) | `#1E3932` | 다크 그린 텍스트, 어두운 섹션 |
| Forest Mid | `#2B5148` | 중간 다크 그린 |

### Warm Neutral Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Cream BG | `#F5F1EB` | 페이지 기본 배경 (중요) |
| Warm White | `#FAF6EE` | 카드 배경 |
| Parchment | `#F2F0EB` | 섹션 배경 |
| Light Green Tint | `#D4E9E2` | 그린 섹션 tint |
| Gold | `#CBA258` | 포인트 골드 |
| Caramel | `#F3CEA1` | 제품 이미지 배경 |
| Error Red | `#C82014` | 오류 상태 |

---

## 07. Spacing
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘·태그 간격 |
| sm | 8px | 인라인 요소 |
| md | 16px | 카드 내부 |
| lg | 24px | 섹션 내부 패딩 |
| xl | 40px | 섹션 간격 |
| 2xl | 64px | 주요 섹션 |
| 3xl | 96px | hero 패딩 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| sm | 4px | 태그, 배지 |
| md | 8px | 버튼 (CTA) |
| lg | 16px | 카드, 이미지 컨테이너 |
| xl | 24px | hero 배너 |
| pill | 50px | 둥근 CTA (Mobile App) |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card | `0 2px 8px rgba(0,0,0,.1)` | 제품 카드 |
| elevated | `0 4px 16px rgba(0,0,0,.12)` | 모달, 드롭다운 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 150ms | hover 전환 |
| duration-base | 300ms | 카드, 드롭다운 |
| easing | `ease` | 모든 전환 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **최대 너비**: 1440px, 콘텐츠 1200px
- **Hero**: full-width 이미지 + 오버레이 텍스트 또는 크림 배경 텍스트
- **Product Grid**: 3–4 col (desktop), 2 col (tablet), 1 col (mobile)
- **Story Section**: 2-col 텍스트 + 이미지 교차
- **배경 리듬**: 크림(#F5F1EB) ↔ 그린(#1E3932) 섹션 교차

---

## 12. Components
<!-- SOURCE: manual -->

### CTA 버튼

```css
.btn-primary {
  background: #006242;
  color: #FFFFFF;
  font-family: "SoDoSans", sans-serif;
  font-size: 14px; font-weight: 700;
  padding: 10px 24px;
  border-radius: 8px;
  border: none; cursor: pointer;
  letter-spacing: 0.02em;
  transition: background 150ms ease;
}
.btn-primary:hover { background: #00754A; }
```

### 제품 카드

```css
.product-card {
  background: #FAF6EE;
  border-radius: 16px;
  overflow: hidden;
  transition: transform 150ms ease, box-shadow 150ms ease;
}
.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,.12);
}
.product-card__name {
  font-family: "SoDoSans", sans-serif;
  font-size: 16px; font-weight: 600;
  color: #1E3932;
}
.product-card__price {
  font-size: 14px; color: #006242; font-weight: 600;
}
```

### 네비게이션 로고존

```css
.nav {
  background: #006242;
  color: #FFFFFF;
  padding: 0 24px;
  height: 64px;
  display: flex; align-items: center;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: "Good coffee should be shared" — 따뜻하고 감성적
- **서브**: 제품 혜택 + 경험 중심 서술
- **CTA**: "Order now" / "Find a store" / "Join Starbucks Rewards"
- **제품명**: 고유 명칭 (예: "Iced Brown Sugar Oatmilk Shaken Espresso")
- **톤**: 친근함 + 따뜻함 + 커뮤니티

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand Green */
  --brand: #006242;
  --brand-accent: #00754A; /* --colorGreenAccent */
  --brand-forest: #1E3932;
  --brand-hover: #008046;

  /* Warm Neutral */
  --bg: #F5F1EB;
  --bg-card: #FAF6EE;
  --fg: #1E3932;
  --fg-muted: #2B5148;

  /* Gold */
  --gold: #CBA258;
  --caramel: #F3CEA1;

  /* Status */
  --error: #C82014;

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
  --radius-pill: 50px;
}

body {
  font-family: "SoDoSans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
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
        brand: '#006242',
        'brand-accent': '#00754A',
        'brand-forest': '#1E3932',
        'brand-hover': '#008046',
        cream: '#F5F1EB',
        'card-bg': '#FAF6EE',
        gold: '#CBA258',
        caramel: '#F3CEA1',
        error: '#C82014',
      },
      fontFamily: {
        sans: ['"SoDoSans"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
        display: ['"Lander Tall"', '"SoDoSans"', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '8px',
        sm: '4px',
        lg: '16px',
        xl: '24px',
        pill: '50px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- **배경은 크림(#F5F1EB)** — 순백이 아닌 따뜻한 크림 베이스
- **그린은 #006242** — 공식 브랜드 그린 (CSS frequency 최다 chromatic)
- **카드 배경은 #FAF6EE** (크림보다 살짝 흰) — 표면 레이어 구분
- **다크 섹션은 포레스트 그린 #1E3932** — 검정 대신 그린 계열 다크
- **제품 이미지 배경은 카라멜/골드 계열** (#F3CEA1, #CBA258)

### DON'T

- **배경을 순백(#FFFFFF)으로 쓰지 않는다** — Starbucks 브랜드 따뜻함 파괴
- **그린 위에 빨강(#C82014)을 사용하지 않는다** — 에러 전용 색상
- **그린(#006242)과 #FBBC05(구글 노랑)를 함께 쓰지 않는다** — Google Maps 오염 색상
- **SoDoSans weight 300으로 쓰지 않는다** — 400 이상이 기준
- **다크 배경에 그린 CTA를 그대로 쓰지 않는다** — 대비 부족으로 흰 버튼 사용
