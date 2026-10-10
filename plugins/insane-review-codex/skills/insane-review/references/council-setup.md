# GPT Pro를 agent-council 웹 전용 멤버로 등록

GPT Pro(현 플래그십 — 지금은 GPT-5.6 Sol — 의 Pro 추론단계)는 API가 없어 기존 council 멤버(claude/codex/gemini, 전부 CLI/API)로는 못 넣는다.
insane-review의 `--council` 모드가 그 간극을 메운다 — **프롬프트를 위치인자로 받고, 응답만 stdout으로** 내보내(진행 로그는 stderr) council worker가 `output.txt`로 그대로 캡처한다.

이 문서의 외부 프로세스 `--council` 계약은 CLI/CDP 경로다. Desktop IAB 도구를 외부 Python 프로세스가 호출할 수 있다고 가정하지 않는다.

## 작동 방식 (council worker 계약)

council worker는 멤버 `command` 문자열을 토큰화한 뒤 **프롬프트를 마지막 인자로 붙여** `spawn(program, [...args, prompt])` 하고 **stdout을 캡처**한다. `--council`은 정확히 그 계약에 맞춰져 있다.

## council.config.yaml 에 멤버 추가

```yaml
council:
  chairman:
    role: "auto"
  members:
    - name: claude
      command: "claude -p"
      emoji: "🧠"
      color: "CYAN"
    - name: codex
      command: "codex exec"
      emoji: "🤖"
      color: "BLUE"
    # ── GPT Pro (웹 전용, insane-review-codex 경유) ──
    - name: gpt-pro
      command: "python3 /ABS/PATH/plugins/insane-review-codex/bin/pack_and_ask.py --council --model pro --require-model \"GPT-5.6\" --force-answer-after 120"
      emoji: "🌐"
      color: "MAGENTA"
  settings:
    exclude_chairman_from_members: true
    timeout: 600   # ⚠️ Pro 리즈닝이 길다 — 기본 120s로는 SIGTERM될 수 있어 늘린다
```

- `/ABS/PATH`는 절대경로로. (council worker는 셸 없이 execFile 하므로 경로에 공백 없게.)
- `--require-model "GPT-5.6"`: council 경로에서도 활성 모델명을 검증(불일치/미확정이면 fail-closed로 전송 중단). 빼면 effort만 검증되고 기반 모델은 무엇이든 통과한다. **모델명은 부분 일치라 "GPT-5.6"이면 "GPT-5.6 Sol"에 매칭된다. 플래그십이 바뀌면 이 값도 갱신할 것**(안 하면 fail-closed로 전 실행이 차단됨) — 자동 추종을 원하면 아예 빼라.
- `--force-answer-after 120`: 120초 후 "지금 답변 받기"로 리즈닝을 끊어 회수 시간을 bound. council `timeout`은 그보다 넉넉히(예: 600).
- council은 멤버를 **병렬 detached**로 띄운다. gpt-pro는 자기 브라우저 탭을 새로 열므로 다른 멤버와 충돌하지 않지만, **동시에 두 개의 insane-review 잡이 같은 브라우저를 몰면 안 된다**(한 council 잡에 gpt-pro 멤버는 하나).

## 선행 조건
- Comet/Chrome가 디버그포트(9222)로 실행 + chatgpt.com 로그인 + 모델 Pro.
- `playwright`, `pyperclip` 설치.

## 검증 방법
```bash
# 단독으로 council 계약 확인: stdout엔 응답만, stderr엔 로그
python3 plugins/insane-review-codex/bin/pack_and_ask.py --council --model pro --require-model "GPT-5.6" \
  --force-answer-after 60 "한 문장으로: 1+1은?" 2>/dev/null
# → GPT 응답 텍스트만 출력되어야 한다
```
