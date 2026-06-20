# 스크립트 템플릿 가이드 (Codex)

워크플로우에서 script 타입 단계가 필요할 때 참고하는 템플릿.

**언어 기본값: Python.** Bash는 Windows에서 `set -euo pipefail`, process substitution, Unix 유틸이 동작하지 않는다. 크로스플랫폼 보장을 위해 Python을 우선하고, Bash는 macOS/Linux 전용이 확실할 때만 쓴다. 경로는 `$PLUGIN_ROOT` 기준.

## Python 기본 템플릿
```python
#!/usr/bin/env python3
"""{스크립트 설명} — Usage: python3 {script}.py [args]"""
import sys, json

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Usage: {script}.py <arg>"}), file=sys.stderr)
        sys.exit(1)
    try:
        result = process(sys.argv[1])
        print(json.dumps({"status": "success", "data": result}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}), file=sys.stderr)
        sys.exit(1)

def process(input_data):
    return {"processed": input_data}

if __name__ == "__main__":
    main()
```

## API 호출 템플릿
```python
#!/usr/bin/env python3
"""{API} 호출 — Usage: python3 {script}.py <endpoint> [api_key]"""
import sys, json, urllib.request, urllib.error

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "endpoint required"}), file=sys.stderr)
        sys.exit(1)
    endpoint = sys.argv[1]
    api_key = sys.argv[2] if len(sys.argv) > 2 else None
    try:
        print(json.dumps({"status": "success", "data": call_api(endpoint, api_key)}, ensure_ascii=False))
    except urllib.error.HTTPError as e:
        print(json.dumps({"status": "error", "code": e.code, "message": f"HTTP {e.code}: {e.reason}"}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}), file=sys.stderr)
        sys.exit(1)

def call_api(endpoint, api_key=None):
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(endpoint, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

if __name__ == "__main__":
    main()
```

## 파일 처리 템플릿
```python
#!/usr/bin/env python3
"""파일 변환/처리 — Usage: python3 {script}.py <input> <output>"""
import sys, json, os

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"status": "error", "message": "Usage: {script}.py <input> <output>"}), file=sys.stderr)
        sys.exit(1)
    input_file, output_file = sys.argv[1], sys.argv[2]
    if not os.path.exists(input_file):
        print(json.dumps({"status": "error", "message": f"File not found: {input_file}"}), file=sys.stderr)
        sys.exit(1)
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        result = process(content)
        os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        print(json.dumps({"status": "success", "output": output_file, "size": len(result)}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}), file=sys.stderr)
        sys.exit(1)

def process(content):
    return content

if __name__ == "__main__":
    main()
```

## Bash 기본 템플릿 (macOS/Linux 전용일 때만)
```bash
#!/usr/bin/env bash
# {스크립트 설명} — Usage: bash {script}.sh [args]
set -euo pipefail
if [ $# -lt 1 ]; then echo "Usage: bash $0 <arg>" >&2; exit 1; fi
ARG="$1"
echo "완료: ${ARG} 처리됨"
```

## 스크립트 공통 규칙

**필수:** shebang 포함, 에러 시 exit 1 + stderr 메시지, 성공 시 stdout JSON, 외부 의존성 최소화(표준 라이브러리 우선), `$PLUGIN_ROOT` 경로 사용.
**권장:** Python `json.dumps(result, ensure_ascii=False)`로 한글 지원, Bash `set -euo pipefail`, 인자 없으면 usage 출력, UTF-8 명시.
**금지:** 런타임 `pip install`, 하드코딩 절대 경로, 네트워크 없이 동작 불가한 필수 로직(fallback 필요), 표준 라이브러리 외 import(불가피하면 SKILL.md에 의존성 명시).

## 크로스 플랫폼
- `which` 대신 `command -v` (POSIX).
- `~` 대신 `$HOME`.
- `python3` 실패 시 폴백: `python3 script.py 2>/dev/null || python script.py`.
- Node.js 스크립트는 `path.join()`으로 OS별 구분자 처리.
