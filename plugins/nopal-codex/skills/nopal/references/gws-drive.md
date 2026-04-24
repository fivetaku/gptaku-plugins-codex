# Drive (v3)

```bash
gws drive <resource> <method> [flags]
```

## 헬퍼 명령어

### +upload -- 파일 업로드

```bash
gws drive +upload <file>
```

| 플래그 | 필수 | 설명 |
|--------|------|------|
| `<file>` | O | 업로드할 파일 경로 |
| `--parent` | - | 부모 폴더 ID |
| `--name` | - | 대상 파일명 (기본: 원본 파일명) |

```bash
gws drive +upload ./report.pdf
gws drive +upload ./report.pdf --parent FOLDER_ID
gws drive +upload ./data.csv --name 'Sales Data.csv'
```

- MIME 타입 자동 감지
- **write 명령** -- 실행 전 사용자 확인 필수

## API 리소스

### files

```bash
# 파일 목록 (검색)
gws drive files list --params '{"q": "name contains '\''Report'\''"}' --format table

# 파일 상세
gws drive files get --params '{"fileId": "FILE_ID"}'

# 파일 생성 (폴더)
gws drive files create --json '{"name": "Q2 Project", "mimeType": "application/vnd.google-apps.folder"}'

# 파일 생성 (하위 폴더)
gws drive files create --json '{"name": "Documents", "mimeType": "application/vnd.google-apps.folder", "parents": ["PARENT_FOLDER_ID"]}'

# 파일 복사
gws drive files copy --params '{"fileId": "TEMPLATE_ID"}' --json '{"name": "New Document"}'

# 파일 메타데이터 수정
gws drive files update --params '{"fileId": "FILE_ID"}' --json '{"name": "New Name"}'

# 파일 이동 (부모 변경)
gws drive files update --params '{"fileId": "FILE_ID", "addParents": "FOLDER_ID", "removeParents": "OLD_PARENT_ID"}'

# 파일 삭제 (영구)
gws drive files delete --params '{"fileId": "FILE_ID"}'

# 파일 다운로드
gws drive files get --params '{"fileId": "FILE_ID", "alt": "media"}' -o filename.ext

# Google Docs/Sheets/Slides를 PDF로 내보내기
gws drive files export --params '{"fileId": "FILE_ID", "mimeType": "application/pdf"}' -o document.pdf

# 휴지통 비우기
gws drive files emptyTrash
```

### permissions (공유/권한)

```bash
# 권한 목록
gws drive permissions list --params '{"fileId": "FILE_ID"}' --format table

# 사용자에게 편집 권한 부여
gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "user@company.com"}'

# 읽기 권한 부여
gws drive permissions create --params '{"fileId": "FILE_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "user@company.com"}'

# 소유권 이전
gws drive permissions create --params '{"fileId": "FILE_ID", "transferOwnership": true}' --json '{"role": "owner", "type": "user", "emailAddress": "newowner@company.com"}'

# 권한 삭제
gws drive permissions delete --params '{"fileId": "FILE_ID", "permissionId": "PERM_ID"}'
```

role 값: `owner`, `organizer`, `fileOrganizer`, `writer`, `commenter`, `reader`
type 값: `user`, `group`, `domain`, `anyone`

### comments

```bash
# 댓글 목록
gws drive comments list --params '{"fileId": "FILE_ID", "fields": "comments(id,content,author)"}'

# 댓글 생성
gws drive comments create --params '{"fileId": "FILE_ID", "fields": "id,content"}' --json '{"content": "Please review this section."}'
```

### drives (공유 드라이브)

```bash
# 공유 드라이브 생성
gws drive drives create --params '{"requestId": "unique-id"}' --json '{"name": "Project X"}'

# 공유 드라이브 목록
gws drive drives list --format table

# 공유 드라이브에 멤버 추가
gws drive permissions create --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}' --json '{"role": "writer", "type": "user", "emailAddress": "member@company.com"}'
```

### revisions

```bash
# 리비전 목록
gws drive revisions list --params '{"fileId": "FILE_ID"}'

# 특정 리비전 가져오기
gws drive revisions get --params '{"fileId": "FILE_ID", "revisionId": "REV_ID"}'
```

### about

```bash
# 사용자/드라이브 정보
gws drive about get --params '{"fields": "user,storageQuota"}'
```

## 검색 쿼리 문법 (q 파라미터)

| 연산자 | 예시 |
|--------|------|
| `name contains` | `"name contains 'Report'"` |
| `name =` | `"name = 'Quarterly Report'"` |
| `mimeType =` | `"mimeType = 'application/vnd.google-apps.folder'"` |
| `in parents` | `"'FOLDER_ID' in parents"` |
| `in owners` | `"'user@company.com' in owners"` |
| `trashed` | `"trashed = false"` |
| `visibility` | `"visibility = 'anyoneWithLink'"` |
| `modifiedTime` | `"modifiedTime > '2024-01-01T00:00:00'"` |

주요 MIME 타입:
- 폴더: `application/vnd.google-apps.folder`
- Google Docs: `application/vnd.google-apps.document`
- Google Sheets: `application/vnd.google-apps.spreadsheet`
- Google Slides: `application/vnd.google-apps.presentation`
