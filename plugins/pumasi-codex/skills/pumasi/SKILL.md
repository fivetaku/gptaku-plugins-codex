---
name: pumasi
description: Codex-native parallel build orchestration. Use when the user explicitly wants to delegate a greenfield or large multi-module implementation into parallel Codex worker sessions, while the host agent stays in the PM/architect role. Best for 3 or more independent modules with clear gates and interfaces. Korean triggers — "품앗이로 만들어줘", "품앗이 켜줘", "병렬로 외주". English triggers — "pumasi", "parallel codex workers", "delegate to codex".
---

# 품앗이 (Pumasi) — Codex 병렬 외주 개발

> 품앗이: 서로 협력하며 일을 나눠 하는 한국 전통 방식
> Host agent = 설계/감독(PM) | Codex worker × N = 병렬 구현자
>
> 이 스킬을 실행하는 **호스트 에이전트는 Codex** 자신이다. 병렬 워커는 Codex 멀티에이전트
> (v0.139에서 안정화) 또는 `Codex non-interactive run` 세션으로 스폰한다. Codex 전용 도구를 가정하지 않는다.

## 먼저 읽을 것

instruction(작업 브리프) 작성 전 반드시 Read:
- `$PLUGIN_ROOT/skills/pumasi/references/anti-patterns.md` — 복붙형 instruction 절대 금지 규칙 + Red Flags 자가체크표
- `$PLUGIN_ROOT/skills/pumasi/references/role-separation.md` — 호스트 vs Codex 워커 역할 경계
- `$PLUGIN_ROOT/skills/pumasi/references/codex-guide.md` — Codex 특성, DO/DON'T, 라이브러리 대체 방지
- `$PLUGIN_ROOT/skills/pumasi/references/instruction-templates.md` — 템플릿, 좋은/나쁜 예시, 자기 점검 체크리스트
- `$PLUGIN_ROOT/skills/pumasi/references/tech-stack.md` — 2025-2026 모던 스택 추천표

필요할 때 Read:
- `$PLUGIN_ROOT/skills/pumasi/references/examples.md` — 실행 예시 (Todo 앱, 인증 시스템)

## 개념

```
┌─────────────────────────────────────────────────────────┐
│              Host agent (Codex, 설계/감독/PM)            │
│  1. 요구사항 분석 → 기획 → 독립 서브태스크 분해           │
│  2. 시그니처 + 요구사항 + 게이트 작성                     │
│  3. .pumasi/tasks 브리프 작성 → Codex 워커 병렬 스폰      │
│  4. 게이트 검증 → 통합                                   │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
  ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ Codex #1 │     │ Codex #2 │     │ Codex #3 │
  │ 시그니처  │     │ 시그니처  │     │ 시그니처  │
  │ 기반 구현 │     │ 기반 구현 │     │ 기반 구현 │
  └──────────┘     └──────────┘     └──────────┘
        │                 │                 │
        └─────────────────┴─────────────────┘
                          │
                          ▼
              게이트 검증 → 통합 → 완성
```

## 핵심 가치

**품앗이의 존재 이유는 "호스트 에이전트가 코드를 직접 짜지 않는 것"이다.**

| 가치 | 설명 |
|------|------|
| 호스트 토큰 절약 | 호스트는 설계만, 구현은 Codex 워커가 담당 |
| 속도 향상 | N개 모듈을 워커가 병렬로 동시 구현 |
| 검증 최적화 | 동적 게이트(bash, 토큰 0)로 자동 검증 |

**전제 조건**: 워커가 **실제 구현**을 해야 한다. 호스트가 코드를 다 짜고 워커에게 파일 저장만 시키면 토큰 절약 효과 = 0.

---

## 안티패턴 및 역할 분리

**핵심 원칙 요약**: 호스트는 시그니처+요구사항만 작성. 코드 본문(body)은 절대 작성 금지. 강한 게이트(tsc/build/test)로 검증. 상세 규칙은 위 `anti-patterns.md` / `role-separation.md` 참조.

---

## 트리거 조건

```
명시적 트리거:
- "품앗이로 [작업]해줘"
- "품앗이 켜줘"
- "codex 워커로 [작업]"
- "병렬로 [작업] 외주"

자동 감지 (대규모 코딩 요청 시):
- 4개 이상의 독립 파일/모듈 동시 작성 요청
- "전체 [기능] 구현해줘" + 규모가 큰 경우
- 여러 컴포넌트/서비스를 한 번에 만들어야 할 때
```

### 작업 규모별 분기 (중요)

| 규모 | 권장 방식 | 이유 |
|------|----------|------|
| 태스크 1~2개 | **호스트 직접 코딩** | 품앗이 오버헤드가 더 큼 |
| 태스크 3~4개 | **품앗이 사용 가능** | 병렬 이득이 오버헤드와 비슷 |
| 태스크 5개+ | **품앗이 강력 권장** | 병렬 이득이 확실히 큼 |

**또한 다음 경우에는 품앗이를 사용하지 않는다:**
- 기존 코드 수정/버그 수정 (컨텍스트 주입이 과도해짐)
- 단일 파일 작업 (병렬 이점 없음)
- 게이트를 만들 수 없는 작업 (UI 미세 조정 등)

### 품앗이 모드 진입 시 호스트의 행동 변화

```
일반 모드:              품앗이 모드:
호스트가 직접 코딩      호스트가 시그니처+요구사항 작성
                       → .pumasi/tasks 브리프 → Codex 워커 스폰
                       → 게이트 자동 검증 → 통합
```

---

## 사용자 질문 규칙 (§A)

Codex CLI에는 Codex CLI의 `question prompt` 카드 UI가 **없다.** 결정이 꼭 필요할 때는
`shared/questioning-policy.md §A`의 **채팅 번호형 선택지 블록**으로 대체한다.

- 품앗이 요청은 대개 **이미 구체적**이다(만들 것이 명확). §1 + §2c에 따라 추론 가능한 건 묻지 말고,
  요청이 충분히 구체적이거나 사용자가 직접 지시했으면 **즉시 진행**한다(과잉 질문 = 마찰 실패).
- 진짜로 결정이 필요한 경우(예: 스택 선택지가 갈릴 때)만 아래 형식으로 한 번 묻는다:
  ```text
  질문: 어떤 백엔드 스택으로 갈까요?
  1. Next.js Route Handlers — 한 레포에 통합, 배포 단순. 트레이드오프: 무거운 백엔드엔 부담
  2. 별도 Fastify API — 역할 분리 명확. 트레이드오프: 레포/배포 2개
  3. 문장으로 직접 알려주기
  ```
- 추천안은 항상 **1번**. "모르면 1번으로 진행하겠습니다"로 안내한다. 카드 UI를 흉내내지 말 것.

---

## 7단계 워크플로우

### Phase 0: 기획 (Host as PM)

사용자 요청을 분석하여 **완성도 있는 기획안**을 작성. 기획 체크리스트 통과 후 사용자 승인을 받는다.

**기획 체크리스트** (태스크 분해 전 반드시 확인):

```
□ 이 앱/기능의 핵심 사용 시나리오는?
□ 경쟁 제품/일반적 기대치 대비 빠진 기능은?
□ 데이터 모델에 필요한 필드가 충분한가?
□ UX 관점: 검색, 정렬, 필터, 벌크 작업이 필요한가?
□ 비기능 요구사항: 반응형, 다크모드, 접근성은?
□ 태스크 수가 4개 이상인가? (아니면 호스트 직접 코딩)
```

**데이터 모델 설계 원칙**: 타입/인터페이스는 호스트가 설계. 구현 로직은 워커가 작성.

### Phase 1: 분석 (Host)

요청을 받으면 **독립적으로 병렬 실행 가능한** 서브태스크로 분해.

**좋은 서브태스크 조건**:
- 다른 서브태스크 완료를 기다리지 않아도 됨
- 명확한 입출력(시그니처) 정의 가능
- 워커 혼자 구현 가능한 범위
- 파일/기능 경계가 명확함

### Phase 2: 공유 상태 초기화 (Host)

```bash
python3 $PLUGIN_ROOT/skills/pumasi/scripts/init_workspace.py --root "$PWD" --task "<작업 요약>"
```

생성물:
- `.pumasi/job.json` — 잡 상태(태스크/라운드)
- `.pumasi/plan.md` — 통합 컨텍스트 (워커 실행 중 계속 갱신)
- `.pumasi/tasks/<task>.md` — 태스크별 작업 브리프

**작업 브리프(`.pumasi/tasks/<task>.md`)에 반드시 담을 것:**
1. 시그니처와 요구사항만 작성 (코드 본문 작성 금지)
2. owned files / 디렉토리 (다른 워커와 겹치지 않게)
3. 필수 import / 라이브러리 + 금지 대체
4. 강한 게이트 명령 (tsc/build/test 중심)
5. "다른 워커가 같은 레포를 동시에 편집 중"이라는 알림

### Phase 3: 워커 스폰 (Host → Codex 멀티에이전트 / `Codex non-interactive run`)

태스크당 워커 1개를 병렬로 스폰한다. 각 워커 프롬프트에는 해당 `.pumasi/tasks/<task>.md` 브리프를 그대로 전달한다.

- **Codex 멀티에이전트**(v0.139+ 안정): 태스크별 sub-agent를 동시 실행
- 또는 **`Codex non-interactive run`** 세션을 태스크별로 백그라운드 스폰

> 워커는 브리프의 시그니처/요구사항/게이트만 받고 **구현 본문은 워커가 작성**한다. 호스트가 본문을 써서 넘기면 안 된다.

> ⚠️ **샌드박스/승인 우회 경계 (opt-in).** 비대화형 병렬 워커가 승인 프롬프트 없이 파일을 쓰려면
> `Codex non-interactive run --dangerously-bypass-approvals-and-sandbox`(또는 `--full-auto`)가 필요하다 — 병렬 외주
> 자동화를 위해 필요한 동작이다. 따라서 품앗이는 **신뢰하는 본인 레포에서만** 실행하고, 외부에서
> 받은/검토 안 된 코드베이스나 프롬프트에는 쓰지 않는다. 품앗이 호출 자체가 이 우회에 대한 명시적
> 동의이며, 우회 없이 돌리려면 codex 기본 샌드박스(`--full-auto` 등)로 워커를 스폰한다.

### Phase 4: 모니터링 (Host)

워커가 도는 동안 `.pumasi/plan.md`의 통합 컨텍스트를 최신으로 유지한다. 완료 보고/산출 파일을 `.pumasi/reports/`에서 수집한다.

### Phase 5: 게이트 검증 + 선택적 코드 리뷰 (Host)

**4단계 검증 프로세스:**

```
Step 0: 의존성 확인 (게이트 실행 전 필수)
  └── node_modules가 없으면: cd [프로젝트] && npm install --silent
  └── tsc/build/test 게이트는 의존성 설치 후에만 유효

Step 1: 자동 게이트 실행 (bash, 토큰 0)
  └── tsc --noEmit → npm run build → npm test → grep 확인

Step 2: 결과 판정
  ├── 전부 통과 → 워커 보고서만 읽기 (토큰 소량)
  └── 실패 있음 → 실패한 게이트 관련 코드만 읽기 (토큰 최소화)

Step 3: 서브태스크 간 인터페이스 확인
  └── 타입/import 경로 등 교차 검증
```

### Phase 5.5: 코드 정리 (선택적)

> 게이트가 모두 통과했지만 코드 품질을 한 단계 높이고 싶을 때 사용.

**조건**: Phase 5 게이트 전부 PASS + 태스크 3개 이상일 때 권장.
정리(simplify) 패스 후 게이트를 재실행하고 Phase 6 통합으로 넘어간다.

### Phase 6: 통합 및 수정 (Host 판단 + 워커 재위임)

**수정이 필요한 경우**: 호스트가 직접 고치지 않고 해당 태스크만 워커에게 재위임.

```
호스트가 하는 일: "뭘 고칠지" 결정 (자연어 수정 지시 + 좁힌 컨텍스트)
워커가 하는 일: 실제 수정 실행
```

**수정이 필요 없는 경우**: 서브태스크 간 연결만 확인 후 통합한다.

> **실행 예시 참고**: `$PLUGIN_ROOT/skills/pumasi/references/examples.md`

---

## 라운드 (순서 의존성 처리)

태스크 간 의존성이 있으면 **라운드**로 분리한다. 공유 인터페이스를 두고 병렬 워커가
경쟁(race)하지 않도록, 의존성이 있을 때는 항상 라운드를 쓴다.

```
Round 1: 공유 타입/스키마/유틸리티 (3개 병렬)
Round 2+: Round 1 결과(인터페이스)를 사용하는 태스크 (2개 병렬)
Final:   호스트가 직접 로컬 통합 및 검증
```

---

## 워커 룰 (요약)

- 호스트(lead)가 시그니처·타입·제약·게이트를 작성한다.
- 워커가 구현 본문을 작성한다.
- 작업 브리프에 완성된 함수 본문을 절대 붙여넣지 않는다.
- 모든 워커 프롬프트에 반드시 포함:
  - owned files / 디렉토리
  - 필수 시그니처와 import
  - 필수 라이브러리 + 금지 대체
  - 정확한 게이트 명령
  - 다른 워커가 같은 레포를 편집 중이라는 알림

---

## 사전 조건

```bash
command -v codex   # 설치 확인
# 없으면: npm install -g @openai/codex
```

- Codex CLI 설치 + 로그인 완료
- 워커 스폰: Codex 멀티에이전트(v0.139+) 또는 `Codex non-interactive run`

---

## 파일 구조

```
$PLUGIN_ROOT/skills/pumasi/
├── SKILL.md                    # 이 문서
├── references/
│   ├── anti-patterns.md        # 복붙형 instruction 금지 + Red Flags
│   ├── role-separation.md      # 호스트 vs 워커 역할 경계
│   ├── codex-guide.md          # Codex 특성 + instruction 규칙
│   ├── instruction-templates.md # 템플릿 + 좋은/나쁜 예시
│   ├── tech-stack.md           # 모던 기술스택 추천표
│   └── examples.md             # 실행 예시
└── scripts/
    ├── init_workspace.py       # .pumasi 공유 상태 초기화
    └── codex-output-schema.json # 워커 구조화 보고 스키마
```
