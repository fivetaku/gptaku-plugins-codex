# 워크플로우 단계 타입 상세 가이드

## 개요

스킬러들의 수다는 6가지 워크플로우 단계 타입을 조합하여 스킬을 설계한다.
각 단계는 목적에 맞는 타입을 선택하고, 순서대로 실행된다.

## 1. 프롬프트 단계 (prompt)

Codex가 추론으로 처리하는 단계. AI의 언어 이해 능력이 핵심.

### 언제 사용하는가
- 텍스트 분석, 요약, 판단, 변환
- 매번 다른 입력에 대해 유연한 처리가 필요할 때
- 창의적 생성이 필요할 때
- 맥락을 이해하고 판단해야 할 때

### SKILL.md 작성 형식
```
### Step N: {단계 이름}
**타입**: prompt

{구체적인 지시사항을 명령형으로 작성한다.}

- 입력: {무엇을 받는지}
- 출력: {무엇을 생성하는지}
- 주의: {지키면 좋은 것}
```

### 예시
```yaml
- order: 3
  name: "번역 실행"
  type: prompt
  description: "용어집을 참조하여 기술 문서를 번역한다"
  input: "원본 텍스트 + 용어집"
  output: "번역된 텍스트"
  validation: "전문 용어가 용어집과 일치하는지 확인"
```

### 프롬프트 단계 설계 팁
- 구체적인 지시: "번역해라" 보다 "기술 문서의 정확성을 유지하면서 자연스럽게 번역해라"
- 제약 조건 명시: "원문의 마크다운 구조를 유지해라"
- 출력 형식 지정: "결과를 마크다운 테이블로 정리해라"

## 2. 스크립트 단계 (script)

반복성, 일관성, API 호출이 필요한 작업. Python 또는 Bash.

### 언제 사용하는가
- **반복성**: 같은 작업을 매번 동일하게 실행해야 할 때
- **일관성**: 결과가 항상 같은 형식이어야 할 때
- **API 호출**: 외부 서비스와 통신이 필요할 때
- **데이터 처리**: JSON 파싱, CSV 변환 등 구조화된 작업
- **파일 변환**: 포맷 변경, 인코딩 처리 등

### 언제 사용하지 않는가
- Codex가 판단/추론으로 충분한 경우 → prompt
- 한 번만 실행하고 끝나는 경우 → prompt
- 복잡한 자연어 처리가 필요한 경우 → prompt

### SKILL.md 작성 형식
```
### Step N: {단계 이름}
**타입**: script
**스크립트**: `scripts/{filename}.py`

{이 스크립트가 하는 일을 설명한다.}

Bash로 실행한다:
\`\`\`bash
python3 $PLUGIN_ROOT/skills/{skill-name}/scripts/{filename}.py [args] 2>/dev/null || python $PLUGIN_ROOT/skills/{skill-name}/scripts/{filename}.py [args]
\`\`\`

- 입력: {인자 설명}
- 출력: {JSON stdout 형식}
- 실패 시: {fallback 동작}
```

### 예시
```yaml
- order: 1
  name: "API로 용어 사전 가져오기"
  type: script
  description: "회사 용어 API에서 최신 용어집을 가져온다"
  script_path: "scripts/fetch_glossary.py"
  input: "API 엔드포인트"
  output: "references/glossary.md 업데이트"
  fallback: "기존 glossary.md 사용"
```

## 3. API·MCP 단계 (api_mcp)

외부 도구를 연동하는 단계.

### 연동 우선순위
1. **API가 있으면** → API 직접 호출 (스크립트로 구현)
2. **API 없고 MCP가 있으면** → MCP 서버 연동
3. **둘 다 없으면** → Codex가 직접 구현

### 언제 사용하는가
- 외부 서비스(Slack, Notion, GitHub 등)와 상호작용
- 실시간 데이터 조회 (DB, 날씨, 주가 등)
- 파일 저장소 접근 (Google Drive, Dropbox 등)
- 메시지 전송 (Slack, Email 등)

### SKILL.md 작성 형식 (API)
```
### Step N: {단계 이름}
**타입**: api_mcp (API)
**스크립트**: `scripts/{api_script}.py`

{API 연동 설명}

- API: {엔드포인트}
- 인증: {API 키 환경변수}
- 실패 시: {fallback}
```

### SKILL.md 작성 형식 (MCP)
```
### Step N: {단계 이름}
**타입**: api_mcp (MCP)
**MCP 서버**: {server-name}

{MCP 도구를 사용하여 수행할 작업}

- 도구: {MCP tool name}
- 실패 시: {fallback}
```

### 예시
```yaml
- order: 5
  name: "Slack에 번역 결과 공유"
  type: api_mcp
  description: "번역된 문서를 Slack 채널에 전송한다"
  mcp_server: "slack-mcp"
  input: "번역된 텍스트 + 채널 ID"
  output: "Slack 메시지 전송 완료"
  fallback: "파일로 저장하고 경로 안내"
```

### 중요 규칙
- API/MCP 단계 뒤에는 **반드시** 검토(review) 또는 생성(generate) 단계가 따라야 한다
- 외부 데이터를 그대로 최종 출력으로 사용하면 안 된다

## 4. RAG 단계 (rag)

references/에서 도메인 지식을 검색하는 단계.

### 언제 사용하는가
- 도메인 지식 참조 (용어집, 정책, 매뉴얼)
- 과거 데이터 검색
- 컨텍스트 윈도우에 항상 넣기엔 큰 데이터
- 스타일 가이드, 템플릿 참조

### SKILL.md 작성 형식
```
### Step N: {단계 이름}
**타입**: rag
**참조**: `references/{filename}.md`

{참조 파일에서 무엇을 검색하고 어떻게 활용하는지}

Read 도구로 `$PLUGIN_ROOT/skills/{skill-name}/references/{filename}.md`를 읽는다.
```

### 예시
```yaml
- order: 2
  name: "용어집 참조"
  type: rag
  description: "도메인 용어집에서 해당 분야 용어를 검색한다"
  reference_path: "references/glossary.md"
  input: "원본 텍스트에서 추출한 전문 용어 목록"
  output: "용어 매핑 테이블"
```

### 중요 규칙
- RAG 단계 뒤에는 **반드시** 검토 또는 프롬프트 단계가 따라야 한다
- 참조 데이터를 그대로 쓰지 말고 맥락에 맞게 가공

## 5. 검토 단계 (review)

AI 또는 사용자가 결과를 확인하는 품질 게이트.

### 언제 사용하는가
- 외부 데이터(API/MCP/RAG)를 받은 직후 → **반드시 검토**
- 중요한 의사결정 전
- 품질 게이트 (정확도 기준 충족 여부)
- 사용자 확인이 필요한 시점

### SKILL.md 작성 형식
```
### Step N: {단계 이름}
**타입**: review

{검토 기준과 통과/실패 조건}

통과 조건:
- {조건 1}
- {조건 2}

실패 시:
- {재처리 동작}
```

### 예시
```yaml
- order: 4
  name: "번역 품질 검토"
  type: review
  description: "번역 결과의 정확성과 자연스러움을 검토한다"
  input: "원본 + 번역본"
  output: "검토 결과 (통과/수정필요)"
  validation: "전문 용어 일치율 95% 이상"
```

### 검토 유형
- **자동 검토**: Codex가 기준에 따라 판단
- **사용자 검토**: §A 질문 도구(없으면 번호형 선택지 블록 폴백)로 사용자에게 확인. 생성된 스킬에도 이 규칙을 그대로 쓴다

## 6. 생성 단계 (generate)

최종 결과물을 출력하는 단계. 워크플로우의 마지막.

### 언제 사용하는가
- 최종 결과물 출력 (파일 저장, 메시지 전송)
- 워크플로우의 마지막 단계
- Write 도구로 파일 생성
- 사용자에게 결과 전달

### SKILL.md 작성 형식
```
### Step N: {단계 이름}
**타입**: generate

{최종 출력물 설명}

Write 도구로 {경로}에 저장한다.
결과를 사용자에게 요약하여 보여준다.
```

### 예시
```yaml
- order: 6
  name: "번역 파일 저장"
  type: generate
  description: "번역된 문서를 파일로 저장한다"
  tool: "Write"
  input: "검토 완료된 번역본"
  output: "translated/{원본파일명}_en.md"
```

## 단계 조합 패턴

### 기본 패턴: 프롬프트 중심
```
prompt → review → generate
```

### 데이터 참조 패턴
```
rag → prompt → review → generate
```

### 외부 연동 패턴
```
script(API) → review → prompt → generate
```

### 복합 패턴
```
script(API) → rag → prompt → review → generate
```

### MCP 연동 패턴
```
prompt → review → generate → api_mcp(전송)
```

## 단계 수 가이드

| 복잡도 | 단계 수 | 예시 |
|--------|---------|------|
| 단순 | 2-3개 | 텍스트 요약 (prompt → generate) |
| 보통 | 3-5개 | 번역 (rag → prompt → review → generate) |
| 복잡 | 5-7개 | 데이터 분석 (script → rag → prompt → review → generate → api_mcp) |

7개 초과는 지양. 너무 복잡하면 여러 스킬로 분리.
