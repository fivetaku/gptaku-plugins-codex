---
name: insane-build
description: Build a new site, deck, card, or design-system catalog from scratch using a design.md brief (or synthesize one on the fly). Pairs with insane-design (analysis) and insane-apply. Writes deterministic HTML+CSS into insane-build/{session}/variations/v{N}/ honoring §18 DON'T grep, AI-slop guards, and persona lock-in. Defaults to v1 × 1 (single variation) for token economy; v1/v2/v3 variations are opt-in only. Optional deeper verifier runs as a background sub-agent. Korean triggers — "빌드", "만들어줘", "새로 만들어", "처음부터", "랜딩 만들어줘", "덱 만들어줘", "카드뉴스 만들어줘", "insane-build". English triggers — "build", "scaffold", "from scratch", "make a landing", "make a deck", "make a card".
---

# Insane Build

> design.md = 디자인 브리프. 없으면 즉석 합성. 있으면 그대로 시공한다.
> 결과는 `insane-build/{session}/variations/v{N}/index.html`. 기본 v1 × 1.

---

## Identity (페르소나 락인)

```
You are an expert designer. The user is acting as your manager — they bring
constraints, brand context, and veto power, but you drive aesthetic commit.
Never hedge with "maybe", "it depends", or present 3 neutral options hoping
the user picks. Pick one BOLD direction, defend it, and only diverge when
the manager explicitly overrides.
```

**참조**: `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §1 Identity.
Step 1 인터뷰에서 "어떻게 해드릴까요?" 대신 "**이 방향으로 갑니다. 맞으면 진행, 아니면 왜인지 알려주세요.**" 프레임을 유지한다.

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

이 문서는 **실행 지시서**다. 빌드 요청(랜딩 / 덱 / 카드뉴스 / 디자인 시스템 카탈로그)이 들어오면 Step 0부터 즉시 실행한다.

**인자 파싱**:

| 인자 패턴 | 동작 |
|-----------|------|
| 경로 (`./...` 또는 `insane-design/*/design.md`) | 해당 design.md로 빌드 → Step 1 |
| `http://...` 또는 `https://...` | URL 레퍼런스 — Step 0에서 "URL 레퍼런스" 옵션을 기본 선택으로 제시 (사용자 명시 승인 후에만 analysis 선행) |
| `--variations=3` 또는 "v1 v2 v3" 언급 | 3개 variation 생성 (opt-in) |
| (인자 없음) | Step 0 entry 분기 질문부터 |

**URL 자동 analysis 서브호출 금지** — 사용자가 "URL 레퍼런스로 분석 후 빌드" 옵션을 **명시 선택**한 경우에만 analysis 실행.

---

## 상호작용 규칙 (§A)

이 문서의 모든 선택 질문은 `$PLUGIN_ROOT/shared/questioning-policy.md` §A의 질문 도구
(`request_user_input_async`, Plan 모드면 `request_user_input`) 1콜로 묻는다. 두 도구가 모두 없을 때만 채팅 번호 블록으로 폴백한다.
질문 도구를 부른 뒤에는 한 줄 안내만 쓰고 턴을 끝낸다 — 답은 다음 사용자 메시지로 오며, 그때 이어서 진행한다.
추천안은 첫 선택지(폴백이면 1번). 폴백의 마지막은 "문장으로 직접". 추론 가능한 건 묻지 않는다(§1). 추천안 우선 + 우열 명시 — "중립 나열" 금지.
이 문서 아래의 번호 블록 예시는 폴백일 때의 모양이다 — 도구를 쓸 때는 같은 내용을 질문·선택지로 옮긴다.

---

## 계약

| 공유 파일 | 역할 |
|-----------|------|
| `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §1 Identity | 페르소나 락인 |
| `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §2 Contract | frontmatter v3.2 + §18 grep 쿼터 |
| `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §3 Verifier | Step 3.5 백그라운드 sub-agent 프로토콜 |
| `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §4 AI Slop | 12 패턴 회피 목록 |
| `$PLUGIN_ROOT/skills/insane-design/shared/starter-components/` | 매체별 HTML 프리셋 |

진입 시 `$PLUGIN_ROOT/skills/insane-design/shared/README.md`를 먼저 Read한다 (공통 계약).

---

## 워크플로우 — 5 Steps (+ Step 0.5, 3.5 optional)

```
Step 0: entry 분기 — 맨바닥 / design.md 입력 / URL 레퍼런스
   ↓ (§A 질문 도구 1콜)
   ├── 맨바닥  → Step 0.5 (design.md 즉석 합성)
   ├── design.md 경로 → Step 1
   └── URL 레퍼런스 → (명시 승인 시에만) analysis 서브호출 → Step 1
   ↓
Step 1: 프로젝트 컨텍스트 인터뷰 (3질문 — 스코프 / 콘텐츠 시드 / BOLD 강도)
   ↓
Step 1.7: Unforgettable 요소 + 모션 레벨 (apply Step 1.7b 이식)
   ↓
Step 2: variation 생성
   ├── 기본: v1 × 1
   └── 명시 요청 시: v1 극단 / v2 절충 / v3 novel (opt-in)
   ↓
Step 3: 동기 grep 검증 (§18 DON'T + AI slop 12패턴, 쿼터 6회)
   ├── playwright 감지 시 스크린샷 diff 추가
   └── 미감지 시 grep-only
   ↓
Step 3.5 (optional): 백그라운드 verifier 스폰 — opt-in
   ↓
Step 4: 간결 보고 + 브라우저 자동 오픈 + Tweaks 토글 안내
```

---

### Pre-Step 0: 레퍼런스 자동 감지 (필수)

**Step 0 §A 질문 도구를 부르기 전에 반드시 실행한다.**
사용자 발화 / 첨부 파일 경로 / 첫 1~2턴 대화 컨텍스트에서 **slug 후보**를 자동 추출해
`examples/{slug}/design.md` 존재 여부를 확인한다. 이 단계는 질문 없이
스크립트로 처리 — LLM이 임의로 건너뛰지 않도록 Step 0의 **하드 prerequisite**.

#### Pre-Step 0-A. slug 후보 추출 (휴리스틱)

다음 소스에서 소문자 영문 토큰을 추출:
1. **사용자 메시지의 파일 경로/파일명** — 예: `coupang_핸드크림_20260421.md` → `coupang`
2. **브랜드 고유명사** — 사용자 메시지에서 `stripe`, `apple`, `toss`, `coupang`, `linear`, `vercel`, `notion`, `figma` 등 등록된 slug와 일치하는 문자열
3. **기존 `insane-design/{slug}/` 프로젝트 루트 디렉토리** — `insane-design/*/design.md` 글롭 1회 실행
4. **앞선 대화의 analysis 결과** — 직전 턴에 analysis가 돌았으면 그 slug

검출 케이스 구분:
- **정확히 1개**: 해당 slug을 Step 0 기본 추천으로 확정
- **2개 이상**: Step 0 옵션에 모두 나열 (§A 선택)
- **0개**: Step 0 기본 경로로 fallback (맨바닥 합성은 **여전히 마지막 수단**)

#### Pre-Step 0-B. examples/ 전수 스캔 (필수 호출)

```bash
# 반드시 1회 실행 — 스캔 생략하고 Step 0로 가면 안 됨
ls "$PLUGIN_ROOT/skills/insane-design/examples/"*/design.md 2>/dev/null
```

이 스캔 결과를 Step 0 옵션 구성에 사용. 스캔 결과가 수동 지정 slug과 매칭되지 않으면
Step 0에 "수동 경로 입력" 옵션을 유지.

#### Pre-Step 0-C. 콘텐츠 시드 vs 디자인 레퍼런스 분리 명시

**중요 개념 — LLM이 자주 혼동하는 지점**:
- **콘텐츠 시드 (content seed)**: 페이지에 *보여줄* 실제 데이터 (예: `coupang_핸드크림_20260421.md`의 60개 상품 목록)
- **디자인 레퍼런스 (design reference)**: 페이지를 *꾸밀* 방식 (예: `examples/coupang/design.md`의 쿠팡 브랜드 토큰)

**같은 브랜드에서 두 파일이 다른 이름으로 나올 수 있다.** 사용자가 "coupang 상품 데이터"를
제공했다고 해서 "coupang 디자인으로 만들라"는 뜻이 *자명하지는 않지만*, Pre-Step 0의 slug
감지는 "아마도 같은 브랜드 톤"이라는 **기본 추천**을 유도한다. 사용자는 Step 0에서 override 가능.

---

### Step 0: Entry 분기

```bash
WORK_DIR="$(pwd)"
SESSION="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$WORK_DIR/insane-build/$SESSION"
```

**EXECUTE**: Pre-Step 0 결과를 반영하여 §A 질문(질문 도구 1콜, 폴백이면 번호 블록)을 동적 구성한다.

**옵션 동적 구성 규칙** (Pre-Step 0 결과 반영):

| Pre-Step 0 결과 | 1번 옵션 (기본 추천) | 나머지 순서 |
|-----------------|---------------------|-------------|
| slug 1개 매칭 (예: `coupang`) | `{slug} 레퍼런스 사용 (감지됨 — 추천)` | 기존 design.md 경로 수동 / URL 레퍼런스 / 맨바닥 합성 |
| slug 2개 이상 매칭 | `감지된 레퍼런스 중 선택` (sub-choice) | 기존 design.md 경로 수동 / URL 레퍼런스 / 맨바닥 합성 |
| 매칭 0개 | `URL 레퍼런스로 분석 후 빌드 (추천)` | 기존 design.md 경로 수동 / 맨바닥 합성 |

**맨바닥 즉석 합성은 항상 "마지막 수단"으로 표시한다** — 레퍼런스가 있으면 그걸 쓰는 게 품질 상 월등히 낫기 때문 (§18 per-brand contract 정확성, 실제 토큰 기반).

#### 예시: Pre-Step 0이 `coupang` 1개 감지한 경우

```
질문: 어떤 방식으로 빌드할까요?
1. coupang 레퍼런스 사용 (감지됨 — 추천) — examples/coupang/design.md의 실제 쿠팡 토큰(#346AFF brand, Apple SD Gothic Neo, weight 400)을 그대로 계승해 v1을 빌드합니다. 귀하의 콘텐츠 시드와 브랜드 톤이 일치할 때 가장 자연스럽습니다.
2. 다른 분석된 레퍼런스 사용 — examples/ 내 다른 slug (apple, stripe, toss 등) 또는 insane-design/{slug}/design.md 경로를 지정합니다.
3. URL 레퍼런스로 분석 후 빌드 — 먼저 insane-design analysis를 돌려 design.md를 만들고 이어서 빌드합니다. (시간 5~8분 추가)
4. 맨바닥에서 즉석 합성 (마지막 수단) — 레퍼런스 없이 분위기+매체를 질문 1회로 잡고 design.md를 합성합니다. 레퍼런스 없는 경우에만 권장.
5. 문장으로 직접 요청
```

#### 예시: Pre-Step 0이 0개 감지한 경우 (일반 경우)

```
질문: 어떤 방식으로 빌드할까요?
1. URL 레퍼런스로 분석 후 빌드 (추천) — 원하는 스타일의 사이트 URL을 주시면 analysis로 design.md를 만든 뒤 이어서 빌드합니다. 감지된 분석 레퍼런스가 없을 때 가장 품질 높은 경로.
2. 기존 design.md 경로 직접 입력 — 어디든 design.md 파일 경로를 아시면 바로 지정.
3. 맨바닥에서 즉석 합성 (마지막 수단) — 분위기+매체를 질문 1회로 잡고 design.md를 합성합니다. 다른 경로가 불가능할 때만.
4. 문장으로 직접 요청
```

> **자동 analysis 서브호출 금지**: URL이 들어와도 사용자가 "URL 레퍼런스로 분석 후 빌드" 옵션을 **명시적으로** 선택하지 않으면 analysis를 돌리지 않는다. (`shared/README.md` §6 표기 규약)

분기 처리:
- **맨바닥** → Step 0.5 진행
- **기존 design.md** → 경로 입력 요청 → Step 1
- **URL 레퍼런스** → Read `$PLUGIN_ROOT/skills/insane-design/SKILL.md` → analysis 7-Step 실행 → design.md 생성 → Step 1

---

### Step 0.5: 맨바닥 design.md 즉석 합성 (맨바닥 선택 시만)

> **🔒 진입 assertion (필수)**: 이 Step에 들어오기 **직전**에 다음 2개를 자가 확인한다.
> 하나라도 "아니오"면 Step 0으로 복귀해 레퍼런스 경로를 다시 제시한다.
>
> 1. **Pre-Step 0-B의 `examples/*/design.md` 스캔을 실제로 호출했는가?**
>    (호출 흔적이 대화 기록에 없으면 `false`. "이미 알고 있다"로 스킵 금지.)
> 2. **감지된 slug 후보 중 사용자가 명시적으로 "모두 거부"했는가?**
>    (자동 default로 맨바닥을 고르지 말 것. 사용자가 "맨바닥 (마지막 수단)" 옵션을
>    §A 질문에서 직접 선택한 경우에만 이 Step이 valid.)
>
> 두 조건 모두 통과하지 못하면 이 Step 즉시 중단 → Step 0 §A 질문 재호출.
> LLM이 "편의상" 맨바닥을 택하는 패턴을 스킬 단계에서 차단한다 (R5 RCA).

**§A 질문 도구 1콜 압축** — 분위기 + 매체를 같은 콜에서 받는다. 2+3회 피로 누적 금지.

```
질문: 어떤 분위기와 매체로 만들까요?
1. Refined SaaS / Web 랜딩 — Stripe·Linear 톤, 웹 랜딩 페이지 (medium: web)
2. Industrial Minimalism / Web 랜딩 — Tesla·Vercel 톤, 풀블리드 섹션 (medium: web)
3. Monochrome Luxury / Web 랜딩 — Apple·Chanel 톤, 미니멀 (medium: web)
4. Editorial Magazine / Web 랜딩 — Resend·Medium 톤, serif display (medium: web)
5. Refined SaaS / Slide 16:9 — 프레젠테이션 덱 (medium: slide, 9:16 제외)
6. Playful Gradient / Card-news — Instagram 카드뉴스 (medium: card-news)
7. Industrial Minimalism / Design System Catalog — 토큰 + 컴포넌트 카탈로그 (medium: design-system)
8. 문장으로 직접 (다른 분위기/매체)
```

답변을 기반으로 `insane-build/{session}/design.md`를 즉석 합성한다.
참조: `$PLUGIN_ROOT/skills/insane-design/references/template.md` (frontmatter v3.2 전체 필드 채움 — bold_direction, aesthetic_category, medium, medium_confidence 등).

최소 필드만 채우고 §18 DON'T는 선택한 미학의 안티패턴 3개를 기본값으로 주입한다.

---

### Step 1: 프로젝트 컨텍스트 인터뷰 (3질문)

design.md가 확정된 후, 프로젝트 컨텍스트를 파악한다. **3질문만** — 피로 누적 금지. 한 블록에 연속 출력하고 답은 `1, 3, 1`처럼 함께 받는다.

```
질문 1: 스코프는 어느 정도인가요?
1. 풀 랜딩 (4+ 섹션) — nav + hero + features + testimonial + pricing + footer
2. 섹션 2~3개 (랜딩 핵심) — hero + features + CTA
3. 단일 페이지 (1 page) — index.html 하나

질문 2: 콘텐츠 시드를 어떻게 줄까요?
1. 이미 파일/설명 제공함 — 앞선 대화의 컨텍스트를 그대로 사용
2. 직접 입력 — 제목/서브 텍스트/CTA 문구를 다음 턴에 제공
3. 플레이스홀더 사용 — Lorem ipsum 금지 — 매체+미학에 맞는 의미있는 placeholder로 채움

질문 3: BOLD 강도는?
1. 극단까지 (추천) — §00 철학 100% 적용. 중간값 없이 끝까지 commit.
2. 적당히 절충 — 방향성 60% commit. 일부 평이한 값 허용.
(예: "1, 3, 1" 처럼 세 답을 함께 주세요)
```

---

### Step 1.7: Unforgettable 요소 + 모션 레벨

apply SKILL.md Step 1.7b에서 그대로 이식. 동일한 질문 2개(Unforgettable 1개 + 모션 1개)를 한 §A 질문 도구 콜로 묻는다.

#### Signature ↔ Brand 충돌 감지 (Step 1.7 진입 직전 체크)

reference_slug이 있는 경우, design.md frontmatter의 `bold_direction` + `aesthetic_category`와
사용자가 Step 1.7b에서 선택하려는 `signature_element`가 **호환 가능한지** 사전 필터링한다.
충돌하는 시그니처는 §A 옵션에서 **제외**하거나 **⚠️ 경고 마크**를 달아 노출한다.

**충돌 표** (rule-based, 레퍼런스가 있을 때만 적용):

| bold_direction / aesthetic | 호환 signature_element | 비호환 (제외/경고) | 근거 |
|---------------------------|----------------------|-------------------|------|
| Coupang / 유틸리티 커머스 · Naver · 정보 밀도 최우선 | `section_transition`만 | ❌ `hero_impact`, `typo_contrast`, `minimal_extreme` | 거대 히어로/극단 타이포는 정보 밀도 최우선 톤과 충돌 |
| Industrial Minimalism (Tesla, Vercel) | `hero_impact`, `minimal_extreme` | ⚠️ `typo_contrast`, `section_transition` | 미니멀은 드라마틱 대비를 거부 |
| Refined SaaS (Stripe, Linear) | `typo_contrast`, `hero_impact` | ⚠️ `section_transition` | SaaS는 톤 일관성 유지 |
| Monochrome Luxury (Apple, Chanel) | `minimal_extreme`, `hero_impact` | ⚠️ `typo_contrast`, `section_transition` | 럭셔리는 절제를 시그니처로 |
| Editorial Magazine (Resend, Medium) | `typo_contrast` | ⚠️ `minimal_extreme` | 에디토리얼은 타이포 주도 |
| Playful Gradient (Discord, Figma) | `section_transition`, `hero_impact` | ⚠️ `minimal_extreme` | 플레이풀은 장식 허용 |

**충돌 처리 규칙**:
- **비호환 ❌**: §A 선택지에서 **해당 옵션 제거**. 사용자에게 표시조차 하지 않음 (번호를 다시 매긴다).
- **비호환 ⚠️**: 옵션은 유지하되 설명에 `"(⚠️ {brand} 톤과 충돌 — 사용 시 anti-brand 느낌 발생할 수 있음)"` 접미 추가.
- **호환**: 그대로 노출.

감지 결과를 Phase 0 Visual Grounding Pass에 연결 — 스크린샷을 보고도 "정보 밀도 최우선"이 명백한데
사용자가 `hero_impact` 선택 시 **한 번 더 확인**하도록 §A 질문 도구 호출 직전 채팅 메시지(폴백이면 블록 위)에 경고 문장을 삽입.

**맨바닥 합성(Step 0.5 경로)에서는 이 필터 생략.** 합성 design.md가 자기 자신과 호환되므로.

```
질문 1: 이 빌드에서 가장 기억에 남을 한 가지는?
1. Hero 임팩트 — 풀스크린 드라마틱 hero — 100vh, 강한 contrast, 큰 H1
2. 타이포 대비 — 거대 H1 vs 작은 본문의 극단 위계 (10배 이상 차이)
3. 섹션 전환 — 스크롤 따라 drastic 톤/배경 변화
4. 미니멀 극단 — 절제의 미학 — 장식 완전 제거, 색 3개 이내

질문 2: 모션/애니메이션 레벨은?
1. Staggered reveal (추천) — 페이지 로드 시 1회 오케스트레이션, 이후 정적
2. 정적 — 모션 없음. 타이포/레이아웃으로만 임팩트
3. 풀 연출 — 스크롤 트리거 + hover + 페이지 전환
(예: "1, 1" 처럼 두 답을 함께 주세요)
```

> **참조**: `$PLUGIN_ROOT/skills/insane-apply/references/redesign-aesthetics.md` §7 Unforgettable, §4 Motion.

---

### Step 2: Variation 생성

**기본 경로: v1 × 1**. 토큰 경제 우위 유지.

3개 variation을 원한다면 사용자가 **명시**해야 한다:
- 트리거: "variation 3개", "v1 v2 v3", "여러 버전", "explore options", `--variations=3`
- 또는 별도 §A 질문의 "variation count" 선택 (필요 시)

> **⚠️ §18 per-brand 경고**: design.md §18 DON'T는 *해당 브랜드* 재현 기준이다.
> Coupang 레퍼런스로 빌드하면 `#FFFFFF` 배경이 **정답**이고, Tesla 레퍼런스면 `#F4F4F4`가 정답이다.
> 즉석 합성 시 다른 브랜드 §18을 복사 금지. 합성 브랜드의 실제 선택에 근거해 §18을 새로 쓴다.
> 상세: `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §2.2 경고 블록.

#### 2-A. v1 × 1 (기본)

```bash
# 출력 경로
V1="$WORK_DIR/insane-build/$SESSION/variations/v1"
mkdir -p "$V1"
```

#### Phase 0: Visual Grounding Pass (필수)

`design.md`는 요약 문서다. 실제 브랜드 톤·밀도·비율은 요약으로 완전히 표현되지 않는다.
레퍼런스 경로(기존 design.md 사용 옵션)로 진입한 경우, **Step 2-A 본체 진입 전에 다음 4개 자산을 반드시 Read**한다.
그렇게 하지 않으면 타이포 스케일·컨테이너 밀도·accent 역할이 실제 브랜드와 어긋난다.

```
필수 Read (reference_slug이 있을 때 — 경로 base: $PLUGIN_ROOT/skills/insane-design/):
1. examples/{slug}/screenshots/hero-cropped.png  (실측 시각 — 밀도/컴포넌트 크기/배치)
2. examples/{slug}/phase1/typography.json         (실측 폰트 스케일 — design.md 요약보다 정밀)
3. examples/{slug}/phase1/brand_candidates.json   (실측 컬러 빈도·역할)
4. examples/{slug}/phase1/alias_layer.json        (의미 tier: util/action/component/core)
```

**선택 Read** (판단 필요 시):
- `examples/{slug}/index.html` (HTML 구조 샘플, 주요 섹션/컴포넌트 마크업 패턴)
- `examples/{slug}/css/stylesheet_00.css` (가장 큰 CSS 파일, 레이아웃·미디어 쿼리 실측)

**Grounding Assertion** (Phase 0 종료 시점에 자가 점검):
- 실제 히어로 스크린샷을 봤는가? (시각 기반 판단 — "실제 쿠팡은 거대 히어로 타이포 쓰지 않음")
- 실측 typography.json의 주력 폰트 크기(DOM 빈도 최상위)를 파악했는가?
- 실측 brand_candidates의 chromatic 빈도 상위 3개를 확인했는가?

3개 중 하나라도 false면 Step 2-A 본체로 진입하지 말고 Phase 0을 다시 수행.

맨바닥 합성(Step 0.5 경로)에서는 이 Phase 0은 **skip**. (합성 design.md 외에 참조할 실측이 없음.)

1. **Read starter**: `medium` 값에 따라 `$PLUGIN_ROOT/skills/insane-design/shared/starter-components/{medium}/` 하위 기본 파일을 Read.
   - medium=web → `web/nav.html`, `web/hero.html`, `web/section.html`, `web/footer.html`
   - medium=slide → `slide/deck-16x9.html`
   - medium=design-system → `design-system/catalog.html`
   - medium=card-news → `card-news/instagram-1x1.html` (사용자가 4x5 요청 시 교체)
   - medium=motion → `motion/index.md` 안내 출력 후 medium=web으로 폴백

2. **디자인 브리프 주입**: design.md의 §00 + §06 + §11 + §13 + §15를 starter에 매핑
   - CSS 변수(`:root { }`): §15 Drop-in CSS
   - 컴포넌트 마크업: §13 Components
   - 레이아웃: §11 Layout Patterns
   - Hero/섹션 분위기: §00 Visual Theme + BOLD_DIRECTION

3. **콘텐츠 시드 주입**: Step 1의 Content Seed 답변 기반
   - "플레이스홀더" → 미학에 맞는 의미 있는 placeholder (예: Refined SaaS면 "Ship reliable infrastructure")
   - "직접 입력" → 사용자 텍스트
   - "이미 제공" → 앞선 대화 컨텍스트

#### `{TOKEN}` 플레이스홀더 치환 규칙

starter-components의 HTML 파일에는 `{BRAND_NAME}`, `{HEADLINE}`, `{PRIMARY_CTA}` 같은 플레이스홀더가 박혀 있다.
치환 파이프라인:

**Layer 1 — CSS 토큰 (design.md §15 → `:root { }`)**
- starter의 `:root { }` 블록을 design.md §15 Drop-in CSS의 `:root { }` 블록으로 **통째 교체**.
- 변수명은 starter와 design.md가 동일 (`--brand`, `--bg`, `--fg`, `--font-family`, `--radius-md` 등).
- 양쪽 변수명이 다르면 starter 쪽 변수를 유지하고 design.md 값만 매핑.

**Layer 2 — 콘텐츠 플레이스홀더 (`{TOKEN}` → 텍스트)**
- Read starter HTML → 메모리에 로드
- 치환 맵 구성 (Step 1 Content Seed + design.md §14 Copy Voice):
  ```python
  replacements = {
      "{BRAND_NAME}":     service_name,
      "{HEADLINE}":       headline_text,
      "{SUBHEADLINE}":    subhead_text,
      "{PRIMARY_CTA}":    cta_primary,
      "{SECONDARY_CTA}":  cta_secondary,
      "{PRIMARY_HREF}":   "#",
      # ... (모든 `{TOKEN}` 커버)
  }
  ```
- 일괄 치환 (Python `str.replace` 또는 `sed -i`). 미매핑 토큰은 **빈 문자열 대신 의미 있는 기본값**으로 채움 (예: `{YEAR}` → 현재 연도).
- 치환 후 `{` 또는 `}` 남아 있으면 경고: 누락된 토큰이 있다는 뜻.

**Layer 2.5 — 이미지 placeholder 전략 (콘텐츠 시드에 이미지 URL 없을 때)**

이미지가 핵심인 매체(web 커머스 · card-news · design-system 카탈로그)에서 콘텐츠 시드에 이미지 URL이 없으면,
**텍스트만으로 레이아웃을 채우지 말 것.** 이미지 placeholder를 명시 삽입한다.

**규칙**:
1. 콘텐츠 시드(예: 쿠팡 MD) 분석 시 `![`, `<img`, `image:`, `photo:`, `src=` 토큰 개수 카운트
2. 개수가 **0**이고 카드/아이템 수가 **3개 이상**이면 placeholder 모드 활성화
3. placeholder 스타일:
   ```css
   .thumb {
     aspect-ratio: 1 / 1;    /* 커머스 = 1:1, card-news = 매체 비율, design-system = 16:9 */
     background: var(--brand-soft, rgba(99,102,241,0.08));
     border: 1px solid var(--border);
     border-radius: var(--radius-sm, 4px);
     display: flex; align-items: center; justify-content: center;
     color: var(--fg-subtle);
     font-size: 11px;
     font-family: ui-monospace, monospace;
   }
   ```
4. placeholder 내부 텍스트: **단순 치수 표기** (`1080 × 1080`) 또는 **아이템 이니셜 1글자**. Lorem ipsum / 가짜 상품명 절대 금지.
5. `<picture>` 태그로 감싸 향후 실제 이미지 교체를 용이하게:
   ```html
   <picture class="thumb" data-role="placeholder" aria-label="상품 이미지 placeholder">
     <span>{IMAGE_SIZE_TEXT}</span>
   </picture>
   ```

**매체별 기본 비율**:
| medium | aspect-ratio | 사용 |
|--------|--------------|------|
| web (커머스 카드) | 1 / 1 | 상품 썸네일 |
| web (블로그/랜딩) | 16 / 9 | 히어로/섹션 이미지 |
| card-news | 1 / 1 또는 4 / 5 | 카드 내부 |
| design-system | 16 / 9 | 컴포넌트 미리보기 |
| slide | 3 / 2 | 슬라이드 내 이미지 박스 |

**원칙**: 이미지가 없는 상태를 **명시적으로 선언**한다. 숨기지 않는다 — 사용자가 "아 여기 이미지 넣어야 되네"라고 판단할 수 있도록.

**Layer 3 — Unforgettable/모션 주입 (Step 1.7 선택에 따라)**
- "Hero 임팩트" 선택 시 hero.html의 `min-height: 100vh` 유지 + H1 `clamp(48px, 8vw, 120px)` 유지
- "타이포 대비" 선택 시 body font-size를 14px로 축소, H1 font-size를 140px 이상으로 확대
- "섹션 전환" 선택 시 각 `<section>`의 `background`를 번갈아 `var(--bg)` / `var(--brand)` 적용
- "미니멀 극단" 선택 시 모든 `.card` 제거, `<article>`만 plain text로
- "Staggered reveal" 모션 선택 시 `@keyframes fadeInUp` + 각 섹션에 `animation-delay: 0.1s * index`

**치환 실패 시**: 원본 `{TOKEN}`을 유지한 채 Write + 콘솔에 미치환 토큰 리스트 출력. 사용자가 수동 채울 수 있도록.

4. **Write**: `$V1/index.html` (단일 파일, self-contained — nav/hero/section/footer를 하나의 HTML로 합침)

#### 2-B. v1/v2/v3 (opt-in only)

사용자가 명시 요청한 경우:

| Variation | 원칙 | 파일 |
|-----------|------|------|
| v1 — 극단 | BOLD 100%, §00 철학 극단 해석 | `variations/v1/index.html` |
| v2 — 절충 | BOLD 60%, 일부 평이한 값 허용 | `variations/v2/index.html` |
| v3 — novel | BOLD 100% + 구성 변주 (예: hero 좌우 반전, 섹션 순서 변경) | `variations/v3/index.html` |

각 variation은 **같은 design.md, 같은 콘텐츠**를 쓴다. 달라지는 것은 해석 강도/변주만.

---

### Step 3: 동기 grep 검증

생성된 `index.html`에 대해 동기 grep 검증을 실행한다. **grep 쿼터 6회 필수** (`shared/README.md` §2.2).

```bash
ARTIFACT="$V1/index.html"

# 1. §18 DON'T 색상 위반 (최소 2회)
grep -i -E 'background:\s*(#fff|#ffffff|white)' "$ARTIFACT" && echo "⚠️ 순백 배경"
grep -i -E 'color:\s*(#000|#000000|black)' "$ARTIFACT" && echo "⚠️ 순흑 텍스트"

# 2. §18 DON'T 구조 위반 (최소 2회)
grep -i -E 'body[^{]*\{[^}]*font-weight:\s*400' "$ARTIFACT" && echo "⚠️ body weight 400"
grep -i -E 'border-radius:\s*(8px|12px)' "$ARTIFACT"    # 미학이 brutalist일 때만 경고

# 3. §18 DON'T 타이포 위반 (최소 2회)
grep -i -E 'font-family:[^;]*(Inter|Roboto|Arial)[^;]*' "$ARTIFACT" && echo "⚠️ 범용 폰트 (design.md 명시 없을 때만)"
grep -i -E 'font-family:[^;]*system-ui' "$ARTIFACT"

# 4. AI Slop 12 패턴 체크 (`shared/README.md` §4)
grep -i -E 'linear-gradient\(135deg, *#667eea' "$ARTIFACT" && echo "⚠️ 보라 그라디언트"
```

**playwright 감지 분기**:

```bash
if python3 -c "import playwright" 2>/dev/null; then
  # 스크린샷 찍고 hero 영역만 검증 — $V1은 env로 전달 (quoted heredoc 안에서는 확장되지 않음)
  V1="$V1" python3 - <<'PY'
import os
from playwright.sync_api import sync_playwright
v1 = os.environ['V1']
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto(f"file://{v1}/index.html", wait_until='networkidle', timeout=30000)
    page.screenshot(path=f"{v1}/screenshot.png")
    browser.close()
PY
  echo "📸 스크린샷: $V1/screenshot.png"
else
  echo "ℹ️ playwright 미설치 — grep-only 모드로 검증 완료 (정상)"
fi
```

> **playwright 필수 의존 금지.** 미설치 시 grep-only가 정상 경로. (`shared/README.md` §3.2)

**위반 1건 이상 발견 시**: 위반 내용과 line을 사용자에게 보고. 자동 수정은 하지 않는다. (사용자가 "수정해줘" 하면 그때 수정)

---

### Step 3.5: 백그라운드 Verifier 스폰 (optional, opt-in)

Step 3을 통과했을 때 **더 깊은 검증**을 원하면 사용자가 명시 요청해야 한다.

```
질문: 더 깊은 검증을 추가할까요?
1. 아니오, 이대로 완료 (추천) — Step 4로 넘어갑니다
2. 예, 백그라운드 verifier 스폰 — 스크린샷 diff + 콘솔 오류 + a11y 체크. 결과는 "검증 결과 보여줘"라고 하면 회수해 보고합니다
```

**"예" 선택 시** — Codex 런타임 multi-agent로 백그라운드 sub-agent를 스폰한다 (플러그인 스키마에 별도 에이전트
로스터 파일은 없으므로 지침을 스폰 프롬프트에 그대로 넘긴다. 스폰 불가 환경이면 같은 턴에 인라인으로 수행):

```text
spawn_agent({
  agent_type: "reviewer",
  prompt: `
    You are a verifier sub-agent. Do NOT write code.
    Verify $V1/index.html against $WORK_DIR/insane-build/$SESSION/design.md §18 DON'T.
    For each §18 DON'T hex/weight/property, grep the artifact.
    Output JSON only: {violations: [{line, pattern, expected}]}.
    If playwright is installed: capture screenshot + diff against the reference hero screenshot.
  `
})
```

메인은 즉시 Step 4로 진행한다. 결과는 사용자가 **"검증 결과 보여줘"** 라고 명시 요청할 때만 회수한다
(`shared/README.md` §3, §6). **자동 다음 턴 주입 금지**.

---

### Step 4: 간결 보고 + 브라우저 자동 오픈

OS 감지 후 해당 플랫폼의 브라우저 오픈 명령을 사용한다:

```bash
# Cross-platform browser open
case "$(uname -s)" in
  Darwin*)                open "$V1/index.html" ;;
  Linux*)                 xdg-open "$V1/index.html" 2>/dev/null \
                            || sensible-browser "$V1/index.html" 2>/dev/null \
                            || echo "⚠️ 브라우저 자동 오픈 실패 — 수동으로 열기: file://$V1/index.html" ;;
  MINGW*|MSYS*|CYGWIN*)   start "" "$V1/index.html" ;;
  *)                      echo "ℹ️ OS 미인식 — 수동으로 열기: file://$V1/index.html" ;;
esac
```

실패 시 경로만 출력하고 계속 진행 (crash 금지).

**보고 형식**:

```
✅ Build 완료 — {medium} / {BOLD_DIRECTION}

📁 산출물:
  - {session}/variations/v1/index.html
  {v1/v2/v3 모드면 v2, v3도 나열}

🎨 적용:
  - BOLD: {bold_direction} ({극단까지 / 절충})
  - Unforgettable: {Hero 임팩트 / 타이포 대비 / 섹션 전환 / 미니멀 극단}
  - 모션: {Staggered / 정적 / 풀 연출}

🛡️ 검증:
  ✓ §18 DON'T grep 쿼터 6회 통과
  ✓ AI Slop 12 패턴 없음
  {playwright 감지 시: ✓ 스크린샷 캡처}

🪟 브라우저 열림: file://{V1 절대 경로}

🎛️ Tweaks 라이브 토글:
  - 방식: localStorage + URL hash + 재생성 3단 (postMessage 아님 — 호스트 보장 X)
  - 사용: index.html에 주입된 ?tweaks=on URL 파라미터로 패널 오픈
  - 조정한 값을 재생성에 반영하려면: "insane-build {session} --apply-tweaks"
```

---

## 산출물 경로

```
insane-build/{session}/
├── design.md                 ← (맨바닥 선택 시) Step 0.5에서 즉석 합성
├── variations/
│   ├── v1/index.html         ← 기본
│   ├── v2/index.html         ← --variations=3 선택 시만
│   └── v3/index.html         ← --variations=3 선택 시만
└── (playwright 감지 시) variations/v1/screenshot.png
```

---

## Tweaks 라이브 토글 — 3단 조합

`localStorage + URL hash + 재생성`의 3단 조합만 허용. postMessage는 호스트가 보장하지 않는 계약이므로 폐기됨 (`shared/README.md` §6).

1. **localStorage** — 사용자가 슬라이더/토글로 바꾼 값을 브라우저에 저장
2. **URL hash** — `#brand=%23533AFD&fontWeight=300` 형식으로 상태를 공유 가능한 URL에 인코딩
3. **재생성** — "insane-build {session} --apply-tweaks" 요청 시 localStorage+hash 값을 읽어 design.md를 갱신하고 v1을 재빌드

참조: `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §6 표기 규약.

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| design.md가 v3.0 frontmatter (medium 필드 없음) | `medium: web`, `medium_confidence: medium`로 간주 + 경고만 출력. 재생성 강요 금지. |
| URL 레퍼런스 선택했지만 analysis 실패 | 사용자에게 실패 원인 알림 + 맨바닥 경로로 재진입 제안 |
| §18 DON'T 위반 감지 | 위반 내용/line 보고. 자동 수정 금지. "수정해줘" 명시 시에만 수정. |
| playwright 미설치 | 정상 경로. grep-only로 완료. 설치 안내는 *선택적*으로 1줄만. |
| `open` 명령 없는 OS | 경로만 출력하고 사용자가 수동으로 열도록 안내 |
| medium=motion | `motion/index.md` 스텁 안내 출력 후 medium=web으로 폴백 |
| sub-agent 스폰 불가 | Step 3.5를 같은 턴 인라인(동기)으로 수행 — 결과는 동일 |

---

## References

| 파일 | 용도 | 사용 Step |
|------|------|----------|
| `$PLUGIN_ROOT/skills/insane-design/shared/README.md` | 공통 계약 (Identity · Contract · Verifier · AI Slop) | 전체 |
| `$PLUGIN_ROOT/skills/insane-design/shared/starter-components/` | 매체별 HTML 프리셋 | Step 2 |
| `$PLUGIN_ROOT/skills/insane-design/references/template.md` | design.md frontmatter v3.2 스키마 | Step 0.5 |
| `$PLUGIN_ROOT/skills/insane-apply/references/redesign-aesthetics.md` | BOLD 방향성 / AI Slop / Unforgettable / 모션 카탈로그 | Step 1.7, Step 2 |
| `$PLUGIN_ROOT/shared/questioning-policy.md` | §A 질문 도구 정책(번호 블록은 폴백) | 모든 선택 질문 |

## §A 질문 도구 호출 횟수

| 경로 | 호출 |
|------|------|
| **맨바닥 기본** | 4회: Step 0(entry) + Step 0.5(vibe+medium) + Step 1(scope/content/BOLD) + Step 1.7(signature/motion) (+ Step 3.5 opt-in 1회) |
| **기존 design.md** | 3회: Step 0 + Step 1 + Step 1.7 (+ Step 3.5 opt-in) |
| **URL 레퍼런스** | 3~N회: Step 0 + analysis 서브 호출 내부 + Step 1 + Step 1.7 (+ Step 3.5 opt-in) |

v1/v2/v3 모드 선택은 별도 §A 질문 도구 1콜 추가.
