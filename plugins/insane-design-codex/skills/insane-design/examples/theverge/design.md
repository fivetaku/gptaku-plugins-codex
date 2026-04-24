---
slug: theverge
service_name: The Verge
site_url: https://www.theverge.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#5200FF"
primary_font: Poly Sans
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — The Verge (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 The Verge처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Poly Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #131313; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #5200FF; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 컬러를 보라(#5200FF)로 두지 않고 민트(#3CFFD0)를 primary로 쓰는 것. #3CFFD0은 보조 악센트이고 CTA·링크 등 인터랙션 기준은 보라다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.theverge.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | N/A |
| Token prefix | N/A (no --* token prefix detected) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (SSR, `__polySans_*` next/font hashed 클래스명)
- **Design system**: 인-하우스 (토큰 prefix 없음)
- **CSS architecture**: utility-class + scoped module (Tailwind 아님)
- **Default theme**: dark (검정 배경 기반, 편집 섹션별 컬러 교차)
- **Font loading**: Next.js `next/font` — `__polySans_9afc27`, `__fkRomanStandard_cfceed`, `__manuka_62afb5` 해시 클래스
- **Typography layers**: Poly Sans (UI), FK Roman Standard (body 기사), Manuka (display 헤드라인)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary UI font**: `Poly Sans` (Commercial Type, 유료 라이선스)
- **Editorial body**: `FK Roman Standard` (Florian Karsten, 유료)
- **Display headline**: `Manuka` (Klim Type Foundry, 유료) — Impact fallback 지정
- **Mono**: `Poly Sans Mono` (같은 패밀리)
- **Weight normal / bold**: `400` / `700`

```css
/* UI */
body {
  font-family: "__polySans_9afc27", "__polySans_Fallback_9afc27", Helvetica, Arial, sans-serif;
  font-weight: 400;
}
/* 기사 본문 */
.article-body {
  font-family: "__fkRomanStandard_cfceed", "__fkRomanStandard_Fallback_cfceed", Georgia, serif;
  font-weight: 400;
}
/* 대형 헤드라인 */
.headline-display {
  font-family: "__manuka_62afb5", "__manuka_Fallback_62afb5", Impact, Helvetica, sans-serif;
  font-weight: 900;
}
```

> **라이선스 주의**: 세 폰트 모두 유료 라이선스. 대체재: UI → `Inter`, 기사 본문 → `Source Serif 4`, 대형 헤드 → `Bebas Neue` (무료).

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Display XL | Manuka | ~72–96px | 900 | 0.95 | -0.02em |
| Section Heading | Poly Sans | 32–48px | 700 | 1.1 | -0.015em |
| Card Title | Poly Sans | 18–22px | 700 | 1.25 | -0.01em |
| Body UI | Poly Sans | 15–16px | 400 | 1.6 | 0 |
| Article Body | FK Roman Standard | 17–18px | 400 | 1.75 | 0 |
| Caption / Meta | Poly Sans | 12–13px | 500 | 1.4 | 0.02em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Verge Purple | `#5200FF` | CTA 버튼, 링크 악센트, 브랜드 identity |
| Verge Mint | `#3CFFD0` | 보조 악센트, 섹션 구분 포인트 |
| Deep Green | `#309875` | 카테고리 태그 (science/environment) |
| Near-Black | `#131313` | 기본 배경 |
| Off-White | `#E9E9E9` | 보조 배경, 경계선 |
| Light Purple | `#EEE6FF` | 퍼플 섹션 배경 tint |
| Lavender | `#A980FF` | 퍼플 lighter variant |

### Semantic Roles

| 역할 | Hex | 용도 |
|---|---|---|
| Page BG | `#131313` | body 배경 |
| Card BG | `#1A1A1A` | 카드 표면 |
| Border | `#313131` | 섹션 경계 |
| Text Primary | `#FFFFFF` | 헤드라인, 본문 |
| Text Muted | `#636363` | 부제목, 메타 정보 |
| Text Secondary | `#4A4A4A` | 비활성 레이블 |
| CTA Primary | `#5200FF` | 버튼 primary |
| Accent Mint | `#3CFFD0` | 하이라이트 링크 |
| Error / Live | `#EE0033` | 속보·라이브 배지 |

---

## 07. Spacing
<!-- SOURCE: manual -->

> The Verge는 별도 토큰 없이 4px 베이스 그리드 사용.

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘·텍스트 간격 |
| sm | 8px | 인라인 요소 간격 |
| md | 16px | 컴포넌트 내부 패딩 |
| lg | 24px | 카드 내부 패딩 |
| xl | 32px | 섹션 수직 간격 |
| 2xl | 48px | 주요 섹션 사이 |
| 3xl | 64px | hero 패딩 |
| 4xl | 96px | 최상위 레이아웃 여백 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| none | 0px | 뉴스 카드 (엣지 디자인) |
| sm | 2px | 태그 배지 |
| md | 4px | 버튼 |
| lg | 8px | 이미지 컨테이너 (선택적) |
| pill | 999px | 카테고리 칩 |

---

## 09. Shadows
<!-- SOURCE: manual -->

> The Verge는 다크 배경이라 shadow 최소 사용. 오버레이/드롭다운에 한정.

| 이름 | 값 | 용도 |
|---|---|---|
| dropdown | `0 4px 20px rgba(0,0,0,0.5)` | 네비게이션 드롭다운 |
| modal | `0 8px 40px rgba(0,0,0,0.8)` | 모달/오버레이 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 140ms | hover 상태 전환 |
| duration-base | 240ms | 카드 트랜지션 |
| duration-slow | 400ms | 섹션 진입 |
| easing-standard | `cubic-bezier(0.4,0,0.2,1)` | 대부분 애니메이션 |
| easing-enter | `cubic-bezier(0,0,0.2,1)` | 요소 등장 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **그리드**: 12컬럼 기반, 최대 너비 1280px, 좌우 패딩 clamp(16px, 4vw, 64px)
- **카드 레이아웃**: 4-col (desktop), 2-col (tablet), 1-col (mobile) 뉴스 그리드
- **Hero**: full-bleed 이미지 + 오버레이 텍스트 (모바일 stack)
- **섹션 교차**: 다크/퍼플/민트 배경 섹션이 교대 (editorial choice)
- **사이드바**: sticky 광고 콘텐츠 패널, 좌측 메인 760px + 우측 280px

---

## 12. Components
<!-- SOURCE: manual -->

### 뉴스 카드

```html
<article class="news-card">
  <a href="..."><img ... /></a>
  <div class="card-body">
    <span class="category-tag">TECH</span>
    <h2 class="card-title">...</h2>
    <p class="card-meta">By Author · 2h ago</p>
  </div>
</article>
```

```css
.news-card { background: #131313; border-bottom: 1px solid #313131; }
.category-tag {
  font-family: "Poly Sans", sans-serif;
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: #3CFFD0; /* mint accent for tech category */
}
.card-title { font-size: 18px; font-weight: 700; color: #FFFFFF; line-height: 1.25; }
.card-meta { font-size: 12px; color: #636363; }
```

### CTA 버튼

```css
.btn-primary {
  background: #5200FF;
  color: #FFFFFF;
  font-family: "Poly Sans", sans-serif;
  font-size: 14px; font-weight: 700;
  padding: 10px 20px;
  border-radius: 4px;
  border: none; cursor: pointer;
  transition: background 140ms;
}
.btn-primary:hover { background: #6B1FFF; }
```

### 카테고리 칩

```css
.category-chip {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em;
  background: #5200FF; color: #FFFFFF;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 간결·직접적, 최대 10단어. 동사형 시작 ("Google confirms...", "Apple says...")
- **리드**: 1문장으로 결론 먼저 (inverted pyramid)
- **섹션 레이블**: 전부 대문자 + wide letter-spacing (ex: TECH, SCIENCE, AI)
- **CTA 문구**: 단순 동사 ("Read more", "Watch now", "Subscribe")
- **태그**: 2–3단어, 소문자 kebab (ex: artificial-intelligence, apple-watch)

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand */
  --brand: #5200FF;
  --accent-mint: #3CFFD0;
  --accent-green: #309875;

  /* Surface */
  --bg: #131313;
  --bg-card: #1A1A1A;
  --bg-section-alt: #000000;

  /* Text */
  --fg: #FFFFFF;
  --fg-muted: #636363;
  --fg-secondary: #4A4A4A;

  /* Border */
  --border: #313131;
  --border-strong: #4A4A4A;

  /* Status */
  --live: #EE0033;

  /* Spacing (4px grid) */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;

  /* Radius */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
  --radius-pill: 999px;
}

body {
  font-family: "Poly Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  font-size: 15px;
  line-height: 1.6;
  background: var(--bg);
  color: var(--fg);
  -webkit-font-smoothing: antialiased;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: '#5200FF',
        'brand-hover': '#6B1FFF',
        'accent-mint': '#3CFFD0',
        'accent-green': '#309875',
        'bg-base': '#131313',
        'bg-card': '#1A1A1A',
        'border-default': '#313131',
        'text-muted': '#636363',
        'live': '#EE0033',
      },
      fontFamily: {
        sans: ['"Poly Sans"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
        serif: ['"FK Roman Standard"', 'Georgia', 'serif'],
        display: ['Manuka', 'Impact', 'Helvetica', 'sans-serif'],
        mono: ['"Poly Sans Mono"', 'Courier New', 'monospace'],
      },
      borderRadius: {
        DEFAULT: '4px',
        sm: '2px',
        lg: '8px',
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

- **보라(#5200FF)를 CTA·인터랙션에 사용**한다 — 브랜드 identity의 핵심
- **민트(#3CFFD0)는 보조 악센트**로만 — 카테고리 태그, 포인트 underline
- **배경은 #131313** (pure black #000000 아님) — 더 따뜻하고 읽기 편함
- **헤드라인은 Manuka 또는 Poly Sans Bold** — 무게감 있는 뉴스 톤
- **카드 경계는 border-bottom 1px #313131** — shadow 대신 라인으로 구분

### DON'T

- **민트(#3CFFD0)를 primary 버튼 색으로 쓰지 않는다** — 보조 역할, 독립 CTA 금지
- **흰 배경에 검정 텍스트** 조합을 default로 쓰지 않는다 — The Verge는 다크 퍼스트
- **Poly Sans를 weight 300으로 쓰지 않는다** — 뉴스 미디어 특성상 400 이상
- **둥근 모서리(radius > 8px) 과다 사용 금지** — 엣지 있는 디자인이 정체성
- **빨간(#EE0033)을 브랜드 컬러로 오해하지 않는다** — Live/속보 전용 시그널 컬러
