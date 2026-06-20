---
schema_version: 3.2                           # 🆕 v3.2 — Designer Guidebook 전환 (ADDITIVE only)
slug: {SLUG}
service_name: {SERVICE_NAME}
site_url: {SITE_URL}
fetched_at: {FETCHED_AT}
default_theme: {light|dark|mixed}
brand_color: {BRAND_HEX}
primary_font: {PRIMARY_FONT}
font_weight_normal: {WEIGHT_NORMAL}
token_prefix: {TOKEN_PREFIX}

# apply Lv3 BOLD 리디자인 지원 필드 (v3.0~)
bold_direction: {BOLD_DIRECTION}              # 1~2 단어 (예: "Industrial Minimalism")
aesthetic_category: {AESTHETIC_CATEGORY}      # redesign-aesthetics.md §3 12가지 + "other"
signature_element: {SIGNATURE_ELEMENT}        # hero_impact / typo_contrast / section_transition / minimal_extreme
code_complexity: {CODE_COMPLEXITY}            # low / medium / high / very_high

# v3.1 — 매체 분기 (build 스킬이 starter-components 로드 시 사용)
medium: {MEDIUM}                              # web | slide | design-system | card-news | motion | print
medium_confidence: {MEDIUM_CONFIDENCE}        # high | medium | low

# 🆕 v3.2 — Archetype + Design System Level (Gemini council 권고)
archetype: {ARCHETYPE}                        # commerce-marketplace / editorial-product / editorial-magazine /
                                              # app-dashboard / saas-marketing / landing-utility /
                                              # documentation-site / portfolio-personal / automotive /
                                              # luxury-brand / other
archetype_confidence: {ARCHETYPE_CONFIDENCE}  # high | medium | low
design_system_level: {DS_LEVEL}               # lv1 (engineer spec) / lv2 (system in use) / lv3 (designer guidebook)
design_system_level_evidence: "{DS_LEVEL_EVIDENCE}"  # 한 줄 근거

# 🆕 v3.2 — 데이터 객체화 (Gemini "데이터는 YAML, 영혼은 Prose" 권고)
# 본문 hex 직접 박힘 → Cross-reference Dual Notation 가능
# 예: color: #0071e3 /* {colors.primary} */
# apply 정규식은 hex를 그대로 grep — 객체는 ADDITIVE 사용

colors:                                       # named color tokens (모두 CSS에 실재해야 함)
  # primary: "{HEX}"
  # surface-light: "{HEX}"
  # text-primary: "{HEX}"
  # ... 발견된 named token만 — 가상 alias 생성 금지

typography:                                   # 폰트 + ladder + 부재 weight
  # display: "{FONT_FAMILY}"
  # body: "{FONT_FAMILY}"
  # ladder:
  #   - { token: h1, size: "56px", weight: 700, tracking: "-0.022em" }
  # weights_used: [400, 600]
  # weights_absent: [500]                     # Negative identity 단서

components:                                   # named variant map (§13-2와 동기화)
  # button-primary: { bg: "{colors.primary}", radius: "980px", padding: "12px 22px" }
  # 발견된 변주만 — 강제 floor 없음
---

<!--
  DesignMD Analyzer — design.md 템플릿
  버전: 3.1 (2026-04-19)

  v3.1 변경: frontmatter 최상단 `schema_version: 3.1` 추가,
             `medium` + `medium_confidence` 필드 추가 (build 스킬 매체 분기용).

  섹션 번호: 00~18 (통일)
  Visual Theme = 00, Quick Start = 01, Provenance = 02, Tech Stack = 03 ...

  N/A 처리 규칙:
  - 섹션 전체 생략: 해당 ## 블록을 통째로 제거
  - 표 전체 누락:   표 대신 `> N/A — {reason}` 한 줄 작성
  - 필드 단일 누락: `{VAR}` → `N/A` 로 채움

  SOURCE 표기:
  <!-- SOURCE: auto -->  — CSS 파싱으로 추출
  <!-- SOURCE: manual --> — 사람이 직접 관찰·작성
  <!-- SOURCE: auto+manual --> — 자동 추출 후 사람이 보완

  Template ↔ Report 매핑:
  §00 Visual Theme     → report mood section
  §01 Quick Start      → report hero
  §02 Provenance       → report §01
  §03 Tech Stack       → report §02
  §04 Font Stack       → report §03 (merged)
  §05 Typography Scale → report §03
  §06 Colors           → report §04
  §07 Spacing          → report §05
  §08 Radius           → report §06
  §09 Shadows          → report §07
  §10 Motion           → report §08 (if data exists)
  §11 Layout Patterns  → report §09
  §12 Responsive       → report §09-resp
  §13 Components       → report §10
  §14 Content Voice    → report §11 (if data exists)
  §15 Drop-in CSS      → report sidebar
  §16 Tailwind         → report sidebar
  §17 Agent Prompt     → report §agent
  §18 DO / DON'T       → report §12
-->

# DESIGN.md — {SERVICE_NAME} (Claude Code Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: manual -->
<!--
  🆕 v3.2 샌드위치 구조 (Gemini council 권고):
    위 = 디자이너의 영혼 (자유 narrative + 비유 + 메타포)
    아래 = 기계의 계약 (apply Lv3 정규식 입력점 — 절대 변형 금지)
  
  apply Phase 3는 "**BOLD Direction**:" 패턴을 정규식으로 grep함.
  Narrative는 그 위에 자유롭게 추가해도 정규식 영향 없음.
-->

### Narrative

{VISUAL_THEME_NARRATIVE}

<!--
  자유 서술 — 형식 강제 없음. 3-6 문단 권장.
  
  사이트 정체성에 맞는 항목을 우선 (순서·문단수 자유):
  - 분위기 / 색 사용 / 타이포 / 공간 / 모션
  - 사진처리 / 마이크로카피 / 대비 / 리듬 / 시그니처 디테일
  
  비유와 시그니처 메타포 환영:
    "이 사이트는 박물관 갤러리처럼 벽이 사라진다"
    "잡지 편집자의 손이 닿은 듯한 카탈로그"
    "산업 데모룸의 정밀함"
  
  Cross-reference 토큰 사용 권장 (Dual Notation):
    "텍스트는 #1D1D1F (`{colors.text-primary}`)로 떨어진다"
  
  부정형 정체성 명시 환영:
    "두 번째 brand color는 존재하지 않는다"
    "shadow는 product photography에만 — chrome에는 일절 없다"
  
  ❌ 금지:
  - 5문단 강제 순서 (분위기/색/타이포/여백/모션 lock-in)
  - generic phrase ("절제된 갤러리 톤" 같이 사이트 단서 없는 비유)
  - 모든 사이트가 같은 단어로 시작하는 형식
-->

### Key Characteristics

- {KEY_CHAR_1}
- {KEY_CHAR_2}
- {KEY_CHAR_3}
- ... ({KEY_CHAR_N} — 5-10 항목, 핵심 시각 특징)

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: {BOLD_DIRECTION}
> **Aesthetic Category**: {AESTHETIC_CATEGORY}
> **Signature Element**: 이 사이트는 **{SIGNATURE_DESCRIPTION}**으로 기억된다.
> **Code Complexity**: {CODE_COMPLEXITY} — {COMPLEXITY_REASON}

<!--
  이 4줄 블록은 apply 스킬이 정규식으로 파싱한다. 형식 변경 금지.
  
  - BOLD_DIRECTION: 1~2 단어 레이블 (Step 4 판정 #13)
  - AESTHETIC_CATEGORY: redesign-aesthetics.md §3의 12가지 + "other"
  - SIGNATURE_DESCRIPTION: hero_impact / typo_contrast / section_transition / minimal_extreme + freeform 보조
  - CODE_COMPLEXITY: low / medium / high / very_high + 근거 한줄
  
  frontmatter 필드(bold_direction / aesthetic_category / signature_element / code_complexity)와 정확히 일치해야 함.
  
  하위 호환: v3.1의 "### 🆕 BOLD Direction Summary" 헤더는 deprecated. apply 정규식은
  "**BOLD Direction**:" 라인을 찾으므로 헤더명 변경에 영향 없음.
-->

---

## 01. Quick Start
<!-- SOURCE: manual -->
<!--
  {SINGLE_BIGGEST_MISTAKE} 선정 기준:
  실제 CSS와 가장 다른 것 중 "이거 하나 고치면 70% 달라 보이는 것".
  예: Stripe → "body weight 300 (400 아님)"
      Linear → "violet 악센트는 primary에만. 전체에 쓰지 마라"
      Notion  → "배경은 순백이 아니라 warm #F7F7F5"
-->

> 5분 안에 {SERVICE_NAME}처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "{PRIMARY_FONT}", "{FALLBACK_1}", -apple-system, sans-serif;
  font-weight: {WEIGHT_NORMAL};
}

/* 2. 배경 + 텍스트 */
:root { --bg: {PAGE_BG_HEX}; --fg: {TEXT_HEX}; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: {BRAND_HEX}; }
```

**절대 하지 말아야 할 것 하나**: {SINGLE_BIGGEST_MISTAKE}

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `{SITE_URL}` |
| Fetched | {FETCHED_AT} |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | {HTML_SIZE} bytes ({FRAMEWORK} SSR) |
| CSS files | {CSS_FILE_COUNT}개 외부 + {INLINE_COUNT} 인라인, 총 {CSS_TOTAL_CHARS}자 |
| Token prefix | `{TOKEN_PREFIX}` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: {FRAMEWORK} ({BUILD_DESCRIPTOR})
- **Design system**: {DS_NAME} — prefix `{TOKEN_PREFIX}`
- **CSS architecture**: {CSS_ARCHITECTURE}
  ```
  {TIER_CORE}   (--{PREFIX}-core-*)      raw hex 값
  {TIER_UTIL}   (--{PREFIX}-util-*)      semantic alias, core 참조
  {TIER_COMP}   (--{PREFIX}-{comp}-*)    컴포넌트별 조합
  ```
- **Class naming**: {CLASS_NAMING_PATTERN}
- **Default theme**: {DEFAULT_THEME} (bg = `{DEFAULT_BG_HEX}`)
- **Font loading**: {FONT_LOADING_METHOD}
- **Canonical anchor**: {CANONICAL_ANCHOR_DESC}

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `{PRIMARY_FONT}` ({FONT_LICENSE})
- **Code font**: `{CODE_FONT}` ({CODE_FONT_LICENSE})
- **Weight normal / bold**: `{WEIGHT_NORMAL}` / `{WEIGHT_BOLD}`

```css
:root {
  --{PREFIX}-font-family:       {FONT_FAMILY_CSS_VALUE};
  --{PREFIX}-font-family-code:  {CODE_FONT_CSS_VALUE};
  --{PREFIX}-font-weight-normal: {WEIGHT_NORMAL};
  --{PREFIX}-font-weight-bold:   {WEIGHT_BOLD};
}
body {
  font-family: var(--{PREFIX}-font-family);
  font-weight: var(--{PREFIX}-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- 🆕 v3.2 — SOURCE: manual / OPTIONAL -->
<!--
  라이선스 폰트가 사용자 환경에 없을 때 디자이너가 직접 적용 가능한
  open-source fallback + 보정값.
  
  generic이 아니라 사이트 특이 ("Inter at 600 + ss03 + line-height 1.47→1.44"처럼).
  사이트가 generic system font만 쓰면 이 sub-section 통째 생략 OK.
-->

{FONT_SUBSTITUTE_GUIDE}

<!--
  작성 형식 (자유):
  - **{PRIMARY_FONT}** ({라이선스 / 환경 제약})
    - Open-source 대안: **{FALLBACK_FONT}** at weight {N} + `font-feature-settings: {FEATURES}`
    - 보정: line-height {ORIGINAL} → {ADJUSTED} ({이유})
    - 보정: letter-spacing {ORIGINAL} → {ADJUSTED} ({이유})
-->

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
{TYPOGRAPHY_ROWS}

> ⚠️ {TYPOGRAPHY_KEY_INSIGHT}

### Principles
<!-- 🆕 v3.2 — SOURCE: manual / OPTIONAL -->
<!--
  표가 말하지 못하는 것을 말한다 (의도 / 부재 / 비대칭).
  4-6개 numbered statements 권장. craft 사이트는 더 많을 수도.
  사이트가 generic이면 0개 (sub-section 생략).
  
  ref 예시 (Apple):
    1. Body size is 17px, not 16px — Apple's signature density.
    2. Negative letter-spacing on display only. Body keeps 0.
    3. Weight 400 for body, weight 600 for display. Weight 500 deliberately absent.
    4. Two optical sizes (Display + Text) — not one font with axes.
    5. line-height 1.47 on body — looser than typical to balance dense letter-spacing.
-->

{TYPOGRAPHY_PRINCIPLES}

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp ({BRAND_RAMP_COUNT} steps)
<!-- {TOKEN_PREFIX}-color-core-{BRAND_FAMILY}-* -->

| Token | Hex |
|---|---|
{BRAND_RAMP_ROWS}

### 06-2. Brand Dark Variant
<!-- OPTIONAL: omit if service uses single-theme ramp -->
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
{BRAND_DARK_ROWS}

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light (`{NEUTRAL_NAME}`) | Dark (`{NEUTRAL_DARK_NAME}`) |
|---|---|---|
{NEUTRAL_PAIR_ROWS}

### 06-4. Accent Families
<!-- OPTIONAL: omit if no accent palette exists -->
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
{ACCENT_ROWS}

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
{SEMANTIC_ROWS}

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->
<!--
  이 tier가 컴포넌트 레벨 API.
  core 토큰보다 alias를 우선 사용.
  {TOKEN_PREFIX}-color-util-* → {TOKEN_PREFIX}-color-core-* → hex
-->

| Alias | Resolves to | Usage |
|---|---|---|
{ALIAS_ROWS}

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->
<!--
  §06-1~06-6 = design time (설계된 토큰 시스템)
  §06-7      = runtime measurement (실제 페이지에 얼마나 쓰이는지)
  중복 있음은 정상 — 역할이 다름.
  자동 추출 전용: CSS 전체 hex 빈도 카운트로 생성, 수동 작성 불가.
-->

| Token | Hex | Frequency |
|---|---|---|
{DOMINANT_ROWS}

### 06-8. Color Stories
<!-- 🆕 v3.2 — SOURCE: manual / OPTIONAL — 상위 4 색만 -->
<!--
  Gemini council 권고: "verbosity tax 회피"
  
  brand / surface / text / hairline 상위 4 색에만 1-3 문장 prose.
  각 색에 "왜 / 언제 / 무엇 대신 / 어디에만" 답변.
  
  ❌ 강제 금지:
  - 모든 색에 prose (5번째 색부터 generic이 됨)
  - monochrome 사이트에 prose 강제 (sub-section 통째 생략 OK)
  
  ref 예시 (Airbnb):
    **`{colors.primary}` (#FF385C)** — Rausch, the single brand color.
    Used for primary CTA backgrounds (Reserve, Continue), the search orb,
    the heart save state on property cards, and inline brand links. The
    most recognizable color in consumer travel. There is no second brand
    color — neutrals carry secondary actions.
    
    **`{colors.surface-base}` (#FFFFFF)** — Pure white floor. Airbnb's
    listings demand neutrality so photography can carry the visual weight.
    Hairlines and shadows do the structural work that color would in
    other marketplaces.
-->

{COLOR_STORIES}

---

## 07. Spacing
<!-- SOURCE: auto -->
<!--
  네이밍 규칙: {SPACING_NAMING_RULE}
  예) stripe: core-200 = 16px = 200 ÷ 12.5
-->

| Token | Value | Use case |
|---|---|---|
{SPACING_ROWS}

**주요 alias**:
- `{SPACE_ALIAS_1}` → {SPACE_ALIAS_1_VALUE} ({SPACE_ALIAS_1_USE})

### Whitespace Philosophy
<!-- 🆕 v3.2 — SOURCE: manual / OPTIONAL -->
<!--
  Spacing 표가 말하지 못하는 것: 사이트의 공간 운용 의도.
  1-2 paragraph 자유 서술. 사이트가 generic이면 생략 OK.
  
  "이 사이트는 빽빽한가 여유로운가" "리듬은 어떤가"가 아니라,
  사이트의 의도가 드러나는 구체 단서를 짚어야 한다.
  
  ref 예시 (Apple):
    Every tile begins with at least 64px of air above the headline.
    This isn't decoration — it's a rhythm. The eye gets to the headline
    only after a full breath. By the time it reaches the product image,
    the breath has settled into focus.
    
    Apple's spacing system is not 4-8-16-32 ladder. It's 64-80-128 —
    three scales for vertical air, with content at 1068px max-width.
    The air owns the page.
  
  ref 예시 (Airbnb):
    The system gives editorial bands 64px of vertical breathing room
    but compresses card grids — property and city-link cards sit just
    16px apart. The contrast is intentional: "open hero, dense
    marketplace below."
-->

{WHITESPACE_PHILOSOPHY}

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
{RADIUS_ROWS}

---

## 09. Shadows
<!-- SOURCE: auto -->
<!--
  패턴: {SHADOW_PATTERN}
  예) stripe: 모든 elevation이 dual-shadow 원자 (top + bottom 레이어)
-->

| Level | Value | Usage |
|---|---|---|
{SHADOW_ROWS}

---

## 10. Motion
<!-- OPTIONAL: omit if no motion tokens found in CSS -->
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
{MOTION_ROWS}

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: {CONTENT_MAX_WIDTH}
- **Grid type**: {GRID_TYPE}
- **Column count**: {GRID_COLUMNS}
- **Gutter**: {GRID_GUTTER}

### Hero
- **🆕 Pattern Summary**: {HERO_PATTERN_SUMMARY}
  <!-- 한줄 요약: "{height}vh + {bg 처리} + {H1 정렬} + {CTA 배치}"
       예: "100vh + 풀스크린 차량 사진 + 중앙 H1 + dual CTA 아래"
       예: "70vh + gradient flame bg + 좌측 H1 + 우측 제품 mockup" -->
- Layout: {HERO_LAYOUT}
- Background: {HERO_BG}
- **🆕 Background Treatment**: {HERO_BG_TREATMENT}
  <!-- atmospheric 효과 명시: solid / gradient mesh / noise texture / image overlay / video / dot pattern / grain
       예: "image-overlay (vehicle.jpg + linear-gradient(180deg, rgba(0,0,0,0.3), rgba(0,0,0,0.6)))"
       예: "gradient-mesh (radial 2-layer)"
       예: "solid #F5F5F7" — 단색이면 단색이라고 명시 -->
- H1: `{H1_SIZE}` / weight `{H1_WEIGHT}` / tracking `{H1_TRACKING}`
- Max-width: {HERO_MAX_WIDTH}

### Section Rhythm
```css
section {
  padding: {SECTION_PADDING_V} {SECTION_PADDING_H};
  max-width: {SECTION_MAX_WIDTH};
}
```

### Card Patterns
- **Card background**: {CARD_BG}
- **Card border**: {CARD_BORDER}
- **Card radius**: {CARD_RADIUS}
- **Card padding**: {CARD_PADDING}
- **Card shadow**: {CARD_SHADOW}

### Navigation Structure
- **Type**: {NAV_TYPE}
- **Position**: {NAV_POSITION}
- **Height**: {NAV_HEIGHT}
- **Background**: {NAV_BG}
- **Border**: {NAV_BORDER}

### Content Width
- **Prose max-width**: {PROSE_MAX_WIDTH}
- **Container max-width**: {CONTAINER_MAX_WIDTH}
- **Sidebar width**: {SIDEBAR_WIDTH}

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->
<!--
  자동 추출된 미디어 쿼리 + 수동 관찰 보완.
  모바일 퍼스트/데스크톱 퍼스트 여부도 명시.
-->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | {BP_MOBILE} | {BP_MOBILE_DESC} |
| Tablet | {BP_TABLET} | {BP_TABLET_DESC} |
| Desktop | {BP_DESKTOP} | {BP_DESKTOP_DESC} |
| Large | {BP_LARGE} | {BP_LARGE_DESC} |

### Touch Targets
- **Minimum tap size**: {TOUCH_MIN_SIZE}
- **Button height (mobile)**: {TOUCH_BUTTON_HEIGHT}
- **Input height (mobile)**: {TOUCH_INPUT_HEIGHT}

### Collapsing Strategy
- **Navigation**: {COLLAPSE_NAV}
- **Grid columns**: {COLLAPSE_GRID}
- **Sidebar**: {COLLAPSE_SIDEBAR}
- **Hero layout**: {COLLAPSE_HERO}

### Image Behavior
- **Strategy**: {IMAGE_STRATEGY}
- **Max-width**: {IMAGE_MAX_WIDTH}
- **Aspect ratio handling**: {IMAGE_ASPECT_RATIO}

---

## 13. Components
<!-- SOURCE: auto+manual -->
<!--
  {COMPONENTS_BLOCK} = 아래 패턴을 서비스별로 반복한 마크다운 블록을 주입.
  자동 생성 또는 수동 작성 후 단일 블록으로 삽입.
  각 컴포넌트: BEM 클래스 + HTML 마크업 + spec 표 + 상태별(hover/active) 값
-->

### Buttons
{BUTTONS_BLOCK}

### Badges
{BADGES_BLOCK}

### Cards & Containers
<!--
  카드/컨테이너 패턴: bg, border, radius, padding, shadow
  hover 상태: shadow 변화, border-color 변화, transform 등
-->
{CARDS_BLOCK}

### Navigation
<!--
  네비게이션 컴포넌트: 링크 스타일, active 상태, 모바일 메뉴
-->
{NAVIGATION_BLOCK}

### Inputs & Forms
<!--
  입력 필드: height, padding, border, focus 스타일, error 스타일
-->
{INPUTS_BLOCK}

### Hero Section
<!--
  히어로 영역: 배경, 텍스트 크기/weight, CTA 배치, 이미지/일러스트
-->
{HERO_SECTION_BLOCK}

### 13-2. Named Variants
<!-- 🆕 v3.2 — SOURCE: manual / OPTIONAL — 사이트별 0~N개 -->
<!--
  기본 6 카테고리(Buttons/Badges/Cards/Navigation/Inputs/Hero) 안에 변주가 많을 때
  named token으로 분리한다. ref(apple/airbnb/bmw)는 button만 5-8개 named variant.
  
  ❌ 강제 floor 없음. 사이트가 단순하면 0개 OK (sub-section 통째 생략).
  ❌ "12 컴포넌트 floor" 강제 금지 (Gemini "Grep-Death" 경고 — 빈 표를 generic으로 채우는 환각).
  
  ✅ 발견된 변주만 — 가상 variant 생성 금지.
  ✅ frontmatter `components:` map과 동기화.
  
  ref 예시 (Apple, 8개):
    button-primary           # blue pill CTA
    button-primary-active    # 같은 hex의 active 상태
    button-primary-focus     # focus ring (accessibility)
    button-secondary-pill    # white outline pill
    button-dark-utility      # dark surface 위 small button
    button-pearl-capsule     # store hero capsule
    button-store-hero        # 큰 buy button
    button-icon-circular     # circular icon button
  
  각 variant: spec 표 + HTML markup + state notes.
  상태 6종 권장(있는 것만): hover / focus / active / disabled / loading / error.
-->

{NAMED_VARIANTS_BLOCK}

### 13-3. Signature Micro-Specs
<!-- 🆕 v3.2 — SOURCE: manual / OPTIONAL — 사이트의 craft -->
<!--
  Apple 격차 해소의 핵심 (Gemini council 권고):
  "Apple은 색상이 아니라 공법으로 만들어진다.
   미세 그라데이션, backdrop-filter, 0.5px border가 핵심.
   우리는 '면'은 보지만 '결'은 못 본다."
  
  사이트가 가진 기술적 특이점을 공법(craft) 결합 명칭으로 추출:
  - backdrop-filter / blur / 그라디언트 stops / 노이즈 / blend mode
  - 0.5px / 1.5px 같은 비표준 두께
  - letter-spacing 보정 패턴
  - single drop-shadow의 위치/스코프 같은 메타 규칙
  - hover/transition의 사이트 시그니처 동작
  
  ❌ 강제 floor 없음 (사이트가 generic CSS만 쓰면 0개).
  ❌ "모든 사이트에 micro-spec 5개" 강제 금지.
  ✅ craft 사이트 (Apple/Stripe/Linear)는 3-5개.
  
  ref 예시 (Apple):
    glassmorphism-hero-tile:
      description: "프리미엄 제품 카드의 시그니처 효과"
      technique: "backdrop-filter: blur(20px) saturate(180%); rgba background 0.7 alpha"
      applied_to: ["{component.product-tile}", "{component.utility-card}"]
      visual_signature: "투명 유리 위에 떠 있는 듯한 깊이감"
    
    photography-drop-shadow:
      description: "제품 사진에만 적용되는 단일 그림자"
      technique: "rgba(0, 0, 0, 0.22) 3px 5px 30px"
      applied_to: ["product-imagery only — never chrome"]
      visual_signature: "제품이 표면 위에 놓인 듯한 무게감"
    
    apple-tight-tracking:
      description: "디스플레이 사이즈 letter-spacing 보정"
      technique: "letter-spacing: -0.022em on h1-h3"
      applied_to: ["display sizes only — body keeps 0"]
      visual_signature: "응집된 헤드라인 표정"
-->

{SIGNATURE_MICRO_SPECS}

---

## 14. Content / Copy Voice
<!-- OPTIONAL: omit if insufficient data -->
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | {HEADLINE_RULE} | "{HEADLINE_EXAMPLE}" |
| Primary CTA | {CTA_RULE} | "{CTA_EXAMPLE}" |
| Secondary CTA | {SECONDARY_CTA_RULE} | "{SECONDARY_CTA_EXAMPLE}" |
| Subheading | {SUBHEADING_RULE} | |
| Tone | {TONE_DESC} | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->
<!--
  핵심 토큰 5개만 (brand: 25/300/500/600anchor/900).
  전체 ramp는 §06 참조.
-->

```css
/* {SERVICE_NAME} — copy into your root stylesheet */
:root {
  /* Fonts */
  --{PREFIX}-font-family:       {FONT_FAMILY_CSS_VALUE};
  --{PREFIX}-font-family-code:  {CODE_FONT_CSS_VALUE};
  --{PREFIX}-font-weight-normal: {WEIGHT_NORMAL};
  --{PREFIX}-font-weight-bold:   {WEIGHT_BOLD};

  /* Brand (anchor + 4 steps) */
  --{PREFIX}-color-brand-25:  {BRAND_25};
  --{PREFIX}-color-brand-300: {BRAND_300};
  --{PREFIX}-color-brand-500: {BRAND_500};
  --{PREFIX}-color-brand-600: {BRAND_600};   /* ← canonical */
  --{PREFIX}-color-brand-900: {BRAND_900};

  /* Surfaces */
  --{PREFIX}-bg-page:   {PAGE_BG_HEX};
  --{PREFIX}-bg-dark:   {DARK_BG_HEX};
  --{PREFIX}-text:      {TEXT_HEX};
  --{PREFIX}-text-muted:{TEXT_MUTED_HEX};

  /* Key spacing */
  --{PREFIX}-space-sm:  {SPACE_SM};
  --{PREFIX}-space-md:  {SPACE_MD};
  --{PREFIX}-space-lg:  {SPACE_LG};

  /* Radius */
  --{PREFIX}-radius-sm: {RADIUS_SM};
  --{PREFIX}-radius-md: {RADIUS_MD};
}
```

---

## 16. Tailwind Config
<!-- OPTIONAL: omit if service doesn't use Tailwind or config not derivable -->
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — {SERVICE_NAME}
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '{BRAND_25}',
          300: '{BRAND_300}',
          500: '{BRAND_500}',
          600: '{BRAND_600}',
          900: '{BRAND_900}',
        },
        neutral: {
{TAILWIND_NEUTRAL_TOKENS}
        },
      },
      fontFamily: {
        sans: ['{PRIMARY_FONT}', '{FALLBACK_1}', 'system-ui'],
        mono: ['{CODE_FONT}', 'ui-monospace'],
      },
      fontWeight: {
        normal: '{WEIGHT_NORMAL}',
        bold:   '{WEIGHT_BOLD}',
      },
      borderRadius: {
{TAILWIND_RADIUS_TOKENS}
      },
      boxShadow: {
{TAILWIND_SHADOW_TOKENS}
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->
<!--
  AI 에이전트(Claude, GPT 등)가 이 디자인 시스템으로 구현할 때 참조하는 섹션.
  design.md의 토큰을 실전 프롬프트에서 어떻게 활용하는지 빠른 레퍼런스 제공.
-->

### Quick Color Reference
<!--
  역할별로 hex 값을 한눈에 볼 수 있는 요약 테이블.
  §06의 전체 토큰 중 실전에서 가장 자주 쓰이는 것만 추출.
-->

| Role | Token | Hex |
|---|---|---|
| Brand primary | {AGENT_BRAND_TOKEN} | {AGENT_BRAND_HEX} |
| Background | {AGENT_BG_TOKEN} | {AGENT_BG_HEX} |
| Text primary | {AGENT_TEXT_TOKEN} | {AGENT_TEXT_HEX} |
| Text muted | {AGENT_MUTED_TOKEN} | {AGENT_MUTED_HEX} |
| Border | {AGENT_BORDER_TOKEN} | {AGENT_BORDER_HEX} |
| Success | {AGENT_SUCCESS_TOKEN} | {AGENT_SUCCESS_HEX} |
| Error | {AGENT_ERROR_TOKEN} | {AGENT_ERROR_HEX} |

### Example Component Prompts
<!--
  "이 프롬프트를 복사해서 AI에게 주면 이 서비스 스타일의 컴포넌트가 나온다."
-->

#### Hero Section
```
{SERVICE_NAME} 스타일 히어로 섹션을 만들어줘.
- 배경: {PAGE_BG_HEX}
- H1: {PRIMARY_FONT}, {H1_SIZE}, weight {H1_WEIGHT}, tracking {H1_TRACKING}
- 서브텍스트: {TEXT_MUTED_HEX}, 16px
- CTA 버튼: 배경 {BRAND_HEX}, 텍스트 white, radius {RADIUS_MD}, padding 12px 24px
- 최대 너비: {HERO_MAX_WIDTH}
```

#### Card Component
```
{SERVICE_NAME} 스타일 카드 컴포넌트를 만들어줘.
- 배경: {CARD_BG}, border: 1px solid {AGENT_BORDER_HEX}, radius: {CARD_RADIUS}
- padding: {CARD_PADDING}
- shadow: {CARD_SHADOW}
- hover 시: {CARD_HOVER_EFFECT}
- 제목: {PRIMARY_FONT}, 16px, weight {WEIGHT_BOLD}
- 본문: 14px, color {AGENT_TEXT_HEX}, line-height 1.6
```

#### Badge
```
{SERVICE_NAME} 스타일 배지를 만들어줘.
- font: {PRIMARY_FONT}, 12px, weight 500
- padding: 2px 8px, radius: 999px
- 기본: bg {AGENT_BG_HEX}, border 1px solid {AGENT_BORDER_HEX}
- 브랜드: bg {BRAND_HEX}20, color {BRAND_HEX}, border 없음
```

#### Navigation
```
{SERVICE_NAME} 스타일 상단 네비게이션을 만들어줘.
- 높이: {NAV_HEIGHT}, 배경: {NAV_BG}, 하단 border: 1px solid {AGENT_BORDER_HEX}
- 로고: 좌측, 14px, weight 600
- 링크: {PRIMARY_FONT}, 14px, weight 400, color {AGENT_MUTED_HEX}
- 활성 링크: color {AGENT_TEXT_HEX}, weight 500
- CTA 버튼: 우측, 브랜드 컬러
```

### Iteration Guide
<!--
  반복 작업·수정 요청 시 주의사항.
  "이거만 주의하면 일관성이 유지된다"는 실전 팁.
-->

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight {WEIGHT_NORMAL}이 기본. {WEIGHT_BOLD}는 제목/강조에만.
- **여백 조정 시**: §07의 spacing scale 단위로만. 임의 값(13px, 27px 등) 금지.
- **새 컴포넌트 추가 시**: §13의 기존 패턴(radius, shadow, border 스타일)을 따를 것.
- **다크 모드**: §06-2의 dark variant 토큰을 사용. light 토큰에 opacity 적용하지 말 것.
- **반응형**: §12의 breakpoint를 그대로 사용. 커스텀 breakpoint 추가 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->
<!--
  실제 CSS에서 검증된 규칙만 작성.
  이 서비스 디자인을 구현할 때 흔히 틀리는 것들.
-->

### ✅ DO
{DO_ITEMS}

### ❌ DON'T
<!--
  apply 자동 검증 호환 (apply Step 3 grep 6쿼터 보존):
  색상 DON'T는 반드시 hex inline-code (`#FFFFFF`) 또는 표 형식 — prose로 풀면 grep 불가.
  
  쓰기 패턴: "X를 [금지 hex/값]으로 두지 말 것 — 대신 [올바른 hex/값] 사용"
  예: "배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#F5F5F7` 사용"
  예: "body에 `font-weight: 400` 사용 금지 — Apple은 default 400이지만 헤드라인은 600 강제"
-->

{DONT_ITEMS}

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- 🆕 v3.2 — SOURCE: manual / OPTIONAL -->
<!--
  Gemini council 권고: "디자인 시스템의 정체성은 '허용'보다 '금지'에서 더 명확해진다.
  'Apple은 폰트 웨이트 500을 쓰지 않는다'는 정보는 디자이너가 불필요한 시도를 하지 않게 만든다."
  
  단순 금지가 아니라 "사이트가 의도적으로 결정한 부재"를 명시.
  5-10 항목, 자유 서술. craft 사이트는 더 많을 수도.
  
  "absent / none / zero / never" 같은 단호한 표현 권장.
  
  ref 예시 (Apple):
    - Brand Gradient: zero gradient-based design tokens
    - Weight 500: deliberately absent — only 400 (body) and 600 (display) used
    - Hover documentation: never. Default and Active/Pressed states only.
    - Second brand color: none — `{colors.primary}` carries every interactive element
    - Chrome shadow: none — exactly one drop-shadow, applied to product imagery
    - Border on cards: rarely — surface contrast does the structural work
    - Animated transitions: minimal — color fade < 0.1s, no transform/shadow animations
  
  ref 예시 (Airbnb):
    - Second brand color: none — Rausch alone carries every CTA
    - Decorative borders: none on listing cards — just shadow + radius
    - Bold display weights: 700+ rare — most display sits at 600
-->

{NEGATIVE_SPACE_IDENTITY}

---

## 19. Known Gaps & Assumptions
<!-- 🆕 v3.2 — SOURCE: manual / REQUIRED -->
<!--
  Codex council 권고: "evidence-or-gap 계약"
  데이터가 없으면 추정하지 말고 "이건 모른다"를 명시한다.
  환각 방어의 마지막 안전판.
  
  최소 3 항목 (Step 7 validator는 ≥3 강제). 보통 5-10 항목.
  자유 서술 (불릿 권장).
  
  카테고리 예시:
  - 측정 한계 (single page / desktop only / sub-flow 미방문)
  - 추출 정확도 (logo wall 자동 분리 80% 등)
  - 미관측 토큰 (form validation states / loading states / error states)
  - 다크모드 매핑 부재
  - 모션/애니메이션 미수집 (CSS는 봤지만 IntersectionObserver/scroll-trigger 로직 미분석)
  - Sub-flow 미방문 (configurator / checkout / settings 페이지)
  
  ref 예시 (Apple):
    - **Form validation states not surfaced** — homepage 단일 page 분석.
      로그인/결제 흐름 미방문.
    - **Dark-mode counterpart palette** — 일부 토큰만 dark에서 확인됨.
      전체 mapping 미수집.
    - **Exact blur radius** — backdrop-filter는 platform-dependent.
      CSS에 `blur(20px)` 명시지만 실측 다를 수 있음.
    - **Animation curves** — CSS의 cubic-bezier 값은 추출됐지만,
      IntersectionObserver/scroll-trigger 로직 미분석.
    - **Sub-flow surfaces** — Configurator(`/buy/iphone-17-pro`),
      accessories grid는 hero/store와 다른 chassis. 본 분석 미포함.
    - **Logo wall colors** — 일부 chromatic hex가 customer logo SVG에서 옴.
      brand_color 후보에서 의도적으로 제외했지만 자동 분리 정확도 80%.
  
  ❌ 절대 추정 금지:
  - 추정 hex 작성 — CSS에 없으면 "측정 불가" 표기
  - 가상 토큰명 — 실제 CSS 변수에 없는 alias 생성 금지
  - 모바일 실측 미수집 — desktop CSS만 분석한 경우 명시
-->

{KNOWN_GAPS}
