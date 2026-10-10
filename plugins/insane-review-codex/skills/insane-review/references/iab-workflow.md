# Codex Desktop 내장 Browser/IAB 실행

이 경로는 Codex가 로컬 준비 → 현재 세션 브라우저 조작 → 로컬 기록을 수행한다.
`iab_review.py`는 브라우저 드라이버가 아니다. Python에서 IAB의 포트를 탐지하거나 CDP로 연결하지 않는다.
로그인·Pro 선택·첨부·완료 표시는 실제 UI 근거로 판단하며, 로컬 상태 기록만으로 성공을 선언하지 않는다.

## 1. 범위와 로컬 준비

SKILL의 의도 파악/타겟 선별 규칙을 적용한다. 공개되지 않은 시크릿은 포함하지 않는다.
질문을 UTF-8 파일로 저장하고 실행한다(순수 질문은 `--target` 생략):

```bash
python3 "$PLUGIN_ROOT/bin/iab_review.py" prepare \
  --target <repo_root> --include '<관련 글롭 또는 생략=전체>' \
  --prompt-file <질문파일> --out-dir <작업폴더/.insane-review>
```

출력 manifest를 읽는다. `state=prepared`는 전송 전 상태다.
`pack`과 `prompt`는 절대경로다. 기존 repomix 엔진의 포함 파일 감사 목록을 확인한다.
Node/repomix는 코드 패킹에만 필요하다. IAB 경로에 playwright/pyperclip 설치나 별도 브라우저 온보딩은 필요 없다.

## 2. 내장 브라우저와 로그인 확인

첫 `cua_repl` 호출은 현재 도구 계약의 진입 호출 하나만 실행한다.
사용자 지정 탭이 없으면 `await cua.getBrowser({id: "iab"})`로 시작하고 반환된 문서를 읽는다.
이후 `cua.listTabs({browser: "iab"})`로 실제 탭을 확인한다.
사용자가 지정한 탭은 그대로 사용하되, 작성 중인 입력이나 생성 중인 응답을 덮어쓰지 않는다.
일반 실행은 기존 ChatGPT 탭에서 로그인 상태만 확인하고 리뷰용 새 탭을 만든다:
`await cua.createBrowserTab("iab", "https://chatgpt.com/", {visible: false})`.
기존 탭의 진행 중 대화를 리뷰용으로 재사용하지 않는다.

새 탭의 `getAXState()` 또는 `playwright.domSnapshot()`을 읽고 로그인 벽/컴포저를 확인한다.
로딩 미완료는 로그아웃으로 단정하지 않는다. 실제 로그인 벽이면 사용자에게 해당 탭 로그인을 요청한다.
인증 정보·쿠키를 읽거나 다른 브라우저 프로필에서 가져오지 않는다.
UI의 Chat/Work 토글이 있으면 Chat으로 전환한다. 모델 메뉴를 열어 **실제 모델명 + Pro 추론단계**를 선택하고
선택된 상태를 다시 확인한다. UI에 Pro가 없거나 선택을 확인할 수 없으면 전송을 중단한다.
모델 이름/셀렉터/AX 인덱스는 매 실행의 화면에서 얻는다. 옛 GPT 버전이나 고정 인덱스를 가정하지 않는다.
프로젝트 그룹핑이 필요하면 보이는 프로젝트 UI로 선택한다. IAB는 CDP의 쿠키 기반 캐시나 backend API를 사용하지 않는다.
프로젝트 미지원 시 일반 새 채팅을 사용하고 그 사실을 기록한다.

## 3. 첨부와 전송 결속

`pack`이 있으면 현재 런타임의 `file-uploads` 문서를 읽는다.
문서가 제공하는 파일 선택 API를 사용하고 chooser 이벤트는 첨부 버튼 클릭 **전에** 구독한다.
파일명과 업로드 완료/오류를 화면에서 확인한 뒤 전송한다. 확인되지 않은 첨부는 보내지 않는다.
작은 pack의 인라인 대체는 전체 내용을 넣고 길이/컴포저 반영을 확인할 때만 허용한다.
상한은 기존 `INSANE_REVIEW_PASTE_MAX`(기본 50,000자)이며, `--attach`에 준하는 첨부 강제 요청에는 대체하지 않는다.

전송 전 assistant `data-message-id` 목록을 **실제 렌더된 DOM**에서 읽어 JSON 배열 파일로 저장한다.
DOM에 ID가 노출되지 않으면 신뢰할 결속 근거가 없으므로 중단한다.
확인한 모델명/Pro 상태와 탭 ID를 사용해 **전송 버튼 클릭 전에** 기록한다:

```bash
python3 "$PLUGIN_ROOT/bin/iab_review.py" begin --manifest <manifest> \
  --tab-id <실제탭ID> --model '<화면에서 확인한 모델명>' --effort pro \
  --baseline-file <전송전ID목록.json>
```

`state=sending`부터 자동 재전송은 금지한다. 컴포저에 manifest의 `prompt` 내용을 입력하고 전송한다.
사용자 메시지의 내용/첨부와 신규 message ID를 확인하고 실제 `/c/<id>` URL을 얻는 즉시 기록한다:

```bash
python3 "$PLUGIN_ROOT/bin/iab_review.py" bind --manifest <manifest> \
  --chat-url '<실제대화URL>' --user-message-id <전송된사용자메시지ID>
```

`bind` 실패나 URL 미확보는 성공이 아니다. `sending` manifest와 탭을 보존하고 현재 상태를 확인한다.
prepared로 되돌리거나 같은 질문을 다시 보내지 않는다. 수동 확인 없이 `sending`을 새 실행으로 대체하지 않는다.

## 4. 완료 판정과 회수

동일 탭/결속 URL에서 baseline에 없고 전송된 사용자 턴 **뒤에 있는** assistant message ID만 대상으로 삼는다.
그 턴의 완료 표시(예: 복사 컨트롤), 생성/추론 중 표시 종료, 연속 관찰의 본문 안정화를 함께 확인한다.
한 번 본 텍스트, 예전 복사 버튼, 숨겨진 추론 텍스트를 완료 응답으로 저장하지 않는다.
조회는 짧게 나눠 다른 유효한 작업과 진행 보고를 이어간다. 도구가 제공하지 않는 자동 재개를 약속하지 않는다.
Pro의 기본 최대 대기는 60분이며 사용자 지정 제한을 우선한다. 정밀 리뷰는 '지금 답변 받기'로 추론을 강제 종료하지 않는다.
한도/타임아웃/중단이면 manifest와 탭을 보존하고 미완료를 보고한다.

완료 턴의 실제 보이는 응답을 읽어 UTF-8 임시 파일로 저장한다. `evaluate`는 읽기 전용 DOM 조회만 사용하며
숨겨진 API, 네트워크 요청, 페이지 상태 변경으로 대체하지 않는다. 복사 경로를 쓰면 해당 턴 본문과 대조한다.

```bash
python3 "$PLUGIN_ROOT/bin/iab_review.py" complete --manifest <manifest> \
  --chat-url '<결속대화URL>' --message-id <신규assistantID> \
  --response-file <실제로회수한본문.txt> --completion-observed
```

`--completion-observed`는 Codex가 UI에서 확인했다는 선언이며, 도구 자체가 브라우저를 검증하는 옵션이 아니다.
완료 파일과 `state=complete`를 다시 읽고 실제 모델명·대화 URL·GPT 의견을 명시해 검토 결과를 전달한다.
GPT 의견은 원문/테스트와 대조해 판단한다. 브라우저에서 변경한 결과의 캡처는 현재 런타임 지침에 따라 남긴다.

## 5. 중단 뒤 재개

IAB manifest는 Python CDP의 `--harvest`에 넣지 않는다.
`sent` 상태면 manifest의 `tab_id`를 다시 바인딩하고, 탭이 없으면 동일 `chat_url`을 새 IAB 탭에서 연다.
위 완료 판정 후 `complete`만 실행한다. 모델 재선택이나 질문 재전송은 하지 않는다.
`sending` 상태면 기존 탭에서 사용자 턴과 URL을 찾아 `bind`부터 복구한다. 확인 불가면 미확정으로 남긴다.
대기가 남은 탭은 현재 도구가 지원하는 `markHandoff()`로 보존하고, 완료된 임시 탭은 정리한다.
