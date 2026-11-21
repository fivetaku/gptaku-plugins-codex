"""Codex 설치 경로와 신규 세션을 실제 스냅샷/게이트 CLI로 검증한다."""

import json
import os
import runpy
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from test_snapshot_sources import FAKE_ENGINE, SCRIPTS, make
from test_evidence_gate import COUNTER, run_gate


@pytest.mark.parametrize("route", ["explicit", "environment", "sibling", "cache"])
def test_codex_engine_resolution_precedence(tmp_path: Path, route: str) -> None:
    source = {"id": "src_001", "url": "https://docs.example.com/a"}
    claim = {"risk": "high", "source_ids": ["src_001"]}
    session, _ = make(tmp_path, [claim], [source])
    packages = tmp_path / "packages"
    script = packages / "insane-research-codex/skills/insane-research-main/scripts/snapshot_sources.py"
    script.parent.mkdir(parents=True)
    shutil.copyfile(SCRIPTS / "snapshot_sources.py", script)
    cache_root = tmp_path / "codex-config"
    engines = {
        "explicit": tmp_path / "explicit",
        "environment": tmp_path / "environment",
        "sibling": packages / "insane-search-codex/skills/insane-search",
        "cache": cache_root / "plugins/cache/vendor/insane-search-codex/0.10.0/skills/insane-search",
        "old-cache": cache_root / "plugins/cache/vendor/insane-search-codex/0.9.0/skills/insane-search",
    }
    for name, directory in engines.items():
        if name == "sibling" and route == "cache":
            continue
        (directory / "engine").mkdir(parents=True)
        (directory / "engine/__init__.py").write_text(
            FAKE_ENGINE.replace("The default timeout is 90 seconds in every region.",
                                f"The selected engine route is {name}."), encoding="utf-8"
        )
    env = dict(os.environ, CODEX_HOME=str(cache_root))
    env.pop("INSANE_SEARCH_ENGINE_DIR", None)
    if route in {"explicit", "environment"}:
        env["INSANE_SEARCH_ENGINE_DIR"] = str(engines["environment"])
    command = [sys.executable, str(script), "--session", str(session)]
    if route == "explicit":
        command += ["--engine-dir", str(engines["explicit"])]

    result = subprocess.run(command, env=env, capture_output=True, text=True)

    assert result.returncode == 0, result.stderr
    assert (session / "sources/snapshots/src_001.txt").read_text() == (
        f"The selected engine route is {route}."
    )


def test_new_session_rejects_high_risk_claim_without_quote(tmp_path: Path) -> None:
    namespace = runpy.run_path(str(SCRIPTS / "orchestrator.py"))
    state = namespace["ResearchState"](str(tmp_path))
    session = tmp_path / state.create_session("Evidence required")
    sources = [
        {"id": "src_001", "url": "https://docs.example.com/a", "type": "official_docs", "quality_rating": "A"},
        {"id": "src_002", "url": "https://bench.example.net/b", "type": "independent_benchmark", "quality_rating": "B"},
    ]
    claim = {"claim_id": "clm_001", "text": "기본 타임아웃은 90초", "risk": "high",
             "claim_type": "numeric", "source_ids": ["src_001", "src_002"], "counter_search": COUNTER}
    (session / "sources/sources.jsonl").write_text("\n".join(map(json.dumps, sources)) + "\n")
    (session / "artifacts/claim_ledger.jsonl").write_text(json.dumps(claim) + "\n")

    result, statuses = run_gate(session)

    assert result.returncode == 0, result.stderr
    assert statuses["clm_001"]["status"] == "unresolved"
    assert "evidence 없음" in statuses["clm_001"]["status_reason"]
