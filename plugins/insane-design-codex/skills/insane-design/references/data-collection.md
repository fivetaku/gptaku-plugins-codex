# Data Collection — 다층 fallback 전략

> URL 하나 들어왔을 때, 어떤 사이트든 실제 CSS/HTML/스크린샷을 확보하기 위한 전략.
> insane-search 프로젝트의 우회 기법을 참고해 5단계 계층 구성.

---

## 0. 왜 고도화가 필요한가

현재 `fetch_all.py` 는 단순 `curl + Chrome UA` 만 씀. 실제로 부딪힌 문제:

| 실패 케이스 | 원인 | 영향 |
|---|---|---|
| **planetfall** | CDN 실패 (`curl exit 56`) | 8개 서비스 중 1개 fetch 못함 |
| **Vercel homepage** | 5KB 빈 SSR HTML (실제는 JS 렌더링) | 컴포넌트 클래스 추출 불가 |
| **Cloudflare bot fight mode** | TLS 핑거프린트 검사 | 단순 curl 차단 |
| **iframe 기반 사이트** | HTML 에 실제 콘텐츠 없음 | CSS 링크만 있고 클래스 없음 |
| **Edge case: SPA 초기 HTML** | `<div id="root"></div>` 뿐 | 토큰 추출 불가 |

이 문서는 5단계 fallback 체인을 제안합니다. 각 단계마다 **성공 조건**과 **다음 단계 트리거 조건**이 명확합니다.

---

## 1. Fallback 체인 (5 tiers)

```
┌─────────────────────────────────────────┐
│ Tier 1: 기본 curl + Chrome UA            │  ← 기존 방식, 80% 사이트 커버
│   ↓ 실패 시                              │
│ Tier 2: Mobile UA + Referer + gzip       │  ← 모바일 차별 없는 사이트 우회
│   ↓ 실패 시                              │
│ Tier 3: Jina Reader (r.jina.ai)          │  ← JS SPA + 실제 브라우저 렌더링
│   ↓ 실패 시                              │
│ Tier 4: curl_cffi chrome124 impersonate  │  ← TLS fingerprint 우회 (Cloudflare)
│   ↓ 실패 시                              │
│ Tier 5: Playwright headless Chrome       │  ← 최후 수단, 모든 JS 실행
└─────────────────────────────────────────┘
```

각 tier 성공 시 **수집 품질 점수**를 메타데이터에 기록:

| Tier | Quality | 설명 |
|---|---|---|
| 1 | `direct` | 정본 HTML, 100% 신뢰 |
| 2 | `mobile-direct` | 모바일 뷰 본문. HTML 구조 조금 다를 수 있음 |
| 3 | `jina-markdown` | Jina Reader 가 마크다운으로 변환. CSS 링크 일부 손실 가능 |
| 4 | `curl_cffi-direct` | TLS 우회, 정본과 동일 |
| 5 | `playwright-rendered` | JS 실행 후 DOM. 실제 runtime 값 (SPA 에 유리) |

---

## 2. Tier 1: 기본 curl + Chrome UA

```bash
curl -sL \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.9,ko;q=0.8" \
  -H "Accept-Encoding: gzip, deflate, br" \
  --compressed \
  --max-time 30 \
  -o index.html \
  "$URL"
```

### 성공 조건
- HTTP 2xx
- HTML 크기 ≥ 5KB
- `<html>` / `<body>` 태그 존재

### 실패 트리거 (Tier 2 로 진행)
- HTTP 403 / 429 / 5xx
- HTML 크기 < 5KB
- `exit 56` (CDN connection reset)
- Cloudflare challenge page 감지 (`Just a moment...`, `cf-chl-bypass`)

---

## 3. Tier 2: Mobile UA + Referer

```bash
curl -sL \
  -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: ko-KR,ko;q=0.9,en;q=0.8" \
  -H "Referer: https://www.google.com/" \
  -H "Accept-Encoding: gzip, deflate, br" \
  --compressed \
  --max-time 30 \
  -o index.html \
  "$URL"
```

### 왜 효과적인가
- 모바일 트래픽 차별 없는 사이트 (Naver 블로그, 일부 CMS)
- Google Referer 로 검색 유입 시뮬레이션
- 일부 bot detection 이 desktop UA 에만 트리거됨

### 실패 트리거 (Tier 3 로 진행)
- 여전히 403 / 429
- SPA 빈 껍질 (`<div id="__next"></div>` 정도만)
- HTML < 5KB

---

## 4. Tier 3: Jina Reader (r.jina.ai)

> **핵심 무기**. Puppeteer 실제 브라우저로 JS 렌더링 후 마크다운 + 메타데이터 반환. API 키 없음. 분당 500 RPM 무료.

### 4.1 기본 사용 (마크다운)

```bash
curl -sL "https://r.jina.ai/$URL"
```

### 4.2 JSON 구조화 출력 (권장)

```bash
curl -sL -H "Accept: application/json" "https://r.jina.ai/$URL"
```

반환 예시:
```json
{
  "data": {
    "title": "Stripe | Financial Infrastructure",
    "description": "...",
    "url": "https://stripe.com",
    "content": "# Financial infrastructure...\n...",
    "metadata": {
      "ogImage": "https://stripe.com/og.png",
      "twitterCard": "summary_large_image"
    },
    "external": {
      "alternate": [
        { "href": "https://stripe.com/feed", "title": "RSS" }
      ]
    },
    "usage": { "tokens": 1234 }
  }
}
```

### 4.3 스크린샷 (Bonus)

```bash
curl -sL -H "X-Respond-With: screenshot" "https://r.jina.ai/$URL"
# → GCS 서명 URL 반환 (4시간 유효)
```

이걸로 스크린샷도 동시에 확보 가능. Playwright 없이도.

### 4.4 한계
- Jina Reader 는 HTML → 마크다운 변환이라 **원본 CSS 링크는 손실**
- 우리가 CSS 파싱을 해야 하므로 Jina 만으로는 불완전
- **대응**: Jina 로 먼저 HTML 형태의 본문 + og 메타데이터 확보 후, 원본 CSS 링크가 있는지 확인. 원본 CSS 링크가 Jina 응답에 있으면 그걸로 Tier 1 재시도.

### 4.5 HTML 모드 (원본 CSS 링크 보존)

```bash
curl -sL -H "X-Return-Format: html" "https://r.jina.ai/$URL"
```

이 모드면 원본 HTML을 돌려줌. Jina 가 Puppeteer 로 받은 fully-rendered HTML → 우리 파이프라인에 그대로 투입 가능.

---

## 5. Tier 4: curl_cffi (TLS 핑거프린트 우회)

```python
# pip install curl_cffi
from curl_cffi import requests

response = requests.get(
    url,
    impersonate="chrome124",  # 또는 "chrome120", "safari17_0"
    timeout=30,
)
html = response.text
```

### 언제 쓰는가
- Cloudflare Bot Fight Mode
- Akamai / Imperva / Datadome WAF
- 일반 curl 은 TLS ClientHello 가 "Python user-agent" 처럼 보여서 차단당함
- curl_cffi 는 실제 Chrome 의 TLS ClientHello 를 복제함

### 주의
- Python 의존성 추가 필요 (`pip install curl_cffi`)
- 일부 사이트는 이마저도 차단 (Quora, Facebook 등)

---

## 6. Tier 5: Playwright Headless Chrome

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; ...) Chrome/120.0.0.0",
        viewport={"width": 1280, "height": 800},
        locale="en-US",
    )
    page = context.new_page()
    page.goto(url, wait_until="networkidle", timeout=60000)
    
    # 1. HTML 저장
    html = page.content()
    
    # 2. 스크린샷 (fullpage + hero viewport)
    page.screenshot(path="fullpage.png", full_page=True)
    page.screenshot(path="hero.png")  # viewport only
    
    # 3. computed styles 추출 (보너스 — 실제 runtime 값)
    brand_element = page.query_selector("button[class*='primary']")
    if brand_element:
        computed = brand_element.evaluate("el => getComputedStyle(el).backgroundColor")
    
    browser.close()
```

### 언제 쓰는가
- Tier 1~4 가 전부 실패
- JS 기반 SPA 가 확실 (첫 HTML 에 콘텐츠 없음)
- **computed styles** 가 필요한 경우 (런타임 값 vs CSS 변수의 차이)

### 추가 이점
- 실제 **computed CSS** 를 뽑을 수 있음 (var() 해결 후 최종 hex 값)
- getBoundingClientRect 로 **실제 간격** 측정 가능
- dark mode 토글 자동화 (`color_scheme: "dark"`)

### 단점
- 느림 (10~30초/사이트)
- Playwright 설치 필요 (`pip install playwright && playwright install chromium`)

---

## 7. 단계별 자동 fallback 로직

```python
# scripts/fetch_site.py (의사 코드)

def fetch_site(url: str, slug: str) -> dict:
    out_dir = Path(f"designmd-data/real/{slug}")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    report = {"slug": slug, "url": url, "tier": None, "quality": None, "errors": []}
    
    # === Tier 1: curl Chrome ===
    try:
        html = _curl_chrome(url)
        if _is_valid(html):
            (out_dir / "index.html").write_text(html)
            report["tier"] = 1
            report["quality"] = "direct"
            _extract_css_links_and_download(html, url, out_dir / "css")
            return report
    except Exception as e:
        report["errors"].append(f"tier1: {e}")
    
    # === Tier 2: curl Mobile ===
    try:
        html = _curl_mobile(url)
        if _is_valid(html):
            (out_dir / "index.html").write_text(html)
            report["tier"] = 2
            report["quality"] = "mobile-direct"
            _extract_css_links_and_download(html, url, out_dir / "css")
            return report
    except Exception as e:
        report["errors"].append(f"tier2: {e}")
    
    # === Tier 3: Jina Reader ===
    try:
        # 먼저 HTML mode 시도 (원본 CSS 링크 보존)
        html = _jina_html_mode(url)
        if _is_valid(html):
            (out_dir / "index.html").write_text(html)
            report["tier"] = 3
            report["quality"] = "jina-html"
            _extract_css_links_and_download(html, url, out_dir / "css")
            return report
    except Exception as e:
        report["errors"].append(f"tier3: {e}")
    
    # === Tier 4: curl_cffi ===
    try:
        html = _curl_cffi(url)
        if _is_valid(html):
            (out_dir / "index.html").write_text(html)
            report["tier"] = 4
            report["quality"] = "curl_cffi-direct"
            _extract_css_links_and_download(html, url, out_dir / "css")
            return report
    except Exception as e:
        report["errors"].append(f"tier4: {e}")
    
    # === Tier 5: Playwright ===
    try:
        html, screenshots = _playwright_render(url)
        (out_dir / "index.html").write_text(html)
        (out_dir / "screenshots").mkdir(exist_ok=True)
        for name, png in screenshots.items():
            (out_dir / "screenshots" / name).write_bytes(png)
        report["tier"] = 5
        report["quality"] = "playwright-rendered"
        _extract_css_links_and_download(html, url, out_dir / "css")
        return report
    except Exception as e:
        report["errors"].append(f"tier5: {e}")
        report["tier"] = "FAILED"
        return report


def _is_valid(html: str) -> bool:
    if not html or len(html) < 5000:
        return False
    # Cloudflare challenge 감지
    if "Just a moment..." in html or "cf-chl-bypass" in html:
        return False
    # 빈 SPA 감지
    body_content = _extract_body_text(html)
    if len(body_content) < 500:
        return False
    return True
```

---

## 8. Screenshot 통합 전략

사용자 요청: **"페이지의 이미지 캡쳐도 자료로 넣고 싶어"**

### 8.1 언제 캡처?
모든 서비스에 대해 **기본으로** 스크린샷 확보. 데이터 수집 단계에 통합.

### 8.2 3가지 소스

| 소스 | 언제 | 품질 |
|---|---|---|
| **Jina Reader screenshot API** | Tier 3 에서 자동 확보 | 1280×800, GCS 4시간 |
| **Playwright** | Tier 5 에서 자동 확보 | fullpage + hero, 영구 저장 |
| **별도 Playwright 호출** | 필요 시 수동 | light/dark 모드 각각 |

### 8.3 저장 경로

```
designmd-data/real/{slug}/screenshots/
├── hero-light.png        1280×800 (viewport)
├── hero-dark.png         1280×800 (prefers-color-scheme: dark)
├── fullpage-light.png    1280×N (full page)
└── fullpage-dark.png     1280×N (full page)
```

### 8.4 리포트 HTML 에 삽입

`report.ko.html` 의 hero 섹션에 스크린샷 표시:

```html
<section id="hero">
  <div class="hero-screenshot">
    <img src="screenshots/hero-light.png" alt="{Service} 홈페이지 스크린샷" loading="lazy" />
  </div>
  <h1>{Service} — 디자인 시스템 리포트</h1>
  ...
</section>
```

또는 별도 섹션:
```html
<section id="visual">
  <h2>실제 사이트 미리보기</h2>
  <div class="screenshot-grid">
    <figure>
      <img src="screenshots/hero-light.png" />
      <figcaption>Hero viewport (light)</figcaption>
    </figure>
    <figure>
      <img src="screenshots/fullpage-light.png" />
      <figcaption>Full page</figcaption>
    </figure>
  </div>
</section>
```

### 8.5 DESIGN.claude.manual.md 에도 삽입

```markdown
## 02. Provenance

| | |
|---|---|
| Source URL | `https://stripe.com` |
| Fetched | 2026-04-12 |
| Tier | 1 (direct) |
| Screenshot | `screenshots/hero-light.png` |
| HTML size | 574,643 bytes |
| CSS files | 7개 외부, 총 425,918자 |
```

---

## 9. 스크립트화 가능 항목 (감사 결과)

### 9.1 이미 만들어진 스크립트 (재사용)

`designmd-data/scripts/`:

| 파일 | 기능 | 상태 | 재사용 |
|---|---|---|---|
| `brand_candidates.py` | Brand hex 후보 추출 | ✓ 동작 | Phase 2 그대로 |
| `var_resolver.py` | var() 체인 해결 | ✓ 동작 | Phase 2 그대로 |
| `typo_extractor.py` | 타이포 스케일 추출 | ✓ 동작 | Phase 2 그대로 |
| `alias_layer.py` | util/action/component tier 분류 | ✓ 동작 | Phase 2 그대로 |
| `capture_screenshots.py` | Playwright 스크린샷 | ✓ 동작 | Phase 1 통합 |
| `merge_design_md.py` | Phase1+2 머지 → DESIGN.md | △ hybrid 실험용 | 참고만 (manual 우선) |

### 9.2 새로 만들어야 할 스크립트 (우선순위)

#### 🔴 필수 (스킬 빌드 시 즉시 필요)

| 파일 | 기능 | 난이도 | 예상 시간 |
|---|---|---|---|
| **`fetch_site.py`** | 5-tier fallback fetch | 중 | 2시간 |
| **`parse_tokens.py`** | 모든 토큰 한 번에 파싱 (custom props, fonts, hex, typo, spacing, radius, shadow, classes) | 중 | 2시간 |
| **`generate_report_html.py`** | DESIGN.md → `report.ko.html` HTML 렌더링 | 높 | 4시간 |

#### 🟡 권장 (품질 향상)

| 파일 | 기능 | 난이도 | 예상 시간 |
|---|---|---|---|
| `detect_theme.py` | light/dark 자동 판정 (luminance + 스크린샷) | 중 | 1시간 |
| `detect_framework.py` | Next.js / Framer / Webflow / Tailwind v4 시그너처 감지 | 중 | 1.5시간 |
| `brand_color_picker.py` | Selector role + frequency + screenshot 3-way 검증 | 높 | 2시간 |
| `validate_designmd.py` | 생성된 MD 의 hex 가 실제 CSS 에 있는지 grep 검증 | 낮 | 30분 |

#### 🟢 보너스 (있으면 좋은 것)

| 파일 | 기능 | 난이도 |
|---|---|---|
| `extract_motion.py` | transition-duration / easing 토큰 추출 | 중 |
| `extract_breakpoints.py` | `@media (min-width: Xpx)` 값 추출 | 낮 |
| `extract_computed_styles.py` | Playwright 로 runtime computed CSS 추출 | 높 |

### 9.3 스크립트화 불가능한 영역 (AI 필수)

이건 반드시 사람 또는 Claude 가 해야:

- **§01 Quick Start 치트시트** — "가장 치명적인 실수 하나"를 고르는 판단
- **§03 Tech Stack 서술** — framework 이름만 자동, 3-tier 구조 설명은 AI
- **§06 Semantic Alias 해석** — 어떤 alias 를 우선 추천할지 (util-action-bg-solid 가 primary 인가)
- **§09~§11 Motion/Layout 서술** — 수치는 자동, 내러티브는 AI
- **§12 Components 서술** — BEM 클래스 자동 추출, 역할 그룹핑은 AI
- **§13 Content Voice** — 헤드라인 패턴, CTA 규칙 (사이트 둘러보며 수동)
- **§16 DO/DON'T** — 서비스 고유의 실수 포인트 선정

→ 즉 **"값 추출은 스크립트, 해석은 AI"** 원칙 유지.

---

## 10. 통합 워크플로우 (업데이트 버전)

```
┌────────────────────────────────────────────────────────┐
│ Input: URL, slug                                        │
└──────────────────┬─────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────┐
│ Phase 1: Data Collection (자동)                         │
│   - fetch_site.py (5-tier fallback)                    │
│     → index.html, css/*.css, screenshots/              │
│   - tier, quality 메타데이터 기록                       │
└──────────────────┬─────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────┐
│ Phase 2: Token Extraction (자동)                        │
│   - parse_tokens.py                                     │
│     → tokens.json (색상, 폰트, 타이포, spacing, ...)    │
│   - var_resolver.py → resolved_tokens.json             │
│   - brand_candidates.py → brand 후보                    │
│   - detect_theme.py → light/dark/mixed                 │
│   - detect_framework.py → Next.js/Framer/Webflow       │
└──────────────────┬─────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────┐
│ Phase 3: Visual Verification (멀티모달 AI)              │
│   - Claude 가 screenshots/ + tokens.json 읽기           │
│     → brand color 최종 확정                             │
│     → 폰트 시각적 특성 확인                              │
│     → Hero anatomy 서술                                  │
└──────────────────┬─────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────┐
│ Phase 4: DESIGN.claude.manual.md 작성 (AI)              │
│   - 템플릿 v2.0 기반 16 섹션                             │
│   - validate_designmd.py 로 hex 실존 자동 검증           │
└──────────────────┬─────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────┐
│ Phase 5: HTML Report Generation                         │
│   - generate_report_html.py                             │
│     → DESIGN.md + 스크린샷 → report.ko.html             │
│   - screenshots 를 hero 섹션에 삽입                      │
└──────────────────┬─────────────────────────────────────┘
                   ▼
┌────────────────────────────────────────────────────────┐
│ Output:                                                  │
│   real/{slug}/                                          │
│   ├── DESIGN.claude.manual.md                           │
│   ├── report.ko.html                                    │
│   ├── screenshots/*.png  ← 신규                         │
│   └── tokens.json         ← 신규 (디버깅용)             │
└────────────────────────────────────────────────────────┘
```

---

## 11. 실제 적용 시나리오

### 시나리오 A: 평범한 Next.js 사이트 (Stripe)
- Tier 1 성공 → 10초 완료

### 시나리오 B: Cloudflare 뒤 사이트 (Quora)
- Tier 1 → 403 → Tier 2 → 403 → Tier 3 (Jina) → 성공 → 30초 완료

### 시나리오 C: SPA (Vercel 초기)
- Tier 1 → 빈 HTML → Tier 2 → 빈 HTML → Tier 3 (Jina) → rendered HTML 성공 → 40초 완료

### 시나리오 D: TLS 핑거프린트 차단 (일부 게임 사이트)
- Tier 1 → 403 → Tier 2 → 403 → Tier 3 → Jina timeout → Tier 4 (curl_cffi) → 성공 → 25초 완료

### 시나리오 E: 모든 우회 실패
- Tier 1~4 전부 실패 → Tier 5 (Playwright) → 성공 → 1분 완료

### 시나리오 F: 완전 실패 (레어)
- 전부 실패 → 에러 로그 + 스킬 중단 또는 사용자에게 보고

---

## 12. 다음 단계

1. ✅ 이 문서 작성 완료
2. 🔜 `scripts/fetch_site.py` 구현 (5-tier fallback)
3. 🔜 `scripts/parse_tokens.py` 구현 (all-in-one 추출)
4. 🔜 `scripts/generate_report_html.py` 구현 (DESIGN.md → HTML)
5. 🔜 기존 34개 서비스에 screenshot 확보 (retro-fit)
6. 🔜 `report.ko.html` 템플릿 업데이트 — hero 에 스크린샷 삽입
7. 🔜 스킬화: `SKILL.md` + references + scripts 통합

---

## 관련 문서
- `/Users/chulrolee/designmd-writer/METHODOLOGY.md` — 분석 5단계
- `/Users/chulrolee/designmd-writer/WORKFLOW.md` — 전체 파이프라인
- `/Users/chulrolee/designmd-writer/DESIGN.claude.template.md` — 템플릿 v2.0
- `/Users/chulrolee/insane-search/skills/insane-search/SKILL.md` — 우회 기법 원본
- `/Users/chulrolee/insane-search/skills/insane-search/references/fallback.md` — Fallback 상세
