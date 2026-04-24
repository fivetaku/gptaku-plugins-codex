# 워크플로우 패턴

`gws workflow` 명령어는 여러 Google Workspace 서비스를 결합한 자동화 워크플로우를 제공한다.

```bash
gws workflow +<workflow-name> [flags]
```

---

## 1. standup-report -- 스탠드업 리포트

**설명:** 오늘의 회의 일정 + 미완료 태스크를 스탠드업 요약으로 출력

**사용 서비스:** Calendar, Tasks

```bash
gws workflow +standup-report
gws workflow +standup-report --format table
```

| 플래그 | 기본값 | 설명 |
|--------|--------|------|
| `--format` | json | 출력 형식: json, table, yaml, csv |

**내부 동작:**
1. `gws calendar +agenda --today` -- 오늘 일정 조회
2. `gws tasks tasks list --params '{"tasklist": "@default", "showCompleted": false}'` -- 미완료 태스크 조회
3. 두 결과를 합쳐 스탠드업 요약 생성

- 읽기 전용, 데이터 수정 없음

---

## 2. meeting-prep -- 회의 준비

**설명:** 다음 회의의 의제, 참석자, 관련 문서를 준비

**사용 서비스:** Calendar

```bash
gws workflow +meeting-prep
gws workflow +meeting-prep --calendar Work
```

| 플래그 | 기본값 | 설명 |
|--------|--------|------|
| `--calendar` | primary | 캘린더 ID |
| `--format` | json | 출력 형식 |

**내부 동작:**
1. `gws calendar events list --params '{"calendarId": "primary", "timeMin": "NOW", "maxResults": 1, "singleEvents": true, "orderBy": "startTime"}'` -- 다음 일정 조회
2. 이벤트의 description, attendees, attachments 정보 추출
3. 회의 준비 요약 생성

- 읽기 전용, 데이터 수정 없음

---

## 3. email-to-task -- 이메일을 태스크로 변환

**설명:** Gmail 메시지를 Google Tasks 항목으로 변환

**사용 서비스:** Gmail, Tasks

```bash
gws workflow +email-to-task --message-id <ID>
gws workflow +email-to-task --message-id MSG_ID --tasklist LIST_ID
```

| 플래그 | 필수 | 기본값 | 설명 |
|--------|------|--------|------|
| `--message-id` | O | - | 변환할 Gmail 메시지 ID |
| `--tasklist` | - | @default | 태스크 리스트 ID |

**내부 동작:**
1. `gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'` -- 이메일 조회
2. 제목을 태스크 title로, 본문 스니펫을 notes로 추출
3. `gws tasks tasks insert --params '{"tasklist": "@default"}' --json '{"title": "EMAIL_SUBJECT", "notes": "EMAIL_SNIPPET"}'` -- 태스크 생성

- **write 명령** -- 태스크를 생성하므로 사용자 확인 필요

---

## 4. weekly-digest -- 주간 다이제스트

**설명:** 이번 주 회의 일정 + 읽지 않은 이메일 수 요약

**사용 서비스:** Calendar, Gmail

```bash
gws workflow +weekly-digest
gws workflow +weekly-digest --format table
```

| 플래그 | 기본값 | 설명 |
|--------|--------|------|
| `--format` | json | 출력 형식 |

**내부 동작:**
1. `gws calendar +agenda --week` -- 이번 주 일정 조회
2. `gws gmail +triage` -- 읽지 않은 이메일 요약 조회
3. 두 결과를 합쳐 주간 요약 생성

- 읽기 전용, 데이터 수정 없음

---

## 5. file-announce -- 파일 공유 알림

**설명:** Drive 파일을 Chat 스페이스에 공지

**사용 서비스:** Drive, Chat

```bash
gws workflow +file-announce --file-id <ID> --space <SPACE>
gws workflow +file-announce --file-id FILE_ID --space spaces/ABC123 --message 'Check this out!'
```

| 플래그 | 필수 | 설명 |
|--------|------|------|
| `--file-id` | O | Drive 파일 ID |
| `--space` | O | Chat 스페이스 이름 (예: spaces/SPACE_ID) |
| `--message` | - | 커스텀 공지 메시지 |
| `--format` | - | 출력 형식 |

**내부 동작:**
1. `gws drive files get --params '{"fileId": "FILE_ID"}'` -- 파일 이름/URL 조회
2. 공지 메시지 구성 (파일 이름 + 링크)
3. `gws chat +send --space spaces/ABC123 --text '파일 공유: FILE_NAME - LINK'` -- Chat 메시지 발송

- **write 명령** -- Chat 메시지를 발송하므로 사용자 확인 필요
- `gws drive +upload`로 먼저 파일 업로드 후 이 워크플로우로 공지 가능

---

## 워크플로우 조합 패턴

워크플로우를 수동으로 조합할 수도 있다:

```bash
# 아침 루틴: 스탠드업 + 주간 요약
gws workflow +standup-report --format table
gws workflow +weekly-digest --format table

# 이메일에서 태스크 생성 후 스탠드업에 반영
gws workflow +email-to-task --message-id MSG_ID
gws workflow +standup-report

# 파일 업로드 후 팀에 공지
gws drive +upload ./report.pdf --parent FOLDER_ID
gws workflow +file-announce --file-id FILE_ID --space spaces/TEAM_SPACE
```
