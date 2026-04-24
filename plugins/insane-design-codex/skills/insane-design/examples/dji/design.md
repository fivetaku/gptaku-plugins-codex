---
slug: dji
service_name: DJI
site_url: https://www.dji.com
fetched_at: 2026-04-13
default_theme: mixed
brand_color: "#1E9DF7"
primary_font: Open Sans
font_weight_normal: 400
token_prefix: .dui-*
---

# DESIGN.md — DJI (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 DJI처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'Open Sans', 'PingFang SC', 'Microsoft YaHei',
               'Helvetica Neue', Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 (다크 기본) */
:root { --bg: #3C3E40; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 파랑 (Buy 버튼) */
:root { --brand: #1E9DF7; }
```

**절대 하지 말아야 할 것 하나**: DJI 버튼 시스템을 단일 컬러로 단순화하는 것. DJI는 `#3C3E40` 다크 회색 primary 버튼 + `#1E9DF7` 파란 buy 버튼을 명확하게 구분한다. 이 이중 구조를 하나로 합치면 구매 전환 신호가 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.dji.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes |
| CSS files | 다수 외부 CSS + DUI 컴포넌트 라이브러리 |
| Token prefix | `.dui-*` (DJI UI Component Library) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Vue.js 기반 (글로벌 이커머스)
- **Design system**: DUI (DJI UI Component Library) — `.dui-btn`, `.dui-btn-buy`, `.dui-btn-primary` 등
- **CSS architecture**: 클래스 기반 컴포넌트 + BEM-ish
- **Default theme**: mixed (다크 다크 `#3C3E40` + 흰 마케팅 섹션 교차)
- **Font loading**: Google Fonts — `Open Sans` (400, 500, 600), 커스텀 `Dji` 폰트
- **Canonical anchor**: `#1E9DF7` — `.dui-btn-buy` 배경색으로 명시. buy CTA 전용

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `Open Sans` (11회 사용, 구글 폰트)
- **Brand font**: `Dji` (3회 — 로고, 헤드라인 전용 커스텀 폰트)
- **Weight system**: 300(light), 400(regular), 500(medium), 600(semibold), 700(bold), 800(extrabold)

```css
body {
  font-family: 'Open Sans', 'PingFang SC', 'Microsoft YaHei',
               'Helvetica Neue', 'Hiragino Sans GB',
               'WenQuanYi Micro Hei', Arial, sans-serif;
  font-weight: 400;
}

.hero-heading {
  font-family: 'Dji', 'PingFang SC', 'Microsoft YaHei', Arial, sans-serif;
}
```

> **다국어 최적화**: DJI 폰트 스택에는 중국어(PingFang SC, Microsoft YaHei), 일본어(Hiragino) 폰트가 포함된다. 글로벌 이커머스 필수 패턴.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight | 폰트 |
|---|---|---|---|
| Hero Display | clamp(40px, 6vw, 80px) | 700–800 | Dji |
| Section Heading | 32px–48px | 600 | Open Sans |
| Card Title | 18px–22px | 600 | Open Sans |
| Body | 14px–16px | 400 | Open Sans |
| Caption | 12px | 300–400 | Open Sans |
| Button | 16px | 600 | Open Sans |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand

| Hex | 역할 | 출처 |
|---|---|---|
| `#1E9DF7` | Buy CTA 버튼 배경 | .dui-btn-buy |
| `#1392ED` | Buy 버튼 그라디언트 끝 | |
| `#4CB5FF` | Buy 버튼 hover 시작 | |

### Primary Button (다크 회색)

| Hex | 역할 | 출처 |
|---|---|---|
| `#3C3E40` | Primary/Normal 버튼 | .dui-btn-primary |
| `#303233` | 버튼 그라디언트 끝 | |
| `#545759` | 버튼 hover | |

### Neutrals

| Hex | 역할 |
|---|---|
| `#FFFFFF` | 텍스트, 라이트 배경 |
| `#3C3E40` | 다크 배경 / primary btn |
| `#555555` | 보조 텍스트 |
| `#EFEFEF` | 연한 배경 |

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
<!-- SOURCE: auto+manual -->

| 역할 | Radius |
|---|---|
| Button | 2px (DJI는 거의 직각) |
| Card | 4px–8px |
| Input | 2px |
| Modal | 8px |

> DJI 버튼의 `border-radius: 2px` — 군사/기술 장비 브랜드의 샤프한 엣지.

---

## 09. Shadows
<!-- SOURCE: manual -->

| 레이어 | CSS |
|---|---|
| Card | `box-shadow: 0 4px 12px rgba(0,0,0,.2)` |
| Dropdown | `box-shadow: 0 8px 24px rgba(0,0,0,.25)` |
| Modal | `box-shadow: 0 16px 48px rgba(0,0,0,.35)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| All transitions | `all .3s ease` (DJI 기본) |
| Button hover | 200ms ease |
| Image fade | 300ms ease |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 풀 블리드 항공 영상/사진, 텍스트 오버레이 중앙
- **제품 페이지**: 스펙 사이드바 + 제품 이미지 레이아웃
- **다크 + 라이트 교차**: 다크 섹션(#3C3E40) ↔ 흰 섹션 교차
- **컨테이너**: `max-width: 1200px; margin: 0 auto; padding: 0 20px`
- **Nav**: sticky, 반투명 다크 배경

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Buy Button (브랜드 파랑 CTA)

```css
.dui-btn-buy {
  background: #1E9DF7;
  background-image: linear-gradient(-180deg, #1E9DF7 0%, #1392ED 100%);
  color: #FFFFFF;
  border: none;
  border-radius: 2px;
  height: 46px;
  font-size: 16px;
  padding: 15px 32px;
  transition: all .3s ease;
}
.dui-btn-buy:hover {
  background-image: linear-gradient(-180deg, #4CB5FF 0%, #1392ED 100%);
}
```

### Primary Button (다크 회색)

```css
.dui-btn-primary {
  background: #3C3E40;
  background-image: linear-gradient(-180deg, #3C3E40 0%, #303233 100%);
  color: #FFFFFF;
  border: none;
  border-radius: 2px;
  height: 46px;
  font-size: 16px;
  padding: 15px 32px;
}
.dui-btn-primary:hover {
  background-image: linear-gradient(-180deg, #545759 0%, #303233 100%);
}
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: 기술 우월성, 모험. "See the world from above."
- **스펙**: 정밀 수치. "48MP Hasselblad Camera", "15.4 miles range"
- **CTA**: "Buy" / "Explore" — 단순 명확
- **어조**: 기술적 권위 + 드론 파일럿 커뮤니티 감성

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* DJI Design System — Drop-in */
:root {
  --dui-brand-blue:  #1E9DF7;
  --dui-brand-hover: #4CB5FF;
  --dui-btn-dark:    #3C3E40;
  --dui-btn-darker:  #303233;

  --color-bg-dark: #3C3E40;
  --color-bg-page: #FFFFFF;
  --color-fg:      #FFFFFF;
  --color-fg-dark: #212121;
  --color-subtle:  #555555;
  --color-muted:   #EFEFEF;

  --font-primary: 'Open Sans', 'PingFang SC', 'Helvetica Neue', Arial, sans-serif;
}

body {
  font-family: var(--font-primary);
  font-weight: 400;
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
        dji: {
          blue:    '#1E9DF7',
          'blue-hover': '#4CB5FF',
          dark:    '#3C3E40',
          darker:  '#303233',
          hover:   '#545759',
        },
        neutral: {
          900: '#212121',
          700: '#555555',
          100: '#EFEFEF',
        },
      },
      fontFamily: {
        sans: ['Open Sans', 'PingFang SC', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        btn: '2px',
        card: '4px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Buy 버튼은 반드시 `#1E9DF7` 파랑 — 구매 신호
- Primary 버튼은 `#3C3E40` 다크 회색 — 탐색/정보 버튼
- 두 버튼의 역할 구분 유지 (블루=구매, 다크=탐색)
- 다크 배경 섹션과 흰 섹션 교차
- 기술 스펙 수치 정밀하게 — DJI 신뢰도의 핵심
- 버튼 radius는 2px — 기술/군사 장비 샤프함

### DON'T

- 두 버튼 시스템을 하나로 통합 — 구매 전환 신호 손실
- 버튼에 큰 radius — DJI는 거의 직각
- Buy 버튼 색상을 다른 컬러로 변경
- 화려한 파스텔 — DJI는 테크 다크

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| DJI는 단색 버튼 | 다크 primary + 파란 buy 이중 구조 |
| 버튼에 큰 radius | 2px 거의 직각 버튼 |
| 라이트 테마만 | 다크 섹션과 교차가 기본 패턴 |
