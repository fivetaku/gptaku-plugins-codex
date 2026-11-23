---
name: insane-design
description: Design system analyze / apply / build router plus the analysis engine. Extracts a deterministic design system from any URL by fetching real CSS, parsing custom properties, and writing a 19-section design.md (schema_version 3.2 with medium + archetype detection) plus an interactive report.ko.html. Also exports design.md frontmatter to a W3C DTCG tokens.json. Pairs with insane-apply and insane-build via the §18 DON'T hex-grep contract. Korean triggers — "디자인 분석해줘", "이 사이트 디자인 시스템 뽑아줘", "CSS 뜯어봐", "design.md 만들어줘", "레퍼런스 리포트 만들어줘", "사이트 분석", "디자인 토큰 추출", "tokens.json 내보내줘". English triggers — "analyze design", "extract design tokens", "rip the design system", "what CSS does this site use", "export DTCG tokens".
---

# Insane Design

> URL 하나 → 실제 CSS 기반 design.md + 인터랙티브 HTML 리포트.
> design.md frontmatter → W3C DTCG tokens.json export도 이 스킬이 담당한다.

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

이 문서는 참고 문서가 아니라 **실행 지시서**다.
URL이 제공되면 즉시 Step 1부터 실행한다.

---

## Persona

```
You are an expert designer. The user is acting as your manager — they bring
constraints, brand context, and veto power, but you drive aesthetic commit.
Never hedge; pick one BOLD direction and defend it.
```

전체 계약: `$PLUGIN_ROOT/skills/insane-design/shared/README.md` §1 Identity.

## 상호작용 규칙 (§A)

질문이 필요하면 `$PLUGIN_ROOT/shared/questioning-policy.md` §A의 질문 도구
(`request_user_input_async`, Plan 모드면 `request_user_input`)로 묻는다. 두 도구가 모두 없을 때만 채팅 번호 블록으로 폴백한다.
질문 도구를 부른 뒤에는 한 줄 안내만 쓰고 턴을 끝내며, 답이 오는 다음 메시지에서 이어서 진행한다.

async 호출 형식: `{"questions":[{"title":"헤더 — 질문","options":["추천안 (추천) — 설명","대안 — 설명"]}]}`. 문항에는 `title`·`options`(문자열 배열)만 넣는다. `question`·`header`·`id`는 Plan 모드 `request_user_input` 전용이라 async에 넣으면 파싱 오류가 난다. "기타·직접 적기" 선택지는 넣지 않는다(자유 입력 칸이 자동으로 붙는다).

- analysis는 인터뷰형이 아니라 **추출형**이다. URL과 출력 루트가 명확하면 질문 없이 진행하고,
  추론 가능한 건 묻지 않는다(§1 "추론 가능한 건 안 묻기").
- URL/출력 루트가 모호할 때만 §A 질문 도구로 **1회** 확인한다(추천안을 1번에).
- 토큰/색/폰트는 **추출**한다 — 환각으로 만들지 않는다.

---

## Smart Router — 입력에 따라 analysis / apply / build / export 판별

이 스킬은 `insane-design` 패밀리의 진입점이기도 하다. 사용자 입력을 보고 모드를 판별한다.

| 입력 패턴 | 동작 | 모드 |
|-----------|------|------|
| `http://...` 또는 `https://...` | URL 분석 시작 (아래 7-Step) | → analysis (이 스킬) |
| `build` 또는 `build ...` | 새 빌드 (맨바닥 / design.md / URL) | → `$PLUGIN_ROOT/skills/insane-build/SKILL.md` |
| `export <slug>` / "tokens.json 내보내줘" | design.md → DTCG tokens.json | → Export 모드 (이 스킬, 아래) |
| `[slug]` (URL이 아닌 문자열) | 해당 design.md를 프로젝트에 적용 | → `$PLUGIN_ROOT/skills/insane-apply/SKILL.md` |
| (인자 없음) | 모드 선택 요청 | → 아래 §A 질문 |

**자연어인 경우 → 의도 판별**:
- "분석해줘", "CSS 뜯어봐", "디자인 시스템 뽑아줘" → analysis (URL 요청)
- "적용해줘", "이 스타일로", "처럼 만들어줘" → apply (slug 요청)
- "만들어줘", "빌드", "처음부터", "랜딩 만들어줘", "덱 만들어줘", "카드뉴스 만들어줘" → build
- "내보내줘", "tokens.json", "DTCG", "Figma Tokens" → export

**apply / build로 넘길 때**: 해당 SKILL.md를 Read하고 그 워크플로우를 따른다. 남은 인자를 그대로 전달한다
(`build` 이후 텍스트, 또는 slug). build 진입 전에는 `$PLUGIN_ROOT/skills/insane-design/shared/README.md`(공통 계약)를 먼저 Read한다.

**인자가 없을 때** — §A 질문 도구 1콜로 묻는다(아래 블록은 번호 블록 폴백일 때의 모양; 도구를 쓰면 같은 질문·선택지로 옮기고 호출 뒤 턴을 끝낸다):

```
질문: 무엇을 할까요?
1. 사이트 분석 (analysis) — URL을 주시면 해당 사이트의 디자인 시스템을 분석해 design.md + report를 생성합니다. (추천 — 다른 모드의 입력이 됩니다)
2. 디자인 적용 (apply) — 이미 분석된 디자인(Stripe, Apple 등 100개)을 내 프로젝트에 적용합니다.
3. 새 빌드 (build) — 맨바닥에서 랜딩/덱/카드뉴스/디자인 시스템 카탈로그를 즉석 합성 또는 design.md 기반으로 빌드합니다.
4. DTCG export — 분석된 design.md를 tokens.json(Figma Tokens Studio / Style Dictionary 호환)으로 내보냅니다.
5. 문장으로 직접 요청
```

- 1 → analysis 진입. URL이 없으면 한 줄로 URL을 요청한다 (예시: `https://stripe.com`, `https://linear.app`, `https://vercel.com`).
- 2 → apply 진입. slug가 없으면 §A 질문으로 레퍼런스를 고르게 한다 (예: `1. stripe — 보라 브랜드, sohne, weight 300 (SaaS 대표)` / `2. apple — 모노크롬, SF Pro, 미니멀` / `3. toss — Toss Blue 핀테크` / `4. nike — Futura/Helvetica 스포티` / `5. 다른 slug 직접 입력`).
- 3 → build 진입 (Step 0 entry 분기부터).
- 4 → Export 모드.

---

## 사전 준비

스킬 실행 전 다음 레퍼런스를 필요한 Step에서 읽는다:

- **`$PLUGIN_ROOT/skills/insane-design/references/schema.v3.2.md`** — frontmatter + 섹션 구조의 **단일 진실 원천** (Step 0 — 가장 먼저 Read 필수). 이 파일을 읽지 않으면 frontmatter 일관성을 보장할 수 없음.
- `$PLUGIN_ROOT/skills/insane-design/references/template.md` — design.md 19섹션 v3.2 템플릿 (§00~§19) (Step 5에서 Read)
- `$PLUGIN_ROOT/skills/insane-design/references/report-prompt.md` — HTML 리포트 생성 규칙 v2.1 (Step 6에서 Read)
- `$PLUGIN_ROOT/skills/insane-design/references/report.css` — canonical CSS (Step 6에서 Read, 있으면 사용)
- `$PLUGIN_ROOT/skills/insane-design/references/pitfalls.md` — 14가지 함정 (Step 4에서 Read)
- `$PLUGIN_ROOT/skills/insane-design/examples/stripe/design.md` — 골드 스탠다드 예시 (Step 5에서 참조)
- `$PLUGIN_ROOT/skills/insane-design/examples/stripe/report.ko.html` — 리포트 골드 스탠다드 (Step 6에서 참조)

---

## 워크플로우 — 7 Steps

> **경로 규칙**: 모든 Bash 명령은 반드시 **프로젝트 루트에서** 실행한다.
> Step 실행 전 `WORK_DIR`을 확정하고, 모든 경로를 절대 경로 또는 `$WORK_DIR` 기준으로 사용한다.
> 모든 결과물은 `insane-design/{slug}/` 하위에 통합 저장한다. 플러그인 자산(`$PLUGIN_ROOT/...`)은 읽기 전용.

```bash
# Step 0: 프로젝트 루트 확정 (모든 Step에서 공유)
WORK_DIR="$(pwd)"   # 사용자의 현재 디렉토리를 프로젝트 루트로 사용
```

### Step 1: INIT — script

URL을 파싱하고 작업 환경을 준비한다.

1. URL에서 slug 추출 (도메인 → kebab-case: `stripe.com` → `stripe`, `linear.app` → `linear`)
2. URL 검증 (**보안 필수**):
   - `http://` 또는 `https://` 프로토콜 확인
   - `localhost`, `127.0.0.1`, `file://` 차단
   - 도메인 형식 유효성 확인
   - **셸 특수문자 검증**: URL에 `` ` ``, `$`, `(`, `)`, `;`, `|`, `&`, `>`, `<` 등 셸 메타문자가 포함되면 거부
   - 이후 모든 Bash 명령에서 URL은 반드시 **큰따옴표로 감싸서** 사용: `"$URL"`
3. **매체(medium) 감지** (frontmatter 필드용):

   | 입력 패턴 | medium | medium_confidence |
   |----------|--------|-------------------|
   | URL이 `.pptx`/`.ppt`로 끝남 | `slide` | `high` |
   | URL이 `docs.google.com/presentation/*` | `slide` | `high` |
   | URL이 `*.pdf`로 끝남 | `print` | `high` (스텁만, 현 세션 미구현) |
   | URL이 `*.figma.com/file/*` (디자인 시스템 탐지 시) | `design-system` | `medium` |
   | 이미지 업로드 입력 + 정사각 비율 | `card-news` | `medium` |
   | 그 외 일반 URL | `web` | `high` (기본값) |

   감지 결과는 Step 5 WRITE-MD에서 frontmatter `medium`, `medium_confidence` 필드에 그대로 기록한다.

4. **Archetype 감지** (v3.2 frontmatter 필드용 — 판정 #21):

   사이트의 컨텍스트를 11 enum + freeform으로 분류. Step 4 INTERPRET이 archetype을 컨텍스트로 사용하여 §00 Narrative 어휘와 §13 핵심 컴포넌트 강조점을 결정.

   **1차 단서** (도메인 + meta tag 기반 자동 감지):
   - 도메인 끝 (`.shop`, `.store`, `.app`, `.dev`, `.docs.*` 등)
   - meta tag (`og:type`, `twitter:card`, `application-name`)
   - hero 구조 첫 인상 (스크린샷)

   **11 enum**:

   | archetype | 단서 | 예시 |
   |-----------|------|------|
   | `commerce-marketplace` | listing card 위주, search-bar 큼 | Airbnb, Coupang, Etsy |
   | `editorial-product` | 풀-블리드 제품 photography | Apple, Tesla, Nike |
   | `editorial-magazine` | article-first, headline 강조 | Verge, Wired, Medium |
   | `app-dashboard` | sidebar nav, dense data | Linear, Notion, Figma |
   | `saas-marketing` | hero CTA + feature grid | Stripe, Vercel, Supabase |
   | `landing-utility` | single-page, 가입 유도 | Resend, Posthog landing |
   | `documentation-site` | sidebar TOC + code blocks | Tailwind docs, MDN |
   | `portfolio-personal` | 프로젝트 grid + 자유 레이아웃 | 개인 포트폴리오 |
   | `automotive` | 차량 photography + spec | BMW, Ferrari, Tesla |
   | `luxury-brand` | 미니멀 + 고급 photography | Chanel, Dior, Gucci |
   | `other` | 위 안 맞음 | (보조 freeform 필드 사용) |

   **`archetype_confidence`**: high (명확) / medium (혼합) / low (추정)

   감지 결과는 Step 5 WRITE-MD에서 frontmatter `archetype`, `archetype_confidence`에 기록.
5. 출력 디렉토리 생성 (**절대 경로 사용**):

```bash
mkdir -p "$WORK_DIR/insane-design/{slug}/{screenshots,css,phase1}"
```

6. 사용자에게 시작 알림:
```
🎨 {slug} 디자인 분석을 시작합니다.
URL: {url}
예상 소요: 3-5분
```

---

### Step 2: FETCH — script

HTML/CSS와 스크린샷을 **병렬**로 수집한다.

> **접근 전략**: insane-search Phase 0→1→2→3 에스컬레이션 체인을 적용.
> 어떤 방법도 미리 제외하지 않는다 — 되는지는 시도해봐야 안다.
> 상세: `$PLUGIN_ROOT/skills/insane-design/references/data-collection.md`.

#### 성공 판정 함수

모든 tier에서 수집한 HTML에 반드시 적용:

```bash
html_ok() {
  local f="$1"
  [ -s "$f" ] || return 1
  [ "$(wc -c < "$f")" -ge 5000 ] || return 1
  grep -q "<html" "$f" || return 1
  # Cloudflare/WAF 챌린지 감지
  grep -qiE "challenge-error-text|cf_chl_opt|__cf_chl_jschl|verify you are human|checking your browser" "$f" && return 1
  return 0
}

css_ok() {
  local f="$1"
  [ -s "$f" ] || return 1
  [ "$(wc -c < "$f")" -ge 200 ] || return 1
  # 403/error HTML이 CSS로 저장된 경우 감지
  grep -qiE "DOCTYPE HTML|403 ERROR|Access Denied|Request could not be satisfied|challenge-error-text" "$f" && return 1
  return 0
}
```

#### 2A. HTML + CSS 수집

**6-tier 에스컬레이션 체인**으로 HTML을 수집한다:

```bash
URL="{url}"  # Step 1에서 검증된 URL
OUT="$WORK_DIR/insane-design/{slug}/index.html"

# Tier 1: curl Chrome Desktop UA
curl -sL \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.9" \
  --compressed --max-time 30 -o "$OUT" "$URL"

# Tier 2: curl Mobile UA
if ! html_ok "$OUT"; then
  curl -sL \
    -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1" \
    -H "Accept-Language: en-US,en;q=0.9" \
    --compressed --max-time 30 -o "$OUT" "$URL"
fi

# Tier 3: Jina Reader HTML 모드 (Cloudflare/WAF 우회 — 실증된 방법)
# ⚠️ 대상 URL이 r.jina.ai로 전송됩니다. 민감한 내부 URL 사용 금지.
if ! html_ok "$OUT"; then
  curl -sL --max-time 45 \
    -H "X-Return-Format: html" \
    "https://r.jina.ai/$URL" -o "$OUT"
fi

# Tier 4: curl_cffi TLS 임퍼소네이션 (Phase 2 에스컬레이션)
# 출력 경로는 argv로 전달 — quoted heredoc 안에서는 $OUT이 확장되지 않는다.
if ! html_ok "$OUT"; then
  python3 -c "import curl_cffi" 2>/dev/null || pip install curl_cffi -q
  python3 - "$OUT" <<'PYEOF'
from curl_cffi import requests as cffi_req
import sys
url = "{url}"
out = sys.argv[1]
for target in ["safari", "chrome", "firefox"]:
    try:
        r = cffi_req.get(url, impersonate=target, timeout=20,
                         headers={"Accept-Language": "en-US,en;q=0.9",
                                  "Referer": "https://www.google.com/"})
        if r.status_code == 200 and len(r.text) > 5000:
            open(out, "w").write(r.text)
            break
    except: continue
PYEOF
fi

# Tier 5: Wayback Machine 캐시 (사이드카 — 원본 전부 실패 시)
if ! html_ok "$OUT"; then
  WB=$(curl -sL --max-time 15 "http://archive.org/wayback/available?url=$URL" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('archived_snapshots',{}).get('closest',{}).get('url',''))" 2>/dev/null)
  [ -n "$WB" ] && curl -sL --max-time 30 "$WB" -o "$OUT"
fi

# Tier 6: headless playwright (최후 수단 — JS 챌린지 전용, python playwright가 설치돼 있을 때만)
# html_ok "$OUT" 실패 시 → 아래 2B의 playwright 스니펫과 같은 방식으로 page.content()를 "$OUT"에 저장
```

> **⚠️ 외부 API 고지**: Tier 3(Jina), Tier 5(Wayback Machine)에서 대상 URL이 외부로 전송됩니다.

**CSS 수집 — 403 fallback 포함**:

```bash
# 1. CSS 링크 추출
grep -oE 'href="[^"]+\.css[^"]*"' "$OUT" | \
  sed 's/href="//;s/"$//' | sort -u > "$WORK_DIR/insane-design/{slug}/css/_urls.txt"

# 2. CSS 다운로드 + 403 fallback
BASE_URL="{url}"
while IFS= read -r css_href; do
  case "$css_href" in
    http*) abs_url="$css_href" ;;
    //*) abs_url="https:$css_href" ;;
    /*) abs_url="$(echo "$BASE_URL" | grep -oE 'https?://[^/]+')$css_href" ;;
    *) abs_url="$BASE_URL/$css_href" ;;
  esac
  fname="$(echo "$css_href" | sed 's/[?#].*//' | xargs basename)"
  dest="$WORK_DIR/insane-design/{slug}/css/$fname"

  # 직접 다운로드
  curl -sL --max-time 15 -o "$dest" "$abs_url"

  # CSS 유효성 검사 — 403/challenge HTML이면 순차 fallback
  if ! css_ok "$dest"; then
    # Fallback 1: curl_cffi (safari → firefox) — WAF/CDN 403 우회
    python3 - <<PYEOF
from curl_cffi import requests as cffi_req
for target in ["safari", "firefox", "chrome"]:
    try:
        r = cffi_req.get("$abs_url", impersonate=target, timeout=15)
        if r.status_code == 200 and len(r.text) > 200 and "{" in r.text[:500]:
            open("$dest", "w").write(r.text)
            break
    except: continue
PYEOF
  fi

  if ! css_ok "$dest"; then
    # Fallback 2: Wayback Machine CDX 캐시
    WB_CSS=$(curl -sL --max-time 10 "http://archive.org/wayback/available?url=$abs_url" | \
      python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('archived_snapshots',{}).get('closest',{}).get('url',''))" 2>/dev/null)
    [ -n "$WB_CSS" ] && curl -sL --max-time 15 "$WB_CSS" -o "$dest"
    # 여전히 유효하지 않으면 삭제
    css_ok "$dest" || rm -f "$dest"
  fi
done < "$WORK_DIR/insane-design/{slug}/css/_urls.txt"
wait
rm -f "$WORK_DIR/insane-design/{slug}/css/_urls.txt"

# 3. CSS 0개면 인라인 <style> 추출
if [ -z "$(ls "$WORK_DIR/insane-design/{slug}/css/"*.css 2>/dev/null)" ]; then
  python3 -c "
import re, pathlib
html = pathlib.Path('$OUT').read_text(errors='replace')
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
combined = '\n'.join(s for s in styles if len(s.strip()) > 50)
if combined:
    pathlib.Path('$WORK_DIR/insane-design/{slug}/css/_inline.css').write_text(combined)
    print(f'Inline CSS extracted: {len(combined)} bytes')
"
fi
```

#### 2B. 스크린샷 수집 (병렬)

```bash
# 1차: Jina 스크린샷 (X-Respond-With: screenshot + 5초 대기)
# ⚠️ 대상 URL이 r.jina.ai로 전송됩니다.
curl -sL \
  -H "X-Respond-With: screenshot" \
  -H "X-Wait-For: 5000" \
  --max-time 45 \
  "https://r.jina.ai/$URL" \
  -o "$WORK_DIR/insane-design/{slug}/screenshots/jina-hero.png"

# PIL crop
python3 -c "
from PIL import Image
img = Image.open('$WORK_DIR/insane-design/{slug}/screenshots/jina-hero.png')
cropped = img.crop((0, 0, img.width, min(800, img.height)))
cropped.save('$WORK_DIR/insane-design/{slug}/screenshots/hero-cropped.png')
" 2>/dev/null

# 2차: Playwright fallback (Jina 실패 또는 < 50KB) — python playwright가 설치돼 있을 때만
SHOT="$WORK_DIR/insane-design/{slug}/screenshots/hero-cropped.png"
if [ ! -s "$SHOT" ] || [ "$(wc -c < "$SHOT")" -lt 50000 ]; then
  python3 -c "
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=[
        '--no-sandbox','--disable-blink-features=AutomationControlled'])
    ctx = browser.new_context(viewport={'width':1280,'height':800},
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
    ctx.add_init_script(\"Object.defineProperty(navigator,'webdriver',{get:()=>undefined})\")
    page = ctx.new_page()
    page.goto('$URL', wait_until='domcontentloaded', timeout=60000)
    try: page.wait_for_load_state('networkidle', timeout=15000)
    except: pass
    time.sleep(8)
    page.evaluate('window.scrollTo(0,0)')
    time.sleep(1)
    page.screenshot(path='$SHOT', clip={'x':0,'y':0,'width':1280,'height':800})
    browser.close()
" 2>/dev/null && echo "Playwright screenshot saved"
fi
```

#### 수집 실패 처리

- HTML Tier 1~6 전부 실패 → 사용자에게 "접근 불가" 메시지 + 중단
- CSS 0개 (인라인 추출도 실패) → "CSS 토큰 부족" 경고 후 Step 3 hex frequency 분석으로 진행
- 스크린샷 실패 → 경고 후 계속 진행 (스크린샷 없어도 design.md 생성 가능)

---

### Step 3: EXTRACT — script

CSS에서 디자인 토큰을 추출한다. 4개 스크립트를 `$WORK_DIR`에서 **반드시 다음 순서**로 호출:

```bash
cd "$WORK_DIR"

# v3.2: var_resolver 먼저 — brand_candidates가 resolved_tokens.json을 활용해
# var() 체인으로만 정의된 토큰 (Ferrari `--f-color-accent-100: var(--f-color-rosso-corsa-100)` 같은)도 잡음.
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/var_resolver.py" {slug}
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/brand_candidates.py" {slug}
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/typo_extractor.py" {slug}
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/alias_layer.py" {slug}
```

결과: `$WORK_DIR/insane-design/{slug}/phase1/` 에 4개 JSON:
- `brand_candidates.json` — 브랜드 색상 후보 (semantic + selector-role + frequency)
- `resolved_tokens.json` — var() 체인 해결된 토큰 (`samples: {name: {raw, resolved, chain}}` 형식 — brand_candidates가 이 형식을 직접 소비한다. 상위 50개 캡이라 var가 많은 사이트에선 부분 복구)
- `typography.json` — 타이포 스케일 (heading/text/input/quote)
- `alias_layer.json` — tier 분류 (util/action/component/core)

> **§11 Layout / §12 Responsive / §13 Components는 스크립트로 추출하지 않는다.**
> 사이트마다 CSS 구조가 완전히 다르므로 범용 파서가 불가능하다.
> Step 4에서 에이전트가 CSS를 직접 읽고 AI 판단으로 분석한다.

#### 추출 실패 처리

CSS custom properties 0개면:
- "CSS 토큰 부족 — Tailwind/CSS-in-JS 사이트일 수 있습니다. 빈도 기반 hex 분석으로 대체합니다." 경고
- hex frequency 기반 분석으로 전환 (brand_candidates.json의 frequency_candidates 활용)

---

### Step 4: INTERPRET — prompt (멀티모달)

에이전트가 스크린샷 + 추출 결과 + **CSS 원본**을 직접 읽고 AI 판정을 수행한다.

1. Read: `insane-design/{slug}/screenshots/hero-cropped.png` (또는 `jina-hero.png`)
2. Read: `insane-design/{slug}/phase1/brand_candidates.json`
3. Read: `insane-design/{slug}/phase1/typography.json`
4. Read: `insane-design/{slug}/phase1/alias_layer.json`
5. Read: `$PLUGIN_ROOT/skills/insane-design/references/pitfalls.md` — 14가지 함정
6. Read: `insane-design/{slug}/index.html` — HTML 구조 직접 확인 (§11/§13용)
7. Read: `insane-design/{slug}/css/` 주요 CSS 파일 — 레이아웃/컴포넌트 직접 분석 (§11/§12/§13용)

> **§11/§12/§13은 스크립트가 아니라 에이전트가 직접 CSS를 읽고 분석한다.**
> 사이트마다 클래스명, 레이아웃 방식, 컴포넌트 구조가 전부 다르기 때문에
> 범용 파서가 아닌 AI 해석이 필요하다.
> CSS 파일이 너무 크면 (>500KB) 상위 2-3개 파일만 읽되, 주요 패턴을 파악한다.

**판정 항목 (22가지)** — v3.2: 6개 추가 (Designer Guidebook 전환):

| # | 판정 | 출력 |
|---|---|---|
| 1 | Brand color 확정 | hex (예: `#533AFD`) |
| 2 | Light/Dark 테마 | `light` / `dark` / `mixed` |
| 3 | Custom font 식별 | `sohne-var = 유료`, `Inter = 오픈` 등 |
| 4 | Framework 식별 | `Next.js + HDS`, `Tailwind v4` 등 |
| 5 | Hero anatomy 서술 | "2-column, gradient flame bg" 등 |
| 6 | Quick Start "절대 하지 말 것" | 가장 치명적인 한 가지 |
| 7 | DO/DON'T | 각 4~8 항목 (**색상 DON'T는 hex 명시 강제**) |
| 8 | §00 Direction & Metaphor (자유 narrative) | 3-6 문단 자유 서술 + Key Characteristics 5-10 + Direction Summary 4-line |
| 9 | §11 Layout Patterns 분석 | Grid, Hero(+Pattern Summary, BG Treatment), Section, Card, Nav 구조 |
| 10 | §12 Responsive Behavior | 브레이크포인트, 터치 타겟, 접기 전략 |
| 11 | §13 Components 확장 | 6 카테고리 + 상태 6종 + Named Variants + Signature Micro-Specs |
| 12 | §17 Agent Prompt Guide | Quick Color Reference + 프롬프트 예시 |
| 13 | BOLD 방향성 | 1~2 단어 (예: `Industrial Minimalism`, `Refined SaaS`) |
| 14 | Aesthetic Category | redesign-aesthetics.md §3 12가지 + `other` |
| 15 | Signature Element | `hero_impact` / `typo_contrast` / `section_transition` / `minimal_extreme` (+ freeform 보조) |
| 16 | Code Complexity | `low` / `medium` / `high` / `very_high` + 근거 한줄 |
| **17** | **Negative-Space Identity** | "안 쓰는 것" 5-10 항목 (§18 끝) |
| **18** | **Signature Micro-Specs** | 사이트 craft 0-5개 (§13-3) |
| **19** | **Typography Principles** | 4-6 numbered statements (§05 끝) |
| **20** | **Known Gaps & Assumptions** | 측정 한계 + 미관측 항목 ≥3개 (§19 신설) |
| **21** | **Archetype** | 11 enum + freeform (frontmatter) — Step 1에서 결정 |
| **22** | **design_system_level** | lv1 / lv2 / lv3 + 근거 (frontmatter) — Step 5에서 결정 |

#### BOLD 방향성 매핑 판단 트리 (판정 #13~16)

`$PLUGIN_ROOT/skills/insane-apply/references/redesign-aesthetics.md` §3을 먼저 Read.

**판정 #13 (BOLD 방향성) 결정 알고리즘:**

```
1. 채도 측정: brand_candidates.json 최빈 chromatic hex의 HSL 채도(%)
2. 레이아웃 밀도: §11 grid-columns × card-count 추산 (low / medium / high)
3. 톤 키워드: §00 1문단의 핵심 단어 (warm / cool / neon / monochrome / industrial)

매핑 규칙:
- 채도 <15% + 밀도 낮음                → "Industrial Minimalism" / "Monochrome Luxury"
- 채도 <15% + 밀도 높음                → "Brutalist Raw" / "Cool Productivity"
- 채도 50-80% + 밀도 낮음              → "Refined SaaS" / "Friendly Fintech"
- 채도 >80% + 밀도 높음                → "Playful Gradient" / "Maximalist Chaos"
- warm 키워드 + 낮은 채도              → "Warm Productivity" / "Editorial Magazine"
- neon 키워드 + dark 테마              → "Retro-Futuristic"
- pastel 키워드                        → "Soft Pastel"

12가지 중 가장 부합하는 1개 선택. 두 가지 사이면 더 극단적인 것.
```

**판정 #15 (Signature Element) 결정 기준:**

| Signature | 적용 조건 |
|-----------|----------|
| `hero_impact` | Hero가 100vh 풀스크린, 큰 H1, 강한 contrast (Apple, Tesla) |
| `typo_contrast` | display vs body 10배 이상 사이즈 차이 (Stripe, Editorial Magazine) |
| `section_transition` | 섹션마다 배경 톤 drastic 변화 (Notion, Discord) |
| `minimal_extreme` | 장식 완전 제거, 색 3개 이내 (Vercel, Brutalist) |

**판정 #16 (Code Complexity) 결정 기준:**

| Complexity | 미학 예시 | 근거 |
|-----------|----------|------|
| `low` | Refined Minimalism, Brutalist | CSS 변수 + 1개 transition + 절제된 hover |
| `medium` | Industrial Minimalism, Editorial | + staggered reveal, IntersectionObserver |
| `high` | Playful Gradient, Refined SaaS | + 다층 그라디언트, hover bounce, 풍부한 transitions |
| `very_high` | Maximalist Chaos | + parallax, scroll-triggered, particle, custom cursor |

**Step 5 WRITE-MD에서:**
- frontmatter에 4개 필드(`bold_direction`, `aesthetic_category`, `signature_element`, `code_complexity`) 채움
- §00 끝에 `### BOLD Direction Summary` 블록 4줄 추가

#### §00 Direction & Metaphor 작성 (판정 #8 — v3.2 샌드위치)

§00은 **샌드위치 구조**: 위는 디자이너용 자유 narrative, 아래는 기계용 Direction Summary 4-line block.

##### Narrative (위 — 디자이너 영혼)

스크린샷 + tokens.json + 16 판정 결과를 바탕으로 사이트 정체성을 **자유 서술**한다.

**원칙**:
1. **형식 강제 없음** — 사이트마다 다른 순서, 다른 항목 우선. 3-6 문단 권장.
2. **비유와 메타포 환영** — "박물관 갤러리", "잡지 편집자", "산업 데모룸" 같은 자유 표현.
3. **부정형 정체성 명시 권장** — "no second brand color", "shadow only on photography", "weight 500 absent".
4. **Cross-reference 토큰 사용 권장** — `{colors.primary}` 같은 alias 인라인.
5. **Key Characteristics**: 핵심 시각 특징 5-10 bullet (사이트의 "이게 이 사이트다" 항목).

**선택 가능한 항목** (사이트 정체성에 맞는 것을 우선 — 모두 다룰 필요 없음):
- 분위기 / 색 사용 / 타이포 / 공간 / 모션
- 사진처리 / 마이크로카피 / 대비 / 리듬 / 시그니처 디테일
- 부정형 정체성 (안 쓰는 것)

**v3.3 Archetype Vocabulary Floor (71 ref 분석 기반)**:

§00 narrative 작성 시 **archetype 식별 → archetype의 top metaphor에서 최소 1개 + 보편 어휘에서 최소 2개** 결합. 총 metaphor 3+ 사용이 floor.

📚 상세 카탈로그: `$PLUGIN_ROOT/skills/insane-design/references/narrative-vocabulary.md`

**Archetype 빠른 참조 (top signature metaphor)**:
| archetype | signature metaphor |
|-----------|-------------------|
| saas-marketing | terminal / console / parchment / canvas |
| ai-products | runway / gallery / canvas / editorial |
| app-dashboard | canvas / dashboard / rhythm |
| editorial-product | parchment / store / museum / gallery |
| automotive | showroom / cockpit / gallery / canvas |
| fintech-payment | dashboard / spreadsheet / exchange / ledger |
| commerce-marketplace | marketplace / store / boutique / theatre |
| editorial-magazine | broadsheet / magazine / editorial |
| travel-hospitality | marketplace / canvas / editorial |
| entertainment | theater / stage / concert-hall |

**First-Sentence 패턴 5종** (ref 빈도순, 1개 이상 권장):
1. "X is the canonical example of [archetype/space]" — 정체성 선언
2. "X reads like [persona/space]" — 비유 직접 호출
3. "X's marketing surface is [color] canvas holding [type] in [layout]" — 구조형
4. "X is a masterclass in [signature]" — 찬사형 (sparingly)
5. "X stages [object] like [stage metaphor]" — 무대 호출형

**❌ 금지 (Track C "지침 과잉 → 자유도 손상" 패턴)**:
- "1문단=분위기 / 2문단=색 / 3문단=타이포 / 4문단=여백 / 5문단=모션" 강제 순서 lock-in
- generic phrase ("절제된 갤러리 톤" 같이 사이트 특이 단서 없는 형식적 비유)
- 모든 사이트가 같은 단어로 시작하는 형식
- v3.3: "절제된 / 모던한 / 미니멀한 / premium / clean / elegant" 형용사로만 끝나는 문장

##### Direction Summary 4-line block (아래 — 기계 인터페이스)

apply Phase 3 정규식이 정확히 매칭하는 부분. 형식 변경 절대 금지.

```
> **BOLD Direction**: {1-2 단어}
> **Aesthetic Category**: {12 enum + "other"}
> **Signature Element**: 이 사이트는 **{메타포}**으로 기억된다.
> **Code Complexity**: {low/medium/high/very_high} — {근거 한줄}
```

frontmatter 4개 필드(`bold_direction`/`aesthetic_category`/`signature_element`/`code_complexity`)와 정확히 일치해야 함.

#### §11 Layout Patterns 분석 (판정 #9)

HTML 구조 + CSS를 분석하여 다음 항목을 추출:

- **Grid System**: content max-width, grid type (CSS Grid / Flexbox / float), column count, gutter
- **Hero**: layout 방식 (1-column centered / 2-column split / full-width image), background, H1 스펙, max-width
- **Section Rhythm**: section padding (vertical/horizontal), max-width
- **Card Patterns**: card bg, border, radius, padding, shadow, hover 효과
- **Navigation Structure**: type (horizontal / hamburger), position (fixed/sticky/static), height, bg, border
- **Content Width**: prose max-width, container max-width, sidebar width

분석 소스:
- HTML의 `<section>`, `<nav>`, `<header>`, `<main>`, `<article>` 태그 구조
- CSS의 `max-width`, `display: grid`, `display: flex`, `grid-template-columns` 속성
- CSS의 `padding`, `margin`, `gap` 값에서 섹션 리듬 파악

#### §12 Responsive Behavior 분석 (판정 #10)

CSS에서 `@media` 쿼리를 추출하여 다음을 파싱:

- **Breakpoints**: 모든 `min-width` / `max-width` 값 수집 → Name/Value/Description 테이블
- **Touch Targets**: 모바일에서의 button height, input height, minimum tap size (44px 이상인지)
- **Collapsing Strategy**: 네비게이션 접기 방식, 그리드 컬럼 축소, 사이드바 처리, 히어로 레이아웃 변경
- **Image Behavior**: `max-width: 100%`, `object-fit`, aspect-ratio 처리

분석 소스:
- CSS의 `@media (min-width: ...)` / `@media (max-width: ...)` 블록
- 모바일 퍼스트 vs 데스크톱 퍼스트 판별 (`min-width` 우세 → 모바일 퍼스트)

#### §13 Components 확장 분석 (판정 #11 — v3.2 강화)

§13은 세 영역으로 구성 (apply Phase 3 호환 보존):

##### 13-1. Core Patterns (6 카테고리 — 필수, apply 호환)

기존 Buttons/Badges + 추가 분석:

- **Cards & Containers**: bg, border, radius, padding, shadow, hover 상태
- **Navigation**: 링크 스타일, active 상태, 모바일 메뉴
- **Inputs & Forms**: input height, padding, border, focus 스타일, error/placeholder
- **Hero Section**: 배경 처리, 텍스트 크기/weight, CTA 배치

각 컴포넌트: BEM 클래스명 + HTML 마크업 + spec 표 + **상태 6종**(있는 것만): hover / focus / active / disabled / loading / error.

##### 13-2. Named Variants (선택, 0~N개)

기본 6 카테고리 안에 변주가 많을 때 named token으로 분리:
- `button-primary` / `button-primary-active` / `button-primary-focus`
- `button-secondary-pill` / `button-dark-utility` / `button-store-hero`

**ref 가이드**:
- Apple ref는 button만 8개 named variant
- 단순 사이트는 0개 (sub-section 통째 생략 OK)
- frontmatter `components:` map과 동기화

**❌ 강제 금지** ("Grep-Death" 경고):
- "12 컴포넌트 floor" 강제 — 빈 표를 generic으로 채우는 환각 유발
- 가상 variant 생성 — 발견된 변주만

##### 13-3. Signature Micro-Specs (선택, 0~N개) — Apple 격차의 본질

**council 권고 핵심**:
> "Apple은 색상이 아니라 공법으로 만들어진다. backdrop-filter, 0.5px border, blur가 핵심.
> 단순 카테고리 분류는 '면'만 본다 — '결'(craft)을 봐야 한다."

사이트의 기술적 특이점을 **공법 결합 명칭**으로 추출:
- backdrop-filter / blur / 그라디언트 stops / 노이즈 / blend mode
- 0.5px / 1.5px 같은 비표준 두께
- letter-spacing 보정 패턴
- single drop-shadow의 위치/스코프 같은 메타 규칙

**ref 예시 (Apple)**:
- `glassmorphism-hero-tile` (blur(20px) saturate(180%) on rgba 0.7)
- `photography-drop-shadow` (rgba(0,0,0,0.22) 3px 5px 30px on product-imagery only)
- `apple-tight-tracking` (-0.022em on display sizes only)

**조건부**:
- craft 사이트 (Apple/Stripe/Linear): 3-5개
- generic CSS 사이트: 0개 (sub-section 생략 OK)
- 자동 추출 불가 — AI가 CSS + 스크린샷을 보고 직접 판단

#### §17 Agent Prompt Guide 생성 (판정 #12)

분석된 토큰을 바탕으로 자동 생성:

- **Quick Color Reference**: 역할별(Brand primary, Background, Text primary, Text muted, Border, Success, Error) hex 요약 테이블
- **Example Component Prompts**: Hero Section, Card, Badge, Navigation 각각에 대한 복사-가능한 프롬프트 예시
  - 프롬프트에는 실제 추출된 hex, font, size, weight, radius 값 삽입
- **Iteration Guide**: 색상/폰트/여백/컴포넌트 변경 시 주의사항 (semantic token 사용, spacing scale 준수 등)

#### §18 DON'T 작성 규칙 (판정 #7 상세) — apply 자동 검증 지원

**색상 관련 DON'T 항목은 반드시 구체 hex를 포함**해야 한다. apply 스킬의 Step 3 자동 위반 검증이 hex를 grep 패턴으로 사용하기 때문.

**❌ 잘못된 작성 (apply가 검증 불가)**:
- "순백 배경을 쓰지 말 것"
- "검정 텍스트 쓰지 말 것"
- "본문 weight 가볍게 두지 말 것"

**✅ 올바른 작성 (apply가 grep 가능)**:
- "배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#F4F4F4` 사용"
- "텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#1D1D1F` 사용"
- "body에 `font-weight: 400` 사용 금지 — Stripe는 300이 맞다"

**작성 패턴**:
```
"X를 [금지 hex/값]으로 두지 말 것 — 대신 [올바른 hex/값] 사용"
```

apply가 자동 grep 하는 패턴 예시:
- `background:\s*(#fff|#FFFFFF|white)` → 위반 알림
- `color:\s*(#000|#000000|black)` → 위반 알림
- `body[^{]*\{[^}]*font-weight:\s*400` → 위반 알림

**비-색상 DON'T (구조적 금지)는 자유 형식**:
- "CTA 버튼을 정사각형으로 만들지 마라 — pill shape (border-radius 980px)"
- "다크 배경 링크에 brand-500을 그대로 쓰지 마라"

#### §18 Negative-Space Identity (판정 #17 — v3.2 신규)

§18 DON'T 다음에 별도 sub-section "🚫 What This Site Doesn't Use"를 작성한다.

**목적**: 단순 금지가 아니라 **"사이트가 의도적으로 결정한 부재"** — 부정형 정체성.

**작성 원칙**:
- 5-10 항목, 자유 서술 (불릿 권장)
- "absent / none / zero / never" 같은 단호한 표현 권장
- gradient / shadow / weight / 두 번째 brand color / hover 등 카테고리 무관

**ref 예시 (Apple)**:
- Brand Gradient: zero gradient-based design tokens
- Weight 500: deliberately absent — only 400 (body) and 600 (display) used
- Hover documentation: never. Default and Active/Pressed states only.
- Second brand color: none — `{colors.primary}` carries every interactive element
- Chrome shadow: none — exactly one drop-shadow, applied to product imagery

**조건부**: 사이트가 모든 카테고리를 다 쓰면 0개도 OK (sub-section 통째 생략).

#### §13-3 Signature Micro-Specs (판정 #18 — v3.2 신규)

위 §13 가이드의 13-3 sub-section 참조. Apple 격차의 본질 — craft 추출.

#### §05 Typography Principles (판정 #19 — v3.2 신규)

§05 Typography Scale 표 다음에 ### Principles 블록 추가.

**작성 원칙**:
- 4-6 numbered statements
- 표가 말하지 못하는 것 (의도 / 부재 / 비대칭)
- "선택의 의도" 명시 ("Body 17px not 16px")
- 부정형 환영 ("weight 500 absent")

**ref 예시 (Apple)**:
1. Body size is 17px, not 16px — Apple's signature density.
2. Negative letter-spacing on display only. Body keeps 0.
3. Weight 400 for body, weight 600 for display. Weight 500 deliberately absent.
4. Two optical sizes (Display + Text) — not one font with axes.

**조건부**: 사이트가 generic이면 0개 (sub-section 생략 OK).

#### §19 Known Gaps & Assumptions (판정 #20 — v3.2 신규)

§18 다음에 새 §19 신설. **evidence-or-gap 계약** (council 권고).

**작성 원칙**:
- 최소 3 항목 강제 (Step 7 validator)
- 5-10 항목 권장
- 자유 서술 (불릿 권장)

**카테고리 예시**:
- 측정 한계 (single page / desktop only / sub-flow 미방문)
- 추출 정확도 (logo wall 자동 분리 80% 등)
- 미관측 토큰 (form validation / loading / error states)
- 다크모드 매핑 부재
- 모션 디테일 (CSS는 봤지만 JS 로직 미분석)

**❌ 절대 추정 금지**:
- 추정 hex 작성 — CSS에 없으면 "측정 불가" 표기
- 가상 토큰명 — 실제 CSS 변수에 없는 alias 생성 금지

#### §06-8 Color Stories (판정 #7 보강 — v3.2)

§06 Colors 끝에 ### Color Stories sub-section 추가.

**상위 4 색만** (verbosity tax 회피):
- Brand Primary
- Surface (가장 큰 영역)
- Text Primary
- Hairline / Border

각 색에 1-3 문장 prose: "왜 / 언제 / 무엇 대신 / 어디에만"

**ref 예시 (Airbnb)**:
> **`{colors.primary}` (#FF385C)** — Rausch, the single brand color. Used for primary CTA backgrounds (Reserve, Continue), the search orb, the heart save state. The most recognizable color in consumer travel. There is no second brand color.

**❌ 강제 금지**:
- 모든 색에 prose (5번째 색부터 generic이 됨)
- monochrome 사이트 (sub-section 생략 OK)

#### §07 Whitespace Philosophy (v3.2)

§07 Spacing 끝에 ### Whitespace Philosophy sub-section 추가.

1-2 paragraph 자유 서술. 사이트 의도가 드러나는 구체 단서.

**ref 예시 (Apple)**: "Every tile begins with at least 64px of air above the headline. This isn't decoration — it's a rhythm."

**조건부**: 사이트가 generic이면 생략 OK.

#### §04 Note on Font Substitutes (v3.2)

§04 Font Stack 끝에 ### Note on Font Substitutes sub-section 추가.

**작성 원칙**:
- 라이선스 폰트가 환경에 없을 때 open-source fallback + 보정값
- 사이트 특이 ("Inter at 600 + ss03 + line-height 1.47→1.44"처럼)
- generic system font만 쓰는 사이트는 생략 OK

#### Brand color 선택 규칙 (판정 #1 상세)

brand_color는 아래 우선순위로 결정한다:

| 우선순위 | 소스 | 예시 |
|---------|------|------|
| 1 | **CTA/primary button의 background-color** | Stripe `#533AFD`, Toss `#3182F6` |
| 2 | **CSS 토큰에서 `brand`/`primary`/`accent` 이름을 가진 변수** | `--hds-color-core-brand-600` |
| 3 | **chromatic hex 빈도 상위** (neutral/white/black 제외) | brand_candidates.json의 chromatic 1위 |
| 4 | **공식 로고 색** (위 3가지가 모두 불명확할 때만) | — |

**brand_color가 될 수 없는 것**:
- `#000000`, `#FFFFFF` 또는 near-black/near-white (채도 < 5%) — 이들은 neutral이지 brand가 아님
- foreground text 색 (`#1d1c1b` 같은 본문 색)
- 고객사 로고/SVG에서만 등장하는 색 (logo wall 오염)

**Dual-anchor 사이트** (light hero와 dark section에 서로 다른 accent가 있는 경우):
- brand_color에는 **CTA 버튼 색** 또는 **더 높은 빈도의 chromatic** 선택
- 나머지는 §06 Colors에서 별도 서술

#### Monochrome 사이트 처리

채도 있는 컬러가 거의 없는 사이트 (Figma, Vercel, Warp 등):

1. **frontmatter에 `color_system: monochrome` 추가**
2. **brand_color**: 가장 채도 높은 accent hex 선택. accent도 없으면 `#000000` 사용하되, §01 Quick Start에 "이 사이트는 monochrome 디자인" 명시
3. **§06 Colors**: 컬러 램프 대신 **grayscale/neutral ramp** + **accent 목록** 구조로 작성
4. **§18 DO/DON'T**: "❌ 임의의 brand color를 지어내지 말 것 — 이 사이트의 정체성은 색이 아니라 톤/타이포"

**원칙 3가지** (절대 위반 금지):
1. AI는 hex 값을 만들지 않는다 — CSS에 없는 hex 생성 = 환각
2. AI는 토큰명을 만들지 않는다 — `color-brand` 같은 가상 이름 금지
3. AI는 팩트 위에 해석만 얹는다 — 값 변경 NO, 분류/설명 OK

---

### Step 5: WRITE-MD — generate

design.md를 생성한다.

1. Read: `$PLUGIN_ROOT/skills/insane-design/references/schema.v3.2.md` — **frontmatter + 섹션 구조 단일 진실 원천 (필수)**. §1 표를 그대로 채우고, §3 토큰 참조 룰을 §13/§15에서 적용한다.
2. Read: `$PLUGIN_ROOT/skills/insane-design/references/template.md` — 19섹션 v3.2 (§00~§19) 산문 템플릿
3. Read: `$PLUGIN_ROOT/skills/insane-design/examples/stripe/design.md` — 골드 스탠다드 (구조 참조)
4. Step 3 팩트 + Step 4 해석(판정 #1~#12)을 조합하여 19섹션 채우기
5. Write: `insane-design/{slug}/design.md`

**필수 사항**:
- YAML frontmatter 맨 위 (`---` 블록)
- v3.2 frontmatter 최상단에 `schema_version: 3.2` 필수 (v3.1은 deprecated)
- frontmatter에 `medium` + `medium_confidence` 필드 (Step 1에서 감지한 값) 필수
- v3.2 frontmatter에 `archetype` + `archetype_confidence` 필드 (Step 1 판정 #21)
- v3.2 frontmatter에 `design_system_level` + `design_system_level_evidence` 필드 (판정 #22)
- v3.2 frontmatter 객체화 OPTIONAL: `colors:`, `typography:`, `components:` (Cross-reference 토큰 그래프)
- 필수 섹션 15개: 00, 01, 02, 03, 04, 05, 06, 07, 08, 11, 13, 15, 17, 18, **19** (Known Gaps 신규 필수)
- 선택 섹션 5개: 09, 10, 12, 14, 16 — 데이터 없으면 통째 제거
- 파일 크기 ≥ 12KB (v3.2 권장 — Designer Guidebook 전환으로 분량 회복)
- 모든 hex 값이 실제 CSS에 존재

**v3.2 토큰 참조 일관성 룰** (schema.v3.2.md §3와 1:1 매핑):

| 섹션 | hex 표기 룰 | 검증 방법 |
|---|---|---|
| frontmatter (1.6 객체) | hex 직접 (정의 위치) | — |
| §00 Direction | hex + `{colors.x}` dual notation **권장** | — |
| §06 Colors 표 | hex 직접 (정의 위치) | — |
| **§13 Components 표/YAML** | **`{colors.x}` 참조 사용 (필수)** | grep 카운트 |
| **§15 Drop-in CSS** | dual notation `#xxx /* {colors.x} */` **권장** | grep 카운트 |
| §16 Tailwind | hex 직접 | — |
| §18 DO/DON'T | hex 직접 (위반 grep용) | — |

**목표 토큰화율:** §13 + §15 합쳐서 `{colors.x}` 참조 비율 **≥ 70%**.
**측정:** `awk '/^## 13\./,/^## 14\./' design.md | grep -oE '\{colors\.[a-z-]+\}' | wc -l` vs `... | grep -oE '#[0-9A-Fa-f]{6}' | wc -l`.

**작성 시 강제 패턴:**
```yaml
# ❌ BEFORE — components 표에서 raw hex
| `button-primary` | bg #0071E3, color #FFFFFF |
| `button-primary-hover` | bg #0076DF |

# ✅ AFTER — frontmatter colors:에 정의 후 참조
| `button-primary` | bg `{colors.primary}`, color #FFFFFF |
| `button-primary-hover` | bg `{colors.primary-hover}` |
```

raw hex가 §13/§15에 70% 넘으면 frontmatter `colors:` 객체 누락 신호. 거꾸로 작업: 발견된 hex를 `colors:`에 named token으로 등록 → 본문에서 참조로 교체.

**v3.2 design_system_level 판정 (#22)**:

| level | 단서 | 예시 |
|-------|------|------|
| `lv1` (engineer spec) | hex/font/size 추출만, 토큰 시스템 미발견 | personal portfolio, 단순 landing |
| `lv2` (system in use) | CSS 변수 + alias layer + 일관 컴포넌트 패턴 | Apple, Stripe, Notion |
| `lv3` (designer guidebook) | 공식 DS 명시 (HDS, Polaris 등) + token tier + naming convention | Stripe HDS using sites |

판정 근거를 `design_system_level_evidence` 필드에 한 줄 기록 (예: "CSS 변수 245개 + alias 100+ + named components 22개").

**v3.2 frontmatter 객체화 (Cross-reference 토큰 그래프)**:

기존 frontmatter 16필드는 그대로 보존 (apply 호환). 추가 객체:

```yaml
colors:
  primary: "{HEX}"            # named token만 — CSS에 실재
  surface-light: "{HEX}"
  text-primary: "{HEX}"
  # ... 가상 alias 생성 금지

typography:
  display: "{FONT}"
  body: "{FONT}"
  ladder:
    - { token: h1, size: "56px", weight: 700 }
  weights_used: [400, 600]
  weights_absent: [500]       # Negative identity 단서

components:
  button-primary: { bg: "{colors.primary}", radius: "980px" }
  # 발견된 변주만 — §13-2 Named Variants와 동기화
```

본문에서 Cross-reference Dual Notation 사용 권장:
```css
color: #0071e3 /* {colors.primary} */;
```
또는 prose에서: "텍스트는 #1D1D1F (`{colors.text-primary}`)로 떨어진다"

**v3 섹션 번호 매핑** (§00~§18):
| § | 섹션 | 필수 |
|---|---|---|
| 00 | Visual Theme & Atmosphere | ✅ |
| 01 | Quick Start | ✅ |
| 02 | Provenance | ✅ |
| 03 | Tech Stack | ✅ |
| 04 | Font Stack | ✅ |
| 05 | Typography Scale | ✅ |
| 06 | Colors | ✅ |
| 07 | Spacing | ✅ |
| 08 | Radius | ✅ |
| 09 | Shadows | ⭕ |
| 10 | Motion | ⭕ |
| 11 | Layout Patterns | ✅ |
| 12 | Responsive Behavior | ⭕ |
| 13 | Components | ✅ |
| 14 | Content / Copy Voice | ⭕ |
| 15 | Drop-in CSS | ✅ |
| 16 | Tailwind Config | ⭕ |
| 17 | Agent Prompt Guide | ✅ |
| 18 | DO / DON'T | ✅ |

---

### Step 6: RENDER-HTML — generate

report.ko.html을 생성한다.

1. Read: `$PLUGIN_ROOT/skills/insane-design/references/report-prompt.md` — 생성 규칙 v2.1 (v3 섹션 매핑 포함)
2. Read: `$PLUGIN_ROOT/skills/insane-design/references/report.css` — canonical CSS (있으면 사용, 없으면 Stripe report에서 추출)
3. Read: `$PLUGIN_ROOT/skills/insane-design/examples/stripe/report.ko.html` — 골드 스탠다드 (CSS/JS/구조 복사)
4. Read: `insane-design/{slug}/design.md` — 데이터 소스
5. Stripe report의 `<style>` 블록 + JS 구조를 기반으로, 토큰/섹션만 현재 서비스로 교체
6. Write: `insane-design/{slug}/report.ko.html`

**v3 → report 섹션 매핑** (template.md 주석 참조):
- §00 Visual Theme → report mood section
- §01 Quick Start → report hero
- §02 Provenance → report §01
- §03 Tech Stack → report §02
- §04+§05 Font/Typography → report §03 (통합)
- §06 Colors → report §04
- §07 Spacing → report §05
- §08 Radius → report §06
- §09 Shadows → report §07
- §10 Motion → report §08 (optional)
- §11 Layout Patterns → report §09
- §12 Responsive → report §09-resp
- §13 Components → report §10
- §14 Content Voice → report §11 (optional)
- §15+§16 CSS/Tailwind → report sidebar
- §17 Agent Prompt → report §agent
- §18 DO/DON'T → report §12

**필수 사항**:
- 한국어
- shadcn zinc 테마 (Pretendard Variable + Inter + JetBrains Mono)
- `--brand-color` 만 서비스별로 교체
- 인터랙티브: 컬러 스와치 hover, 타이포 live preview, 스페이싱 바, Copy 버튼
- 스크린샷: `screenshots/hero-cropped.png` hero 섹션에 삽입
- 파일 크기 ≥ 20KB

---

### Step 7: VALIDATE — script + review

생성 결과를 검증한다.

```bash
# 0. 자동 validator (v3.2 8-check)
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/validate.py" insane-design/{slug}/design.md

# 1. YAML frontmatter 맨 위
head -1 insane-design/{slug}/design.md | grep -q '^---$'

# 2. 필수 섹션 존재 (v3.2: §00~§19)
for n in 00 01 02 03 04 05 06 07 08 11 13 15 17 18 19; do
  grep -q "^## $n\." insane-design/{slug}/design.md || echo "Missing §$n"
done

# 3. 파일 크기
[ $(wc -c < insane-design/{slug}/design.md) -ge 8000 ]
[ $(wc -c < insane-design/{slug}/report.ko.html) -ge 20000 ]

# 4. hex 실존 (상위 3개)
for hex in $(grep -oE '#[0-9A-Fa-f]{6}' insane-design/{slug}/design.md | sort -u | head -3); do
  grep -qi "$hex" insane-design/{slug}/css/*.css || echo "Missing: $hex"
done
```

**실패 시**: 최대 2회 재생성 (실패 항목만 수정). 2회 후에도 실패면 경고 포함 출력.

**성공 시**:
```
✅ {slug} 분석 완료!

📄 design.md:     insane-design/{slug}/design.md ({size}KB)
🌐 report.ko.html: insane-design/{slug}/report.ko.html ({size}KB)
📸 screenshot:     insane-design/{slug}/screenshots/hero-cropped.png

design.md를 코딩 에이전트에 첨부하면 이 사이트 스타일로 UI를 만들 수 있습니다.
report.ko.html을 브라우저에서 열면 인터랙티브 디자인 리포트를 볼 수 있습니다.
DTCG tokens.json이 필요하면 "tokens.json 내보내줘"라고 요청하세요.
```

---

## Export 모드 — design.md → W3C DTCG tokens.json

사용자가 `export <slug>`, "tokens.json 내보내줘", "DTCG export", "export tokens" 등을 요청하면 실행한다.
분석된 design.md의 frontmatter 토큰 그래프를 **W3C DTCG (Design Tokens Format Module)** JSON으로 변환한다.
변환 결과는 즉시 다음 도구들에서 import 가능:

- Figma Tokens Studio (Figma 변수)
- Style Dictionary (Amazon — iOS/Android/Web multi-platform 빌드)
- Specify
- Cobalt UI
- Penpot
- Knapsack
- Supernova
- @google/design.md

### 인자

| 인자 | 동작 |
|------|------|
| `<slug>` | `insane-design/<slug>/design.md` 를 입력으로 사용 |
| `--output <path>` (선택) | tokens.json 저장 경로. 생략 시 `insane-design/<slug>/tokens.json` |
| `--compact` (선택) | indent 없이 minified JSON |

### Step E1: 입력 검증

```bash
WORK_DIR="$(pwd)"
INPUT="$WORK_DIR/insane-design/{slug}/design.md"
[ -f "$INPUT" ] || { echo "❌ 파일 없음: $INPUT"; exit 1; }
```

slug에 셸 메타문자(`` ` `` `$` `(` `)` `;` `|` `&`)가 포함되면 거부.

### Step E2: DTCG 변환

```bash
OUTPUT="$WORK_DIR/insane-design/{slug}/tokens.json"
python3 "$PLUGIN_ROOT/skills/insane-design/scripts/export_dtcg.py" \
  "$INPUT" -o "$OUTPUT"
```

스크립트는 frontmatter의 `colors:` / `typography:` / `spacing:` / `rounded:` 객체를 읽어:
- `colors:` → DTCG `color` 그룹 (`$type: color`)
- `typography.ladder:` → DTCG `typography` 그룹 (composite — `$type: typography`)
- `spacing:` → DTCG `spacing` 그룹 (`$type: dimension`)
- `rounded:` → DTCG `radius` 그룹 (`$type: dimension`)
- 메타 (slug, archetype, design_system_level 등) → `$extensions["com.insane-design"]`

### Step E3: 결과 보고

```
✅ DTCG export 완료

📄 입력:   insane-design/{slug}/design.md
📦 출력:   insane-design/{slug}/tokens.json (N KB)

토큰 통계:
  - color:      M개
  - typography: K개
  - spacing:    L개
  - radius:     P개

다음 도구에서 import 가능:
  → Figma Tokens Studio: Settings → Sync → JSON → 위 경로
  → Style Dictionary:    style-dictionary build --tokens tokens.json
  → @google/design.md:   호환 (DTCG 표준)
```

### 폴백

frontmatter 토큰 그래프 객체(colors:/typography:/...)가 비어 있으면 export는 메타 wrapper만 출력하고 경고:

```
⚠️ frontmatter 토큰 그래프 누락 — schema_version 3.2로 재분석 권장
   현재 파일은 메타 정보만 export됨
```

### 의존성

- Python 3.8+
- PyYAML 권장 (없으면 내장 minimal parser 사용 — v3.2 frontmatter 형식만 지원)

---

## References

| 파일 | 용도 | 참조 Step |
|------|------|-----------|
| **`references/schema.v3.2.md`** | frontmatter + 섹션 구조의 단일 진실 원천 (§1.6 토큰 그래프 = export 입력) | Step 0, 5, 7, Export |
| **`references/architecture.md`** | 전체 시스템 아키텍처 (Phase 1~6, 스크립트/AI 분담, 파일 구조) | 전체 |
| **`references/data-collection.md`** | 5-tier fallback 수집 전략 + Jina Reader 스크린샷 상세 | Step 2 |
| **`references/methodology.md`** | 분석 5단계 프로세스 + 서비스당 체크리스트 | 전체 |
| **`references/workflow.md`** | 서비스당 절차 상세 (소요 시간, 섹션별 데이터 소스) | 전체 |
| **`references/template.md`** | design.md 19섹션 템플릿 v3.2 (§00~§19, YAML frontmatter, 필수/선택 섹션, medium 분기, N/A 규칙) | Step 5 |
| **`references/report-prompt.md`** | HTML 리포트 생성 규칙 v2.1 (v3 섹션 매핑, 인터랙티브 요소, 한글 네이밍) | Step 6 |
| **`references/report.css`** | canonical CSS (리포트 공통 스타일시트, 있으면 사용) | Step 6 |
| **`references/pitfalls.md`** | 35개 서비스 분석에서 발견된 14가지 함정 (가상 토큰명, 리브랜딩, light/dark 역전 등) | Step 4 |
| **`references/narrative-vocabulary.md`** | v3.3 archetype별 metaphor 카탈로그 + first-sentence 패턴 5종 (71 getdesign.md ref 분석 기반) | Step 4 §00 작성 |
| `shared/README.md` | 세 스킬 공통 계약 (Identity · Contract · Verifier · AI Slop · Starter Components) | 전체 |
| `$PLUGIN_ROOT/shared/questioning-policy.md` | §A 질문 도구 정책(번호 블록은 폴백) | Router, 모호한 입력 |
| W3C DTCG spec | https://tr.designtokens.org/format/ | Export |

## Scripts

- **`scripts/brand_candidates.py`** — CSS에서 브랜드 색상 후보 추출 (semantic + selector-role + frequency). var_resolver의 `samples` 출력 + 레거시 2형식(tokens 리스트 · 플랫 dict)을 소비
- **`scripts/var_resolver.py`** — CSS var() 체인 재귀 해결
- **`scripts/typo_extractor.py`** — 타이포그래피 스케일 추출
- **`scripts/alias_layer.py`** — 시멘틱 alias tier 분류 (util/action/component/core)
- **`scripts/capture_jina_screenshots.py`** — Jina Reader API 스크린샷 + PIL crop
- **`scripts/validate.py`** — v3.2 design.md 8-check validator (schema/frontmatter/sections/craft/negative-space/gaps/size/direction-summary). Usage: `python3 validate.py <file_or_dir>` 또는 `--summary-only`
- **`scripts/export_dtcg.py`** — design.md frontmatter → W3C DTCG tokens.json (0 dependencies, PyYAML 있으면 사용)

## Examples

- **`examples/stripe/design.md`** — Stripe 골드 스탠다드 (25KB, 16섹션)
- **`examples/stripe/report.ko.html`** — Stripe HTML 리포트 골드 스탠다드 (74KB)
- `examples/*/design.md` — 100+ 사이트 분석 코퍼스 (apply/build의 레퍼런스, 읽기 전용)

## Settings

| 설정 | 기본값 | 변경 방법 |
|------|--------|-----------|
| 리포트 언어 | 한국어 (report.ko.html) | Step 6에서 영어 전환 가능 |
| 스크린샷 | Jina Reader + PIL crop | Playwright fallback 자동 (설치 시) |
| design.md 파일명 | `design.md` | Step 5에서 변경 가능 |
| 출력 경로 | `insane-design/{slug}/` | Step 1에서 변경 가능 |
| tokens.json 경로 | `insane-design/{slug}/tokens.json` | Export `--output`으로 변경 가능 |
