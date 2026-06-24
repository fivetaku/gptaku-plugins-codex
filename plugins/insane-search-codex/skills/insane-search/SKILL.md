---
name: insane-search
description: >
  Auto-bypass for blocked websites — tries every method until one works.
  Use when ordinary fetch returns 402/403/blocked, or when accessing X/Twitter,
  Reddit, YouTube, GitHub, Mastodon, Medium, Substack, Stack Overflow, Threads,
  Naver, Coupang, LinkedIn, or any platform with WAF/bot protection. Leverages
  yt-dlp (1,858 media sites), Jina Reader, public APIs (HN, Bluesky, arXiv), and
  a generic WAF-profile-driven fetch chain (curl_cffi TLS impersonation, mobile
  URL transforms, Playwright real-Chrome) with auto dependency install.
  Korean triggers — 트위터/X 못 열어, 레딧 안 읽혀, 유튜브 자막 뽑아줘, 깃헙 검색,
  사이트 차단됨, 스레드 안 열려, 마스토돈, 미디엄, 서브스택, 스택오버플로우,
  네이버 블로그, 디시인사이드, 에펨코리아, 요즘IT, 긱뉴스, 클리앙, 쿠팡, 링크드인,
  당근마켓. English triggers — twitter access, reddit blocked, youtube subtitles,
  github search, arxiv papers, threads, mastodon, medium, substack, stackoverflow,
  naver blog, dcinside, fmkorea, coupang, linkedin, yozm, wishket.
  Do NOT trigger for simple web searches that web.search_query can handle directly.
---

# Insane Search for Codex

> URL 접근이 차단될 때, **사이트 무관한** 우회 전략을 자동 선택한다.

이 스킬은 인터뷰 대상이 아니다 — 사용자에게 거의 묻지 않고 **바로 실행**한다. 진짜 선택지가
불가피할 때만 `shared/questioning-policy.md` §A 번호형 블록을 쓰되, 준비된 사용자를 과도하게
붙들지 않는다(§2c). 평소엔 차단 감지 → engine 실행 → trace 진단의 결정론적 흐름만 돈다.

## 하네스 규칙 (어시스턴트에게 강제되는 지침)

이 규칙은 어시스턴트가 즉흥 판단으로 엇나가지 못하게 하기 위한 **고삐**다. 위반 시 "200에서 break →
대체 경로 미시도 → Playwright 미설치라 포기" 식의 오판이 재현된다.

**R1 — 일반 웹 URL 차단/403/402 감지 시**:
1. 기본 `web` fetch, 즉흥 curl, 수동 헤더 조합 **시도 금지**
2. 즉시 engine 래퍼를 실행:
   ```bash
   bash scripts/run_engine.sh "<URL>" [--selector "<CSS>"] [--device auto|desktop|mobile] [--trace]
   ```
   (래퍼는 스킬 디렉토리에서 `python3 -m engine`을 호출한다. 직접 호출도 동일:
   `python3 -m engine "<URL>" ...`)
3. 종료코드 0(ok) 또는 1(fail) 받은 뒤 판단. trace를 먼저 읽고 재시도 결정.
4. 실패 시에만 `--trace --json`으로 재호출해서 원인 진단 후 `--device` 또는 `user_hint` 조정.

**R2 — 첫 200에서 탈출 금지**: HTTP 200은 **검사 시작 조건**이지 성공이 아니다. `validate()`의
4-계층 검증을 통과해야 성공 선언. CLI는 이미 강제한다.

**R3 — 편향 금지**: `engine/**`, `waf_profiles.yaml`에 특정 사이트 도메인·셀렉터·브랜드명 하드코딩
금지. `python3 engine/bias_check.py`가 CI 게이트. 자세한 규칙은 **No-Site-Name Rule** 섹션.

**R4 — 힌트는 런타임에만**: 사이트 고유 정보(성공 셀렉터, 우선 Referer)는 CLI 인자 또는
`user_hint`로만 전달, 저장소에 고정 금지.

**R5 — Phase 0 공식 API 우선**: X/Reddit/YouTube/HN/arXiv 등 **공식 공개 엔드포인트**가 있는
플랫폼은 Phase 0 테이블을 먼저 확인하고 해당 API를 쓴다. 이건 편향이 아니라 합의된 접근 경로.

**R6 — 실패 선언은 "전수 시도" 후에만 (engine이 강제하는 실패 게이트)**: engine은 실패 시 `ok=false`와 함께 **아직 안 해본 경로**(`untried_routes`)와 `must_invoke_playwright_mcp` 플래그를 반환한다. 아래가 **모두** 충족되기 전엔 "뚫을 수 없음" 결론 **금지**:
1. `grid_exhausted=true` — false면 `fetch(max_attempts=None)`(=CLI 기본, exhaustive)로 끝까지 재호출.
2. `untried_routes`가 **빈 배열** — 비어있지 않으면 그 경로들을 먼저 실행.
3. `must_invoke_playwright_mcp=false` — true면 **어시스턴트가 직접** 정찰 라우트(`scripts/playwright_recon.js`)를 돌린 뒤에만 통과: Local Node + `channel:'chrome'`로 대상 페이지를 로드 → 발생한 네트워크 요청에서 내부 `/api`·`/graphql`·`.json` 엔드포인트 탐지 → 그 URL을 `bash scripts/run_engine.sh`(= `python3 -m engine`)로 재호출(API는 WAF가 얕음); 또는 렌더된 HTML 회수. (engine은 로컬 Node Chrome만 띄울 수 있으므로, 정찰은 **구조적으로** 어시스턴트의 몫이다 — Codex에는 MCP Playwright가 없으니 `must_invoke_playwright_mcp`는 곧 로컬 정찰 스크립트 호출 신호로 읽는다.)
4. `stop_reason`이 `auth_required`/`404`/paywall 등 **terminal**일 때만 정직하게 실패 인정 — engine이 `untried_routes`를 **빈 채로** 돌려준다. **429(rate-limit)는 terminal 아님** — 백오프 후 재시도/다른 TLS/정찰로 우회.

요지: **engine의 give-up은 "그만해도 된다"는 허가가 아니다.** CLI는 실패 시 `⛔ NOT EXHAUSTED` 블록을 stderr로 출력한다 — 그게 보이면 위 4개를 끝낼 때까지 멈추지 않는다.
단, R7 조건(WAF 조기 감지)이 성립하면 engine 격자는 계속 돌되, 어시스턴트가 **병렬로** 정찰 루트를 시도할 수 있다. 빠른 쪽이 이긴다.

**R7 — WAF 조기 감지 시 API-first 병행 분기** (분기 결정은 자동이지만 사용자가 결과에서 확인 가능
— 어떤 우회 경로로 성공/실패했는지 결과 metadata에 명시):
발동 조건 (AND):
1. engine 실행 초기에 첫 2~3회 attempt가 모두 `verdict=challenge`
2. `profile_used`가 `akamai_bot_manager`, `cloudflare_turnstile`, `datadome_probable`,
   `perimeterx_human`, `f5_big_ip`, `aws_waf` 중 하나로 확정
3. **사용자 요청이 리스트/수집/반복 의도** (여러 페이지, N개 이상, "전부", "크롤링", 페이지네이션
   등). 단건 본문 조회는 해당 없음.

세 조건 모두 참일 때 어시스턴트는 **병렬 경로**를 시작한다:

**"병렬"의 실행 의미** (Codex 도구 호출이 순차이므로 명확화):
- engine은 백그라운드로 띄워둔다 — 격자는 그대로 돌되 블로킹하지 않음
- 그 사이 foreground에서 Playwright 정찰 루트를 진행:
  `node scripts/playwright_recon.js <<'EOF'` / `{"url":"https://example.com","timeout":20000}` / `EOF`
- engine이 먼저 성공해도 좋고, 정찰로 얻은 API가 먼저 성공해도 좋음. 빠른 쪽 결과 채택

**정찰 루트 (`scripts/playwright_recon.js`)**:
1. 대상 페이지를 로드 (Local Node + `channel:'chrome'`)
2. 페이지가 발생시킨 XHR/fetch 네트워크 요청 목록을 수집, `/api/`·`graphql`·`\.json`
   패턴으로 내부 엔드포인트를 자동 필터해 stdout JSON으로 반환
3. 식별된 JSON API URL을 `bash scripts/run_engine.sh <API_URL>`(또는 `python3 -m engine <API_URL>`)로
   재호출. 대부분 API 레이어는 페이지 HTML보다 WAF 보호가 얕아 curl_cffi로 바로 수집됨
4. 응답 스키마 파악 후 pagination / query parameter 조합해 반복 수집

**왜**: SPA + WAF 사이트(쇼핑몰·커머스 다수)는 마케팅 페이지(HTML)만 WAF로 중투자하고 내부 API는
gateway 레벨 기본 방어만 쓰는 경우가 많다. HTML 격자 전수 낭비(50회 × 0.5s + Playwright fallback
40s ≈ 65초)보다 **정찰 1회(5~10초) + API 재호출(0.5초)**가 훨씬 경제적이고 성공률 높음.

**R7을 쓰지 말아야 할 때**: 단일 페이지 본문 읽기만 필요한 단건 조회(문서 하나, 블로그 포스트
하나)는 engine만으로 충분하다 — 발동 조건 #3이 이를 배제한다.

**R7 편향 방지**: 내부 API URL·파라미터는 `engine/**`에 하드코딩 금지. 탐지된 URL은 런타임
호출에만 쓰고 저장소에 고정하지 않는다.

---

이 스킬의 핵심 불변식:

- **단일 진입점**: 일반 웹 페이지는 항상 `bash scripts/run_engine.sh <URL>` (= `python3 -m engine <URL>`)
  또는 `from engine import fetch; fetch(...)`.
- **편향 금지**: `engine/**`, `waf_profiles.yaml`에 특정 사이트 하드코딩 금지.
- **힌트는 런타임에만**: 사이트 고유 정보는 CLI/`user_hint` 경유.

## 의도 분류 (Phase 0 진입 전)

| 사용자 입력 | 경로 |
|------------|------|
| URL 제공 (`https://...`) | → Phase 0 검사 후 없으면 Phase 1 (generic fetch chain) |
| 핸들 제공 (`@username`) | → Phase 0 syndication/API |
| 키워드만 ("X에서 AI 검색") | → `web.search_query`(`site:{domain} {keyword}`) 먼저 → URL 확보 후 재진입 |

> **한국어 신규 콘텐츠 한계**: 네이버/다음/한국 커뮤니티의 키워드 검색은 `web.search_query` 경유가
> 유일하며, 신규 콘텐츠 인덱싱이 지연될 수 있다.

## Phase 0 — 플랫폼 공식 API 인덱스

> 플랫폼이 **공식 공개한** 전용 API/CLI만 여기에 둔다. 이건 편향이 아니라 합의된 엔드포인트 사용이다.

### 소셜/커뮤니티 전용 API

| 플랫폼 | 방법 | 상세 |
|--------|------|------|
| X/Twitter | syndication (타임라인) + tweet-result/oEmbed (개별 트윗) + 키워드 검색: web.search_query → tweet-result | [twitter.md](references/twitter.md) |
| Reddit | Atom/RSS 피드(`.rss`) — 비인증 `.json`은 WAF 차단(403), score·댓글수는 OAuth | [json-api.md](references/json-api.md) |
| Bluesky | AT Protocol (`public.api.bsky.app/xrpc/...`) | [public-api.md](references/public-api.md) |
| Mastodon | 인스턴스별 공개 API | [public-api.md](references/public-api.md) |
| Hacker News | Firebase API + Algolia Search | [json-api.md](references/json-api.md) |
| Stack Overflow | SE API v2.3 | [public-api.md](references/public-api.md) |
| Lobste.rs / V2EX / dev.to | 공개 JSON API | [json-api.md](references/json-api.md) |

### 미디어 (CLI 도구 필수)

| 플랫폼 | 방법 | 상세 |
|--------|------|------|
| YouTube/Vimeo/Twitch/TikTok/SoundCloud 등 1,858개 | `yt-dlp --dump-json` | [media.md](references/media.md) |

### 학술/레지스트리

| 플랫폼 | 방법 | 상세 |
|--------|------|------|
| arXiv | Atom API | [public-api.md](references/public-api.md) |
| CrossRef | REST API | [public-api.md](references/public-api.md) |
| Wikipedia | REST API | [json-api.md](references/json-api.md) |
| OpenLibrary | JSON API | [public-api.md](references/public-api.md) |
| GitHub | gh CLI / REST API | [public-api.md](references/public-api.md) |
| npm / PyPI | Registry API | [json-api.md](references/json-api.md) |
| Wayback Machine | CDX API | [public-api.md](references/public-api.md) |

### 한국 전용 공식 API

| 플랫폼 | 방법 | 상세 |
|--------|------|------|
| 네이버 검색 | `search.naver.com` (통합/블로그/뉴스탭) | [naver.md](references/naver.md) |
| 네이버 금융 시세 | `api.finance.naver.com/siseJson.naver` (비공식 JSON) | [naver.md](references/naver.md) |

**그 외 모든 사이트는 Phase 1(generic fetch chain)이 자동 처리한다.**

## Phase 1 — Generic Fetch Chain

### 단일 진입점

CLI(권장):
```bash
bash scripts/run_engine.sh "https://example.com/path" --selector "article" --device auto --trace
# 동치: python3 -m engine "https://example.com/path" --selector "article" --device auto --trace
```

Python API:
```python
from engine import fetch

result = fetch(
    "https://example.com/path",
    success_selectors=["article", "[class*='product-card']"],  # 포지티브 프루프 (선택)
    device_class="auto",      # "auto" | "desktop" | "mobile"
    user_hint=None,           # {"referer_strategy": "self_root", "impersonate_first": "safari"}
    timeout=25,
)

if result.ok:
    print(result.verdict)     # strong_ok | weak_ok
    html = result.content
else:
    # Phase 3 수동 개입 (Playwright) 필요 — result.trace로 원인 진단
    pass
```

### 내부 단계 (디버깅용 노출)

`fetch()`는 단일 API이지만 내부는 phase로 나뉘어 있다. `result.trace`(또는 `--trace`)에서 각 시도를
확인할 수 있다.

```
probe      — curl_cffi + safari + self-referer로 첫 시도
validate   — 4-계층 검증 (marker / size / cookie / success_selectors)
detect     — WAF 제품 감지 ([(profile_id, confidence)] 랭킹)
plan       — 프로파일의 tls_candidates × url_transforms × referer 격자 구성
execute    — 격자 전수 시도 (첫 200에서 탈출하지 않음)
fallback   — capability 태그 기반 Playwright 라우팅 (정찰 스크립트 or local+chrome)
report     — FetchResult(ok, verdict, profile_used, trace, summary)
```

### 검증 원칙

- HTTP 200은 **검사 시작 조건**이지 성공이 아니다.
- 성공 판정은 **4-계층 AND**:
  1. 챌린지 마커 없음 (`sec-if-cpt-container`, `Access Denied`, `Just a moment...`, `DataDome`)
  2. 비정상 크기 아님 (< 3KB 또는 WAF fingerprint 크기)
  3. 쿠키 센서 상태 정상 (`_abck=~-1~` 아님)
  4. `success_selectors` 중 하나 이상 매칭 (caller 제공 시 → `strong_ok`, 미제공 시 → `weak_ok`)

### 격자 축 (profile이 우선순위 추천, 격자는 전수 시도)

| 축 | 값 | 비고 |
|----|-----|------|
| `url_transforms` | `original`, `mobile_subdomain` (`www.→m.`), `am_prefix`, `drop_www` | 사이트명 없음, 규칙만 |
| `tls_impersonate` | `safari`, `safari_ios`, `chrome99`, `chrome119`, `chrome131`, `chrome_android`, `firefox`... | 프로파일별 avoid 리스트 존재 |
| `referer_strategy` | `self_root`, `google_search`, `none` | |

**device_class**:
- `"auto"` (기본) — 프로파일 전략 따름
- `"desktop"` — TLS 데스크톱만 + `mobile_subdomain` 비활성
- `"mobile"` — TLS 모바일만 + `mobile_subdomain` 활성

### Playwright 폴백 (capability-matched)

`engine/executor.py`가 프로파일의 `capabilities_needed`를 읽고 실행기를 자동 선택:

| 태그 | 실행기 | 언제 |
|------|--------|------|
| `needs_real_tls_stack` + `needs_js_exec` | `engine/templates/playwright_real_chrome.js` (로컬 Node) | Akamai Bot Manager 등 — Chromium 번들 TLS는 탐지됨 |
| `needs_js_exec` only | Playwright MCP / 현재 어시스턴트 세션의 브라우저 도구 | Cloudflare 기본 방어 등 |
| `needs_mobile_context` (+ real_tls) | `engine/templates/playwright_mobile_chrome.js` | 모바일 디바이스 에뮬레이션 필요 |

자세한 선택 기준: [playwright.md](references/playwright.md).

### Playwright (JS 실행) 호출 규칙

`fetch_chain`의 `needs_js_exec only` 케이스는 **현재 어시스턴트 세션에서 브라우저 도구를 직접 구동**
해야 한다. subprocess 경로 없음. 즉:
1. `result.summary`에 "Playwright MCP must be invoked from the active assistant session"이 포함되면
2. 사용 가능한 브라우저 도구(navigate → wait → snapshot)로 세션이 직접 처리한다.
   브라우저 도구가 없는 환경이면 한계를 보고하고 Local Node 템플릿
   (`engine/templates/playwright_real_chrome.js`) 또는 Jina/archive/플랫폼 API 경로로 대체한다.

## Phase 2 — 수동 개입 (옵션)

Phase 1이 `ok=False`를 반환하면 사용자 힌트를 받아 재시도:

```python
result = fetch(
    url,
    success_selectors=[...],
    user_hint={"impersonate_first": "safari_ios", "referer_strategy": "none"},
)
```

힌트는 **현재 호출 1회에만** 적용되며 저장되지 않는다.

## 의존성 자동 설치

최초 호출 시 필요 패키지를 확인/설치한다. 점검만 하려면 인자 없이, 설치까지 하려면 `--install`.
**curl_cffi는 0.15.0 이상**을 요구한다 — 0.15부터 `impersonate="chrome"`이 최신 Chrome(146+) 지문으로
갱신되고(0.14는 chrome142에 고정), HTTP/3 지문과 SSRF-safe redirect 기본값이 추가됐다. 아래 수동 가드는
**미설치뿐 아니라 0.15 미만이면 업그레이드**한다:
```bash
bash scripts/bootstrap.sh            # 점검만 (curl_cffi / beautifulsoup4 / pyyaml / node)
bash scripts/bootstrap.sh --install  # 누락 패키지 설치
# 수동 확인 (0.15 미만이면 업그레이드):
python3 -c "import curl_cffi,bs4,yaml; v=curl_cffi.__version__.split('.'); assert (int(v[0]),int(v[1]))>=(0,15)" 2>/dev/null \
  || pip install -U "curl_cffi>=0.15.0" beautifulsoup4 pyyaml -q
```

Playwright 로컬 경로 사용 시 Node가 필요:
```bash
npm i -g playwright playwright-extra puppeteer-extra-plugin-stealth
npx playwright install chrome
```

## engine 코드를 건드렸다면 (CI 게이트)

```bash
python3 engine/bias_check.py        # No-Site-Name Rule 린터
bash scripts/smoke_test.sh          # bias_check + unit/online smoke (pytest 및 직접 실행 모두 지원)
```

## 빠른 참조 — Phase 0 명령어

> **먼저 이걸 기억하라: Reddit/X/YouTube는 이제 engine이 자동 처리한다.**
> `bash scripts/run_engine.sh "<URL>"` (= `python3 -m engine "<URL>"`) 하나면 Phase 0 라우터(`engine/phase0.py`)가
> **격자보다 먼저** 공식 경로를 시도한다 — Reddit→`.rss`, X 트윗→`tweet-result`/oEmbed, X 프로필→syndication, YouTube→`yt-dlp`.
> 아래 수동 스니펫은 디버그/참조용이며 trace에 `phase=phase0`로 기록된다.
> (실측 주의: Reddit `.json`+모바일UA·`syndication-timeline`은 흔히 403/429라 plain `curl`은 신뢰 불가 — engine이 curl_cffi 지문으로 우회한다.)

```bash
# ★ 거의 모든 경우 이거면 됨 (Phase 0 자동 + 실패 시 격자→정찰 에스컬레이션)
bash scripts/run_engine.sh "<URL>"      # = python3 -m engine "<URL>"

# 범용 웹 (Jina Reader — 일반 HTML만, WAF 사이트엔 무효)
curl -s "https://r.jina.ai/{URL}"

# yt-dlp — 1,858 사이트 미디어 메타데이터 / 자막
yt-dlp --dump-json "URL"
yt-dlp --write-sub --write-auto-sub --sub-lang "en,ko" --skip-download -o "/tmp/%(id)s" "URL"

# Reddit — .rss (curl_cffi 지문 필요; plain curl은 TLS로 403)
python3 -c "from curl_cffi import requests as r; print(r.get('https://www.reddit.com/r/{sub}/.rss', impersonate='safari').text[:2000])"

# X/Twitter — 개별 트윗(가장 안정적): tweet-result / oEmbed
python3 -c "from curl_cffi import requests as r; print(r.get('https://cdn.syndication.twimg.com/tweet-result?id={TWEET_ID}&token=a', impersonate='safari').text)"
# X 프로필 타임라인 (rate-limit 변동 — engine이 재시도) / 키워드: web.search_query(site:x.com {kw})→tweet-result
curl -sL "https://syndication.twitter.com/srv/timeline-profile/screen-name/{handle}"

# Hacker News
curl -sL "https://hacker-news.firebaseio.com/v0/topstories.json?limitToFirst=10&orderBy=%22%24key%22"
```

> 커버리지 회귀 점검: `python3 tests/coverage_battery.py` — 플랫폼별 전수 경로 pass/fail + 썩은 예시 자동 적발.

## No-Site-Name Rule

`engine/**`, `waf_profiles.yaml`, `engine/templates/**` 파일에는 **특정 사이트의
도메인/URL/셀렉터/브랜드명을 하드코딩하지 않는다**.

### 금지

- `"coupang.com": {...}` 같은 사이트별 레지스트리 엔트리
- `if "coupang" in url: ...` 같은 도메인 분기
- WAF 프로파일 `notes`에 특정 사이트 이름이나 경험적 byte 크기 박제

### 허용

- `SKILL.md` / `references/*.md`의 **설명 텍스트**에 사이트 이름 예시 (독자 이해용)
- `Phase 0` 공식 API 인덱스 (플랫폼이 공식 공개한 엔드포인트)
- `observations/*.jsonl` 로그 (append-only 관측 데이터 — 코드 경로에 영향 없음)
- 호출자가 제공하는 `success_selectors`, `user_hint` (현재 호출에만 유효)

### 경계 사례 판단 기준

> "이 엔트리가 다른 사이트에서도 같은 WAF를 쓰면 일반적으로 유효한가?" → YES면 `waf_profiles.yaml`,
> NO면 runtime hint.

### 새 사이트가 안 뚫릴 때

1. 먼저 `result.trace`에서 어느 phase가 실패했는지 확인
2. 사용자의 `user_hint`로 1회 재시도
3. 반복 성공 패턴이 관측되면 `observations/`에 로그 (아직 자동 기록 없음 — 수동)
4. 3회+ 반복 확인되고 **동일 WAF를 쓰는 다른 사이트에도 유효**하면 `waf_profiles.yaml` 해당
   프로파일의 `tls_impersonate_candidates` / `url_transform_order`를 튜닝 (사이트명 절대 넣지 않음)
5. 여전히 안 되면 새 WAF 프로파일 후보 검토 (예: DataDome 세부화, Kasada 등)

## 관련 문서 (references/) — 언제 무엇을 읽을지

이 섹션은 **참조 파일 선택 가이드**다. 문제가 생겼을 때 어떤 `references/*.md`를 열어야 할지
결정하는 기준으로 쓴다. 필요할 때만 해당 파일을 읽고, 선제적으로 전부 읽지 않는다.
빠른 시작이 필요하면 `references/fallback.md`부터 본다.

### A. Engine 확장·진단 (하네스 내부)

| 파일 | 언제 읽는가 | 무엇을 다루는가 |
|------|-------------|-----------------|
| [`tls-impersonate.md`](references/tls-impersonate.md) | curl_cffi 격자가 전부 `challenge`/`blocked`로 끝날 때, 새 impersonate 타겟을 `waf_profiles.yaml`에 추가할 때 | curl_cffi로 Safari/Chrome/Firefox TLS(JA3/JA4) 지문 복제하는 방법, WAF(Akamai/Cloudflare/F5 등)별 최적 타겟 조합, 임퍼소네이션 타겟 버전 목록, `tls_impersonate_avoid`의 실증 근거 |
| [`playwright.md`](references/playwright.md) | engine이 Playwright fallback으로 넘어가는데 MCP/Local Chrome 중 어디로 갈지 확인 필요할 때 | Approach 1 (브라우저 도구 — Cloudflare급 챌린지), Approach 2 (Local Node + `channel:'chrome'` + stealth — Akamai Bot Manager급), 템플릿 파라미터 규격 |
| [`fallback.md`](references/fallback.md) | `verdict`가 애매하거나 Phase 전환 타이밍 결정 필요할 때 | engine의 Phase 0→1→2→3 에스컬레이션 원칙, 응답 성공/실패 판정 기준 세부, 각 Phase 종료 조건 |
| [`metadata.md`](references/metadata.md) | 본문 전체를 못 가져왔지만 제목·요약·가격·저자 같은 핵심만이라도 필요할 때 | OGP 메타 태그, JSON-LD (Schema.org), Twitter Card 파싱, 구조화 데이터 추출 패턴 |

### B. 경량 대안 (engine 말고 다른 도구가 나은 상황)

| 파일 | 언제 읽는가 | 무엇을 다루는가 |
|------|-------------|-----------------|
| [`jina.md`](references/jina.md) | WAF 없는 일반 웹(블로그·뉴스·Wiki)의 깨끗한 마크다운 추출 필요할 때 | `r.jina.ai/URL` 한 줄로 Puppeteer 기반 JS SPA 렌더링, 마크다운 변환, 무료 500 RPM, API 키 불필요 |
| [`cache-archive.md`](references/cache-archive.md) | 원본 사이트가 차단됐지만 과거 스냅샷으로라도 접근 필요할 때 | Wayback Machine CDX API, archive.today, AMP Cache (Google Cache는 2024-07 종료됨) |
| [`rss.md`](references/rss.md) | 뉴스·블로그·커뮤니티의 시계열 업데이트를 구조화해 받고 싶을 때 | RSS/Atom 자동 발견, 피드 파싱, 인증 불필요 — 가장 깔끔한 시계열 데이터 소스 |

### C. 플랫폼별 공식/공개 API (Phase 0 인덱스와 연결)

| 파일 | 언제 읽는가 | 무엇을 다루는가 |
|------|-------------|-----------------|
| [`json-api.md`](references/json-api.md) | Reddit/Wikipedia/HN/npm/PyPI 등 **URL 변형만으로** JSON/피드를 주는 사이트 | Reddit Atom/RSS(`.rss`) 우회 + score·댓글용 OAuth(`.json`은 WAF 차단), HN Firebase, Algolia Search, Wikipedia REST, npm/PyPI Registry API |
| [`public-api.md`](references/public-api.md) | Bluesky/Mastodon/arXiv/Stack Overflow/CrossRef/GitHub/OpenLibrary/Wayback 공식 API 사용 시 | 인증 없이 쓰는 공식 공개 REST/AT/Atom API 엔드포인트, 요청 형식, 공통 파라미터 |
| [`twitter.md`](references/twitter.md) | X/Twitter 접근 — 프로필 타임라인, 특정 트윗, 키워드 검색 | `syndication.twitter.com` 타임라인, tweet-result/oEmbed 개별 트윗, 검색은 web.search_query로 URL 확보 후 tweet-result |
| [`naver.md`](references/naver.md) | 네이버 블로그·뉴스·증권·검색 접근 | 서비스별 우회(블로그는 `m.blog.naver.com` 변환, 증권은 비공식 JSON, 검색은 `search.naver.com`), 한글 검색 쿼리 패턴 |
| [`media.md`](references/media.md) | YouTube/Vimeo/Twitch/TikTok/SoundCloud 등 미디어 메타·자막·오디오 필요 시 | `yt-dlp --dump-json` 기반 1,858개 사이트 커버, 자막 다운로드(`--write-sub`), 포맷 선택, 라이브/팟캐스트 |

### D. Engine 코드 직접 읽을 때

| 파일 | 언제 읽는가 |
|------|-------------|
| `engine/phase0.py` | Phase 0 공식-API 라우터 (Reddit/X/YouTube 자동 경로). 플랫폼·경로 추가 시. bias_check 면제 파일(R5 sanctioned) |
| `engine/fetch_chain.py` | 체인 단계 로직·`Attempt`/`FetchResult` schema·`untried_routes`/`must_invoke_playwright_mcp` 실패게이트 |
| `engine/validators.py` | 4-계층 검증 세부 (Verdict 분류, 챌린지 마커 목록) |
| `engine/waf_detector.py` | WAF 랭킹 감지 알고리즘, `_LAST_LOAD_ERROR` 처리 |
| `engine/waf_profiles.yaml` | 프로파일별 detectors·tls_candidates·capabilities_needed |
| `engine/url_transforms.py` | URL 변환 규칙 추가할 때 |
| `engine/executor.py` | Playwright MCP vs local capability 매칭 로직 |
| `engine/templates/*.js` | Playwright 템플릿 튜닝 (warmup, reload, devices) |
| `engine/bias_check.py` | 편향 린터 규칙 — brand denylist, URL_PATTERN, excluded dirs |

## Port Notes (Codex)

- 단일 진입점은 `bash scripts/run_engine.sh <URL>` (= `python3 -m engine <URL>`). engine의 WAF
  로직을 즉흥으로 재구현하지 않는다.
- 의존성 점검/설치는 `scripts/bootstrap.sh [--install]`.
- R7 정찰은 `scripts/playwright_recon.js` (stdin JSON → 내부 `/api/`·`graphql`·`.json` 요청 추출).
- Local Node 브라우저 폴백이 없으면 한계를 보고하고 generic engine / Jina / archive / 플랫폼 API
  경로로 계속 진행한다.
- 산문보다 결정론적 증거(trace 요약)를 우선한다. engine 실패 시 trace 요약 + 차선 경로를 먼저 보인다.
