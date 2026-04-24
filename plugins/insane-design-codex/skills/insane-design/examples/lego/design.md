---
slug: lego
service_name: LEGO
site_url: https://www.lego.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#E3000B"
primary_font: Cera Pro
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — LEGO (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 LEGO처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Cera Pro", "Nunito", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1A1A1A; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 레드 */
:root { --brand: #E3000B; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 레드를 위험/에러 색으로만 취급하는 것. LEGO 레드(#E3000B)는 primary CTA·버튼·브랜드 식별자다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.lego.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | N/A (CSS 파싱 결과 최소, #313131 단일) |
| Method | CSS 파싱 + 브랜드 지식 보완 (Tailwind SSR 난독화 추정) |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js 또는 Nuxt.js (SSR, Tailwind v3 사용 추정)
- **Design system**: LEGO 인-하우스 (Binocular Design System)
- **CSS architecture**: Tailwind utility + CSS Modules (빌드 시 토큰 인라인화)
- **Default theme**: light (흰 배경)
- **Font loading**: 자체 호스트 — Cera Pro (LEGO 라이선스)
- **Notable**: CSS 추출이 매우 희박 (Tailwind JIT + 번들 난독화)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary**: `Cera Pro` (TypeMates, LEGO 라이선스)
- **Fallback**: `Nunito`, `Helvetica Neue`, `Arial`, sans-serif
- **Weight**: `400` (normal), `700` (bold), `900` (black — 주요 헤드라인)

```css
body {
  font-family: "Cera Pro", "Nunito", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}
h1, .headline {
  font-weight: 900; /* LEGO 특유의 두꺼운 블랙 헤드라인 */
  text-transform: uppercase;
  letter-spacing: -0.02em;
}
```

> **라이선스 주의**: Cera Pro 유료 라이선스. 대체재: `Nunito Black` (Google Fonts, 유사한 둥근 기하학).

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Display | Cera Pro | 56–96px | 900 | 0.95 | -0.02em |
| Section H2 | Cera Pro | 32–48px | 900 | 1.05 | -0.015em |
| Card Title | Cera Pro | 18–24px | 700 | 1.25 | 0 |
| Body | Cera Pro | 14–16px | 400 | 1.6 | 0 |
| Price | Cera Pro | 16–20px | 700 | 1 | 0 |
| Caption | Cera Pro | 12–13px | 400 | 1.4 | 0 |
| Age Range | Cera Pro | 14px | 700 | 1 | 0.02em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Core Palette

| 이름 | Hex | 용도 |
|---|---|---|
| LEGO Red | `#E3000B` | CTA 버튼, 브랜드 identity, 헤더 |
| Red Dark | `#CC0009` | hover 상태 |
| LEGO Yellow | `#FFD700` | 서브 브랜드, 포인트, 특별 CTA |
| LEGO Blue | `#006CB7` | 링크, 정보 섹션 |
| LEGO Green | `#00A650` | 재고 있음, 성공 상태 |
| LEGO Black | `#1A1A1A` | 본문 텍스트 |

### Surface / Neutral Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Page BG | `#FFFFFF` | body 배경 |
| Section BG | `#F5F5F5` | 교차 섹션 |
| Border | `#D8D8D8` | 경계선 |
| Muted Text | `#6A6A6A` | 부제목, 메타 |
| Dark BG | `#313131` | 다크 섹션 배경 (CSS에서 추출) |

---

## 07. Spacing
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘·배지 |
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
| sm | 4px | 태그, 작은 배지 |
| md | 8px | 버튼, 카드 |
| lg | 12px | 큰 카드 |
| circle | 50% | 연령 배지, 아바타 |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card | `0 2px 8px rgba(0,0,0,.1)` | 제품 카드 |
| card-hover | `0 8px 24px rgba(0,0,0,.15)` | hover 상태 |
| dropdown | `0 4px 16px rgba(0,0,0,.15)` | 드롭다운 메뉴 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 150ms | hover 전환 |
| duration-base | 300ms | 카드 lift |
| easing | `ease-out` | 요소 등장 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **최대 너비**: 1440px, 콘텐츠 1200px
- **Product Grid**: 4-col (desktop), 3-col (tablet), 2-col (small), 1-col (mobile)
- **Hero**: full-width 이미지 + 텍스트 오버레이 또는 split
- **Age + Price Strip**: 하단 고정 띠 (연령 범위, 조각 수, 가격)
- **Category Nav**: 수평 스크롤 pill 탭

---

## 12. Components
<!-- SOURCE: manual -->

### CTA 버튼 (레드)

```css
.btn-primary {
  background: #E3000B;
  color: #FFFFFF;
  font-family: "Cera Pro", sans-serif;
  font-size: 14px; font-weight: 700;
  padding: 12px 24px;
  border-radius: 8px;
  border: none; cursor: pointer;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  transition: background 150ms ease;
}
.btn-primary:hover { background: #CC0009; }
```

### 제품 카드

```css
.product-card {
  background: #FFFFFF;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid transparent;
  transition: box-shadow 150ms ease, transform 150ms ease;
}
.product-card:hover {
  box-shadow: 0 8px 24px rgba(0,0,0,.15);
  transform: translateY(-4px);
}
.product-card__age {
  display: inline-flex; align-items: center;
  background: #FFD700; color: #1A1A1A;
  font-size: 12px; font-weight: 700;
  padding: 2px 8px; border-radius: 50px;
}
.product-card__price {
  font-size: 18px; font-weight: 700; color: #1A1A1A;
}
```

### 연령 배지

```css
.age-badge {
  background: #FFD700;
  color: #1A1A1A;
  font-family: "Cera Pro", sans-serif;
  font-size: 12px; font-weight: 700;
  padding: 3px 10px;
  border-radius: 50px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: "Build your world" — 어린이·가족 모두를 위한 긍정적 언어
- **제품명**: 구체적 + 세트명 (LEGO Technic, LEGO City, LEGO Star Wars)
- **연령/조각 수**: 항상 표시 ("Ages 8+", "1,471 pieces")
- **CTA**: "Add to bag" / "Buy now" / "Find in store"
- **톤**: 즐거움·상상력·포용

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand */
  --brand: #E3000B;
  --brand-hover: #CC0009;
  --brand-yellow: #FFD700;
  --brand-blue: #006CB7;
  --brand-green: #00A650;

  /* Surface */
  --bg: #FFFFFF;
  --bg-section: #F5F5F5;
  --fg: #1A1A1A;
  --fg-muted: #6A6A6A;

  /* Border */
  --border: #D8D8D8;

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
  --radius-lg: 12px;
  --radius-circle: 50%;
}

body {
  font-family: "Cera Pro", "Nunito", "Helvetica Neue", Arial, sans-serif;
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
        brand: '#E3000B',
        'brand-hover': '#CC0009',
        'brand-yellow': '#FFD700',
        'brand-blue': '#006CB7',
        'brand-green': '#00A650',
        'near-black': '#1A1A1A',
        'text-muted': '#6A6A6A',
        'section-bg': '#F5F5F5',
      },
      fontFamily: {
        sans: ['"Cera Pro"', '"Nunito"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '8px',
        sm: '4px',
        lg: '12px',
        full: '9999px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- **CTA는 레드(#E3000B)** — LEGO 브랜드의 핵심 식별자
- **헤드라인은 weight 900 + uppercase** — 굵고 대문자 스타일이 정체성
- **노랑(#FFD700)은 연령 배지·보조 포인트** 전용
- **제품 카드에 반드시 연령/조각 수 배지** — LEGO 필수 정보
- **배경은 순백(#FFFFFF)** — 제품 이미지 대비 최대화

### DON'T

- **레드를 에러 색으로만 쓰지 않는다** — LEGO에서 레드는 긍정적 브랜드 색
- **노랑(#FFD700)을 배경 전면 사용하지 않는다** — 포인트 컬러 역할
- **border-radius 24px 이상 과도 사용 금지** — 장난감 브랜드라도 너무 둥글면 유치
- **폰트를 Comic Sans 계열로 대체하지 않는다** — Cera Pro는 정밀하고 현대적
- **다크 배경(#313131)을 기본으로 쓰지 않는다** — 밝고 활기찬 라이트 우선
