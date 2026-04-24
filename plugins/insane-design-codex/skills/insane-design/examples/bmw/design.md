---
slug: bmw
service_name: BMW
site_url: https://bmw.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#1C69D4"
primary_font: BMWTypeNext
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — BMW (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 BMW처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "BMWTypeNext", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1A1A1A; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #1C69D4; }
```

**절대 하지 말아야 할 것 하나**: BMW 파란색을 UI 전반에 과용하는 것. BMW의 마케팅 사이트는 거의 완전한 모노크롬(흑/백)이고, 파란색은 극도로 절제된 accent로만 나타난다. CSS 분석에서 chromatic 컬러가 단 하나도 포착되지 않을 만큼 억제되어 있다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://bmw.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | N/A |
| Token prefix | N/A — 커스텀 프로퍼티 시스템 미감지 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 플랫폼)
- **Design system**: BMW Group 내부 디자인 시스템
- **CSS architecture**: N/A (토큰 시스템 미노출)
- **Class naming**: N/A
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스트 (BMWTypeNext)
- **Canonical anchor**: `#1C69D4` — BMW 브랜드 블루 (CSS 파싱 데이터에 미포착, 브랜드 아이덴티티)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `BMWTypeNext` (BMW Group 독점)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

> **라이선스 주의**: `BMWTypeNext`는 BMW Group 독점 폰트. 외부 프로젝트에서는 `Barlow` 또는 `Heebo`가 시각적으로 유사한 오픈소스 대체재.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-3. Neutral Ramp

| Step | Hex | Count |
|---|---|---|
| 중간 회색 | `#8E8E8E` | 1회 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| 중간 회색 | `#8E8E8E` | 보조 텍스트, 구분선 |

> **참고**: BMW 마케팅 사이트의 CSS에서 chromatic 컬러가 전혀 감지되지 않음. 사이트는 흑/백/회색의 극도로 미니멀한 모노크롬 팔레트를 사용하며, 브랜드 블루는 로고와 아이콘에 한정됨.

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — radius 토큰이 CSS에서 추출되지 않음.

---

## 12. Components
<!-- SOURCE: manual -->

### CTA Button (Primary)

```html
<a href="#" class="bmw-btn bmw-btn--primary">
  Configure
</a>
```

| 속성 | 값 |
|---|---|
| background | `#1A1A1A` |
| color | `#FFFFFF` |
| border-radius | 0 (샤프 코너) |
| font-family | `BMWTypeNext` |
| font-weight | `700` |
| letter-spacing | `0.08em` |
| text-transform | `uppercase` |

### Navigation

```html
<nav class="bmw-nav">
  <div class="bmw-nav__logo">
    <!-- BMW 원형 로고 -->
  </div>
  <ul class="bmw-nav__items">
    <li class="bmw-nav__item">Models</li>
  </ul>
</nav>
```

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결, 위엄 있는 단문 | "The BMW 7 Series." |
| Primary CTA | 영어 중심, 행동형 | "Configure" / "Test Drive" |
| Secondary CTA | 정보 탐색형 | "Discover More" |
| Subheading | 스펙 + 감성 혼합 | "Efficiency meets performance." |
| Tone | 프리미엄, 절제, 독일식 정밀성 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* BMW — copy into your root stylesheet */
:root {
  /* Fonts */
  --bmw-font-family: "BMWTypeNext", "Helvetica Neue", Arial, sans-serif;
  --bmw-font-weight-normal: 400;
  --bmw-font-weight-bold: 700;

  /* Brand */
  --bmw-color-brand-blue: #1C69D4;

  /* Surfaces */
  --bmw-bg-page: #FFFFFF;
  --bmw-bg-dark: #1A1A1A;
  --bmw-text: #1A1A1A;
  --bmw-text-muted: #8E8E8E;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 레이아웃을 극도로 미니멀하게 — 흑/백/회색 중심
- Hero는 차량 전체 폭 사진으로 채우기
- CTA 버튼 모서리를 샤프하게 (radius: 0)
- letter-spacing `0.08em` 이상으로 프리미엄 feel 확보
- 중간 회색은 `#8E8E8E` 사용

### ❌ DON'T
- BMW 블루를 배경이나 버튼에 과용하지 말 것
- 둥근 버튼 모서리 쓰지 말 것 — BMW는 샤프 코너
- 컬러풀한 그라디언트나 장식 쓰지 말 것
- font-weight 300 이하 쓰지 말 것 — BMW의 미니멀은 얇음이 아니라 절제
