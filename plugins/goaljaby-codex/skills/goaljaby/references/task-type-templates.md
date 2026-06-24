# 작업 유형 × 파일 강조 매핑 (Step 5)

작업 유형 6종 각각에 대해 VALIDATION/RECOVERY 슬롯 추가 항목 + 사용할 /goal 템플릿을 정의한다.

**언어 정책 (shared/language-policy.md)**: 아래 추가 항목은 한국어로 표기돼 있으나 생성 시 `output_lang`으로 렌더링한다. 식별자(`feature flag`, `viewport`, `design token`, `scope`, `refactor`, `public API`, `DB 스키마`, `eval` 등)는 번역하지 않는다.

기본 템플릿은 `templates.md` 참조. 이 파일은 **유형별 추가/오버라이드**만 명시한다.

> **PLANS.md 매핑**: 아래 유형별 추가 항목은 개별 파일(VALIDATION/RECOVERY)에 들어간 뒤, PLANS.md의 `## Validation` / `## Decision-Log` 섹션에도 요약 반영된다 — Codex /goal이 PLANS.md 한 파일만 읽어도 유형별 강조를 잡도록.

## 1. 기능 구현 (Feature)

| 슬롯 | 값 |
|------|-----|
| `{REQUIRED_CHECK_COMMANDS}` | 단위 테스트 명령 + 통합 테스트 명령 (Step 3 multiSelect 결과) |
| `{TASK_TYPE_NOT_DONE_IF_ADDITIONS}` | `- 기능 토글이 켜졌으나 내부 플래그가 연결되지 않음` |
| `{TASK_TYPE_SCOPE_ADDITIONS}` | `- 문서·롤백 경로 없는 feature flag 추가 금지` |
| `{VISUAL_VERIFICATION_BLOCK_OR_OMIT}` | (생략) |
| /goal 템플릿 | **F-2** |

## 2. 버그 수정 (Bugfix)

| 슬롯 | 값 |
|------|-----|
| `{REQUIRED_CHECK_COMMANDS}` | 원본 재현 절차 + 회귀 테스트 명령 |
| `{TASK_TYPE_NOT_DONE_IF_ADDITIONS}` | `- 버그 재현이 여전히 실패`<br>`- 재현 scope 밖 모듈을 수정함` |
| `{TASK_TYPE_SCOPE_ADDITIONS}` | `- 수정 중 무관한 모듈 refactor 금지` |
| `{VISUAL_VERIFICATION_BLOCK_OR_OMIT}` | (생략) |
| /goal 템플릿 | **F-1** |

## 3. UI 구현 (UI)

| 슬롯 | 값 |
|------|-----|
| `{REQUIRED_CHECK_COMMANDS}` | 빌드 명령 (예: `npm run build`) + 스크린샷 캡처 명령 |
| `{TASK_TYPE_NOT_DONE_IF_ADDITIONS}` | `- 텍스트 겹침·잘림 발생`<br>`- 모바일 viewport 미확인` |
| `{TASK_TYPE_SCOPE_ADDITIONS}` | `- PLAN 승인 없이 design token·전역 스타일 변경 금지` |
| `{VISUAL_VERIFICATION_BLOCK_OR_OMIT}` | `templates.md`의 시각 검증 블록 포함 |
| /goal 템플릿 | **F-3** |

## 4. 문서 집필 (Doc)

| 슬롯 | 값 |
|------|-----|
| `{REQUIRED_CHECK_COMMANDS}` | 자동 검증 명령 없음. markdown lint가 있으면 포함. 그 외엔 섹션별 자가 검토 |
| `{TARGETED_CHECK_COMMANDS}` | 섹션별 자가 검토 체크리스트 |
| `{TASK_TYPE_NOT_DONE_IF_ADDITIONS}` | `- 인용해야 할 참고 자료가 섹션에서 누락됨`<br>`- 문서 중간에 톤이 바뀜` |
| `{TASK_TYPE_SCOPE_ADDITIONS}` | `- 승인된 섹션은 톤·구조 변경 금지` |
| `{VISUAL_VERIFICATION_BLOCK_OR_OMIT}` | (생략) |
| /goal 템플릿 | **F-4** |

## 5. 마이그레이션 (Migration)

| 슬롯 | 값 |
|------|-----|
| `{REQUIRED_CHECK_COMMANDS}` | 패리티 체크 명령 + 롤백 가능성 확인 명령 |
| `{TASK_TYPE_NOT_DONE_IF_ADDITIONS}` | `- 패리티 체크 실패`<br>`- 롤백 리허설 증거 없음` |
| `{TASK_TYPE_SCOPE_ADDITIONS}` | `- PLAN/SDD 명시 없이 public API surface·DB 스키마 변경 금지` |
| `{SDD_INCLUDE}` | `, SDD.md` (PRD 디렉토리에 SDD가 있으면 추가) |
| `{VISUAL_VERIFICATION_BLOCK_OR_OMIT}` | (생략) |
| /goal 템플릿 | **F-5** |

## 6. eval 개선 (Eval)

| 슬롯 | 값 |
|------|-----|
| `{REQUIRED_CHECK_COMMANDS}` | eval suite 실행 명령 + 베이스라인 비교 명령 |
| `{TASK_TYPE_NOT_DONE_IF_ADDITIONS}` | `- 베이스라인 대비 점수 회귀`<br>`- eval 데이터셋 자체를 변경함` |
| `{TASK_TYPE_SCOPE_ADDITIONS}` | `- 한 번에 하나 이상의 프롬프트 변경 금지`<br>`- eval 데이터셋 수정 금지` |
| `{VISUAL_VERIFICATION_BLOCK_OR_OMIT}` | (생략) |
| /goal 템플릿 | **F-6** |

## 적용 순서

1. Step 1에서 작업 유형 추정 (`task-type-classifier.md`)
2. Step 3에서 사용자가 §A 번호 블록으로 최종 확정
3. Step 5에서 위 표의 해당 행을 가져와 `templates.md`의 슬롯 치환 (6종 파일 + PLANS.md)
4. 빈 슬롯이 남으면 해당 줄 자체 제거 (placeholder 잔존 금지)
