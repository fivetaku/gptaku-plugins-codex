# Gmail (v1)

```bash
gws gmail <resource> <method> [flags]
```

## 헬퍼 명령어

### +send -- 이메일 발송 (ASCII 전용)

> **주의:** `+send`는 한글 등 non-ASCII 문자를 RFC 2047 인코딩하지 않아 수신 시 깨진다.
> **한글이 포함된 메일은 반드시 아래 raw API 방식을 사용한다.**

```bash
# ASCII 전용 (영문만)
gws gmail +send --to <EMAIL> --subject <SUBJECT> --body <TEXT>
```

- **write 명령** -- 실행 전 사용자 확인 필수

### 한글 이메일 발송 (raw API — 권장)

```bash
RAW=$(node -e "
const to='user@example.com';
const subject='한글 제목';
const body='한글 본문 내용';
const cc='';  // CC가 있으면 이메일 입력
const mime=[
  'MIME-Version: 1.0',
  'Content-Type: text/plain; charset=utf-8',
  'Content-Transfer-Encoding: base64',
  'To: '+to,
  cc ? 'Cc: '+cc : null,
  'Subject: =?UTF-8?B?'+Buffer.from(subject).toString('base64')+'?=',
  '',
  Buffer.from(body).toString('base64')
].filter(Boolean).join('\r\n');
process.stdout.write(Buffer.from(mime).toString('base64url'));
")
gws gmail users messages send --params '{"userId":"me"}' --json "{\"raw\":\"$RAW\"}"
```

- RFC 2047 + base64url 인코딩으로 한글 제목/본문 완벽 지원
- CC/BCC: `cc`, `bcc` 변수에 이메일 입력
- **write 명령** -- 실행 전 사용자 확인 필수

### +triage -- 받은편지함 요약

```bash
gws gmail +triage
```

| 플래그 | 기본값 | 설명 |
|--------|--------|------|
| `--max` | 20 | 최대 메시지 수 |
| `--query` | is:unread | Gmail 검색 쿼리 |
| `--labels` | - | 라벨 이름 포함 |

```bash
gws gmail +triage
gws gmail +triage --max 5 --query 'from:boss'
gws gmail +triage --format json | jq '.[].subject'
gws gmail +triage --labels
```

- 읽기 전용, 메일함 수정 없음
- 기본 출력은 table 형식

### +watch -- 새 이메일 스트리밍

```bash
gws gmail +watch --project <GCP_PROJECT_ID>
```

| 플래그 | 기본값 | 설명 |
|--------|--------|------|
| `--project` | - | GCP 프로젝트 ID (Pub/Sub용) |
| `--subscription` | - | 기존 Pub/Sub 구독 이름 |
| `--topic` | - | 기존 Pub/Sub 토픽 |
| `--label-ids` | - | 필터할 Gmail 라벨 ID (쉼표 구분) |
| `--max-messages` | 10 | pull 배치당 최대 메시지 |
| `--poll-interval` | 5 | pull 간격 (초) |
| `--msg-format` | full | 메시지 형식: full, metadata, minimal, raw |
| `--once` | - | 한 번 pull 후 종료 |
| `--cleanup` | - | 종료 시 Pub/Sub 리소스 삭제 |
| `--output-dir` | - | 메시지를 개별 JSON 파일로 저장 |

```bash
gws gmail +watch --project my-gcp-project
gws gmail +watch --project my-project --label-ids INBOX --once
gws gmail +watch --project my-project --cleanup --output-dir ./emails
```

- watch는 7일 후 만료 -- 재실행으로 갱신
- `--cleanup` 없으면 Pub/Sub 리소스 유지 (재연결용)

## API 리소스

### users

| 메서드 | 설명 |
|--------|------|
| `getProfile` | 현재 사용자 Gmail 프로필 |
| `stop` | push 알림 중지 |
| `watch` | push 알림 설정 |

### users.messages

```bash
# 메시지 목록 (검색)
gws gmail users messages list --params '{"userId": "me", "q": "from:boss is:unread"}'

# 메시지 상세
gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'

# 메시지 발송 (raw API)
gws gmail users messages send --params '{"userId": "me"}' --json '{"raw": "BASE64_RFC2822"}'

# 라벨 수정 (읽음/보관 처리)
gws gmail users messages modify --params '{"userId": "me", "id": "MSG_ID"}' --json '{"removeLabelIds": ["UNREAD"]}'
gws gmail users messages modify --params '{"userId": "me", "id": "MSG_ID"}' --json '{"removeLabelIds": ["INBOX"]}'

# 메시지 휴지통 이동 (gws 0.6.1+ 에서 411 버그 수정됨)
gws gmail users messages trash --params '{"userId":"me","id":"MSG_ID"}'

# 메시지 영구 삭제
gws gmail users messages delete --params '{"userId": "me", "id": "MSG_ID"}'
```

### users.labels

```bash
# 라벨 목록
gws gmail users labels list --params '{"userId": "me"}' --format table

# 라벨 생성
gws gmail users labels create --params '{"userId": "me"}' --json '{"name": "Project-X"}'
```

### users.drafts

```bash
# 임시저장 목록
gws gmail users drafts list --params '{"userId": "me"}'

# 임시저장 생성
gws gmail users drafts create --params '{"userId": "me"}' --json '{"message": {"raw": "BASE64"}}'
```

### users.threads

```bash
# 스레드 목록
gws gmail users threads list --params '{"userId": "me", "q": "subject:meeting"}'

# 스레드 상세
gws gmail users threads get --params '{"userId": "me", "id": "THREAD_ID"}'
```

### users.settings

```bash
# 필터 생성
gws gmail users settings filters create --params '{"userId": "me"}' --json '{"criteria": {"from": "noreply@service.com"}, "action": {"addLabelIds": ["LABEL_ID"], "removeLabelIds": ["INBOX"]}}'

# 부재중 응답 설정
gws gmail users settings updateVacation --params '{"userId": "me"}' --json '{"enableAutoReply": true, "responseSubject": "Out of Office", "responseBodyPlainText": "..."}'
```

### users.messages.attachments

```bash
# 첨부파일 가져오기
gws gmail users messages attachments get --params '{"userId": "me", "messageId": "MSG_ID", "id": "ATTACHMENT_ID"}'
```

## 검색 쿼리 문법 (q 파라미터)

| 연산자 | 예시 |
|--------|------|
| `from:` | `from:alice@example.com` |
| `to:` | `to:team@company.com` |
| `subject:` | `subject:meeting` |
| `is:` | `is:unread`, `is:starred`, `is:important` |
| `label:` | `label:project-x` |
| `has:` | `has:attachment` |
| `after:` / `before:` | `after:2024/01/01 before:2024/12/31` |
| `newer_than:` / `older_than:` | `newer_than:7d` |
| 조합 | `from:boss is:unread has:attachment` |
