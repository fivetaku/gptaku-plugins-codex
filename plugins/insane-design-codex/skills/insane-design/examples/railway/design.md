---
schema_version: 3.1
slug: railway
service_name: Railway
site_url: https://railway.com
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#9A059A"
primary_font: Inter
font_weight_normal: 400
token_prefix: --mantine-*, --c1/c2/c3

bold_direction: "Retro-Futuristic"
aesthetic_category: "Retro-Futuristic"
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Railway (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Railway 홈페이지는 near-black #13111C 바탕에 보라-남색 구름 일러스트가 깔린 cinematic dark 테마다. 첫 인상은 'peaceful ship software'라는 카피와 함께 중앙에 뜨는 플립보드(flap) 타이머가 retro-futuristic 감성을 만든다. CTA는 Deploy →, Demo 두 개가 병치된다.

컬러 전략은 딥 퍼플 + 블루 gradient core + Mantine UI 기본 팔레트의 하이브리드다. 커스텀 토큰 --c1 #9A059A (magenta), --c2 #5909A9 (purple), --c3 #100095 (deep blue)가 CTA 그라디언트를 만들고, Mantine의 blue-0 ~ blue-9 ramp (#E7F5FF → #1971C2)가 UI 위젯에 쓰인다. 플립보드 배경은 --flap-bg #F4F1EC paper 톤, flip-bg는 #121118 ink.

타이포그래피는 Inter를 축으로 하되 JetBrains Mono가 flip 타이머/로그에 자주 등장한다. 본문 16px, H1은 ~56-72px weight 700으로 압도적이지 않은 대신 cinematic한 sub-copy가 공간을 지배한다. Mantine font-family monospace fallback을 별도로 정의한다.

레이아웃은 1200px 컨테이너 + 중앙 정렬 hero + 아래 product mockup dark panel이다. 섹션마다 구름/별 일러스트레이션이 background layer로 깔리고, 카드는 얇은 rgba(255,255,255,0.1) border + flip bg로 깊이를 만든다. 플립 타이머는 top/bottom 반으로 나뉜 --flip-center-border rgba(0,0,0,0.18)로 구현.

인터랙션은 플립 애니메이션 + scroll-triggered fade + hover color scale. 코드 복잡도는 high — 3D transform, intersection observer, stagger reveal 다수. Retro TV 감성을 위해 scanline noise / grain을 subtle하게 깔기도 한다.

### Key Characteristics

- Near-black #13111C
- Purple-blue gradient
- Flipboard timer
- Retro-futuristic
- Cinematic hero
- Cloud illustration

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Retro-Futuristic
> **Aesthetic Category**: Retro-Futuristic
> **Signature Element**: 이 사이트는 **밤하늘 구름 위의 플립보드 타이머**으로 기억된다.
> **Code Complexity**: high — Railway 홈페이지의 Mantine + 자체 플립 토큰 기반 다크 cinematic 디자인 시스템.

---

## 01. Quick Start

> 5분 안에 Railway처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: "Inter", ui-sans-serif, sans-serif;
  font-weight: 400;
  font-size: 16px;
}
.mono {
  font-family: "JetBrains Mono",
    ui-monospace, SFMono-Regular;
}

/* 2. 배경 + 텍스트 (dark) */
:root {
  --bg: #13111C;
  --bg-oatmeal: #13111c;
  --fg: #E5E7EB;
  --muted: #9CA3AF;
  --border: rgba(255,255,255,0.1);
}
body {
  background: var(--bg);
  color: var(--fg);
  font-feature-settings: "cv11";
}

/* 3. 브랜드 gradient */
:root {
  --c1: #9A059A; /* magenta */
  --c2: #5909A9; /* purple */
  --c3: #100095; /* blue */
  --brand:
    linear-gradient(135deg,
      var(--c1), var(--c2), var(--c3));
}

```

**절대 하지 말아야 할 것 하나**: Railway의 브랜드는 단일 hex가 아니라 #9A059A → #5909A9 → #100095 3-stop gradient다. CTA를 solid purple로 두지 마라. gradient 방향도 135deg 고정 — 바꾸면 retro 감성이 깨진다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | <code>https://railway.com</code> |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 230,275 bytes (Next.js SSR) |
| CSS files | 11개 외부, 1.3MB minified |
| Token prefix | <code>--mantine-*</code>, <code>--c1/--c2/--c3</code>, <code>--flap-*</code>, <code>--flip-*</code> |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Mantine UI (React)
- **Design system**: Mantine 기본 + Railway 자체 flip 토큰
- **CSS architecture**: Mantine CSS variables + scoped modules
- **Class naming**: Mantine + CSS Modules
- **Default theme**: <code>dark</code> (bg <code>#13111C</code>)
- **Font loading**: Inter + JetBrains Mono self-host + Google Fonts fallback
- **Canonical anchor**: <code>#9A059A</code> magenta (gradient start)
- **Extra**: Flipboard timer + cloud SVG background layer

---

## 04. Font Stack

- **Body/Display**: <code>Inter</code> (OFL)
- **Code/Mono**: <code>JetBrains Mono</code> (OFL)
- **Fallback**: <code>ui-sans-serif, system-ui</code>
- **Weights**: 400 / 500 / 600 / 700

---

## 05. Typography Scale

> Inter body 16px + JetBrains Mono for timer/logs. Hero H1 56-72px weight 700.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `body` | 16px | 400 | 1.5 | 0 |
| `caption mono` | 13px | 400 | 1.4 | 0 |
| `lead` | 18px | 400 | 1.5 | 0 |
| `H3` | 24px | 600 | 1.3 | -0.01em |
| `H2` | 36px | 700 | 1.2 | -0.02em |
| `Hero H1` | 56-72px | 700 | 1.05 | -0.03em |

---

## 06. Colors

> Magenta/Purple/Blue 3-stop gradient brand + Mantine neutral + oatmeal paper accent.

### Brand Gradient

| Token | Hex |
|---|---|
| `c1 magenta ★` | `#9A059A` |
| `c2 purple` | `#5909A9` |
| `c3 blue` | `#100095` |
| `purple-alt` | `#8145B5` |
| `indigo-dark` | `#381DBD` |

### Neutral Dark

| Token | Hex |
|---|---|
| `bg` | `#13111C` |
| `bg-oatmeal` | `#13111C` |
| `near-black` | `#08070C` |
| `flip-bg` | `#121118` |
| `text-muted` | `#9CA3AF` |
| `border-gray` | `#374151` |

### Paper / Flipboard

| Token | Hex |
|---|---|
| `flap-bg` | `#F4F1EC` |
| `surface-warm` | `#F9F3E9` |
| `surface-cream` | `#E7E5E3` |

### Mantine Blue (UI)

| Token | Hex |
|---|---|
| `blue-0` | `#E7F5FF` |
| `blue-3` | `#74C0FC` |
| `blue-5` | `#339AF0` |
| `blue-7` | `#1C7ED6` |

### Accent Extra

| Token | Hex |
|---|---|
| `clay` | `#D97757` |
| `google blue` | `#4285F4` |
| `mint` | `#95D0B4` |
| `ruby` | `#B62D2B` |

### Semantic Alias Layer

| Alias | Resolves to / Usage |
|---|---|
| `--bg-oatmeal` | #13111C — global bg token |
| `--flap-bg` | #F4F1EC — flipboard paper top |
| `--flap-border-color` | rgba(0,0,0,0.12) — paper edge |
| `--flip-bg` | #121118 — flipboard digit bg |
| `--flip-border-color` | rgba(255,255,255,0.1) — digit edge |
| `--flip-center-border` | rgba(0,0,0,0.18) — flip split line |
| `--mantine-color-body` | inherits bg-oatmeal |

### Dominant Colors (CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#08070C` | 14 | near-black bg |
| 2 | `#9CA3AF` | 5 | muted text |
| 3 | `#F9F3E9` | 5 | paper surface |
| 4 | `#E7E5E3` | 5 | surface cream |
| 5 | `#59497A` | 5 | purple accent |
| 6 | `#381DBD` | 4 | indigo |
| 7 | `#4A3D66` | 4 | purple muted |
| 8 | `#374151` | 3 | border |

---

## 07. Spacing

> Mantine 기본 spacing (xs/sm/md/lg/xl) + 1200px container.

container-width: 1200px · py-20 / py-24 · gap-4/gap-6

| Token | Value | Use |
|---|---|---|
| `mantine-xs` | 10px | tight chip |
| `mantine-sm` | 12px | button inner |
| `mantine-md` | 16px | card inner |
| `mantine-lg` | 20px | card large |
| `mantine-xl` | 32px | section inner |
| `py-20` | 80px | section |
| `py-24` | 96px | hero |
| `container` | 1200px | page width |

---

## 08. Radius

> Mantine defaults — xs(2) / sm(4) / md(8) / lg(16) / xl(32). 플립 타이머는 8px.

| Token | Value | Context |
|---|---|---|
| `mantine-xs` | 2px | chip |
| `mantine-sm` | 4px | input |
| `mantine-md` | 8px | button / flip |
| `mantine-lg` | 16px | card |
| `mantine-xl` | 32px | hero block |

---

## 09. Shadows

> 다크 테마라 shadow 거의 없음. 대신 rgba border glow 사용.

| Level | Usage | Value |
|---|---|---|
| `flip digit` | 센터 스플릿 | `inset 0 -1px 0 rgba(0,0,0,0.18)` |
| `card glow` | hover | `0 0 0 1px rgba(255,255,255,0.15)` |
| `gradient shadow` | CTA hover | `0 8px 24px rgba(154,5,154,0.3)` |

---

## 10. Motion

> 플립 애니메이션 + scroll stagger. <code>.3s cubic-bezier(.4,0,.2,1)</code> 기본.

| Pattern | Value | Use |
|---|---|---|
| `flip rotate` | `600ms ease-out` | flipboard digit flip |
| `scroll reveal` | `400ms` | IntersectionObserver stagger |
| `cta gradient` | `300ms` | hover brightness shift |
| `cloud parallax` | `scroll-linked` | background drift |

---

## 11. Layout Patterns

> 1200px + 중앙 정렬 hero + 전체 너비 cloud SVG background layer + dark product mockup.

### Grid System

- Container max-width: 1200px
- Grid type: CSS Grid + Mantine Container
- Columns: 12 (Mantine default)
- Gutter: 16-24px

### Hero

- Layout: 1-column centered + cloud background
- Background: #13111C + SVG cloud/star overlay
- H1: 56-72px / weight 700 / tracking -0.03em
- Max-width: 720px
- Pattern: ~90vh + flipboard timer center + dual CTA

### Section Rhythm

- Padding: 80-96px vertical
- Max-width: 1200px
- cloud SVG layer가 섹션 경계 흐리게

### Card Patterns

- Background: #121118 flip-bg 또는 #1E1F2A
- Border: 1px solid rgba(255,255,255,0.1)
- Radius: 8-16px
- Padding: 20-32px
- Shadow: 없음, glow on hover

### Navigation

- Type: horizontal + 드롭다운
- Position: sticky top
- Height: ~64px
- Background: rgba(19,17,28,0.8) + blur

### Content Width

- Prose: 720px
- Container: 1200px
- Sidebar: Docs용 240px

---

## 12. Responsive Behavior

> Mantine breakpoints (xs 36em / sm 48em / md 62em / lg 75em / xl 88em). Mobile-first.

### Breakpoints

| Name | Value | Description |
|---|---|---|
| xs | `< 576px` | mobile |
| sm | `≥ 576px` |  |
| md | `≥ 768px` | tablet |
| lg | `≥ 992px` | desktop nav |
| xl | `≥ 1200px` | container max |

### Collapsing Strategy

- **Touch targets**: button 40-48px
- **Nav collapse**: lg 이하 햄버거
- **Grid columns**: 3 → 2 → 1
- **Flipboard**: mobile 스케일 축소
- **Cloud BG**: mobile static, desktop parallax
- **First-class**: mobile-first Mantine

---

## 13. Components

> Gradient CTA + flipboard timer + dark product mockup + cloud illustration.

### .btn-gradient (Deploy)

_3-stop gradient CTA_

```html
<button style="background:linear-gradient(135deg,#9A059A,#5909A9,#100095);color:#FFF;border:0;border-radius:8px;padding:12px 24px;font-size:15px;font-weight:600;cursor:pointer;">Deploy →</button>
```

Spec:

- background: linear-gradient(135deg,#9A059A,#5909A9,#100095)
- color: white
- radius: 8px
- padding: 12px 24px
- weight: 600

### .btn-ghost (Demo)

_Secondary — ghost with border_

```html
<button style="background:transparent;color:#E5E7EB;border:1px solid rgba(255,255,255,0.2);border-radius:8px;padding:12px 24px;font-size:15px;font-weight:500;cursor:pointer;">Demo</button>
```

Spec:

- background: transparent
- border: 1px solid rgba(255,255,255,0.2)
- color: #E5E7EB

### .flipboard-digit

_retro flip 타이머 digit_

```html
<div style="display:inline-block;background:#121118;color:#F4F1EC;font-family:ui-monospace;font-size:40px;font-weight:700;padding:16px 12px;border-radius:8px;border:1px solid rgba(255,255,255,0.1);position:relative;">00<div style="position:absolute;left:0;right:0;top:50%;height:1px;background:rgba(0,0,0,0.3);"></div></div>
```

Spec:

- bg: #121118
- color: #F4F1EC
- font-family: mono
- center split: rgba(0,0,0,0.18)

---

## 15. Drop-in CSS

```css
/* Railway — copy into your root */
:root {
  --font-sans: "Inter", ui-sans-serif, system-ui;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular;

  /* Brand gradient */
  --c1: #9A059A;
  --c2: #5909A9;
  --c3: #100095;
  --brand-gradient: linear-gradient(135deg, var(--c1), var(--c2), var(--c3));

  /* Surfaces */
  --bg: #13111C;
  --bg-oatmeal: #13111C;
  --fg: #E5E7EB;
  --muted: #9CA3AF;
  --border: rgba(255,255,255,0.1);

  /* Flipboard */
  --flap-bg: #F4F1EC;
  --flap-border-color: rgba(0,0,0,0.12);
  --flip-bg: #121118;
  --flip-border-color: rgba(255,255,255,0.1);
  --flip-center-border: rgba(0,0,0,0.18);

  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-xl: 32px;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Railway-like
module.exports = {
  theme: {
    extend: {
      colors: {
        bg: { DEFAULT: '#13111C', oatmeal: '#13111C' },
        brand: { c1: '#9A059A', c2: '#5909A9', c3: '#100095' },
      },
      backgroundImage: {
        'brand-gradient': 'linear-gradient(135deg, #9A059A, #5909A9, #100095)',
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace'],
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand gradient start | `--c1` | `#9A059A` |
| Brand gradient mid | `--c2` | `#5909A9` |
| Brand gradient end | `--c3` | `#100095` |
| Background | `--bg` | `#13111C` |
| Text primary | `--fg` | `#E5E7EB` |
| Text muted | `--muted` | `#9CA3AF` |
| Border | `--border` | `rgba(255,255,255,0.1)` |

### Example Component Prompts

#### Hero

```
Railway 스타일 히어로:
- 배경: #13111C + cloud SVG layer
- H1: Inter 64px weight 700 color #E5E7EB, tracking -0.03em
- Sub: 18px #9CA3AF
- CTA primary: background linear-gradient(135deg,#9A059A,#5909A9,#100095) + radius 8px
- CTA ghost: transparent + border rgba(255,255,255,0.2)
```

#### Flipboard

```
Railway 플립보드 타이머:
- container: bg #F4F1EC paper
- digit: bg #121118 color #F4F1EC
- font: JetBrains Mono 40px weight 700
- center split: rgba(0,0,0,0.18) 1px
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본.
- **여백 조정 시**: §07의 spacing scale 단위로만.
- **새 컴포넌트 추가 시**: §13의 기존 패턴을 따를 것.

---

## 18. DO / DON'T

### ✅ DO

- 배경은 #13111C near-black + 구름 SVG overlay layer.
- CTA primary는 3-stop gradient linear-gradient(135deg, #9A059A, #5909A9, #100095).
- Flipboard 타이머는 --flip-bg #121118 + --flap-bg #F4F1EC paper 조합.
- 카드 border는 rgba(255,255,255,0.1) — 실선 grey 금지.
- mono 폰트가 필요한 곳은 반드시 JetBrains Mono로.

### ❌ DON'T

- CTA 배경을 solid #9A059A 단색으로 두지 말 것 — 반드시 3-stop gradient.
- gradient 각도를 바꾸지 말 것 — 135deg 고정.
- 본문 텍스트를 #FFFFFF white로 두지 말 것 — #E5E7EB warm off-white.
- flipboard digit bg를 #000000로 두지 말 것 — #121118.
- 다크 theme 카드 border를 solid #374151로 두지 말 것 — rgba(255,255,255,0.1).
- body weight를 300로 두지 말 것 — 400.
