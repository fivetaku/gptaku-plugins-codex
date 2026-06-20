---
name: nopal
description: Codex용 Google Workspace 오케스트레이션 스킬. "nopal", "/nopal", "gws", "gmail", "calendar", "drive", "sheets", "docs", "slides", "chat", "tasks", "meet", "메일 보내줘", "일정 확인", "회의 준비", "스프레드시트 만들어", "문서/시트/드라이브 작업" 같은 요청에 사용됩니다.
---

# nopal for Codex

Read these first:
- `$PLUGIN_ROOT/skills/nopal/references/gws-shared.md`

Load as needed (필요한 서비스만):
- `$PLUGIN_ROOT/skills/nopal/references/gws-gmail.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-calendar.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-drive.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-docs.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-sheets.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-slides.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-chat.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-tasks.md`
- `$PLUGIN_ROOT/skills/nopal/references/gws-meet.md`
- `$PLUGIN_ROOT/skills/nopal/references/recipes.md`
- `$PLUGIN_ROOT/skills/nopal/references/workflows.md`

Use this skill when the user wants Google Workspace work orchestrated from natural language.

Questioning policy: `shared/questioning-policy.md` §A + §1 + §2c.
- Codex CLI has no AskUserQuestion card UI. When a decision is needed, output numbered-options-in-chat per §A.
- Infer what you can; ask only what is genuinely unknown (§1). If the request is already concrete, skip clarification and proceed (§2c).

---

## 지원 서비스 (9개)

| 서비스 | 헬퍼 명령어 | 주요 용도 |
|--------|------------|----------|
| Gmail | `+send`, `+triage`, `+watch` | 이메일 보내기/읽기/관리 |
| Calendar | `+insert`, `+agenda` | 일정/이벤트 관리 |
| Drive | `+upload` | 파일/폴더/공유 관리 |
| Sheets | `+read`, `+append` | 스프레드시트 읽기/쓰기 |
| Docs | `+write` | 문서 읽기/쓰기 |
| Slides | (직접 API) | 프레젠테이션 생성/편집 |
| Chat | `+send` | 채팅 스페이스/메시지 |
| Tasks | (직접 API) | 할일 목록/태스크 관리 |
| Meet | (직접 API) | 회의 링크 생성/참가자/녹화/스크립트 |

---

## Codex Workflow (5단계)

### Step 0: 환경 확인 (자동)

gws CLI 설치 여부와 인증 상태를 자동으로 확인한다. 사용자에게 묻지 않는다.

**0-1. gws CLI 설치 확인**

`command -v gws` 실행.

- 미설치: `npm install -g @googleworkspace/cli` 자동 설치. 완료 후 `gws --version` 확인.
- 설치 실패 시: `$PLUGIN_ROOT/skills/nopal-setup/SKILL.md` 내용을 기반으로 수동 안내 후 중단.
- 설치된 경우: 0-2로 진행.

**0-2. 인증 상태 확인**

`gws auth status` 실행.

- 인증 안 된 경우: `$PLUGIN_ROOT/skills/nopal-setup/SKILL.md` 기반으로 설정 안내를 채팅에 출력하고 중단. 사용자가 설정 완료 후 재실행하면 0-2부터 재확인 후 Step 1로 진행.
- 인증 완료: Step 1로 진행.

---

### Step 1: 요청 파싱

**요청이 주어진 경우** — 사용자의 자연어 요청을 그대로 오케스트레이션 입력으로 사용하고 Step 2로 진행.

**요청이 없는 경우** — §A 번호 블록으로 채팅에 출력하고 답변을 기다린다:

```
무엇을 도와드릴까요?
1. 자유 요청 (추천) — 하고 싶은 작업을 자유롭게 말씀해주세요
2. 오늘 일정 확인 — Google Calendar 오늘 일정 조회
3. 이메일 확인 — Gmail 최근 읽지 않은 이메일 확인
4. 사용법 안내 — Nopal이 할 수 있는 일과 예시
```

- 1 또는 자유 입력 → 입력 텍스트를 요청으로 사용, Step 2로 진행
- 2 → "오늘 일정을 확인해줘"로 설정, Step 2로 진행
- 3 → "읽지 않은 이메일을 확인해줘"로 설정, Step 2로 진행
- 4 → 아래 안내를 채팅에 출력하고 종료:

```
Nopal — Google Workspace 9개 서비스 자연어 오케스트레이션

지원: Gmail, Calendar, Drive, Sheets, Docs, Slides, Chat, Tasks, Meet

예시:
  내일 오전 10시에 팀 회의 잡아줘
  지난주 매출 스프레드시트에서 합계 구해줘
  회의록을 Google Docs로 만들고 참석자에게 공유해줘
  읽지 않은 이메일 중 중요한 것만 요약해줘
  내일 회의 참석자 목록을 스프레드시트로 만들고 각자에게 메일로 안건 보내줘
```

---

### Step 2: 의도 파악

**2-1. 필요한 서비스 식별**

| 키워드/의도 | 매핑 서비스 |
|------------|-----------|
| 메일, 이메일, 보내, 수신, 답장 | Gmail |
| 일정, 회의, 미팅, 약속, 캘린더, 스케줄 | Calendar |
| 파일, 폴더, 업로드, 다운로드, 공유, 드라이브 | Drive |
| 스프레드시트, 엑셀, 표, 데이터, 시트, 합계, 매출 | Sheets |
| 문서, 글, 작성, 편집, 보고서, 회의록 | Docs |
| 발표, 슬라이드, 프레젠테이션, PPT | Slides |
| 채팅, 메시지, 알림 | Chat |
| 할일, 태스크, 체크리스트, 투두 | Tasks |
| 화상회의, 미트, 회의 링크, 녹화, 참가자, 스크립트 | Meet |

하나의 요청에 여러 서비스가 관여할 수 있다. 예: "회의 참석자에게 메일 보내줘" → Calendar + Gmail

**2-2. 실행 유형 판별**

| 유형 | 설명 | 예시 |
|------|------|------|
| 단순 조회 | 정보만 읽기 | "오늘 일정 알려줘" |
| 단순 실행 | 한 서비스 동작 | "메일 보내줘" |
| 복합 조합 | 여러 서비스 체이닝 | "회의록 작성 후 참석자에게 공유" |

---

### Step 3: 인터뷰 (부족한 정보 수집)

**원칙 (§1 + §2c): 추론 가능한 건 묻지 않는다. 요청이 이미 구체적이면 즉시 Step 4로 진행.**

**3-1. 정보 갭 분석 (내부 처리)**

요청 실행에 필요한 파라미터를 확인한다. 기본값으로 해결 가능한 것은 묻지 않는다:
- 회의 시간: 기본 1시간
- 이메일 형식: 기본 일반 텍스트
- 파일 공유 권한: 기본 "보기 가능"

**3-2. GWS 데이터 선조회 후 선택지 제시**

가능하면 Google Workspace에서 데이터를 먼저 조회하여 선택지에 반영한다.

예 — "어떤 회의를 준비할까요?" 대신 `gws calendar +agenda --days 3 --format json` 먼저 실행 후:

```
어떤 회의를 준비할까요?
1. 내일 10:00 — 주간 스탠드업 (참석자 5명, Google Meet)
2. 내일 14:00 — 프로젝트 리뷰 (참석자 3명, 회의실 B)
3. 모레 09:00 — 전체 회의 (참석자 12명, 대회의실)
4. 직접 입력해주세요
```

**3-3. 인터뷰 패턴**

부족한 파라미터가 있을 때만 §A 번호 블록으로 질문한다. 한 번에 묶어서 최대한 라운드트립을 줄인다.

```
예: 요청 "회의 준비해줘"
→ [Calendar 조회 후] 번호 블록으로 회의 목록 제시
→ "자료도 공유할까요? 1. 네  2. 아니오"
→ "참석자에게 메일도 보낼까요? 1. 네  2. 아니오"

예: 요청 "보고서 보내줘"
→ [Drive 조회 후] 번호 블록으로 최근 파일 목록 제시
→ "누구에게 보낼까요? (이메일 주소를 적어주세요)"

예: 요청 "이번 주 할일 정리해줘"
→ [Tasks 조회 후] 바로 정리 (추가 질문 불필요)
```

---

### Step 4: 계획 수립 및 확인

**4-1. 레퍼런스 로딩**

필요한 서비스의 reference 파일만 선택적으로 읽는다:

```
$PLUGIN_ROOT/skills/nopal/references/gws-shared.md   (항상)
$PLUGIN_ROOT/skills/nopal/references/gws-{서비스명}.md  (필요한 것만)
```

`workflows.md`, `recipes.md`가 있으면 검증된 패턴을 우선 사용한다. 없어도 동적으로 새 조합을 생성할 수 있다.

**4-2. ExecutionPlan 동적 생성**

| 필드 | 설명 |
|------|------|
| order | 실행 순서 |
| service | 사용하는 서비스 |
| command | 실제 gws 명령어 |
| depends_on | 이전 단계 의존 여부 |
| description | 이 단계가 하는 일 (한글) |

예시:
```
| # | 서비스 | 작업 | 의존 |
|---|--------|------|------|
| 1 | Calendar | 내일 일정 조회 | - |
| 2 | Docs | 회의록 문서 생성 | - |
| 3 | Drive | 문서를 참석자에게 공유 | 1, 2 |
| 4 | Gmail | 참석자에게 회의록 링크 메일 발송 | 1, 2, 3 |
```

**4-3. 사용자 확인 (조건부)**

| 실행 유형 | 확인 |
|-----------|------|
| 단순 조회 (read-only) | 생략 → 바로 Step 5 |
| 단순 실행 (write 1개) | 확인 필요 |
| 복합 조합 (2+ 서비스) | 확인 필요 |

단순 조회 판별: 서비스 1개, 명령어가 `list`/`get`/`+triage`/`+agenda` 등 읽기 전용, 쓰기 동작 없음.

쓰기/복합 작업은 계획 테이블을 채팅에 보여주고 §A 번호 블록으로 확인받는다:

```
이렇게 실행할까요?
[계획 테이블]

1. 네, 실행해주세요 (추천)
2. 수정할 부분이 있어요 — 변경하고 싶은 단계를 알려주세요
3. 취소
```

- 1 → Step 5로 진행
- 2 → 피드백 반영 후 계획 재수립
- 3 → 종료

---

### Step 5: 실행

**5-1. 명령어 실행 규칙**

| 규칙 | 설명 |
|------|------|
| 헬퍼 우선 | 헬퍼(`+send`, `+agenda` 등)가 있으면 헬퍼 사용 |
| JSON 출력 | `--format json` 플래그 항상 사용 |
| 결과 파싱 | 각 단계 후 JSON에서 다음 단계에 필요한 ID/값 추출 |
| 에러 격리 | 한 단계 실패해도 나머지 단계는 계속 진행 |

**5-2. 서비스별 명령어 가이드**

#### Gmail

**한글 이메일 발송 — RFC 2047 인코딩 필수:**

`gws gmail +send`는 한글 제목을 인코딩하지 않아 수신 시 깨진다.
한글이 포함된 메일은 반드시 아래 raw API 방식을 사용한다.

```bash
RAW=$(node -e "
const to='user@example.com';
const subject='한글 제목';
const body='한글 본문 내용';
const mime=[
  'MIME-Version: 1.0',
  'Content-Type: text/plain; charset=utf-8',
  'Content-Transfer-Encoding: base64',
  'To: '+to,
  'Subject: =?UTF-8?B?'+Buffer.from(subject).toString('base64')+'?=',
  '',
  Buffer.from(body).toString('base64')
].join('\r\n');
process.stdout.write(Buffer.from(mime).toString('base64url'));
")
gws gmail users messages send --params '{"userId":"me"}' --json "{\"raw\":\"$RAW\"}"
```

```bash
# 이메일 목록 조회 (안 읽은 메일)
gws gmail +triage --format json
# 최근 메일 전체 (명시적으로 "안 읽은 메일"이라고 하지 않은 경우)
gws gmail +triage --max 10 --query 'newer_than:1d' --format json
# 특정 조건 검색
gws gmail +triage --max 10 --query 'from:boss' --format json
# 이메일 상세 읽기
gws gmail users messages get --params '{"userId":"me","id":"MESSAGE_ID"}' --format json
# 이메일 휴지통 이동
gws gmail users messages trash --params '{"userId":"me","id":"MESSAGE_ID"}'
```

#### Calendar

```bash
# 일정 조회 (헬퍼)
gws calendar +agenda --days 7 --format json

# 일정 생성 (헬퍼) — --summary (NOT --title)
gws calendar +insert --summary "회의 제목" --start "2026-03-06T14:00:00+09:00" --end "2026-03-06T15:00:00+09:00"
gws calendar +insert --summary "팀 미팅" --start "2026-03-06T14:00:00+09:00" --end "2026-03-06T15:00:00+09:00" --attendee "alice@example.com" --location "회의실 B"

# 일정 생성 (참석자 여럿, 직접 API)
gws calendar events insert --params '{"calendarId": "primary"}' --json '{
  "summary": "팀 회의",
  "start": {"dateTime": "2026-03-06T14:00:00+09:00"},
  "end": {"dateTime": "2026-03-06T15:00:00+09:00"},
  "attendees": [{"email": "alice@example.com"}, {"email": "bob@example.com"}]
}' --format json

# 일정 수정
gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID"}' --json '{"summary": "수정된 제목"}' --format json

# 일정 삭제
gws calendar events delete --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'
```

#### Drive

```bash
# 파일 업로드 (헬퍼) — 파일 경로는 위치 인자 (--file 아님)
gws drive +upload /path/to/file.pdf
gws drive +upload /path/to/file.pdf --parent FOLDER_ID --name "새이름.pdf"

# 파일 목록 조회
gws drive files list --params '{"q": "name contains '\''Report'\''", "pageSize": 10}' --format json

# 파일 공유 (권한 추가)
gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{
  "role": "reader", "type": "user", "emailAddress": "user@example.com"
}' --format json

# 폴더 생성
gws drive files create --json '{"name": "새 폴더", "mimeType": "application/vnd.google-apps.folder"}' --format json
```

#### Sheets

```bash
# 시트 읽기 (헬퍼) — --spreadsheet (NOT --spreadsheet-id)
gws sheets +read --spreadsheet "SHEET_ID" --range "A1:D10" --format json

# 데이터 추가 (헬퍼)
gws sheets +append --spreadsheet "SHEET_ID" --values '이름,점수,홍길동,95'
gws sheets +append --spreadsheet "SHEET_ID" --json-values '[["이름","점수"],["홍길동","95"]]'

# 새 스프레드시트 생성
gws sheets spreadsheets create --json '{"properties": {"title": "매출 보고서"}}' --format json

# 셀 값 업데이트
gws sheets spreadsheets.values update \
  --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1:B2", "valueInputOption": "USER_ENTERED"}' \
  --json '{"values": [["이름", "점수"], ["홍길동", "95"]]}' --format json
```

#### Docs

```bash
# 문서에 텍스트 추가 (헬퍼) — 기존 문서 끝에 삽입
gws docs +write --document "DOC_ID" --text "회의 내용..."

# 문서 읽기
gws docs documents get --params '{"documentId": "DOC_ID"}' --format json

# 새 문서 생성
gws docs documents create --json '{"title": "프로젝트 보고서"}' --format json

# 문서에 텍스트 삽입 (직접 API)
gws docs documents batchUpdate --params '{"documentId": "DOC_ID"}' --json '{
  "requests": [{"insertText": {"location": {"index": 1}, "text": "삽입할 텍스트"}}]
}' --format json
```

#### Slides

```bash
# 새 프레젠테이션 생성
gws slides presentations create --json '{"title": "분기 발표"}' --format json

# 슬라이드 추가
gws slides presentations batchUpdate --params '{"presentationId": "PRES_ID"}' --json '{
  "requests": [{"createSlide": {"slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"}}}]
}' --format json

# 프레젠테이션 읽기
gws slides presentations get --params '{"presentationId": "PRES_ID"}' --format json
```

#### Chat

```bash
# 메시지 보내기 (헬퍼)
gws chat +send --space "spaces/SPACE_ID" --text "안녕하세요"

# 스페이스 목록 조회
gws chat spaces list --format json

# 메시지 목록 조회
gws chat spaces.messages list --params '{"parent": "spaces/SPACE_ID"}' --format json
```

#### Tasks

```bash
# 태스크 목록 조회
gws tasks tasklists list --format json
gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format json

# 태스크 생성
gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{
  "title": "보고서 작성", "due": "2026-03-10T00:00:00Z", "notes": "분기 매출 보고서"
}' --format json

# 태스크 완료 처리
gws tasks tasks patch --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}' \
  --json '{"status": "completed"}' --format json
```

#### Meet

```bash
# 회의 공간(링크) 생성
gws meet spaces create --json '{}' --format json

# 회의 공간 조회
gws meet spaces get --params '{"name": "spaces/SPACE_ID"}' --format json

# 회의 기록 목록
gws meet conferenceRecords list --format json

# 회의 참가자 조회
gws meet conferenceRecords.participants list --params '{"parent": "conferenceRecords/RECORD_ID"}' --format json

# 회의 녹화 조회
gws meet conferenceRecords.recordings list --params '{"parent": "conferenceRecords/RECORD_ID"}' --format json

# 회의 스크립트 조회
gws meet conferenceRecords.transcripts list --params '{"parent": "conferenceRecords/RECORD_ID"}' --format json

# 진행 중인 회의 종료
gws meet spaces endActiveConference --params '{"name": "spaces/SPACE_ID"}' --format json
```

**5-3. 결과 체이닝 패턴**

```bash
# 예: 파일 생성 → 공유
FILE_ID=$(gws docs documents create --json '{"title": "회의록"}' --format json | jq -r '.documentId')
gws drive permissions create --params "{\"fileId\": \"$FILE_ID\"}" --json '{
  "role": "writer", "type": "user", "emailAddress": "colleague@example.com"
}' --format json
```

```bash
# 예: 일정 조회 → 참석자 추출 → 메일 발송
ATTENDEES=$(gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}' --format json | jq -r '.attendees[].email')
for EMAIL in $ATTENDEES; do
  gws gmail +send --to "$EMAIL" --subject "회의 안건" --body "내일 회의 안건입니다."
done
```

**5-4. 에러 처리**

실행 중 에러 발생 시:
1. 실패한 단계를 기록 (명령어, 에러 메시지).
2. 해당 단계에 의존하는 후속 단계도 스킵.
3. 의존하지 않는 나머지 단계는 계속 진행.
4. 전체를 중단하지 않는다.

---

### Step 6: 결과 요약

모든 단계 완료 후 사람이 읽기 쉬운 통합 리포트를 채팅에 제공한다. 원시 JSON 출력 금지.

```
## 실행 결과

### 완료된 작업
1. Calendar: 내일 오후 2시에 "팀 회의" 일정 생성 완료
   - 참석자: alice@example.com, bob@example.com
   - Google Meet 링크: https://meet.google.com/xxx-xxxx-xxx

2. Docs: "팀 회의 안건" 문서 생성 완료
   - 문서 링크: https://docs.google.com/document/d/xxx

3. Gmail: 참석자 2명에게 회의 안건 메일 발송 완료

### 실패한 작업
(없음)

### 다음에 할 수 있는 작업
- "회의 끝나면 회의록 정리해줘"
```

리포트 규칙: 생성된 리소스의 직접 링크 포함 / 성공·실패 명확히 구분 / 실패 시 원인 + 해결 방법 안내 / 후속 액션 제안은 의미 있을 때만 (0개 OK) / JSON 덤프 금지.

---

## 절대 하지 마 (DO NOT)

1. gws CLI를 거치지 않고 Google API를 직접 HTTP 호출하지 마.
2. OAuth 토큰이나 API 키를 하드코딩하지 마.
3. references/ 파일을 실행 시점에 전부 읽지 마. 필요한 서비스만 선택적으로 읽는다.
4. 사용자에게 gws 명령어를 직접 타이핑하라고 안내하지 마. Nopal이 Bash로 대신 실행한다.
5. 프리셋 패턴에 없다고 거부하지 마. 동적으로 새 조합을 생성한다.
6. 실행 중 에러가 나면 전체를 중단하지 마. 실패한 단계만 보고하고 나머지는 계속 진행.
7. gws CLI 미설치 시 안내만 하지 마. `npm install -g @googleworkspace/cli`로 자동 설치한다.
8. 원시 JSON을 결과로 출력하지 마.
9. 단순 조회를 확인 없이 바로 실행하는 것은 괜찮다 — 읽기 전용은 확인을 생략한다.
10. 존재하지 않는 AskUserQuestion 카드 UI를 가정하지 마. 반드시 §A 번호 블록을 채팅에 출력한다.

## 항상 해 (ALWAYS DO)

1. 실행 시 `gws auth status`로 인증 상태를 먼저 확인한다.
2. 추론 가능한 건 묻지 않는다. 요청이 이미 구체적이면 즉시 실행한다 (§2c).
3. 명확화가 필요하면 §A 번호 블록을 채팅에 출력한다. 열린 텍스트 질문은 핵심 의도 파악 시만.
4. 쓰기/복합 작업은 계획을 보여주고 확인받은 후 실행한다.
5. 각 gws 명령어 실행 후 결과를 파싱하여 다음 단계에 필요한 ID/값을 추출한다.
6. 최종 결과를 사람이 읽기 쉬운 요약으로 정리한다.
7. 에러 발생 시 친절한 한글 메시지로 안내하고 해결 방법을 제시한다.
8. 헬퍼 명령어가 있는 서비스는 헬퍼를 우선 사용한다.
9. `--format json`을 사용하여 구조화된 출력을 획득한다.
10. 실행 결과에 생성된 리소스의 직접 링크를 포함한다.

---

## 복합 조합 예시

### 예시 1: 회의 준비 자동화

요청: "내일 팀 회의 준비해줘"

```
ExecutionPlan:
| # | 서비스 | 작업 | 의존 |
|---|--------|------|------|
| 1 | Calendar | 내일 팀 회의 일정 조회 | - |
| 2 | Docs | 회의 안건 문서 생성 | 1 |
| 3 | Drive | 문서를 참석자에게 공유 | 1, 2 |
| 4 | Gmail | 참석자에게 안건 메일 발송 | 1, 2, 3 |
```

```bash
gws calendar +agenda --days 2 --format json
DOC_ID=$(gws docs documents create --json '{"title": "팀 회의 안건 - 2026-03-06"}' --format json | jq -r '.documentId')
gws drive permissions create --params "{\"fileId\": \"$DOC_ID\"}" --json '{"role": "writer", "type": "user", "emailAddress": "alice@example.com"}' --format json
gws gmail +send --to "alice@example.com" --subject "내일 팀 회의 안건" --body "안건 문서: https://docs.google.com/document/d/$DOC_ID"
```

### 예시 2: 주간 보고서 자동화

요청: "이번 주 매출 시트에서 합계 구하고 보고서 만들어서 팀장에게 보내줘"

```bash
SALES_DATA=$(gws sheets +read --spreadsheet "SHEET_ID" --range "A1:D50" --format json)
DOC_ID=$(gws docs documents create --json '{"title":"주간 매출 보고서 - 2026 W10"}' --format json | jq -r '.documentId')
gws docs +write --document "$DOC_ID" --text "이번 주 매출 요약..."
gws gmail +send --to "manager@example.com" --subject "주간 매출 보고서" --body "보고서: https://docs.google.com/document/d/$DOC_ID"
```

### 예시 3: 할일 관리

요청: "오늘 마감인 할일 확인하고 못 끝낸 거 내일로 옮겨줘"

```bash
gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format json
gws tasks tasks patch --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}' --json '{"due": "2026-03-06T00:00:00Z"}' --format json
```
