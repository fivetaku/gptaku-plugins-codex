---
name: insane-search
description: Auto-bypass for blocked or difficult URLs using a generic fetch engine, public APIs, RSS, Jina, TLS impersonation, and optional local Playwright templates. Use when normal search/fetch paths fail, or when the user needs content from X, Reddit, Medium, LinkedIn, Naver, Coupang, YouTube, or other WAF-heavy platforms.
---

# Insane Search for Codex

Read these first:
- `references/fallback.md`

Load platform references only when relevant:
- `references/twitter.md`
- `references/naver.md`
- `references/media.md`
- `references/json-api.md`
- `references/public-api.md`
- `references/rss.md`
- `references/metadata.md`
- `references/tls-impersonate.md`
- `references/playwright.md`
- `references/cache-archive.md`

Use this skill only when ordinary `web` access is blocked, incomplete, or clearly the wrong tool for the platform. For simple current searches that `web.search_query` and `web.open` can answer directly, start there instead.

## Codex Workflow

1. For keyword-only requests, acquire URLs first with `web.search_query` or a platform API route from the references.
2. For blocked or hard URLs, use the engine wrapper:
   `bash scripts/run_engine.sh "<url>" [--selector "<css>"] [--device auto|desktop|mobile] [--trace]`
3. If Python or local browser dependencies are missing, check them with:
   `bash scripts/bootstrap.sh`
   Add `--install` only when you intentionally want the script to install missing packages.
4. Treat the engine as the single generic entrypoint. Do not re-implement its WAF logic ad hoc.
5. For R7-style API-first recon on JS-heavy sites, use:
   `node scripts/playwright_recon.js <<'EOF'`
   `{"url":"https://example.com","timeout":20000}`
   `EOF`
6. If you touch engine code, run:
   - `python3 engine/bias_check.py`
   - `bash scripts/smoke_test.sh`
7. Keep the no-site-name rule intact. Site-specific behavior belongs in runtime hints or the reference docs, not in `engine/**`.

## Port Notes

- Prefer local Node templates under `engine/templates/` when Node and Chrome are available, and use `scripts/playwright_recon.js` for network-request discovery.
- If local browser fallback is unavailable, report the limitation and continue with the generic engine, Jina, archive, or platform-API routes.
- Prefer deterministic evidence over prose. When the engine fails, surface the trace summary and the next-best route.
