# Component Decision Guide (Codex)

인터뷰 결과로 **스킬 / 플러그인 / 레퍼런스 / 스크립트** 중 적합한 형태를 판단한다. Codex CLI의 command·agent 컴포넌트는 Codex에 없으므로 제안하지 않는다 — 진입은 항상 description 트리거다.

## Artifact Types

- **Skill** — 지시 중심 워크플로우, 결정적 스크립트, 재사용 도메인 지식. **기본값.**
- **Plugin** — 여러 스킬·자산·메타데이터·MCP/App 설정·마켓플레이스 패키징이 하나의 제품으로 묶일 때.
- **Reference** — 큰 표·예시·표준·스키마·긴 설명 — 매번 로드하면 안 되는 것.
- **Script** — 결정적 검증·파싱·파일 생성·API 래퍼·반복 변환.
- **MCP/App** — 워크플로우가 이미 도구로 노출된 라이브 외부 기능을 필요로 할 때만.

## 판단 로직

### 스킬을 선택하는 경우
- 한 가지 목적의 워크플로우
- 대화 맥락 안에서 처리 가능
- 사용자와 대화하며 진행
- 중간 확인이 필요 (§A 번호 블록으로 처리)

예: 번역 스킬, 코드 리뷰 스킬, 문서 생성 스킬.

### 플러그인 패키지를 선택하는 경우
- 여러 스킬을 하나의 제품으로 배포
- 자산(아이콘/템플릿) + 메타데이터(interface) 필요
- MCP/App 설정을 함께 묶음
- 마켓플레이스 등재 대상

구조·매니페스트 규칙: `references/plugin-package-guide.md`.

## Split Rules

- 한 제품으로 배포되는 워크플로우는 하나의 플러그인에 묶는다.
- 트리거 문구와 사용자 의도가 명확히 다를 때만 여러 스킬로 분리한다.
- 문서가 길다는 이유만으로 분리하지 않는다 — 긴 내용은 `references/`로 옮긴다.
- 짧은 지시로 충분한데 스크립트를 만들지 않는다.

## 자율 실행이 필요해 보이는 경우

Codex CLI였다면 agent로 갔을 "자율 다단계 실행"도 Codex에서는 **스킬 안의 워크플로우**로 표현한다. 사용자가 명시적으로 요청하고 환경이 지원할 때만 bounded sub-agent에 위임하되, 그 위임은 스킬 워크플로우의 한 단계로 문서화한다. 별도 `agents/` 폴더나 agent 파일을 만들지 않는다.

## Codex Package Shape

```text
plugin-name/
  .codex-plugin/plugin.json
  README.md
  skills/
    skill-name/
      SKILL.md
      references/
      scripts/
  assets/
```

마이그레이션 작업 시, 임시 소스-포트 노트는 마켓플레이스 레포 밖에 두고 최종 패키지 형태만 발행한다.

## 각 컴포넌트 파일 구조

### Skill
```yaml
---
name: skill-name
description: This skill should be used when...
---
# 워크플로우 (명령형)
```

### Plugin manifest (`.codex-plugin/plugin.json`)
허용 필드만: `id, name, version, description, skills, apps, mcpServers, interface, author, homepage, repository, license, keywords`. `agents` 필드·폴더는 없다. `version`은 strict semver, `skills`는 `./skills/`를 가리킨다.
