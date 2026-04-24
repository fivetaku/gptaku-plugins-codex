# Slides (v1)

```bash
gws slides <resource> <method> [flags]
```

## API 리소스

### presentations

```bash
# 프레젠테이션 생성
gws slides presentations create --json '{"title": "Quarterly Review Q2"}'

# 프레젠테이션 조회
gws slides presentations get --params '{"presentationId": "PRES_ID"}'

# 일괄 업데이트
gws slides presentations batchUpdate --params '{"presentationId": "PRES_ID"}' --json '{
  "requests": [...]
}'
```

### presentations.pages

```bash
# 특정 페이지(슬라이드) 조회
gws slides presentations pages get --params '{"presentationId": "PRES_ID", "pageObjectId": "PAGE_ID"}'
```

## batchUpdate 요청 타입

### 슬라이드 추가

```json
{
  "createSlide": {
    "objectId": "custom_slide_id",
    "insertionIndex": 1,
    "slideLayoutReference": {
      "predefinedLayout": "TITLE_AND_BODY"
    }
  }
}
```

### 텍스트 삽입

```json
{
  "insertText": {
    "objectId": "TEXT_BOX_ID",
    "insertionIndex": 0,
    "text": "Hello, World!"
  }
}
```

### 텍스트 스타일 적용

```json
{
  "updateTextStyle": {
    "objectId": "TEXT_BOX_ID",
    "style": {
      "bold": true,
      "fontSize": {"magnitude": 24, "unit": "PT"}
    },
    "textRange": {"type": "ALL"},
    "fields": "bold,fontSize"
  }
}
```

### 도형(텍스트 박스) 생성

```json
{
  "createShape": {
    "objectId": "textbox_01",
    "shapeType": "TEXT_BOX",
    "elementProperties": {
      "pageObjectId": "PAGE_ID",
      "size": {
        "width": {"magnitude": 300, "unit": "PT"},
        "height": {"magnitude": 50, "unit": "PT"}
      },
      "transform": {
        "scaleX": 1, "scaleY": 1,
        "translateX": 100, "translateY": 100,
        "unit": "PT"
      }
    }
  }
}
```

### 이미지 삽입

```json
{
  "createImage": {
    "objectId": "image_01",
    "url": "https://example.com/image.png",
    "elementProperties": {
      "pageObjectId": "PAGE_ID",
      "size": {
        "width": {"magnitude": 200, "unit": "PT"},
        "height": {"magnitude": 150, "unit": "PT"}
      }
    }
  }
}
```

### 슬라이드 삭제

```json
{
  "deleteObject": {
    "objectId": "SLIDE_ID"
  }
}
```

### 텍스트 치환 (플레이스홀더)

```json
{
  "replaceAllText": {
    "containsText": {"text": "{{TITLE}}", "matchCase": true},
    "replaceText": "Q2 Quarterly Review"
  }
}
```

## 사전 정의 레이아웃 (predefinedLayout)

| 값 | 설명 |
|----|------|
| `BLANK` | 빈 슬라이드 |
| `CAPTION_ONLY` | 캡션만 |
| `TITLE` | 제목 슬라이드 |
| `TITLE_AND_BODY` | 제목 + 본문 |
| `TITLE_AND_TWO_COLUMNS` | 제목 + 2열 |
| `TITLE_ONLY` | 제목만 |
| `SECTION_HEADER` | 섹션 헤더 |
| `ONE_COLUMN_TEXT` | 단일 열 텍스트 |
| `MAIN_POINT` | 핵심 포인트 |
| `BIG_NUMBER` | 큰 숫자 |

## 공유 (Drive API 사용)

프레젠테이션 공유는 Drive permissions API를 사용한다:

```bash
gws drive permissions create --params '{"fileId": "PRES_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}'
```
