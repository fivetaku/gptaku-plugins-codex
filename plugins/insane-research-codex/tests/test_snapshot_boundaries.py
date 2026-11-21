"""Snapshot confinement, lazy optional engine and byte integrity via real CLIs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from test_evidence_gate import GOOD_Q, SNAP, build_session, run_gate
from test_snapshot_sources import load_sources, make, run


@pytest.mark.parametrize("risk", ["normal", "high"])
def test_no_fetch_needed_without_engine(tmp_path: Path, risk: str) -> None:
    source = {"id": "src_001", "url": "https://docs.example.com/a"}
    session, _ = make(tmp_path, [{"risk": risk, "source_ids": ["src_001"]}], [source])
    if risk == "high":
        raw = "이미 확보한 원문입니다.".encode()
        path = session / "sources/snapshots/src_001.txt"
        path.parent.mkdir()
        path.write_bytes(raw)
        source["snapshot"] = {"path": "sources/snapshots/src_001.txt", "status": "ok",
                              "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
        (session / "sources/sources.jsonl").write_text(json.dumps(source) + "\n")

    result = run(session, tmp_path / "missing-engine")

    assert result.returncode == 0, result.stderr
    assert ("skipped(기존 ok)=1" in result.stderr) is (risk == "high")


@pytest.mark.parametrize("escape", ["absolute", "traversal", "symlink", "root_symlink"])
def test_gate_rejects_snapshot_outside_root(tmp_path: Path, escape: str) -> None:
    session = build_session(tmp_path, [({"evidence": [{"quote": GOOD_Q}]}, SNAP, "ok")])
    registry = session / "sources/sources.jsonl"
    sources = [json.loads(line) for line in registry.read_text().splitlines()]
    outside = session / "outside.txt"
    outside.write_text(SNAP)
    snapshot = session / "sources/snapshots/src_001.txt"
    if escape == "absolute":
        sources[0]["snapshot"]["path"] = str(outside)
    elif escape == "traversal":
        sources[0]["snapshot"]["path"] = "sources/snapshots/../../outside.txt"
    elif escape == "symlink":
        snapshot.unlink()
        snapshot.symlink_to(outside)
    else:
        snapshot.parent.rename(session / "elsewhere")
        snapshot.parent.symlink_to(session / "elsewhere", target_is_directory=True)
    registry.write_text("\n".join(json.dumps(source) for source in sources) + "\n")

    result, statuses = run_gate(session)

    assert result.returncode == 0, result.stderr
    assert statuses["clm_001"]["status"] == "unresolved"
    assert "경로" in statuses["clm_001"]["status_reason"]


@pytest.mark.parametrize("escape", ["id_traversal", "symlink", "root_symlink"])
def test_writer_does_not_follow_escaping_paths(tmp_path: Path, escape: str) -> None:
    sid = "../../outside" if escape == "id_traversal" else "src_001"
    session, engine = make(tmp_path, [{"risk": "high", "source_ids": [sid]}],
                           [{"id": sid, "url": "https://docs.example.com/a"}])
    outside = session / "outside.txt"
    outside.write_text("preserve original bytes")
    root = session / "sources/snapshots"
    if escape == "root_symlink":
        root.symlink_to(session, target_is_directory=True)
    else:
        root.mkdir()
        if escape == "symlink":
            (root / "src_001.txt").symlink_to(outside)

    result = run(session, engine)

    assert outside.read_text() == "preserve original bytes"
    assert not (session / "src_001.txt").exists()
    assert load_sources(session)[sid]["snapshot"]["status"] == "error"
    assert not (engine / "engine/__init__.py.calls").exists()


@pytest.mark.parametrize("damage", ["sha", "bytes", "missing_sha"])
def test_existing_snapshot_integrity_checked_by_writer_and_gate(tmp_path: Path, damage: str) -> None:
    session = build_session(tmp_path, [({"evidence": [{"quote": GOOD_Q}]}, SNAP, "ok")])
    registry = session / "sources/sources.jsonl"
    sources = [json.loads(line) for line in registry.read_text().splitlines()]
    snapshot = sources[0]["snapshot"]
    snapshot["bytes"] = len(SNAP.encode())
    if damage == "sha":
        snapshot["sha256"] = "0" * 64
    elif damage == "bytes":
        snapshot["bytes"] += 1
    else:
        del snapshot["sha256"]
    registry.write_text("\n".join(json.dumps(source) for source in sources) + "\n")
    # Keep the second high-risk source from needing a fetch.
    sources[1].pop("url")
    original = registry.read_bytes()

    result, statuses = run_gate(session)
    assert statuses["clm_001"]["status"] == "unresolved"
    registry.write_text("\n".join(json.dumps(source) for source in sources) + "\n")
    result = run(session, tmp_path / "missing-engine")

    assert result.returncode == 0, result.stderr
    assert load_sources(session)["src_001"]["snapshot"]["status"] == "error"
    assert (session / snapshot["path"]).read_bytes() == SNAP.encode()
    (session / "registry.before.jsonl").write_bytes(original)


def test_new_snapshot_records_exact_utf8_bytes(tmp_path: Path) -> None:
    session, engine = make(tmp_path, [{"risk": "high", "source_ids": ["src_001"]}],
                           [{"id": "src_001", "url": "https://docs.example.com/a"}])
    module = engine / "engine/__init__.py"
    module.write_text(module.read_text().replace("The default timeout is 90 seconds in every region.",
                                               "기본 타임아웃은 모든 지역에서 90초입니다."))

    result = run(session, engine)
    snapshot = load_sources(session)["src_001"]["snapshot"]
    raw = (session / snapshot["path"]).read_bytes()

    assert result.returncode == 0, result.stderr
    assert snapshot["bytes"] == len(raw)
    assert snapshot["chars"] == len(raw.decode())
    assert snapshot["bytes"] > snapshot["chars"]
    assert snapshot["sha256"] == hashlib.sha256(raw).hexdigest()


def test_existing_external_snapshot_is_not_skipped(tmp_path: Path) -> None:
    outside = tmp_path / "outside.txt"
    raw = "원래 외부 파일".encode()
    outside.write_bytes(raw)
    source = {"id": "src_001", "url": "https://docs.example.com/a",
              "snapshot": {"status": "ok", "path": str(outside),
                           "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}}
    session, _ = make(tmp_path, [{"risk": "high", "source_ids": ["src_001"]}], [source])

    result = run(session, tmp_path / "missing-engine")
    (session / "cli.stderr").write_text(result.stderr)

    assert result.returncode == 0, result.stderr
    assert load_sources(session)["src_001"]["snapshot"]["status"] == "error"
    assert "경로" in load_sources(session)["src_001"]["snapshot"]["error"]
    assert outside.read_bytes() == raw


def test_snapshot_write_preserves_external_hardlink(tmp_path: Path) -> None:
    session, engine = make(tmp_path, [{"risk": "high", "source_ids": ["src_001"]}],
                           [{"id": "src_001", "url": "https://docs.example.com/a"}])
    outside = tmp_path / "outside.txt"
    outside.write_text("preserve external bytes")
    path = session / "sources/snapshots/src_001.txt"
    path.parent.mkdir()
    path.hardlink_to(outside)

    result = run(session, engine)
    (session / "cli.stderr").write_text(result.stderr)

    assert result.returncode == 0, result.stderr
    assert outside.read_text() == "preserve external bytes"
    assert path.read_text() == "The default timeout is 90 seconds in every region."
