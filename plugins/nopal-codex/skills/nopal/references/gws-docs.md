# Docs (v1)

```bash
gws docs <resource> <method> [flags]
```

## 헬퍼 명령어

### +write -- 문서에 텍스트 추가

```bash
gws docs +write --document <ID> --text <TEXT>
```

| 플래그 | 필수 | 설명 |
|--------|------|------|
| `--document` | O | 문서 ID |
| `--text` | O | 추가할 텍스트 (plain text) |

```bash
gws docs +write --document DOC_ID --text 'Hello, world!'
```

- 텍스트는 문서 본문 끝에 삽입
- 서식(리치 포맷)이 필요하면 직접 batchUpdate API 사용
- **write 명령** -- 실행 전 사용자 확인 필수

## API 리소스

### documents

```bash
# 문서 생성
gws docs documents create --json '{"title": "Meeting Notes"}'

# 문서 조회 (전체 구조 포함)
gws docs documents get --params '{"documentId": "DOC_ID"}'

# 문서 일괄 업데이트
gws docs documents batchUpdate --params '{"documentId": "DOC_ID"}' --json '{
  "requests": [
    {
      "insertText": {
        "location": {"index": 1},
        "text": "Hello, World!\n"
      }
    }
  ]
}'
```

## batchUpdate 요청 타입

### 텍스트 삽입

```json
{
  "insertText": {
    "location": {"index": 1},
    "text": "새로운 텍스트\n"
  }
}
```

### 텍스트 삭제

```json
{
  "deleteContentRange": {
    "range": {
      "startIndex": 1,
      "endIndex": 10
    }
  }
}
```

### 텍스트 스타일 적용

```json
{
  "updateTextStyle": {
    "range": {"startIndex": 1, "endIndex": 10},
    "textStyle": {"bold": true, "fontSize": {"magnitude": 14, "unit": "PT"}},
    "fields": "bold,fontSize"
  }
}
```

### 단락 스타일 적용

```json
{
  "updateParagraphStyle": {
    "range": {"startIndex": 1, "endIndex": 10},
    "paragraphStyle": {"namedStyleType": "HEADING_1"},
    "fields": "namedStyleType"
  }
}
```

### 표 삽입

```json
{
  "insertTable": {
    "rows": 3,
    "columns": 3,
    "location": {"index": 1}
  }
}
```

## 문서 구조

- 문서 본문은 `body.content` 배열로 구성
- 각 요소는 `paragraph`, `table`, `sectionBreak` 등
- index는 1부터 시작 (0은 문서 시작 마커)
- batchUpdate 시 여러 요청을 배열로 전달하면 순서대로 실행

## namedStyleType 값

| 값 | 설명 |
|----|------|
| `NORMAL_TEXT` | 일반 텍스트 |
| `TITLE` | 제목 |
| `SUBTITLE` | 부제목 |
| `HEADING_1` ~ `HEADING_6` | 제목 수준 1~6 |
