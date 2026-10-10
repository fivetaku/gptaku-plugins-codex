---
name: insane-review
description: GPT Pro(웹 전용·API 없음 — 현 시점 최신 플래그십 모델의 Pro 추론)를 Codex CLI 안에서 활용한다. 사용자가 검토/수정/문제/리뷰/의견을 요청하면, 의도를 파악해 repomix로 관련 코드만 정밀 패킹한 뒤 구독 ChatGPT Pro에 투입하고 분석을 회수해 반영한다. 트리거 — "GPT한테 물어봐", "Pro 모델 의견", "다른 모델로 검토해줘", "GPT Pro로 리뷰", "repomix로 묶어서 GPT에 넣어줘", "GPT는 어떻게 생각해", "ask gpt pro", "second opinion". agent-council의 웹 전용 멤버로도 동작.
---

# insane-review (Codex 판)

**왜 존재하나:** GPT Pro(최신 플래그십 모델의 Pro 추론)는 **웹(구독)에서만** 쓸 수 있고 **API가 없다.** 그래서 `omc ask`·agent-council의 기존 API provider로는 못 부른다. 이 스킬은 **구독 ChatGPT 웹을 자동화해 Pro를 Codex CLI 안으로 끌어오는 유일한 경로**다. API 비용 0, 사용자의 요금제로 동작.

핵심 가치는 "통째 패킹"이 아니라 **"의도 파악 → 관련 타겟만 정밀 선별 → 그것만 패킹"** 이다. 이 선별을 Codex(너)가 수행하는 것이 이 도구의 차별점이다.

CLI/CDP 엔진은 `$PLUGIN_ROOT/bin/pack_and_ask.py`(순수 Python)다. Desktop IAB는 로컬 기록 도구 `bin/iab_review.py`와 현재 세션의 브라우저 도구를 사용한다. 이 문서가 실행 지시서다 — 아래 순서대로 **네가 직접 실행**한다.

> **원칙: 사용자에게 CLI 타이핑을 시키지 않는다.** 환경이 안 갖춰졌으면 먼저 아래 실행 경로를 선택한다. CLI/CDP 경로에서만 `--ensure-env`로 감지하고, 필요한 결정은
> `$PLUGIN_ROOT/shared/questioning-policy.md §A` 방식(채팅에 번호형 선택지 블록을 출력하고 자유 텍스트 답변을 읽음)으로 물어본 뒤
> 네가 대신 실행한다. 초보자도 번호만 골라 따라올 수 있어야 한다. 이미 결정 가능하면(§2c) 묻지 말고 즉시 진행한다.

`$PLUGIN_ROOT`는 아래 명령의 경로 표기다. 현재 읽은 스킬의 설치 위치로부터 플러그인 루트 절대경로를 확인해 직접 치환한다. 런타임이 이 환경 변수를 자동 설정한다고 가정하지 않는다.

## 실행 경로 선택 — 환경 점검보다 먼저

현재 세션에 `mcp__cua_repl.js`와 Codex 내장 Browser/IAB가 제공되면 **Desktop 기본 경로**로
`references/iab-workflow.md`를 읽고 실행한다. 사용자가 명시한 브라우저/탭은 우선한다.
이 경로에서는 아래 Step 0/0.5의 CDP 온보딩과 Step 3의 Python 브라우저 전송을 실행하지 않는다.
패킹은 기존 엔진을 재사용하는 `$PLUGIN_ROOT/bin/iab_review.py prepare`로 하고,
로그인·모델 선택·첨부·전송·회수는 현재 도구 문서를 확인한 `cua_repl`로 수행한다.

IAB에서 로그인이 안 됐거나 Pro가 없다는 이유로 외부 Chromium을 자동 기동하지 않는다.
실제 차단을 보고하고 사용자 로그인 또는 선택을 기다린다. 쿠키·토큰 추출이나 숨겨진 API 호출은 하지 않는다.
내장 도구가 없는 CLI, 또는 사용자가 CDP 경로를 명시한 경우에만 아래 기존 경로를 사용한다.
`--council`은 외부 프로세스 계약이므로 기존 CDP 경로다. IAB 도구가 CLI에서 호출된다고 가정하지 않는다.

## Step 0 — 첫 실행 셋업 (1회, 수동)

Codex에는 설치 훅이 없다. 그래서 pip 의존성(`playwright`·`pyperclip`)은 **1회 직접** 설치한다 — Step 0.5의 `deps=missing` 분기에서
`--check-env --install`로 채운다. repomix는 `npx -y`로 실행되어 사전설치 불필요(Node.js만 있으면 된다).

## Step 0.5 — 환경 온보딩 (브라우저·로그인; 선택지 기반, 막힌 단계만)

먼저 네가 직접 실행한다(사용자에게 시키지 말 것):

```bash
python3 "$PLUGIN_ROOT/bin/pack_and_ask.py" --ensure-env
```

`--ensure-env`는 **저장된 브라우저가 있고 CDP가 닫혀 있으면 조용히 1회 자동 기동**한 뒤 상태를 보고한다
(저장값-only·첫감지 폴백 없음, `browser=wrong`이면 자동기동 안 함). **즉 최초 1회 온보딩 이후엔 브라우저를 다시 묻지 않고 알아서 뜬다.**
마지막 줄 `STATUS node=… deps=… browser=… login=… cookie=… cookie_exp=… saved_browser=… os=… launch_mode=… mode=…`을 파싱한다.
**전부 ok가 아니면**, 막힌 첫 단계를 아래처럼 §A 번호 선택지로 물어보고 → 선택대로 네가 실행 → `--ensure-env`를 다시 돌려 재확인한다(최대 3~4회 반복).

- **`deps=missing`** → 선택지(`의존성`):
  1. 지금 자동 설치 (추천) → 네가 `--check-env --install` 실행
  2. 직접 설치할게요 → `pip install playwright pyperclip` 안내만
  3. 취소
- **`browser=down`** — `--ensure-env`가 저장값 자동기동을 **이미 시도한 뒤**의 상태다. `saved_browser`로 분기한다:
  - **`saved_browser=<이름>`인데도 down** (저장 브라우저 자동기동 **실패** — 보통 프로필 락/앱 이동) → 선택지(`브라우저`):
    1. 다시 시도 (→ `--ensure-env` 재호출) 2. 다른 브라우저로 변경 (→ 아래 감지 분기) 3. 취소. **이때만 묻는다** — 저장값이 있으면 자동기동이 기본이며 매번 새로 묻지 않는다.
  - **`saved_browser=none`** (최초 1회 — 아직 기본 미설정) → 아래 감지 분기로 한 번 묻고 `--launch-browser "<이름>"`로 띄운다(선택 **자동 저장 → 다음 실행부터 무질문 자동기동**).

  사용자에게 물어 직접 띄울 때는 `open -a`가 아니라
  `python3 "$PLUGIN_ROOT/bin/pack_and_ask.py" --launch-browser "<이름>"` (크로스플랫폼 mac/win/linux·전용 프로필·선택 자동 저장)로 한다.
  **항상 전용(격리) 프로필로 실행되므로 사용자 주 브라우저 세션은 건드리지 않는다**(Chrome 136+는 전용 프로필 없이는 CDP가 안 열린다). `BROWSERS …` 라인(설치된 크로미움 목록)으로 분기:
  - **2개 이상 감지** → 선택지(`브라우저`): `BROWSERS`의 각 브라우저를 번호로 준다. 사용자 주 브라우저로
    추정되는 것(현재 실행 중일 가능성)엔 "메인 추정 — 가급적 다른 것" 주석. 선택 → `--launch-browser "<이름>"` → 재점검.
  - **정확히 1개 감지**(그게 사용자 메인일 가능성↑) → 선택지(`브라우저`):
    1. **전용 브라우저 하나 설치 (추천)** → 가벼운 크로미움(Chrome/Brave 등)을 자동화 전용으로 따로 설치하도록 안내
       (ChatGPT Pro 로그인해두고 그 창은 안 건드림). 설치 후 `--launch-browser "<이름>"`.
       *(왜: 메인과 같은 앱을 2창으로 띄우면 빈 프로필·오조작·일부 앱의 멀티인스턴스 불안정으로 혼란이 생긴다.)*
    2. **지금 이 브라우저의 격리 프로필로 진행** → `--launch-browser "<그 이름>"`. 전용 프로필이라 메인과 분리되지만,
       **같은 앱 2창이라 자동화 창은 실수로 건드리지 말 것**을 한 줄 고지.
    3. 취소
  - **0개 감지** → 선택지(`브라우저`): "크로미움 계열 브라우저가 없습니다 — 설치할까요?" → 1. Chrome 설치 안내 2. 취소
- **`browser=wrong`**(포트 점유) → 선택지(`포트충돌`): "9222를 다른 프로세스가 쓰고 있어요. 종료하고 전용 브라우저를 다시 띄울까요?" → 1. 다시 띄우기(점유 프로세스 종료 안내 후 `--launch-browser`) 2. 취소
- **`launch_mode=unset`**(최초 1회) → 선택지(`실행 방식`)로 한 번 물어 `--set-launch-mode <값>`으로 저장한다(이후 재질문 없음):
  1. `background` (권장·기본) — 창을 숨긴 채 실행, 포커스를 안 뺏어 작업 흐름이 안 끊긴다
  2. `foreground` — 창이 뜨고 앞으로 나온다. 진행 상황을 눈으로 보고 싶을 때만
  3. `headless` — **권장 안 함**(아래 참고)

  사용자가 답을 안 주거나 넘기면 **background로 진행**한다(미설정 기본값도 background라 그대로 동작). 값이 이미 있으면 묻지 말 것.
  나중에 바꾸려면 `--set-launch-mode <값>`(env `INSANE_REVIEW_LAUNCH_MODE`가 config보다 우선). 세 모드의 실측(2026-08-26, macOS):
  - `background` **(기본)**: `open -g`로 띄우고, playwright가 새 탭을 만들 때 앱이 앞으로 나오므로 **탭 생성 직후 다시 숨긴다**. ChatGPT는 정상 브라우저로 인식 → **왕복 성공**.
  - `foreground`: 왕복은 되지만 하던 일이 끊긴다.
  - `headless`(`--headless=new`): 창이 아예 없다. **하지만 ChatGPT가 컴포저를 안 내줘 전송이 실패한다**(쿠키가 유효해도 `ChatGPT 컴포저 미확인`으로 재시도 소진 — CF 챌린지 추정). 굳이 쓰려면 `--check-env`로 `login=ok`를 확인하고, 실패하면 즉시 background로 되돌릴 것.
- **`login=no`** (로그인 벽이 실제로 확인된 경우에만 나온다) → 선택지(`로그인`): "방금 띄운 **전용 브라우저 창**에서 **chatgpt.com 로그인 + Pro 추론(최신 플래그십 모델) 선택**을 끝낸 뒤 계속하세요. (전용 프로필이라 이 로그인은 계속 유지됩니다.)"
  1. 로그인 완료 — 계속 → `--ensure-env` 재확인
  2. 취소

  **로그인은 자동 불가 → 반드시 사용자에게 요청**(에러로 끝내지 말 것). background 모드면 창이 숨어 있으니 사용자가 창을 못 찾으면 `--set-launch-mode foreground`로 잠시 바꿔 띄워 준다.
- **`login=unknown`** (컴포저·로그인 벽 모두 미확인 — 로딩 지연/CF 챌린지 가능. **로그인을 요구하지 말 것**):
  - `cookie=ok`면 세션은 살아있는 것 → `--ensure-env`를 1~2회 재실행해 재점검. 계속 unknown이면 사용자에게 "전용 브라우저 창에 챌린지/오류 화면이 떠 있는지 확인" 요청 (재로그인 아님).
  - `cookie=missing|expired`면 그때만 위 `login=no` 분기와 동일하게 로그인 안내.
- **`mode=work`** → ChatGPT의 Chat/Work 토글이 **Work**에 놓여 있다. Work 모드엔 Pro 추론단계가 아예 없다(슬라이더에 Pro 눈금 부재). 본 실행 시 스크립트가 모델 스위처를 열기 **전에** `ensure_chat_mode()`로 Chat으로 자동 전환하고, 전환에 실패하면 `--model pro` 전송을 **fail-closed로 중단**한다. 자동 전환이 반복 실패하면 사용자에게 전용 창에서 토글을 Chat으로 바꿔 달라고 한 줄 요청한다. (`mode=chat`·`mode=unknown`은 통과 — 토글이 없는 구 UI/개인 계정은 애초에 분기가 없다.)
- **`node=missing`** → 선택지(`Node`): "Node.js가 필요합니다(repomix 자동설치에 사용). 설치를 도와드릴까요?" → 1. brew로 설치(`brew install node`) 2. 직접 설치할게요 3. 취소

`STATUS … login=ok`까지 가면 Step 1로. 사용자가 "취소"하면 멈추고 무엇이 남았는지 한 줄로 알려준다.

- **모델 Pro 티어**: 스크립트 `--model pro`가 추론단계 **Pro**를 자동선택·검증한다. Pro 티어는 플래그십 모델에만 존재하므로, 모델명을 못박지 않아도 "현 최신 플래그십 + 최대 추론"이 보장된다(GPT 버전이 올라가도 자동 추종). 안 되면 사용자가 1회 수동 설정하면 새 채팅이 상속. 특정 모델명으로 고정하려면 `--require-model "<이름>"`을 추가(부분 일치; **플래그십이 바뀌면 fail-closed로 전 실행이 차단되니 갱신 필수** — 자동 추종을 원하면 빼라).

## 핵심 절차 (검토/수정/리뷰 요청을 받았을 때)

### 1) 의도 파악
사용자의 요청(또는 직전 대화 맥락)에서 GPT Pro에게 물을 핵심 질문을 한 문장으로 정한다. (버그 원인? 설계 리뷰? 리팩터 방향? 특정 함수 검증?)
타겟/범위가 애매하면 **§A 번호 선택지**를 줘서 고르게 한다(타이핑 요구 금지). 예) `리뷰 대상`: 후보 디렉토리들 + "프로젝트 전체" + "질문만(코드 없이)".

### 2) 타겟 선별 — **완전한 관련 집합을 네가(Codex) 판단** (사용자가 누락을 잡아주는 구조면 안 된다)
"repomix로 무엇을 넣을지 = 무엇이 완전한 관련 집합인지", "repomix만으로 충분한지 vs 관련 파일을 다 넣어야 하는지"의 **판단은 네 책임**이다. 기본은 **"넓게, 빠짐없이"**:
- **단일 모듈/플러그인/기능 리뷰면 그 디렉토리를 통째로** 넣어라(`--target <dir>`, `--include` 생략 또는 광범위). 코드 한 파일만 넣으면 실행지시서·설정·통합 맥락이 빠진다(실측: `bin/**`만 넣어 3파일 → README/SKILL/config 누락).
- 더 넓은 범위면 지목 파일에서 **import/require·호출자·피호출자(grep/LSP)·테스트·타입·설정**까지 추적해 집합을 *닫는다*.
- **패킹 후 `📦 패킹 포함 N개 파일` 감사 목록이 네가 의도한 완전한 집합을 담았는지 직접 확인**한다(§3.5). 사용자가 지적하기 전에 네가 잡아라.
- 결과를 **글롭**(→ `--include "src/auth/**,*.test.ts"`)으로 만든다.
- **코드 리뷰/원인분석은 풀 코드로 보내라 — `--compress` 쓰지 마라.** 압축은 함수 본문(조건·early return·예외·루프 = 버그 판단 근거)을 제거해 리뷰 AI가 구현을 *상상*하게 만든다(실측: 본문 58% 손실 → false-positive·fail-open 폭증). 멀티 AI 합의로 확정.
- 타겟이 너무 커서 컨텍스트를 넘기면 **압축하지 말고 `--include`로 관련 파일만 좁혀 풀로** 보낸다. `--compress`는 오직 "큰 레포 *개요*"(정확성 리뷰 아님)용.

### 3) 패킹 + 투입 + 회수 — 스크립트 실행
```bash
python3 "$PLUGIN_ROOT/bin/pack_and_ask.py" \
  --target <repo_root> --include "<관련 파일 글롭 또는 생략=전체>" \
  --model pro \
  --prompt "<의도를 담은 정확한 질문 — '판정마다 파일/라인/코드조각을 인용하라'를 반드시 포함>"
```
- 응답이 오래 걸려도 되면 그대로(완전추론; `--model pro` 검증 시 최대 대기가 자동 3600s로 상향). 시간을 bound하고 싶으면 `--force-answer-after <초>`로 "거기까지 추론한 내용으로" 답을 받는다. 단독 리뷰는 보통 끄고(완전추론), council은 켜서 cap.

**레포 없이 순수 질문(의견)만:** `--target` 생략 → 프롬프트만 전송.
```bash
python3 "$PLUGIN_ROOT/bin/pack_and_ask.py" --model pro --force-answer-after 90 \
  --prompt "<질문>"
```

### 3.5) 누락 검증 — **빠진 파일 없는지 감사**
패킹 직후 출력의 **`📦 패킹 포함 N개 파일: ...`** 목록이 **의도한 관련 파일을 전부 담았는지** 확인한다. 빠진 게 있으면 repomix가 떨어뜨린 것 — 원인별 대응:
- `🔒 secretlint: 의심 파일 N개 제외` → **시크릿 든 파일이 통째 빠짐**(숨은 누락). 그 파일이 리뷰 대상이면 시크릿을 가린 사본을 따로 넣거나 `--no-security-check`(외부 유출 주의).
- 기본 ignore/`.gitignore`가 떨어뜨림 → `--no-default-patterns`/`--no-gitignore`.
- 서브모듈 파일이 빠짐(부모서 패킹) → 서브모듈 안에서 `--target`.
- `⚠️ pack이 큼(truncation)` 경고 → ChatGPT가 잘라먹을 수 있으니 `--include`로 더 좁히거나 여러 번 나눠 보낸다.
- **손실 플래그 금지**: `--compress`/`--remove-comments`/`--remove-empty-lines`는 내용을 누락시키니 리뷰엔 쓰지 않는다. 라인번호는 기본 ON(인용용).

### 4) 회수 & 반영
- 응답은 **현재 프로젝트의 `.insane-review/response_*.md`**에 저장되고, stdout 끝에 미리보기가 나온다.
- 그 의견을 읽고 **GPT Pro의 의견임을 명시**하여 사용자에게 반영/요약한다(모델명은 리포트 상단 `- 모델:` 라인의 실제 검증된 이름을 인용). 동의/이견을 너의 판단과 함께 제시하라.

### 4.5) 타임아웃·중단 뒤 회수 — `--harvest`
전송은 됐는데 회수를 못 한 경우(최대 대기 초과·프로세스 사망·사용량 한도), **재전송하지 마라**(중복 채팅·Pro 쿼터 낭비). 실패 메시지에 안내된 **결속 대화 URL** 또는 `.insane-review/manifest_*.json`으로 완료된 응답만 회수한다:
```bash
python3 "$PLUGIN_ROOT/bin/pack_and_ask.py" --harvest '<채팅URL 또는 manifest 경로>'
```
manifest는 전송 직후 대화 URL이 결속되는 즉시 원자적으로 기록되므로, 프로세스가 죽어도 항상 회수 가능하다. 사용량 한도(`quota`)로 멈췄으면 한도 해제 후 같은 명령을 다시 돌린다.

## 주의/가드 (실측 기반)

- **git submodule**: 부모 레포 루트에서 서브모듈 파일은 repomix가 제외한다. 서브모듈 안에서 실행하거나 `--target <submodule>` 또는 `--no-gitignore --no-default-patterns`.
- **압축은 코드 파일만** 줄인다(마크다운/문서 위주 폴더엔 무효).
- **정밀 리뷰엔 `--force-answer-after`를 쓰지 마라** — Pro 추론을 중간에 끊어 "다 생각 안 한 채" 답하게 만든다(fail-open과 곱해져 미완성 답을 정답 저장). 완전 추론이 더 정확. 안전장치는 `--max-wait`(기본 20분, Pro 검증 시 60분; env `INSANE_REVIEW_MAX_WAIT`/`INSANE_REVIEW_PRO_MAX_WAIT`)만. force-answer는 빠른 의견·짧은 질문·council cap에만.
- **타임아웃 최후수단(기본 동작)**: 최대 대기 소진 시점에 아직 리즈닝 중이면 스크립트가 자동으로 '지금 답변 받기'를 누르고 `INSANE_REVIEW_FORCE_GRACE`(기본 240s) 추가 대기 후 플러시된 답변을 회수한다 — 장시간 리즈닝 끝에 빈손으로 끝나지 않는다.
- **fail-closed**: 첨부 미확인 / Chat 모드 전환 실패(Work 모드엔 Pro 없음) / 모델·추론단계 미검증(`--model pro` 검증 실패, 또는 `--require-model` 사용 시 모델명 불일치) / 대화 URL 포착 실패(`sent-unknown-location`) / timeout·빈 응답은 **성공 저장 안 하고 중단·재시도**한다(잘못된 컨텍스트나 미완성 답을 리뷰로 저장하지 않음).
- **identity 결속**: 전송 직후 SPA가 발급하는 대화 URL(`/c/<id>`)에 회수를 고정하고(대기 중 이탈하면 자동 복귀), 신규 assistant 턴은 `data-message-id` 차집합으로 판정한다 — 옛 채팅 메시지를 새 응답으로 오인 저장하는 스테일 캡처가 구조적으로 불가. 대화 URL 확보 후의 재시도는 **재전송 없이 같은 채팅에서 회수만** 재시도한다(`not_sent`만 재전송 허용).
- **스톨 복구**: 전송 후 assistant 턴이 빈 채로 스트리밍 표시 없이 `INSANE_REVIEW_STALL_RELOAD`(기본 45s) 이상 멈추면(클라이언트 스트림 유실 — 서버엔 답이 있음) 결속 URL로 재로드해 회수한다(최대 3회, 재전송 아님).
- **사용량 한도 감지**: dialog/alert 표면에서 쿼터 문구를 대조해 `quota`로 조기 종료 — 전송 경로는 재전송 없이 중단, 회수 경로는 재시도 중단 후 `--harvest` 안내. 응답 본문은 스캔하지 않는다(오탐 방지).
- **클립보드 대조**: copy 회수 시 해당 턴 DOM 텍스트와 대조(80자 미만은 전체 일치, 이상은 3조각) — 대기 중 사용자가 다른 것을 복사한 경합을 걸러내고 DOM 폴백.
- **첨부 → 인라인 폴백**: 큰 콘텐츠는 **파일 첨부**가 기본. 첨부가 실패하면 pack이 상한(기본 50,000자, env `INSANE_REVIEW_PASTE_MAX`) 내일 때만 프롬프트에 인라인으로 붙여 보내고, 초과면 fail-closed(잘린 전송 방지). `--attach`는 폴백 없이 첨부만 강제. 패킹 첨부 전송엔 "이번 첨부만 근거로" 가드 한 줄이 자동 부착된다(프로젝트 내 다른 채팅 오염 방지).
- **실행 중 전용 브라우저 창을 조작하지 말 것** — 사용자에게도 한 줄 고지. (background 모드면 창이 숨어 있어 자연히 안전.)
- **스테일 CDP·전용 프로필 자가복구**: 전용 브라우저가 떠 있는 동안 디스크에서 자동 업데이트돼 CDP가 깨지거나(`Browser context management is not supported`), 스테일 인스턴스가 디버그 포트를 막는 싱글톤 교착이면 전용 프로필 프로세스만 재기동(쿠키 디스크 보존 → **로그인 유지**)하고 1회 재연결한다. "로그인 풀림"으로 보이던 상황의 상당수가 이 케이스.
- **브라우저별 프로필 분리**: 크로미움 계열은 앱마다 쿠키 암호화 키가 달라 같은 프로필을 다른 브라우저로 열면 세션이 통째로 깨진다 — 최초 사용 브라우저가 기존 프로필을 소유하고, 다른 브라우저는 접미사 디렉토리를 쓴다.
- **CDP 다이얼로그 핸들링**: ChatGPT 페이지의 JS 다이얼로그(beforeunload 등)가 playwright 기본 auto-dismiss와 레이스해 드라이버가 크래시하던 문제를 자체 핸들러로 차단.
- 실패 시 `--retries N`으로 전송/회수를 재시도(대화 URL 확보 후엔 회수만).

## 채팅 정리 — 폴더명 ChatGPT 프로젝트 (기본 on)
매 실행이 일반 채팅 목록에 쌓이지 않도록, **현재 폴더명(+경로해시)과 같은 이름의 ChatGPT 프로젝트** 안에 채팅을 정리한다. 폴더당 프로젝트 1개로 묶여 일반 목록이 깨끗하게 유지된다.
- 폴더명→프로젝트는 per-repo 캐시(`.insane-review/projects.json`, 레코드=`{url, workspace_id}`)에 저장 → 다음 실행부턴 탐색 없이 바로 그 프로젝트로 들어간다. 동명 다른 폴더(`/a/api`, `/b/api`)도 경로해시·절대경로 키로 분리돼 병합되지 않는다.
- **워크스페이스 결속**: 캐시에 활성 워크스페이스 id(`_account` 쿠키)를 함께 기록한다. 계정이 개인↔팀 워크스페이스로 이동해 캐시의 워크스페이스가 현재와 다르면 죽은 URL을 열어 보지도 않고 즉시 dead 판정 → 현 워크스페이스에서 재탐색/재생성한다. 구형 문자열 캐시는 검증 성공 시 자동 승격.
- **생존 판정 4상태**(`ok/dead/auth/unknown`): 캐시 URL을 열어 ① 그 `g-p-<id>`가 URL에 그대로 있고 ② 접근불가 에러 텍스트가 없고 ③ 컴포저가 있어야 `ok`. `dead`면 즉시 폐기(매 런마다 에러 팝업을 반복하지 않음), `unknown`(로딩 지연 등)이면 캐시를 지우지도 새로 만들지도 않는다.
- **프로젝트 탐색은 API 1순위**: 사이드바 DOM에 프로젝트 링크가 렌더되지 않는 UI에 대응해 `/backend-api/gizmos/snorlax/sidebar`를 in-page fetch로 조회, 표시이름 정확 일치로 홈 URL을 만든다(언어·가상화·접힘 무관). DOM 탐색·생성은 폴백.
- 프로젝트가 없으면 자동 생성, 있으면 재사용(중복 생성 안 함). **프로젝트 미지원 플랜이거나 UI가 바뀌어 실패해도 하드중단 없이 일반 채팅으로 폴백.**
- 이름 바꾸려면 `--project "<이름>"`, 끄려면 `--no-project`.

## 주요 플래그
`--target`(생략=프롬프트only) · `--include`(정밀 글롭) · `--ignore` · `--compress` · `--style xml|markdown|plain` · `--attach` · `--model pro` · `--require-model "<이름>"`(옵트인 고정 핀; `--model`과 함께) · `--force-answer-after N` · `--max-wait N` · `--retries N` · `--harvest <채팅URL|manifest>` · `--browser <이름|경로>`(전용 프로필; 생략=config→첫 감지) · `--launch-browser <이름>`(전용 프로필 실행+저장) · `--list-browsers` · `--set-launch-mode background|foreground|headless` · `--project "<이름>"`(기본=폴더명+해시) · `--no-project` · `--pack-only` · `--delete-pack` · `--out-dir <경로>` · `--check-env [--install]`(순수 점검) · `--ensure-env`(저장 브라우저 자동기동 + 점검) · `--council`

## agent-council 멤버로 쓰기
`references/council-setup.md` 참고. `--council` 모드는 프롬프트를 위치인자로 받고 **응답만 stdout**으로 내보내(진행로그는 stderr) council worker가 그대로 캡처한다. Pro를 웹 전용 council 멤버로 등록하면 다른 모델들과 토론에 참여시킬 수 있다.

## Codex 렌더링 규칙 (질문이 필요할 때)

Codex CLI에는 선택지 카드 UI가 없다. 질문이 반드시 필요하면 `$PLUGIN_ROOT/shared/questioning-policy.md §A` 방식 — 채팅에 번호형 선택지 블록을 출력하고 사용자의 자유 텍스트 답변을 읽는다. 주로 §2c(이미 구체적이면 즉시 진행)가 적용된다. 위 온보딩 분기는 전부 이 규칙으로 렌더한다.
