---
schema_version: 3.1
slug: notion
service_name: Notion
site_url: https://www.notion.so
fetched_at: 2026-04-20
default_theme: mixed
brand_color: "#9849E8"
primary_font: NotionInter
font_weight_normal: 400
token_prefix: --color-*, --font-*, --spacing-*, --shadow-*

bold_direction: "Warm Productivity"
aesthetic_category: "Editorial Magazine"
signature_element: section_transition
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Notion (Codex Edition)

---

## 00. Visual Theme & Atmosphere

Notion의 마케팅 홈은 **워드프로세서가 매거진이 된 느낌**을 전달한다. 순백 `#FFFFFF`이 아니라 **warm ink** 계열 `#31302E` 본문, `#191918` ink-black, `#F9F9F8` paper-cream 배경이 UI 전반의 기본 조합이다 (함정 #10 — warm neutral). 2026년 4월 현재 홈은 "Meet the night shift" 캠페인을 걸고 있으며, 이 때문에 `--color-background: var(--color-purple-100)` → 실제 렌더는 dark purple 무드로 전환된다. 즉 Notion은 **light가 default지만 캠페인 모멘트마다 섹션 단위 drastic dark 테마 전환**을 구사한다 — `section_transition`이 바로 이 사이트의 시그니처다.

색상 전략은 2계층으로 읽힌다. **Structural layer (gray ramp 9단계)** 가 거의 모든 UI — 네비, 카드, 테이블 셀, 푸터 — 를 덮는다. `--color-gray-100 #F9F9F8`에서 `--color-gray-900 #191918`까지 warm ink 톤이다 (`#F5F5F7` Apple 같은 cool neutral이 아니다). **Semantic layer (blue/purple/pink/orange/yellow/green/teal/red 8-family × 9 step)** 은 블록 태그, 태그 칩, 일러스트 illustration에만 제한적으로 등장한다. 브랜드 앵커로 선택되는 건 홈 캠페인에 맞춰 `#9849E8` (`--color-purple-500`) — night shift accent.

타이포그래피는 **NotionInter**(Notion이 자체 호스팅하는 Inter 계열 variable font)와 **Lyon Text**(Commercial Type의 유료 serif)의 **duo 시스템**이다. body는 NotionInter 400, H1은 Lyon Text — 이 이중 구성이 "Notion은 결국 문서 도구"라는 정체성을 반영한다. Weight는 `400 / 500 / 600 / 700` 4단계 + variable axis 용 `420 / 520 / 620 / 680`이 별도로 존재한다. 타이포 scale은 10단계 `--font-size-50` (12px) → `--font-size-1000` (76px)로 매우 넓게 펼쳐져 있으며, 큰 사이즈 (600 이상) 에는 letter-spacing 음수값 (`-0.046875em` ~ `-0.25em`)이 weight 별로 3-variant로 제공된다. 이 정도 세밀한 optical compensation은 매거진 레이아웃 전통이다. 코드용으로 **iA Writer Mono** (Information Architects, 유료 라이선스)를 쓴다.

레이아웃은 `1252px` 또는 `839px` max-width 2단 (sidebar-on / sidebar-off 구간), `1080px / 1280px / 1440px` 3단 breakpoint로 동작한다. spacing scale은 `--spacing-0` ~ `--spacing-160` 의 rem 단위 시스템 (`0 / 4 / 8 / 12 / 16 / 20 / 24 / 28 / 32 / 40 / 48 / 56 / 64 / 72 / 80 / 96 / 128 / 160`) — 4/8px 배수가 아닌 **spacing naming = px 값**을 그대로 씀. radius는 `--border-radius-200` (4px) ~ `--border-radius-900` (16px) + `--border-radius-round` (9999px) 10단. shadow는 3-layer 다층 (`--shadow-level-100/200/300`)으로 설계, 각각 2-3층의 opacity 스택.

인터랙션 모션의 특징은 **text-decoration-color transition** 을 광범위하게 씀 — `transition: text-decoration-color var(--motion-global-fade-out-duration)` 이 transition top 1-2위를 차지한다. 링크 underline이 "스르륵" 나타나고 사라지는 서브틸한 효과가 Notion UI 전체에 깔려 있다.

### Key Characteristics

- Warm neutral ink (`#31302E` text, `#191918` ink, `#F9F9F8` paper) — NOT cool gray
- Lyon Text serif + NotionInter sans 듀얼 시스템 — "매거진 + 워드프로세서"
- Section-level drastic theme transition — light ↔ dark 캠페인 모멘트
- 타이포 scale 10단 (12px → 76px) + weight별 letter-spacing 3-variant
- Color family 8종 × 9 step 구조 — illustration/태그 전용
- Spacing = px 값 그대로 네이밍 (`--spacing-16 = 1rem = 16px`)
- Radius 10단 + `round` (9999px)
- Shadow 3-level dual-layer stack
- Text-decoration-color transition 시그니처

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Warm Productivity
> **Aesthetic Category**: Editorial Magazine
> **Signature Element**: 이 사이트는 **warm ink 듀얼 타이포(Lyon Text + NotionInter)와 섹션 간 drastic 테마 전환**으로 기억된다.
> **Code Complexity**: medium — 다층 shadow stack + duration token + text-decoration transition, 애니메이션은 절제

---

## 01. Quick Start

> 5분 안에 Notion처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight — sans + serif 듀얼 */
body {
  font-family: "NotionInter", Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
  color: #31302E; /* warm ink */
}
h1, h2, h3 {
  font-family: "Lyon Text", Georgia, serif;
}

/* 2. 배경 + 텍스트 (warm neutral, NOT cool) */
:root {
  --bg: #FFFFFF;
  --paper: #F9F9F8;       /* --color-gray-100, warm cream */
  --ink: #31302E;         /* --color-gray-800 */
  --ink-strong: #191918;  /* --color-gray-900 */
}
body { background: var(--bg); color: var(--ink); }

/* 3. 브랜드 악센트 (현재 캠페인 = purple) */
:root { --brand: #9849E8; }    /* --color-purple-500 */
```

**절대 하지 말아야 할 것 하나**: 배경을 cool `#FFFFFF` + 본문을 pure `#000000`으로 두지 마라. Notion의 정체성은 **warm ink**다 — 본문은 `#31302E`(warm 800), 헤드라인은 `#191918` (warm 900), 페이퍼 배경은 `#F9F9F8`. 한 톤만 식혀도 즉시 Office 365 느낌이 된다 (함정 #10).

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.notion.so` |
| Fetched | 2026-04-20 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 264,268 bytes (Next.js SSR + campaign shell) |
| CSS files | 15개 외부, 총 약 804KB minified |
| Token prefix | `--color-*`, `--font-*`, `--spacing-*`, `--shadow-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (SSR, CSS Modules)
- **Design system**: 자체 토큰 시스템, 언어/지역별 폰트 분기 (serif-chinese-traditional, sans-vietnamese, sans-arabic, sans-hebrew 등 9종)
- **CSS architecture**: 2-tier with locale fallback
  ```
  primary   (--font-family-primary-*, --color-*-NNN)    raw value
  fallback  (--font-family-fallback-*)                  locale별 fallback
  semantic  (--color-background-*, --color-accent-*)    역할 alias, core 참조
  ```
- **Class naming**: CSS Modules + semantic (`.globalNavigation_globalNavigation__7c1YP`, `.button_button__atjat`, `.cardCompact_cardCompact__W2i4I`)
- **Default theme**: mixed — base `light` (bg `#FFFFFF`, warm ink), 캠페인 섹션 단위 `dark` 전환
- **Font loading**: 셀프 호스트 `NotionInter`, `Lyon Text`, `iA Writer Mono` (유료), locale fallback `Inter/Georgia/YuMincho/Songti/Nanum Myeongjo/Batang/Hiragino Mincho`
- **Canonical anchor**: 현재 홈 기준 `#9849E8` (`--color-purple-500`, campaign) — 평상시는 `#191918` ink-black이 실질 앵커

---

## 04. Font Stack

- **Display font (serif)**: `Lyon Text` (Commercial Type, 유료)
- **Body font (sans)**: `NotionInter` (자체 호스팅 Inter 변형, OFL 파생)
- **Code font**: `iA Writer Mono` (Information Architects, 유료)
- **Handwriting**: `Permanent Marker` (Google Fonts, OFL)
- **Emoji**: `Apple Color Emoji`
- **Locale fonts**: `Noto Sans Arabic`, `Noto Sans Hebrew`, Japanese/Chinese/Korean serif stack
- **Weight normal / bold**: `400` / `700` (중간 `500 / 600` 상시)
- **Variable axis weights**: `420 / 520 / 620 / 680`

```css
:root {
  --font-family-primary-sans: NotionInter;
  --font-family-primary-serif: "Lyon Text";
  --font-family-primary-mono: "iA Writer Mono";
  --font-family-fallback-sans: Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";
  --font-family-fallback-serif: Georgia,YuMincho,"Yu Mincho","Hiragino Mincho ProN","Hiragino Mincho Pro","Songti TC","Songti SC",SimSun,"Nanum Myeongjo",NanumMyeongjo,Batang,serif;
  --font-family-fallback-mono: Nitti,Menlo,Courier,monospace;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-variable-regular: 420;
  --font-weight-variable-medium: 520;
  --font-weight-variable-semibold: 620;
  --font-weight-variable-bold: 680;
}
body {
  font-family: var(--font-family-primary-sans), var(--font-family-fallback-sans);
  font-weight: var(--font-weight-regular);
}
h1, h2, h3 {
  font-family: var(--font-family-primary-serif), var(--font-family-fallback-serif);
}
```

> **라이선스 주의**: Lyon Text, iA Writer Mono 모두 상업 라이선스 필수. 복제 시 각각 `Georgia` / `ui-serif` 와 `JetBrains Mono` / `IBM Plex Mono`로 대체.

---

## 05. Typography Scale

| Token | Size (rem) | Size (px) | Line-height | Letter-spacing (weight 400) |
|---|---|---|---|---|
| `--font-size-50` | `0.75rem` | 12px | `1rem` (16px) | `0.0078125em` |
| `--font-size-100` | `0.875rem` | 14px | `1.25rem` (20px) | `0` |
| `--font-size-150` | `0.9375rem` | 15px | `1.25rem` (20px) | `0` |
| `--font-size-200` | `1rem` | 16px | `1.5rem` (24px) | `0` |
| `--font-size-300` | `1.125rem` | 18px | `1.75rem` (28px) | `-0.0078125em` |
| `--font-size-350` | `1.25rem` | 20px | `1.75rem` (28px) | `-0.0078125em` |
| `--font-size-400` | `1.375rem` | 22px | `1.75rem` (28px) | `-0.015625em` |
| `--font-size-500` | `1.625rem` | 26px | `2rem` (32px) | `-0.0390625em` |
| `--font-size-600` | `2rem` | 32px | `2.5rem` (40px) | `-0.0625em` (regular) / `-0.046875em` (semi/bold) |
| `--font-size-700` | `2.625rem` | 42px | `3rem` (48px) | `-0.125em` (regular) / `-0.09375em` (semi/bold) |
| `--font-size-800` | `3.375rem` | 54px | `3.5rem` (56px) | `-0.21875em` (regular) / `-0.1171875em` (semi/bold) |
| `--font-size-900` | `4rem` | 64px | `4rem` (64px) | `-0.171875em` (regular) |
| `--font-size-1000` | `4.75rem` | 76px | `5rem` (80px) | `-0.25em` (regular) |

> ⚠️ Notion은 **weight별 letter-spacing 3-variant** (regular/semibold/bold)를 사이즈 600 이상에서 분리 제공한다. Bold는 덜 음수, regular는 더 음수 — optical compensation이 매우 섬세하다 (함정 #13의 정석). 이걸 그냥 `-0.02em` 고정으로 쓰면 즉시 Notion처럼 안 보인다.

---

## 06. Colors

### 06-1. Brand (현재 캠페인 기준 — Purple)

| Token | Hex | Use |
|---|---|---|
| `--color-purple-100` | `#F8F5FC` | campaign bg tint (light mode) |
| `--color-purple-200` | `#EADBFA` | accent-muted, surface-accent-soft |
| `--color-purple-300` | `#D6B6F6` | surface-accent-soft-hover |
| `--color-purple-400` | `#AD6DED` | accent-muted |
| `--color-purple-500` | `#9849E8` | **canonical campaign accent** |
| `--color-purple-600` | `#7237AE` | accent-hover |
| `--color-purple-700` | `#562983` | accent-active |
| `--color-purple-800` | `#391C57` | — |
| `--color-purple-900` | `#1C0E2C` | — |

> 평상시(캠페인 없음) 앵커는 `--color-blue-500 #097FE8` 또는 `--color-gray-900 #191918` ink-black.

### 06-3. Neutral Ramp (warm ink system)

| Step | Hex | Role |
|---|---|---|
| `--color-gray-100` | `#F9F9F8` | paper cream |
| `--color-gray-200` | `#F6F5F4` | panel subtle |
| `--color-gray-300` | `#DFDCD9` | border subtle |
| `--color-gray-400` | `#A39E98` | muted text |
| `--color-gray-500` | `#78736F` | fg-secondary |
| `--color-gray-600` | `#615D59` | fg-tertiary |
| `--color-gray-700` | `#494744` | fg-strong |
| `--color-gray-800` | `#31302E` | **body text (canonical)** |
| `--color-gray-900` | `#191918` | **ink black (heading)** |

### 06-4. Accent Families (9 colors × 9 steps = 72 tokens)

| Family | 300 (soft) | 500 (mid) | 700 (strong) |
|---|---|---|---|
| Blue | `#93CDFE` | `#097FE8` | `#005BAB` |
| Purple | `#D6B6F6` | `#9849E8` | `#562983` |
| Pink | `#FFB5EB` | `#FF64C8` | `#9D2472` |
| Red | `#FF8B7C` | `#F64932` | `#B01601` |
| Orange | `#FFAD71` | `#FF6D00` | `#AB4A00` |
| Yellow | `#FFD786` | `#FFB110` | `#C78600` |
| Green | `#ABE5B8` | `#1AAE39` | `#0F6220` |
| Teal | `#83CBC9` | `#27918D` | `#126764` |

(각 family별로 100/200/300/400/500/600/700/800/900 9단계 완비 — 전체 72 tokens)

### 06-5. Semantic (surface + accent)

| Token | Resolves to | Usage |
|---|---|---|
| `--color-background-base` | `var(--color-white)` (`#FFFFFF`) | page background (light) |
| `--color-background-base-hover` | `var(--color-alpha-black-100)` | hover surface (light) |
| `--color-background-surface-neutral` | `var(--color-gray-200)` (`#F6F5F4`) | subtle neutral panel |
| `--color-background-surface-neutral-hover` | `var(--color-gray-300)` (`#DFDCD9`) | panel hover |
| `--color-background-surface-accent` | `var(--color-blue-400)` (`#62AEF0`) | CTA accent bg |
| `--color-background-surface-accent-hover` | `var(--color-blue-500)` (`#097FE8`) | CTA hover |
| `--color-background-surface-accent-focus` | `var(--color-blue-600)` (`#0075DE`) | CTA focus |
| `--color-background-surface-accent-active` | `var(--color-blue-700)` (`#005BAB`) | CTA active |
| `--color-accent` | `var(--color-blue-400)` (평상시) or `purple-500` (캠페인) | dynamic accent |
| `--color-background` | `var(--color-purple-100)` (현재 캠페인) | campaign override |
| `--color-foreground` | `var(--color-purple-500)` (현재 캠페인) | campaign ink override |

### 06-7. Dominant Colors (실제 DOM 빈도 — "Meet the night shift" 캠페인 반영)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#00000000` | 많음 | transparent utility |
| 2 | `#FFFFFF` | 많음 | light bg + campaign text |
| 3 | `#000000BF` | 6+ | play button overlay (75% black) |
| 4 | `#000000D9` | 3+ | play button hover (85% black) |
| 5 | `#2867B2` | 1 | LinkedIn share hover |
| 6 | `#3071AA` | 1 | Footer LinkedIn hover |
| 7 | `#0000001F` | 많음 | shadow base opacity |
| 8 | `#9849E8` | campaign | purple-500 accent (Campaign CTA) |
| 9 | `#31302E` | body | warm ink text |
| 10 | `#191918` | heading | ink black |

---

## 07. Spacing

네이밍: **`--spacing-N` 의 N = px 값**. scale 은 `0 / 4 / 8 / 12 / 16 / 20 / 24 / 28 / 32 / 40 / 48 / 56 / 64 / 72 / 80 / 96 / 128 / 160` (rem 환산 등록).

| Token | rem | px | Use case |
|---|---|---|---|
| `--spacing-0` | `0` | `0` | reset |
| `--spacing-4` | `0.25rem` | `4` | hairline gap |
| `--spacing-8` | `0.5rem` | `8` | tight inline |
| `--spacing-12` | `0.75rem` | `12` | button gap |
| `--spacing-16` | `1rem` | `16` | paragraph gap, default |
| `--spacing-20` | `1.25rem` | `20` | card inner gap |
| `--spacing-24` | `1.5rem` | `24` | section inner |
| `--spacing-28` | `1.75rem` | `28` | line-height companion |
| `--spacing-32` | `2rem` | `32` | section vertical |
| `--spacing-40` | `2.5rem` | `40` | — |
| `--spacing-48` | `3rem` | `48` | — |
| `--spacing-56` | `3.5rem` | `56` | — |
| `--spacing-64` | `4rem` | `64` | major section |
| `--spacing-80` | `5rem` | `80` | hero bottom padding |
| `--spacing-96` | `6rem` | `96` | — |
| `--spacing-128` | `8rem` | `128` | hero vertical |
| `--spacing-160` | `10rem` | `160` | oversized margin |

**주요 alias**:

- `--spacing-block-l` → `32px` (block-level large)

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `--border-radius-200` | `0.25rem` (4px) | 작은 chip |
| `--border-radius-300` | `0.3125rem` (5px) | 작은 button |
| `--border-radius-400` | `0.375rem` (6px) | input |
| `--border-radius-500` | `0.5rem` (8px) | 기본 button |
| `--border-radius-600` | `0.625rem` (10px) | card small |
| `--border-radius-700` | `0.75rem` (12px) | **card 기본** |
| `--border-radius-800` | `0.875rem` (14px) | large surface |
| `--border-radius-900` | `1rem` (16px) | hero block |
| `--border-radius-round` | `624.9375rem` (≈9999px) | pill, avatar |

---

## 09. Shadows

Notion은 **3-level dual-layer shadow stack**을 쓴다 — 함정 #11의 실사용.

| Level | Value | Usage |
|---|---|---|
| `--shadow-level-100` | `0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,.015)` | resting card, icon button |
| `--shadow-level-200` | `0px 4px 18px #0000000a, 0px 2.025px 7.84688px rgba(0,0,0,.027), 0px 0.8px 2.925px #00000005, 0px 0.175px 1.04062px rgba(0,0,0,.013)` | hover card (4-layer) |
| `--shadow-level-300` | `0px 20px 50px #00000014, 0px 6px 16px #0000000a` | dropdown, modal |
| `--shadow-filter` | `0 4px 18px #0000004d` | filter drop-shadow 용 |

---

## 10. Motion

| Token (patternized) | Value | Usage |
|---|---|---|
| `--motion-global-fade-in-duration` | `.2s` 추정 | text-decoration, outline fade in |
| `--motion-global-fade-out-duration` | `.15s` 추정 | fade out |
| `transition: text-decoration-color …` | 16회+ | 링크 underline 시그니처 |
| `transition: outline-color …` | 10회+ | focus ring fade |
| 기본 transition | `.15s`, `.2s` | 컴포넌트 hover |

> 패턴: Notion은 `text-decoration-color` + `outline-color` transition을 duration 토큰으로 일괄 관리한다. 이 두 속성의 부드러운 페이드가 Notion 인터페이스의 "부드러움" 핵심.

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1252px` (narrow) / `839px` (sidebar-on prose) / `1200px` (marketing)
- **Grid type**: CSS Grid + Flexbox 혼합
- **Column count**: 12-column implicit (visual layout)
- **Gutter**: `24px` (`--spacing-24`)

### Hero

- **🆕 Pattern Summary**: `~85vh + dark navy 캠페인 배경(현재 night shift) + 중앙 정렬 H1(Lyon Text-like display) + sub + dual CTA(primary purple + secondary outline) + 하단 product mockup 이미지 overlay`
- Layout: 1-column centered (텍스트 스택) + 하단 product screenshot
- Background: 현재 campaign — dark navy/purple fade, 평상시 — `#FFFFFF`
- **🆕 Background Treatment**: `radial-gradient(circle, #0A0E2B 0%, #050714 100%)` 추정 (night shift campaign) — 평상시 solid `#FFFFFF`
- H1: `--font-size-900` (64px) / weight `600` / line-height `64px` / tracking `-0.1328125em`
- Max-width: `960px` (hero text) · `1252px` (hero canvas)

### Section Rhythm

```css
section {
  padding: 80px 24px;           /* --spacing-80 --spacing-24 */
  max-width: 1252px;
  margin: 0 auto;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` (light) / `#31302E` dark surface (캠페인)
- **Card border**: `1px solid var(--color-gray-300)` (`#DFDCD9`) — 또는 none + shadow
- **Card radius**: `12px` (`--border-radius-700`) 기본
- **Card padding**: `24px` (`--spacing-24`)
- **Card shadow**: `--shadow-level-100` (resting) → `--shadow-level-200` (hover, 4-layer)

### Navigation Structure

- **Type**: horizontal (`globalNavigation_globalNavigation__7c1YP`)
- **Position**: `position: relative; top: 0; z-index: 100`
- **Height**: `60px` (`--global-navigation-height`) — `--header-height: 60px`
- **Background**: `var(--color-background-base)` (`#FFFFFF`) 또는 campaign-nav-bg `#00000000` transparent initial
- **Border**: `1px solid transparent` initial, `#DFDCD9` on scroll
- **Dropdown**: `--dropdown-padding: 24px 95px 32px 87px` 비대칭 padding + `--dropdown-shadow: 0 4px 4px -2px #00000014`

### Content Width

- **Prose max-width**: `600px` (`--spacing-equivalent`) — 블로그 본문
- **Marketing container**: `1252px`
- **Sidebar width**: `280px` 관찰 (docs drawer)

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 600px` | 1-column, 햄버거 |
| Mobile-L | `≥ 600px` | tablet portrait 경계 |
| Tablet | `≥ 840px` | **주 breakpoint** (`840px` 205회) |
| Desktop | `≥ 1080px` | `1080px` (`164회`) 일반 desktop |
| Large | `≥ 1280px` | wide container |
| XL | `≥ 1440px` | oversize (`92회`) |

*Mobile-first* — `min-width` 많음 (600/840/1080/1280/1440). `840px`가 가장 많은 사용.

### Touch Targets

- **Minimum tap size**: `32px` 관찰 (`.numberedPagination_link` `min-width: 32px, height: 36px`)
- **Button height (mobile)**: `36px` 기본, `40px` large
- **Input height (mobile)**: `--input-height` 관찰상 `40px`

### Collapsing Strategy

- **Navigation**: 840px 이하에서 햄버거 → full-screen drawer
- **Grid columns**: 3-col → 2-col (840px) → 1-col (600px)
- **Sidebar**: 1080px 이하에서 숨김 (docs에서만 drawer로 유지)
- **Hero layout**: 그대로 — 이미 1-column 중앙 정렬

### Image Behavior

- **Strategy**: Next.js `<Image>` + CDN (`image-cdn.notion.so`) + aspect-ratio, object-fit
- **Max-width**: `100%`
- **Aspect ratio handling**: `aspect-ratio: N/M` + `object-fit: cover`

---

## 13. Components

### Buttons

```html
<button class="button_button__atjat" data-variant="primary">Get Notion free</button>
<button class="button_button__atjat" data-variant="secondary">Request a demo</button>
```

| Variant | background | color | border | radius | hover |
|---|---|---|---|---|---|
| primary (light) | `var(--color-gray-900)` `#191918` | `#FFFFFF` | none | `--border-radius-500` `8px` | `background: #31302E` |
| primary (campaign) | `var(--color-purple-500)` `#9849E8` | `#FFFFFF` | none | 동일 | `#7237AE` |
| secondary | `transparent` | `#191918` | `1px solid #DFDCD9` | 동일 | `background: #F6F5F4` |
| tertiary (link-like) | `transparent` | `#191918` | none | 0 | `text-decoration: underline` |

- gap: `var(--spacing-12)` = `12px`
- border-width-1: `1px`
- transition: `background var(--motion-global-fade-in-duration)` + `text-decoration-color` 동반

### Badges

```html
<span class="badge">Coming soon</span>
```

- `background: var(--color-gray-200)` `#F6F5F4`
- `color: var(--color-gray-800)` `#31302E`
- `border-radius: var(--border-radius-round)` pill
- `font: var(--typography-sans-200-bold-font)` (14px bold, NotionInter)
- `padding: 2px 10px`

### Cards & Containers

```html
<div class="cardCompact_cardCompact__W2i4I">…</div>
```

- bg: `#FFFFFF`
- border-radius: inherit from parent (`12px` default)
- shadow: `var(--shadow-level-200)` 4-layer on `:after` pseudo for hover
- `:after` pseudo with `background-color: #0000` + `box-shadow: var(--shadow-level-200)` + `opacity 0 → 1` on hover
- padding: `24px`

### Navigation

- `.globalNavigation_globalNavigation__7c1YP` — relative position, z-index 100
- bg: `var(--color-background-base)` `#FFFFFF` 또는 `var(--campaign-nav-bg)` transparent
- 로고: 좌측, SVG wordmark. Campaign mode에서 `--logo-stroke-color: #FFFFFF` + drop-shadow 1.5px
- 링크: NotionInter 14px weight 500
- 활성: color `var(--color-gray-900)` + underline via text-decoration-color fade
- CTA 우측 페어: "Log in" text + "Get Notion free" primary button

### Inputs & Forms

- height: `40px` 기본
- padding: `0 12px` (`var(--spacing-12)`)
- border: `1px solid var(--color-gray-300)` (`#DFDCD9`)
- radius: `var(--border-radius-500)` (`8px`)
- focus: `outline: 2px solid var(--color-accent); outline-offset: 2px; transition: outline-color .15s`
- placeholder: `color: var(--color-gray-400)` `#A39E98`

### Hero Section

- 배경: 현재 캠페인 dark navy/purple radial gradient; 평상시 `#FFFFFF`
- H1: Lyon Text (or campaign font), `--font-size-900` 64px, weight 600, tracking `-0.1328125em`
- Sub: NotionInter 18-20px weight 400, color `#A39E98` (dark 버전) / `#615D59` (light)
- Primary CTA: campaign purple (`#9849E8`) / 평상시 ink-black (`#191918`), radius `8px`
- Secondary CTA: outline, 동일 radius
- 하단: product screenshot overlay (카드 형태, radius `16px`, shadow-level-300)

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 짧은 선언, 매거진 제목 톤 | "Meet the night shift." |
| Primary CTA | 3-4 단어, 명확한 행동 | "Get Notion free" |
| Secondary CTA | 상담/데모 지향 | "Request a demo" |
| Subheading | 기능+가치 1문장 | "Notion agents keep work moving 24/7. Manage knowledge, answer questions, and push projects forward—all while you sleep." |
| Tone | 친근-편안한 productivity — 사과스럽게 warm | — |

---

## 15. Drop-in CSS

```css
/* Notion — copy into your root stylesheet */
:root {
  /* Fonts */
  --n-font-sans: "NotionInter", Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, sans-serif;
  --n-font-serif: "Lyon Text", Georgia, YuMincho, serif;
  --n-font-mono: "iA Writer Mono", Menlo, monospace;
  --n-font-weight-regular: 400;
  --n-font-weight-medium: 500;
  --n-font-weight-semibold: 600;
  --n-font-weight-bold: 700;

  /* Warm neutral ink */
  --n-bg-paper:    #F9F9F8;    /* gray-100 cream */
  --n-bg-surface:  #F6F5F4;    /* gray-200 panel */
  --n-border:      #DFDCD9;    /* gray-300 */
  --n-muted:       #A39E98;    /* gray-400 */
  --n-text-sec:    #78736F;    /* gray-500 */
  --n-text:        #31302E;    /* gray-800 body */
  --n-ink:         #191918;    /* gray-900 heading */

  /* Brand (campaign purple / default blue) */
  --n-accent:       #9849E8;    /* purple-500 canonical campaign */
  --n-accent-hover: #7237AE;    /* purple-600 */
  --n-accent-soft:  #EADBFA;    /* purple-200 */

  --n-blue-500:     #097FE8;    /* default accent outside campaign */

  /* Spacing (px = token suffix) */
  --n-space-8:   0.5rem;
  --n-space-12:  0.75rem;
  --n-space-16:  1rem;
  --n-space-24:  1.5rem;
  --n-space-32:  2rem;
  --n-space-48:  3rem;
  --n-space-64:  4rem;
  --n-space-80:  5rem;

  /* Radius */
  --n-radius-sm:   0.25rem;  /* 4px — 200 */
  --n-radius-md:   0.5rem;   /* 8px — 500 */
  --n-radius-lg:   0.75rem;  /* 12px — 700 */
  --n-radius-xl:   1rem;     /* 16px — 900 */
  --n-radius-pill: 9999px;

  /* Shadow (multi-layer) */
  --n-shadow-1: 0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,.015);
  --n-shadow-2: 0px 4px 18px #0000000a, 0px 2.025px 7.84688px rgba(0,0,0,.027), 0px 0.8px 2.925px #00000005, 0px 0.175px 1.04062px rgba(0,0,0,.013);
  --n-shadow-3: 0px 20px 50px #00000014, 0px 6px 16px #0000000a;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Notion
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#9849E8',  /* purple-500 canonical campaign */
          hover:   '#7237AE',
          soft:    '#EADBFA',
          ink:     '#191918',  /* default fallback accent */
        },
        gray: {
          100: '#F9F9F8',
          200: '#F6F5F4',
          300: '#DFDCD9',
          400: '#A39E98',
          500: '#78736F',
          600: '#615D59',
          700: '#494744',
          800: '#31302E',
          900: '#191918',
        },
        purple: {
          100:'#F8F5FC', 200:'#EADBFA', 300:'#D6B6F6', 400:'#AD6DED',
          500:'#9849E8', 600:'#7237AE', 700:'#562983', 800:'#391C57', 900:'#1C0E2C',
        },
        blue:   { 500:'#097FE8' },
        pink:   { 500:'#FF64C8' },
        orange: { 500:'#FF6D00' },
        yellow: { 500:'#FFB110' },
        green:  { 500:'#1AAE39' },
        teal:   { 500:'#27918D' },
        red:    { 500:'#F64932' },
      },
      fontFamily: {
        sans:  ['NotionInter', 'Inter', 'system-ui', 'sans-serif'],
        serif: ['Lyon Text', 'Georgia', 'serif'],
        mono:  ['iA Writer Mono', 'ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal:   '400',
        medium:   '500',
        semibold: '600',
        bold:     '700',
      },
      borderRadius: {
        sm:   '4px',
        md:   '8px',
        lg:   '12px',
        xl:   '16px',
        pill: '9999px',
      },
      boxShadow: {
        l1: '0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,.015)',
        l2: '0px 4px 18px #0000000a, 0px 2.025px 7.84688px rgba(0,0,0,.027), 0px 0.8px 2.925px #00000005, 0px 0.175px 1.04062px rgba(0,0,0,.013)',
        l3: '0px 20px 50px #00000014, 0px 6px 16px #0000000a',
      },
      transitionDuration: {
        DEFAULT: '200ms',
        fast:    '150ms',
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
| Brand primary (campaign) | `--n-accent` / `--color-purple-500` | `#9849E8` |
| Brand default (평상시) | `--color-gray-900` | `#191918` |
| Background | `--color-background-base` | `#FFFFFF` |
| Paper | `--color-gray-100` | `#F9F9F8` |
| Text primary | `--color-gray-800` | `#31302E` |
| Text muted | `--color-gray-400` | `#A39E98` |
| Border | `--color-gray-300` | `#DFDCD9` |
| Success | `--color-green-500` | `#1AAE39` |
| Error | `--color-red-500` | `#F64932` |

### Example Component Prompts

#### Hero Section (current "Night Shift" campaign variant)

```
Notion 스타일 히어로 섹션을 만들어줘. (Meet the night shift 캠페인 다크 모드)
- 배경: radial-gradient(circle, #0A0E2B 0%, #050714 100%) + 주변 isometric agent illustrations
- 상단 banner: "Developers: Get a first look at our new Developer Platform on May 13" + "Register today" link
- H1: Lyon Text, 64px (--font-size-900), weight 600, color #FFFFFF, letter-spacing -0.1328125em, 중앙 정렬
- 서브텍스트: NotionInter 18px, color rgba(255,255,255,0.7), 중앙 정렬, max-width 600px
- Primary CTA: bg #FFFFFF, color #191918, radius 8px, padding 0 24px, height 44px, font-weight 500 "Get Notion free"
- Secondary CTA: transparent + border 1px solid rgba(255,255,255,0.3), color #FFFFFF, 동일 radius/height "Request a demo"
- 하단: product screenshot (Ramp HQ database view) card, radius 16px, shadow-level-300, 3-col pipeline UI
```

#### Hero Section (default light variant)

```
Notion 스타일 히어로 섹션(평상시).
- 배경: #FFFFFF
- H1: Lyon Text, 54px (--font-size-800), weight 600, color #191918, letter-spacing -0.1171875em
- 서브텍스트: NotionInter 20px, color #31302E
- Primary CTA: bg #191918, color #FFFFFF, radius 8px
- Secondary CTA: transparent + border 1px solid #DFDCD9, color #191918
```

#### Card Component

```
Notion 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border-radius 12px, border 1px solid #DFDCD9
- padding: 24px (--spacing-24)
- shadow (resting): 0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,.015) (--shadow-level-100)
- hover 시: 4-layer shadow-level-200, transition 200ms
- 제목: NotionInter 18px weight 600, color #191918
- 본문: NotionInter 15px weight 400, color #31302E, line-height 1.5
- 링크: text-decoration-color transition 200ms fade-in/out
```

#### Badge

```
Notion 스타일 배지를 만들어줘.
- font: NotionInter, 14px, weight 700 (--typography-sans-200-bold-font)
- padding: 2px 10px, radius 9999px (pill)
- 기본: bg #F6F5F4, color #31302E
- 강조 (campaign): bg #9849E8, color #FFFFFF
```

#### Navigation

```
Notion 스타일 상단 네비게이션을 만들어줘.
- 높이: 60px (--header-height), position relative, z-index 100
- 배경: #FFFFFF 또는 transparent (campaign), 하단 border 1px solid #DFDCD9 (scroll 시)
- 로고: 좌측, SVG wordmark. 캠페인 다크 mode면 white + drop-shadow 1.5px
- 링크: NotionInter 14px weight 500, color #31302E, hover color #191918
- 링크 underline: text-decoration-color 200ms fade transition
- CTA 우측 페어: "Log in" (text link) + "Get Notion free" (primary button, #191918 bg, radius 8px)
```

### Iteration Guide

- **색상 변경 시**: 본문 텍스트는 반드시 warm `#31302E` (gray-800) — pure black 금지. 배경은 `#FFFFFF` 또는 paper `#F9F9F8`.
- **폰트 변경 시**: body `NotionInter` 400, heading `Lyon Text` 600. 둘 중 하나만 쓰면 Notion 느낌 안 남.
- **weight 계단**: `400 / 500 / 600 / 700` — 350/550 같은 중간 weight 금지.
- **letter-spacing**: 사이즈 600 이상이면 반드시 음수 tracking (weight별 3-variant). 한 값으로 통일하지 말 것.
- **여백 조정 시**: `--spacing-N` 의 N (px 값) 토큰만. `13px`, `27px` 같은 임의 값 금지.
- **새 컴포넌트 추가 시**: radius `4 / 6 / 8 / 10 / 12 / 14 / 16 / 9999` 중 하나.
- **섹션 전환**: 캠페인 모멘트에만 dark theme — 평상시 light 유지. 카드 단위로 dark 전환하지 말 것.
- **shadow**: level-100/200/300 multi-layer stack 유지. 단층 `0 2px 4px rgba(0,0,0,0.1)` 금지 (함정 #11).
- **링크 hover**: `text-decoration-color transition` 사용 — 즉각 색 바뀌게 하지 말 것.
- **반응형**: 600/840/1080/1280/1440 5단. mobile-first.

---

## 18. DO / DON'T

### ✅ DO

- 본문 텍스트 색은 `#31302E` (warm gray-800). 헤딩은 `#191918` (ink).
- 배경은 `#FFFFFF` 또는 `#F9F9F8` (paper cream). 중간 회색 금지.
- H1/H2에 `Lyon Text` (serif) + body에 `NotionInter` (sans) 듀얼 타이포.
- weight는 `400 / 500 / 600 / 700` 4단계로만.
- 사이즈 600(32px) 이상에는 weight별 negative letter-spacing 적용.
- Spacing은 `--spacing-N` 의 N 값 (4/8/12/16/20/24/28/32/40/48/56/64/72/80/96/128/160) 중에서만.
- Shadow는 `--shadow-level-100/200/300` 다층 stack 사용.
- Link underline은 `text-decoration-color transition 200ms`로 fade.
- radius는 `4 / 5 / 6 / 8 / 10 / 12 / 14 / 16 / 9999` (border-radius-200~900 + round).

### ❌ DON'T

- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#31302E` (warm ink) 사용.
- 배경을 cool `#F5F5F7` (Apple) 또는 `#EEEEEE`로 두지 말 것 — 대신 `#F9F9F8` (warm paper) 사용.
- CTA primary 배경을 brand-500 raw로 두지 말 것 — 캠페인이면 `#9849E8`, 평상시면 `#191918`. 상황 분기.
- body에 `font-weight: 300` 또는 `350` 사용 금지 — Notion은 `400`이 맞다.
- 한 가지 letter-spacing (`-0.02em` 등)으로 전체 H1-H6 통일 금지 — 사이즈와 weight별로 다른 음수 tracking이 정상 (함정 #13).
- 폰트를 body-only `Inter`로 대체하지 말 것 — heading의 `Lyon Text` 없으면 매거진 느낌 사라짐.
- radius `20px`, `30px` 같은 외부 값 금지 — 10단 시스템 (200~900) + round만.
- `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 같은 단층 shadow 금지 — `--shadow-level-200` 4-layer stack을 써라 (함정 #11).
- 링크 색을 즉시 바뀌는 `color .1s` transition으로 두지 말 것 — `text-decoration-color`에 transition 걸어 underline만 fade되게.
- color system을 `--color-brand` 같은 가상 prefix로 시작하지 말 것 — Notion은 `--color-*` + family + step (e.g. `--color-purple-500`) 직접 naming.
- light/dark를 같은 섹션 안에서 강제 전환하지 말 것 — Notion의 drastic transition은 **섹션 단위**여야 한다 (`section_transition` signature).
