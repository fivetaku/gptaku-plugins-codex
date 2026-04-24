---
name: docs-guide
description: Fetch and explain official documentation for libraries, frameworks, and tools using llms.txt-first retrieval and official-source fallbacks. Use when the user wants official docs, version-aware references, or an explanation grounded in primary documentation.
---

# docs-guide for Codex

Read these first:
- `references/knowledge-base.md`

Load as needed:
- `references/llms-txt-sites.md`
- `references/fallback-strategies.md`

Use this skill when the user explicitly wants official documentation, version-aware behavior, or source-backed answers about a library or framework.

## Codex Workflow

1. Identify the library, tool, and topic from the user request.
2. Inspect local dependency files when they exist to infer version:
   - `package.json`
   - `requirements.txt`
   - `pyproject.toml`
   - `go.mod`
   - `Cargo.toml`
3. Ask at most one clarification if the library is ambiguous.
4. Prefer official documentation routes in this order:
   - known `llms.txt` site from `references/llms-txt-sites.md`
   - likely `llms.txt` on the official site
   - official GitHub docs source
   - `sitemap.xml` or platform-specific index
   - official-domain search only as a last resort
5. Summarize only the relevant section.
6. Include the source URL and, when possible, the inferred version and retrieval method.

## Guardrails

- Prefer official sources over secondary summaries.
- For OpenAI products, rely on official OpenAI docs only.
- Do not answer from memory alone if the request is version-sensitive or asks for official docs.
- If official docs cannot be confirmed, say so plainly.
