# gws CLI 공통 패턴

## 인증

```bash
# 브라우저 기반 OAuth (인터랙티브)
gws auth login

# 서비스 계정
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json

# 인증 상태 확인
gws auth status
```

**보안 규칙:**
- 토큰/API 키를 직접 출력하거나 관리하지 않는다 -- `gws auth`가 전담
- write/delete 명령 실행 전 반드시 사용자 확인
- 파괴적 작업에는 `--dry-run` 우선 사용

## CLI 구문

```bash
gws <service> <resource> [sub-resource] <method> [flags]
```

### 스키마 조회

```bash
# 리소스/메서드 탐색
gws <service> --help

# 메서드의 필수 파라미터, 타입, 기본값 조회
gws schema <service>.<resource>.<method>
```

`gws schema` 출력을 보고 `--params`와 `--json` 플래그를 구성한다.

## 글로벌 플래그

| 플래그 | 설명 |
|--------|------|
| `--format <FORMAT>` | 출력 형식: `json`(기본), `table`, `yaml`, `csv` |
| `--dry-run` | API 호출 없이 로컬 검증만 수행 |
| `--sanitize <TEMPLATE>` | Model Armor를 통한 응답 필터링 |

## 메서드 플래그

| 플래그 | 설명 |
|--------|------|
| `--params '{"key": "val"}'` | URL/쿼리 파라미터 |
| `--json '{"key": "val"}'` | 요청 본문 (JSON) |
| `-o, --output <PATH>` | 바이너리 응답을 파일로 저장 |
| `--upload <PATH>` | 파일 업로드 (멀티파트) |
| `--page-all` | 자동 페이지네이션 (NDJSON 출력) |
| `--page-limit <N>` | `--page-all` 시 최대 페이지 수 (기본: 10) |
| `--page-delay <MS>` | 페이지 간 딜레이 ms (기본: 100) |

## 헬퍼 명령어

각 서비스에는 `+` 접두사 헬퍼 명령어가 있다. 간편한 인터페이스를 제공한다.

```bash
gws gmail +send --to alice@example.com --subject 'Hello' --body 'Hi!'
gws calendar +agenda --today
gws drive +upload ./report.pdf
```

복잡한 요구사항(HTML 본문, 반복 일정 등)은 직접 API를 사용한다.

## 에러 처리

- API 에러는 JSON 형식으로 반환된다
- `gws schema`로 필수 파라미터를 먼저 확인
- 인증 만료 시 `gws auth login`으로 재인증

## 페이지네이션

```bash
# 모든 결과를 자동으로 가져오기 (NDJSON)
gws gmail users messages list --params '{"userId": "me", "q": "is:unread"}' --page-all

# 최대 5페이지만
gws drive files list --page-all --page-limit 5
```
