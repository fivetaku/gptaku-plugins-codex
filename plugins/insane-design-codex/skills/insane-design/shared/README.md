# insane-design — Shared Contract for Codex (v3.2)

> 이 문서는 `insane-design`(analysis), `insane-apply`, `insane-build` 세 스킬이 공유하는
> **페르소나 · 계약 · 검증 프로토콜 · AI Slop 안티패턴 · Starter Components 인덱스**다.
> 각 스킬의 SKILL.md는 해당 섹션을 Read하여 사용한다.
>
> **변경 금지 원칙**: 세 스킬이 이 파일을 공통 계약으로 본다. 필드·섹션 번호·frontmatter
> 스키마를 바꾸면 analysis ↔ apply ↔ build 간 파이프가 즉시 깨진다.
>
> **Codex 차이**: 본진(Claude Code) `_shared/README.md`의 Codex 이식판. 정책·계약은 동일하되,
> (1) `${CLAUDE_PLUGIN_ROOT}` → `$PLUGIN_ROOT`, (2) `AskUserQuestion` 카드 → `shared/questioning-policy.md §A` 번호 블록,
> (3) 비동기 `Task(run_in_background)` verifier → **동기 grep/lint 검증**으로 치환했다.

---

## 1. Identity (페르소나 락인)

모든 스킬의 SKILL.md 상단에 다음 5줄을 identity 선언으로 포함한다. 사용자 발화가 어떤
톤이든 이 role을 유지한다. Manager(사용자)의 취향을 수집하되, *디자인 판단의 최종 권한은
당신에게 있다.*

```
You are an expert designer. The user is acting as your manager — they bring
constraints, brand context, and veto power, but you drive aesthetic commit.
Never hedge with "maybe", "it depends", or present 3 neutral options hoping
the user picks. Pick one BOLD direction, defend it, and only diverge when
the manager explicitly overrides.
```

**페르소나 위반 시그널** (자가 진단용 — 스스로 발견 시 즉시 복귀):
- 선택지 3개 이상 제시 + 우열 표시 없음
- "사용자 취향에 따라…" 류 책임 회피 문장
- design.md에 명시된 값 대신 "일반적으로는…" 제시
- BOLD 방향성 커밋 없이 중립 값 선택

> §A 번호 블록과 페르소나는 충돌하지 않는다. 번호 블록을 쓸 때도 **추천안을 1번에 두고
> 우열을 명시**한다(질문 정책 §A). "중립 3옵션 나열"은 금지.

---

## 2. Contract — §18 DON'T · frontmatter 스키마

세 스킬이 공유하는 **쓰기/읽기 계약**. 이 계약을 깨면 analysis가 만든 design.md를
apply/build가 읽지 못한다.

### 2.1 frontmatter 스키마 v3.2 (Designer Guidebook 전환)

`analysis`는 반드시 다음 필드를 모두 채워 `design.md` 맨 위에 쓴다.
`apply`/`build`는 이 필드를 정규식으로 파싱한다.

```yaml
---
schema_version: 3.2                  # 필수 — literal 3.2 (다른 값 거부)
slug: {SLUG}
service_name: {SERVICE_NAME}
site_url: {SITE_URL}
fetched_at: {FETCHED_AT}
default_theme: {light|dark|mixed}
brand_color: {BRAND_HEX}
primary_font: {PRIMARY_FONT}
font_weight_normal: {WEIGHT_NORMAL}
token_prefix: {TOKEN_PREFIX}

# Lv3 BOLD 리디자인 지원 (v3.0~)
bold_direction: {BOLD_DIRECTION}
aesthetic_category: {AESTHETIC_CATEGORY}     # 12 enum + "other"
signature_element: {SIGNATURE_ELEMENT}
code_complexity: {CODE_COMPLEXITY}

# v3.1 — 매체 분기
medium: web                          # web | slide | design-system | card-news | motion | print
medium_confidence: high              # high | medium | low

# v3.2 — Archetype + Design System Level (판정 #21, #22)
archetype: {ARCHETYPE}               # commerce-marketplace / editorial-product / editorial-magazine /
                                     # app-dashboard / saas-marketing / landing-utility /
                                     # documentation-site / portfolio-personal / automotive /
                                     # luxury-brand / other
archetype_confidence: high           # high | medium | low
design_system_level: lv2             # lv1 (engineer spec) / lv2 (system in use) / lv3 (designer guidebook)
design_system_level_evidence: "{한 줄 근거}"

# v3.2 — 데이터 객체화 (OPTIONAL, Cross-reference 토큰 그래프)
# "데이터는 YAML, 영혼은 Prose". 본문 hex 직접 박힘은 그대로 유지 — apply 정규식은 hex grep.
# 객체는 ADDITIVE 사용 (apply가 무시하면 영향 없음)

colors:                              # named token만 — CSS에 실재해야 함
  # primary: "{HEX}"

typography:
  # display: "{FONT}"
  # ladder: [...]
  # weights_used: [...]
  # weights_absent: [...]            # Negative identity 단서

components:                          # §13-2 Named Variants와 동기화
  # button-primary: { ... }
---
```

**하위 호환**:
- v3.1 파일은 archetype/design_system_level/객체 없음 → apply/build가 default 처리, 경고만
- v3.0 파일은 medium 없음 → `medium: web`, `medium_confidence: medium` 간주
- 재생성 강요 금지

**v3.2 변경 요약 (ADDITIVE only — BREAKING 0)**:
- 신규 frontmatter 필드: archetype / archetype_confidence / design_system_level / design_system_level_evidence
- 신규 frontmatter 객체 (OPTIONAL): colors / typography / components
- 신규 섹션: §19 Known Gaps & Assumptions (필수)
- 신규 sub-section: §00 Narrative + Direction Summary 분리, §04 Note on Font Substitutes, §05 Principles, §06-8 Color Stories, §07 Whitespace Philosophy, §13-2 Named Variants, §13-3 Signature Micro-Specs, §18 What This Site Doesn't Use
- 자유도 회복: §00 4문단 강제 → 자유 narrative
- apply Phase 3 정규식 모두 보존 (BOLD Direction Summary 4-line / §13 6 카테고리 / §15 :root / §18 hex grep 6쿼터)

스키마 단일 진실 원천: `$PLUGIN_ROOT/skills/insane-design/references/schema.v3.2.md`.

### 2.2 §18 DON'T hex-grep 계약 (analysis 쓰기 · apply/build 읽기)

> **⚠️ per-brand contract — 즉석 합성 시 특히 주의**
> §18 DON'T는 **"이 브랜드를 재현할 때 하지 말 것"** 의 per-brand 규칙이다.
> 범용/global 규칙이 아니다.
>
> - Coupang 재현 → 배경 `#FFFFFF` 사용은 **맞음** (쿠팡 실제 배경)
> - Tesla 재현 → 배경 `#FFFFFF` 사용은 **금지** (Tesla는 `#F4F4F4`)
> - Stripe 재현 → body `font-weight: 400` 사용은 **금지** (Stripe는 300)
>
> 맨바닥 즉석 합성(insane-build Step 0.5) 시 다른 브랜드의 §18 DON'T를 그대로 복사하지
> 말 것. 합성하는 가상 브랜드의 실제 선택을 기반으로 §18 DON'T를 새로 작성해야 한다.

`analysis`는 §18 DON'T 항목 중 **색상 관련 모든 항목에 구체 hex를 포함**한다.
이 계약이 깨지면 apply/build의 Step 3 동기 검증이 무력화된다.

**쓰기 규칙 (analysis)**:
```
"X를 [금지 hex/값]으로 두지 말 것 — 대신 [올바른 hex/값] 사용"

예:
- "배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#F4F4F4` 사용"
- "텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#1D1D1F` 사용"
- "body에 `font-weight: 400` 사용 금지 — Stripe는 300이 맞다"
```

**읽기 규칙 (apply/build Step 3)**:
생성된 HTML/CSS를 design.md §18 DON'T의 hex/weight/속성으로 grep(`rg`/`grep`) 하여
위반을 탐지한다.

**grep 쿼터 (Step 3 필수 최소 호출)**:
- 색상 DON'T 위반 스캔: **최소 2회** (배경 + 텍스트)
- 구조 DON'T 위반 스캔: **최소 2회** (예: body weight, border-radius)
- 타이포 DON'T 위반 스캔: **최소 2회** (예: 금지 폰트, weight)

총 **최소 6회 grep**. 위반 1건도 미검증이면 Step 3 미통과 처리.

### 2.3 경로 계약

| 산출물 | 경로 | 쓰는 스킬 | 읽는 스킬 |
|--------|------|-----------|-----------|
| `design.md` | `insane-design/{slug}/design.md` | analysis | apply, build |
| `report.ko.html` | `insane-design/{slug}/report.ko.html` | analysis | (사용자 열람) |
| `tokens.json` (DTCG) | `insane-design/{slug}/tokens.json` | analysis(export) | (외부 도구) |
| build variations | `insane-build/{session}/variations/v{N}/index.html` | build | (사용자 열람) |
| screenshots | `insane-design/{slug}/screenshots/hero-cropped.png` | analysis | apply §00 참고 |

모든 산출물 경로는 **프로젝트 루트 기준**. 플러그인 내부 자산(`examples/`, `scripts/`,
`references/`, `shared/`)은 `$PLUGIN_ROOT/skills/insane-design/...` 하위에서 **읽기 전용**.

---

## 3. Verifier Protocol — Codex는 동기 검증

> **Codex 차이**: Claude Code 판은 `Task(run_in_background)`로 비동기 verifier를 포크하고
> 별도 `verify` 커맨드로 polling 했다. **Codex CLI에는 비동기 백그라운드 Task 포크 계약이
> 없으므로**, 검증은 **모두 동기(synchronous)** 로 같은 턴 안에서 수행한다. 별도 verify
> 커맨드/job_id polling은 존재하지 않는다.

### 3.1 기본 원칙

- **기본값**: 동기 `rg`/`grep`-only. (§2.2 grep 쿼터 6회)
- **더 깊은 검증**(스크린샷 diff · 콘솔 오류)은 **playwright가 설치돼 있을 때만** 같은 턴에
  추가로 돌린다. 미설치 시 grep-only가 정상 경로 — 설치 강요 금지.
- 메인 흐름을 멈추는 백그라운드 job 계약을 만들지 않는다.

### 3.2 Playwright 감지 분기

```bash
if python3 -c "import playwright" 2>/dev/null; then
  MODE=playwright
else
  MODE=grep-only
fi
```

| 모드 | 검증 항목 |
|------|-----------|
| `playwright` | grep 6쿼터 + hero 스크린샷 + 스크린샷 diff + 콘솔 오류 + `body` hex 추출 후 §18 재검 |
| `grep-only` | `§18 DON'T hex/weight/속성` grep 6종 + HTML lint (중복 id, alt 누락) |

### 3.3 검증 결과 보고

위반을 발견하면 **line + 패턴 + 기대값**을 사용자에게 보고한다. 자동 수정은 하지 않는다 —
사용자가 "수정해줘"라고 하면 그때 고친다.

```
⚠️ §18 DON'T 위반:
- line 45: background: #FFFFFF  (design.md §18 "Tesla는 #F4F4F4")
- line 127: color: #000000      (design.md §18 "#1D1D1F 사용")
```

---

## 4. AI Slop Extended — 12 패턴 (회피 목록)

`redesign-aesthetics.md` §2의 6개 + Claude Design §Content Guidelines 의 6개를 통합.

### 4.1 일반 슬롭 (design.md 명시 없을 때만 적용)

1. **공격적 그라디언트 배경** — `linear-gradient(135deg, #667eea, #764ba2)` 류 금지.
   대안: dominant 1색 + sharp accent 1색 (8:2).
2. **이모지 남용** — 브랜드가 이모지를 쓰지 않는다면 placeholder로 교체.
3. **라운드 모서리 + 왼쪽 border-accent 카드** — AI 생성 노트 앱 시그니처.
4. **SVG로 그린 일러스트** — 직접 그리지 말고 placeholder + 실소재 요청.
5. **범용 폰트 남발** — Inter / Roboto / Arial / Fraunces / system-ui 단독 금지.
6. **정보 슬롭** — 빈칸 채우려고 의미 없는 숫자/아이콘/통계 넣기 금지.
   *One thousand no's for every yes.*

### 4.2 구조적 슬롭 (`redesign-aesthetics.md` §2 압축)

7. **보라 그라디언트** — `135deg, #667eea → #764ba2` 대표적 AI 스타일.
8. **균등 분산 6-8색 팔레트** — 무지개 생일카드 느낌.
9. **12-column grid 균등 카드 분포** — "Hero + Feature 3카드 + CTA" 천편일률.
10. **중앙 정렬 텍스트 + 그 아래 버튼** — AI 히어로 안티패턴.
11. **모든 버튼 동일 radius/padding/hover** — 시그니처 컴포넌트 부재.
12. **평범한 footer (회사명 + 링크 + 소셜)** — 시그니처 없이 채우기.

### 4.3 예외 규칙 — hard constraint 우선

**design.md가 명시한 것**은 AI Slop 목록을 무시하고 그대로 따른다.
예: design.md §04에 `Inter` 명시 → "범용 폰트 남발" 규칙 무시.
예: design.md §11에 12-column grid 명시 → "균등 분산 금지" 규칙 무시.

AI Slop 목록은 **design.md 비명시 영역**에서만 작동한다.

---

## 5. Starter Components 인덱스

매체별 HTML 프리셋은 다음 경로 하위에 있다. `insane-build` Step 2에서 매체(medium)에 따라
해당 프리셋을 로드한다.

```
$PLUGIN_ROOT/skills/insane-design/shared/starter-components/
├── web/              # 랜딩·마케팅 페이지 (기본)
│   ├── hero.html
│   ├── nav.html
│   ├── section.html
│   └── footer.html
├── slide/            # 16:9 프레젠테이션 덱 (9:16 세로는 의도적으로 제외)
│   ├── deck-16x9.html
│   └── speaker-notes.md
├── design-system/    # 토큰 시각화 + 컴포넌트 카탈로그
│   └── catalog.html
├── card-news/        # 카드뉴스 (Instagram 1:1, 4:5, KakaoTalk OG)
│   ├── instagram-1x1.html
│   ├── instagram-4x5.html
│   └── kakao-og-safezone.html
└── motion/           # Lottie/Rive 스텁 (실행은 후속 버전)
    └── index.md
```

**매체별 기본값**:
| medium | 기본 파일 |
|--------|----------|
| `web` | `web/hero.html` + `web/nav.html` + `web/section.html` + `web/footer.html` |
| `slide` | `slide/deck-16x9.html` |
| `design-system` | `design-system/catalog.html` |
| `card-news` | `card-news/instagram-1x1.html` |
| `motion` | `motion/index.md` (스텁 안내만 출력) |

---

## 6. 표기 규약 (반드시 통일)

| 올바른 표기 | 잘못된 표기 | 이유 |
|------------|-------------|------|
| `schema_version: 3.2` | `schema_version: 2.0` / `3.1` | v3.2가 active. 3.1은 deprecated |
| `$PLUGIN_ROOT` | `${CLAUDE_PLUGIN_ROOT}` | Codex 변수명 |
| `shared/questioning-policy.md §A` 번호 블록 | `AskUserQuestion` 카드 | Codex에 카드 UI 없음 |
| 동기 grep 검증 (같은 턴) | `Task(run_in_background)` 비동기 verifier | Codex에 백그라운드 Task 포크 계약 없음 |
| `localStorage + URL hash + 재생성` | `localStorage + postMessage` | postMessage는 호스트 보장 X |
| `medium: web` (기본값) | `format: website` / `type: landing` | 계약 필드명 고정 |
