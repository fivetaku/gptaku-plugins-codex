---
name: insane-apply
description: Applies an analyzed design.md to an existing project while preserving content. Supports three levels — Lv1 swaps tokens only, Lv2 rewrites styles, Lv3 does a full redesign with BOLD direction commit, Unforgettable signature, and motion level. Includes persona lock-in (expert designer + user as manager), a §18 DON'T grep quota (min 6 calls across color / structure / typo), and an opt-in deeper verifier that runs as a background sub-agent. Pairs with insane-design (analysis) and insane-build. Korean triggers — "디자인 적용해줘", "stripe처럼 만들어줘", "이 스타일로 리디자인", "레이아웃 바꿔줘", "Tesla 느낌으로", "톤앤매너 적용", "그 사이트 스타일로 만들어줘". English triggers — "apply design", "redesign like", "make it feel like", "adopt this style".
---

# Insane Apply

> design.md = 디자인 브리프. 기존 콘텐츠를 유지하면서 구조와 스타일을 재설계한다.

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
Manager가 "극단까지"를 선택하면 100% commit. "절충"을 선택해도 60% commit은 유지한다.
중립으로 후퇴하지 않는다.

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

이 문서는 참고 문서가 아니라 **실행 지시서**다.
slug가 제공되면 즉시 Step 0부터 실행한다.

slug가 없으면 §A 질문 도구로 레퍼런스를 고르게 한다 (추천안 첫 번째, 마지막은 "다른 slug 직접 입력"; 아래 블록은 번호 블록 폴백일 때의 모양):

```
질문: 어떤 사이트의 디자인을 적용할까요?
1. stripe — 보라 브랜드, sohne 폰트, weight 300 — SaaS 대표
2. apple — 모노크롬, SF Pro, 미니멀 — 프리미엄
3. toss — Toss Blue, 깔끔한 핀테크 UI
4. nike — Futura/Helvetica, 스포티한 느낌
5. 다른 slug 직접 입력 (examples/ 100+ 코퍼스 또는 insane-design/{slug}/design.md)
```

---

## 상호작용 규칙 (§A)

이 문서의 모든 선택 질문은 `$PLUGIN_ROOT/shared/questioning-policy.md` §A의 질문 도구
(`request_user_input_async`, Plan 모드면 `request_user_input`) 1콜로 묻는다. 두 도구가 모두 없을 때만 채팅 번호 블록으로 폴백한다.
질문 도구를 부른 뒤에는 한 줄 안내만 쓰고 **턴을 끝낸다** — 답은 다음 사용자 메시지로 오며, 그때 다음 Step으로 이어간다.
이 문서 아래의 "EXECUTE" 번호 블록 예시는 폴백일 때의 모양이다. 도구를 쓸 때는 같은 질문·선택지를 도구 인자로 옮긴다.

async 호출 형식: `{"questions":[{"title":"헤더 — 질문","options":["추천안 (추천) — 설명","대안 — 설명"]}]}`. 문항에는 `title`·`options`(문자열 배열)만 넣는다. `question`·`header`·`id`는 Plan 모드 `request_user_input` 전용이라 async에 넣으면 파싱 오류가 난다. "기타·직접 적기" 선택지는 넣지 않는다(자유 입력 칸이 자동으로 붙는다).

- 추천안은 항상 **첫 선택지**(폴백이면 1번). 여러 개 고를 수 있으면 제목에 "(여러 개면 쉼표로)"(폴백이면 "여러 개면 1,3처럼 적어주세요") 안내.
- 폴백의 마지막 선택지는 "문장으로 직접 수정 요청"(Other 대체). 도구에는 "기타"를 넣지 않는다(자유 입력이 자동 추가됨).
- 본진 `preview`는 질문 도구 호출 **직전 채팅 메시지**(폴백이면 선택지 위)에 짧은 예시 블록(코드/변경 요약)으로 먼저 보여준다.
- 추론 가능한 건 묻지 않는다(§1). 사용자가 이미 구체적이면 즉시 진행(§2c).
- 번호 블록과 페르소나는 충돌하지 않는다 — 번호 블록을 쓸 때도 추천안 1번 + 우열 명시. "중립 3옵션 나열" 금지.

---

## 핵심 원칙

1. **콘텐츠는 보존, 디자인만 변경**: 텍스트, 이미지 URL, 링크, 데이터는 그대로 유지
2. **design.md가 디자인 브리프**: §00(분위기) + §11(레이아웃) + §13(컴포넌트) + §15(토큰)이 시공 지시서
3. **CSS Edit가 아니라 코드 재작성**: HTML 구조 + CSS를 design.md 기준으로 다시 쓴다
4. **원본 백업 보장**: 적용 전 git 상태 확인, 롤백 명령어 안내

---

## 워크플로우 — 5 Steps (Step 1.7 / Lv3만 적용)

```
Step 0: 소스 + 프로젝트 분석 (BOLD 방향성 자동 추출)
   ↓
Step 1: 적용 범위 선택 (Lv1/Lv2/Lv3)
   ↓
   ├── Lv1/Lv2 → Step 1.5 (카테고리별 선택)
   └── Lv3    → Step 1.7 (톤앤매너 강도 + Unforgettable + 모션)
   ↓
Step 2: 실행 (Lv3는 Aesthetic 내면화 → 4-Phase 재작성)
   ↓
Step 2.5: 최종 확인 (Lv1/Lv2)
   ↓
Step 3: 검증 (BOLD commit + §18 DON'T + AI Slop 체크)
   ↓
Step 3.5 (optional): 백그라운드 verifier 스폰 — opt-in
   ↓
Step 4: 완료 보고
```

### Step 0: 소스 확인 + 프로젝트 분석

#### 0-1. design.md 찾기

우선순위 순:
1. `$PLUGIN_ROOT/skills/insane-design/examples/{slug}/design.md`
2. `insane-design/{slug}/design.md` (프로젝트 루트)
3. 못 찾으면 → 사용 가능한 slug 목록 출력 후 중단

#### 0-2. design.md에서 디자인 브리프 추출

다음 섹션을 Read:

| 섹션 | 용도 | 추출 내용 |
|------|------|----------|
| §00 Visual Theme | 전체 분위기/철학 + **BOLD 방향성 1단어** | 예: "Industrial Minimalism", "Refined SaaS" |
| §01 Quick Start | 핵심 3가지 | 폰트 + 배경/텍스트 + 브랜드 컬러 |
| §11 Layout Patterns | 구조 설계 | Grid, Hero, Section rhythm, Card, Nav, Content width |
| §12 Responsive | 반응형 전략 | Breakpoints, Touch targets, Collapsing strategy |
| §13 Components | 컴포넌트 패턴 | Button, Card, Input, Nav, Hero 구조 + CSS |
| §14 Content Voice | 카피 톤 | Headline/CTA/Subheading 패턴 |
| §15 Drop-in CSS | 토큰 | CSS 변수 블록 |
| §17 Agent Prompt | 컴포넌트 프롬프트 | 구현 참조 |
| §18 DO/DON'T | **위반 검증 기준** | 전체 DON'T 리스트 (Step 3 검증용) |

#### 0-2-1. BOLD 방향성 추출 (Lv3 전용)

**Lv3 선택 시 필수**: §00 Visual Theme의 첫 문단에서 **1~2 단어**의 BOLD 방향성을 추출.

참조: `$PLUGIN_ROOT/skills/insane-apply/references/redesign-aesthetics.md` 의 §1 BOLD 방향성 Commit 표

예시:
- Stripe → "Refined SaaS"
- Tesla → "Industrial Minimalism"
- Apple → "Monochrome Luxury"
- Discord → "Playful Gradient"

**이 단어는 Lv3 재작성 단계 전체의 기준**이 된다. Step 1.7a에서 사용자가 강도(극단/절충)를 선택.

#### 0-3. 기존 프로젝트 코드 분석

대상 파일을 Read해서 다음을 파악:

1. **콘텐츠 인벤토리** — 보존해야 할 것:
   - 모든 텍스트 (제목, 본문, CTA 문구)
   - 이미지 URL / 파일 경로
   - 링크 (href, 앵커)
   - 메타데이터 (title, description, og 태그)
   - 외부 스크립트/임베드

2. **현재 구조 파악**:
   - 섹션 목록 (hero, projects, about, contact 등)
   - 컴포넌트 종류 (카드, 버튼, 네비, 폼 등)
   - 기술 스택 (Tailwind? CSS modules? inline?)

3. **스캔 결과 출력**:
   ```
   📁 기존 프로젝트 분석:
   - 파일: portfolio.html (34KB, 단일 HTML)
   - 섹션: nav → hero → project×4 → about → contact → footer
   - 컴포넌트: 카드 4개, CTA 버튼 4개, 네비, 연락 폼
   - 콘텐츠: 텍스트 28개, 이미지 8개, 링크 12개

   🎨 디자인 브리프: Tesla (design.md)
   - BOLD 방향성: "Industrial Minimalism"
   - §00: 미니멀, 풀스크린 이미지, 수치 중심
   - §11: 100vh hero, 단일 컬럼, 풀블리드 섹션
   - §13: flat black CTA, 이미지 오버레이 hero
   - §18 핵심 DON'T: 순백 #FFFFFF 사용 금지
   ```

---

### Step 1: 적용 범위 선택

**EXECUTE:** §A 질문 도구를 즉시 호출한다 (preview → 호출 직전 채팅에 변경 범위 요약으로; 아래는 번호 블록 폴백일 때의 모양):

```
변경 범위 미리보기:
  전체 리디자인  ✓ HTML 구조 재설계 ✓ CSS 전면 재작성 ✓ 컴포넌트/레이아웃/토큰   보존: 텍스트·이미지 URL·링크
  스타일만 변경  ✓ CSS 전면 재작성 ✓ 토큰            ✗ HTML 구조 유지           보존: 모든 HTML 구조·콘텐츠
  토큰만 교체    ✓ :root { --brand; --font; --radius } 값만 교체   ✗ CSS 규칙·HTML 유지

질문: 어떤 수준으로 적용할까요?
1. 전체 리디자인 (추천) — HTML 구조 + CSS를 design.md 기준으로 재작성. 콘텐츠(텍스트/이미지/링크)는 그대로 유지. 가장 임팩트 큼.
2. 스타일만 변경 — HTML 구조 유지, CSS만 design.md 기준으로 재작성. 안전·중간.
3. 토큰만 교체 — 기존 CSS 변수 값만 design.md 값으로 교체. 가장 안전.
4. 문장으로 직접 수정 요청
(모르면 1번으로 진행하겠습니다.)
```

- 1 → Lv3 → Step 1.7
- 2 → Lv2 → Step 1.5 (a, b, c)
- 3 → Lv1 → Step 1.5 (a, b)

---

### Step 1.7: 미학 설정 (Lv3 전용)

**Lv1/Lv2 선택 시 이 Step을 건너뛰고 Step 1.5로 진행한다.**
Lv3 전체 리디자인 선택 시 아래 2개의 §A 질문 도구 콜을 순서대로 호출한다(각 콜 뒤에 턴을 끝내고 답을 받는다).

> **🔒 페르소나 재확인 (assertion)**: 이 Step 진입 직전, Identity 블록(상단)을 재인지한다. Step 1.7a/1.7b에서 옵션을 제시할 때도 "사용자 결정"이 아니라 **"expert designer의 추천 + manager의 승인"** 구도를 유지한다. "극단까지" 옵션을 1번에 제시하고 (추천) 태그를 붙인다.

> **참조 필수**: `$PLUGIN_ROOT/skills/insane-apply/references/redesign-aesthetics.md` 를 먼저 Read하여 옵션을 정확히 구성한다.
> **계약 참조**: `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §2 Contract — design.md frontmatter v3.2 필드를 반드시 파싱한다.

#### Step 1.7a: 톤앤매너 강도

Step 0-2-1에서 추출한 BOLD 방향성을 어디까지 밀지 결정.

**EXECUTE:** §A 질문 도구 즉시 호출 (옵션 동적 생성; 아래는 번호 블록 폴백일 때의 모양):

```
예시 프리뷰 (극단까지):
  • {핵심특징1}
  • {핵심특징2}
  • {핵심특징3}
  • 장식 완전 제거 / 극단 대비

질문: {서비스명}의 '{BOLD 방향성}'을 어느 정도까지 밀까요?
1. 극단까지 (추천) — §00 철학 100% 적용. 중간값 없이 끝까지 commit.
2. 적당히 절충 — {서비스명} 느낌 살리되 기존 프로젝트 톤과 균형. 부분 적용, 대비 완화, 일부 기존 요소 유지.
3. 문장으로 직접 수정 요청
```

**옵션 동적 생성 규칙:**
- `{서비스명}` → frontmatter `service_name`
- `{BOLD 방향성}` → Step 0-2-1에서 추출
- `{핵심특징1~3}` → §00 텍스트의 키워드 또는 Key Characteristics 리스트

#### Step 1.7b: Unforgettable 요소 + 모션 레벨

질문 2개를 한 블록에 연속 출력한다 (답은 `1, 2`처럼 질문 순서대로 받는다):

```
질문 1: 이 리디자인에서 가장 기억에 남을 한 가지는?
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

**선택 결과 저장**: 이후 Step 2의 재작성에서 reference로 사용.

---

### Step 1.5: 카테고리별 상세 선택 (Lv2/Lv1만)

**Lv3 전체 리디자인을 선택한 경우 이 Step을 건너뛰고 Step 2로 진행한다.**
Lv2(스타일만) 또는 Lv1(토큰만) 선택 시 아래 §A 질문 도구 콜을 순서대로 호출한다(각 콜 뒤에 턴을 끝내고 답을 받는다).

#### Step 1.5a: 폰트 + 브랜드 컬러

**EXECUTE:** §A 질문 도구 즉시 호출 (preview는 호출 직전 채팅의 코드 블록으로; 아래는 번호 블록 폴백일 때의 모양):

```
예시 프리뷰:
  현재 유지:          body { font-family: "{현재폰트}"; font-weight: {현재weight}; }
  {레퍼런스} 적용:    body { font-family: "{레퍼런스폰트}"; font-weight: {레퍼런스weight}; }
  weight만 변경:      body { font-family: "{현재폰트}"; font-weight: {레퍼런스weight}; }

질문 1: 폰트를 어떻게 할까요?
1. {레퍼런스} 적용 (추천) — {서비스명}의 {레퍼런스폰트}, weight {레퍼런스weight}로 변경
2. 현재 유지 — 지금 쓰고 있는 {현재폰트}, weight {현재weight} 유지
3. weight만 변경 — 현재 폰트 유지, weight만 {레퍼런스weight}로

질문 2: 브랜드 컬러는?
1. {레퍼런스brand} 적용 (추천) — {서비스명}의 브랜드 컬러로 변경 (:root { --brand: {레퍼런스brand}; })
2. 현재 유지 ({현재brand}) — 지금 쓰고 있는 브랜드 컬러 유지
(예: "1, 2" 처럼 두 답을 함께 주세요)
```

**옵션 동적 생성 규칙:**
- `{현재폰트}`, `{현재weight}` → Step 0에서 스캔한 프로젝트 현재 값
- `{레퍼런스폰트}`, `{레퍼런스weight}` → design.md frontmatter 값
- 현재 값을 감지 못했으면 "현재 유지" 대신 "설정 없음 (새로 추가)"로 표시

#### Step 1.5b: 배경톤 + 라디우스 + 그림자

**EXECUTE:** §A 질문 도구 즉시 호출 (다중 선택; 아래는 번호 블록 폴백일 때의 모양):

```
예시 프리뷰:
  :root { --bg: {bg_hex}; --fg: {fg_hex}; }
  :root { --radius-sm: {r_sm}; --radius-md: {r_md}; --radius-lg: {r_lg}; }
  :root { --shadow-sm: {shadow_sm}; --shadow-md: {shadow_md}; }

질문: 배경/텍스트 톤과 모서리, 그림자 중 적용할 것을 골라주세요. (여러 개면 1,3처럼 적어주세요)
1. 배경/텍스트 톤 적용 — {서비스명}의 배경({bg_hex})과 텍스트({fg_hex}) 톤으로 변경
2. 라디우스 적용 — {서비스명}의 모서리 둥글기로 변경 (sm: {r_sm}, md: {r_md})
3. 그림자 적용 — {서비스명}의 그림자 스타일로 변경
4. 모두 현재 유지
```

#### Step 1.5c: 구조 옵션 (Lv2만, Lv1은 건너뜀)

design.md에 §11/§12/§13 중 하나라도 있으면 이 질문을 추가한다.

**EXECUTE:** §A 질문 도구 즉시 호출 (다중 선택; 아래는 번호 블록 폴백일 때의 모양):

```
예시 프리뷰:
  section { padding: {section_padding}; max-width: {max_width}; }  .container { display: {grid_type}; }
  .card { bg: {card_bg}; border: {card_border}; radius: {card_radius}; }  .btn { bg: {btn_bg}; padding: {btn_padding}; }

질문: 구조/레이아웃도 변경할까요? (여러 개면 1,2처럼 적어주세요)
1. 레이아웃 패턴 적용 — {서비스명}의 그리드/섹션 구조로 CSS 변경
2. 컴포넌트 CSS 적용 — {서비스명}의 카드/버튼/네비 CSS로 변경 (HTML 구조 유지)
3. 구조 변경 안 함 — 토큰만 적용, 레이아웃/컴포넌트 CSS는 유지
```

---

### Step 2: 실행

선택된 범위에 따라 실행:

#### 모드 A: 전체 리디자인 (Lv3) — 4-Phase 강화

Step 1.5를 거치지 않고 Step 1.7 답변 기반으로 실행.

**Phase 1: Aesthetic 내면화**

```
1. Read: $PLUGIN_ROOT/skills/insane-apply/references/redesign-aesthetics.md
   - §1 BOLD 방향성 Commit 표
   - §2 AI Slop 안티패턴 (회피 목록)
   - §3 톤앤매너 카탈로그 (12가지 미학별 가이드)
   - §4 모션 가이드
   - §5 Atmosphere 카탈로그
   - §6 코드 복잡도 매칭
   - §7 Unforgettable 시그니처
   - §10 검증 체크리스트

2. 내면화할 네 가지:
   • BOLD 방향성: Step 0-2-1에서 추출 (예: "Industrial Minimalism")
   • 강도: Step 1.7a 답변 (극단까지 / 절충)
   • Unforgettable: Step 1.7b 답변 (Hero 임팩트 / 타이포 대비 / 섹션 전환 / 미니멀 극단)
   • 모션 레벨: Step 1.7b 답변 (Staggered / 정적 / 풀 연출)

3. 이 4가지가 이후 모든 코드 결정의 기준.
```

**Phase 2: 콘텐츠 추출**
- Step 0에서 파악한 텍스트/이미지/링크를 변수로 정리

**Phase 3: 코드 재작성** (Write 도구)

재작성 시 참조 순서:
```
0. redesign-aesthetics.md의 BOLD 방향성/강도/Unforgettable/모션 4가지 commit 유지
1. §00 Visual Theme → 분위기 (방향성과 일치)
2. §11 Layout Patterns → 섹션 구조, 그리드, Hero
3. §13 Components → 버튼/카드/네비/히어로 마크업 + CSS
4. §15 Drop-in CSS → :root { } 토큰 블록
5. §12 Responsive → @media 쿼리
6. §14 Content Voice → CTA 문구 톤 (선택적)
7. §17 Agent Prompt → 컴포넌트별 구체 스펙
```

**재작성 시 체크리스트 (코드 작성 중 반드시 점검):**

```
✓ BOLD 방향성 commit 유지 — 중간값/타협 금지
✓ Unforgettable 요소 코드로 명확히 구현
  - "Hero 임팩트" → 100vh + 드라마틱 배경 + 큰 H1
  - "타이포 대비" → display vs body 10배 이상 차이
  - "섹션 전환" → 섹션마다 배경 톤 drastic 변화
  - "미니멀 극단" → 장식 완전 제거, 색 3개 이내
✓ 모션 레벨 적용
  - "Staggered" → 페이지 로드 fadeInUp + animation-delay 순차
  - "정적" → 모션 코드 추가 안 함
  - "풀 연출" → IntersectionObserver + hover + 페이지 전환
✓ AI Slop 회피 (design.md 명시 영역은 예외)
  - design.md에 폰트 명시 없을 때만 Inter/Arial 금지
  - 보라 그라디언트 자동 추가 금지
  - 평범한 카드 그리드 지양
✓ §18 DON'T 준수
  - 예: Tesla면 #FFFFFF 배경 절대 금지
  - 예: Stripe면 body weight 400 절대 금지
✓ 코드 복잡도 ↔ 미학 매칭
  - 미니멀 미학 → 절제된 CSS (불필요한 transition/animation 금지)
  - 맥시멀 미학 → 풍부한 효과 허용
✓ Atmosphere 추가 (design.md 비명시 + 단색 배경일 때만)
  - Hero 단색 → noise/gradient mesh
  - 섹션 구분 밋밋 → subtle border/shadow
✓ 환각 금지
  - design.md에 없는 hex 값 생성 금지
  - design.md에 없는 토큰명 만들기 금지
```

**Phase 4: 파일 Write**
- 파일 전체를 새 코드로 Write
- `<!-- insane-design: {slug} ({날짜}) -->` 주석 삽입
- 원본 파일 대체

---

#### 모드 B: 스타일만 변경 (Lv2)

Step 1.5a~c에서 선택한 항목만 적용:

1. HTML 구조 유지
2. `<style>` 블록 또는 CSS 파일을 재작성
3. 선택된 토큰(폰트/컬러/라디우스/그림자) 적용
4. 선택된 구조 CSS(레이아웃/컴포넌트) 적용 (Step 1.5c에서 선택한 경우)
5. "현재 유지" 선택된 카테고리는 기존 CSS 값 보존
6. Edit/Write 도구로 CSS 부분만 교체

#### 모드 C: 토큰만 교체 (Lv1)

Step 1.5a~b에서 선택한 항목만 적용:

1. 기존 `:root { }` 또는 `/* insane-design */` 블록 찾기
2. 선택된 토큰만 교체 ("현재 유지"는 건너뜀)
3. Edit 도구로 변수 값만 swap
4. 모든 선택이 "현재 유지"면 파일 수정 없이 "변경 사항 없음" 출력

---

### Step 2.5: 최종 확인 (실행 전)

**EXECUTE:** §A 질문 도구 즉시 호출 (preview = 선택된 변경 사항 전체 요약을 호출 직전 채팅에; 아래는 번호 블록 폴백일 때의 모양):

```
=== 변경 사항 ===
✓ 폰트: Inter 400 → sohne-var 300
✓ 브랜드: #3B82F6 → #533AFD
✗ 배경/텍스트: 현재 유지
✓ 라디우스: 6px → 12px
✗ 그림자: 현재 유지
✓ 레이아웃 패턴: 적용
✗ 컴포넌트 CSS: 현재 유지

수정 파일: {파일 목록}
롤백: git restore {파일}

질문: 이렇게 적용할까요?
1. 적용하기 (추천) — 선택한 내용을 프로젝트에 적용합니다
2. 다시 선택 — Step 1부터 다시 선택합니다
3. 문장으로 직접 수정 요청
```

- "다시 선택" → Step 1로 돌아간다
- preview에는 **선택된 변경 사항을 모두 요약**한다

---

### Step 3: 검증 + 확인

리디자인 완료 후:

1. **콘텐츠 보존 검증**: 기존 텍스트/이미지/링크가 모두 새 코드에 존재하는지 확인
   ```
   ✓ 텍스트 28개 중 28개 보존
   ✓ 이미지 8개 중 8개 보존
   ✓ 링크 12개 중 12개 보존
   ✗ 누락: 없음
   ```

2. **design.md 반영 검증**: 주요 토큰이 적용되었는지 확인
   ```
   ✓ brand_color: #CC0000
   ✓ primary_font: Gotham SSm
   ✓ bg: #F4F4F4
   ✓ Hero: 풀스크린 이미지 오버레이
   ✓ CTA: flat black 버튼
   ```

3. **BOLD 방향성 commit 검증** (Lv3 전용)

   ```
   ✓ BOLD 방향성 ("Industrial Minimalism") 타협 없이 유지됨
   ✓ Unforgettable 요소 ("Hero 임팩트") 코드에 명확히 구현됨
     - hero { height: 100vh } ✓
     - hero h1 { font-size: clamp(60px, 8vw, 120px) } ✓
     - 드라마틱 배경 (그라디언트/이미지/노이즈) ✓
   ✓ 모션 레벨 ("Staggered reveal") 적용됨
     - @keyframes fadeInUp 정의 ✓
     - animation-delay 순차 적용 ✓
   ```

4. **§18 DON'T 위반 검증** (Lv3 전용) — **grep 쿼터 필수**

   design.md §18 DON'T 리스트와 코드를 자동 대조. 최소 grep 호출 쿼터를 충족하지 못하면 Step 3 미통과:
   - **색상 DON'T**: 최소 2회 (배경 + 텍스트)
   - **구조 DON'T**: 최소 2회 (예: body weight, border-radius)
   - **타이포 DON'T**: 최소 2회 (예: 금지 폰트, weight)
   - 총 **최소 6회 grep**. (`$PLUGIN_ROOT/skills/insane-design/shared/README.md` §2.2 계약)

   예시:
   ```
   Tesla §18: "배경을 #FFFFFF 순백으로 두지 말 것"
   → grep 'background:\s*(#fff|#FFFFFF|white)' 코드
   → 발견 시: ❌ 위반! 사용자에게 알림 + 수정 옵션 제공

   Stripe §18: "body weight 400으로 두지 말 것"
   → grep 'body\s*{[^}]*font-weight:\s*400' 코드
   → 발견 시: ❌ 위반!

   Notion §18: "텍스트를 #000 순흑으로 두지 말 것"
   → grep 'color:\s*(#000|#000000|black)' 코드
   → 발견 시: ❌ 위반!
   ```

   위반 발견 시 콘솔 출력:
   ```
   ⚠️ §18 DON'T 위반 발견:
   - background: #FFFFFF (line 45) ← Tesla는 #F4F4F4 사용해야 함
   수정하시겠습니까?
   ```

5. **AI Slop 검증** (Lv3 전용)

   design.md에 명시되지 않은 AI 패턴이 들어갔는지 체크:
   ```
   - design.md frontmatter에 폰트가 없는데 Inter/Arial/Roboto 사용 → 경고
   - design.md에 그라디언트 명시 없는데 'linear-gradient(135deg, #667eea, #764ba2)' 사용 → 경고
   - design.md §11에 정직한 grid가 명시 안 됐는데 12-column grid에 균등 분포 → 경고
   ```

6. **§A 질문 도구로 확인** (아래는 번호 블록 폴백일 때의 모양):

```
질문: 리디자인 결과를 확인해주세요. 브라우저에서 열어보셨나요?
1. 좋아요, 완료 — 리디자인 결과가 만족스럽습니다
2. 수정할 부분 있어요 — 어떤 부분을 바꾸고 싶은지 알려주세요
3. 되돌리기 — git restore로 원래 상태로 돌립니다
```

- "수정할 부분 있어요" → 사용자 피드백 받고 해당 부분만 수정
- "되돌리기" → `git restore {파일}` 실행

---

### Step 3.5: 백그라운드 Verifier 스폰 (optional, opt-in)

Step 3 동기 grep 검증을 통과한 상태에서, 사용자가 **더 깊은 검증**을 원할 때만 실행한다.
자동 실행 금지 — §A 질문 도구로 opt-in 확인 후 스폰.

```
질문: 더 깊은 검증(스크린샷 diff + 콘솔 오류 + a11y)을 백그라운드로 돌릴까요?
1. 아니오, 이대로 완료 (추천) — Step 4로 넘어갑니다
2. 예, 백그라운드 verifier 스폰 — 결과는 "검증 결과 보여줘"라고 하면 회수해 보고합니다
```

> **기본 원칙**: grep-only가 기본. Playwright 설치 감지 시에만 스크린샷 검증 추가.
> 자세한 프로토콜은 `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §3 Verifier Protocol 참조.

**"예" 선택 시** — Codex 런타임 multi-agent로 백그라운드 sub-agent를 스폰한다. 플러그인 스키마에 별도 에이전트
로스터 파일은 없으므로 아래 지침을 스폰 프롬프트에 그대로 넘긴다. 스폰이 불가능한 환경이면 같은 턴에 인라인(동기)으로 수행한다.

```text
spawn_agent({
  agent_type: "reviewer",
  prompt: `
    You are a verifier sub-agent. Do NOT write code.
    1. Read {applied_file_path}
    2. Read {design_md_path} §18 DON'T
    3. For each §18 DON'T hex/weight/property, grep the applied file.
    4. Report violations as JSON: {violations: [{line, pattern, expected}]}
    5. If \`python3 -c "import playwright"\` succeeds (mode=playwright):
       capture hero screenshot, diff against
       $PLUGIN_ROOT/skills/insane-design/examples/{slug}/screenshots/hero-cropped.png.
    6. Return JSON only, no prose.
  `
})
```

**메인 에이전트는 스폰 직후 Step 4 보고로 즉시 진행한다.** 결과를 기다리지 않는다.
결과는 사용자가 **"검증 결과 보여줘" / "verifier 결과"** 라고 명시 요청할 때만 스폰한 에이전트의 결과를 회수해 보고한다
(`shared/README.md` §6 표기 규약). 자동 다음 턴 주입은 하지 않는다.

회수 시 보고 형식:
```
🔍 Verifier 결과:

§18 DON'T 위반 (N건):
  - line 45: background: #FFFFFF (design.md §18 "Tesla는 #F4F4F4")
  - line 127: color: #000000 (design.md §18 "#1D1D1F 사용")

{playwright 모드일 때만}
📸 스크린샷 diff: vs reference ~{유사도}%

수정하려면: "위 위반을 수정해줘" 라고 요청하세요.
```

---

### Step 4: 완료 보고

**Lv3 (전체 리디자인)** 보고 형식:
```
✅ {서비스명} 스타일 전체 리디자인 완료!

🎨 적용된 미학:
  - BOLD 방향성: {방향성 단어} ({극단까지 / 절충})
  - Unforgettable: {Hero 임팩트 / 타이포 대비 / 섹션 전환 / 미니멀 극단}
  - 모션 레벨: {Staggered / 정적 / 풀 연출}

🔄 적용된 디자인:
  - §00: {분위기 한줄 요약}
  - §11: {레이아웃 변경 요약}
  - §13: {컴포넌트 변경 요약}
  - §15: {토큰 요약}

🛡️ 검증 통과:
  ✓ BOLD 방향성 commit 유지
  ✓ §18 DON'T 위반 없음 (grep 쿼터 6회 통과)
  ✓ AI Slop 패턴 없음
  ✓ 콘텐츠 100% 보존

📋 콘텐츠: {N}개 텍스트, {N}개 이미지, {N}개 링크 — 모두 유지
📝 변경 파일: {파일 목록}
↩️ 되돌리기: git restore {파일 목록}
📖 레퍼런스: {design.md 경로}

🔍 더 깊은 검증(스크린샷 diff + 콘솔 오류) 결과가 필요하면:
   "검증 결과 보여줘"
   (Step 3.5에서 스폰한 백그라운드 verifier의 결과를 회수합니다. 스폰하지 않았다면 표시 안 함)
```

**Lv1/Lv2** 보고 형식:
```
✅ {서비스명} {스타일만 / 토큰만} 적용 완료!

📝 변경 파일: {파일 목록}
🔄 적용된 항목: {선택한 카테고리 요약}
📋 콘텐츠 보존: 모두 유지

↩️ 되돌리기: git restore {파일 목록}
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| slug에 해당하는 design.md 없음 | 사용 가능한 slug 목록 출력 후 중단 |
| design.md에 §11/§13 없음 | "스타일만 변경" 모드로 자동 전환 (구조 리디자인 불가) |
| design.md에 §15도 없음 | §01 Quick Start + frontmatter로 최소 토큰 추출 |
| 대상 파일이 너무 큼 (>100KB) | 파일 단위로 분할 처리 제안 |
| 콘텐츠 누락 감지 | 누락 항목 경고 + 수동 확인 요청 |
| uncommitted changes 존재 | 경고 + "계속하시겠습니까?" 확인 |
| 대상이 여러 파일 프로젝트 | 파일별로 처리할지, 전체 한번에 할지 선택 |
| sub-agent 스폰 불가 | Step 3.5를 같은 턴 인라인(동기)으로 수행 — 결과는 동일 |

---

## 적용 레벨 요약

| 레벨 | 변경 범위 | 도구 | design.md 섹션 |
|------|----------|------|---------------|
| **Lv3 전체 리디자인** | HTML + CSS 재작성 | Write | §00 + §11 + §12 + §13 + §15 |
| **Lv2 스타일 변경** | CSS만 재작성 | Write/Edit | §13 + §15 |
| **Lv1 토큰 교체** | CSS 변수 값만 swap | Edit | §15 |

---

## References

| 파일 | 용도 | 사용 Step |
|------|------|----------|
| `$PLUGIN_ROOT/skills/insane-apply/references/apply-workflow.md` | 파싱/스캔/주입 규칙 | Step 0, Step 2 모드 B/C |
| `$PLUGIN_ROOT/skills/insane-apply/references/redesign-aesthetics.md` | 미학 가이드 (BOLD 방향성, AI slop 회피, 톤앤매너 카탈로그, 모션, atmosphere) | Step 1.7, Step 2 모드 A Phase 1, Step 3 검증 |
| `$PLUGIN_ROOT/skills/insane-design/shared/README.md` | 공통 계약 (Identity · Contract · Verifier · AI Slop) | 전체 |
| `$PLUGIN_ROOT/shared/questioning-policy.md` | §A 질문 도구 정책(번호 블록은 폴백) | 모든 선택 질문 |

## Lv별 §A 질문 도구 호출 횟수

| 모드 | §A 질문 도구 호출 |
|------|-------------|
| **Lv1 토큰만** | 3회: Step 1(범위) + Step 1.5a(폰트/브랜드) + Step 1.5b(톤/Shape) + Step 2.5(확인) |
| **Lv2 스타일만** | 4회: Step 1 + 1.5a + 1.5b + 1.5c(구조) + Step 2.5 |
| **Lv3 전체 리디자인** | 4회 (+ Step 3.5 opt-in 1회): Step 1(범위) + Step 1.7a(톤앤매너 강도) + Step 1.7b(Unforgettable + 모션) + Step 3(결과 확인) / Step 3.5는 사용자가 "더 깊은 검증"을 원할 때만 추가 |
