[English](README.md) | 한국어

# gptaku-plugins-codex

> **AI Native가 되고 싶은 사람들을 위한 Codex 플러그인 마켓플레이스.**

AI Native란 AI를 단순히 도구로 쓰는 게 아닙니다. 기획부터 실행까지 AI를 자연스럽게 녹여내는 것입니다. 연습이 필요하고, 배우는 사람들을 위한 도구가 필요합니다. 이 플러그인들은 Codex로 작업하면서 만나는 구체적인 벽을 하나씩 허물기 위해 만들어졌습니다.

[빠른 시작](#빠른-시작) | [플러그인](#사용-가능한-플러그인) | [왜 만들었나?](#왜-이-플러그인들인가) | [요구사항](#요구사항)

---

## 빠른 시작

### 1. 마켓플레이스 등록

```bash
codex plugin marketplace add https://github.com/fivetaku/gptaku-plugins-codex.git
```

### 2. Codex 재시작

마켓플레이스를 추가한 뒤 Codex를 재시작해서 플러그인 목록을 다시 로드합니다.

### 3. Codex에서 플러그인 설치

Codex 플러그인 UI를 열고 `GPTaku Codex`에서 필요한 플러그인을 설치합니다.

### 4. 자연어로 사용

새 Codex 세션을 시작한 뒤 평소처럼 요청하면 됩니다.

```text
이 아이디어를 PRD로 정리해줘.
품앗이로 이 기능을 병렬 작업으로 나눠서 만들어줘.
이 막힌 페이지 가져와서 요약해줘.
이 Git 흐름 단계별로 가르쳐줘.
```

### 5. 업데이트

```bash
codex plugin marketplace upgrade gptaku-codex
```

---

## 왜 이 플러그인들인가

- **배우는 사람을 위해** - Git을 모르면 `git-teacher-codex`가 단계별로 설명하고, PRD를 못 쓰면 `show-me-the-prd-codex`가 인터뷰로 정리해줍니다.
- **Codex 네이티브** - `.codex-plugin/plugin.json`, Codex 스킬, Codex 서브에이전트 패턴, 채팅 우선 인터랙션 규칙에 맞춰 패키징했습니다.
- **기능보다 결과 중심** - 차단 사이트, 백지 PRD, 병렬 코딩, 딥리서치, 공식문서 탐색, 업무공간 자동화, 성장 코칭 같은 구체적인 벽을 해결합니다.
- **한글 우선, 영문 지원** - 한글로 먼저 쓰기 좋게 만들고, 필요한 곳에는 영문 문서도 함께 둡니다.
- **조합 가능** - 필요한 플러그인만 설치해서 독립적으로 사용할 수 있습니다.

---

## 사용 가능한 플러그인

- **docs-guide-codex** - 공식문서 기반 답변. `llms.txt` 우선 전략과 공식 출처 fallback을 사용합니다.
- **git-teacher-codex** - 비개발자를 위한 Git/GitHub 온보딩. 클라우드 서비스 비유와 안전한 초보자 흐름을 제공합니다.
- **vibe-sunsang-codex** - 바이브코더를 위한 AI 협업 멘토링. 세션 회고, 멘토링, 성장 리포트를 제공합니다.
- **deep-research-codex** - 질문 설계, 소스 교차검증, 인용, 품질 점검을 포함한 구조화 딥리서치.
- **pumasi-codex** - Codex 네이티브 병렬 빌드 오케스트레이션과 이미지 생성 companion 스킬.
- **show-me-the-prd-codex** - 거친 아이디어를 인터뷰 기반 PRD 문서 묶음으로 정리합니다.
- **kkirikkiri-codex** - 자연어 요청에서 Codex 에이전트 팀을 구성하고, 공유 메모리와 제한된 위임으로 진행합니다.
- **skillers-suda-codex** - Codex 스킬이나 플러그인 번들을 설계, 리뷰, 패키징하는 워크숍.
- **nopal-codex** - `gws`를 통해 Gmail, Calendar, Drive, Docs, Sheets, Slides, Chat, Tasks, Meet 작업을 오케스트레이션합니다.
- **insane-search-codex** - 차단되거나 WAF가 강한 페이지를 generic fetch, public API, RSS, Jina, 선택적 Playwright로 우회합니다.
- **insane-design-codex** - 실제 웹사이트 CSS를 디자인 시스템으로 추출하거나, 번들된 디자인 코퍼스를 재사용합니다.

> 플러그인은 계속 추가될 수 있습니다. 릴리스 알림을 받으려면 저장소를 Watch 해두세요.

---

## 요구사항

- **플러그인 마켓플레이스를 지원하는 Codex CLI**
- **macOS / Linux**: 바로 사용 가능
- **Windows**: WSL2 사용 권장
- 일부 플러그인은 `git`, `gh`, `node`, `python3`, `tmux`, `gws` 같은 선택 도구를 사용합니다. 필요한 도구는 각 플러그인 안내에서 알려줍니다.

---

## 마켓플레이스 검증

유지보수용 명령입니다.

```bash
python3 scripts/validate_packages.py
bash scripts/run_package_smoke_tests.sh
```

검증은 마켓플레이스 엔트리, 플러그인 매니페스트, 스킬 frontmatter, 참조 파일, 레거시 런타임 흔적, 포트 노트 흔적, 스크립트 문법, 가능한 smoke test를 확인합니다.

---

## 라이선스

MIT

---

<div align="center">

**벽 하나씩, AI Native가 되어갑니다.**

</div>
