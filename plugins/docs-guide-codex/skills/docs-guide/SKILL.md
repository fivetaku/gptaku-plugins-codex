---
name: docs-guide
description: Fetch and explain official documentation for any library, framework, or service — triggers on questions like "How do I…", "What is…", "공식 문서", "문서 기반으로", version-specific or spec-level queries. Covers everything except Claude Code / Claude Agent SDK / Claude API (those go to claude-code-guide).
---

# docs-guide for Codex

Read these first:
- `references/llms-txt-sites.md`
- `references/fallback-strategies.md`

Load on demand (spec-level or WebFetch workflow questions):
- `references/webfetch-prompts.md`
- `references/regression-cases.md`

---

## Scope

Everything EXCEPT Claude Code, Claude Agent SDK, and Claude API (handled by the built-in claude-code-guide agent).

Trigger on:
- "How do I…", "What is…", "How does X work", "Best practice for…" about any library or framework
- Explicit doc requests — "공식문서", "official docs", "문서 기반으로", "docs에서 확인해줘"
- Version-sensitive or spec-level questions about external libraries

---

## Clarification — docs-guide is minimal-interview

This plugin mostly needs just two facts: **library** and **topic**.

Per `shared/questioning-policy.md` §2c — if the user already named the library and topic, proceed immediately without asking anything.

If the library OR topic is genuinely ambiguous (e.g., "Router" with no project context), ask exactly ONE numbered-option question per §A below, then proceed.

### §A — Numbered-option format (Codex CLI — no AskUserQuestion)

Codex CLI has no card UI. When you must ask, output a chat block:

```
질문: <한 줄 질문>
1. <추천안> — 무엇인지, 왜 이걸 추천하는지
2. <대안> — 무엇인지, 트레이드오프
3. 직접 입력 (문장으로 말씀해 주세요)
```

- Recommended option always goes first (1번).
- Multi-pick → "여러 개면 `1,3`처럼 적어주세요."
- Never ask more than once; if still unclear, proceed with the most likely interpretation.

---

## Step 0 — Project Context Detection

Before fetching, quickly scan local dependency files to detect library version:

```
package.json, requirements.txt, pyproject.toml, go.mod, Cargo.toml, pom.xml, build.gradle
```

Use this for:
- **Version detection**: `"react": "^19.0.0"` → fetch React 19 docs
- **Disambiguation**: project has both `react-router-dom` and `express`, user asks "Router" → resolve silently

Skip this step if the question already names a specific library and version.

---

## Intent Classification (Smart Broad)

### FETCH (external lookup needed)
- Library/framework APIs, configuration, features
- Setup/installation, migration guides, breaking changes
- API reference (endpoints, parameters, return types)
- Questions where wrong info causes bugs (auth, payments, DB queries)
- Explicit doc requests

### SKIP (answer from knowledge)
- Basic language syntax (Python for loop, JS array methods)
- General CS concepts (REST, closures)
- Architecture discussions not tied to a specific library version

### DISAMBIGUATE
- Generic term maps to multiple libraries ("Router", "ORM", "auth", "store")
- Check Step 0 first; if still ambiguous, ask one §A question

When unsure between FETCH and SKIP, answer from knowledge first, then offer: "공식 문서도 확인해볼까요?"

---

## Version Awareness

1. **Project context first** — check Step 0
2. **User mention** — "React 19", "Django 5.0"
3. **Normalize** — `react 18`, `React v18`, `@18`, `^18.2.0` → all mean React 18.x
4. **Version-specific URLs** — Next.js `/docs/14/`, Django `/en/5.0/`, Python `/3.12/library/`
5. **Default** — latest stable; note which version was used

Common pitfalls:

| Situation | Risk | Action |
|-----------|------|--------|
| "React" without version | React 18 vs 19 differ significantly | Check package.json first |
| Library has LTS and current | User may need LTS-specific docs | Ask if unclear |
| Pre-release/canary docs | May contain unstable APIs | Warn user |
| Archived docs (e.g., CRA) | Deprecated project | Note it |

---

## Documentation Retrieval Strategy

### Step 1 — Check known llms.txt sites

Load `references/llms-txt-sites.md`. If the library is listed, use that URL directly.

### Step 2 — Try llms.txt on the official site

If not in the known list:
1. If you know the official docs domain → try llms.txt directly
2. If unsure → search for `{library name} official site` to find the domain
3. Try in order:
   - `{official-site}/llms.txt`
   - `{official-site}/docs/llms.txt`
   - `{official-site}/llms-full.txt`

If llms.txt exists:
- Read the index to find relevant page URLs
- Fetch the specific page(s) for the user's question
- **URL fix**: if a linked URL ends in `.md` but returns 404, retry without `.md`

### Step 3 — Fallback strategies (no llms.txt)

Load `references/fallback-strategies.md` and try in order:

**3a. Per-technology strategy** — 40+ technologies with best known URLs

**3b. GitHub raw markdown** (most reliable for OSS):
- Search: `{library name} documentation site:github.com`
- Try: `https://raw.githubusercontent.com/{owner}/{repo}/main/docs/{topic}.md`
- Branch fallback: `main` → `master` → version branches (e.g., `8.17`)

**3c. sitemap.xml** (universal fallback):
- Fetch `{official-site}/sitemap.xml`
- Filter for `/docs/`, `/guide/`, `/reference/` patterns
- Fetch the most relevant page

**3d. Platform-specific signals**:
- `/search/search_index.json` → MkDocs (full page text)
- `/objects.inv` → Sphinx

**3e. Search** (last resort):
- Search `{library name} official documentation {topic}`
- Prefer official domains over tutorials/blogs
- Tell the user which method was used

---

## Spec-Level Drill-Down Requirement (v1.3.3)

For these question types, fetching only the index/overview page is **INSUFFICIENT**. You MUST fetch the per-item detail page.

### Spec-level triggers
- "최신 / 현재 / newest / latest" model, version, release
- Exact API identifiers (model IDs, function names, env var names, parameter names)
- Pricing, token limits, rate limits, quota, deprecation dates
- Context window / max tokens / output limit
- Region availability / preview vs GA / tier availability
- Endpoint compatibility (Responses API, Chat Completions, Batch, embeddings)
- Modalities / tool support (vision, audio, structured output, function calling)
- SDK / package version / migration / breaking changes
- Request parameter names / response schema fields
- Default model 변경 / sunset date / release date / "deprecated" / "legacy"
- Feature support matrix ("X 지원하나?", "Y 가능?")

### Drill-down protocol

Load `references/webfetch-prompts.md` before fetching spec-level pages.

1. Fetch the index/overview page (llms.txt or root docs)
2. If the question matches any spec-level trigger above, do NOT stop here
3. From the index, **extract actual href URLs** for each relevant item
   - Use Template 1 from `references/webfetch-prompts.md`
   - Do NOT guess URLs from natural names — `*-preview`, `*-beta`, `*-canary`, `*-experimental` suffixes are unguessable
4. Fetch each detail page (claim-type-bounded cap below)
5. Cite the **detail page URL** in the answer, not just the index

### Drill-down cap

| Question class | Index | Detail max |
|---|---|---|
| general how-to | 1 | 1-2 |
| spec single target | 1 | 3 |
| latest / current 질문 | 1 | 5 (overview + changelog + pricing/deprecation) |
| matrix / comparison | up to 8 total | 3 per provider |
| 30+ candidates | rank by exact token/title/href match → top 5-8 | only those needed for claim |

**Stop condition**: each exact claim in the answer (model ID, price, date, availability, schema) has at least one detail-page source.

---

## Quality Gate

### General questions
- Minimum: at least 1 official URL actually fetched + 1 specific fact or code example from that source

### Spec-level questions
- **1 index/overview URL** (proves item exists in current docs)
- **1 detail page URL per item** being answered about (proves the spec)
- If detail page returns 404 → extract hrefs from index using Template 1, **NOT** guess
- If guessing was used and failed, output MUST flag: `⚠️ URL 추측 — 검증 안 됨` and answer must say "공식 문서에서 확인하지 못했습니다"

### Self-reflection checklist (before sending answer for spec-level questions)
- [ ] Index URL was actually fetched (not just from memory)
- [ ] Detail page was fetched for every exact claim in the answer
- [ ] All URLs were extracted from real hrefs, not guessed from natural names
- [ ] Source citation shows detail URL(s), not just index

If any unchecked → backtrack to drill-down step or downgrade answer to "확인하지 못함".

### Insufficient evidence fallback
"공식 문서에서 확인하지 못했습니다. 내부 지식 기반으로 답변합니다." / "Could not verify from official docs. Answering from knowledge."

### User feedback handling
- "이 문서 아니야" / "wrong docs" → immediately try next fallback strategy
- "코드만 보여줘" / "just show code" → switch to code-only output mode
- "더 자세히" / "more detail" → fetch additional pages from the same docs

---

## Disambiguation Patterns

When a query maps to multiple libraries:

### By project context
- "Router" in React project → `react-router-dom`
- "Router" in Express project → `express.Router`
- "ORM" in Python → check for `sqlalchemy`, `django`, `tortoise-orm`
- "auth" → `next-auth`, `passport`, `firebase-auth`, `supabase-auth` etc.

### Ecosystem conventions
- "middleware" in Next.js → `middleware.ts` (edge middleware)
- "middleware" in Express → `app.use()` pattern
- "store" in Vue → Pinia (modern) or Vuex (legacy)
- "state management" in React → useState/useReducer (built-in) or Zustand/Redux

---

## Known Limitations

### JS-rendered doc sites
- `developer.apple.com` (SwiftUI, UIKit) → answer from knowledge, provide official URL
- `docs.oracle.com` (Java SE) → answer from knowledge

### Marketing llms.txt
- `neo4j.com/llms.txt` → marketing index, not Cypher/docs. Use `neo4j.com/docs/` directly.

---

## Error Handling

| Situation | Action |
|-----------|--------|
| llms.txt returns 404 | Silently try next URL pattern, then fall back |
| llms.txt linked URL returns 404 | Strip `.md` extension and retry |
| Specific doc path 404 | Try parent path for table of contents |
| GitHub `main` branch 404 | Try `master`, then version-specific branches |
| WebFetch returns empty/JS content | Try GitHub source or answer from knowledge |
| Item in index but detail URL unknown | Re-fetch index with Template 1 from `references/webfetch-prompts.md` — never guess |
| 404 on guessed URL (spec-level) | STOP guessing. Re-fetch parent index, extract actual hrefs. If still no result → "확인하지 못함" |
| No documentation found | Inform user, answer from knowledge, suggest they provide the docs URL |

---

## Retrieval Optimization

1. **Index first** — always fetch `llms.txt` (index) before `llms-full.txt`
2. **Targeted fetch** — from index, identify the single most relevant page URL
3. **Section extraction** — extract only the relevant section; do not dump entire page
4. **Progressive depth** — if user asks "더 자세히", fetch additional pages
5. **Multi-page max** — 3 pages for broad topics; summarize connections

---

## Response Rules

1. **Language** — match the user's language (Korean → Korean, English → English)
2. **Source citation** — ALWAYS include documentation URL(s) at the end with "Source:" label
3. **Method transparency** — note retrieval method (llms.txt / GitHub / sitemap / WebSearch)
4. **Code examples** — include them when the official docs provide them
5. **Version note** — note the version (e.g., "React 19 기준", "as of Next.js 15")
6. **Conciseness** — answer the specific question; don't dump entire pages

## Output Format

### Default mode

```
[Explanation based on official documentation]

[Code examples if relevant]

---
Source: [URL(s) fetched]
(version: X.Y | method: llms.txt/GitHub/sitemap/WebSearch)
```

### Code-only mode (when user asks for code)

```
[Code examples with minimal inline comments]

---
Source: [URL(s)]
```
