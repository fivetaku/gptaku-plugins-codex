---
schema_version: 3.1
slug: tinybird
service_name: Tinybird
site_url: https://www.tinybird.co
fetched_at: 2026-04-20
default_theme: dark
brand_color: "#27F795"
primary_font: Roboto Mono
font_weight_normal: 400
token_prefix: "--primary, --primary-dark + Tailwind scale"

bold_direction: "Data-Native Terminal"
aesthetic_category: "Developer Brutalism"
signature_element: code_first_terminal
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Tinybird (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Tinybird의 공식 사이트(`www.tinybird.co`)는 real-time analytics infra라는 포지셔닝을 극단적 **Data-Native Terminal** 비주얼로 풀어냈다. near-black `#0A0A0A` 바닥 위에 **neon green `#27F795`** 단 하나의 primary와 **dark primary `#008060`** (semantic var `--primary-dark`)로 이원화, 전 사이트가 터미널 / log stream / 7-segment display를 시각적 레퍼런스로 가져온다. 가장 특이한 점은 `sevenSegment` 폰트 패밀리가 별도 로드되어 있어 Bloomberg-terminal 스타일의 시간 표시나 실시간 숫자를 실제로 그려준다는 것.

컬러 시스템은 `#27F795` bright-green primary 외에도, 데이터 상태 표시용 amber/red/cyan 보조 팔레트가 있다 — `#F5C451`(amber), `#EC6D62`(red), `#61C454`(green-soft), `#00C1FF`(cyan). 이들은 각각 warning / error / success / info 계열 상태 표시에 쓰인다. bg는 `#0A0A0A`부터 `#151515`, `#202020`, `#262626` 4-5단 dark neutral로 계단을 만들고, fg는 `#FFFFFF`와 `#FFFFFF50` 두 가지로만 운영 — 정말 데이터 UI처럼 high-contrast + sparse gray.

타이포그래피는 **Roboto Mono**(primary)와 **Fira Mono**(secondary)가 축이고, 일반 Roboto는 거의 보조 역할이다. 즉 모든 marketing 텍스트가 mono로 렌더되어 "우리는 code와 terminal이 native인 회사"라는 메시지를 준다. 여기에 `sevenSegment`라는 LCD-style 디스플레이 폰트가 숫자 강조에 쓰인다. weight는 300/400/500/700/bold — 보통 400 또는 500이 body, 700이 강조.

레이아웃은 Next.js + Tailwind 기반이지만, 시각적으로는 terminal/IDE의 chrome을 그대로 끌어온다. Section border가 `1px solid #1E1E1E`로 정확하게 그려지고, `#303347` 같은 blueprint-paper dark accent도 등장한다. hero는 대부분 `query` 예제 + live streaming data dashboard 스크린샷.

인터랙션은 매우 제한되어 있다. hover는 border-color change + green text glow 정도. scale/rotate 거의 없음. "터미널 UI가 과한 애니메이션을 쓰지 않는다"는 일관성.

### Key Characteristics

- Neon green `#27F795` + dark green `#008060` 이원화 primary
- true-black-ish `#0A0A0A` bg base
- Roboto Mono + Fira Mono (모든 텍스트를 mono로)
- sevenSegment LCD 디스플레이 폰트 (숫자 강조)
- amber/red/cyan 데이터 상태 팔레트
- high-contrast white + 50% muted only
- Terminal chrome 연출 + blueprint accent `#303347`
- 모션 최소 (정보 밀도 우선)

### BOLD Direction Summary

> **BOLD Direction**: Data-Native Terminal — 모든 텍스트를 mono + 숫자는 LCD 폰트
> **Aesthetic Category**: Developer Brutalism
> **Signature Element**: code_first_terminal — query / stream / LCD 숫자가 hero
> **Code Complexity**: medium — Tailwind + mono-first type + sevenSegment

---

## 01. Quick Start

```css
:root {
  --primary: #27F795;
  --primary-dark: #008060;
  --bg-base: #0A0A0A;
  --bg-elev: #151515;
  --bg-card: #202020;
  --border: #262626;
  --fg: #FFFFFF;
  --fg-muted: rgba(255,255,255,0.5);
  --blueprint: #303347;
}
```

```css
body {
  font-family: "Roboto Mono", "Fira Mono", ui-monospace, monospace;
  font-weight: 400;
  font-size: 14px;
  background: var(--bg-base);
  color: var(--fg);
}
.lcd-number { font-family: "sevenSegment", "Roboto Mono", monospace; }
```

```css
/* Signature green outline CTA */
.btn-primary {
  background: transparent;
  border: 1px solid #27F795;
  color: #27F795;
  padding: 10px 20px;
  border-radius: 4px;
  font-family: "Roboto Mono", monospace;
  font-weight: 500;
  transition: all .15s ease;
}
.btn-primary:hover {
  background: rgba(39,247,149,0.1);
  box-shadow: 0 0 24px rgba(39,247,149,0.2);
}
```

**절대 하지 말 것 하나**: Tinybird body에 sans-serif(Inter/Roboto) 쓰지 말 것 — 모든 marketing 텍스트가 mono로 렌더되는 게 핵심. sans로 바꾸는 순간 Tinybird가 아니라 Supabase가 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.tinybird.co` |
| Fetched | 2026-04-20 |
| Framework | Next.js + Tailwind |
| Signature font | `sevenSegment` (LCD display) |
| Theme | dark only |

---

## 03. Tech Stack

- Framework: Next.js
- CSS: Tailwind + custom CSS vars (`--primary`, `--primary-dark`)
- Typography: Roboto Mono + Fira Mono + sevenSegment (numbers)
- Theme: dark only
- Signature: mono-everywhere + LCD digit display

---

## 04. Font Stack

- **Primary Mono**: `Roboto Mono` (var `--font-roboto-mono`)
- **Secondary Mono**: `Fira Mono` (var `--font-fira-mono`)
- **LCD/Display**: `sevenSegment` — 숫자 · 시간 · metric
- **Sans (rare)**: `Roboto` (몇몇 UI)
- **Fallback**: monospace system
- **Weights**: 300 · 400 · 500 · 700 · bold

---

## 05. Typography Scale

| Token | Size | Weight | lh | Use |
|---|---|---|---|---|
| mono-xs | 11px | 400 | 1.5 | meta / ts |
| mono-sm | 13px | 400 | 1.5 | body |
| mono-base | 14px | 400 | 1.6 | default |
| mono-lg | 16px | 500 | 1.5 | emphasis |
| heading-3 | 20px | 700 | 1.3 | h3 |
| heading-2 | 28px | 700 | 1.2 | h2 |
| heading-1 | 40-56px | 700 | 1.1 | h1 |
| display-lcd | 56-72px | 400 | 1.0 | numbers (sevenSegment) |

---

## 06. Colors

### Signature

| Name | Hex | Use |
|---|---|---|
| primary (neon green) | `#27F795` | brand highlight · CTA outline |
| primary-dark | `#008060` | hover · filled variant · deep green |
| primary-tint | `#61C454` | success / soft green |
| pure-green | `#00FF00` | debug highlight (rarely) |

### Dark Stack

| Name | Hex | Use |
|---|---|---|
| bg-base | `#0A0A0A` | body bg |
| bg-elev | `#151515` | section tint |
| bg-card | `#202020` | card base |
| bg-card-2 | `#262626` | raised card |
| border | `#3C3C3C` | hairline |
| fg | `#FFFFFF` | text primary |
| fg-muted | `#FFFFFF50` (50% α) | text secondary |

### Data State Palette

| Name | Hex | Use |
|---|---|---|
| amber | `#F5C451` / `#F8AC49` | warning / pending |
| red | `#EC6D62` / `#FF8389` | error |
| cyan | `#00C1FF` | info |
| orange | `#FC9F5B` | alert |

### Blueprint Accent

| Name | Hex | Use |
|---|---|---|
| blueprint | `#303347` | data-panel divider |
| blueprint-transparent | `#30334700` | section scrim |
| navy | `#25283D` | deep dark accent |

### Anti-Brand Reference

| Hex | Note |
|---|---|
| `#800000` | **anti-brand** — 절대 사용 금지 선언 컬러 (phase1 내 frequency 34 등장하지만 never-used marker 역할) |

---

## 07. Spacing

Tailwind 4px base scale (1,2,3,4,6,8,12,16,24,32).

---

## 08. Radius

| Name | Value | Use |
|---|---|---|
| `rounded` | 4px | input / small CTA |
| `rounded-md` | 6px | button |
| `rounded-lg` | 8px | card |
| `rounded-xl` | 12px | panel |
| `rounded-full` | 9999px | avatar (rarely) |

Tinybird는 radius를 강하게 쓰지 않는다 — 4-8px 샤프 모서리가 terminal 느낌.

---

## 09. Shadows

| Name | Value | Use |
|---|---|---|
| shadow-sm | `0 1px 2px rgba(0,0,0,.3)` | subtle |
| shadow-glow-green | `0 0 24px rgba(39,247,149,.2)` | **signature green aura** |
| shadow-glow-amber | `0 0 16px rgba(245,196,81,.3)` | warning highlight |

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| hover transition | `.15s ease` | border/color |
| data stream | smooth scroll | log-stream UI |
| LCD digit flip | instant | number change |

---

## 11. Layout Patterns

### Hero — code_first_terminal
- bg: `#0A0A0A`
- headline: 40-56px Roboto Mono weight 700
- **Live query + streaming dashboard** 스크린샷
- CTA: green outline primary + ghost secondary

### Section Rhythm
- padding 64-96px
- max-width 1200-1280px
- alternating `#0A0A0A / #151515`

### Card
- bg `#202020`
- border 1px solid `#3C3C3C`
- radius 8px
- hover: border `#27F795`, glow

### Navigation
- height 56-64px (compact, data-UI style)
- bg `#0A0A0A` solid
- mono text

---

## 12. Responsive

sm 640 / md 768 / lg 1024 / xl 1280 / 2xl 1536.

---

## 13. Components

### Green Outline CTA (Signature)
```css
.btn-primary {
  background: transparent;
  border: 1px solid #27F795;
  color: #27F795;
  padding: 10px 20px;
  border-radius: 4px;
  font-family: "Roboto Mono", monospace;
  font-weight: 500;
  letter-spacing: 0.02em;
  transition: all .15s ease;
}
.btn-primary:hover {
  background: rgba(39,247,149,0.1);
  box-shadow: 0 0 24px rgba(39,247,149,.2);
}
```

### Filled Deep-Green CTA
```css
.btn-deep {
  background: #008060;
  color: #FFFFFF;
  padding: 10px 20px;
  border-radius: 4px;
  font-family: "Roboto Mono", monospace;
  font-weight: 500;
}
.btn-deep:hover { background: #27F795; color: #0A0A0A; }
```

### Terminal Panel
```css
.terminal {
  background: #0A0A0A;
  border: 1px solid #303347;
  border-radius: 8px;
  font-family: "Roboto Mono", monospace;
  font-size: 13px;
  padding: 16px;
  color: #27F795;
}
```

### LCD Number Display
```css
.lcd {
  font-family: "sevenSegment", "Roboto Mono", monospace;
  font-size: 64px;
  color: #27F795;
  letter-spacing: 0.05em;
  text-shadow: 0 0 12px rgba(39,247,149,.5);
}
```

---

## 14. Content Voice

| Label | Rule |
|---|---|
| Tone | data-native, precise, technical |
| Copy | mono-only (no serif, minimal sans) |
| Numbers | sevenSegment LCD 폰트로 강조 |
| CTA verb | "Start building" / "See demo" / "Read the docs" |

---

## 15. Drop-in CSS

```css
:root {
  --primary: #27F795;
  --primary-dark: #008060;
  --bg-base: #0A0A0A;
  --bg-elev: #151515;
  --bg-card: #202020;
  --border: #3C3C3C;
  --fg: #FFFFFF;
  --fg-muted: rgba(255,255,255,0.5);
  --blueprint: #303347;
  --font-mono: "Roboto Mono", "Fira Mono", monospace;
  --font-lcd: "sevenSegment", "Roboto Mono", monospace;
}
body {
  background: var(--bg-base);
  color: var(--fg);
  font-family: var(--font-mono);
  font-size: 14px;
}
.btn-primary {
  background: transparent; border: 1px solid var(--primary);
  color: var(--primary); padding: 10px 20px; border-radius: 4px;
  font-family: var(--font-mono); font-weight: 500;
}
```

---

## 16. Tailwind Config

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT:'#27F795', dark:'#008060' },
        data: { amber:'#F5C451', red:'#EC6D62', cyan:'#00C1FF' },
        blueprint: '#303347',
      },
      fontFamily: {
        mono: ['"Roboto Mono"','"Fira Mono"','monospace'],
        lcd: ['sevenSegment','"Roboto Mono"','monospace'],
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide

| Role | Token | Hex |
|---|---|---|
| Primary | `--primary` | `#27F795` |
| Primary dark | `--primary-dark` | `#008060` |
| Bg | `--bg-base` | `#0A0A0A` |
| Card | `--bg-card` | `#202020` |
| Border | `--border` | `#3C3C3C` |
| Text | `--fg` | `#FFFFFF` |
| Muted | `--fg-muted` | `#FFFFFF50` |

**Prompts**:
- **Hero**: "Tinybird style hero: bg #0A0A0A, headline 48px Roboto Mono weight 700 color white. Below: terminal panel bg #0A0A0A, border 1px #303347, radius 8px, displaying SQL query with #27F795 green syntax. LCD-style number beside using sevenSegment font at 64px color #27F795 with green glow text-shadow."
- **CTA**: "Tinybird CTA: transparent bg, 1px solid #27F795, #27F795 text, padding 10px 20px, radius 4px, Roboto Mono. Hover bg rgba(39,247,149,.1) + glow 0 0 24px rgba(39,247,149,.2)."
- **LCD Number**: "LCD display: sevenSegment font 64px color #27F795, text-shadow 0 0 12px rgba(39,247,149,.5), letter-spacing 0.05em."

---

## 18. DO / DON'T

### DO
- ✅ 모든 marketing 텍스트를 Roboto Mono로
- ✅ primary `#27F795` + primary-dark `#008060` 이원화 사용
- ✅ 숫자 강조에 sevenSegment LCD 폰트
- ✅ bg `#0A0A0A` 고수 (true black 아님)
- ✅ 모션 최소 — hover는 border+glow only

### DON'T
- body에 sans-serif 쓰지 말 것 — mono 필수
- green `#27F795`을 bg fill로 쓰지 말 것 — outline/text only
- radius 16px+ 크게 쓰지 말 것 — 4-8px 샤프 모서리 유지
- 색상을 primary 외 늘리지 말 것 — amber/red/cyan은 status용만
- Motion을 scale(1.04) 같은 Spotify 식으로 쓰지 말 것
