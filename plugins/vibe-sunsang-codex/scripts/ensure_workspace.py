#!/usr/bin/env python3
"""
바선생 워크스페이스 상태 보증기 (self-healing).

모든 스킬(retro/mentor/growth/onboard)의 Step 0에서 호출한다.
- v2 레이아웃(config/ conversations/ exports/ growth-log/)을 보장한다.
- v1 번호 접두사 레이아웃(10-scripts/ 30-growth-log/ 40-conversations/ 90-exports/)이
  감지되면 데이터를 비파괴적으로 이관한다. **기존 파일은 절대 덮어쓰지 않는다.**
- v1 config(10-scripts/*.json)를 config/로 이관한다 — 구 onboard 마이그레이션이
  누락하던 유실 결함을 여기서 수정한다.

출력(마지막 줄, `--json` 시 JSON):
  STATUS <fresh|v2|v1_migrated>  CONFIG <present|absent>
호출부(스킬)는 이 한 줄만 보면 초기설정 여부를 판단할 수 있다.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

V1_DATA_DIRS = {
    "40-conversations": "conversations",
    "90-exports": "exports",
    "30-growth-log": "growth-log",
}
V1_CONFIG_DIR = "10-scripts"
CONFIG_FILES = ("project_names.json", "workspace_types.json")


def merge_move(src: Path, dst: Path, actions: list) -> None:
    """src의 모든 파일을 dst로 이동한다. dst에 이미 있는 파일은 건드리지 않는다."""
    if not src.exists():
        return
    for item in sorted(src.rglob("*")):
        if item.is_dir():
            continue
        rel = item.relative_to(src)
        target = dst / rel
        if target.exists():
            continue  # 비파괴: 기존 데이터 보존
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(item), str(target))
        actions.append(f"move {item} -> {target}")


def ensure(base: Path) -> dict:
    base = base.expanduser()
    actions: list = []

    # v2 표준 디렉토리 보장
    for d in ("config", "conversations", "exports", "growth-log/weekly"):
        p = base / d
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
            actions.append(f"mkdir {p}")

    # v1 데이터 디렉토리 이관 (비파괴 병합)
    for old, new in V1_DATA_DIRS.items():
        old_p = base / old
        if old_p.exists():
            merge_move(old_p, base / new, actions)

    # v1 config 이관 — 복사(원본은 백업으로 보존)
    for name in CONFIG_FILES:
        src = base / V1_CONFIG_DIR / name
        dst = base / "config" / name
        if src.exists() and not dst.exists():
            shutil.copy2(str(src), str(dst))
            actions.append(f"copy {src} -> {dst}")

    # 데이터를 옮기고 비어버린 v1 디렉토리 정리 (비어있을 때만 rmdir)
    for old in V1_DATA_DIRS:
        old_p = base / old
        if old_p.exists():
            for sub in sorted(old_p.rglob("*"), reverse=True):
                if sub.is_dir() and not any(sub.iterdir()):
                    sub.rmdir()
            if not any(old_p.iterdir()):
                old_p.rmdir()
                actions.append(f"rmdir empty {old_p}")

    migrated = any(a.startswith(("move ", "copy ")) for a in actions)
    config_present = any((base / "config" / n).exists() for n in CONFIG_FILES)

    if migrated:
        status = "v1_migrated"
    elif config_present:
        status = "v2"
    else:
        status = "fresh"

    return {
        "base": str(base),
        "status": status,
        "config_present": config_present,
        "actions": actions,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="바선생 워크스페이스 상태 보증기")
    ap.add_argument("--base", type=Path, default=Path.home() / "vibe-sunsang",
                    help="워크스페이스 루트 (기본: ~/vibe-sunsang)")
    ap.add_argument("--json", action="store_true", help="JSON으로 상세 출력")
    args = ap.parse_args()

    result = ensure(args.base)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for a in result["actions"]:
            print(f"  {a}")
    # 스킬이 파싱하는 상태 라인 (항상 마지막)
    print(f"STATUS {result['status']}  CONFIG "
          f"{'present' if result['config_present'] else 'absent'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
