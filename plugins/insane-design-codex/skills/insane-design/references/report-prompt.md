# Report Generation Spec v3.0

> `design.md` -> `report.ko.html` 변환 규칙.
> v3.0: 5 Layer 위계 구조, canonical CSS 분리, template.md v3 (SS00~SS18) 대응.

---

## Layer 0: 불변 계약 (IMMUTABLE CONTRACT)

이 레이어의 규칙은 **예외 없이** 적용. 위반 시 전체 리포트를 폐기하고 재생성.

### 0-1. CSS 수정 금지

`report.css` 파일을 `<style>` 태그 안에 **그대로** 삽입. sentinel 주석으로 감싼다:

```html
<style>
<!-- BEGIN:CANONICAL_STYLE -->
{report.css 내용 전체 — 1바이트도 변경 금지}
<!-- END:CANONICAL_STYLE -->
</style>
```

**절대 금지:**
- 클래스 추가/제거/이름 변경
- 속성값 수정 (px, color, font 등)
- 선택자 변경
- 새 CSS 규칙 삽입
- `@media` 쿼리 수정

### 0-2. 변경 허용 변수 — 딱 2개

```css
:root {
  --brand-color: {frontmatter의 brand_color};
  --font-display: "{서비스 display font}", -apple-system, sans-serif;
}
```

이 2개 값만 서비스별로 교체. 나머지 `:root` 변수는 모든 리포트에서 동일.

### 0-3. JS 수정 금지

`</body>` 직전의 `<script>` 블록은 canonical JS. 기능:
- Code Export 탭 전환
- `.copy[data-copy]` 클립보드 복사
- `[data-copy-active]` 활성 탭 코드 복사

그대로 복사. 수정 금지.

### 0-4. 값 조작 금지

design.md에 없는 값을 **절대 생성하지 않는다:**
- hex 값 지어내기 금지
- 토큰명 지어내기 금지
- 폰트명 지어내기 금지
- 스펙 수치 지어내기 금지

design.md에 적힌 것만 사용.

---

## Layer 1: 입출력 계약 (I/O CONTRACT)

### 1-1. 입출력

| | |
|---|---|
| **입력** | `insane-design/<slug>/design.md` (YAML frontmatter + SS00~SS18) |
| **출력** | `insane-design/<slug>/report.ko.html` (자체 완결 한글 HTML) |
| **CSS** | `references/report.css` — Layer 0 규칙으로 삽입 |

소스 파일명: `design.md` 우선. 없으면 `DESIGN.claude.manual.md`.

### 1-2. Input Contract — frontmatter 필드

| 필드 | 필수 | fallback (없을 때) |
|---|---|---|
| `slug` | YES | 폴더명 사용 |
| `service_name` | YES | slug를 capitalize |
| `brand_color` | YES | `#18181b` (zinc-900) |
| `primary_font` | YES | `system-ui` |
| `site_url` | YES | `https://{slug}.com` |
| `fetched_at` | OPT | 파일 수정일 |
| `font_weight_normal` | OPT | `400` |
| `token_prefix` | OPT | 생략 (Hero에서도 표시 안 함) |
| `default_theme` | OPT | `light` |

### 1-3. 섹션 매핑 테이블

| design.md | HTML section ID | TOC 그룹 | TOC 이름 | 필수 |
|---|---|---|---|---|
| SS00 Visual Theme | `mood` | Overview | 분위기와 철학 | YES |
| SS01 Quick Start | hero 안 카드 | Overview | 한눈에 보기 | YES |
| SS02 Provenance | `provenance` | Overview | 출처와 수집 기준 | YES |
| SS03 Tech Stack | `stack` | Overview | 테크 스택 | YES |
| SS04+SS05 Typography | `typography` | Foundations | 타이포그래피 | YES |
| SS06 Colors | `colors` | Foundations | 컬러 | YES |
| SS07 Spacing | `spacing` | Tokens | 스페이싱 | YES |
| SS08 Radius | `radius` | Tokens | 라디우스 | YES |
| SS09 Shadows | `shadows` | Tokens | 섀도우 | OPT |
| SS10 Motion | `motion` | Tokens | 모션 | OPT |
| SS11 Layout Patterns | `layout` | Structure | 레이아웃 패턴 | YES |
| SS12 Responsive | `responsive` | Structure | 반응형 | YES |
| SS13 Components | `components` | Patterns | 컴포넌트 | YES |
| SS14 Content Voice | `voice` | Patterns | 라이팅 원칙 | OPT |
| SS15+SS16 Code Export | `export` | Code | CSS / Tailwind | YES |
| SS17 Agent Prompt | `agent` | Code | 에이전트 가이드 | YES |
| SS18 Do/Don't | `verdict` | Rules | Do / Don't | YES |

### 1-4. TOC — 7그룹

```
── Overview ──
  00  분위기와 철학
  01  한눈에 보기
  02  출처와 수집 기준
  03  테크 스택

── Foundations ──
  04  타이포그래피
  05  컬러

── Tokens ──
  06  스페이싱
  07  라디우스
  08  섀도우          ← optional
  09  모션            ← optional

── Structure ──
  10  레이아웃 패턴
  11  반응형

── Patterns ──
  12  컴포넌트
  13  라이팅 원칙     ← optional

── Code ──
  14  CSS / Tailwind
  15  에이전트 가이드

── Rules ──
  16  Do / Don't
```

- 그룹 라벨: `.toc__group-label` (영어, uppercase, monospace)
- 항목 번호: `.toc__num` (monospace, 10px)
- optional 섹션 제거 시: HTML 섹션 AND TOC 항목 **둘 다** 제거
- TOC 번호 재계산: optional 제거 후 빈 번호 없이 연속 번호 (00, 01, 02, 03...)

### 1-5. 반응형

`report.css`의 `@media (max-width:1024px)` 블록이 처리한다. CSS에 이미 포함되어 있으므로 별도 작업 불필요.

---

## Layer 2: 콘텐츠 섹션 렌더러 (SECTION RENDERERS)

각 섹션의 HTML 구조. design.md 섹션 -> HTML 변환 규칙.

### 2-00. SS00 Visual Theme -> `.mood` 카드

```
section#mood
  .mood__accent-bar         <- brand-color 4px bar
  .mood__title              <- "분위기와 철학" 류 서술형 타이틀
  .mood__body               <- 서술형 텍스트 (3~5 문단, <p> 태그)
  .mood__keywords           <- 키 특성 리스트 (.mood__keyword pill들)
```

- SS00의 서술형 텍스트를 `.mood__body` 안에 `<p>` 태그로 분리
- 핵심 키워드가 있으면 `.mood__keywords` 로 pill 렌더

### 2-01. SS01 Quick Start -> Hero 안 카드

Hero 구성 순서 (위->아래):

1. **Eyebrow pill** `.hero__eye`: `Design System Report` + `.dot` (brand-color)
2. **h1** `.hero__title`: `{service_name}` + `.sub` `— {system_name 또는 token_prefix}`
3. **sub** `.hero__sub`: design.md SS01 아래 설명 문장 또는 한 줄 요약
4. **Screenshot** (조건부): `screenshots/hero-cropped.png` 존재 시만 삽입
   ```html
   <div class="hero__screenshot">
     <img src="screenshots/hero-cropped.png" alt="{service_name} — 실제 홈페이지 스크린샷">
   </div>
   ```
   파일 없으면 이 div 전체 생략.
5. **Quick Start 카드** `.qs`: 3칸 dark code cards + 경고 callout
6. **4-stat 카드** `.hero__stats`: Source / Fetched / System / 핵심 수치

#### Quick Start 3칸 분리

- SS01의 CSS 코드 블록에서 `/* 1. */` `/* 2. */` `/* 3. */` 주석으로 3개 스텝 분리
- 각 스텝 -> `.qs__step` dark card (`.qs__grid` 3열)
- `/* 1. */` 주석 구분 안 되면 -> 전체를 1개 스텝에 넣어도 됨
- "절대 하지 말 것" -> `.qs__warn` 빨간 callout

#### 4-stat 카드

| 칸 | 값 |
|---|---|
| Source | `site_url`에서 도메인만 |
| Fetched | `fetched_at` |
| System | `token_prefix` 또는 디자인 시스템 이름 (없으면 "Custom") |
| 4번째 | 해당 서비스의 가장 특징적인 수치 (SS01 핵심 포인트에서 선택) |

### 2-02. SS02 Provenance -> `.prov` 메타데이터 테이블

```
section#provenance
  .prov
    .prov__row x N
      .prov__k  <- 키 (monospace)
      .prov__v  <- 값
```

SS02의 테이블 행을 `.prov__row` 로 1:1 매핑.

### 2-03. SS03 Tech Stack -> `.ts` 카드

```
section#stack
  .ts (2열 grid)
    .ts__item x N
      .ts__head  <- 카테고리명 (monospace, uppercase)
      .ts__body  <- 내용 (code, bold 허용)
```

SS03의 각 항목(Framework, Design system, CSS architecture, Class naming, Default theme, Font loading 등)을 개별 `.ts__item` 카드로.

### 2-04. SS04+SS05 Typography -> Font Stack + 라이브 프리뷰

#### Font Stack 카드 (SS04)

```
.fs-card
  .fs-card__row x N
    .fs-card__k  <- 키 (Display, Code, Weight, Fallback)
    .fs-card__v  <- 값
```

#### 타이포 라이브 프리뷰 (SS05)

```
.type-table
  .type-row x N
    .type-row__s   <- 실제 inline style 적용 (font-size, font-weight, line-height, letter-spacing)
    .type-row__spec
      .tk          <- 토큰명
      b + text     <- 스펙 텍스트
```

**MUST**: `.type-row__s`에 실제 CSS inline style을 적용한다. 텍스트만 표시하는 것이 아니라 해당 크기/굵기로 실제 렌더.

font-family는 `"SF Pro Display", -apple-system, BlinkMacSystemFont, sans-serif` 고정.

### 2-05. SS06 Colors -> 스와치 그리드 + Dominant chart

서브섹션 06-1 ~ 06-7을 순서대로 렌더. 없는 서브섹션은 건너뜀.

#### 컬러 램프 스와치 (06-1 ~ 06-5)

```
.ramp-group
  .ramp-label    <- 램프명 + step 수
  .ramp.ramp--{N}  <- N = step 수로 grid columns 동적 조정
    .sw.sw--{l|d}  x N
      .n           <- step 이름
      hex 텍스트
```

- 각 step -> 실제 배경색 (`style="background:{hex}"`)
- `.sw--l` (밝은 배경 -> 어두운 텍스트) vs `.sw--d` (어두운 배경 -> 밝은 텍스트) — Layer 3 Color Brightness 규칙으로 결정
- anchor step(★) -> `.is-anchor` 추가

#### Alias Layer (06-6)

```
.alias-table
  .row x N
    .k     <- alias 이름
    .arrow <- ->
    .v     <- 실제 값 + 용도
```

#### Dominant Colors (06-7)

```
.dom-chart
  .dom-bar       <- 가로 누적 막대 (각 .dom-bar__seg에 flex + 배경색)
  .dom-list      <- 3열 grid, .item x N
    .chip        <- 색상 칩
    .hex         <- hex 값
    .cnt         <- 빈도 수
```

없으면 생략.

### 2-06. SS07 Spacing -> `.space-row` bar chart

```
section#spacing
  .space-note    <- 네이밍 규칙 callout (있으면)
  .space-table
    .space-row x N
      .tk        <- 토큰명
      .val       <- px 값
      .bar       <- 실제 width를 px 값으로 설정
```

**MUST**: `.bar`의 `width`를 해당 토큰의 실제 px 값으로 설정.

### 2-07. SS08 Radius -> `.rad-card`

```
section#radius
  .rad-grid (step 수에 따라 columns 조정: 7개=7열, 6개=6열 등)
    .rad-card x N
      .rad-box   <- 실제 border-radius 적용
      .rad-card__n <- 이름
      .rad-card__v <- 값 + 용도
```

**MUST**: `.rad-box`에 `style="border-radius:{value}"` 적용.

### 2-08. SS09 Shadows -> `.sh-card`

```
section#shadows
  .sh-grid (3열)
    .sh-card x N  <- 실제 box-shadow CSS 적용
      .sh-card__n <- level 이름
      .sh-card__d <- 설명
      .sh-card__v <- shadow 값 (monospace)
```

**MUST**: `.sh-card`에 `style="box-shadow:{value}"` 적용.

### 2-09. SS10 Motion -> `.motion-table`

```
section#motion
  .motion-table
    .motion-row x N
      .pt   <- 패턴명
      .val  <- 값 (duration, easing)
      .use  <- 용도
```

### 2-10. SS11 Layout Patterns -> `.lp-grid` 2열 카드

```
section#layout
  .lp-grid (2열)
    .lp-card x 4~6
      h3    <- 카테고리 (Grid, Hero, Card, Nav, Section Rhythm, Content Width 등)
      ul li <- 항목들 (bold 키 + 값)
      pre   <- 코드 블록 (있으면)
```

SS11의 서브섹션(Grid System, Hero, Section Rhythm, Card Patterns, Navigation, Content Width)을 각각 `.lp-card`로.

### 2-11. SS12 Responsive -> `.resp-table` + `.resp-grid`

```
section#responsive
  .resp-table         <- 브레이크포인트 테이블
    .resp-row--head   <- 헤더
    .resp-row x N
      .bp-name        <- 이름 (Mobile, Tablet 등)
      .bp-val         <- 값
      .bp-desc        <- 설명
  .resp-grid (2열)    <- 접기 전략, Touch targets, Image behavior
    .resp-card x N
      .resp-card__head <- 카테고리
      .resp-card__body <- 내용
```

### 2-12. SS13 Components -> `.cmp-block`

```
section#components
  .cmp-block x N
    .cmp-block__head
      .cmp-block__name  <- 클래스명
      .cmp-block__desc  <- variant 설명
    .cmp-block__body (2열: 데모 + 스펙)
      .cmp-demo         <- 데모 영역 (가능하면 실제 스타일 적용)
      .cmp-spec         <- 스펙 상세 (monospace)
    .cmp-code           <- HTML 마크업 + Copy 버튼
```

- design.md에 ```html 블록이 있으면 `.cmp-code`에 그대로 사용
- 데모 재현 불가 시: `.cmp-demo`에 muted placeholder

### 2-13. SS14 Content Voice -> `.voice-grid`

```
section#voice
  .voice-grid (2열)
    .voice-card x N
      .voice-card__label <- 패턴명 (Headline, CTA 등)
      .voice-card__rule  <- 규칙
      .voice-card__ex    <- 예시 (brand-color left border)
```

### 2-14. SS15+SS16 Code Export -> 탭 전환 + Copy

```
section#export
  .code-export
    .code-tabs
      button "CSS 스니펫" (.is-active)
      button "Tailwind 설정"
      .code-copy "Copy"
    .code-pane[data-pane="css"].is-active
      pre <- SS15 코드 블록
    .code-pane[data-pane="tw"]
      pre <- SS16 코드 블록 (없으면 탭 자체 제거)
```

- SS16 Tailwind 없으면 -> Tailwind 탭 버튼 제거, CSS만
- 탭 전환 + 클립보드 복사는 Layer 0의 canonical JS가 처리

### 2-15. SS17 Agent Prompt Guide -> `.agent-ref` + `.agent-prompt-card`

```
section#agent
  .agent-ref            <- Quick Color Reference 테이블
    .agent-ref__head
    .agent-ref__row x N
      .agent-ref__role  <- 역할
      .agent-ref__token <- 토큰명
      .agent-ref__hex   <- hex + .agent-ref__chip (색상 칩)
  .agent-prompts (2열)  <- Example Component Prompts
    .agent-prompt-card x N
      .agent-prompt-card__head
        .agent-prompt-card__icon
        .agent-prompt-card__name
      .agent-prompt-card__body
        pre             <- 프롬프트 텍스트
  .agent-tips           <- Iteration Guide
    .agent-tips__head
    ul li x N
```

### 2-16. SS18 Do/Don't -> `.dd-grid` 2열

```
section#verdict
  .dd-grid (2열)
    .dd-card.dd-card--do   <- 녹색 배지 + check 리스트
      h3 "DO"
      ul li x N
    .dd-card.dd-card--dont <- 빨간 배지 + X 리스트
      h3 "DON'T"
      ul li x N
  .myth-table (있으면)     <- 교정표/Myth 테이블
    .myth-row--head
    .myth-row x N
      .wrong
      .right
      .why
```

---

## Layer 3: 파싱 규칙 (PARSING RULES)

### 3-1. Typography Normalization

design.md의 타이포 테이블은 서비스마다 컬럼 구조가 다름. 의미 기반으로 매핑:

#### 컬럼 동의어 테이블

| 속성 | 동의어 (어느 것이든 매칭) |
|---|---|
| **size** | Size, rem, px, font-size, 크기 |
| **weight** | Weight, font-weight, bold, 굵기 |
| **line-height** | Line-height, lh, 줄높이, leading |
| **letter-spacing** | Letter-spacing, tracking, 자간, ls |
| **token** | Token, Class, Name, 토큰 |
| **usage** | Usage, Use, Context, 용도 |

#### 매핑 우선순위

1. 테이블 헤더 행의 컬럼명을 위 동의어로 매칭
2. 매칭 안 되는 컬럼 -> 해당 속성은 inline style에서 생략
3. Weight 컬럼이 없으면 -> frontmatter `font_weight_normal` 값을 기본값으로
4. 숫자 뒤 주석: `"400 (3회)"` -> 첫 번째 정수 `400`만 추출
5. `.875rem` 같은 소수점 시작 -> **앞점 반드시 유지**
6. 헤더 행 (`| Token | Size | ...`)과 구분자 행 (`|---|---|...`)은 데이터가 아님 -> 렌더 금지

### 3-2. Color Brightness — `.sw--l` vs `.sw--d` 결정

WCAG 상대 휘도 공식:

```
hex -> RGB (0~255)
R' = R/255, G' = G/255, B' = B/255

각 채널 선형화:
  c <= 0.04045 -> c/12.92
  c > 0.04045 -> ((c + 0.055)/1.055)^2.4

상대 휘도 L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin

L > 0.179 -> 밝은 배경 -> .sw--l (어두운 텍스트)
L <= 0.179 -> 어두운 배경 -> .sw--d (밝은 텍스트)
```

간이 판단: R+G+B 합이 384 (=128x3) 이상이면 `.sw--l`, 미만이면 `.sw--d`.

### 3-3. 한글 톤 규칙

| 영역 | 처리 |
|---|---|
| CSS 속성, 토큰명, 클래스, hex | 영어 유지 |
| 섹션명 | 혼용 외래어 (스페이싱, 라디우스, 섀도우) |
| 본문 | 한국어, 과장 금지 |
| 첫 등장 용어 | 하이브리드: `라디우스(모서리 반경)` |
| Do / Don't | 영어 유지 |

#### 섹션 타이틀 작성법

- **MUST**: 정보 서술형. 직역 금지.
- 각 서비스의 핵심 특징을 반영
- 예: Stripe "본문 굵기는 300이다", Linear "Marketing vs App 이중 팔레트"

| 금지 | 올바른 |
|---|---|
| "일곱 개의 모서리" | "라디우스 7단" |
| "가짜 데이터의 함정" | "자주 틀리는 것들" |
| "그림자는 쌍으로 온다" | "섀도우는 항상 두 겹" |

---

## Layer 4: QA (QUALITY ASSURANCE)

### 4-1. 필수 PASS (하나라도 실패 -> 재생성)

- [ ] `<!doctype html>`로 시작, `</html>`로 끝남
- [ ] `<!-- BEGIN:CANONICAL_STYLE -->` ~ `<!-- END:CANONICAL_STYLE -->` sentinel 존재
- [ ] `--brand-color`가 frontmatter의 `brand_color`와 일치
- [ ] `--font-display`가 서비스 display font를 포함
- [ ] TOC 7그룹 존재, 한글 라벨 정확
- [ ] TOC 번호가 연속 (빈 번호 없음)
- [ ] Quick Start: dark card + 빨간 경고 존재
- [ ] Typography: 실제 font-size/weight로 inline style 렌더, 헤더 행 없음
- [ ] Colors: hex 값이 design.md와 일치, 스와치 배경색 적용됨
- [ ] Code Export: 탭 전환 JS 존재, Copy 버튼 존재
- [ ] Do/Don't: 녹색/빨간 카드
- [ ] 선택 섹션: design.md에 없는 섹션은 HTML + TOC 둘 다 없음
- [ ] 한글 네이밍: 스페이싱/라디우스/섀도우/Do/Don't

### 4-2. 권장 PASS

- [ ] Screenshot: `screenshots/hero-cropped.png` 있으면 Hero에 삽입, 없으면 생략
- [ ] Spacing: bar의 width가 실제 px 값
- [ ] Radius: `.rad-box`에 실제 border-radius 적용
- [ ] Shadows: `.sh-card`에 실제 box-shadow 적용
- [ ] design.md에 없는 값이 HTML에 나타나지 않음

### 4-3. Failure Policy

| 상황 | 처리 |
|---|---|
| YAML frontmatter 파싱 실패 | 폴더명을 slug로, 나머지 1-2의 fallback 적용 |
| 섹션 내용이 비어있거나 N/A만 | 해당 섹션 건너뜀 (TOC에서도 제거) |
| 코드블록 없음 (SS15/SS16) | Code Export 섹션 전체 생략 |
| hex 값 비표준 형식 | 문자열 그대로 표시 (변환 시도 안 함) |
| 컴포넌트 데모 재현 불가 | 코드 블록만 표시, 데모 영역은 muted placeholder |
| 스크린샷 파일 없음 | Hero screenshot div 전체 생략 |
| 테이블 파싱 불가 | 원문 마크다운 그대로 `<pre>` 블록에 삽입 |

### 4-4. Batch Isolation

한 에이전트가 여러 서비스를 연속 처리할 때:

1. **서비스 간 독립.** 이전 서비스의 값/구조를 다음 서비스에 carry-over 금지.
2. **TOC 번호 재계산**: optional 섹션 제거 후 빈 번호 없이 연속 번호 (00, 01, 02, 03...).
3. **상태 리셋**: 각 서비스 시작 전, 이전 서비스의 brand_color, font, theme 등을 완전히 잊고 새 frontmatter에서만 읽는다.
4. **파일 격리**: 출력은 반드시 해당 서비스 폴더 안에만 (`insane-design/{slug}/report.ko.html`).

### 4-5. Anti-patterns — 12개 절대 금지

| # | 안티패턴 | 올바른 처리 |
|---|---|---|
| 1 | design.md에 없는 hex/토큰명/폰트명 지어내기 | design.md에 적힌 것만 사용 |
| 2 | 다른 서비스의 값을 이 서비스에 복사 | 각 서비스는 자기 design.md만 참조 |
| 3 | 마크다운 테이블 헤더 행을 데이터로 렌더 | `\| Token \| Size \|`는 헤더 -> 스킵 |
| 4 | font-weight에 font-size px 값 넣기 | weight와 size 컬럼 구분 (3-1 참조) |
| 5 | `"400 (3회)"` -> `4003`으로 파싱 | 첫 번째 정수만 추출 -> `400` |
| 6 | `.875rem` -> `875rem` 앞점 탈락 | 소수점 유지 -> `.875rem` |
| 7 | 섹션 타이틀 1:1 직역 | 정보 서술형 (3-3 참조) |
| 8 | 과장 부사 ("충격적", "놀라운", "혁신적") | 사실 서술만 |
| 9 | Quick Start 3칸을 1칸으로 합치기 | `/* 1. */` 주석 기준 분리 |
| 10 | Stripe 데이터를 다른 서비스에 사용 | Stripe report는 구조 참조만 |
| 11 | `report.css` 클래스/속성 수정 | Layer 0 위반 — CSS 수정 금지 |
| 12 | sentinel 주석 (`BEGIN/END:CANONICAL_STYLE`) 누락 | 반드시 포함 |
