# Google Meet (v2)

> `gws meet <resource> <method> [flags]`

## API Resources

### conferenceRecords

- `get` — 회의 기록 조회 (회의 ID로)
- `list` — 회의 기록 목록 조회 (기본: 시작 시간 내림차순)
- `participants` — 참가자 정보 조회
- `recordings` — 녹화 영상 조회
- `transcripts` — 회의 자막/스크립트 조회

### spaces

- `create` — 회의 공간(링크) 생성
- `endActiveConference` — 진행 중인 회의 종료
- `get` — 회의 공간 상세 조회
- `patch` — 회의 공간 설정 수정

## 주요 명령어

```bash
# 회의 공간(링크) 생성
gws meet spaces create --json '{}' --format json

# 회의 공간 조회
gws meet spaces get --params '{"name": "spaces/SPACE_ID"}' --format json

# 회의 기록 목록
gws meet conferenceRecords list --format json

# 특정 회의 참가자 조회
gws meet conferenceRecords.participants list --params '{"parent": "conferenceRecords/RECORD_ID"}' --format json

# 회의 녹화 조회
gws meet conferenceRecords.recordings list --params '{"parent": "conferenceRecords/RECORD_ID"}' --format json

# 회의 스크립트 조회
gws meet conferenceRecords.transcripts list --params '{"parent": "conferenceRecords/RECORD_ID"}' --format json

# 진행 중인 회의 종료
gws meet spaces endActiveConference --params '{"name": "spaces/SPACE_ID"}' --format json
```

## 명령어 탐색

```bash
gws meet --help
gws schema meet.<resource>.<method>
```
