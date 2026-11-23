# 컴포넌트 타입 판단 기준 (Codex)

## 개요

인터뷰 결과를 바탕으로 **스킬(Skill) / 서브에이전트(Sub-agent, 스킬에 임베드) / 플러그인 패키지(Plugin)** 중 적합한 형태를 자동 판단한다.

Codex 플러그인에는 슬래시 커맨드 폴더도 에이전트 로스터 폴더도 **없다**. 진입은 항상 SKILL.md의 description 트리거로 이뤄지고, 자율 실행이 필요한 역할은 **소유 스킬 안에 프롬프트로 임베드해 Codex 런타임의 sub-agent로 스폰**한다. 본진의 "커맨드"가 하던 인수 기반 분기는 SKILL.md 안의 "진입점 판단" 표로 흡수한다.

## 비교 테이블

| 기준 | 스킬 (Skill) | 서브에이전트 (Sub-agent) | 플러그인 패키지 (Plugin) |
|------|-------------|-------------------------|--------------------------|
| 트리거 | 자동 감지 (description 매칭) | 소유 스킬이 워크플로우 중 스폰 | 마켓 설치 단위 — 내부 스킬들이 각자 트리거 |
| 컨텍스트 | 기존 대화에 녹아듦 | 독립 컨텍스트 (bounded 작업 후 결과만 반환) | 해당 없음 (묶음 단위) |
| 실행 방식 | 메인 스레드가 직접 실행 | 별도 sub-agent가 자율 실행, 메인이 종합 | 각 스킬이 실행 |
| 복잡도 | 단순~중간 | 중간~복잡 | 여러 스킬·자산·MCP를 한 제품으로 |
| 도구 접근 | 모든 도구 | 프롬프트에서 범위 제한 (읽기 전용 등) | 스킬별 |
| 상태 | 대화 상태 공유 | 자체 상태, 결과만 반환 | 해당 없음 |
| 적합한 작업 | 한 가지 일을 처리 | 병렬 분석·긴 자율 작업·독립 관점 검증 | 스킬 2개 이상 + 공용 references/MCP |

## 자동 판단 로직

### 스킬을 선택하는 경우 (기본값)
```
IF 아래 조건 중 하나라도 해당:
  - 한 가지 목적의 워크플로우
  - 대화 맥락 안에서 처리 가능
  - 사용자와 대화하면서 진행해야 함
  - §A 질문 도구(없으면 번호형 선택지 폴백)로 중간 확인 필요
  - 인수/상황에 따라 분기하지만 진입은 하나 (진입점 판단 표로 처리)
THEN → 스킬
```

예시:
- "번역 스킬" → 대화 내에서 번역 워크플로우 실행
- "코드 리뷰 스킬" → 파일 읽고 분석 후 리포트
- "문서 생성 스킬" → 인터뷰 후 문서 작성
- "/deploy 같은 명시 호출" → description에 트리거 문구를 넣은 스킬 + 진입점 판단 표

### 서브에이전트를 임베드하는 경우
```
IF 아래 조건 중 하나라도 해당:
  - 자율적으로 여러 단계를 실행해야 함
  - 독립적인 컨텍스트가 필요함 (메인 대화를 오염시키지 않아야 함)
  - 오래 걸리는 작업을 메인과 분리
  - 여러 관점을 병렬로 독립 검증 (예: 이 플러그인의 4 전문가)
  - 제한된 도구만 접근해야 안전함
THEN → 소유 스킬 안에 sub-agent 프롬프트를 임베드 (references/agents/{name}.md)
```

예시:
- "보안 감사" → 스킬이 코드베이스 스캔 sub-agent를 스폰하고 결과를 종합
- "리서치" → 축별 sub-agent 병렬 스폰 + 종합
- "QA 테스트" → 테스트 실행 sub-agent + 채점 sub-agent

sub-agent 프롬프트 파일의 품질 기준과 표준 구조는 `references/agent-templates.md`를 따른다. 스폰 규칙(동시 스폰·bounded·결과 형식 명시)은 `references/interview-guide.md` §2를 따른다.

### 플러그인 패키지로 묶는 경우
```
IF 아래 조건 중 하나라도 해당:
  - 스킬이 2개 이상이고 references/scripts를 공유함
  - MCP 서버 설정을 함께 배포해야 함
  - 마켓 노출용 interface 메타데이터(표시 이름·아이콘·기본 프롬프트)가 필요함
THEN → 플러그인 패키지 (.codex-plugin/plugin.json + skills/)
```

## 복합 구성

하나의 플러그인에 여러 스킬과 임베드 sub-agent를 조합할 수 있다:

```
플러그인/
├── .codex-plugin/plugin.json      # 매니페스트 (name, version, skills, interface, mcpServers)
├── skills/
│   ├── main-skill/
│   │   ├── SKILL.md               # 자동 감지 워크플로우 + 진입점 판단 표
│   │   ├── references/agents/     # 스킬이 스폰하는 sub-agent 프롬프트
│   │   └── scripts/
│   └── quick-skill/SKILL.md       # 두 번째 진입 스킬
└── shared/                        # 스킬 간 공용 문서
```

예시: 번역 플러그인
- Skill "translate": "번역해줘" → 자동 감지, 인터뷰 후 번역. "파일 경로 + 언어쌍"이 인수로 주어지면 진입점 판단 표에서 바로 번역 단계로
- Sub-agent: 대규모 번역 → 챕터별 sub-agent 병렬 스폰, 메인이 용어 일관성 검토

## 판단 순서도

```
사용자 요청 분석
    │
    ├── 자율 실행·독립 컨텍스트·병렬 검증이 필요한가?
    │   ├── Yes → 스킬 + 임베드 sub-agent
    │   └── No → 스킬
    │
    └── 스킬 2개 이상 또는 MCP/interface 배포가 필요한가?
        ├── Yes → 플러그인 패키지로 묶음
        └── No → 단일 스킬
```

## 각 컴포넌트의 파일 구조

### Skill 파일 구조
```yaml
---
name: skill-name
description: This skill should be used when...
---
# 워크플로우 내용
```

frontmatter는 `name`과 `description` 두 필드만 쓴다. `allowed-tools` 같은 본진 전용 필드는 Codex에서 무시되거나 검증에 실패한다.

### Sub-agent 프롬프트 파일 구조 (`references/agents/{name}.md`)
```markdown
# {Agent Name}

## 역할
{한 줄 정의 — 이 sub-agent가 무엇을 판단·생산하는지}

## 입력
{소유 스킬이 넘기는 것 — 아이디어, 파일 경로, 비교 대상}

## 절차
1. ...

## 출력 형식
{구조화된 결과 — 메인이 종합할 수 있게 "한줄 요약" 포함}

## 하지 않는 것
{읽기 전용 / 파일 수정 금지 / 사용자에게 직접 질문 금지 등 범위 제한}
```

> 표준 구조·품질 등급(L1/L2/L3)·검증: `references/agent-templates.md`, `scripts/verify_agent.py`.

### Plugin 매니페스트 구조 (`.codex-plugin/plugin.json`)
```json
{
  "name": "plugin-name",
  "version": "0.1.0",
  "description": "한 줄 설명",
  "skills": "./skills/",
  "interface": { "displayName": "...", "shortDescription": "..." }
}
```
