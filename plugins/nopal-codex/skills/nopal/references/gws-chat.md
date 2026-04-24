# Chat (v1)

```bash
gws chat <resource> <method> [flags]
```

## 헬퍼 명령어

### +send -- 메시지 발송

```bash
gws chat +send --space <NAME> --text <TEXT>
```

| 플래그 | 필수 | 설명 |
|--------|------|------|
| `--space` | O | 스페이스 이름 (예: `spaces/AAAAxxxx`) |
| `--text` | O | 메시지 텍스트 (plain text) |

```bash
gws chat +send --space spaces/AAAAxxxx --text 'Hello team!'
```

- `gws chat spaces list`로 스페이스 이름 조회
- 카드, 스레드 답장은 직접 API 사용
- **write 명령** -- 실행 전 사용자 확인 필수

## API 리소스

### spaces

```bash
# 스페이스 목록
gws chat spaces list --format table

# 스페이스 상세
gws chat spaces get --params '{"name": "spaces/SPACE_ID"}'

# 스페이스 생성
gws chat spaces create --json '{"displayName": "Project X", "spaceType": "SPACE"}'

# 스페이스 설정 (멤버 포함 생성)
gws chat spaces setup --json '{
  "space": {"displayName": "New Team", "spaceType": "SPACE"},
  "memberships": [{"member": {"name": "users/user@company.com", "type": "HUMAN"}}]
}'

# 스페이스 수정
gws chat spaces patch --params '{"name": "spaces/SPACE_ID", "updateMask": "displayName"}' --json '{"displayName": "New Name"}'

# 스페이스 삭제
gws chat spaces delete --params '{"name": "spaces/SPACE_ID"}'

# DM 찾기
gws chat spaces findDirectMessage --params '{"name": "users/user@company.com"}'

# 스페이스 검색 (관리자)
gws chat spaces search --params '{"useAdminAccess": true, "query": "customer"}'
```

### spaces.messages

```bash
# 메시지 발송 (직접 API)
gws chat spaces messages create --params '{"parent": "spaces/SPACE_ID"}' --json '{"text": "Hello from API!"}'

# 스레드 답장
gws chat spaces messages create --params '{"parent": "spaces/SPACE_ID"}' --json '{
  "text": "This is a reply",
  "thread": {"name": "spaces/SPACE_ID/threads/THREAD_ID"}
}'

# 메시지 목록
gws chat spaces messages list --params '{"parent": "spaces/SPACE_ID"}' --format table

# 메시지 상세
gws chat spaces messages get --params '{"name": "spaces/SPACE_ID/messages/MSG_ID"}'

# 메시지 수정
gws chat spaces messages patch --params '{"name": "spaces/SPACE_ID/messages/MSG_ID", "updateMask": "text"}' --json '{"text": "Updated message"}'

# 메시지 삭제
gws chat spaces messages delete --params '{"name": "spaces/SPACE_ID/messages/MSG_ID"}'
```

### spaces.members

```bash
# 멤버 목록
gws chat spaces members list --params '{"parent": "spaces/SPACE_ID"}' --format table

# 멤버 추가
gws chat spaces members create --params '{"parent": "spaces/SPACE_ID"}' --json '{"member": {"name": "users/user@company.com", "type": "HUMAN"}}'

# 멤버 삭제
gws chat spaces members delete --params '{"name": "spaces/SPACE_ID/members/MEMBER_ID"}'
```

### media

```bash
# 미디어 다운로드
gws chat media download --params '{"resourceName": "spaces/SPACE_ID/messages/MSG_ID/attachments/ATT_ID"}' -o file.ext

# 미디어 업로드
gws chat media upload --params '{"parent": "spaces/SPACE_ID"}' --upload ./file.pdf
```

## 스페이스 이름 형식

- 스페이스: `spaces/AAAA...` (영숫자 ID)
- 메시지: `spaces/SPACE_ID/messages/MSG_ID`
- 멤버: `spaces/SPACE_ID/members/MEMBER_ID`
- 스레드: `spaces/SPACE_ID/threads/THREAD_ID`
- 사용자: `users/user@company.com` 또는 `users/USER_ID`
