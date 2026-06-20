# 공유 메모리 초기화 가이드 (Codex)

> **공유 메모리 파일 생성 전 이 파일을 끝까지 읽고 절차대로 실행한다.**
> 기억 외부화 원칙: 클로드/Codex의 기억력을 믿지 마. 중요한 결정은 반드시 파일에 기록. 대화가 길어지면 까먹는다 — 파일을 읽으면 복구된다.

---

## 세션 격리 모델

각 세션은 독립된 디렉토리를 사용한다.
`KKIRIKKIRI_DIR = .kkirikkiri/teams/{team_name}/`

이 모델에서는 **세션 간 파일 충돌이 구조적으로 불가능**하다. 각 세션은 자신의 디렉토리에만 쓰고, 이전 세션 디렉토리는 그대로 남는다.

> `scripts/init_shared_memory.py`는 기본적으로 `.kkirikkiri/` 루트에 4종 파일을 만든다. 세션 격리가 필요하면 `--root` 아래 `teams/{team_name}/` 경로를 직접 만들고 그 안에 초기화하거나, 스킬이 직접 Write로 생성한다.

### 세션 내 재계획 (within-session archive)
같은 세션 안에서 방식 B(전체 재구성)가 발생할 때 이전 라운드 결과 보존:
```bash
cp .kkirikkiri/teams/{team_name}/TEAM_PLAN.md .kkirikkiri/teams/{team_name}/archive/reconfigure-$(date +%s).md
```
- 보존 대상: TEAM_FINDINGS.md (DEAD_ENDS 포함) — 재구성 시 새 팀에 전달
- TEAM_PLAN.md, TEAM_PROGRESS.md는 재구성 시 새로 작성 (구버전은 archive/에 선택 보존)
- FINDINGS가 10KB 초과 시 아카이빙 대신 요약본 생성 고려 (토큰 절약)

---

## 생성 대상 파일

```
.kkirikkiri/teams/{team_name}/TEAM_PLAN.md
.kkirikkiri/teams/{team_name}/TEAM_PROGRESS.md
.kkirikkiri/teams/{team_name}/TEAM_FINDINGS.md
.kkirikkiri/teams/{team_name}/TEAM_REPORT.md   (최종 통합 리포트 — 작업 완료 시)
```

---

## 파일 템플릿

### TEAM_PLAN.md (팀장이 관리)
```markdown
# 팀 작업 계획

- 팀명: [team_name]
- 목표: [인터뷰에서 파악한 목표]
- 생성 시각: [timestamp]

## 팀 구성
| 이름 | archetype | 역할 | 티어 | 담당 업무 |
|------|-----------|------|------|----------|
| [leader] | Leader | 팀장 | Opus | 계획/배분/검증/통합 |
| [member-1] | [archetype] | [역할] | [티어] | [업무] |

## 태스크 목록
- [ ] 태스크 1: [설명] → [담당자]
- [ ] 태스크 2: [설명] → [담당자]

## 주요 결정사항
(팀장이 결정할 때마다 여기에 기록 — 게이트 결과도 캐시)
```

### TEAM_PROGRESS.md (모든 팀원이 기록)
```markdown
# 진행 상황

## [timestamp] — [팀원명]
- 상태: 진행 중 / 완료 / 차단됨
- 작업: [수행한 작업]
- 결과: [핵심 발견/산출물]
- 다음: [다음 할 일]
```

### TEAM_FINDINGS.md (모든 팀원이 기록)
```markdown
# 발견 사항 & 공유 자료

## [timestamp] — [팀원명]: [제목]
[발견한 내용, URL, 코드 스니펫 등]

---

# DEAD_ENDS (시도했으나 실패한 접근)

## [timestamp] — [팀원명]: [시도한 접근]
- 시도: [무엇을 했는지]
- 결과: [왜 실패/부적합했는지]
- 근거: [파일경로, 에러 메시지, 테스트 결과 등]
```

> **DEAD_ENDS가 중요한 이유**: 팀 재구성 시 새 팀이 같은 막다른 골목을 다시 탐색하는 것을 방지한다.
> 긍정적 발견만 기록하면 공유 메모리 효과가 60-70%에 그치지만, 실패한 접근까지 기록하면 75-80%까지 컨텍스트를 복구한다.

---

## 공유 메모리 규칙

| 규칙 | 설명 |
|------|------|
| **팀장은 TEAM_PLAN.md를 유지** | 결정이 나올 때마다 즉시 기록 |
| **모든 팀원은 PROGRESS에 기록** | 작업 시작/완료/차단 시 반드시 업데이트 |
| **팀원은 FINDINGS에 공유** | 다른 팀원에게 유용한 발견은 파일로 공유 |
| **실패한 접근은 DEAD_ENDS에 기록** | "시도 → 실패 이유 → 근거"를 남겨 다음 라운드/새 팀이 같은 실수 방지 |
| **기억이 의심되면 파일을 읽어** | 컨텍스트가 길어졌다 싶으면 공유 파일 재확인 |
| **팀장은 통합 전 3개 파일 전부 읽어** | 최종 결과물 만들기 전 전체 맥락 복구 |
| **새/교체 팀원은 합류 시 3개 파일 + DEAD_ENDS 먼저 읽어** | 이전 컨텍스트 복구 후 작업 시작 |

### 교체 팀원 온보딩 순서
DEAD_ENDS(하지 말 것) → TEAM_PLAN(할 것) → PROGRESS(현재 상황) → FINDINGS(참고)
