---
slug: arc
service_name: Arc Browser
site_url: https://arc.net
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#3139FB"
primary_font: Marlin Soft SQ
font_weight_normal: 400
token_prefix: --colors-*
---

# DESIGN.md — Arc Browser (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Arc처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Marlin Soft SQ", "Marlin Soft Basic", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

/* 2. 다크 배경 + 텍스트 */
:root { --bg: #000354; --fg: #FFFCEC; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 블루 */
:root { --brand: #3139FB; }
```

**절대 하지 말아야 할 것 하나**: `--colors-brandOffwhite` (#FFFCEC)를 배경으로만 쓰고 텍스트에 흰색(#FFFFFF)을 쓰는 것. Arc는 흰색 대신 따뜻한 크림(#FFFCEC/#FFFCEA)을 텍스트와 배경 모두에 사용한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://arc.net` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | `--colors-*` (brandBlue, brandRed, brandOffwhite, brandDarkBlue, brandDeepBlue) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · semantic_vars 추출 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React SPA + Stitches CSS-in-JS (hashed classname 패턴 `.c-bCeQxv-*`)
- **Design system**: 인-하우스 — `--colors-brand*` 시멘틱 토큰
- **CSS architecture**: Stitches variant system (`.c-bCeQxv-ebGbss-type-primaryLight`)
- **Default theme**: dark (deep navy #000354 기반)
- **Font loading**: 자체 호스트 — Marlin Soft SQ, ABC Favorit Mono, Exposure VAR, Space Mono
- **Notable**: 브랜드 색상 5종 CSS 변수에 직접 노출 (rare)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary**: `Marlin Soft SQ` (인-하우스 또는 라이선스 폰트) — 부드러운 기하학 sans
- **Secondary**: `Marlin Soft Basic` (같은 패밀리)
- **Display/Variable**: `Exposure VAR` — variable font 헤드라인
- **Mono**: `ABC Favorit Mono`, `Space Mono`
- **Accent**: `Sohne Breit` (확장형 헤드라인)
- **Weight normal / bold**: `400` / `700`

```css
body {
  font-family: "Marlin Soft SQ", "Marlin Soft Basic", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}
.headline {
  font-family: "Exposure VAR", "Sohne Breit Extrafett", sans-serif;
  font-weight: 900;
}
.mono {
  font-family: "ABC Favorit Mono", "Space Mono", monospace;
}
```

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Display | Exposure VAR | 72–100px | 750–900 | 0.9 | -0.03em |
| Section H2 | Marlin Soft SQ | 36–48px | 700 | 1.1 | -0.02em |
| Card Title | Marlin Soft SQ | 20–24px | 600 | 1.3 | -0.01em |
| Body | Marlin Soft SQ | 16–18px | 400 | 1.65 | 0 |
| Mono Code | ABC Favorit Mono | 13–14px | 400 | 1.5 | 0 |
| Label | Marlin Soft SQ | 12px | 500 | 1 | 0.04em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Palette (CSS 변수 직접 추출)

| CSS 변수 | Hex | 용도 |
|---|---|---|
| `--colors-brandBlue` | `#3139FB` | Primary CTA, 링크 |
| `--colors-brandDeepBlue` | `#2404AA` | Blue 더 어둡게 |
| `--colors-brandDarkBlue` | `#000354` | 페이지 배경 (deep navy) |
| `--colors-brandRed` | `#FB3A4D` | 액센트 레드 |
| `--colors-brandOffwhite` | `#FFFCEC` | 텍스트, 크림 배경 |

### 추가 시멘틱 컬러

| 이름 | Hex | 용도 |
|---|---|---|
| CTA Hover | `#2702C2` | 버튼 hover (primaryLightAlt) |
| Button Red | `#FF3333` | 레드 primary 버튼 |
| Blue Light | `#96C4FF` | 라이트 블루 악센트 |
| Offwhite Alt | `#FFFCEA` | 크림 배경 variant |
| Purple Tint | `#F0F1FF` | 라이트 섹션 배경 |

---

## 07. Spacing
<!-- SOURCE: manual -->

> Arc는 8px 기반 그리드. generous whitespace로 프리미엄 느낌.

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘 간격 |
| sm | 8px | 인라인 요소 |
| md | 16px | 컴포넌트 내부 |
| lg | 24px | 카드 패딩 |
| xl | 40px | 섹션 간격 |
| 2xl | 64px | 주요 섹션 |
| 3xl | 96px | hero 패딩 |
| 4xl | 120px | 최상위 레이아웃 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| sm | 6px | 작은 배지 |
| md | 12px | 버튼, 카드 |
| lg | 20px | 큰 카드, 패널 |
| xl | 28px | hero 카드 |
| pill | 999px | pill 버튼, 태그 |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card-navy | `0 8px 32px rgba(0,3,84,.4)` | 다크 배경 카드 |
| card-lift | `0 20px 60px rgba(0,3,84,.6)` | hover 상태 |
| glow-blue | `0 0 40px rgba(49,57,251,.4)` | 블루 글로우 효과 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 120ms | hover 전환 |
| duration-base | 240ms | 카드·패널 |
| duration-slow | 500ms | 섹션 진입 |
| easing-spring | `cubic-bezier(0.34,1.56,0.64,1)` | 튀는 spring 효과 |
| easing-standard | `cubic-bezier(0.4,0,0.2,1)` | 일반 전환 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **그리드**: 최대 너비 1200px, 좌우 패딩 clamp(20px, 5vw, 80px)
- **Hero**: full-viewport height, 중앙 정렬 텍스트, deep navy 배경
- **Feature section**: 2-col (텍스트 + 이미지/앱 데모) 교차 레이아웃
- **Download CTA**: 중앙 배치, 대형 pill 버튼 + 플랫폼 선택
- **배경 교차**: #000354(navy) ↔ #FFFCEC(offwhite) 섹션 교차

---

## 12. Components
<!-- SOURCE: manual -->

### CTA 버튼 (다운로드)

```css
.btn-download {
  background: #3139FB;
  color: #FFFCEC;
  font-family: "Marlin Soft SQ", sans-serif;
  font-size: 16px; font-weight: 700;
  padding: 14px 28px;
  border-radius: 999px;
  border: none; cursor: pointer;
  transition: background 120ms, transform 120ms;
}
.btn-download:hover {
  background: #2702C2;
  transform: translateY(-1px);
}
```

### 라이트 배경 버튼 (primaryLight)

```css
/* CSS 변수에서 추출: primaryLight type */
.btn-light {
  background: #FFFFFF;
  color: #2702C2;
  border-radius: 999px;
  padding: 12px 24px;
  font-weight: 700;
  border: none;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: "The browser that puts you first" — 사용자 중심 포지셔닝
- **서브**: 간결한 benefit 강조, 감성적 언어 사용
- **CTA**: "Download Arc for Mac" — 플랫폼 명시
- **Feature 설명**: 명사형 제목 + 2–3줄 설명

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand tokens (CSS 변수 직접 추출) */
  --colors-brandBlue: #3139FB;
  --colors-brandDeepBlue: #2404AA;
  --colors-brandDarkBlue: #000354;
  --colors-brandRed: #FB3A4D;
  --colors-brandOffwhite: #FFFCEC;

  /* Alias */
  --brand: var(--colors-brandBlue);
  --bg: var(--colors-brandDarkBlue);
  --fg: var(--colors-brandOffwhite);
  --cta-hover: #2702C2;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 40px;
  --space-2xl: 64px;
  --space-3xl: 96px;

  /* Radius */
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-pill: 999px;
}

body {
  font-family: "Marlin Soft SQ", "Marlin Soft Basic", -apple-system, BlinkMacSystemFont, sans-serif;
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
        brand: '#3139FB',
        'brand-deep': '#2404AA',
        'brand-navy': '#000354',
        'brand-red': '#FB3A4D',
        'brand-cream': '#FFFCEC',
        'cta-hover': '#2702C2',
      },
      fontFamily: {
        sans: ['"Marlin Soft SQ"', '"Marlin Soft Basic"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        mono: ['"ABC Favorit Mono"', '"Space Mono"', 'monospace'],
      },
      borderRadius: {
        DEFAULT: '12px',
        sm: '6px',
        lg: '20px',
        xl: '28px',
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

- **배경은 deep navy #000354** — 진짜 검정(#000) 아닌 짙은 네이비
- **텍스트는 크림 #FFFCEC** — 순백(#FFFFFF) 아닌 따뜻한 오프화이트
- **CTA 버튼은 pill 형태** (radius 999px) + 블루 배경 #3139FB
- **CSS 변수명 `--colors-brand*`** 그대로 사용 — prefix 일반화 금지
- **Spring easing** 적용 — Arc는 물리 기반 bouncy 애니메이션이 정체성

### DON'T

- **순흰색(#FFFFFF)을 body 배경으로 쓰지 않는다** — Arc는 다크 퍼스트
- **브랜드 레드(#FB3A4D)를 error 전용으로만 쓰지 않는다** — 악센트 디자인 역할
- **Exposure VAR 없이 Impact나 Arial Black을 헤드에 쓰지 않는다** — 전혀 다른 톤
- **네이비 배경에 글로우 없이 파랑 버튼 쓰지 않는다** — 배경과 구분 불가
- **텍스트에 순흰(#FFFFFF) 고집하지 않는다** — 크림(#FFFCEC)이 Arc의 정체성
