---
slug: salesforce
service_name: Salesforce
site_url: https://www.salesforce.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0176D3"
primary_font: Salesforce Sans
font_weight_normal: 400
token_prefix: --sds-g-*
---

# DESIGN.md — Salesforce (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Salesforce처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Salesforce Sans", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #032D60; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 블루 */
:root { --brand: #0176D3; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 블루를 단순 `#1B96FF` (밝은 파랑)로만 쓰는 것. Salesforce의 CTA는 `#0176D3` (진한 파랑)이고, `#1B96FF`는 라이트 모드 대비 텍스트 링크용이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.salesforce.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | `--sds-g-*` (SDS — Salesforce Design System) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · semantic_vars 추출 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React (Heroku/SF marketing stack) + Lightning Web Components
- **Design system**: SDS (Salesforce Lightning Design System) — `--sds-g-*` prefix
- **CSS architecture**: 3-tier 토큰: `--sds-g-color-brand-*` (global) → component
- **Default theme**: light (흰 배경, 네이비 텍스트)
- **Font loading**: 자체 호스트 — Salesforce Sans (전용 폰트)
- **Notable**: 브랜드 컬러 8단계 스케일 (inverse-1 ~ contrast-4) CSS 변수 노출

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary**: `Salesforce Sans` (Salesforce 전용, 재배포 불가)
- **Display**: `ITC Avant Garde Gothic` (일부 마케팅 헤드라인)
- **Fallback**: `Arial`, `sans-serif`
- **Weight**: `400` (normal), `700` (bold)

```css
body {
  font-family: 'Salesforce Sans', 'Helvetica Neue', Arial, sans-serif;
  font-weight: 400;
}
h1, h2, .headline {
  font-family: 'Salesforce Sans', Arial, sans-serif;
  font-weight: 700;
}
```

> **라이선스 주의**: Salesforce Sans 재배포 불가. 대체재: `Helvetica Neue` (거의 동일) 또는 `Inter`.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Display | Salesforce Sans | 48–64px | 700 | 1.1 | -0.01em |
| Section H2 | Salesforce Sans | 28–40px | 700 | 1.25 | -0.005em |
| Card Title | Salesforce Sans | 20–24px | 700 | 1.3 | 0 |
| Body | Salesforce Sans | 16–18px | 400 | 1.65 | 0 |
| Small / Caption | Salesforce Sans | 13–14px | 400 | 1.5 | 0 |
| Button | Salesforce Sans | 14px | 700 | 1 | 0.02em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Blue Scale (CSS 변수 직접 추출)

| CSS 변수 | Hex | 용도 |
|---|---|---|
| `--sds-g-color-brand-base-contrast-1` | `#1B96FF` | 라이트 모드 링크, 텍스트 |
| `--sds-g-color-brand-inverse-contrast-1` | `#0176D3` | **CTA 버튼**, 다크 배경 링크 |
| `--sds-g-color-brand-base-contrast-2` | `#0176D3` | 라이트 배경 secondary CTA |
| `--sds-g-color-brand-inverse-2` | `#032D60` | 다크 네이비 텍스트, 헤더 |
| `--sds-g-color-brand-inverse-3` | `#014486` | 중간 다크 블루 |
| `--sds-g-color-brand-inverse-4` | `#0B5CAB` | 버튼 hover |
| `--sds-g-color-brand-base-2` | `#EEF4FF` | 라이트 블루 배경 tint |
| `--sds-g-color-brand-base-3` | `#D8E6FE` | 블루 섹션 배경 |
| `--sds-g-color-brand-base-4` | `#AACBFF` | 밝은 블루 강조 |

### Semantic Surface

| 이름 | Hex | 용도 |
|---|---|---|
| Page BG | `#FFFFFF` | body 배경 |
| Navy | `#032D60` | 다크 섹션 텍스트·배경 |
| Blue Tint | `#EEF4FF` | 섹션 배경 |
| Text | `#032D60` | 기본 텍스트 (네이비) |

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
| pill | 999px | pill CTA |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card | `0 2px 8px rgba(0,0,0,.1)` | 카드 |
| elevated | `0 4px 20px rgba(0,0,0,.12)` | 모달, 드롭다운 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 150ms | hover 전환 |
| duration-base | 300ms | 드롭다운, 패널 |
| easing | `ease` | 표준 전환 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **최대 너비**: 1440px, 콘텐츠 1200px
- **Hero**: full-width, 네이비 배경 또는 블루 그라디언트 + 흰 텍스트
- **Feature Grid**: 3-col 아이콘 + 텍스트 (SaaS 기능 소개)
- **Customer Stories**: 2-col, 로고 월 (그레이스케일)
- **Pricing Table**: 3–4 col, 가장 인기 플랜 강조

---

## 12. Components
<!-- SOURCE: manual -->

### CTA 버튼 (파랑)

```css
/* --sds-g-color-brand-inverse-contrast-1: #0176D3 */
.btn-primary {
  background: #0176D3;
  color: #FFFFFF;
  font-family: 'Salesforce Sans', Arial, sans-serif;
  font-size: 16px; font-weight: 700;
  padding: 12px 24px;
  border-radius: 8px;
  border: none; cursor: pointer;
  transition: background 150ms ease;
}
.btn-primary:hover { background: #0B5CAB; }
```

### 아웃라인 버튼

```css
.btn-outline {
  background: transparent;
  color: #0176D3;
  border: 2px solid #0176D3;
  font-size: 16px; font-weight: 700;
  padding: 10px 22px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 150ms;
}
.btn-outline:hover { background: #EEF4FF; }
```

### Feature 카드

```css
.feature-card {
  background: #FFFFFF;
  border-radius: 12px;
  padding: 32px 24px;
  border: 1px solid #D8E6FE;
  transition: box-shadow 150ms;
}
.feature-card:hover { box-shadow: 0 8px 24px rgba(1,118,211,.12); }
.feature-card__icon { color: #0176D3; font-size: 32px; }
.feature-card__title { font-size: 20px; font-weight: 700; color: #032D60; }
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라inel**: "The #1 AI CRM" — 시장 1위 포지셔닝, 데이터 중심
- **서브**: "Grow your business with the platform trusted by..." — 사회적 증명
- **CTA**: "Start free trial" / "Watch demo" / "Contact sales"
- **톤**: 전문적·신뢰·기업 성과 중심

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* SDS Brand Tokens */
  --sds-g-color-brand-base-contrast-1: #1B96FF;
  --sds-g-color-brand-inverse-contrast-1: #0176D3;
  --sds-g-color-brand-inverse-2: #032D60;
  --sds-g-color-brand-inverse-4: #0B5CAB;
  --sds-g-color-brand-base-2: #EEF4FF;
  --sds-g-color-brand-base-3: #D8E6FE;

  /* Alias */
  --brand: #0176D3;
  --brand-dark: #032D60;
  --brand-hover: #0B5CAB;
  --brand-tint: #EEF4FF;

  /* Surface */
  --bg: #FFFFFF;
  --fg: #032D60;

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
  --radius-pill: 999px;
}

body {
  font-family: 'Salesforce Sans', 'Helvetica Neue', Arial, sans-serif;
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
        brand: '#0176D3',
        'brand-light': '#1B96FF',
        'brand-dark': '#032D60',
        'brand-hover': '#0B5CAB',
        'brand-tint': '#EEF4FF',
        'brand-tint2': '#D8E6FE',
        navy: '#032D60',
      },
      fontFamily: {
        sans: ['"Salesforce Sans"', '"Helvetica Neue"', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '8px',
        sm: '4px',
        lg: '16px',
        xl: '24px',
        pill: '999px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- **CTA는 #0176D3** (진한 파랑) — `#1B96FF`는 텍스트 링크용
- **CSS 변수명 `--sds-g-*` 원본 그대로 사용** — 축약하거나 일반화 금지
- **텍스트는 네이비 #032D60** — 순검정이 아닌 브랜드 네이비
- **블루 tint #EEF4FF를 배경으로** — 흰 섹션과 블루 섹션 구분
- **아이콘은 #0176D3 파랑** — feature 카드에서 브랜드 색 일관 사용

### DON'T

- **`#1B96FF`를 버튼 background로 쓰지 않는다** — 대비 불충분 (라이트 모드)
- **`--sds-g-*` prefix를 제거하지 않는다** — SDS 네임스페이스 필수
- **진한 검정(#000) 배경을 기본으로 쓰지 않는다** — Salesforce는 라이트 퍼스트
- **8단계 블루 스케일을 무시하고 임의 파랑 만들지 않는다** — 체계가 있음
- **무게 750 이상 weight를 일반 폰트에 지정하지 않는다** — 가독성 저하
