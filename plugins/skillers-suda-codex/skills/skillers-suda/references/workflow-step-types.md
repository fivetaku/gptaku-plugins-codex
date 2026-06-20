# 워크플로우 단계 타입 (Codex)

스킬은 6가지 단계 타입을 조합해 설계한다. 각 단계는 목적에 맞는 타입을 고르고 순서대로 실행한다. 경로는 `$PLUGIN_ROOT` 기준으로 작성한다.

## 1. prompt — 추론 단계

Codex가 추론으로 처리한다. 텍스트 분석·요약·판단·변환·창작.

작성 형식:
```
### Step N: {단계 이름}
**타입**: prompt
{명령형 지시. 입력/출력/주의 명시}
```
팁: 구체적 지시("기술 문서의 정확성을 유지하면서 자연스럽게 번역해라"), 제약 명시("원문 마크다운 구조 유지"), 출력 형식 지정.

## 2. script — 스크립트 단계

반복성·일관성·API 호출·구조화 데이터 처리. **Python 우선**(크로스플랫폼).

언제 쓰지 않나: 추론으로 충분(→prompt), 한 번만 실행(→prompt), 복잡한 자연어(→prompt).

작성 형식:
```
### Step N: {단계 이름}
**타입**: script
**스크립트**: `scripts/{filename}.py`
{스크립트가 하는 일}

python3 $PLUGIN_ROOT/skills/{skill-name}/scripts/{filename}.py [args]

- 입력: {인자}  - 출력: {JSON stdout}  - 실패 시: {fallback}
```

## 3. api_mcp — 외부 연동 단계

연동 우선순위: **API 있으면 → API 직접 호출(스크립트)** > **MCP/App 있으면 → 도구 연동** > **둘 다 없으면 → Codex 직접 구현**.

언제: 외부 서비스 상호작용, 실시간 데이터 조회, 파일 저장소 접근, 메시지 전송.

작성 형식(API):
```
### Step N: {단계 이름}
**타입**: api_mcp (API)
**스크립트**: `scripts/call_{service}.py`
- API: {엔드포인트}  - 인증: {KEY 환경변수}  - 실패 시: {fallback}
```
작성 형식(MCP/App):
```
### Step N: {단계 이름}
**타입**: api_mcp (MCP)
**서버/앱**: {name}
- 도구: {tool name}  - 실패 시: {fallback}
```

**중요:** api_mcp 단계 뒤에는 **반드시** review 또는 generate가 따른다. 외부 데이터를 그대로 최종 출력으로 쓰지 않는다.

## 4. rag — 참조 검색 단계

`references/`에서 도메인 지식을 검색한다(용어집·정책·매뉴얼·스타일 가이드·템플릿).

작성 형식:
```
### Step N: {단계 이름}
**타입**: rag
**참조**: `references/{filename}.md`
$PLUGIN_ROOT/skills/{skill-name}/references/{filename}.md 를 읽는다.
```

**중요:** rag 단계 뒤에는 **반드시** review 또는 prompt가 따른다. 참조 데이터를 그대로 쓰지 말고 맥락에 맞게 가공한다.

## 5. review — 검토 게이트

AI 또는 사용자가 결과를 확인하는 품질 게이트.

언제: 외부 데이터(api_mcp/rag) 직후 **반드시**, 중요 의사결정 전, 품질 기준 충족 확인, 사용자 확인 시점.

작성 형식:
```
### Step N: {단계 이름}
**타입**: review
통과 조건: {조건들}
실패 시: {재처리 동작}
```
검토 유형: 자동 검토(Codex가 기준 판단) / 사용자 검토(§A 번호 블록으로 확인).

## 6. generate — 생성 단계

최종 결과물 출력. 워크플로우의 마지막.

작성 형식:
```
### Step N: {단계 이름}
**타입**: generate
{경로}에 저장한다. 결과를 사용자에게 요약해 보여준다.
```

## 단계 조합 패턴

```
기본:        prompt → review → generate
데이터 참조: rag → prompt → review → generate
외부 연동:   script(API) → review → prompt → generate
복합:        script(API) → rag → prompt → review → generate
전송:        prompt → review → generate → api_mcp(전송)
```

## 단계 수 가이드

| 복잡도 | 단계 수 | 예시 |
|--------|---------|------|
| 단순 | 2-3개 | 텍스트 요약 (prompt → generate) |
| 보통 | 3-5개 | 번역 (rag → prompt → review → generate) |
| 복잡 | 5-7개 | 데이터 분석 (script → rag → prompt → review → generate) |

7개 초과는 지양. 너무 복잡하면 여러 스킬로 분리한다.
