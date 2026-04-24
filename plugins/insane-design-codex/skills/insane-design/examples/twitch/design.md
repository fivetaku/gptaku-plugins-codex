---
schema_version: 3.1
slug: twitch
service_name: Twitch
site_url: https://www.twitch.tv
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#9147FF"
primary_font: Inter
font_weight_normal: 400
token_prefix: ".tw-root--theme-dark / .tw-root--theme-light + BEM (.top-nav__*, .side-nav-*)"

bold_direction: "Streamer Purple"
aesthetic_category: "Refined SaaS"
signature_element: dual_theme_purple
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Twitch (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Twitch(`www.twitch.tv`)는 게임 스트리머 문화를 그대로 색으로 번역한 **Streamer Purple** 시그니처 — **`#9147FF`** primary와 그 hover pair **`#A970FF`** / dark-hover **`#772CE8`** 로 완성된다. 이 purple은 Slack의 aubergine과 완전히 다르다. 밝고 채도 높고 "게이밍 네온"에 가까운 컬러로, Twitch 플랫폼의 10대-20대 스트리머 시청자 정체성을 대변한다.

가장 특이한 건 **dual theme 시스템**이다. `.tw-root--theme-dark` / `.tw-root--theme-light`가 body/root에 얹혀 모든 컴포넌트 컬러가 완전히 두 트랙으로 재정의된다. Purple도 dark에서 `#A970FF`(밝게), light에서 `#5C16C5`(진하게) — 즉 **단일 브랜드 hex가 없고 theme pair로만 존재**. `.navigation-link__active-indicator`부터 `.top-nav__home-link-logo` 까지 거의 모든 요소가 dark/light 두 버전으로 CSS에 중복 선언되어 있다.

레이아웃은 Twitch 플랫폼의 확장판이다. `.top-nav__logo` bg가 진한 `#451093`(dark purple), 일반 `.top-nav`는 white/black swap. side nav는 `#EFEFF1`(light) / `#26262C`(dark) 회색 블록이고, 스트리머 promoted card의 그라데이션이 `#9147FF → #FF75E6`(purple→pink) 시그니처 — "라이브 콘텐츠가 있다"는 energy 표시.

소셜 통합 팔레트도 실제로 CSS에 박혀 있다. `.social-button__icon--facebook` `#3B5998`, `--twitter` `#000000`, `--reddit` `#FF4500`, `--vkontakte` `#45668E` — 진짜 brand color를 그대로 쓴다 (재해석 없이).

타이포는 **Inter** 주 폰트(`--font-display` 참조) + **Roobert**(Twitch 자체 커스텀) 병용, 소수 페이지에서 Tajawal/Noto Sans Arabic를 i18n에 사용. 여기 특이한 점은 weight가 400/500/600/700의 단조로운 scale이라는 것 — 스트리머 콘텐츠가 주인공이므로 typography hierarchy를 과도하게 주지 않음.

인터랙션은 SaaS 수준으로 안전하다. hover는 color change 위주, motion은 `.2s ease` transform. 과한 animation은 배제.

### Key Characteristics

- Twitch Purple `#9147FF` (dark scope: #A970FF bright / light scope: #5C16C5 deep)
- **dual theme system** (.tw-root--theme-dark / --theme-light)
- logo bg `#451093` deep purple
- Promoted gradient `#9147FF → #FF75E6` (purple→pink)
- Dark bg `#18181B` (zinc-900) / Light bg `#FFFFFF`
- Side nav `#EFEFF1` light / `#26262C` dark
- Inter + Roobert 병용
- 실제 브랜드 컬러 그대로 (facebook/reddit/twitter native)
- BEM 네이밍 (`.top-nav__*`, `.side-nav-*`, `.social-button__*`)

### BOLD Direction Summary

> **BOLD Direction**: Streamer Purple — dual theme으로 purple 주도권 유지
> **Aesthetic Category**: Refined SaaS (platform 규모)
> **Signature Element**: dual_theme_purple — dark/light pair로 #A970FF / #5C16C5 swap
> **Code Complexity**: medium — dual-theme CSS + BEM + social brand palette

---

## 01. Quick Start

```css
/* dark 기본 */
:root, .tw-root--theme-dark {
  --twitch-purple: #A970FF;
  --twitch-purple-hover: #BF94FF;
  --twitch-purple-deep: #8205B4;
  --bg: #18181B;
  --bg-elev: #1F1F23;
  --side-nav: #26262C;
  --fg: #EFEFF1;
  --fg-muted: #ADADB8;
}
.tw-root--theme-light {
  --twitch-purple: #5C16C5;
  --twitch-purple-hover: #772CE8;
  --twitch-purple-deep: #451093;
  --bg: #FFFFFF;
  --bg-elev: #F7F7F8;
  --side-nav: #EFEFF1;
  --fg: #0E0E10;
  --fg-muted: #53535F;
}
```

```css
body {
  font-family: var(--font-display, "Inter"),
               "Roobert", -apple-system, sans-serif;
  font-weight: 400;
  font-size: 14px;
  background: var(--bg);
  color: var(--fg);
}
```

```css
.btn-twitch {
  background: var(--twitch-purple);
  color: #FFFFFF;
  padding: 6px 12px;
  border-radius: 4px;
  font-weight: 600;
  transition: background .15s ease;
}
.btn-twitch:hover { background: var(--twitch-purple-hover); }
```

**절대 하지 말 것 하나**: purple을 한 hex로만 고정하지 마라 — Twitch는 dark/light scope에서 purple을 다르게 쓴다. `#9147FF` hardcode는 절반의 theme에서 잘못 보인다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.twitch.tv` |
| Fetched | 2026-04-20 |
| Framework | React (Twitch 자체 스택) |
| Theme | dark + light dual (`.tw-root--theme-*`) |
| Typography | Inter + Roobert |

---

## 03. Tech Stack

- **Framework**: React + Twitch 내부 컴포넌트
- **CSS**: BEM + dual theme scope
- **Typography**: Inter (`--font-display`) + Roobert (커스텀)
- **i18n**: Tajawal / Noto Sans Arabic (아랍어)
- **Theme**: `.tw-root--theme-dark` / `.tw-root--theme-light` root toggle
- **Social integration**: facebook/reddit/twitter/vkontakte native brand colors

---

## 04. Font Stack

- **Primary**: `Inter` (`--font-display`, 21회 사용)
- **Custom**: `Roobert` (Twitch 자체, 4-6회)
- **Arabic**: `Noto Sans Arabic` / `Tajawal`
- **Mono**: monospace system
- **Weights**: 400 · 500 · 600 · 700 (4단 단조로운 scale)

---

## 05. Typography Scale

| Token | Size | Weight | lh | Use |
|---|---|---|---|---|
| tiny | 11px | 400 | 1.4 | meta |
| caption | 12px | 400 | 1.5 | meta/tag |
| body | 14px | 400 | 1.5 | **Twitch body default (15px 아님)** |
| body-bold | 14px | 600 | 1.5 | emphasis |
| lead | 16px | 500 | 1.5 | lead |
| h3 | 20px | 600 | 1.3 | subsection |
| h2 | 24px | 700 | 1.2 | section |
| h1 | 32-40px | 700 | 1.1 | landing |
| display | 48-64px | 700 | 1.05 | hero |

---

## 06. Colors

### Signature Purple Pair (dual theme)

| Name | Hex | Scope |
|---|---|---|
| purple-light-scope | `#5C16C5` | light theme primary |
| purple-dark-scope | `#A970FF` | dark theme primary |
| purple-shared | `#9147FF` | cross-scope middle |
| purple-hover-light | `#772CE8` | light hover |
| purple-hover-dark | `#BF94FF` | dark hover |
| purple-deep | `#8205B4` | deepest / active |
| purple-logo-bg | `#451093` | `.top-nav__logo` bg |

### Dark Theme Ramp

| Name | Hex | Use |
|---|---|---|
| bg-dark | `#18181B` | body bg (zinc-900) |
| bg-elev | `#1F1F23` | card (Twitch 변형) |
| bg-raised | `#26262C` | side nav dark |
| divider | `#19171C` | subtle border |
| fg-light | `#EFEFF1` | text primary on dark |

### Light Theme Ramp

| Name | Hex | Use |
|---|---|---|
| bg-light | `#FFFFFF` | body bg |
| bg-alt | `#F7F7F8` | section bg |
| side-nav | `#EFEFF1` | side nav light |
| fg-dark | `#0E0E10` | text primary on light |
| divider | `#D9D8DD` | border |

### Promoted Gradient

| Name | Hex | Use |
|---|---|---|
| gradient-start | `#9147FF` | promoted card bg left |
| gradient-end | `#FF75E6` | promoted card bg right |
| alt-magenta | `#BE0078` | highlight variant |

### Social Brand Colors (native)

| Name | Hex |
|---|---|
| facebook | `#3B5998` |
| twitter | `#000000` |
| reddit | `#FF4500` |
| vkontakte | `#45668E` |

### Status / Alert

| Name | Hex | Use |
|---|---|---|
| red-beta | `#E91916` | `.top-nav__beta-badge` |
| red-beta-hover | `#BB1411` | hover |
| skip-link | `#990000` / `#FDF6E7` | a11y skip link |
| cyan | `#00A3A3` | live indicator variant |
| neon-green | `#00F593` | streamer accent |
| yellow | `#FAFA19` | highlight variant |
| pink | `#F093F9` | accent |

---

## 07. Spacing

Tailwind-like 4px base. tw-internal rem scale도 사용.

---

## 08. Radius

| Name | Value | Use |
|---|---|---|
| radius-xs | 4px | button / input |
| radius-md | 6px | chip |
| radius-lg | 8px | card |
| radius-pill | 9999px | avatar / tag |

Twitch는 Slack 처럼 radius로 성격 내지 않는다 — 4px이 기본.

---

## 09. Shadows

| Name | Value | Use |
|---|---|---|
| shadow-sm | `0 1px 2px rgba(0,0,0,.12)` | subtle |
| shadow-md | `0 4px 8px rgba(0,0,0,.16)` | card hover |
| shadow-lg | `0 12px 24px rgba(0,0,0,.24)` | modal |

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| hover transition | `.15s ease` | color / bg |
| nav active-indicator | `transform .2s ease` | translate |
| theme toggle | `.3s ease-in-out` | scope swap |

---

## 11. Layout Patterns

### Hero
- dark theme default — bg `#18181B`
- headline 40-64px weight 700 white
- promoted card with `#9147FF → #FF75E6` gradient
- dual CTA: purple primary + outline

### Section Rhythm
- padding 64-96px
- max-width 1440px
- dark/light swap 가능

### Card
- bg `#1F1F23` (dark) / `#FFFFFF` (light)
- border 1px solid `#26262C` / `#D9D8DD`
- radius 8px
- hover: brighten bg + purple border hint

### Top Navigation
- height 50-64px
- bg `#18181B` (dark) / `#FFFFFF` (light)
- `.top-nav__logo` bg `#451093` deep purple
- `.top-nav__home-link-logo` color `#BF94FF` dark / `#5C16C5` light

### Side Navigation
- width ~240px (24rem)
- bg `#26262C` dark / `#EFEFF1` light
- card hover bg `#26262C` / `#EFEFF1` deeper

---

## 12. Responsive

sm 640 / md 768 / lg 1024 / xl 1280. Twitch는 Desktop-first (스트리머 뷰어 경험).

---

## 13. Components

### Purple CTA (Primary)
```css
.btn-twitch {
  background: #9147FF;
  color: #FFFFFF;
  padding: 6px 12px;
  border-radius: 4px;
  font-weight: 600;
  transition: background .15s ease;
}
.tw-root--theme-dark .btn-twitch { background: #A970FF; }
.tw-root--theme-light .btn-twitch { background: #5C16C5; }
.btn-twitch:hover { background: #772CE8; }
.tw-root--theme-dark .btn-twitch:hover { background: #BF94FF; }
```

### Promoted Gradient Card (시그니처)
```css
.side-nav-card--promoted-collapsed,
.side-nav-promoted-followed-card__gradient {
  background: linear-gradient(#9147FF, #FF75E6);
  padding: 16px;
  border-radius: 8px;
  color: #FFFFFF;
}
```

### Navigation Link Active Indicator
```css
.navigation-link__active-indicator {
  background-color: #5C16C5;
  height: .2rem;
  margin-bottom: -.1rem;
  transform-origin: 0 0;
  transition: transform .2s ease;
}
.tw-root--theme-dark .navigation-link__active-indicator {
  background-color: #BF94FF;
}
```

### Beta Badge
```css
.top-nav__beta-badge {
  background: #E91916;
  color: #000000;
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 700;
}
.top-nav__beta-badge:hover { background: #BB1411; }
```

### Social Icon Button
```css
.social-button__icon--twitter { background: #000000; color: #FFF; }
.social-button__icon--facebook { background: #3B5998; color: #FFF; }
.social-button__icon--reddit { background: #FF4500; color: #FFF; }
.social-button__icon--vkontakte { background: #45668E; color: #FFF; }
```

---

## 14. Content / Copy Voice

| Label | Rule |
|---|---|
| Tone | casual, streamer-friendly, direct |
| Headline | 3-8 단어 action-oriented |
| CTA verb | "Start Watching" / "Follow" / "Subscribe" |
| Live indicator | "LIVE" red badge · pulse animation |

---

## 15. Drop-in CSS

```css
:root, .tw-root--theme-dark {
  --twitch-purple: #A970FF;
  --twitch-purple-hover: #BF94FF;
  --bg: #18181B;
  --side-nav: #26262C;
  --fg: #EFEFF1;
  --fg-muted: #ADADB8;
}
.tw-root--theme-light {
  --twitch-purple: #5C16C5;
  --twitch-purple-hover: #772CE8;
  --bg: #FFFFFF;
  --side-nav: #EFEFF1;
  --fg: #0E0E10;
  --fg-muted: #53535F;
}
body {
  font-family: "Inter","Roobert",-apple-system,sans-serif;
  background: var(--bg); color: var(--fg);
  font-size: 14px;
}
.btn-twitch {
  background: var(--twitch-purple); color: #FFFFFF;
  padding: 6px 12px; border-radius: 4px;
  font-weight: 600; transition: background .15s ease;
}
.btn-twitch:hover { background: var(--twitch-purple-hover); }
.promoted-gradient { background: linear-gradient(#9147FF,#FF75E6); }
```

---

## 16. Tailwind Config

```js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        twitch: {
          purple: { DEFAULT:'#9147FF', dark:'#A970FF', light:'#5C16C5', hover:'#772CE8', deep:'#451093' },
          pink: '#FF75E6',
          bg: { dark:'#18181B', light:'#FFFFFF' },
        },
      },
      fontFamily: {
        display: ['Inter','Roobert','sans-serif'],
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide

| Role | Token | Hex (dark / light) |
|---|---|---|
| Purple primary | `--twitch-purple` | `#A970FF` / `#5C16C5` |
| Purple hover | `--twitch-purple-hover` | `#BF94FF` / `#772CE8` |
| Bg | `--bg` | `#18181B` / `#FFFFFF` |
| Side nav | `--side-nav` | `#26262C` / `#EFEFF1` |
| Text | `--fg` | `#EFEFF1` / `#0E0E10` |
| Gradient start | — | `#9147FF` |
| Gradient end | — | `#FF75E6` |

**Prompts**:
- **Hero**: "Twitch dark hero: bg #18181B, headline 48px Inter weight 700 white. Promoted card with linear-gradient(#9147FF,#FF75E6), radius 8, padding 16. Dual CTA: purple #A970FF primary + outline secondary."
- **Promoted Gradient**: "Promoted card: linear-gradient(#9147FF → #FF75E6), radius 8, color white. Use for streamer promotion."
- **Purple CTA**: "Twitch CTA: bg #9147FF (or theme-scoped #A970FF/#5C16C5), color white, padding 6px 12px, radius 4, weight 600. Hover bg #772CE8 (#BF94FF dark scope)."
- **Dual Theme**: "Apply `.tw-root--theme-dark` or `.tw-root--theme-light` to root, and all tokens swap automatically."

---

## 18. DO / DON'T

### DO
- ✅ dual theme `.tw-root--theme-dark/light` scope로 purple 재매핑
- ✅ purple `#9147FF` cross-scope + dark `#A970FF` / light `#5C16C5` pair
- ✅ promoted card에 `#9147FF → #FF75E6` 그라데이션
- ✅ Inter + Roobert 병용
- ✅ social brand colors는 native 그대로
- ✅ radius 4-8px 유지

### DON'T
- Purple을 `#5C16C5` 한 hex로만 hardcode하지 말 것
- Slack aubergine `#4A154B` 계열 어두운 보라로 바꾸지 말 것 — Twitch purple은 밝고 채도 높음
- body font size를 16px로 키우지 말 것 — Twitch는 14px default
- `#000000` pure black bg로 쓰지 말 것 — `#18181B` zinc
- gradient를 `#9147FF → #A970FF` 같은 monopurple로 만들지 말 것 — pink `#FF75E6`까지 가야 Twitch
- weight 300 light 쓰지 말 것 — 400/500/600/700만 사용
