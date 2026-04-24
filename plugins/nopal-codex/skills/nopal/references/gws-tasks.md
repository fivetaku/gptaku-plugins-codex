# Tasks (v1)

```bash
gws tasks <resource> <method> [flags]
```

## API 리소스

### tasklists

```bash
# 태스크 리스트 목록
gws tasks tasklists list --format table

# 태스크 리스트 상세
gws tasks tasklists get --params '{"tasklist": "TASKLIST_ID"}'

# 태스크 리스트 생성
gws tasks tasklists insert --json '{"title": "Q2 Goals"}'

# 태스크 리스트 수정
gws tasks tasklists patch --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Q2 Goals (Updated)"}'

# 태스크 리스트 삭제
gws tasks tasklists delete --params '{"tasklist": "TASKLIST_ID"}'
```

- 사용자당 최대 2,000개 리스트
- 삭제 시 리스트 내 모든 태스크도 함께 삭제

### tasks

```bash
# 태스크 목록
gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format table

# 미완료 태스크만 조회
gws tasks tasks list --params '{"tasklist": "TASKLIST_ID", "showCompleted": false}'

# 태스크 상세
gws tasks tasks get --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}'

# 태스크 생성
gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{
  "title": "Review Q1 metrics",
  "notes": "Pull data from analytics dashboard",
  "due": "2026-04-01T00:00:00Z"
}'

# 태스크 수정 (patch)
gws tasks tasks patch --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}' --json '{
  "status": "completed"
}'

# 태스크 완료 해제
gws tasks tasks patch --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}' --json '{
  "status": "needsAction",
  "completed": null
}'

# 태스크 삭제
gws tasks tasks delete --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}'

# 태스크 이동 (순서/부모 변경)
gws tasks tasks move --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID", "parent": "PARENT_TASK_ID"}'

# 완료된 태스크 숨기기 (clear)
gws tasks tasks clear --params '{"tasklist": "TASKLIST_ID"}'
```

## 태스크 상태

| status 값 | 설명 |
|-----------|------|
| `needsAction` | 미완료 (활성) |
| `completed` | 완료 |

- 완료 시 `completed` 필드에 완료 시간이 자동 설정됨
- 미완료로 되돌릴 때는 `status: "needsAction"`, `completed: null` 설정

## 태스크 필드

| 필드 | 설명 |
|------|------|
| `title` | 태스크 제목 |
| `notes` | 메모/설명 |
| `due` | 마감일 (RFC3339, 예: `2026-04-01T00:00:00Z`) |
| `status` | `needsAction` 또는 `completed` |
| `completed` | 완료 시간 (자동 설정) |
| `parent` | 상위 태스크 ID (서브태스크용) |
| `links` | 관련 링크 배열 |

## 제한사항

- 리스트당 최대 20,000개 미숨김 태스크
- 사용자 전체 최대 100,000개 태스크
- 태스크당 최대 2,000개 서브태스크
- 기본 태스크 리스트는 `@default`로 참조 가능
