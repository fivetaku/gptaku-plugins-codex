"""Offline HTTP fixtures exercised through the public X CLI entrypoints."""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine import __main__ as cli, phase0, x_search

URL = "https://x.com/example/status/123"
TweetCase = tuple[str, bool | None, str]


class TweetPayload(TypedDict):
    id_str: str
    text: str


@dataclass(frozen=True, slots=True)
class Response:
    text: str
    status_code: int = 200

    def json(self) -> TweetPayload:
        return json.loads(self.text)


@pytest.fixture(params=[
    ('"truncated": true', False, "truncated"),
    ('"is_note_tweet": true', False, "is_note_tweet"),
    ('"note_tweet": {"text": "long body"}', False, "note_tweet"),
    ('"note_tweet_results": {"result": {"text": "long body"}}', False, "note_tweet_results"),
    ('"article": {"title": "Article preview"}', False, "article"),
    ('"truncated": false', None, ""),
    ('"is_note_tweet": false, "article": null', None, ""),
])
def tweet_case(
    request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch, tmp_path: Path,
) -> TweetCase:
    fields, complete, reason = request.param
    body = '{"id_str": "123", "text": "Available text…", ' + fields + '}'

    def get(url: str, *, timeout: int) -> Response:
        assert url == "https://cdn.syndication.twimg.com/tweet-result?id=123&token=a"
        return Response(body)

    monkeypatch.setenv("INSANE_LEARN", "0")
    monkeypatch.setenv("INSANE_OBSERVATIONS_DIR", str(tmp_path / "observations"))
    monkeypatch.setattr(phase0, "_cffi_get", get)
    monkeypatch.setattr(x_search, "_http_get", lambda *_args: Response(f'<a href="{URL}">post</a>'))
    return body, complete, reason


@pytest.mark.parametrize("mode", ["--json", "--json-content", "text"])
def test_fetch_cli_reports_completeness(
    tweet_case: TweetCase, mode: str, capsys: pytest.CaptureFixture[str], tmp_path: Path,
) -> None:
    body, complete, reason = tweet_case
    args = [URL, "--no-playwright"] + ([] if mode == "text" else [mode])

    exit_code = cli.main(args)
    captured = capsys.readouterr()
    (tmp_path / "stdout.txt").write_text(captured.out)
    (tmp_path / "stderr.txt").write_text(captured.err or "(empty)")

    assert exit_code == 0
    if mode != "text":
        payload = json.loads(captured.out)
        assert payload["content_complete"] is complete
        assert payload["incomplete_reason"] == reason
        assert payload["ok"] is True
        if mode == "--json-content":
            assert body in payload["untrusted_text"]
    else:
        assert body in captured.out
        assert ("content_complete=False" in captured.err) is (complete is False)
        if reason:
            assert reason in captured.err


def test_keyword_cli_preserves_completeness(
    tweet_case: TweetCase, monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str], tmp_path: Path,
) -> None:
    body, complete, reason = tweet_case
    monkeypatch.setattr(sys, "argv", ["engine.x_search", "fixture", "--free-only"])

    exit_code = x_search.main()
    captured = capsys.readouterr()
    (tmp_path / "stdout.json").write_text(captured.out)
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert len(payload["posts"]) == 1
    post = payload["posts"][0]
    assert post["content_complete"] is complete
    assert post["incomplete_reason"] == reason
    assert post["text"] == json.loads(body)["text"]
    assert set(post["discovered_by"]) == {"brave", "yahoo"}
