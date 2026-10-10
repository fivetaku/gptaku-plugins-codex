#!/usr/bin/env python3
"""Codex Browser/IAB 리뷰의 로컬 준비와 결과 기록. 브라우저 조작은 하지 않는다."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import uuid


def write_atomic(path: Path, text: str) -> None:
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def save_manifest(path: Path, data: dict) -> None:
    write_atomic(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def chat_url(value: str) -> str:
    if not re.fullmatch(r"https://chatgpt\.com/(?:g/[^/?#]+/)?c/[A-Za-z0-9-]+", value):
        raise ValueError("실제 ChatGPT 대화 URL(/c/<id>)이 필요합니다")
    return value


def prepare(args) -> Path:
    out = Path(args.out_dir).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    tag = uuid.uuid4().hex
    prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    if not prompt.strip():
        raise ValueError("빈 프롬프트는 준비할 수 없습니다")
    pack = None
    if args.target:
        # 기존 엔진 재사용. CDP/로그인/환경 설치 함수를 호출하지 않는다.
        from pack_and_ask import pack_repo
        target = Path(args.target).expanduser().resolve()
        if not target.is_dir():
            raise ValueError("패킹 대상 디렉토리가 없습니다")
        ignore = args.ignore
        try:
            relative = out.relative_to(target)
            if relative == Path("."):
                raise ValueError("출력 폴더는 패킹 대상 자체와 같을 수 없습니다")
            pattern = f"{relative.as_posix()}/**"
            ignore = f"{ignore},{pattern}" if ignore else pattern
        except ValueError:
            if out == target:
                raise
        pack, _ = pack_repo(target, include=args.include, ignore=ignore,
                            compress=False, style="markdown", token_budget=None,
                            out_path=out / f"pack_{tag}.md", line_numbers=True)
        pack = pack.resolve()
        prompt = "이번 첨부 파일만 코드 근거로 사용하고 판정마다 파일:라인을 인용하세요.\n\n" + prompt
    prompt_path = out / f"prompt_{tag}.txt"
    write_atomic(prompt_path, prompt)
    path = out / f"manifest_{tag}.json"
    save_manifest(path, {
        "transport": "iab", "state": "prepared", "run_tag": tag,
        "prompt": str(prompt_path),
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "pack": str(pack) if pack else None,
        "chat_url": None, "tab_id": None,
    })
    return path


def begin(path: Path, data: dict, args) -> None:
    if data.get("state") != "prepared":
        raise ValueError("prepared 상태에서만 전송 기록을 결속할 수 있습니다")
    if not args.model.strip() or args.effort.lower() != "pro":
        raise ValueError("화면에서 확인한 모델명과 Pro 추론단계가 필요합니다")
    baseline = json.loads(Path(args.baseline_file).read_text(encoding="utf-8"))
    if not isinstance(baseline, list) or any(not isinstance(x, str) for x in baseline):
        raise ValueError("전송 전 assistant message ID 목록(JSON 배열)이 필요합니다")
    if not args.tab_id.strip():
        raise ValueError("실제 탭 ID가 필요합니다")
    data.update(state="sending", tab_id=args.tab_id,
                model=args.model, effort="pro", baseline_ids=baseline)
    save_manifest(path, data)


def bind(path: Path, data: dict, args) -> None:
    if data.get("state") != "sending":
        raise ValueError("sending 상태에서만 전송을 결속할 수 있습니다")
    if not args.user_message_id.strip():
        raise ValueError("전송 후 사용자 message ID가 필요합니다")
    data.update(state="sent", chat_url=chat_url(args.chat_url),
                user_message_id=args.user_message_id)
    save_manifest(path, data)


def complete(path: Path, data: dict, args) -> None:
    if data.get("state") != "sent":
        raise ValueError("전송이 결속된 sent 상태에서만 완료할 수 있습니다")
    if chat_url(args.chat_url) != data["chat_url"]:
        raise ValueError("결속된 대화 URL과 회수 URL이 다릅니다")
    if (not args.message_id.strip() or args.message_id in data["baseline_ids"]
            or args.message_id == data["user_message_id"]):
        raise ValueError("전송 전 목록에 없는 신규 assistant message ID가 필요합니다")
    response = Path(args.response_file).read_text(encoding="utf-8")
    if not response.strip():
        raise ValueError("빈 응답은 완료로 저장하지 않습니다")
    if not args.completion_observed:
        raise ValueError("같은 턴의 완료 표시와 본문 안정화를 화면에서 확인해야 합니다")
    result = path.parent / f"response_{data['run_tag']}.md"
    body = (f"# GPT Pro 리뷰 (Codex Browser/IAB)\n\n"
            f"- 모델: {data['model']}\n- 추론단계: Pro\n"
            f"- 대화: {data['chat_url']}\n- 메시지: {args.message_id}\n\n---\n\n{response}\n")
    write_atomic(result, body)
    data.update(state="complete", response=str(result), assistant_message_id=args.message_id)
    save_manifest(path, data)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare")
    prep.add_argument("--prompt-file", required=True)
    prep.add_argument("--target")
    prep.add_argument("--include")
    prep.add_argument("--ignore")
    prep.add_argument("--out-dir", default=".insane-review")
    start = commands.add_parser("begin")
    start.add_argument("--manifest", required=True)
    start.add_argument("--tab-id", required=True)
    start.add_argument("--model", required=True)
    start.add_argument("--effort", required=True)
    start.add_argument("--baseline-file", required=True)
    sent = commands.add_parser("bind")
    sent.add_argument("--manifest", required=True)
    sent.add_argument("--chat-url", required=True)
    sent.add_argument("--user-message-id", required=True)
    done = commands.add_parser("complete")
    done.add_argument("--manifest", required=True)
    done.add_argument("--chat-url", required=True)
    done.add_argument("--message-id", required=True)
    done.add_argument("--response-file", required=True)
    done.add_argument("--completion-observed", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            path = prepare(args)
        else:
            path = Path(args.manifest).expanduser().resolve()
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("transport") != "iab":
                raise ValueError("IAB manifest가 아닙니다")
            if args.command == "begin":
                begin(path, data, args)
            elif args.command == "bind":
                bind(path, data, args)
            else:
                complete(path, data, args)
        print(path)
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f"오류: {error}\n")


if __name__ == "__main__":
    main()
