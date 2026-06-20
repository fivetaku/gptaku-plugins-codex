# DesignMD Analysis Methodology
## Stripe 케이스스터디 기준 — 수작업 분석 방법론

> 이 문서는 `real/stripe/report.ko.html` 같은 디자인 시스템 리포트를 만들기 위해
> 어떤 순서로, 무엇을, 어떻게 분석했는지 기록한 방법론입니다.
> 다른 35개 서비스에 적용할 때의 기준이 됩니다.

---

## 전체 흐름

```
1단계: 실제 사이트 데이터 수집
       ↓
2단계: CSS 파싱 (결정적 추출)
       ↓
3단계: 스크린샷 + 시각 검증 (멀티모달)
       ↓
4단계: DESIGN.claude.manual.md 작성
       ↓
5단계: HTML 리포트 생성
```

---

## 1단계: 실제 사이트 데이터 수집

### 1.1 HTML 홈페이지 수집
```bash
curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ..." \
  https://stripe.com -o real/stripe/index.html
```
- User-Agent 필수 (bot 차단 우회)
- 결과: 574,643 bytes (Next.js SSR 완전 렌더링)

### 1.2 외부 CSS 파일 수집
```bash
# HTML에서 stylesheet link 추출
grep -oE 'href="[^"]+\.css[^"]*"' index.html

# 병렬 다운로드 (최대 8개 동시)
xargs -n1 -P8 curl -sL -o css/$(basename {}) {}
```
- Stripe: 7개 외부 CSS + 1 인라인 = 8개, 총 425,918자

### 1.3 DesignMD 원본 수집
```bash
curl -sL https://designmd.me/discover/stripe -o raw/stripe.html
# → services/stripe/DESIGN.md (파싱된 마크다운)
# → services/stripe/meta.json (구조화 데이터)
```

---

## 2단계: CSS 파싱 (결정적 추출 — 스크립트)

### 2.1 CSS 커스텀 프로퍼티 전수 파싱
```python
import re
vars_ = re.findall(r'--([a-zA-Z0-9_-]+)\s*:\s*([^;}]+)', all_css)
# → 819개 CSS 변수 발견
```

### 2.2 컬러 램프 그룹핑
- `--hds-color-core-{family}-{step}` 패턴 → family × step 매트릭스
- Stripe에서 발견된 family:
  - brand (15단계), brandDark (15단계)
  - neutral (15단계), neutralDark (14단계)
  - lemon, magenta, orange, ruby (각 4-6단계)
  - error (4단계), success (3단계)

### 2.3 타이포그래피 스케일 추출
- `--hds-font-{category}-{size_label}-{prop}` 패턴
- category: heading, text, input-label, input-text, quote, quoteAttribution
- prop: size, weight, lineHeight, letterSpacing
- → 16개 scale 엔트리

### 2.4 스페이싱 토큰 추출
- `--hds-space-core-{N}` 패턴, 숫자 정렬
- 네이밍 규칙 발견: token number × 0.08 = px (예: core-200 = 16px)
- → 35개 코어 토큰 (0 ~ 2500)

### 2.5 var() 체인 해결
- `util-*` → `core-*` → hex literal 재귀 해결
- 예: `--hds-color-util-action-bg-solid` → `--hds-color-core-brandDark-500` → `#5d64fe`
- 819개 중 733개 terminal hex까지 해결

### 2.6 시멘틱 alias 계층 분류
```
core tier    (--hds-color-core-*)     : raw hex 값
util tier    (--hds-color-util-*)     : semantic alias, core 참조
action tier  (--hds-color-action-*)   : CTA/button 전용
component tier (--hds-space-button-*) : 컴포넌트별 조합
```

### 2.7 폰트 family 추출
- `font-family: ...` 선언 빈도 카운트
- top 5: sohne-var(3), SourceCodePro(1), inherit(1)
- → 주 폰트: sohne-var + SF Pro Display fallback

### 2.8 BEM 클래스 추출 (HTML)
- HTML에서 `class="..."` 속성 값 파싱 + 빈도 카운트
- 상위 25개 패턴 중 의미 있는 것:
  - hds-heading (80), hds-text--md (70), hds-button--primary (13), hds-button--secondary (23)
  - hds-link--callout (16), section-row (22), logo-carousel__item (36)

---

## 3단계: 시각 검증 (멀티모달 분석)

### 3.1 스크린샷 캡처 (Playwright)
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    # light mode
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto("https://stripe.com")
    page.screenshot(full_page=True, path="light-fullpage.png")
    page.screenshot(path="light-hero.png")
    # dark mode
    ctx = browser.new_context(color_scheme="dark")
    ...
```

### 3.2 멀티모달 분석 결정 사항
스크린샷 보고 판단한 것들:

| 판단 항목 | 결정 | 근거 |
|---|---|---|
| Light vs Dark 기본 테마 | **Light** (mixed) | Hero 배경이 #F8FAFD, 상단 섹션은 light |
| 브랜드 컬러 확정 | **#533AFD** | CTA 버튼 색 + 빈도 9위 chromatic |
| Dark/light toggle 여부 | **없음** | light/dark 스크린샷 동일 |
| Hero 구성 | 2-column (텍스트+목업) | 스크린샷 직접 관찰 |
| Mid-page gradient flame | SVG 애니메이션 | CSS로 토큰화 불가 |
| 폰트 시각적 특성 | 매우 얇은 weight | sohne-var 특유의 얇은 기하학적 형태 |

### 3.3 DesignMD 주장 교차검증
```python
css_text = all_css.lower()
for claimed_hex in designmd_hexes:
    count = css_text.count(claimed_hex.lower())
    # count == 0 → 환각 hex
```
- 결과: 13개 주장 중 6개만 실제 CSS에 존재
- #635BFF (DesignMD brand) → **1회만** (우연), 실제는 #533AFD (9회)
- #00D4AA, #DF1B41, #F5A623, #E3E8EE, #C1C9D2, #425466 → **모두 0회**

---

## 4단계: DESIGN.claude.manual.md 작성

### 섹션 구성 (작성 순서)

```
§0  Provenance          — 출처: URL, fetched_at, 방법론
§1  Tech Stack          — 프레임워크, DS 이름, 토큰 tier, 기본 테마
§2  Font Stack          — 실제 폰트명 + fallback chain + weight 경고
§3  Typography Scale    — 16행 테이블 (size/weight/lh/ls)
§4  Colors              — brand ramp 15단계 + brandDark + neutral + accent
§5  Semantic Alias      — util-action-bg-solid → brandDark-500 등
§6  Spacing             — 35개 토큰 (네이밍 규칙 포함)
§7  Radius              — 7단계 + 사용 컨텍스트
§8  Shadow              — dual-layer 패턴 + sm/md/lg 원자
§9  Components          — BEM 클래스 + HTML 마크업 샘플
§10 Drop-in CSS         — :root { } 30줄 copy-paste 블록
§11 Tailwind config     — tailwind.config.js 완성본
§12 DO / DON'T          — DesignMD 오류 교정 + 사용 규칙
§13 Known Limitations   — 캡처 불가 영역 명시
```

### 작성 원칙
1. **모든 값은 실제 CSS에서 — 추론 없음**: `--hds-color-core-brand-600: #533afd` 형태로 토큰명과 hex 쌍으로
2. **출처 명시**: "CSS 변수에서 직접" vs "HTML 관찰" vs "스크린샷 판단" 구분
3. **DesignMD 비교**: 주요 항목마다 DesignMD가 틀린 것 명시
4. **구현 레디**: copy-paste 즉시 사용 가능한 코드 블록 포함

---

## 5단계: HTML 리포트 생성

### 현재 리포트 구조 (`report.ko.html`)
```
Hero         — 서비스 소개 + 데이터 신뢰성 선언
01 Provenance — 출처, 방법론
02 Tech Stack — 프레임워크, DS 이름, 계층 구조
03 Typography — 실제 폰트로 렌더링된 스케일 (live preview)
04 Colors     — 인터랙티브 컬러 램프 (hover → hex 노출)
05 Spacing    — 시각적 막대로 토큰 폭 표현
06 Radius     — 실제 적용된 박스 예시
07 Shadows    — 실제 카드 그림자 데모
08 Components — BEM 클래스 + 실제 마크업
09 Do/Don't   — DesignMD 오류 vs 실제 정답 테이블
```

---

## 현재 데이터 충분성 검토

### ✅ 충분한 것 (리포트로 바로 쓸 수 있음)
- 전체 컬러 토큰 (brand/brandDark/neutral/neutralDark 완전)
- 타이포그래피 스케일 16엔트리 (size/weight/lh/ls 모두)
- 스페이싱 35토큰 (네이밍 규칙 포함)
- Radius 7단계
- Shadow dual-layer 시스템
- BEM 컴포넌트 클래스 (25개)
- 브랜드 컬러 (멀티모달 확인 완료)
- 폰트 스택 + weight 경고
- Drop-in CSS (manual.md §10)

### ⚠️ 부분적 (있지만 개선 필요)
- **Tailwind config**: manual.md에 있지만 accent ramp 불완전
- **Semantic alias 해석**: alias→var→hex 체인 해결됐지만 사람용 설명 부족
- **Spacing 별칭**: `--hds-space-button-height`, `--hds-space-block-stack-gap-*` 같은 의미 있는 composite 토큰 누락
- **컴포넌트 HTML 마크업**: 클래스명은 있지만 실제 HTML 구조 예시 필요

### ❌ 빠진 것 (다음 iteration에서 추가 필요)
1. **모션/인터랙션 토큰** — hover delay, transition-duration, easing 함수
2. **레이아웃 패턴** — section 세로 리듬, max-width, column 그리드
3. **반응형 브레이크포인트** — `@media (min-width: Xpx)` 값들
4. **콘텐츠/카피 보이스** — 헤드라인 길이/패턴, CTA 문구 구조
5. **접근성** — focus 스타일, 최소 폰트 사이즈, 대비비
6. **Quick-start 치트시트** — "5분 안에 Stripe 느낌 내기 3가지"

---

## 다음 서비스 적용 체크리스트

각 서비스 분석 시 확인해야 할 것:

### Phase 1: 수집 (15-20분)
- [ ] 홈페이지 HTML curl 수집
- [ ] 외부 CSS 파일 병렬 다운로드
- [ ] light/dark 스크린샷 2세트
- [ ] DesignMD `services/{slug}/DESIGN.md` 확인

### Phase 2: CSS 파싱 (10분)
- [ ] CSS 커스텀 프로퍼티 전수 추출
- [ ] 컬러 family 감지 + 램프 그룹핑
- [ ] 폰트 family 빈도 카운트
- [ ] 타이포 스케일 (`--*-font-heading-*`) 추출
- [ ] 스페이싱 토큰 (`--*-space-*`) 추출
- [ ] Radius, Shadow 토큰 추출
- [ ] BEM 클래스 빈도 (HTML)

### Phase 3: 시각 검증 (5-10분)
- [ ] light vs dark 판정 (스크린샷)
- [ ] 브랜드 컬러 확정 (CTA 버튼 색 식별)
- [ ] 폰트 시각적 특성 (커스텀 vs 일반)
- [ ] DesignMD 주장 교차검증 (hex substring count)
- [ ] Light/dark 스크린샷 동일 여부 (toggle 여부)

### Phase 4: DESIGN.md 작성 (30-60분)
- [ ] §0 Provenance
- [ ] §1 Tech Stack (framework + DS name + tier)
- [ ] §2 Font Stack + drop-in CSS
- [ ] §3 Typography scale 테이블 (16행)
- [ ] §4 Colors (완전한 ramp + accent families)
- [ ] §5 Semantic alias layer (util→action→component)
- [ ] §6 Spacing + 네이밍 규칙
- [ ] §7 Radius
- [ ] §8 Shadow (dual-layer 여부)
- [ ] §9 Components (BEM + HTML 마크업)
- [ ] §10 Drop-in CSS (:root { } 블록)
- [ ] §11 Tailwind config
- [ ] §12 DO/DON'T (DesignMD 오류 교정 필수)

### Phase 5: 리포트 생성
- [ ] HTML report.ko.html 생성
- [ ] 각 섹션 live 렌더링 확인 (타이포, 컬러 스와치, 스페이싱 막대)
