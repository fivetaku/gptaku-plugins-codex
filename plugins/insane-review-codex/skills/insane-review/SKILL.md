---
name: insane-review
description: GPT-5.5 Pro(웹 전용 — API 없음)를 Codex CLI 안에서 활용한다. 검토/수정/리뷰/의견 요청을 받으면 의도를 파악하고 repomix로 관련 코드만 정밀 패킹한 뒤 구독 ChatGPT Pro에 투입해 분석을 회수하고 반영한다. 트리거 — "GPT한테 물어봐", "Pro 모델 의견", "다른 모델로 검토해줘", "GPT Pro로 리뷰", "repomix로 묶어서 GPT에 넣어줘", "GPT는 어떻게 생각해", "ask gpt pro", "second opinion". agent-council의 웹 전용 멤버로도 동작.
---

# insane-review (Codex 판)

**왜 존재하나:** GPT-5.5 Pro는 **웹(구독)에서만** 쓸 수 있고 **API가 없다.** Codex CLI의 기존 provider(`omc ask`, agent-council API 경로)로는 못 부른다. 이 스킬은 **구독 ChatGPT 웹을 자동화해 Pro를 Codex CLI 안으로 끌어오는 유일한 경로**다. API 비용 0, 사용자의 요금제로 동작.

핵심 가치는 "통째 패킹"이 아니라 **"의도 파악 → 관련 타겟만 정밀 선별 → 그것만 패킹"** 이다. 이 선별을 Codex(너)가 수행하는 것이 이 도구의 차별점이다.

## 선행 조건 (한 번 확인)

- Comet 또는 Chrome이 **디버그 포트(9222)로** 실행 + `chatgpt.com` 로그인. 이미 떠 있는데 포트가 없으면 **재시작 필요**(쿠키는 디스크 보존 → 로그인 유지). 스크립트가 자동 실행하지만, 이미 일반 모드로 떠 있으면 사용자에게 종료를 요청하라.
- **모델을 5.5 Pro로** (스크립트 `--model pro`가 자동 선택; 안 되면 사용자가 1회 수동 설정하면 새 채팅이 상속).
- `playwright`·`pyperclip`(pip), `npx`(repomix는 `npx -y`로 자동설치) 필요. **처음 쓸 땐 `python3 $PLUGIN_ROOT/scripts/pack_and_ask.py --check-env`로 점검**(부족하면 `--install`로 pip 의존성 자동설치). 브라우저 로그인·Pro 모델은 자동설치 불가 → 위 안내대로.

## 핵심 절차 (검토/수정/리뷰 요청을 받았을 때)

### 1) 의도 파악

사용자가 GPT Pro에게 **무엇을** 묻고 싶은지 한 문장으로 정리한다. (버그 원인? 설계 리뷰? 리팩터 방향? 특정 함수 검증?)

필요하면 `shared/questioning-policy.md §A` 방식(번호형 선택지 블록)으로 한 가지만 묻는다. 주로 §2c — 요청이 이미 구체적이면 묻지 않고 즉시 진행한다.

### 2) 타겟 선별 — **완전한 관련 집합을 네가(Codex) 판단**

"repomix로 무엇을 넣을지 = 무엇이 완전한 관련 집합인지"의 **판단은 네 책임**이다. 기본은 **"넓게, 빠짐없이"**:

- **단일 모듈/플러그인/기능 리뷰면 그 디렉토리를 통째로** 넣어라(`--target <dir>`, `--include` 생략 또는 광범위). 코드 한 파일만 넣으면 실행지시서·설정·통합 맥락이 빠진다.
- 더 넓은 범위면 지목 파일에서 **import/require·호출자·피호출자·테스트·타입·설정**까지 추적해 집합을 *닫는다*.
- **패킹 후 `📦 패킹 포함 N개 파일` 감사 목록이 의도한 완전한 집합을 담았는지 직접 확인**한다. 사용자가 지적하기 전에 네가 잡아라.
- **코드 리뷰/원인분석은 풀 코드로 보내라 — `--compress` 쓰지 마라.** 압축은 함수 본문을 제거해 리뷰 AI가 구현을 *상상*하게 만든다. 타겟이 너무 크면 **압축 대신 `--include`로 관련 파일만 좁혀 풀로** 보낸다.

### 3) 패킹 + 투입 + 회수 — 스크립트 실행

```bash
python3 "$PLUGIN_ROOT/scripts/pack_and_ask.py" \
  --target <repo_root> --include "<관련 파일 글롭>" \
  --model pro --require-model "GPT-5.5" \
  --prompt "<의도를 담은 정확한 질문 — '판정마다 파일/라인/코드조각을 인용하라'를 반드시 포함>"
```

**레포 없이 순수 질문(의견)만:**

```bash
python3 "$PLUGIN_ROOT/scripts/pack_and_ask.py" --model pro --force-answer-after 90 \
  --prompt "<질문>"
```

### 3.5) 누락 검증 — 빠진 파일 없는지 감사

패킹 직후 출력의 **`📦 패킹 포함 N개 파일: ...`** 목록이 **의도한 관련 파일을 전부 담았는지** 확인한다. 빠진 게 있으면 repomix가 떨어뜨린 것 — 원인별 대응:

- `🔒 secretlint: 의심 파일 N개 제외` → 해당 파일이 리뷰 대상이면 시크릿을 가린 사본을 따로 넣거나 `--no-security-check`(외부 유출 주의).
- 기본 ignore/`.gitignore`가 떨어뜨림 → `--no-default-patterns`/`--no-gitignore`.
- 서브모듈 파일이 빠짐(부모서 패킹) → 서브모듈 안에서 `--target`.
- `⚠️ pack이 큼(truncation)` 경고 → `--include`로 더 좁히거나 여러 번 나눠 보낸다.
- **손실 플래그 금지**: `--compress`/`--remove-comments`/`--remove-empty-lines`는 내용을 누락시키니 리뷰엔 쓰지 않는다.

### 4) 회수 & 반영

- 응답은 **현재 프로젝트의 `.insane-review/response_*.md`**에 저장되고, stdout 끝에 미리보기가 나온다.
- 그 의견을 읽고 **GPT-5.5 Pro의 의견임을 명시**해 사용자에게 반영/요약한다. 동의/이견을 너의 판단과 함께 제시하라.

## 주의/가드 (실측 기반)

- **git submodule**: 부모 레포 루트에서 서브모듈 파일은 repomix가 제외한다. 서브모듈 안에서 실행하거나 `--target <submodule>` 또는 `--no-gitignore --no-default-patterns`.
- **정밀 리뷰엔 `--force-answer-after`를 쓰지 마라** — Pro 추론을 중간에 끊어 "다 생각 안 한 채" 답하게 만든다. 안전장치는 `--max-wait`(기본 20분)만. force-answer는 빠른 의견·짧은 질문에만.
- **fail-closed**: 첨부 미확인 / 모델 미검증(`--require-model`) / timeout·빈 응답은 **성공 저장 안 하고 중단·재시도**한다.
- 큰 콘텐츠는 **파일 첨부**로 들어간다(붙여넣기 X). 스크립트가 자동 처리.
- 실패 시 `--retries N`으로 전송/회수를 재시도.

## 주요 플래그

`--target`(생략=프롬프트only) · `--include`(정밀 글롭) · `--compress` · `--model pro` · `--force-answer-after N` · `--retries N` · `--style xml|markdown|plain` · `--browser comet|chrome` · `--pack-only` · `--council`

## agent-council 멤버로 쓰기

`references/council-setup.md` 참고. `--council` 모드는 프롬프트를 위치인자로 받고 **응답만 stdout**으로 내보내(진행로그는 stderr) council worker가 그대로 캡처한다. Pro를 웹 전용 council 멤버로 등록하면 다른 모델들과 토론에 참여시킬 수 있다.

## Codex 렌더링 규칙 (질문이 필요할 때)

Codex CLI에는 `AskUserQuestion` 카드 UI가 없다. 질문이 반드시 필요하면 `shared/questioning-policy.md §A` 방식 — 채팅에 번호형 선택지 블록을 출력하고 사용자의 자유 텍스트 답변을 읽는다. 주로 §2c(이미 구체적이면 즉시 진행)가 적용된다.
