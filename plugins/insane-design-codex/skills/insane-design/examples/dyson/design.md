---
slug: dyson
service_name: Dyson
site_url: https://www.dyson.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0F70F0"
primary_font: system-ui
font_weight_normal: 400
token_prefix: --yxt-*
---

# DESIGN.md — Dyson (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Dyson처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: system-ui, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #212121; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0F70F0; }
```

**절대 하지 말아야 할 것 하나**: Dyson의 CTA 버튼에 회색 계열 배경을 쓰는 것. Dyson UI의 핵심 인터랙션 컬러는 `#0F70F0` 파란색이다. 흰 배경에 이 파란 CTA 하나만으로 Dyson의 프리미엄 클린 룩이 완성된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.dyson.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A bytes (Next.js SSR) |
| CSS files | 다수 외부 + 인라인, 토큰 기반 |
| Token prefix | `--yxt-*` (Yext DS 일부 적용) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (글로벌 이커머스 마케팅 사이트)
- **Design system**: 자체 Dyson DS + Yext 서치 위젯 (`--yxt-*` prefix)
- **CSS architecture**: 커스텀 프로퍼티 기반, Yext 검색 레이어 분리
- **Class naming**: BEM-ish + utility classes
- **Default theme**: light (흰 배경, 검정 텍스트, 파란 CTA)
- **Font loading**: system-ui 스택 (브랜드 커스텀 폰트 없음 — 시스템 폰트로 크로스플랫폼 일관성 확보)
- **Canonical anchor**: `#0F70F0` — `--yxt-color-brand-primary` 에 명시된 CTA 파랑

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Body font**: `system-ui` (플랫폼별 시스템 폰트)
- **Fallback**: `Segoe UI`, Roboto, Oxygen-Sans, Ubuntu, Cantarell, `Helvetica Neue`, sans-serif
- **Weight normal / bold**: `400` / `600`

```css
body {
  font-family: system-ui, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
               Cantarell, "Helvetica Neue", sans-serif;
  font-weight: 400;
}
```

> **특이사항**: Dyson은 별도 웹폰트를 서빙하지 않는다. 글로벌 이커머스 특성상 로딩 속도 우선 — 시스템 폰트 스택이 전략적 선택이다.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

CSS scale 토큰 없음. 실측 관찰 기반 스케일:

| 역할 | 크기 | Weight | 용도 |
|---|---|---|---|
| Hero Heading | clamp(32px, 5vw, 64px) | 600–700 | 제품 히어로 |
| Section Title | 32px–40px | 600 | 카테고리 헤딩 |
| Card Title | 18px–22px | 500–600 | 제품 카드 |
| Body | 14px–16px | 400 | 설명 텍스트 |
| Caption | 12px | 400 | 스펙, 법적 고지 |
| CTA Button | 14px–16px | 500–600 | 구매 버튼 |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand / CTA

| 역할 | Hex | 설명 |
|---|---|---|
| Brand Primary (CTA) | `#0F70F0` | --yxt-color-brand-primary, 모든 CTA 버튼 |
| Brand Hover | `#0C5ECB` | --yxt-color-brand-hover |

### Neutrals

| Hex | 역할 |
|---|---|
| `#FFFFFF` | 페이지 배경 |
| `#F5F5F5` | 섹션 배경 (alternating) |
| `#EFEFEF` | 카드 배경, 보조 버튼 |
| `#E8E8E8` | 호버 배경 |
| `#D7D7D7` | 보더 |
| `#555555` | 보조 텍스트 |
| `#212121` | --yxt-color-text-primary, 메인 텍스트 |

### Semantic

| 역할 | Hex |
|---|---|
| Danger (에러) | `#E64942` |
| Cancel bg | `#EFEFEF` |

---

## 07. Spacing
<!-- SOURCE: manual -->

8pt 그리드 기반 추정:

| Token | Value | 용도 |
|---|---|---|
| xs | 4px | 아이콘 간격 |
| sm | 8px | 인라인 패딩 |
| md | 16px | 컴포넌트 내부 |
| lg | 24px | 섹션 내부 |
| xl | 40px | 섹션 간격 |
| 2xl | 64px | 히어로 패딩 |
| 3xl | 96px | 랜딩 섹션 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 역할 | Radius | 용도 |
|---|---|---|
| Button small | 2px–4px | 소형 CTA |
| Button primary | 4px–6px | 주요 CTA |
| Card | 8px | 제품 카드 |
| Modal | 12px | 팝업 |
| Pill (alert) | 999px | SweetAlert 팝업 |

---

## 09. Shadows
<!-- SOURCE: manual -->

Dyson의 그림자는 미니멀. 제품 이미지가 시각적 깊이를 담당.

| 레이어 | CSS |
|---|---|
| Card hover | `box-shadow: 0 4px 16px rgba(0,0,0,.12)` |
| Modal / Drawer | `box-shadow: 0 8px 32px rgba(0,0,0,.16)` |
| Dropdown | `box-shadow: 0 2px 8px rgba(0,0,0,.10)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| Button hover | 150ms | ease |
| Card expand | 200ms | ease-out |
| Modal open | 280ms | ease-out |
| Image fade | 300ms | ease |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **제품 그리드**: `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))` — 이커머스 최적화
- **히어로**: 풀 블리드 이미지 + 텍스트 왼쪽 정렬 오버레이, 최대너비 1440px
- **섹션 래퍼**: `max-width: 1280px; margin: 0 auto; padding: 0 24px`
- **Nav**: sticky, `height: 64px`, 흰 배경, 하단 보더
- **카드**: aspect-ratio 유지 제품 이미지 + 텍스트 하단

---

## 12. Components
<!-- SOURCE: manual -->

### Primary CTA Button

```css
.btn-primary {
  background-color: #0F70F0;
  color: #FFFFFF;
  border: none;
  border-radius: 4px;
  padding: 12px 24px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 150ms ease;
}
.btn-primary:hover {
  background-color: #0C5ECB;
}
```

### Secondary / Cancel Button

```css
.btn-secondary {
  background-color: #EFEFEF;
  color: #555555;
  border: none;
  border-radius: 4px;
  padding: 10px 24px;
  font-weight: 600;
  cursor: pointer;
}
.btn-secondary:hover {
  background-color: #E8E8E8;
}
```

### Product Card

```css
.product-card {
  background: #FFFFFF;
  border-radius: 8px;
  overflow: hidden;
  transition: box-shadow 200ms ease;
}
.product-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,.12);
}
```

### SweetAlert Popup (브랜드 다이얼로그)

```css
/* 자체 swal 스타일 — 브랜드 파랑 CTA */
.swal-button {
  background-color: #0F70F0;  /* 브랜드 primary 동일 */
  color: #FFFFFF;
  border-radius: 5px;
  font-weight: 600;
  font-size: 14px;
  padding: 10px 24px;
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 기능 중심, 간결. "Engineered for performance." 형식
- **서브카피**: 기술 스펙을 소비자 언어로. "removes 99.97% of particles" 같은 구체 수치
- **CTA**: 직접적. "Shop now", "Buy", "Learn more"
- **어조**: 프리미엄, 자신감, 기술적 권위

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Dyson Design System — Drop-in */
:root {
  /* Brand */
  --yxt-color-brand-primary: #0F70F0;
  --yxt-color-brand-hover:   #0C5ECB;
  --yxt-color-brand-white:   #FFFFFF;

  /* Text */
  --yxt-color-text-primary: #212121;
  --color-text-secondary:   #555555;

  /* Background */
  --color-bg-page:     #FFFFFF;
  --color-bg-section:  #F5F5F5;
  --color-bg-card:     #FFFFFF;
  --color-bg-muted:    #EFEFEF;
  --color-bg-hover:    #E8E8E8;

  /* Border */
  --color-border:      #D7D7D7;

  /* Semantic */
  --color-danger:      #E64942;

  /* Spacing */
  --space-xs:  4px;
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  24px;
  --space-xl:  40px;
  --space-2xl: 64px;

  /* Radius */
  --radius-btn:  4px;
  --radius-card: 8px;
  --radius-modal: 12px;
}

body {
  font-family: system-ui, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
               Cantarell, "Helvetica Neue", sans-serif;
  font-weight: 400;
  background: var(--color-bg-page);
  color: var(--yxt-color-text-primary);
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
        brand: {
          DEFAULT: '#0F70F0',
          hover:   '#0C5ECB',
        },
        neutral: {
          50:  '#F5F5F5',
          100: '#EFEFEF',
          200: '#E8E8E8',
          300: '#D7D7D7',
          500: '#555555',
          900: '#212121',
        },
        danger: '#E64942',
      },
      fontFamily: {
        sans: ['system-ui', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      borderRadius: {
        btn:  '4px',
        card: '8px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- CTA 버튼은 반드시 `#0F70F0` 파란색 사용
- 배경은 `#FFFFFF` 또는 `#F5F5F5` — 흰 공간이 프리미엄감을 만든다
- 텍스트는 `#212121` 에서 `#555555` 범위 내로
- 버튼 radius는 4px–6px 미니멀하게
- 제품 이미지가 히어로 — 이미지 품질이 곧 디자인
- 기술 스펙 수치를 카피에 직접 사용 (신뢰도)

### DON'T

- CTA에 회색 배경 쓰기 — 파란색만이 Dyson CTA 정체성
- 화려한 그라디언트 배경 — Dyson은 클린 화이트
- 웹폰트 무리하게 추가 — 시스템 폰트가 전략적 선택
- 텍스트에 low-contrast 컬러 — 프리미엄 = 가독성
- 다수의 보조색 남용 — 파랑 하나로 충분
- 과도한 그림자 — 제품 사진이 깊이를 담당

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| Dyson은 검은 배경 | 마케팅 사이트는 흰 배경 기본. 다크 배경은 특정 제품 히어로에만 |
| 커스텀 폰트 필수 | system-ui 스택 사용. 폰트보다 이미지와 레이아웃이 핵심 |
| 빨간/노란 포인트 컬러 | Dyson 디지털 UI는 파란 단색 CTA |
