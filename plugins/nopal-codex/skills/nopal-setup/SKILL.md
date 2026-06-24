---
name: nopal-setup
description: Codex용 Google Workspace 설정 가이드 스킬. `gws` 설치와 OAuth 인증이 필요할 때 사용됩니다. triggers — "gws 설치", "인증 안내", "OAuth 설정", "install gws", "setup", "gws authentication"
---

# nopal-setup for Codex

Read these first:
- `$PLUGIN_ROOT/skills/nopal-setup/references/setup-guide.md`

Use this skill only when `gws` is missing or authentication is not complete.

## Codex Workflow

1. Explain the missing requirement briefly.
2. Show the exact setup step the user must perform.
3. If the step is interactive (TUI), do not pretend Codex can complete it automatically — tell the user to run it in their terminal.
4. Tell the user what to rerun after setup is finished.

---

## gws CLI란?

gws(Google Workspace CLI)는 Google Workspace 9개 서비스를 터미널에서 조작할 수 있는 공식 CLI 도구다.
Nopal은 이 gws CLI를 통해 Google Workspace와 상호작용한다.

- gws CLI가 OAuth 토큰을 자체 관리한다.
- Nopal 플러그인은 토큰을 직접 다루지 않는다.
- API 키나 서비스 계정이 아닌 OAuth(사용자 인증) 방식이다.

---

## 1. 설치

전제 조건: Node.js 18 이상, npm

```bash
npm install -g @googleworkspace/cli
gws --version
```

버전 번호가 출력되면 설치 성공.

| 증상 | 해결 방법 |
|------|----------|
| `command not found: gws` | `npm config get prefix` 확인 후 PATH에 추가 |
| permission 에러 | `sudo npm install -g @googleworkspace/cli` 또는 nvm 사용 |
| Node.js 버전 에러 | `node --version` 확인 — 18 미만이면 업그레이드 |

---

## 2. 초기 설정 (`gws auth setup`)

`gws auth setup`은 인터랙티브 TUI다. Codex에서 자동 실행할 수 없으므로 사용자에게 터미널에서 직접 실행하도록 안내한다.

```bash
gws auth setup
```

### 5단계 가이드

**Step 1/5: gcloud CLI 확인**
자동 감지된다. 미설치 시: https://cloud.google.com/sdk/docs/install

**Step 2/5: Google 계정 선택**
사용할 Google 계정을 선택한다.

**Step 3/5: GCP 프로젝트 생성**
"Create new project"를 선택한다 (추천).
- 프로젝트 ID: 소문자 영문 시작, 소문자/숫자/하이픈, 6~30자, 전 세계 유일
- 추천 형식: `nopal-ws-XXXXXX` (예: `nopal-ws-830621`)

**Step 4/5: Workspace API 선택**
Nopal에 필요한 9개를 모두 선택:
- Google Drive, Google Sheets, Gmail, Google Calendar
- Google Docs, Google Slides, Google Tasks, Google Chat, Google Meet
- 나머지(People, Vault, Forms, Keep 등)는 선택하지 않는다.

**Step 5/5: OAuth 인증 정보 (가장 중요)**

A. OAuth 동의 화면 설정:
   - https://console.cloud.google.com/apis/credentials/consent 이동
   - User Type: "External" → 만들기
   - 앱 이름 입력 (예: nopal), 지원 이메일 선택, 나머지 빈칸 → 저장

B. 테스트 사용자 추가 (**필수! 안 하면 "액세스 차단됨" 403 에러**):
   - 동의 화면 설정 → "Test users" 탭 → "+ Add users"
   - 본인 Gmail 주소 입력 → 저장
   - 직접: https://console.cloud.google.com/apis/credentials/consent/edit

C. OAuth 클라이언트 ID 생성:
   - https://console.cloud.google.com/apis/credentials 이동
   - "+ 사용자 인증 정보 만들기" → "OAuth 클라이언트 ID"
   - 애플리케이션 유형: "데스크톱 앱" → 만들기
   - 생성된 Client ID와 Client Secret을 터미널에 붙여넣기

---

## 3. 로그인 (`gws auth login`)

setup 완료 후:

```bash
gws auth login
```

- URL이 표시되면 직접 브라우저에 복사해서 열기 (자동으로 안 열린다).
- "Google hasn't verified this app" 경고 → **고급** → **앱으로 이동(안전하지 않음)** 클릭.
- Google 계정으로 로그인하고 권한을 승인하면 "Authentication successful" 표시.

**로그인 후 반드시 실행** (headless 환경에서 Codex가 gws를 사용하기 위해):

```bash
gws auth export --unmasked 2>/dev/null | grep -v '^Using keyring' > ~/.config/gws/credentials.json
chmod 600 ~/.config/gws/credentials.json   # 평문 토큰 — 본인만 읽도록 제한하고 절대 커밋 금지
```

자격증명은 `gws` CLI가 소유한다. headless 사용을 위해 토큰을 로컬 `~/.config/gws/credentials.json`(평문)으로 내보낼 뿐이며, nopal 자체에는 자격증명을 담지 않는다.

### 인증 확인

```bash
gws auth status
```

정상이면 인증된 Google 계정 이메일과 활성화된 API 목록이 표시된다.

---

## 4. 인증 문제 해결

| 증상 | 원인 | 해결 방법 |
|------|------|----------|
| `Token expired` | OAuth 토큰 만료 | `gws auth login` 재실행 후 export 명령 재실행 |
| `Invalid credentials` | 토큰 파일 손상 | `gws auth logout` 후 재로그인 |
| `액세스 차단됨` / `Access blocked` (403) | Test user 미등록 | GCP 콘솔 → Test users → 본인 이메일 추가 |
| `invalid_scope` (400) | 스코프 과다 (25개 초과) | 불필요한 API 비활성화 또는 새 프로젝트 생성 |
| `No credentials provided` (401) | Keyring 접근 불가 | `gws auth export --unmasked 2>/dev/null \| grep -v '^Using keyring' > ~/.config/gws/credentials.json` |
| 브라우저가 안 열림 | URL 자동 오픈 미지원 | 터미널에 표시된 URL을 직접 브라우저에 붙여넣기 |
| 조직 계정 제한 | Google Workspace 관리자 정책 | 관리자에게 gws CLI 앱 허용 요청 |
| 프로젝트 ID 중복 | 이미 사용 중인 ID | 뒤에 랜덤 숫자를 변경하여 재시도 |

인증 초기화 (최후의 수단):

```bash
gws auth logout
gws auth setup
```

---

## 5. 설치 완료 후

설치와 인증이 모두 완료되면 nopal을 다시 실행한다.

확인 체크리스트:
- `gws --version` → 버전 번호 출력
- `gws auth status` → 인증된 이메일 + API 목록 표시
- nopal 재실행 → 오케스트레이션 시작
