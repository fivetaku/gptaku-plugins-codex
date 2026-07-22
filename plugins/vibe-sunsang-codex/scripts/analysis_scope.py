#!/usr/bin/env python3
"""
바선생 분석 범위 계산기 (증분 워터마크 + 마지막-활동 기준 필터).

문제: 기존 스킬은 파일명(세션 *시작일*) 기준으로 범위를 잡아, 오래전 시작해
이번 주에 이어간 세션을 놓쳤고, "지난 분석 이후 새로 생긴 것만" 개념이 없었다.

해결: 각 변환 md의 frontmatter `end`(마지막 활동)를 활동 시각으로 삼는다.
- `--new`  : analysis_state.json의 last_analyzed_at 이후로 활동한 세션.
             (start > watermark = 신규, start <= watermark < end = 이어짐 → 둘 다 포착)
- `--window-days N` : 최근 N일 내 활동한 세션.
- `--mark` : 대상 세션들의 최대 end로 워터마크를 갱신한다.

출력: 매칭 세션의 md 경로 목록 + 마지막 줄 SUMMARY.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


def parse_frontmatter(md_path: Path) -> dict:
    """md 파일 상단 --- ... --- 프론트매터를 얕게 파싱."""
    fm: dict = {}
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            first = f.readline()
            if first.strip() != "---":
                return fm
            for line in f:
                if line.strip() == "---":
                    break
                if ":" in line and not line.startswith((" ", "-", "\t")):
                    key, _, val = line.partition(":")
                    fm[key.strip()] = val.strip()
    except OSError:
        pass
    return fm


def to_dt(s: str):
    """'YYYY-MM-DD HH:MM' 또는 'YYYY-MM-DD'를 aware datetime(UTC)으로."""
    if not s:
        return None
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def collect_sessions(conv_dir: Path) -> list:
    """conversations/*/*.md 세션들의 (path, start, end, project, messages) 수집."""
    out = []
    for md in sorted(conv_dir.rglob("*.md")):
        if md.name == "INDEX.md":
            continue
        fm = parse_frontmatter(md)
        start = to_dt(fm.get("start") or fm.get("date", ""))
        end = to_dt(fm.get("end") or fm.get("start") or fm.get("date", ""))
        out.append({
            "path": str(md),
            "project": fm.get("project", md.parent.name),
            "start": start,
            "end": end,
            "messages": int(fm.get("messages", "0") or 0),
        })
    return out


def load_state(state_file: Path) -> dict:
    if state_file.exists():
        try:
            return json.load(open(state_file, encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def main() -> int:
    ap = argparse.ArgumentParser(description="바선생 분석 범위 계산기")
    ap.add_argument("--conversations-dir", type=Path,
                    default=Path.home() / "vibe-sunsang" / "conversations")
    ap.add_argument("--state-file", type=Path,
                    default=Path.home() / "vibe-sunsang" / "config" / "analysis_state.json")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--new", action="store_true",
                       help="지난 분석 이후 활동한 세션만")
    group.add_argument("--window-days", type=int, default=None,
                       help="최근 N일 내 활동한 세션만")
    ap.add_argument("--now", type=str, default=None,
                    help="기준 시각(테스트용, 'YYYY-MM-DD HH:MM'). 기본: 현재 UTC")
    ap.add_argument("--mark", action="store_true",
                    help="대상 세션의 최대 end로 워터마크 갱신")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    conv_dir = args.conversations_dir.expanduser()
    if not conv_dir.exists():
        print("SUMMARY total=0 matched=0 new=0 continued=0 watermark=none")
        return 0

    now = (to_dt(args.now) if args.now else None) or datetime.now(timezone.utc)
    sessions = collect_sessions(conv_dir)
    state = load_state(args.state_file.expanduser())
    watermark = to_dt(state.get("last_analyzed_at", ""))

    matched = []
    new_count = continued_count = 0
    for s in sessions:
        act = s["end"] or s["start"]
        if act is None:
            continue
        keep = False
        if args.window_days is not None:
            keep = act >= now - timedelta(days=args.window_days)
        elif args.new:
            keep = watermark is None or act > watermark
        else:
            keep = True  # 범위 미지정 → 전체
        if keep:
            matched.append(s)
            if args.new and watermark is not None and s["start"] and s["start"] <= watermark:
                continued_count += 1
            else:
                new_count += 1

    for s in matched:
        print(s["path"])

    # 워터마크 갱신
    new_watermark = state.get("last_analyzed_at", "")
    if args.mark:
        ends = [s["end"] for s in sessions if s["end"]]
        if ends:
            mx = max(ends)
            new_watermark = mx.strftime("%Y-%m-%d %H:%M")
            state["last_analyzed_at"] = new_watermark
            args.state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(args.state_file, "w", encoding="utf-8") as f:
                json.dump(state, f, ensure_ascii=False, indent=2)

    wm = watermark.strftime("%Y-%m-%d %H:%M") if watermark else "none"
    if args.json:
        print(json.dumps({
            "total": len(sessions),
            "matched": len(matched),
            "new": new_count,
            "continued": continued_count,
            "watermark_before": wm,
            "watermark_after": new_watermark or "none",
        }, ensure_ascii=False))
    print(f"SUMMARY total={len(sessions)} matched={len(matched)} "
          f"new={new_count} continued={continued_count} watermark={wm}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
