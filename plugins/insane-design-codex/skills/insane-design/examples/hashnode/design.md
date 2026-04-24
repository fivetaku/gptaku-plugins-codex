---
schema_version: 3.1
slug: hashnode
service_name: Hashnode
site_url: https://hashnode.com
fetched_at: 2026-04-20
default_theme: light
brand_color: "#1D52DE"
primary_font: suisseIntl
font_weight_normal: 400
token_prefix: --primary, --sidebar-*, --fa-*

bold_direction: "Editorial Developer"
aesthetic_category: "Editorial Developer"
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Hashnode (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Hashnode는 **개발자가 읽는 블로그 플랫폼**이라는 정체성을 시각적으로 정밀히 구현한다. 페이지는 light `#FFFFFF` 기반에 본문이 `#101828` 다크 슬레이트로 깔리고, 코드 구문 강조는 실제 GitHub dark syntax 색(`#A5D6FF` 문자열, `#7EE787` 태그/이름, `#F85149` 에러)을 정확히 재사용한다 — "코드는 코드처럼 보여야 한다"는 규율.

색상 전략은 **brand indigo `#1D52DE` 단일 앵커 + dual-theme primary**다. light 모드에서 primary는 `#1D52DE` deep indigo, dark 모드에서는 `#5288FF` bright blue로 전환. `--primary-foreground`는 항상 `#F5F9FF` near-white. sidebar UI (에디터 레이아웃)도 동일 primary 체계 공유 (`--sidebar-primary`). text 계층은 `#101828` (primary) → `#364153` (secondary) → `#D1D5DC` (muted)의 정교한 slate ramp.

타이포그래피는 Hashnode 자체 호스팅 변형 **suisseIntl** (Swiss International, 유료 — suisseIntl + suisseIntl Fallback + suisseMono). weight `200 / 400 / 500 / 600`을 주로 사용 — 200은 micro-text에 등장. 본문은 `16px` 기본, 긴 기사용 `18px` reading mode. 코드는 **suisseMono** 자체 호스팅.

레이아웃은 **reading-first**. prose max-width `680–768px`, 기사 페이지는 sidebar + main + TOC 3-col. hero는 큰 typography + 저자 정보 + 코드/링크 카드. tailwind 기반 utility (`.file\\:bg-transparent` 같은 escape class 관찰).

인터랙션은 Tailwind `--tw-shadow`로 shadow 처리 — 카드 rest `0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A`. subtle elevation + hover에 shadow 확장.

### Key Characteristics

- Light 기본 `#FFFFFF` + dark mode — dual theme primary
- Brand indigo `#1D52DE` (light) / `#5288FF` (dark)
- suisseIntl + suisseMono 자체 호스팅
- GitHub syntax color 재사용 (코드 구문)
- Reading-first 레이아웃 (prose 680–768px)
- Tailwind utility + shadcn 계열 token (`--primary`, `--sidebar-*`)

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Editorial Developer
> **Aesthetic Category**: Editorial Developer
> **Signature Element**: 이 사이트는 **light-default reading 레이아웃 + indigo primary dual-theme + GitHub syntax 재사용**으로 기억된다.
> **Code Complexity**: medium — Tailwind + shadcn + dual theme swap

---

## 01. Quick Start

> 5분 안에 Hashnode처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "suisseIntl","suisseIntl Fallback",
    system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-weight: 400;
  font-size: 16px;
}

/* 2. 배경 + 텍스트 (light default) */
:root {
  --background: #FFFFFF;
  --foreground: #101828;
  --muted-foreground: #364153;
  --border: #D1D5DC;
}
body { background: var(--background); color: var(--foreground); }

/* 3. Primary indigo (light) */
:root {
  --primary: #1D52DE;
  --primary-foreground: #F5F9FF;
}
.dark {
  --primary: #5288FF;   /* dark theme bright blue */
  --primary-foreground: #F5F9FF;
}
```

**절대 하지 말아야 할 것 하나**: body weight를 `500` 또는 `600`으로 두지 마라. Hashnode는 읽기 플랫폼이다. 본문 `400`, 헤드라인 `600` 가중치 계단을 지켜야 "읽히는 블로그" 느낌이 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://hashnode.com` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 추출 완료 |
| CSS files | 3개 외부 (`161KB + 2.5KB + 241KB` total ~404KB) |
| Token prefix | `--primary`, `--sidebar-*`, `--fa-*` (Font Awesome) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Tailwind CSS + shadcn/ui 계열
- **Design system**: shadcn tokens — `--primary`, `--muted`, `--border`, `--sidebar-*`, `--accent`
- **CSS architecture**: single-tier shadcn + Tailwind utility
  ```
  shadcn  (--primary, --foreground, --muted)    semantic alias
  tw      (.text-*, .bg-*, .p-*)                utility
  ```
- **Class naming**: Tailwind utility + escape (`.file\\:bg-transparent`)
- **Default theme**: light (`.dark` class로 dark swap)
- **Font loading**: suisseIntl + suisseMono 자체 호스팅 + Font Awesome 7
- **Canonical anchor**: `#1D52DE` (light) / `#5288FF` (dark)

---

## 04. Font Stack

- **Display/Body**: `suisseIntl` (Swiss International, 유료)
- **Code**: `suisseMono` (자체 호스팅)
- **Icons**: `Font Awesome 7 Pro` + `Font Awesome 7 Brands` + `Font Awesome 7 Jelly` + `Font Awesome 7 Jelly Fill`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --font-suisse-intl:
    "suisseIntl","suisseIntl Fallback",
    system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --font-suisse-mono:
    "suisseMono","suisseMono Fallback",
    ui-monospace,SFMono-Regular,Menlo,Monaco,
    Consolas,"Liberation Mono","Courier New",monospace;
}
body { font-family: var(--font-suisse-intl); }
code { font-family: var(--font-suisse-mono); }
```

> **라이선스 주의**: suisseIntl은 유료 라이선스 필요. 복제 시 `Inter` 또는 `Söhne` (유료) 대체.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height |
|---|---|---|---|
| caption | `12px` | 400 | 1.5 |
| small | `14px` | 400 | 1.5 |
| body | `16px` | 400 | 1.6 |
| reading | `18px` | 400 | 1.7 |
| lead | `20px` | 500 | 1.5 |
| h3 | `24px` | 600 | 1.3 |
| h2 | `32px` | 600 | 1.25 |
| h1 | `40px` | 600 | 1.2 |
| display | `56–64px` | 600 | 1.1 |

> ⚠️ Hashnode weight `200`이 존재 (1회) — 주로 fine-print나 ultra-subtle 라벨에. 일반 구현 시 무시 가능.

---

## 06. Colors

### 06-1. Brand (dual-theme primary)

| Token | Hex |
|---|---|
| `--primary` (light) | `#1D52DE` |
| `--primary` (dark) | `#5288FF` |
| `--primary-foreground` | `#F5F9FF` |
| `--sidebar-primary` (light) | `#1D52DE` |
| `--sidebar-primary` (dark) | `#5288FF` |
| `--sidebar-primary-foreground` | `#F5F9FF` |

### 06-3. Neutral Ramp (Tailwind slate)

| Step | Hex | Usage |
|---|---|---|
| 50 | `#F9FAFB` | subtle bg |
| 100 | `#F3F4F6` | muted bg |
| 300 | `#D1D5DC` | border |
| 500 | `#6A7282` | text muted |
| 600 | `#4A5565` | text secondary |
| 700 | `#364153` | text strong |
| 900 | `#101828` | text primary |
| white | `#FFFFFF` | page bg |
| black | `#000000` | extreme ink |

### 06-4. Accent Families (syntax/status)

| Family | Hex | Use |
|---|---|---|
| syntax-string | `#A5D6FF` | code string |
| syntax-tag | `#7EE787` | code tag/name |
| syntax-error | `#F85149` | error |
| syntax-keyword | `#FF7B72` | keyword |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--background` (light) | `#FFFFFF` | 페이지 |
| `--foreground` (light) | `#101828` | 본문 |
| `--primary` | `#1D52DE` | CTA / link |
| `--primary-foreground` | `#F5F9FF` | CTA text |
| `--muted` | `#F3F4F6` | 보조 배경 |
| `--muted-foreground` | `#6A7282` | 보조 텍스트 |
| `--border` | `#D1D5DC` | 기본 border |
| `--accent` | `#F3F4F6` | hover bg |
| `--destructive` | `#F85149` | error/delete |

### 06-6. Semantic Alias Layer

| Alias | Resolves to |
|---|---|
| `--sidebar-background` | `--background` |
| `--sidebar-foreground` | `--foreground` |
| `--sidebar-primary` | `--primary` |
| `--sidebar-border` | `--border` |

### 06-7. Dominant Colors

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#00000000` | 40 | transparent (UI) |
| 2 | `#FFFFFF` | 24 | page bg |
| 3 | `#0000001A` | 21 | shadow dim |
| 4 | `#101828` | 12 | text primary |
| 5 | `#364153` | 8 | text strong |
| 6 | `#D1D5DC` | ≥7 | border |
| 7 | `#A5D6FF` | code | syntax |
| 8 | `#7EE787` | code | syntax |

---

## 07. Spacing

Tailwind scale — 4px 배수.

| Token | Value |
|---|---|
| space-1 | `4px` |
| space-2 | `8px` |
| space-3 | `12px` |
| space-4 | `16px` |
| space-6 | `24px` |
| space-8 | `32px` |
| space-12 | `48px` |
| space-16 | `64px` |
| space-24 | `96px` |
| container | `1280px` |
| prose | `680–768px` |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| rounded-sm | `4px` | chip |
| rounded | `6px` | button, input |
| rounded-md | `8px` | card small |
| rounded-lg | `12px` | card 기본 |
| rounded-xl | `16px` | card large |
| rounded-full | `9999px` | avatar, pill |

---

## 09. Shadows

| Level | Value | Usage |
|---|---|---|
| shadow-sm | `0 1px 2px 0 rgba(0,0,0,0.05)` | subtle |
| shadow | `0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A` | card rest (Tailwind default) |
| shadow-md | `0 4px 6px -1px rgba(0,0,0,0.1)` | hover |
| shadow-lg | `0 10px 15px -3px rgba(0,0,0,0.1)` | popover |
| shadow-xl | `0 20px 25px -5px rgba(0,0,0,0.1)` | modal |

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| transition-fast | `150ms cubic-bezier(.4,0,.2,1)` | hover |
| transition-base | `200ms cubic-bezier(.4,0,.2,1)` | color/bg |
| transition-slow | `300ms` | modal/popup |

---

## 11. Layout Patterns

### Grid

- max-width container `1280px`
- prose `680–768px` (reading)
- 3-col (sidebar + main + TOC) for article

### Hero

- Pattern: `light bg + 큰 H1 + 듀얼 CTA + 블로그 커뮤니티 썸네일 그리드`
- Bg: `#FFFFFF` solid + subtle pattern
- H1: `suisseIntl 56–64px weight 600 ls -0.02em`

### Section Rhythm

```css
section { padding-block: 64px; padding-inline: 24px; max-width: 1280px; }
```

### Card

- bg `#FFFFFF` + border `1px solid #D1D5DC` + radius `12px` + padding `24px` + shadow default

### Navigation

- height `64px` fixed top
- bg `rgba(255,255,255,0.95)` + backdrop blur
- 로고 + 링크 + search + Write button CTA

---

## 12. Responsive Behavior

### Breakpoints (Tailwind default)

| Name | Value |
|---|---|
| sm | `≥ 640px` |
| md | `≥ 768px` |
| lg | `≥ 1024px` |
| xl | `≥ 1280px` |
| 2xl | `≥ 1536px` |

### Touch / Collapsing

- min tap `40px`
- nav 햄버거 &lt;768px
- 3-col → 1-col mobile

---

## 13. Components

### Buttons

```html
<button class="bg-primary text-primary-foreground rounded px-4 py-2">Start writing</button>
```

| Variant | bg | color | radius | padding |
|---|---|---|---|---|
| primary | `#1D52DE` | `#F5F9FF` | `6px` | `8px 16px` |
| ghost | transparent | `#101828` | `6px` | 동일 |
| outline | border `#D1D5DC` | `#101828` | `6px` | 동일 |

### Badges

- bg `#F3F4F6` / accent color light
- color `#101828`
- radius `9999px`
- font-size `12px` weight `500`
- padding `0 10px` height `20px`

### Cards

- bg `#FFFFFF`, border `1px solid #D1D5DC`, radius `12px`, padding `24px`, shadow-sm

### Navigation

- suisseIntl 14px weight 500
- CTA "Write" (primary) + "Sign up" (outline)

### Inputs

- height `40px`, padding `0 12px`
- bg `#FFFFFF` + border `1px solid #D1D5DC`
- radius `6px`
- focus `outline 2px solid #1D52DE`

### Hero

- H1 56px weight 600 color `#101828`
- sub 20px color `#364153`

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 커뮤니티 중심 | "Everything you need to build your blog" |
| Primary CTA | 동사+대상 | "Start writing" |
| Secondary CTA | Explore | "Explore blogs" |
| Subheading | 기능 + 커뮤니티 | "Home for technical writers" |
| Tone | 개발자 동료 화법 | — |

---

## 15. Drop-in CSS

```css
/* Hashnode — drop-in */
:root {
  --font-suisse-intl: "suisseIntl",system-ui,-apple-system,sans-serif;
  --font-suisse-mono: "suisseMono",ui-monospace,SFMono-Regular,Menlo,monospace;

  --background: #FFFFFF;
  --foreground: #101828;
  --muted: #F3F4F6;
  --muted-foreground: #6A7282;
  --border: #D1D5DC;

  --primary: #1D52DE;
  --primary-foreground: #F5F9FF;

  --destructive: #F85149;

  --radius: 6px;
  --radius-lg: 12px;
}
.dark {
  --background: #0A0A0A;
  --foreground: #F5F9FF;
  --primary: #5288FF;
  --border: #27272A;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Hashnode
module.exports = {
  theme: {
    extend: {
      colors: {
        background: 'var(--background)',
        foreground: 'var(--foreground)',
        primary: { DEFAULT:'var(--primary)', foreground:'var(--primary-foreground)' },
        muted: { DEFAULT:'var(--muted)', foreground:'var(--muted-foreground)' },
        border: 'var(--border)',
      },
      fontFamily: {
        sans: ['suisseIntl','system-ui','-apple-system'],
        mono: ['suisseMono','ui-monospace','SFMono-Regular'],
      },
      borderRadius: { DEFAULT:'6px', md:'8px', lg:'12px', xl:'16px', full:'9999px' },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary (light) | `--primary` | `#1D52DE` |
| Brand primary (dark) | `--primary` | `#5288FF` |
| CTA text | `--primary-foreground` | `#F5F9FF` |
| Background | `--background` | `#FFFFFF` |
| Text primary | `--foreground` | `#101828` |
| Text muted | `--muted-foreground` | `#6A7282` |
| Border | `--border` | `#D1D5DC` |

### Example Component Prompts

#### Hero

```
Hashnode 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: suisseIntl, 56px, weight 600, color #101828, ls -0.02em
- sub: 20px color #364153
- CTA primary: bg #1D52DE, color #F5F9FF, radius 6px, padding 8px 16px
- CTA ghost: bg transparent, color #101828, border none
- 듀얼 CTA 좌측 정렬
- 하단 블로그 card grid (3-col)
```

#### Card (blog)

```
Hashnode 블로그 카드를 만들어줘.
- bg #FFFFFF, border 1px solid #D1D5DC, radius 12px, padding 24px
- shadow 0 1px 3px 0 rgba(0,0,0,0.1)
- 제목 suisseIntl 20px weight 600
- 메타 14px color #6A7282
- hover shadow-md + border #9CA3AF
```

### Iteration Guide

- **색상** raw hex 금지 — shadcn token 체계 (`--primary`, `--muted`, `--border`).
- **폰트** suisseIntl 대체 시 Inter 사용.
- **dark mode** `.dark` 클래스로 root 토큰 swap.
- **reading-first** prose max 680–768px 고정.

---

## 18. DO / DON'T

### ✅ DO

- 본문 배경 `#FFFFFF` (light) · 본문 텍스트 `#101828`.
- primary CTA는 `#1D52DE` indigo, dark 테마에서 `#5288FF`로 swap.
- 본문 폰트 `suisseIntl` `16px` weight `400`.
- 헤드라인 weight `600`.
- 코드 블록은 GitHub dark syntax 재사용 (`#A5D6FF` string, `#7EE787` tag).
- shadcn/Tailwind token을 그대로 쓰기 — `--primary`, `--muted-foreground`.

### ❌ DON'T

- 본문 weight `500` 또는 `700` 금지 — 읽기 플랫폼답게 `400`.
- primary를 초록·보라 같은 다른 hue로 바꾸지 말 것 — indigo 고정.
- prose max-width `1024px` 이상 쓰지 말 것 — 가독성 파괴.
- raw hex 직접 쓰지 말 것 — shadcn token으로만.
- 카드 shadow 너무 강하게 하지 말 것 — subtle elevation.
