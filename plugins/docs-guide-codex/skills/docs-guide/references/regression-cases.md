# Regression Cases (v1.3.3)

Golden cases that previously broke docs-guide. Manual smoke test before each release.

When updating the skill, run through these and confirm correct behavior.

---

## Case 1 — "Gemini 최신 모델"

**Trigger**: 사용자가 "Gemini 최신 모델 알려줘" / "what's the latest Gemini model"

**Past failure mode**:
- Fetched `ai.google.dev/gemini-api/docs/llms.txt` (index)
- Saw model names listed but no detail pages fetched
- Returned "확인 필요" or guessed natural URL like `gemini-3-flash` → 404

**Expected behavior (v1.3.3)**:
1. Detect spec-level trigger ("최신 / latest")
2. Fetch `gemini-api/docs/llms.txt` index
3. Extract actual hrefs (not generate) — preserves `*-preview` suffix
4. Fetch model overview detail page + release notes/changelog (cap=5 for "latest")
5. Cite detail page URL in answer
6. Cross-check release date between model reference and changelog if disagreement

**Validation**:
- Answer cites at least 2 URLs (overview + detail OR detail + changelog)
- All cited URLs are 200 OK on fetch (no guessing)
- Exact model ID string is verbatim from detail page

---

## Case 2 — Preview/beta suffix model IDs

**Trigger**: 모델 비교 / API integration 질문 (e.g., "Codex 4.7 사용법", "OpenAI o1-preview vs o1")

**Past failure mode**:
- Generated `claude-4.7` or `o1-mini` from natural reading
- Actual ID has suffix: `claude-opus-4-7`, `o1-preview-2024-09-12`
- 404 on guessed URL or wrong API call example

**Expected behavior**:
1. Trigger spec-level (exact API identifier)
2. Extract model IDs from `developers.openai.com/api/docs/llms.txt` or `platform.codex.com/llms.txt`
3. Use Template 2 (detail extraction) with claim "exact model ID string"
4. Verbatim quote in answer

**Validation**:
- Answer contains `claude-opus-4-7` (not `claude-4.7`) verbatim
- API code example uses exact ID string

---

## Case 3 — Pricing query

**Trigger**: "GPT-4o 가격" / "Codex Opus pricing per token"

**Past failure mode**:
- Quoted from training data (stale), or
- Fetched only model overview page, missed pricing page

**Expected behavior**:
1. Trigger spec-level (pricing)
2. Fetch llms.txt → extract model page + pricing page hrefs
3. Cross-validate (Template 3): model reference vs pricing page
4. If disagreement, prefer pricing page
5. Cite both URLs + page freshness signal

**Validation**:
- At least 2 sources cited
- Numerical values quoted verbatim (no rounding/approximation)
- Page freshness mentioned ("Pricing page updated YYYY-MM-DD")

---

## Case 4 — Deprecation date / sunset

**Trigger**: "GPT-4 언제 deprecated 돼?" / "Codex 3 sunset date"

**Past failure mode**:
- Guessed from "everyone says 6 months"
- Or fetched cookbook (not authoritative for deprecation)

**Expected behavior**:
1. Spec-level (deprecation date)
2. Authority chain: deprecation/changelog > model reference > cookbook
3. If no explicit date in docs, return "not_found" — do NOT estimate

**Validation**:
- Cite changelog/deprecation page URL (not generic docs)
- If date absent, answer says "공식 문서에 명시된 deprecation 날짜 없음" (not "probably 6 months")

---

## Case 5 — Context window / token limit

**Trigger**: "Codex Opus context window" / "Gemini 1.5 Pro 토큰 제한"

**Past failure mode**:
- Numeric value invented (e.g., "200K tokens" without source)
- Confusion between input limit / output limit / total context

**Expected behavior**:
1. Spec-level (token limit, context window)
2. Use Template 2 with claim list: ["context window", "max input tokens", "max output tokens"]
3. If page distinguishes input/output, report both separately

**Validation**:
- Each numeric value has verbatim quote
- input/output/total are not conflated

---

## Case 6 — Endpoint compatibility

**Trigger**: "OpenAI Responses API에서 X 가능?" / "Codex Messages API supports vision?"

**Past failure mode**:
- Assumed all endpoints support all features (false)
- Fetched generic docs without endpoint-specific page

**Expected behavior**:
1. Spec-level (endpoint compatibility, modality support)
2. Fetch endpoint-specific page (e.g., `/api-reference/responses` not generic `/api`)
3. If feature support matrix exists, quote it

**Validation**:
- URL fetched is endpoint-specific (path includes endpoint name)
- Answer addresses YES/NO/PARTIAL with quote

---

## Case 7 — Migration / breaking changes

**Trigger**: "Next.js 14 → 15 마이그레이션" / "React 18 to 19 breaking changes"

**Past failure mode**:
- Listed generic improvements, missed specific breaking changes
- Quoted blog posts instead of official migration guide

**Expected behavior**:
1. Spec-level (migration, breaking changes)
2. Fetch official migration guide (priority) + changelog
3. List BREAKING items separately from features

**Validation**:
- At least one URL is migration guide or release notes (not blog/tutorial)
- Breaking changes explicitly labeled

---

## Case 8 — Index returns marketing page (e.g., Neo4j)

**Trigger**: 새로운 라이브러리 spec 질문 + llms-txt-sites.md에 marketing 라벨 있음

**Past failure mode**:
- Fetched llms.txt → got marketing page → answered with marketing fluff

**Expected behavior**:
1. Check llms-txt-sites.md for ⚠️ markers
2. If marketing index, skip llms.txt and go directly to fallback (sitemap, GitHub, etc.)
3. Answer cites real docs URL, not marketing

**Validation**:
- For Neo4j: cited URL is `neo4j.com/docs/`, not `neo4j.com/llms.txt` content

---

## Manual smoke test procedure

Before bumping version:

```
For each case 1-8:
  1. Run docs-guide with the trigger query
  2. Inspect answer:
     - All cited URLs return 200 (curl check)
     - Source URLs are detail pages, not just index
     - Exact strings/numbers are verbatim quotes
  3. PASS/FAIL flag
```

If any case fails → fix the skill, re-test, re-run all 8 cases. Don't ship with regression.
