# insane-search-codex

Codex marketplace package for the `insane-search` skill — adaptive access for blocked / WAF-heavy URLs.

Included skills:
- `insane-search` — generic WAF-profile fetch chain (curl_cffi TLS impersonation, mobile URL
  transforms, local Playwright fallback) plus Phase 0 platform APIs (yt-dlp, Jina, public APIs)
  and 12 platform/diagnostic references. Full parity with the upstream Claude plugin (v0.5.1),
  ported to Codex idiom.

Entry points:
- `bash scripts/run_engine.sh "<URL>" [--selector "<CSS>"] [--device auto|desktop|mobile] [--trace]`
  (= `python3 -m engine "<URL>" ...`)
- `bash scripts/bootstrap.sh [--install]` — check / install Python + Node prerequisites
- `node scripts/playwright_recon.js` — R7 API-first network-request discovery
- `bash scripts/smoke_test.sh` — bias linter + smoke tests (run after touching `engine/**`)

Packaging notes:
- Harness rules R1–R7, Phase 0→3 scheduler, 4-layer validation, and the No-Site-Name rule are all
  carried over in `skills/insane-search/SKILL.md`.
- The smoke tests run under both `pytest` and direct script execution.
