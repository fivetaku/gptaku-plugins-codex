# WebFetch Prompt Templates (v1.3.3)

Standard prompts for fetching documentation indices and detail pages.

The verb that matters: **EXTRACT**, never **GENERATE** or **INVENT**.

---

## Template 1 — href extraction from index page

Use when fetching `llms.txt` or root docs index to find detail URLs.

```text
Extract only actual href URLs present in this index/page that are relevant to:
{user_question}

Return JSON array:
[
  {
    "title": "...",
    "url": "exact href, unchanged",
    "source_section": "...",
    "why_relevant": "...",
    "source_type_guess": "overview|reference|pricing|changelog|cookbook|unknown"
  }
]

Rules:
- Do not invent, normalize, shorten, or natural-language-convert URLs.
- Preserve suffixes such as preview, beta, canary, experimental, latest, exp, dev, rc.
- Preserve version numbers and date stamps in URLs unchanged.
- If no relevant href exists, return [] and say no actual href found.
- If multiple candidates match, rank by exact token/title overlap with the question.
```

**Why this matters**: LLMs given a free-form prompt about "Gemini 3.5 Pro" tend to *generate* a plausible URL like `/models/gemini-3.5-pro`. The actual URL may be `/models/gemini-3-pro-preview` — preview suffix is unguessable.

---

## Template 2 — detail page extraction (spec-level)

Use after Template 1 returns hrefs and you fetch each detail page.

```text
Extract from this documentation page the following specific facts:
{list of claims needed, e.g., "model ID string", "context window in tokens",
 "input price per 1M tokens", "deprecation date if any"}

Return JSON:
{
  "url_fetched": "...",
  "claims": {
    "{claim_name}": "{exact_value_from_page or 'not_found'}",
    ...
  },
  "verbatim_quotes": ["...short quote backing each claim..."],
  "page_freshness_signal": "last-updated date / version number / 'no signal'"
}

Rules:
- Do not synthesize values from related context. If the page does not state a value, return "not_found".
- Quote sources verbatim — do not paraphrase numerical values.
- If a claim has multiple values (e.g., different tiers), return the one closest to the user's question context, and list alternatives in `verbatim_quotes`.
```

---

## Template 3 — multi-source cross-validation (spec-level)

Use when the question requires high-stakes accuracy (pricing, deprecation, latest).
Fetch 2+ source types and compare.

```text
Compare the following spec claims across sources:
- Source A (model reference): {url_a}
- Source B (release notes / pricing / changelog): {url_b}

For each claim:
{list of claims}

Return JSON:
{
  "{claim_name}": {
    "source_a_value": "...",
    "source_b_value": "...",
    "agree": true|false,
    "source_to_trust": "A|B|unknown",
    "rationale": "why one source is more authoritative for this claim"
  }
}

Authority rules:
- Pricing → pricing page > model reference > release notes
- Deprecation → deprecation/changelog > model reference
- Model ID → model reference > cookbook > marketing
- Release date → release notes > model reference
- Region availability → API reference > docs index
```

---

## Anti-patterns (NEVER do)

- "Find the URL for {natural model name}" — implies generation
- "What is the URL of the {feature} page?" — implies guessing
- Free-form "extract any relevant info" — produces hallucinations on uncovered fields
- Fetching detail page WITHOUT pre-defined claim list — model may invent answers

## OK patterns (always do)

- "Extract actual href URLs only..."
- "Extract these specific claims; if not present, return 'not_found'..."
- "Quote verbatim..."
- Pre-define the JSON schema and exact claim names

---

## When to use which template

| Scenario | Template |
|----------|----------|
| User asks general "how to use X" | Skip — fetch single relevant page |
| User asks "최신 / latest / newest" | T1 → T2 (multiple detail pages) |
| User asks model ID / pricing / deprecation | T1 → T2 → T3 (multi-source) |
| User asks comparison across providers | T1 (per provider) → T2 → T3 |
| User asks single API how-to with version | T1 → T2 (single detail) |
