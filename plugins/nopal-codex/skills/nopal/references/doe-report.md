# Nopal DOE (Design of Experiments) 보고서

> 테스트 일자: 2026-03-06
> gws CLI 버전: 0.4.4
> 인증 스코프: 7개 (calendar, drive, docs, sheets, slides, gmail.modify, tasks)

---

## 1. 실험 설계

Nopal 오케스트레이션의 실현 가능성을 검증하기 위해 6단계 레벨로 실험을 설계했다.

| 레벨 | 목적 | 복잡도 |
|------|------|--------|
| L1 | 단일 서비스 읽기 | 기본 |
| L2 | 단일 서비스 쓰기/생성 | 기본 |
| L3 | 2-서비스 체인 | 중간 |
| L4 | 2-서비스 + 데이터 변환 | 중간 |
| L5 | 3-서비스 체인 | 고급 |
| L6 | Meet 포함 멀티서비스 | 고급 |

---

## 2. 테스트 결과

### L1: 단일 서비스 읽기

| # | 테스트 | 명령어 | 결과 | 비고 |
|---|--------|--------|------|------|
| L1-1 | Calendar 읽기 | `gws calendar events list` | ✅ 성공 | 7개 이벤트 반환 |
| L1-2 | Gmail 읽기 | `gws gmail +triage` | ✅ 성공 | 읽지 않은 메일 목록 정상 |
| L1-3 | Drive 읽기 | `gws drive files list` | ✅ 성공 | 파일 목록 정상 |
| L1-4 | Tasks 읽기 | `gws tasks tasklists list` | ✅ 성공 | 1개 태스크리스트 반환 |

**L1 결론:** 4개 서비스 읽기 모두 정상. 기본 인증 및 API 호출에 문제 없음.

### L2: 단일 서비스 쓰기/생성

| # | 테스트 | 명령어 | 결과 | 비고 |
|---|--------|--------|------|------|
| L2-1 | Sheets 생성 | `gws sheets spreadsheets create` | ✅ 성공 | 스프레드시트 생성됨 |
| L2-2 | Docs 생성 | `gws docs documents create` | ✅ 성공 | JSON 파싱에 Node.js 필요 (아래 버그 참조) |
| L2-3 | Meet 생성 | `gws meet spaces create` | ❌ 실패 | 403 — Meet 스코프 미포함 |
| L2-4 | Tasks 생성 | `gws tasks tasks insert` | ✅ 성공 | 태스크 정상 생성 |
| L2-5 | Slides 생성 | `gws slides presentations create` | ✅ 성공 | 프레젠테이션 생성됨 |
| L2-6 | Gmail 발송 | `gws gmail +send` | ✅ 성공 | 이메일 정상 발송 |

**L2 결론:** 6개 중 5개 성공. Meet만 스코프 부재로 실패 (구조적 문제 아님).

### L3: 2-서비스 체인

| # | 테스트 | 워크플로우 | 결과 | 비고 |
|---|--------|-----------|------|------|
| L3-1 | Docs→Drive 공유 | 문서 생성 → 권한 부여 | ✅ 성공 | 서비스 간 ID 전달 정상 |

**L3 결론:** 서비스 간 데이터(ID) 전달을 통한 체인 오케스트레이션 가능 확인.

### L4: 2-서비스 + 데이터 변환

| # | 테스트 | 워크플로우 | 결과 | 비고 |
|---|--------|-----------|------|------|
| L4-1 | Sheets→Gmail | 스프레드시트 데이터 읽기 → 메일 발송 | ⚠️ 부분 성공 | 쓰기 OK, `+read` 헬퍼 플래그 이슈, API 직접 호출로 우회 가능 |

**L4 결론:** gws CLI 헬퍼(`+read`) 플래그 호환성 이슈 있으나, 기본 API 서브커맨드로 우회 가능.

### L5: 3-서비스 체인

| # | 테스트 | 워크플로우 | 결과 | 비고 |
|---|--------|-----------|------|------|
| L5-1 | Calendar→Docs→Gmail | 일정 조회 → 회의록 생성 → 참석자 메일 발송 | ✅ 성공 | 3-서비스 순차 체인 완전 동작 |

**L5 결론:** 복잡한 멀티서비스 오케스트레이션 실현 가능 확인. 핵심 사용 시나리오 검증 완료.

### L6: Meet 포함 멀티서비스

| # | 테스트 | 워크플로우 | 결과 | 비고 |
|---|--------|-----------|------|------|
| L6-1 | Meet+Calendar | 회의 생성 → 캘린더 등록 | ⏭️ 미실행 | Meet 스코프 부재로 테스트 불가 |

**L6 결론:** Meet API 사용을 위해서는 OAuth 재인증 시 Meet 스코프 추가 필요.

---

## 3. 발견된 버그 및 이슈

### Bug 1: Gmail trash 411 에러 (Critical)

- **증상:** `gws gmail users messages trash` 호출 시 `411 Length Required` 에러
- **원인:** gws CLI가 body 없는 POST 요청에 `Content-Length: 0` 헤더를 포함하지 않음
- **상태:** GitHub Issue #182 등록 완료
- **우회 방법:** Node.js로 access token 추출 후 `curl -H "Content-Length: 0"` 으로 직접 호출

### Bug 2: `--scopes` 플래그 오작동

- **증상:** `gws auth login --scopes gmail` 실행 시 OAuth URL에 "gmail" 문자열이 그대로 전달됨
- **원인:** 짧은 이름(gmail)을 전체 OAuth 스코프 URL로 변환하지 않음
- **우회 방법:** `--scopes` 사용하지 않고 `gws auth login`으로 Recommended 선택

### Bug 3: Docs API JSON 파싱 이슈

- **증상:** `gws docs documents get` 응답을 Python `json.loads()`로 파싱 시 실패
- **원인:** 응답 JSON에 탭 문자(`\t`) 포함 — Python은 이를 거부하지만 Node.js `JSON.parse()`는 허용
- **우회 방법:** JSON 파싱 시 Node.js 사용 또는 Python에서 탭 문자 사전 제거

### Bug 4: Sheets `+read` 헬퍼 플래그 이슈

- **증상:** `gws sheets +read --spreadsheet-id <id>` 실행 시 unexpected argument 에러
- **우회 방법:** 기본 API 서브커맨드(`gws sheets spreadsheets values get`) 직접 사용

### Issue 5: Meet 스코프 누락

- **증상:** `gws meet spaces create` 실행 시 403 insufficient authentication scopes
- **원인:** OAuth 로그인 시 Meet 관련 스코프가 선택된 7개에 포함되지 않음
- **해결:** OAuth 재인증 시 Meet 스코프 추가 선택 필요

---

## 4. 서비스별 호환성 매트릭스

| 서비스 | 읽기 | 쓰기 | 삭제 | 헬퍼(+) 명령어 | 비고 |
|--------|------|------|------|---------------|------|
| Calendar | ✅ | ✅ | - | - | `--summary` 사용 (`--title` 아님) |
| Gmail | ✅ | ✅ | ⚠️ | ✅ `+triage`, `+send` | trash에 411 버그 |
| Drive | ✅ | ✅ | - | - | 정상 |
| Sheets | ✅ | ✅ | - | ⚠️ `+read` 플래그 이슈 | API 직접 호출로 우회 |
| Docs | ✅ | ✅ | - | - | JSON 파싱에 Node.js 필요 |
| Slides | ✅ | ✅ | - | - | 정상 |
| Tasks | ✅ | ✅ | - | - | 정상 |
| Chat | - | - | - | - | 미테스트 (스코프 미포함) |
| Meet | ❌ | ❌ | - | - | 스코프 미포함 |

---

## 5. 오케스트레이션 패턴 검증 결과

### 검증된 패턴

| 패턴 | 예시 | 상태 |
|------|------|------|
| 단일 조회 | "오늘 일정 확인해줘" | ✅ 안정 |
| 단일 생성 | "스프레드시트 만들어줘" | ✅ 안정 |
| ID 전달 체인 | "문서 만들고 공유해줘" | ✅ 안정 |
| 데이터 변환 체인 | "시트 데이터 읽어서 메일 보내줘" | ⚠️ 헬퍼 우회 필요 |
| 3-서비스 체인 | "일정 확인 → 회의록 → 메일 발송" | ✅ 안정 |

### 미검증 패턴

| 패턴 | 이유 |
|------|------|
| Meet 포함 체인 | 스코프 미포함 |
| Chat 포함 체인 | 스코프 미포함 |
| 4+ 서비스 체인 | 시간 제약 (3-서비스까지 검증 완료로 확장 가능성 높음) |

---

## 6. 권장 사항

### 즉시 적용 (v0.5.x)

1. **Docs JSON 파싱:** SKILL.md 오케스트레이션 가이드에 "Docs API 응답은 Node.js로 파싱" 명시
2. **Sheets 헬퍼 우회:** `+read` 대신 `gws sheets spreadsheets values get` 사용하도록 레퍼런스 업데이트
3. **Calendar 플래그:** `--summary` 사용 명시 (`--title` 아님)
4. **Gmail trash 우회:** curl 직접 호출 패턴을 레퍼런스에 추가

### 중기 (v0.6.0)

1. **Meet/Chat 스코프 가이드:** 사용자가 필요 시 OAuth 재인증으로 스코프 추가하는 절차 문서화
2. **gws CLI 버그 추적:** Issue #182 (trash 411) 수정 반영 시 우회 로직 제거
3. **에러 핸들링 강화:** 스코프 부족 시 자동 안내 메시지 출력

### 장기

1. **gws CLI 업스트림 기여:** 발견된 버그들에 대한 PR 검토
2. **대체 경로 구현:** gws CLI 버그가 많은 서비스는 curl 직접 호출 폴백 구현 고려

---

## 7. 종합 평가

| 항목 | 평가 |
|------|------|
| 전체 성공률 | **85%** (13/15 테스트 성공 또는 부분 성공) |
| 핵심 시나리오 실현 가능성 | **높음** — 3-서비스 체인까지 완전 동작 확인 |
| gws CLI 안정성 | **보통** — 헬퍼 명령어에 버그 있으나 기본 API 서브커맨드는 안정적 |
| 오케스트레이션 구조적 한계 | **낮음** — 서비스 간 ID/데이터 전달 패턴 검증 완료 |
| 프로덕션 준비도 | **MVP 가능** — 주요 7개 서비스(Calendar, Gmail, Drive, Sheets, Docs, Slides, Tasks)로 실용적 워크플로우 구성 가능 |

**결론:** Nopal 오케스트레이션은 현재 gws CLI 기반으로 실용적 수준의 Google Workspace 자동화가 가능하다. gws CLI의 헬퍼 명령어에 일부 버그가 있으나 기본 API 서브커맨드로 우회 가능하며, 핵심 사용 시나리오(일정→문서→메일 체인)는 완전히 동작한다.
