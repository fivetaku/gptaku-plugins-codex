from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

import pytest

BIN = Path(__file__).resolve().parents[1] / 'plugins/insane-review-codex/bin'
spec = importlib.util.spec_from_file_location('iab_review', BIN / 'iab_review.py')
iab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iab)


def prepared(tmp_path):
    question = tmp_path / 'question.txt'
    question.write_text('설계를 검토해 주세요.', encoding='utf-8')
    path = iab.prepare(SimpleNamespace(out_dir=str(tmp_path / 'out'),
                                     prompt_file=str(question), target=None))
    return path, json.loads(path.read_text())


def sending(tmp_path):
    path, data = prepared(tmp_path)
    baseline = tmp_path / 'baseline.json'
    baseline.write_text('["old"]')
    iab.begin(path, data, SimpleNamespace(model='Observed model', effort='pro',
                                         tab_id='tab-1', baseline_file=str(baseline)))
    return path, data


def test_prompt_only_cli_prepares_without_browser(tmp_path):
    question = tmp_path / 'question.txt'
    question.write_text('질문', encoding='utf-8')
    proc = subprocess.run([sys.executable, '-S', str(BIN / 'iab_review.py'), 'prepare',
                           '--prompt-file', str(question), '--out-dir', str(tmp_path / 'out')],
                          capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    data = json.loads(Path(proc.stdout.strip()).read_text())
    assert data['state'] == 'prepared'
    assert data['chat_url'] is None and data['pack'] is None
    assert Path(data['prompt']).read_text() == '질문'


def test_begin_requires_pro_and_cannot_be_repeated(tmp_path):
    path, data = sending(tmp_path)
    assert json.loads(path.read_text())['state'] == 'sending'
    with pytest.raises(ValueError):
        iab.begin(path, data, SimpleNamespace())
    path, data = prepared(tmp_path)
    with pytest.raises(ValueError):
        iab.begin(path, data, SimpleNamespace(model='Model', effort='thinking'))
    assert json.loads(path.read_text())['state'] == 'prepared'


@pytest.mark.parametrize('url', ['https://example.com/c/abc', 'https://chatgpt.com/',
                                 'https://chatgpt.com/c/abc?x=1'])
def test_bind_rejects_unbound_urls(tmp_path, url):
    path, data = sending(tmp_path)
    with pytest.raises(ValueError):
        iab.bind(path, data, SimpleNamespace(chat_url=url, user_message_id='user-1'))
    assert json.loads(path.read_text())['state'] == 'sending'


def test_complete_requires_new_turn_bound_url_and_observed_completion(tmp_path):
    path, data = sending(tmp_path)
    url = 'https://chatgpt.com/g/g-p-project/c/abc-123'
    iab.bind(path, data, SimpleNamespace(chat_url=url, user_message_id='user-1'))
    response = tmp_path / 'body.txt'
    response.write_text('검토 결과', encoding='utf-8')
    args = SimpleNamespace(chat_url=url, message_id='new', response_file=str(response),
                           completion_observed=True)
    for override in ({'message_id': 'old'}, {'message_id': 'user-1'}, {'chat_url': 'https://chatgpt.com/c/other'},
                     {'completion_observed': False}):
        with pytest.raises(ValueError):
            iab.complete(path, data, SimpleNamespace(**(vars(args) | override)))
        assert not list(path.parent.glob('response_*.md'))
    response.write_text('   ')
    with pytest.raises(ValueError):
        iab.complete(path, data, args)
    response.write_text('검토 결과', encoding='utf-8')
    iab.complete(path, data, args)
    saved = json.loads(path.read_text())
    assert saved['state'] == 'complete'
    assert '검토 결과' in Path(saved['response']).read_text()
    with pytest.raises(ValueError):
        iab.complete(path, data, args)


def test_prepare_reuses_full_code_pack_and_excludes_output(tmp_path, monkeypatch):
    sys.path.insert(0, str(BIN))
    import pack_and_ask
    calls = []
    def pack(target, **kwargs):
        calls.append((target, kwargs))
        kwargs['out_path'].write_text('full code')
        return kwargs['out_path'], 10
    monkeypatch.setattr(pack_and_ask, 'pack_repo', pack)
    question = tmp_path / 'question.txt'
    question.write_text('검토')
    path = iab.prepare(SimpleNamespace(out_dir=str(tmp_path / 'out'),
        prompt_file=str(question), target=str(tmp_path), include='src/**', ignore='secret/**'))
    assert calls[0][1]['compress'] is False
    assert calls[0][1]['line_numbers'] is True
    assert calls[0][1]['ignore'] == 'secret/**,out/**'
    assert Path(json.loads(path.read_text())['pack']).read_text() == 'full code'


def test_cli_can_resume_sent_manifest_without_resending(tmp_path):
    path, data = sending(tmp_path)
    url = 'https://chatgpt.com/c/abc-123'
    def run(*args):
        return subprocess.run([sys.executable, '-S', str(BIN / 'iab_review.py'), *args],
                              capture_output=True, text=True)
    bound = run('bind', '--manifest', str(path), '--chat-url', url,
                '--user-message-id', 'user-1')
    assert bound.returncode == 0, bound.stderr
    response = tmp_path / 'body.txt'
    response.write_text('완료된 응답', encoding='utf-8')
    done = run('complete', '--manifest', str(path), '--chat-url', url,
               '--message-id', 'assistant-1', '--response-file', str(response),
               '--completion-observed')
    assert done.returncode == 0, done.stderr
    saved = json.loads(path.read_text())
    assert saved['state'] == 'complete'
    assert '완료된 응답' in Path(saved['response']).read_text()
