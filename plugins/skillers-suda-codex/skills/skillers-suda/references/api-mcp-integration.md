# API / MCP 연동 가이드 (Codex)

스킬에서 외부 도구와 연동할 때의 판단 기준과 구현 방법.

## 연동 우선순위

```
1순위: API가 있으면 → API 직접 호출 (스크립트로 구현)
2순위: API 없고 MCP/App이 있으면 → 도구 연동
3순위: 둘 다 없으면 → Codex가 직접 구현
```

왜 API 우선? API는 표준화·문서화되어 스크립트로 반복 호출·테스트가 쉽다. MCP/App은 Codex 환경에 의존하고 설치가 필요하다. 직접 구현은 추론 의존이라 일관성 보장이 어렵다.

## API 연동

판단 기준: 공식 API 문서가 있는가? REST/GraphQL인가? 인증이 API 키 또는 OAuth인가?

API 호출은 **반드시 script 타입으로** 구현한다.

```
### Step N: {API 연동 단계}
**타입**: script
**스크립트**: `scripts/call_{service}.py`
{service} API를 호출하여 {목적}을 수행한다.

환경변수: `{SERVICE}_API_KEY`
python3 $PLUGIN_ROOT/skills/{skill}/scripts/call_{service}.py "$INPUT"
```

API 스크립트 패턴(표준 라이브러리만):
```python
#!/usr/bin/env python3
import os, json, urllib.request

API_KEY = os.environ.get("{SERVICE}_API_KEY", "")
BASE_URL = "https://api.{service}.com/v1"

def call(endpoint, data=None):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(f"{BASE_URL}/{endpoint}", data=body, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())
```

인증별 처리:
| 인증 | 환경변수 | 헤더 |
|------|---------|------|
| API Key | `{SERVICE}_API_KEY` | `Authorization: Bearer {key}` |
| Basic | `{SERVICE}_USER`, `{SERVICE}_PASS` | `Authorization: Basic {base64}` |
| OAuth | `{SERVICE}_TOKEN` | `Authorization: Bearer {token}` |

API 키는 환경변수로만 전달. 코드에 하드코딩 금지.

## MCP / App 연동

판단 기준: API가 없거나 복잡한가? MCP 서버/App이 이미 설정돼 있는가?

```
### Step N: {MCP 연동 단계}
**타입**: api_mcp (MCP)
**서버/앱**: {name}
{name}의 {tool-name} 도구로 {목적}을 수행한다.

도구: {tool-name}  파라미터: {param1}, {param2}
실패 시:
- 서버/앱이 없으면 → 사용자에게 설치 안내
- 도구 호출 실패 → {fallback 동작}
```

## 직접 구현 (fallback)

API도 MCP/App도 없을 때, 또는 단순 스크래핑/데이터 처리. Codex의 내장 도구(Read/Write/Bash 등)로 처리하거나 스크립트로 구현한다.

## 핵심 규칙

### API/MCP 결과는 반드시 검토
```
api_mcp 호출 → review → generate
```
외부 데이터를 그대로 최종 출력으로 쓰지 않는다. 검토 단계에서 형식·내용·누락을 확인한다.

### 에러 처리
모든 api_mcp 단계에 fallback 필수: 캐시된 이전 결과 / 기본값 / 사용자 수동 입력 / 단계 스킵(허용 시).

### 환경 의존성 문서화
API 키나 MCP/App이 필요한 스킬은 SKILL.md에 명시한다 — references에만 숨기지 않는다.
```markdown
## 요구사항
- `{SERVICE}_API_KEY` 환경변수 필요
  export {SERVICE}_API_KEY="your-api-key"
- 또는 `{mcp-server}` MCP/App 설정 필요
```
