---
name: insane-design
description: Extract a deterministic design system from any URL by fetching real CSS, parsing custom properties, and writing a 19-section design.md plus an interactive report.ko.html. Also exports design.md frontmatter to W3C DTCG tokens.json. Use when the user wants real CSS tokens, a reusable design reference, design tokens, or a design pack that feeds apply/build flows. Korean triggers — "디자인 분석해줘", "이 사이트 디자인 시스템 뽑아줘", "CSS 뜯어봐", "design.md 만들어줘", "레퍼런스 리포트 만들어줘", "사이트 분석", "디자인 토큰 추출", "tokens.json 내보내줘". English triggers — "analyze design", "extract design tokens", "rip the design system", "what CSS does this site use", "export DTCG tokens".
---

# Insane Design for Codex (analysis + export)

> URL 하나 → 실제 CSS 기반 design.md + 인터랙티브 report.ko.html.
> design.md frontmatter → W3C DTCG tokens.json export도 이 스킬이 담당한다.

이 문서는 참고 문서가 아니라 **실행 지시서**다. URL이 제공되면 즉시 Step 1부터 실행한다.

## Persona

```
You are an expert designer. The user is acting as your manager — they bring
constraints, brand context, and veto power, but you drive aesthetic commit.
Never hedge; pick one BOLD direction and defend it.
```

전체 계약: `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §1 Identity.

## Modes (이 스킬 내부 분기)

- **analysis** (기본): URL → design.md + report.ko.html (아래 7-Step)
- **export**: 이미 만든 design.md → tokens.json (DTCG). 아래 "Export 모드" 참조.

`apply`와 `build`는 별도 스킬(`insane-apply`, `insane-build`)이다.

## Codex 상호작용 규칙 (§A)

Codex CLI에는 `question prompt` 카드 UI가 **없다**. 질문이 필요하면
`shared/questioning-policy.md` §A의 채팅 번호 블록으로 대체한다.

- analysis는 인터뷰형이 아니라 **추출형**이다. URL과 출력 루트가 명확하면 질문 없이 진행하고,
  추론 가능한 건 묻지 않는다(§1 "추론 가능한 건 안 묻기").
- URL/출력 루트가 모호할 때만 §A 번호 블록으로 **1회** 확인한다(추천안을 1번에).
- 토큰/색/폰트는 **추출**한다 — 환각으로 만들지 않는다.

## 사전 준비 (필요 Step에서 Read)

- `$PLUGIN_ROOT/skills/insane-design/references/schema.v3.2.md` — frontmatter+섹션 단일 진실 원천 (Step 0, 가장 먼저 Read 필수)
- `$PLUGIN_ROOT/skills/insane-design/references/template.md` — design.md 19섹션 v3.2 템플릿 (Step 5)
- `$PLUGIN_ROOT/skills/insane-design/references/narrative-vocabulary.md` — §00 archetype metaphor 카탈로그 (Step 4 §00 작성)
- `$PLUGIN_ROOT/skills/insane-design/references/report-prompt.md` — HTML 리포트 생성 규칙 (Step 6)
- `$PLUGIN_ROOT/skills/insane-design/references/report.css` — canonical CSS (Step 6)
- `$PLUGIN_ROOT/skills/insane-design/references/pitfalls.md` — 14가지 함정 (Step 4)
- `$PLUGIN_ROOT/skills/insane-design/references/data-collection.md` — fetch 에스컬레이션 상세 (Step 2)
- `$PLUGIN_ROOT/skills/insane-design/examples/stripe/design.md` — 골드 스탠다드 (Step 5 참조, 있으면)

---

## 워크플로우 — 7 Steps

> **경로 규칙**: 모든 산출물은 **프로젝트 루트** 기준 `insane-design/{slug}/` 하위에 저장.
> Step 실행 전 `WORK_DIR`을 확정한다. 플러그인 자산은 `$PLUGIN_ROOT/...`(읽기 전용).

```bash
WORK_DIR="$(pwd)"   # 사용자의 현재 디렉토리를 프로젝트 루트로 사용
```

### Step 1: INIT — script

1. URL에서 slug 추출 (도메인 → kebab-case: `stripe.com` → `stripe`).
2. URL 검증 (**보안 필수**):
   - `http://` / `https://` 프로토콜 확인
   - `localhost`, `127.0.0.1`, `file://` 차단
   - 셸 메타문자(`` ` `` `$` `(` `)` `;` `|` `&` `>` `<`) 포함 시 거부
   - 이후 모든 명령에서 URL은 큰따옴표로: `"$URL"`
3. **매체(medium) 감지** (frontmatter용):

   | 입력 패턴 | medium | confidence |
   |----------|--------|------------|
   | `.pptx`/`.ppt`로 끝남 | `slide` | high |
   | `docs.google.com/presentation/*` | `slide` | high |
   | `*.pdf`로 끝남 | `print` | high (스텁) |
   | `*.figma.com/file/*` (DS 탐지 시) | `design-system` | medium |
   | 이미지 업로드 + 정사각 | `card-news` | medium |
   | 그 외 일반 URL | `web` | high (기본) |

4. **Archetype 감지** (판정 #21 — 11 enum + freeform): 도메인 끝 / meta tag(`og:type`) /
   hero 첫인상으로 분류. enum: commerce-marketplace / editorial-product / editorial-magazine /
   app-dashboard / saas-marketing / landing-utility / documentation-site / portfolio-personal /
   automotive / luxury-brand / other. `archetype_confidence`: high/medium/low.
5. 출력 디렉토리 생성 (절대 경로):
   ```bash
   mkdir -p "$WORK_DIR/insane-design/{slug}/"{screenshots,css,phase1}
   ```
6. 시작 알림: `🎨 {slug} 디자인 분석을 시작합니다. URL: {url} · 예상 3-5분`.

### Step 2: FETCH — script

HTML/CSS와 스크린샷을 수집한다. 상세 에스컬레이션: `references/data-collection.md`.

**성공 판정 함수** (모든 tier 적용):
```bash
html_ok() {
  local f="$1"
  [ -s "$f" ] || return 1
  [ "$(wc -c < "$f")" -ge 5000 ] || return 1
  grep -q "<html" "$f" || return 1
  grep -qiE "challenge-error-text|cf_chl_opt|__cf_chl_jschl|verify you are human|checking your browser" "$f" && return 1
  return 0
}
css_ok() {
  local f="$1"
  [ -s "$f" ] || return 1
  [ "$(wc -c < "$f")" -ge 200 ] || return 1
  grep -qiE "DOCTYPE HTML|403 ERROR|Access Denied|Request could not be satisfied|challenge-error-text" "$f" && return 1
  return 0
}
```

**HTML 6-tier 에스컬레이션**:
```bash
URL="{url}"; OUT="$WORK_DIR/insane-design/{slug}/index.html"
# Tier 1: curl Chrome Desktop UA
curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" \
  -H "Accept-Language: en-US,en;q=0.9" --compressed --max-time 30 -o "$OUT" "$URL"
# Tier 2: curl Mobile UA
if ! html_ok "$OUT"; then
  curl -sL -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1" \
    --compressed --max-time 30 -o "$OUT" "$URL"; fi
# Tier 3: Jina Reader HTML 모드 (⚠️ 대상 URL이 r.jina.ai로 전송됨 — 민감 URL 금지)
if ! html_ok "$OUT"; then
  curl -sL --max-time 45 -H "X-Return-Format: html" "https://r.jina.ai/$URL" -o "$OUT"; fi
# Tier 4: curl_cffi TLS 임퍼소네이션 (safari/chrome/firefox)
# Tier 5: Wayback Machine 캐시 (⚠️ 외부 전송)
# Tier 6: playwright (JS 챌린지 전용 — 설치돼 있을 때만)
```

**CSS 수집**: HTML에서 `href="*.css"` 추출 → 다운로드 → `css_ok` 실패 시 curl_cffi →
Wayback fallback. CSS 0개면 인라인 `<style>` 추출하여 `css/_inline.css`로 저장.

**스크린샷**: 1차 Jina(`X-Respond-With: screenshot` + `X-Wait-For: 5000`) → PIL crop
(`screenshots/hero-cropped.png`). 2차 playwright fallback(설치 시, < 50KB일 때).

**수집 실패 처리**: HTML 전 tier 실패 → "접근 불가" + 중단. CSS 0개 → 경고 후 hex frequency로 진행.
스크린샷 실패 → 경고 후 계속.

### Step 3: EXTRACT — script

CSS에서 토큰 추출. `$WORK_DIR`에서 **반드시 이 순서**로:
```bash
cd "$WORK_DIR"
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/var_resolver.py" {slug}
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/brand_candidates.py" {slug}
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/typo_extractor.py" {slug}
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/alias_layer.py" {slug}
```
결과: `insane-design/{slug}/phase1/`에 4개 JSON (brand_candidates / resolved_tokens / typography / alias_layer).

> §11 Layout / §12 Responsive / §13 Components는 스크립트로 추출하지 않는다. Step 4에서
> Codex/Codex가 CSS를 직접 읽고 판단한다.

CSS custom properties 0개면: "CSS 토큰 부족" 경고 후 hex frequency 기반으로 전환.

### Step 4: INTERPRET — prompt (멀티모달)

스크린샷 + 추출 결과 + CSS 원본을 직접 읽고 판정한다.

1. Read `insane-design/{slug}/screenshots/hero-cropped.png`
2. Read `phase1/brand_candidates.json`, `phase1/typography.json`, `phase1/alias_layer.json`
3. Read `$PLUGIN_ROOT/skills/insane-design/references/pitfalls.md`
4. Read `insane-design/{slug}/index.html` + 주요 CSS (§11/§13용; >500KB면 상위 2-3개만)

**판정 22가지** (요지): brand color 확정(hex) / light·dark·mixed / custom font / framework /
hero anatomy / 절대 금지 한 가지 / DO·DON'T(색상 DON'T는 hex 강제) / §00 Direction & Metaphor /
§11 Layout / §12 Responsive / §13 Components(6 카테고리+상태 6종+Named Variants+Signature Micro-Specs) /
§17 Agent Prompt / BOLD 방향성 / Aesthetic Category(12+other) / Signature Element /
Code Complexity / Negative-Space Identity / Typography Principles / Known Gaps /
Archetype / design_system_level.

**§00 Narrative**: `references/narrative-vocabulary.md`의 archetype top metaphor에서 1개 + 보편
어휘 2개 = 총 3+ metaphor floor. "절제된/모던한/미니멀한/premium/clean" 형용사로만 끝나는 문장 금지.

**§00 Direction Summary 4-line block** (apply 정규식이 매칭 — 형식 고정):
```
> **BOLD Direction**: {1-2 단어}
> **Aesthetic Category**: {12 enum + "other"}
> **Signature Element**: 이 사이트는 **{메타포}**으로 기억된다.
> **Code Complexity**: {low/medium/high/very_high} — {근거 한줄}
```

**§18 DON'T 색상 항목**: 반드시 구체 hex 포함 (apply/build grep 계약 — shared/README §2.2).
패턴: `"X를 [금지 hex]으로 두지 말 것 — 대신 [올바른 hex] 사용"`.

**환각 금지 3원칙**: hex 만들지 않기 / 토큰명 만들지 않기 / 팩트 위에 해석만.

### Step 5: WRITE-MD — generate

1. Read `references/schema.v3.2.md` (frontmatter+섹션 단일 진실 원천 — 필수)
2. Read `references/template.md` (19섹션 v3.2)
3. Read `examples/stripe/design.md` (있으면 — 구조 참조)
4. Step 3 팩트 + Step 4 해석 조합하여 19섹션 채움
5. Write `insane-design/{slug}/design.md`

**필수**: YAML frontmatter 맨 위 · `schema_version: 3.2` · medium/medium_confidence ·
archetype/archetype_confidence · design_system_level/evidence · 필수 섹션 15개
(00,01,02,03,04,05,06,07,08,11,13,15,17,18,19) · 모든 hex가 실제 CSS에 존재 · 파일 ≥ 12KB.

**토큰 참조 일관성**: §13 + §15 합쳐 `{colors.x}` 참조 비율 ≥ 70%. raw hex는 frontmatter
`colors:`에 named token으로 등록 후 본문에서 참조로 교체. 상세: `schema.v3.2.md` §3.

### Step 6: RENDER-HTML — generate

1. Read `references/report-prompt.md` (생성 규칙)
2. Read `references/report.css` (canonical CSS — 있으면)
3. Read `examples/stripe/report.ko.html` (있으면 — CSS/JS/구조 참조)
4. Read `insane-design/{slug}/design.md`
5. Write `insane-design/{slug}/report.ko.html`

**필수**: 한국어 · shadcn zinc 테마(Pretendard Variable + Inter + JetBrains Mono) ·
`--brand-color`만 서비스별 교체 · 인터랙티브(스와치 hover, 타이포 live preview, Copy 버튼) ·
hero에 `screenshots/hero-cropped.png` 삽입 · 파일 ≥ 20KB.

### Step 7: VALIDATE — script + review

```bash
# 자동 validator (8-check)
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/validate.py" insane-design/{slug}/design.md
# 수동 체크
head -1 insane-design/{slug}/design.md | grep -q '^---$'
for n in 00 01 02 03 04 05 06 07 08 11 13 15 17 18 19; do
  grep -q "^## $n\." insane-design/{slug}/design.md || echo "Missing §$n"; done
[ "$(wc -c < insane-design/{slug}/design.md)" -ge 12000 ]
[ "$(wc -c < insane-design/{slug}/report.ko.html)" -ge 20000 ]
for hex in $(grep -oE '#[0-9A-Fa-f]{6}' insane-design/{slug}/design.md | sort -u | head -3); do
  grep -qi "$hex" insane-design/{slug}/css/*.css || echo "Missing: $hex"; done
```
**실패 시**: 최대 2회 재생성(실패 항목만). 2회 후에도 실패면 경고 포함 출력.

**성공 보고**:
```
✅ {slug} 분석 완료!
📄 design.md:      insane-design/{slug}/design.md ({size}KB)
🌐 report.ko.html: insane-design/{slug}/report.ko.html ({size}KB)
📸 screenshot:     insane-design/{slug}/screenshots/hero-cropped.png

design.md를 첨부하면 이 사이트 스타일로 UI를 만들 수 있습니다.
report.ko.html을 브라우저에서 열면 인터랙티브 리포트를 볼 수 있습니다.
DTCG tokens.json이 필요하면 "tokens.json 내보내줘"라고 요청하세요.
```

---

## Export 모드 — design.md → DTCG tokens.json

사용자가 "tokens.json 내보내줘", "DTCG export", "export tokens" 등을 요청하면 실행한다.
design.md frontmatter의 토큰 그래프를 **W3C DTCG (Design Tokens Format Module)** JSON으로
변환한다. 결과는 Figma Tokens Studio / Style Dictionary / Specify / Cobalt UI 등에서 import 가능.

### Step E1: 입력 검증
```bash
WORK_DIR="$(pwd)"
INPUT="$WORK_DIR/insane-design/{slug}/design.md"
[ -f "$INPUT" ] || { echo "❌ 파일 없음: $INPUT"; exit 1; }
```
slug에 셸 메타문자(`` ` `` `$` `(` `)` `;` `|` `&`)가 포함되면 거부.

### Step E2: DTCG 변환
```bash
OUTPUT="$WORK_DIR/insane-design/{slug}/tokens.json"   # --output로 변경 가능
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/export_dtcg.py" "$INPUT" -o "$OUTPUT"
```
스크립트는 frontmatter의 `colors:`/`typography:`/`spacing:`/`rounded:`를 읽어:
- `colors:` → DTCG `color` 그룹 (`$type: color`)
- `typography.ladder:` → DTCG `typography` composite (`$type: typography`)
- `spacing:` → DTCG `spacing` (`$type: dimension`)
- `rounded:` → DTCG `radius` (`$type: dimension`)
- 메타(slug/archetype/design_system_level 등) → `$extensions["com.insane-design"]`

`--compact`(minified) 옵션 지원.

### Step E3: 결과 보고
```
✅ DTCG export 완료
📦 출력: insane-design/{slug}/tokens.json (N KB)
토큰 통계: color M / typography K / spacing L / radius P
→ Figma Tokens Studio · Style Dictionary · Cobalt UI에서 import 가능
```

**폴백**: frontmatter 토큰 그래프 객체가 비어 있으면 메타 wrapper만 출력 + 경고
("schema_version 3.2로 재분석 권장"). 의존성: Python 3.8+ (PyYAML 권장, 없으면 내장 minimal parser).

---

## References (요지)

| 파일 | 용도 | Step |
|------|------|------|
| `references/schema.v3.2.md` | frontmatter+섹션 단일 진실 원천 | 0, 5, 7 |
| `references/template.md` | design.md 19섹션 v3.2 | 5 |
| `references/narrative-vocabulary.md` | §00 archetype metaphor | 4 |
| `references/data-collection.md` | fetch 에스컬레이션 상세 | 2 |
| `references/report-prompt.md` + `report.css` | HTML 리포트 | 6 |
| `references/pitfalls.md` | 14 함정 | 4 |
| `references/methodology.md` | 분석 프로세스 + 체크리스트 | 전체 |
| `shared/README.md` | 공통 계약 (Identity·Contract·Verifier·AI Slop) | 전체 |

## Scripts

- `scripts/var_resolver.py` — CSS var() 체인 재귀 해결
- `scripts/brand_candidates.py` — 브랜드 색상 후보 (semantic + selector-role + frequency)
- `scripts/typo_extractor.py` — 타이포 스케일
- `scripts/alias_layer.py` — alias tier (util/action/component/core)
- `scripts/capture_jina_screenshots.py` — Jina 스크린샷 + PIL crop
- `scripts/validate.py` — v3.2 design.md 8-check validator
- `scripts/export_dtcg.py` — design.md → DTCG tokens.json
