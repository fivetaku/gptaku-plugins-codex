# Calendar (v3)

```bash
gws calendar <resource> <method> [flags]
```

## 헬퍼 명령어

### +agenda -- 다가오는 일정 조회

```bash
gws calendar +agenda
```

| 플래그 | 설명 |
|--------|------|
| `--today` | 오늘 일정만 |
| `--tomorrow` | 내일 일정만 |
| `--week` | 이번 주 일정 |
| `--days <N>` | 앞으로 N일 일정 |
| `--calendar` | 특정 캘린더 필터 (이름 또는 ID) |

```bash
gws calendar +agenda
gws calendar +agenda --today
gws calendar +agenda --week --format table
gws calendar +agenda --days 3 --calendar 'Work'
```

- 읽기 전용, 일정 수정 없음
- 기본적으로 모든 캘린더 조회

### +insert -- 새 일정 생성

```bash
gws calendar +insert --summary <TEXT> --start <TIME> --end <TIME>
```

| 플래그 | 필수 | 기본값 | 설명 |
|--------|------|--------|------|
| `--calendar` | - | primary | 캘린더 ID |
| `--summary` | O | - | 일정 제목 |
| `--start` | O | - | 시작 시간 (ISO 8601) |
| `--end` | O | - | 종료 시간 (ISO 8601) |
| `--location` | - | - | 장소 |
| `--description` | - | - | 설명 |
| `--attendee` | - | - | 참석자 이메일 (여러 번 사용 가능) |

```bash
gws calendar +insert --summary 'Standup' --start '2026-06-17T09:00:00-07:00' --end '2026-06-17T09:30:00-07:00'
gws calendar +insert --summary 'Review' --start '2026-06-17T10:00:00-07:00' --end '2026-06-17T11:00:00-07:00' --attendee alice@example.com
```

- 시간은 RFC3339 형식 사용 (예: `2026-06-17T09:00:00-07:00`)
- 반복 일정, 화상 회의 링크는 직접 API 사용
- **write 명령** -- 실행 전 사용자 확인 필수

## API 리소스

### events

```bash
# 일정 목록
gws calendar events list --params '{"calendarId": "primary", "timeMin": "2026-01-01T00:00:00Z", "timeMax": "2026-01-31T23:59:59Z", "singleEvents": true, "orderBy": "startTime"}'

# 일정 상세
gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'

# 일정 생성 (직접 API)
gws calendar events insert --params '{"calendarId": "primary"}' --json '{
  "summary": "Weekly Standup",
  "start": {"dateTime": "2026-01-20T09:00:00", "timeZone": "Asia/Seoul"},
  "end": {"dateTime": "2026-01-20T09:30:00", "timeZone": "Asia/Seoul"},
  "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO"],
  "attendees": [{"email": "team@company.com"}]
}'

# 일정 수정 (patch)
gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{
  "start": {"dateTime": "2026-01-22T14:00:00", "timeZone": "Asia/Seoul"},
  "end": {"dateTime": "2026-01-22T15:00:00", "timeZone": "Asia/Seoul"}
}'

# 일정 삭제
gws calendar events delete --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}'

# 빠른 일정 추가 (텍스트 기반)
gws calendar events quickAdd --params '{"calendarId": "primary", "text": "Team lunch Friday 12pm"}'

# 반복 일정 인스턴스 조회
gws calendar events instances --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'
```

### calendarList

```bash
# 사용자의 캘린더 목록
gws calendar calendarList list --format table

# 특정 캘린더 정보
gws calendar calendarList get --params '{"calendarId": "primary"}'
```

### freebusy

```bash
# 여유/바쁨 조회
gws calendar freebusy query --json '{
  "timeMin": "2026-01-20T08:00:00Z",
  "timeMax": "2026-01-20T18:00:00Z",
  "items": [{"id": "user1@company.com"}, {"id": "user2@company.com"}]
}'
```

### calendars

```bash
# 보조 캘린더 생성
gws calendar calendars insert --json '{"summary": "Project X"}'

# 캘린더 메타데이터 조회
gws calendar calendars get --params '{"calendarId": "CAL_ID"}'
```

### settings / colors

```bash
# 사용자 설정 조회
gws calendar settings list

# 색상 정의 조회
gws calendar colors get
```

## 시간 형식

모든 시간은 RFC3339 형식:
- `2026-06-17T09:00:00-07:00` (타임존 오프셋)
- `2026-06-17T09:00:00Z` (UTC)
- 종일 이벤트: `{"date": "2026-06-17"}` (dateTime 대신 date 사용)

`sendUpdates` 파라미터 값:
- `all` -- 모든 참석자에게 알림
- `externalOnly` -- 외부 참석자에게만
- `none` -- 알림 없음
