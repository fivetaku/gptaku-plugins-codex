# Sheets (v4)

```bash
gws sheets <resource> <method> [flags]
```

## 헬퍼 명령어

### +read -- 스프레드시트 값 읽기

```bash
gws sheets +read --spreadsheet <ID> --range <RANGE>
```

| 플래그 | 필수 | 설명 |
|--------|------|------|
| `--spreadsheet` | O | 스프레드시트 ID |
| `--range` | O | 읽을 범위 (예: `Sheet1!A1:B2`) |

```bash
gws sheets +read --spreadsheet ID --range 'Sheet1!A1:D10'
gws sheets +read --spreadsheet ID --range Sheet1
```

- 읽기 전용, 스프레드시트 수정 없음
- 고급 옵션은 직접 values.get API 사용

### +append -- 행 추가

```bash
gws sheets +append --spreadsheet <ID>
```

| 플래그 | 설명 |
|--------|------|
| `--spreadsheet` | 스프레드시트 ID (필수) |
| `--values` | 쉼표 구분 값 (단순 문자열) |
| `--json-values` | JSON 배열 (예: `'[["a","b"],["c","d"]]'`) |

```bash
# 단일 행 추가
gws sheets +append --spreadsheet ID --values 'Alice,100,true'

# 다중 행 일괄 추가
gws sheets +append --spreadsheet ID --json-values '[["a","b"],["c","d"]]'
```

- `--values`는 단순 단일 행 추가용
- `--json-values`는 여러 행 일괄 삽입용
- **write 명령** -- 실행 전 사용자 확인 필수

## API 리소스

### spreadsheets

```bash
# 스프레드시트 생성
gws sheets spreadsheets create --json '{"properties": {"title": "My Sheet"}}'

# 스프레드시트 정보 조회
gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'

# 일괄 업데이트 (시트 조작)
gws sheets spreadsheets batchUpdate --params '{"spreadsheetId": "SHEET_ID"}' --json '{
  "requests": [{
    "updateSheetProperties": {
      "properties": {"sheetId": 0, "title": "February 2025"},
      "fields": "title"
    }
  }]
}'
```

### spreadsheets.values

```bash
# 값 읽기
gws sheets spreadsheets values get --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1:D10"}'

# 값 쓰기
gws sheets spreadsheets values update --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1", "valueInputOption": "USER_ENTERED"}' --json '{"values": [["Name", "Score"], ["Alice", 100]]}'

# 값 추가
gws sheets spreadsheets values append --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1", "valueInputOption": "USER_ENTERED"}' --json '{"values": [["Bob", 95]]}'

# 여러 범위 일괄 읽기
gws sheets spreadsheets values batchGet --params '{"spreadsheetId": "SHEET_ID", "ranges": ["Sheet1!A1:B", "Sheet2!A1:B"]}'

# 여러 범위 일괄 쓰기
gws sheets spreadsheets values batchUpdate --params '{"spreadsheetId": "SHEET_ID"}' --json '{
  "valueInputOption": "USER_ENTERED",
  "data": [
    {"range": "Sheet1!A1", "values": [["Header1", "Header2"]]},
    {"range": "Sheet1!A2", "values": [["Data1", "Data2"]]}
  ]
}'
```

### spreadsheets.sheets

```bash
# 시트(탭) 복사
gws sheets spreadsheets sheets copyTo --params '{"spreadsheetId": "SHEET_ID", "sheetId": 0}' --json '{"destinationSpreadsheetId": "SHEET_ID"}'
```

## A1 Notation

| 표기 | 의미 |
|------|------|
| `Sheet1!A1:B2` | Sheet1의 A1~B2 셀 |
| `Sheet1!A:A` | Sheet1의 A열 전체 |
| `Sheet1!1:3` | Sheet1의 1~3행 |
| `Sheet1` | Sheet1 전체 |
| `A1:B2` | 첫 번째 시트의 A1~B2 |

## valueInputOption

| 값 | 설명 |
|----|------|
| `RAW` | 값을 그대로 저장 (수식 해석 안 함) |
| `USER_ENTERED` | 사용자가 입력한 것처럼 처리 (수식, 숫자 자동 변환) |
