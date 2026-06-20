# DESIGN.md Schema v3.2 — Canonical Specification

> **이 문서는 frontmatter + 섹션 구조의 단일 진실 원천(single source of truth)이다.**
> 분석 스킬 시작 시 가장 먼저 Read 되어 LLM 컨텍스트에 주입된다.
> `template.md`, `SKILL.md` Step 5, `scripts/validate.py`는 모두 이 문서의 종속 산출물이다.

**Version:** 3.2
**Status:** active (3.1 deprecated, 3.0 unsupported)
**Last updated:** 2026-05-15

---

## 1. Frontmatter Schema

### 1.1 식별/메타 (REQUIRED)

| 필드 | 타입 | 필수 | 허용값 / 형식 |
|---|---|:---:|---|
| `schema_version` | number | ✅ | `3.2` (literal — 다른 값은 거부) |
| `slug` | string | ✅ | kebab-case, 도메인 stem (e.g. `apple-fresh-v32`) |
| `service_name` | string | ✅ | 사람이 부르는 이름 (e.g. `Apple`) |
| `site_url` | string (URL) | ✅ | https://… |
| `fetched_at` | date | ✅ | `YYYY-MM-DD` |

### 1.2 1차 디자인 메타 (REQUIRED)

| 필드 | 타입 | 필수 | 허용값 |
|---|---|:---:|---|
| `default_theme` | enum | ✅ | `light` / `dark` / `mixed` |
| `brand_color` | hex | ✅ | `"#RRGGBB"` (반드시 따옴표) |
| `primary_font` | string | ✅ | font-family 이름 |
| `font_weight_normal` | number | ✅ | 100~900 |
| `token_prefix` | string | ✅ | CSS 변수 prefix (e.g. `--sk-`) 또는 `"N/A"` |

### 1.3 BOLD 리디자인 필드 (REQUIRED — apply 호환)

| 필드 | 타입 | 필수 | 허용값 |
|---|---|:---:|---|
| `bold_direction` | string | ✅ | 1~2 단어 BOLD 방향 (e.g. `"Photography Reverence"`) |
| `aesthetic_category` | enum | ✅ | redesign-aesthetics §3의 12종 + `"other"` |
| `signature_element` | enum | ✅ | `hero_impact` / `typo_contrast` / `section_transition` / `minimal_extreme` |
| `code_complexity` | enum | ✅ | `low` / `medium` / `high` / `very_high` |

### 1.4 매체 분기 (REQUIRED — build 스킬용)

| 필드 | 타입 | 필수 | 허용값 |
|---|---|:---:|---|
| `medium` | enum | ✅ | `web` / `slide` / `design-system` / `card-news` / `motion` / `print` |
| `medium_confidence` | enum | ✅ | `high` / `medium` / `low` |

### 1.5 v3.2 신규 필드 — Archetype + DS Level (REQUIRED)

| 필드 | 타입 | 필수 | 허용값 |
|---|---|:---:|---|
| `archetype` | enum | ✅ | `commerce-marketplace` / `editorial-product` / `editorial-magazine` / `app-dashboard` / `saas-marketing` / `landing-utility` / `documentation-site` / `portfolio-personal` / `automotive` / `luxury-brand` / `other` |
| `archetype_confidence` | enum | ✅ | `high` / `medium` / `low` |
| `design_system_level` | enum | ✅ | `lv1` (engineer spec) / `lv2` (system in use) / `lv3` (designer guidebook) |
| `design_system_level_evidence` | string | ✅ | 한 줄 근거 (CSS 변수 개수, alias layer, 명명 컨벤션 등 구체 증거) |

### 1.6 v3.2 토큰 그래프 (OPTIONAL — additive)

기존 16필드 보존. 추가 객체. **본문 hex와 cross-reference 가능**.

```yaml
colors:                                       # named tokens — 모두 CSS에 실재해야 함
  primary: "#0071E3"
  surface-light: "#F5F5F7"
  text-primary: "#1D1D1F"
  # 가상 alias 생성 금지

typography:
  display: "SF Pro Display"
  body: "SF Pro Text"
  ladder:
    - { token: h1, size: "56px", weight: 700, tracking: "-0.022em" }
  weights_used: [400, 600]
  weights_absent: [300, 500, 700]             # Negative identity 단서 — 필수

components:                                   # §13-2 Named Variants와 동기화
  button-primary: { bg: "{colors.primary}", radius: "980px", padding: "12px 22px" }
  # 발견된 변주만
```

**토큰 참조 문법:** `{group.token-name}` — colors/typography/spacing/rounded 그룹 참조.
**Dual notation 권장:** 본문에서 `color: #0071e3 /* {colors.primary} */` 또는 prose에서 `"#1D1D1F (\`{colors.text-primary}\`)"`.

---

## 2. Section Schema

### 2.1 19섹션 정의 (§00~§19)

| § | 섹션 제목 | 필수 | SOURCE |
|---|---|:---:|---|
| 00 | Visual Theme & Atmosphere (또는 `Direction & Metaphor`) | ✅ | manual |
| 01 | Quick Start | ✅ | manual |
| 02 | Provenance | ✅ | auto |
| 03 | Tech Stack | ✅ | auto+manual |
| 04 | Font Stack | ✅ | auto+manual |
| 05 | Typography Scale | ✅ | css |
| 06 | Colors | ✅ | css |
| 07 | Spacing | ✅ | css |
| 08 | Radius | ✅ | css |
| 09 | Shadows | ⭕ | css |
| 10 | Motion | ⭕ | css |
| 11 | Layout Patterns | ✅ | auto+manual |
| 12 | Responsive Behavior | ⭕ | css |
| 13 | Components | ✅ | auto+manual |
| 14 | Content / Copy Voice | ⭕ | manual |
| 15 | Drop-in CSS | ✅ | auto+manual |
| 16 | Tailwind Config | ⭕ | auto |
| 17 | Agent Prompt Guide | ✅ | manual |
| 18 | DO / DON'T | ✅ | auto+manual |
| 19 | Known Gaps & Assumptions | ✅ | manual |

**필수 섹션 합계: 15개** (00, 01, 02, 03, 04, 05, 06, 07, 08, 11, 13, 15, 17, 18, 19).
**선택 섹션 5개:** 09, 10, 12, 14, 16 — 데이터 없으면 통째 제거 (빈 섹션 금지).

### 2.2 섹션 헤딩 규칙

- 모든 섹션은 `## NN. Title` 형식 (`##` h2, 두 자리 번호 + 점 + 공백 + 제목).
- `##` 바로 다음 줄에 `<!-- SOURCE: auto|manual|auto+manual|css -->` 주석 권장.

### 2.3 N/A 처리

| 시나리오 | 동작 |
|---|---|
| 섹션 전체 없음 | 해당 `##` 블록을 통째로 제거 |
| 표 전체 누락 | 표 대신 `> N/A — {reason}` 한 줄 작성 |
| 필드 단일 누락 | `{VAR}` → `N/A` 로 채움 |

---

## 3. 토큰 참조 일관성 룰 (v3.2 신규)

본문 작성 시 hex 표기는 **섹션별로 다른 룰**을 따른다.

| 섹션 카테고리 | 표기 | 예시 |
|---|---|---|
| **YAML frontmatter** (1.6 객체) | hex 직접 표기 | `primary: "#0071E3"` |
| **§00 Direction/Narrative** | hex + 토큰 dual notation 권장 | `"#1D1D1F (\`{colors.text-primary}\`)"` |
| **§06 Colors 표** | hex 직접 표기 (정의 위치) | `\| primary \| #0071E3 \| ...` |
| **§13 Components 표/YAML** | **`{colors.x}` 참조 사용** | `bg: "{colors.primary}"` |
| **§15 Drop-in CSS** | dual notation 권장 | `background: #0071e3 /* {colors.primary} */` |
| **§16 Tailwind Config** | hex 직접 표기 | `colors: { primary: "#0071E3" }` |
| **§18 DO/DON'T** | hex 직접 표기 (위반 grep용) | `❌ border-radius: 8px on .button-primary` |

**목표 토큰화율:** components 섹션 + Drop-in CSS 합쳐서 **≥ 70%** (`{colors.x}` 사용 비율).
**측정:** `grep -oE '\{colors\.[a-z-]+\}' design.md` 카운트 / `grep -oE '#[0-9A-Fa-f]{6}' design.md` 카운트.

---

## 4. 마이그레이션 가이드

### 3.1 → 3.2

1. `schema_version: 3.1` → `3.2` (필수)
2. 추가 필드 6개 채우기:
   - `archetype`, `archetype_confidence`
   - `design_system_level`, `design_system_level_evidence`
3. 토큰 그래프 객체화 (선택, 권장):
   - `colors:` (named tokens)
   - `typography:` (`weights_used` + `weights_absent` 필수)
   - `components:` (§13-2와 동기화)
4. §19 Known Gaps 섹션 추가 (필수)

### < 3.1 (`schema_version` 없음)

레거시. 마이그레이션 시 위 단계 + `medium`, `medium_confidence` 추가.

---

## 5. 검증 체크리스트 (validate.py 8 checks와 1:1 매핑)

| # | Check | 기준 |
|---|---|---|
| 1 | `schema_version` | literal `3.2` |
| 2 | `frontmatter_required` | 1.1~1.5의 필수 필드 모두 존재 |
| 3 | `mandatory_sections` | 15개 필수 섹션 정규식 매치 |
| 4 | `craft_floor` | §13-3 Signature Micro-Specs ≥ 5개 |
| 5 | `negative_space_floor` | 의도된 부재 명시 (`weights_absent` 등) |
| 6 | `known_gaps_floor` | §19 ≥ 1개 항목 |
| 7 | `file_size` | ≥ 12KB |
| 8 | `direction_summary_format` | §00에 4필드 모두 포함 |

---

## 6. LLM 사용 지시

이 스키마를 분석 스킬 시작 시 Read 한 LLM은:
1. **frontmatter를 추측하지 않고 §1의 표를 그대로 채운다.**
2. **§2의 19섹션 순서를 그대로 따른다.**
3. **§3의 토큰 참조 룰을 components/Drop-in CSS에서 강제 적용한다.**

frontmatter 작성 시 위 표의 컬럼 순서대로 출력하되, 섹션별 빈 줄로 구분한다 (가독성).
