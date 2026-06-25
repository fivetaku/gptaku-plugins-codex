---
name: insane-review
description: GPT-5.5 Pro(웹 전용 — API 없음)를 Codex CLI 안에서 활용한다. 검토/수정/리뷰/의견 요청을 받으면 의도를 파악하고 repomix로 관련 코드만 정밀 패킹한 뒤 구독 ChatGPT Pro에 투입해 분석을 회수하고 반영한다. 트리거 — "GPT한테 물어봐", "Pro 모델 의견", "다른 모델로 검토해줘", "GPT Pro로 리뷰", "repomix로 묶어서 GPT에 넣어줘", "GPT는 어떻게 생각해", "ask gpt pro", "second opinion". agent-council의 웹 전용 멤버로도 동작.
---

# insane-review (Codex 판)

**왜 존재하나:** GPT-5.5 Pro는 **웹(구독)에서만** 쓸 수 있고 **API가 없다.** Codex CLI의 기존 provider(`omc ask`, agent-council API 경로)로는 못 부른다. 이 스킬은 **구독 ChatGPT 웹을 자동화해 Pro를 Codex CLI 안으로 끌어오는 유일한 경로**다. API 비용 0, 사용자의 요금제로 동작.

핵심 가치는 "통째 패킹"이 아니라 **"의도 파악 → 관련 타겟만 정밀 선별 → 그것만 패킹"** 이다. 이 선별을 Codex(너)가 수행하는 것이 이 도구의 차별점이다.

엔진(`scripts/pack_and_ask.py`)은 본진(Codex CLI)판과 **1:1로 동일한 순수 Python**이다. Codex에는 setup 훅·`question prompt`이 없으므로, 본진 커맨드가 자동화하던 셋업/온보딩을 여기서는 **수동 선행 단계**로 안내한다(아래).

## 선행 조건 (처음 한 번 — 수동 셋업)

Codex에는 설치 훅이 없다. 그래서 pip 의존성은 **사용자가/네가 1회 직접** 설치한다(자동 훅 아님).

1. **환경 점검을 먼저 돌려라.** 막힌 단계를 STATUS 라인으로 알려준다:
   ```bash
   python3 "$PLUGIN_ROOT/scripts/pack_and_ask.py" --check-env
   ```
   마지막 줄 `STATUS node=… deps=… browser=… login=… os=…` 와 `BROWSERS …`(설치된 크로미움 목록)를 읽고 분기한다.
2. **pip 의존성**(`playwright`·`pyperclip`): `deps=missing`이면 자동설치 플래그로 채운다(repomix는 `npx -y`라 사전설치 불필요):
   ```bash
   python3 "$PLUGIN_ROOT/scripts/pack_and_ask.py" --check-env --install
   ```
3. **브라우저(전용 프로필 + 디버그 포트)**: `browser=down`이면 `BROWSERS`에서 자동화용 브라우저를 하나 골라 띄운다. **항상 전용(격리) 프로필로 뜨므로 사용자의 주 브라우저 세션은 건드리지 않는다.** (Chrome 136+는 전용 프로필 없이는 CDP가 안 열린다.)
   ```bash
   python3 "$PLUGIN_ROOT/scripts/pack_and_ask.py" --launch-browser "<이름>"   # 예: Chrome / Brave / Comet
   ```
   - 설치 브라우저가 **1개뿐**이면 그게 사용자 메인일 가능성이 높다 — 가벼운 크로미움(Chrome/Brave 등) **하나를 자동화 전용으로 따로 설치**하길 권한다. 같은 앱을 2창으로 띄우면 멀티인스턴스 불안정/오조작 위험.
   - 선택한 브라우저는 `~/.insane-review/config.json`에 저장되어 다음 실행부터 재질문 없이 재사용된다.
   - `browser=wrong`(9222 점유)이면 그 프로세스를 종료한 뒤 `--launch-browser`로 전용 프로필을 다시 띄운다.
4. **로그인 + Pro 모델**: `login=no`면 **방금 띄운 전용 브라우저 창**에서 `chatgpt.com` 로그인 + `GPT-5.5 Pro` 선택을 끝낸다. **로그인은 자동 불가 → 반드시 사용자에게 요청**(에러로 끝내지 말 것). 전용 프로필이라 쿠키가 디스크에 보존돼 로그인이 유지된다. 모델은 스크립트 `--model pro`가 자동 선택·검증하지만, 안 되면 사용자가 1회 수동 설정하면 새 채팅이 상속한다.

`STATUS … login=ok`까지 가면 본 작업으로 넘어간다.

> Codex에는 `question prompt` 카드 UI가 없다. 위 분기에서 사용자 선택이 필요하면 `shared/questioning-policy.md §A` 방식(채팅에 번호형 선택지 블록을 출력하고 자유 텍스트 답변을 읽음)으로 묻는다. 주로 §2c — 이미 결정 가능하면 묻지 말고 즉시 진행한다.

## 핵심 절차 (검토/수정/리뷰 요청을 받았을 때)

### 1) 의도 파악

사용자가 GPT Pro에게 **무엇을** 묻고 싶은지 한 문장으로 정리한다. (버그 원인? 설계 리뷰? 리팩터 방향? 특정 함수 검증?) 애매하면 `shared/questioning-policy.md §A`로 한 가지만 묻는다.

### 2) 타겟 선별 — **완전한 관련 집합을 네가(Codex) 판단** (사용자가 누락을 잡아주는 구조면 안 된다)

"repomix로 무엇을 넣을지 = 무엇이 완전한 관련 집합인지"의 **판단은 네 책임**이다. 기본은 **"넓게, 빠짐없이"**:

- **단일 모듈/플러그인/기능 리뷰면 그 디렉토리를 통째로** 넣어라(`--target <dir>`, `--include` 생략 또는 광범위). 코드 한 파일만 넣으면 실행지시서·설정·통합 맥락이 빠진다(실측: `scripts/**`만 넣어 3파일 → README/SKILL/config 누락).
- 더 넓은 범위면 지목 파일에서 **import/require·호출자·피호출자·테스트·타입·설정**까지 추적해 집합을 *닫는다*.
- **패킹 후 `📦 패킹 포함 N개 파일` 감사 목록이 의도한 완전한 집합을 담았는지 직접 확인**한다(§3.5). 사용자가 지적하기 전에 네가 잡아라.
- **코드 리뷰/원인분석은 풀 코드로 보내라 — `--compress` 쓰지 마라.** 압축은 함수 본문(조건·early return·예외·루프 = 버그 판단 근거)을 제거해 리뷰 AI가 구현을 *상상*하게 만든다. 타겟이 너무 크면 **압축 대신 `--include`로 관련 파일만 좁혀 풀로** 보낸다. `--compress`는 오직 "큰 레포 *개요*"(정확성 리뷰 아님)용.

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

- `🔒 secretlint: 의심 파일 N개 제외` → **시크릿 든 파일이 통째 빠짐**(숨은 누락). 해당 파일이 리뷰 대상이면 시크릿을 가린 사본을 따로 넣거나 `--no-security-check`(외부 유출 주의).
- 기본 ignore/`.gitignore`가 떨어뜨림 → `--no-default-patterns`/`--no-gitignore`.
- 서브모듈 파일이 빠짐(부모서 패킹) → 서브모듈 안에서 `--target`.
- `⚠️ pack이 큼(truncation)` 경고 → ChatGPT가 잘라먹을 수 있으니 `--include`로 더 좁히거나 여러 번 나눠 보낸다.
- **손실 플래그 금지**: `--compress`/`--remove-comments`/`--remove-empty-lines`는 내용을 누락시키니 리뷰엔 쓰지 않는다. 라인번호는 기본 ON(인용용).

### 4) 회수 & 반영

- 응답은 **현재 프로젝트의 `.insane-review/response_*.md`**에 저장되고, stdout 끝에 미리보기가 나온다.
- 그 의견을 읽고 **GPT-5.5 Pro의 의견임을 명시**해 사용자에게 반영/요약한다. 동의/이견을 너의 판단과 함께 제시하라.

## 채팅 정리 — 폴더명 ChatGPT 프로젝트 (기본 on)

매 실행이 일반 채팅 목록에 쌓이지 않도록, **현재 폴더명(+경로해시)과 같은 이름의 ChatGPT 프로젝트** 안에 채팅을 정리한다. 폴더당 프로젝트 1개로 묶여 일반 목록이 깨끗하게 유지된다.

- 폴더명→프로젝트URL은 per-repo 캐시(`.insane-review/projects.json`, 키=`{절대경로}::{이름}`)에 저장 → 다음 실행부턴 사이드바를 안 건드리고 바로 그 프로젝트로 들어간다(견고). 동명 다른 폴더(`/a/api`, `/b/api`)도 경로해시·절대경로 키로 분리돼 한 프로젝트로 병합되지 않는다.
- 프로젝트가 없으면 자동 생성, 있으면 재사용(중복 생성 안 함). **프로젝트 미지원 플랜이거나 UI가 바뀌어 실패해도 하드중단 없이 일반 채팅으로 폴백.**
- 이름 바꾸려면 `--project "<이름>"`, 끄려면 `--no-project`.

## 주의/가드 (실측 기반)

- **git submodule**: 부모 레포 루트에서 서브모듈 파일은 repomix가 제외한다. 서브모듈 안에서 실행하거나 `--target <submodule>` 또는 `--no-gitignore --no-default-patterns`.
- **정밀 리뷰엔 `--force-answer-after`를 쓰지 마라** — Pro 추론을 중간에 끊어 "다 생각 안 한 채" 답하게 만든다(fail-open과 곱해져 미완성 답을 정답 저장). 완전 추론이 더 정확. 안전장치는 `--max-wait`(기본 20분, env `INSANE_REVIEW_MAX_WAIT`/`--max-wait`로 조절)만. force-answer는 빠른 의견·짧은 질문·council cap에만.
- **fail-closed**: 첨부 미확인 / 모델 미검증(`--require-model`) / 프롬프트 잘림 / timeout·빈 응답은 **성공 저장 안 하고 중단·재시도**한다(잘못된 컨텍스트나 미완성 답을 리뷰로 저장하지 않음).
- **첨부 → 인라인 폴백**: 큰 콘텐츠는 **파일 첨부**가 기본. 첨부가 실패하면 pack이 상한(기본 50,000자, env `INSANE_REVIEW_PASTE_MAX`) 내일 때만 프롬프트에 인라인으로 붙여 보내고, 초과면 fail-closed(잘린 전송 방지). `--attach`는 폴백 없이 첨부만 강제.
- **전용 프로필 자가복구**: 전용 프로필에 스테일 브라우저가 떠 있어 디버그 포트가 안 열리는 싱글톤 교착을, 그 프로세스를 정리(로그인은 보존)하고 1회 재시도해 푼다.
- **CDP 다이얼로그 핸들링**: ChatGPT 페이지의 JS 다이얼로그(beforeunload 등)가 playwright 기본 auto-dismiss와 레이스해 드라이버가 크래시하던 문제를 자체 핸들러로 차단.
- 실패 시 `--retries N`으로 전송/회수를 재시도.

## 주요 플래그

`--target`(생략=프롬프트only) · `--include`(정밀 글롭) · `--ignore` · `--compress` · `--model pro` · `--require-model "GPT-5.5"` · `--force-answer-after N` · `--max-wait N` · `--retries N` · `--style xml|markdown|plain` · `--attach` · `--browser <이름|경로>`(전용 프로필; 생략=config→첫 감지) · `--launch-browser <이름>`(전용 프로필 실행+저장) · `--list-browsers` · `--project "<이름>"`(기본=폴더명+해시) · `--no-project` · `--pack-only` · `--delete-pack` · `--out-dir <경로>` · `--check-env [--install]` · `--council`

## agent-council 멤버로 쓰기

`references/council-setup.md` 참고. `--council` 모드는 프롬프트를 위치인자로 받고 **응답만 stdout**으로 내보내(진행로그는 stderr) council worker가 그대로 캡처한다. Pro를 웹 전용 council 멤버로 등록하면 다른 모델들과 토론에 참여시킬 수 있다.

## Codex 렌더링 규칙 (질문이 필요할 때)

Codex CLI에는 `question prompt` 카드 UI가 없다. 질문이 반드시 필요하면 `shared/questioning-policy.md §A` 방식 — 채팅에 번호형 선택지 블록을 출력하고 사용자의 자유 텍스트 답변을 읽는다. 주로 §2c(이미 구체적이면 즉시 진행)가 적용된다.
