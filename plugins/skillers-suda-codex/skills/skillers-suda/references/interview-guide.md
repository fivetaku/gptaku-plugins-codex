# Interview Guide

Use chat-first questions. Ask only when the answer changes the generated artifact.

## Minimal Question Set

Ask for missing information in this order:

- target artifact — skill, plugin, eval set, or improvement patch
- trigger behavior — when Codex should use it
- execution surface — prose-only, scripts, MCP/app tools, or package metadata
- safety boundary — what the skill must not do
- output location — source tree, package tree, or existing path

## Prompt Shape

```text
어떤 형태로 만들까요?
1. 단일 스킬 — 빠르고 설치가 단순함
2. 플러그인 패키지 — 여러 스킬/자산/메타데이터를 묶기 좋음
3. 기존 스킬 개선 — 현재 파일을 먼저 읽고 최소 수정
```

## Workshop Preview

Before writing files, show a compact brief:

```text
초안
- 이름: docs-helper
- 형태: 단일 Codex skill
- 트리거: 공식 문서 조회, 버전 민감 질문
- 파일: SKILL.md, references/sites.md
- 검증: quick_validate, 링크 확인
```

Proceed without another question when the user already gave enough detail.
