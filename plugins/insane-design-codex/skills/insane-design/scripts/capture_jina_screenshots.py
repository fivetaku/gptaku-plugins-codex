#!/usr/bin/env python3
"""Capture screenshots for all services using Jina Reader API.

Jina Reader: r.jina.ai/{URL} with X-Respond-With: screenshot
- No API key required
- 500 RPM free
- Puppeteer-based real browser rendering
- Bypasses bot detection, cookie banners, Cloudflare

Usage:
    python3 scripts/capture_jina_screenshots.py           # all missing
    python3 scripts/capture_jina_screenshots.py stripe     # single
    python3 scripts/capture_jina_screenshots.py --all      # force all
"""
import json
import subprocess
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path.cwd()  # $WORK_DIR에서 실행됨

SLUG_URL_MAP = {
    "atlassian": "https://atlassian.com",
    "axiom": "https://axiom.co",
    "cal": "https://cal.com",
    "clerk": "https://clerk.com",
    "contentful": "https://contentful.com",
    "convex": "https://convex.dev",
    "discord": "https://discord.com",
    "dub": "https://dub.co",
    "figma": "https://figma.com",
    "framer": "https://framer.com",
    "github": "https://github.com",
    "hashnode": "https://hashnode.com",
    "lemon-squeezy": "https://lemonsqueezy.com",
    "linear": "https://linear.app",
    "mintlify": "https://mintlify.com",
    "neon": "https://neon.tech",
    "notion": "https://notion.so",
    "planetscale": "https://planetscale.com",
    "posthog": "https://posthog.com",
    "prisma": "https://prisma.io",
    "railway": "https://railway.app",
    "raycast": "https://raycast.com",
    "resend": "https://resend.com",
    "retool": "https://retool.com",
    "shopify": "https://shopify.com",
    "slack": "https://slack.com",
    "spotify": "https://spotify.com",
    "stripe": "https://stripe.com",
    "supabase": "https://supabase.com",
    "tailwindcss": "https://tailwindcss.com",
    "tinybird": "https://tinybird.co",
    "twitch": "https://twitch.tv",
    "vercel": "https://vercel.com",
    "warp": "https://warp.dev",
    "planetfall": "https://www.paradoxinteractive.com/games/age-of-wonders-planetfall/about",
}


def capture_jina(slug: str, url: str) -> dict:
    """Capture screenshot via Jina Reader API."""
    out_dir = ROOT / "insane-design" / slug / "screenshots"
    out_dir.mkdir(parents=True, exist_ok=True)

    result = {"slug": slug, "url": url, "ok": False, "error": None, "size": 0}

    try:
        r = subprocess.run(
            [
                "curl", "-sL",
                "-H", "X-Respond-With: screenshot",
                "-H", "X-Wait-For: 5000",
                "--max-time", "45",
                f"https://r.jina.ai/{url}",
            ],
            capture_output=True,
            timeout=50,
        )
        if r.returncode != 0:
            result["error"] = f"curl exit {r.returncode}"
            return result

        data = r.stdout
        if len(data) < 5000 or not data[:4] == b'\x89PNG':
            result["error"] = f"not PNG or too small ({len(data)} bytes)"
            return result

        (out_dir / "jina-hero.png").write_bytes(data)

        # Crop: 1280×1280 → 1280×800 (상단 유지, 하단 잘라냄)
        try:
            from PIL import Image
            src = out_dir / "jina-hero.png"
            dst = out_dir / "hero-cropped.png"
            img = Image.open(src)
            w, h = img.size
            crop_h = min(800, h)
            cropped = img.crop((0, 0, w, crop_h))
            cropped.save(dst)
        except ImportError:
            pass

        result["ok"] = True
        result["size"] = len(data)
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    args = sys.argv[1:]
    force_all = "--all" in args
    args = [a for a in args if a != "--all"]

    if args:
        slugs = args
    elif force_all:
        slugs = list(SLUG_URL_MAP.keys())
    else:
        # Only missing
        slugs = []
        for slug in SLUG_URL_MAP:
            jina_file = ROOT / "insane-design" / slug / "screenshots" / "jina-hero.png"
            if not jina_file.exists():
                slugs.append(slug)
        if not slugs:
            print("All Jina screenshots already captured. Use --all to force.")
            return

    print(f"Capturing {len(slugs)} services via Jina Reader (5 concurrent)…")

    results = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {ex.submit(capture_jina, slug, SLUG_URL_MAP[slug]): slug for slug in slugs}
        for i, fut in enumerate(as_completed(futures), 1):
            r = fut.result()
            status = "✓" if r["ok"] else "✗"
            sz = f"{r['size']//1024}KB" if r["ok"] else r["error"]
            print(f"  [{i}/{len(slugs)}] {status} {r['slug']:15s} {sz}")
            results.append(r)

    ok = sum(1 for r in results if r["ok"])
    fail = sum(1 for r in results if not r["ok"])
    print(f"\nDone: {ok} success, {fail} failed")
    if fail:
        print("Failed:")
        for r in results:
            if not r["ok"]:
                print(f"  {r['slug']}: {r['error']}")


if __name__ == "__main__":
    main()
