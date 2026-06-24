# nopal Setup Guide for Codex

Use this when `gws` is missing or not authenticated.

## Install

전제 조건: Node.js 18 이상, npm

```bash
npm install -g @googleworkspace/cli
gws --version
```

| 증상 | 해결 방법 |
|------|----------|
| `command not found: gws` | `npm config get prefix` 확인 후 PATH에 추가 |
| permission 에러 | `sudo npm install -g @googleworkspace/cli` 또는 nvm 사용 |
| Node.js 버전 에러 | `node --version` 확인 — 18 미만이면 업그레이드 |

## Auth check

```bash
gws auth status
```

## Interactive setup

`gws auth setup`은 인터랙티브 TUI다. Codex에서 자동 실행할 수 없으므로 사용자에게 터미널에서 직접 실행하도록 안내한다.

```bash
gws auth setup
```

5단계:
1. gcloud CLI 자동 감지 (미설치: https://cloud.google.com/sdk/docs/install)
2. Google 계정 선택
3. GCP 프로젝트 생성 — 추천: `nopal-ws-XXXXXX` (소문자/숫자/하이픈, 6~30자, 전 세계 유일)
4. API 9개 선택: Drive, Sheets, Gmail, Calendar, Docs, Slides, Tasks, Chat, Meet
5. OAuth 인증 정보:
   - A. https://console.cloud.google.com/apis/credentials/consent → External → 앱 이름/이메일 입력
   - B. Test users 탭 → 본인 Gmail 추가 (필수 — 없으면 403 액세스 차단)
   - C. https://console.cloud.google.com/apis/credentials → OAuth 클라이언트 ID → 데스크톱 앱 → Client ID/Secret 터미널에 붙여넣기

## Login

```bash
gws auth login
```

URL이 표시되면 직접 브라우저에 복사해서 열기. "Google hasn't verified this app" 경고 → 고급 → 앱으로 이동(안전하지 않음).

로그인 후 반드시 실행 (headless Codex 환경용):

```bash
gws auth export --unmasked 2>/dev/null | grep -v '^Using keyring' > ~/.config/gws/credentials.json
chmod 600 ~/.config/gws/credentials.json   # 평문 토큰 — 본인만 읽도록 제한하고 절대 커밋 금지
```

자격증명은 `gws` CLI가 OAuth 흐름을 소유한다. headless 사용을 위해 토큰을 로컬 `~/.config/gws/credentials.json`(평문)으로 내보낼 뿐, nopal 자체에는 자격증명을 담지 않는다.

## Troubleshooting

| 증상 | 원인 | 해결 방법 |
|------|------|----------|
| `Token expired` | OAuth 토큰 만료 | `gws auth login` 재실행 후 export 재실행 |
| `Invalid credentials` | 토큰 파일 손상 | `gws auth logout` 후 재로그인 |
| `액세스 차단됨` / 403 | Test user 미등록 | GCP 콘솔 → Test users → 본인 이메일 추가 |
| `invalid_scope` 400 | 스코프 과다 (25개 초과) | 불필요한 API 비활성화 또는 새 프로젝트 생성 |
| `No credentials provided` 401 | Keyring 접근 불가 | `gws auth export --unmasked 2>/dev/null \| grep -v '^Using keyring' > ~/.config/gws/credentials.json` |
| 브라우저 안 열림 | URL 자동 오픈 미지원 | 터미널 URL을 직접 브라우저에 붙여넣기 |

초기화 (최후의 수단):

```bash
gws auth logout
gws auth setup
```

## Important rule

Do not pretend the interactive setup can be completed automatically from a non-interactive Codex turn. Always tell the user to run `gws auth setup` and `gws auth login` in their own terminal.

After setup is done, the user reruns nopal — it will detect auth automatically.
