# 레시피 패턴

코어 9개 서비스(Gmail, Calendar, Drive, Sheets, Docs, Slides, Chat, Tasks, Meet)를 활용하는 실전 레시피 모음.
AI가 동적으로 gws 명령어를 조합할 때 이 패턴들을 참고한다.

---

## 1. label-and-archive-emails

**Gmail 라벨 적용 및 보관**
서비스: Gmail

```bash
# 1. 매칭 이메일 검색
gws gmail users messages list --params '{"userId": "me", "q": "from:notifications@service.com"}' --format table

# 2. 라벨 적용
gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"addLabelIds": ["LABEL_ID"]}'

# 3. 보관 (받은편지함에서 제거)
gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"removeLabelIds": ["INBOX"]}'
```

---

## 2. send-personalized-emails

**Sheets 데이터로 개인화 이메일 발송**
서비스: Sheets, Gmail

```bash
# 1. 수신자 목록 읽기
gws sheets +read --spreadsheet SHEET_ID --range 'Contacts!A2:C'

# 2. 각 행별 개인화 이메일 발송
gws gmail +send --to recipient@example.com --subject 'Hello, Name' --body 'Hi Name, your report is ready.'
```

참고: 각 행에서 이름/이메일을 추출하여 반복 실행

---

## 3. draft-email-from-doc

**Google Docs 내용으로 이메일 작성**
서비스: Docs, Gmail

```bash
# 1. 문서 내용 조회
gws docs documents get --params '{"documentId": "DOC_ID"}'

# 2. 본문 텍스트 추출 후 이메일 발송
gws gmail +send --to recipient@example.com --subject 'Newsletter Update' --body 'CONTENT_FROM_DOC'
```

---

## 4. organize-drive-folder

**Drive 폴더 구조 정리**
서비스: Drive

```bash
# 1. 프로젝트 폴더 생성
gws drive files create --json '{"name": "Q2 Project", "mimeType": "application/vnd.google-apps.folder"}'

# 2. 하위 폴더 생성
gws drive files create --json '{"name": "Documents", "mimeType": "application/vnd.google-apps.folder", "parents": ["PARENT_FOLDER_ID"]}'

# 3. 기존 파일 이동
gws drive files update --params '{"fileId": "FILE_ID", "addParents": "FOLDER_ID", "removeParents": "OLD_PARENT_ID"}'

# 4. 구조 확인
gws drive files list --params '{"q": "'FOLDER_ID' in parents"}' --format table
```

---

## 5. email-drive-link

**Drive 파일 공유 후 이메일 링크 전송**
서비스: Drive, Gmail

```bash
# 1. 파일 검색
gws drive files list --params '{"q": "name = '\''Quarterly Report'\''"}'

# 2. 공유 권한 부여
gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "client@example.com"}'

# 3. 링크 이메일 발송
gws gmail +send --to client@example.com --subject 'Quarterly Report' --body 'Report link: https://docs.google.com/document/d/FILE_ID'
```

---

## 6. create-doc-from-template

**템플릿으로 문서 생성 후 공유**
서비스: Drive, Docs

```bash
# 1. 템플릿 복사
gws drive files copy --params '{"fileId": "TEMPLATE_DOC_ID"}' --json '{"name": "Project Brief - Q2"}'

# 2. 내용 추가
gws docs +write --document NEW_DOC_ID --text '## Project: Q2 Launch\n\n### Objective\nLaunch by end of Q2.'

# 3. 팀에 공유
gws drive permissions create --params '{"fileId": "NEW_DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'
```

---

## 7. create-expense-tracker

**비용 추적 스프레드시트 설정**
서비스: Sheets, Drive

```bash
# 1. 스프레드시트 생성
gws drive files create --json '{"name": "Expense Tracker 2025", "mimeType": "application/vnd.google-apps.spreadsheet"}'

# 2. 헤더 추가
gws sheets +append --spreadsheet SHEET_ID --json-values '[["Date", "Category", "Description", "Amount"]]'

# 3. 데이터 입력
gws sheets +append --spreadsheet SHEET_ID --json-values '[["2025-01-15", "Travel", "Flight to NYC", "450.00"]]'

# 4. 관리자에게 공유
gws drive permissions create --params '{"fileId": "SHEET_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "manager@company.com"}'
```

---

## 8. block-focus-time

**집중 시간 반복 일정 생성**
서비스: Calendar

```bash
# 1. 반복 집중 블록 생성
gws calendar events insert --params '{"calendarId": "primary"}' --json '{
  "summary": "Focus Time",
  "description": "Protected deep work block",
  "start": {"dateTime": "2026-01-20T09:00:00", "timeZone": "Asia/Seoul"},
  "end": {"dateTime": "2026-01-20T11:00:00", "timeZone": "Asia/Seoul"},
  "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"],
  "transparency": "opaque"
}'

# 2. 확인
gws calendar +agenda
```

---

## 9. cancel-and-notify

**회의 취소 후 참석자 알림**
서비스: Calendar, Gmail

```bash
# 1. 일정 확인
gws calendar +agenda --format json

# 2. 일정 삭제 (참석자 알림 포함)
gws calendar events delete --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}'

# 3. 후속 이메일 발송
gws gmail +send --to attendees@company.com --subject 'Meeting Cancelled: [Title]' --body 'Apologies, this meeting has been cancelled.'
```

주의: `sendUpdates: "all"`은 모든 참석자에게 취소 알림을 자동 발송

---

## 10. search-and-export-emails

**이메일 검색 및 내보내기**
서비스: Gmail

```bash
# 1. 이메일 검색
gws gmail users messages list --params '{"userId": "me", "q": "from:client@example.com after:2024/01/01"}'

# 2. 메시지 상세 조회
gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'

# 3. JSON으로 내보내기
gws gmail users messages list --params '{"userId": "me", "q": "label:project-x"}' --format json > project-emails.json
```

---

## 11. create-task-list

**태스크 리스트 생성 및 태스크 추가**
서비스: Tasks

```bash
# 1. 리스트 생성
gws tasks tasklists insert --json '{"title": "Q2 Goals"}'

# 2. 태스크 추가
gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Review Q1 metrics", "notes": "Pull data from analytics dashboard", "due": "2026-04-01T00:00:00Z"}'

# 3. 추가 태스크
gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Draft Q2 OKRs"}'

# 4. 태스크 목록 확인
gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format table
```

---

## 12. save-email-attachments

**Gmail 첨부파일을 Drive에 저장**
서비스: Gmail, Drive

```bash
# 1. 첨부파일 있는 이메일 검색
gws gmail users messages list --params '{"userId": "me", "q": "has:attachment from:client@example.com"}' --format table

# 2. 메시지 상세 (첨부파일 ID 확인)
gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID"}'

# 3. 첨부파일 다운로드
gws gmail users messages attachments get --params '{"userId": "me", "messageId": "MESSAGE_ID", "id": "ATTACHMENT_ID"}'

# 4. Drive에 업로드
gws drive +upload ./attachment.pdf --parent FOLDER_ID
```

---

## 13. generate-report-from-sheet

**Sheets 데이터로 Docs 보고서 생성**
서비스: Sheets, Docs, Drive

```bash
# 1. 데이터 읽기
gws sheets +read --spreadsheet SHEET_ID --range 'Sales!A1:D'

# 2. 보고서 문서 생성
gws docs documents create --json '{"title": "Sales Report - January 2025"}'

# 3. 보고서 내용 작성
gws docs +write --document DOC_ID --text '## Sales Report\n\nTotal deals: 45\nRevenue: $125,000'

# 4. 이해관계자에게 공유
gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "cfo@company.com"}'
```

---

## 14. create-presentation

**프레젠테이션 생성 및 공유**
서비스: Slides, Drive

```bash
# 1. 프레젠테이션 생성
gws slides presentations create --json '{"title": "Quarterly Review Q2"}'

# 2. 팀에 공유
gws drive permissions create --params '{"fileId": "PRESENTATION_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'
```

---

## 15. post-mortem-setup

**포스트모템 문서 + 리뷰 일정 + Chat 알림**
서비스: Docs, Calendar, Chat

```bash
# 1. 포스트모템 문서 생성
gws docs documents create --json '{"title": "Post-Mortem: [Incident]"}'
gws docs +write --document DOC_ID --text '## Summary\n\n## Timeline\n\n## Root Cause\n\n## Action Items'

# 2. 리뷰 미팅 일정 잡기
gws calendar +insert --summary 'Post-Mortem Review: [Incident]' --start '2026-01-27T14:00:00+09:00' --end '2026-01-27T15:00:00+09:00' --attendee team@company.com

# 3. Chat으로 알림
gws chat +send --space spaces/ENG_SPACE --text 'Post-mortem scheduled for [Incident]. Doc: https://docs.google.com/document/d/DOC_ID'
```

---

## 동적 조합 참고 사항

- **단계 간 데이터 전달:** 이전 단계의 응답에서 ID (fileId, documentId, eventId 등)를 추출하여 다음 단계에 사용
- **반복 패턴:** Sheets에서 여러 행을 읽고, 각 행에 대해 명령어를 반복 실행하는 패턴이 자주 사용됨
- **서비스 간 연결:** Drive의 fileId는 Docs/Sheets/Slides의 documentId/spreadsheetId/presentationId와 동일
- **권한 관리:** 문서 공유는 항상 Drive permissions API를 통해 수행 (Docs/Sheets/Slides 자체에는 공유 API 없음)
- **write 명령 확인:** 데이터를 생성/수정/삭제하는 단계에서는 반드시 사용자 확인 후 실행
