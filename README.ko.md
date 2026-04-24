[English](README.md) | 한국어

# GPTaku Codex Plugins

> **GPTaku 플러그인의 Codex 네이티브 플러그인 마켓플레이스.**

이 저장소는 Codex 마켓플레이스 루트입니다. Codex 플러그인 매니페스트, 패키징된 스킬, 플러그인 README, 검증 스크립트, 마켓플레이스 매니페스트를 포함합니다.

## 빠른 시작

마켓플레이스를 추가합니다:

```bash
codex plugin marketplace add OWNER/gptaku-plugins-codex
```

`fivetaku` 계정으로 배포한다면:

```bash
codex plugin marketplace add fivetaku/gptaku-plugins-codex
```

재현 가능한 설치가 필요하면 릴리스나 브랜치를 고정합니다:

```bash
codex plugin marketplace add OWNER/gptaku-plugins-codex@v0.1.0
```

마켓플레이스를 추가한 뒤:
- Codex를 재시작해서 마켓플레이스를 다시 로드합니다.
- Codex 플러그인 UI에서 `GPTaku Codex` 마켓플레이스를 열고 필요한 플러그인을 설치합니다.
- 설치한 스킬을 테스트하려면 새 Codex 세션을 시작합니다.

설치한 플러그인은 채팅에서 자연어로 요청해서 사용합니다. 예시:
- `pumasi-codex` — "품앗이로 이 앱 병렬 작업으로 만들어줘."
- `show-me-the-prd-codex` — "이 제품 아이디어를 PRD로 정리해줘."
- `insane-search-codex` — "이 막힌 페이지 가져와서 요약해줘."
- `kkirikkiri-codex` — "이거 에이전트 팀 꾸려서 조사해줘."
- `docs-guide-codex` — "공식 문서 기준으로 설명해줘."
- `deep-research-codex` — "출처 달아서 딥리서치해줘."
- `nopal-codex` — "Google Workspace 작업 도와줘."
- `git-teacher-codex` — "이 Git 흐름 단계별로 가르쳐줘."
- `skillers-suda-codex` — "Codex 스킬 설계 도와줘."
- `vibe-sunsang-codex` — "최근 Codex 세션 리뷰하고 코칭해줘."

현재 Codex CLI에서 확인되는 마켓플레이스 관리 명령:
- `codex plugin marketplace add <source>` — GitHub, Git URL, SSH URL, 로컬 marketplace root를 추가합니다.
- `codex plugin marketplace upgrade [gptaku-codex]` — 마켓플레이스 클론을 업데이트합니다.
- `codex plugin marketplace remove gptaku-codex` — 이 마켓플레이스를 제거합니다.

## 로컬 체크아웃에서 설치

GitHub에 올리기 전에 로컬에서 테스트할 때:

```bash
codex plugin marketplace add /absolute/path/to/gptaku-plugins-codex
```

현재 staging 체크아웃에서는 아래 명령으로 검증했습니다:

```bash
codex plugin marketplace add /Users/chulrolee/gptaku_plugins/gptaku-plugins-codex
```

예상 결과:

```text
Added marketplace `gptaku-codex` from /Users/chulrolee/gptaku_plugins/gptaku-plugins-codex.
Installed marketplace root: /Users/chulrolee/gptaku_plugins/gptaku-plugins-codex
```

## 게시 체크리스트

- `bash scripts/run_package_smoke_tests.sh` 를 실행합니다.
- `.agents/plugins/marketplace.json` 에 `"name": "gptaku-codex"` 가 들어있는지 확인합니다.
- 모든 패키지에 `.codex-plugin/plugin.json`, `README.md`, `skills/<skill-name>/SKILL.md` 가 있는지 확인합니다.
- 이 디렉토리의 내용물을 `gptaku-plugins-codex` GitHub 저장소 루트로 올립니다.
- 릴리스 태그를 만든 뒤 `OWNER/REPO@v0.1.0` 같은 고정 설치 명령을 권장합니다.
- 마켓플레이스 추가나 업데이트 후에는 Codex를 재시작하라고 안내합니다.

## 저장소 구조

```text
gptaku-plugins-codex/
  .agents/plugins/marketplace.json   # Codex 마켓플레이스 매니페스트
  plugins/
    <plugin-name>/
      .codex-plugin/plugin.json      # 플러그인 매니페스트
      README.md
      assets/
      skills/
        <skill-name>/
          SKILL.md
          references/
          scripts/
  scripts/
    validate_packages.py
    run_package_smoke_tests.sh
```

이 저장소에서 하는 일:
- Codex 마켓플레이스 패키징
- 플러그인 매니페스트 관리
- 마켓플레이스 매니페스트 관리
- 패키징된 플러그인 README 관리

소스 포트 작업장, 레거시 런타임 플러그인 트리, 캐시 디렉토리, 로컬 smoke-test 로그는 이 저장소에 올리지 않습니다.

## 현재 패키징된 플러그인

- `pumasi-codex`
- `show-me-the-prd-codex`
- `insane-search-codex`
- `kkirikkiri-codex`
- `insane-design-codex`
- `docs-guide-codex`
- `deep-research-codex`
- `nopal-codex`
- `git-teacher-codex`
- `skillers-suda-codex`
- `vibe-sunsang-codex`

## 패키징 흐름

1. `plugins/<plugin-name>/` 아래의 패키징된 플러그인을 수정합니다.
2. `skills/<skill-name>/` 안에는 런타임에 필요한 파일만 유지합니다.
3. `.codex-plugin/plugin.json` 을 채웁니다.
4. `.agents/plugins/marketplace.json` 에 플러그인 엔트리를 추가하거나 갱신합니다.
5. 아래 검증과 smoke test 명령을 실행합니다.

## 마켓플레이스 매니페스트

- [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json)

## 검증

저장소 루트에서 패키지 감사를 실행합니다:

```bash
python3 scripts/validate_packages.py
```

이 감사는 마켓플레이스 엔트리, 플러그인 매니페스트, 스킬 frontmatter, 참조 파일, 레거시 런타임 흔적, 포트 노트 흔적, 스크립트 문법을 확인합니다.

패키징된 플러그인 내용을 바꿨다면 smoke suite를 실행합니다:

```bash
bash scripts/run_package_smoke_tests.sh
```

smoke suite는 패키지 감사, JSON 매니페스트 파싱, 가능한 패키지 단위 smoke test, 헬퍼 스크립트 smoke test, 레거시 흔적 스캔을 함께 실행합니다.

## 라이선스

MIT
