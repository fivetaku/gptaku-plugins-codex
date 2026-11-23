---
name: pumasi
description: Host-controlled parallel coding for Codex. The current Codex session stays the host (plans, writes signatures and gates, verifies, integrates) and delegates bounded implementation tasks to N parallel CLI workers — Codex workers by default, or grok / cursor-agent / gjc / agy / claude CLI workers chosen per task. Best for 3 or more independent modules with clear gates and interfaces. Korean triggers — "품앗이로 만들어줘", "품앗이 켜줘", "병렬로 외주", "codex 워커로", "grok으로 외주". English triggers — "pumasi", "parallel codex workers", "delegate to codex", "parallel with grok". Image generation belongs to the separate pumasi-image skill — do not trigger on "이미지/그림/썸네일/로고 만들어줘" even when Codex is named.
---

# 품앗이 (Pumasi) — Codex 병렬 외주 개발

> 품앗이: 서로 협력하며 일을 나눠 하는 한국 전통 방식
> Host = 설계/감독(PM) | 워커 × N = 병렬 구현자
>
> 이 스킬을 실행하는 **호스트는 Codex 자신**이다. 병렬 워커는 Codex 멀티에이전트
> (v0.139에서 안정화) 또는 `codex exec` 세션으로 스폰하고, 필요하면 다른 CLI 워커로 교체한다.
> 다른 에이전트 전용 도구·훅·설정 스크립트를 가정하지 않는다.

## 호스트와 워커 계약

품앗이를 부른 **현재 세션이 항상 호스트**(기획·감독·승인·최종 검증 담당)다. 워커는 브리프 하나를 받아
경계 안에서 구현하고 증거(파일·보고)를 돌려주는 존재다. 워커에게 전체 오케스트레이션을 다시 맡기거나
품앗이를 재귀 실행하지 않는다.

- **호스트 = Codex, 기본 워커 = Codex** (`codex exec`). 사용자가 다른 워커를 지명했거나 Phase 0.5에서
  선택했으면 그 워커의 스폰 명령을 쓴다(아래 "외주 워커 교체"). 명시된 워커를 다른 워커로 몰래 바꾸지 않는다.
- 워커 명령 우선순위: 태스크별 지정 > 잡 기본 지정 > 호스트 기본값(Codex). 태스크별로 섞어 쓸 수 있다.
- `claude` CLI를 워커로 쓸 때의 명령은 `claude --print --permission-mode acceptEdits`다. 프롬프트는 stdin으로
  주고 `--output-format json`으로 구조화 보고를 받는다. 모델·허용 도구·권한은 명시적 명령 옵션으로 조정하며
  호스트 인증을 복사하지 않는다. `acceptEdits`는 무제한 셸 승인이 아니다 — 거부된 권한이 있는지 보고에서 확인한다.
- 잡 상태는 호출 프로젝트의 `.pumasi/`에 둔다. 워커 종료가 곧 성공은 아니다 — **각 워커의 종료 코드·보고서·게이트를
  따로 확인**한다. 실패/부분 완료/잘못된 JSON/누락된 보고는 완료로 승격하지 않고, 원본 stdout·stderr와
  `report.json`을 보존한 뒤 호스트가 재위임 여부를 판단한다.
- 이 문서의 예시에서 **호스트(기획자)** 는 현재 Codex 세션, **Codex(구현자)** 는 선택된 워커 역할로 읽는다.
  Codex 전용 참고(`codex-guide.md`)는 Codex 워커에만 적용한다.

## 먼저 읽을 것

instruction(작업 브리프) 작성 전 반드시 Read:
- `$PLUGIN_ROOT/skills/pumasi/references/anti-patterns.md` — 복붙형 instruction 절대 금지 규칙 + Red Flags 자가체크표
- `$PLUGIN_ROOT/skills/pumasi/references/role-separation.md` — 호스트 vs 워커 역할 경계
- `$PLUGIN_ROOT/skills/pumasi/references/codex-guide.md` — Codex 워커 특성, DO/DON'T, 라이브러리 대체 방지 (Codex 워커일 때만)
- `$PLUGIN_ROOT/skills/pumasi/references/instruction-templates.md` — 템플릿, 좋은/나쁜 예시, 자기 점검 체크리스트
- `$PLUGIN_ROOT/skills/pumasi/references/tech-stack.md` — 2025-2026 모던 스택 추천표

필요할 때 Read:
- `$PLUGIN_ROOT/skills/pumasi/references/examples.md` — 실행 예시 (Todo 앱, 인증 시스템, 브리프 예시)

## 개념

```
┌─────────────────────────────────────────────────────────┐
│              Host (Codex 세션, 설계/감독/PM)             │
│  1. 요구사항 분석 → 기획 → 독립 서브태스크 분해           │
│  2. 시그니처 + 요구사항 + 게이트 작성                     │
│  3. .pumasi/tasks 브리프 작성 → 워커 병렬 스폰            │
│  4. 게이트 검증 → 통합                                   │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
  ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ Worker 1 │     │ Worker 2 │     │ Worker 3 │
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

**품앗이의 존재 이유는 "호스트가 코드를 직접 짜지 않는 것"이다.**

| 가치 | 설명 |
|------|------|
| 호스트 토큰 절약 | 호스트는 설계만, 구현은 워커가 담당 |
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
- "codex 워커로 [작업]" / "grok으로 [작업] 외주"
- "병렬로 [작업] 외주"

자동 감지 (대규모 코딩 요청 시):
- 4개 이상의 독립 파일/모듈 동시 작성 요청
- "전체 [기능] 구현해줘" + 규모가 큰 경우
- 여러 컴포넌트/서비스를 한 번에 만들어야 할 때

트리거 제외:
- "이미지/그림/썸네일/로고 만들어줘" — "코덱스로"가 붙어도 pumasi-image 스킬 소유. 여기로 받지 않는다.
```

### 인자 없이 호출됐을 때

"품앗이 켜줘"처럼 만들 대상이 없으면 §A 질문 도구 1콜로 한 번 묻고(`request_user_input_async`면 호출 후 턴을 끝내고, 답은 다음 메시지로 받는다), 답변을 받은 뒤 상세 설명을 요청한다. 질문 도구가 없을 때만 아래 번호 블록으로 묻는다:

async 호출 형식: `{"questions":[{"title":"헤더 — 질문","options":["추천안 (추천) — 설명","대안 — 설명"]}]}`. 문항에는 `title`·`options`(문자열 배열)만 넣는다. `question`·`header`·`id`는 Plan 모드 `request_user_input` 전용이라 async에 넣으면 파싱 오류가 난다. "기타·직접 적기" 선택지는 넣지 않는다(자유 입력 칸이 자동으로 붙는다).

```text
번호 블록 폴백일 때의 모양
질문: 품앗이 모드로 무엇을 만들까요?
1. 새 프로젝트 — 새로운 앱/서비스를 품앗이 모드로 구현
2. 기능 추가 — 기존 프로젝트에 여러 기능을 병렬로 추가
3. 리팩토링 — 여러 모듈을 동시에 리팩토링
4. 문장으로 직접 알려주기
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
                       → .pumasi/tasks 브리프 → 워커 스폰
                       → 게이트 자동 검증 → 통합
```

---

## 사용자 질문 규칙 (§A)

결정이 꼭 필요할 때는 `$PLUGIN_ROOT/shared/questioning-policy.md §A`의 **질문 도구**(`request_user_input_async`, Plan 모드면 `request_user_input`)로 묻는다.
두 도구가 모두 없을 때만 **채팅 번호형 선택지 블록**(폴백)으로 묻는다.

- 품앗이 요청은 대개 **이미 구체적**이다(만들 것이 명확). §1 + §2c에 따라 추론 가능한 건 묻지 말고,
  요청이 충분히 구체적이거나 사용자가 직접 지시했으면 **즉시 진행**한다(과잉 질문 = 마찰 실패).
- 진짜로 결정이 필요한 경우(예: 스택 선택지가 갈릴 때)만 아래 형식으로 한 번 묻는다(질문 도구가 없을 때의 번호 블록 폴백 모양):
  ```text
  질문: 어떤 백엔드 스택으로 갈까요?
  1. Next.js Route Handlers — 한 레포에 통합, 배포 단순. 트레이드오프: 무거운 백엔드엔 부담
  2. 별도 Fastify API — 역할 분리 명확. 트레이드오프: 레포/배포 2개
  3. 문장으로 직접 알려주기
  ```
- 추천안은 항상 맨 앞(도구에서는 기본 선택, 폴백에서는 **1번**). "모르면 1번으로 진행하겠습니다"로 안내한다. 질문 도구가 있는데 번호 블록으로 때우지 말 것. 도구에서는 "문장으로 직접 알려주기" 선택지를 빼고(자유 입력 자동 추가) 폴백에서만 둔다.
- 이미 명시된 워커·스택은 다시 묻지 않는다.

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

### Phase 0.5: 워커 선택 (기획 승인과 같은 질문에 포함 — 스킵 조건 있음)

기획 승인을 받는 **같은 턴**에 워커 선택 문항을 §A 질문 도구로 함께 낸다(기획 승인 문항과 워커 선택 문항을 도구 1콜에 묶는다. 폴백이면 번호 블록).

아래는 번호 블록 폴백일 때의 모양이다(도구에서는 같은 내용을 선택지로 넣는다. Plan 모드 `request_user_input`은 선택지 2~3개라 1~3번 + "그 밖의 워커는 직접 입력"으로 줄인다).

**스킵 조건**: 사용자가 요청에서 워커를 이미 지명한 경우("grok으로", "codex한테", "cursor로", "agy 외주") — 지명된 워커를 그대로 쓰고 묻지 않는다.

```text
질문: 어떤 CLI 워커에게 외주를 맡길까요?
1. Codex 워커 (권장) — codex exec. 구조화 보고(report.json) 지원, 기본 샌드박스
2. Grok — xAI Grok Build (grok-4.6). SuperGrok 구독이면 한계비용 0. report.json 없이 output.txt 통합
3. 혼합 — 태스크 성격별로 codex/grok/cursor/agy/gjc 나눠 배정 (배정안은 호스트가 제안 후 태스크별 명령으로 반영)
4. Cursor / agy / gjc / claude — Cursor Ultra 구독이면 cursor-agent(Composer·Codex·Opus/Fable급 모델까지 선택 가능), 디자인·UI는 Antigravity(agy), 멀티모델은 gajae-code(gjc), claude CLI(report.json 지원)
```

선택 결과는 Phase 2의 `.pumasi/job.json`에 `defaults.command`(혼합이면 태스크별 `command`)로 기록한다. 각 워커의 정확한 명령 문자열은 아래 **"외주 워커 교체"** 절의 것을 그대로 쓴다.

**선택 직후 설치 확인 1회**: `command -v <cli>` (grok은 실패 시 `$HOME/.grok/bin/grok` 폴백). 미설치·미인증이면 그대로 알리고 중단하거나 §A 질문 도구(없으면 번호 블록)로 다른 워커를 다시 선택받는다. 명시한 워커를 Codex로 몰래 바꾸지 않는다.

### Phase 1: 분석 (Host)

요청을 받으면 **독립적으로 병렬 실행 가능한** 서브태스크로 분해.

**좋은 서브태스크 조건**:
- 다른 서브태스크 완료를 기다리지 않아도 됨
- 명확한 입출력(시그니처) 정의 가능
- 워커 혼자 구현 가능한 범위
- 파일/기능 경계가 명확함

### Phase 2: 공유 상태 초기화 + 브리프 작성 (Host)

```bash
python3 $PLUGIN_ROOT/skills/pumasi/scripts/init_workspace.py --root "$PWD" --task "<작업 요약>"
```

생성물:
- `.pumasi/job.json` — 잡 상태(태스크/라운드/선택된 워커 명령)
- `.pumasi/plan.md` — 통합 컨텍스트 (워커 실행 중 계속 갱신)
- `.pumasi/tasks/<task>.md` — 태스크별 작업 브리프
- `.pumasi/reports/` — 워커 보고 수집 위치

**작업 브리프(`.pumasi/tasks/<task>.md`)에 반드시 담을 것:**
1. 시그니처와 요구사항만 작성 (코드 본문 작성 금지)
2. owned files / 디렉토리 (다른 워커와 겹치지 않게)
3. 필수 import / 라이브러리 + 금지 대체
4. 강한 게이트 명령 (tsc/build/test 중심)
5. "다른 워커가 같은 레포를 동시에 편집 중"이라는 알림
6. 보고 형식 — Codex/claude 워커는 `$PLUGIN_ROOT/skills/pumasi/scripts/codex-output-schema.json` 스키마의 JSON을 `.pumasi/reports/<task>.report.json`으로, 그 외 워커는 마지막 응답을 `.pumasi/reports/<task>.output.txt`로 남기게 한다

### Phase 3: 워커 스폰 (Host → 병렬 워커)

태스크당 워커 1개를 병렬로 스폰한다. 각 워커 프롬프트에는 해당 `.pumasi/tasks/<task>.md` 브리프를 그대로 전달한다.

- **Codex 멀티에이전트**(v0.139+ 안정): 태스크별 sub-agent를 동시 실행
- 또는 **`codex exec`** 세션을 태스크별로 백그라운드 스폰 — 예: `codex exec --dangerously-bypass-approvals-and-sandbox --output-schema $PLUGIN_ROOT/skills/pumasi/scripts/codex-output-schema.json -o .pumasi/reports/<task>.report.json "<브리프>" < /dev/null`
- 다른 워커를 선택했으면 "외주 워커 교체" 절의 명령으로 스폰한다. **`--output-schema`/`-o`는 Codex 전용 플래그**라 다른 CLI에 넘기면 알 수 없는 플래그로 즉사한다 — 절대 새지 않게 한다.

> 워커는 브리프의 시그니처/요구사항/게이트만 받고 **구현 본문은 워커가 작성**한다. 호스트가 본문을 써서 넘기면 안 된다.

> ⚠️ **샌드박스/승인 우회 경계 (opt-in).** 비대화형 병렬 워커가 승인 프롬프트 없이 파일을 쓰려면
> `codex exec --dangerously-bypass-approvals-and-sandbox`(또는 `--full-auto`) / `--sandbox workspace --always-approve`(grok) /
> `--force`(cursor-agent) / `--dangerously-skip-permissions`(agy)가 필요하다 — 병렬 외주 자동화를 위해 필요한 동작이다.
> 따라서 품앗이는 **신뢰하는 본인 레포에서만** 실행하고, 외부에서 받은/검토 안 된 코드베이스나 프롬프트에는 쓰지 않는다.
> 품앗이 호출 자체가 이 우회에 대한 명시적 동의이며, 우회 없이 돌리려면 해당 플래그를 빼고 codex 기본 샌드박스(`--full-auto` 등)로 워커를 스폰한다.

### Phase 4: 모니터링 (Host)

워커가 도는 동안 `.pumasi/plan.md`의 통합 컨텍스트를 최신으로 유지한다. 완료 보고/산출 파일을 `.pumasi/reports/`에서 수집한다.
한 워커가 끝났다고 전체가 끝난 것이 아니다 — 모든 워커가 종료 상태에 도달할 때까지 기다린 뒤 Phase 5로 간다.

### Phase 5: 게이트 검증 + 선택적 코드 리뷰 (Host)

**4단계 검증 프로세스:**

```
Step 0: 의존성 확인 (게이트 실행 전 필수)
  └── node_modules가 없으면: 프로젝트 디렉터리에서 npm install --silent
  └── tsc/build/test 게이트는 의존성 설치 후에만 유효

Step 1: 자동 게이트 실행 (bash, 토큰 0)
  └── tsc --noEmit → npm run build → npm test → grep 확인

Step 2: 결과 판정
  ├── 전부 통과 → 워커 보고서(report.json / output.txt)만 읽기 (토큰 소량)
  └── 실패 있음 → 실패한 게이트 관련 코드만 읽기 (토큰 최소화)

Step 3: 서브태스크 간 인터페이스 확인
  └── 타입/import 경로 등 교차 검증
```

보고서를 읽을 때는 원문 프롬프트·stdout·stderr를 다시 펼치지 말고 **구조화 보고 + 게이트 결과 + 원본 파일 경로**만 보는 compact 방식으로 시작한다. 실패·부분 완료·보고 누락을 조사할 때만 해당 원본 파일을 읽는다.

**공유 읽기 전용 게이트**: 여러 태스크가 같은 작업 디렉터리에서 같은 결정론적·읽기 전용 검사(예: `npx tsc --noEmit`)를 요구하면, 모든 워커가 완료된 뒤 한 번만 실행해 통과 결과를 태스크별로 귀속시킬 수 있다. 실패·타임아웃, 작업 디렉터리가 다른 검사, 포맷터·스냅샷 갱신·외부 서비스·실행 순서에 의존하는 검사에는 적용하지 않고, 다음 검증 라운드에서는 항상 다시 검사한다.

### Phase 5.5: 코드 정리 (선택적)

> 게이트가 모두 통과했지만 코드 품질을 한 단계 높이고 싶을 때 사용.

**조건**: Phase 5 게이트 전부 PASS + 태스크 3개 이상일 때 권장.
정리(simplify) 패스 후 게이트를 재실행하고 Phase 6 통합으로 넘어간다.

### Phase 6: 통합 및 수정 (Host 판단 + 워커 재위임)

**수정이 필요한 경우**: 호스트가 직접 고치지 않고 해당 태스크만 워커에게 재위임. 재위임에도 Phase 0.5에서 고른 워커를 그대로 쓴다.

```
호스트가 하는 일: "뭘 고칠지" 결정 (자연어 수정 지시 + 좁힌 컨텍스트)
워커가 하는 일: 실제 수정 실행
```

**수정이 필요 없는 경우**: 서브태스크 간 연결만 확인 후 통합한다. 검증이 끝나기 전에는 `.pumasi/` 산출물을 지우지 않는다.

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

## 외주 워커 교체 (선택) — Grok(`grok`) / Cursor(`cursor-agent`) / gajae-code(`gjc`) / Antigravity CLI(`agy`) / `claude`

기본 워커(Codex) 대신 태스크별 또는 잡 전체에 다른 CLI를 명시할 수 있다. 프롬프트(브리프)는 **마지막 positional 인자**로 전달한다
(`claude`만 stdin). Codex 전용 `--output-schema`/`-o`는 다른 CLI에 넣지 않는다 → 그 워커들은 `report.json` 없이 `output.txt` 기반으로 통합한다(graceful).

**Grok CLI(`grok`)** — xAI Grok Build (코드·대규모 분석):
```text
grok --no-auto-update --no-alt-screen --sandbox workspace --always-approve -p "<브리프>"
```
- 실측(2026-08-23, grok 1.0.4): 워커 3개 동시 실행 전부 exit 0, 게이트 9/9 통과, 비-TTY 파이프에서 stdout 정상 — agy 같은 누락 버그 없음.
- **샌드박스가 기본 off**라 `--sandbox workspace`로 조인다 (codex와 반대 — codex는 기본 샌드박스).
- **자동 업데이터가 백그라운드로 돌므로 `--no-auto-update` 필수.** 넣지 않으면 워커 실행 중 업데이트가 끼어든다.
- grok 자체는 `--json-schema`로 구조화 출력을 지원하지만 결과가 stdout JSON의 `.text`에 **문자열로 중첩**되므로 파일로 떨어지지 않는다 (언랩 필요 — 미구현).
- 모델은 grok 기본값(`grok-4.6`) 사용. `grok-code-fast-1`은 2026-08-15 폐기되었으므로 쓰지 않는다.
- 인증: `grok login`(구독 세션, `XAI_API_KEY` 불필요) 또는 `XAI_API_KEY` 환경변수.
- ⚠️ **PATH 주의**: `~/.grok/bin/grok`에 설치되고 셸 프로필을 통해 PATH에 들어간다. 비대화형 셸에서 `command -v grok`이 실패하면 절대경로(`$HOME/.grok/bin/grok`)로 지정한다. npm 서드파티 `@vibe-kit/grok-cli`가 같은 `grok` 이름을 쓰므로 어느 쪽이 잡히는지 확인한다.
- 설치: `curl -fsSL https://x.ai/cli/install.sh | bash` (원격 스크립트 즉시 실행 — 내용을 먼저 확인하려면 `-o`로 받아서 읽고 실행).

**Cursor CLI(`cursor-agent`)** — Cursor Ultra 구독 워커 (Composer/Codex/Opus·Fable급 멀티모델):
```text
cursor-agent -p --force --output-format text "<브리프>"
# 모델 핀 예: cursor-agent -p --force --model composer-2.5 --output-format text "<브리프>"
```
- **모델 선택이 최대 강점**: `--model`로 `composer-2.5`(빠른 편집), `gpt-5.3-codex-*` 계열, `claude-opus-5-thinking-high` / `claude-fable-5-thinking-high`까지 지정 가능 — 다른 구독 쿼터가 소진됐을 때 Cursor 구독으로 잇는 우회 경로가 된다. 목록: `cursor-agent --list-models`.
- `-p`(print) + `--output-format text` 필수.
- **`--force` 필수** — 없으면 "Do you trust the contents of this directory?"에서 멈춘다(비대화형 즉사, 파일 생성 0건). CLI 안내대로 `--trust` / `--yolo` / `-f` 중 아무거나면 되고, `--yolo`는 `--force`의 별칭이다. (실측 2026-08-27: 신뢰 이력 없는 새 디렉터리에서 `--force`만으로 통과)
- 실측 E2E(2026-08-27, 2026.08.25 빌드): 워커 2개 동시 실행(하나는 `--model composer-2.5`, 하나는 기본) **둘 다 exit 0, 게이트 4/4 통과, 소요 47~59초**, `output.txt` 정상 회수.
- ⚠️ **훅 충돌 주의**: Orca 등이 `~/.cursor/hooks.json`에 preToolUse 훅을 심어두면 참조 스크립트가 사라졌을 때 "환경 훅 오류로 파일 생성 차단"으로 전 작업이 실패한다. 워커가 이 에러를 내면 `~/.cursor/hooks.json`을 확인한다.
- 인증: `cursor-agent status`로 확인 (IDE 로그인 공유). 자동화·CI는 `CURSOR_API_KEY` 환경변수.
- 설치: `curl https://cursor.com/install -fsS | bash` → `~/.local/bin/`에 배포된다. 같은 바이너리가 `agent`라는 이름으로도 심링크되지만, **`agent`는 grok CLI(`~/.grok/bin/agent`)와 이름이 충돌**하므로 반드시 `cursor-agent`(또는 절대경로)를 쓴다.

**gajae-code(`gjc`)** — 멀티모델 코딩 CLI (`Yeachan-Heo/gajae-code`):
```text
gjc --print "<브리프>"        # 필요 시 gjc --print --model opus 등으로 핀
```
- 실측(2026-06-19): 비-TTY 파이프에서도 stdout 정상 출력. 설치: https://github.com/Yeachan-Heo/gajae-code

**Antigravity CLI(`agy`)** (디자인/UI):
```text
agy --dangerously-skip-permissions -p "<브리프>"
```
- `agy` 1.0.x는 비-TTY(파이프)에서 stdout 출력이 누락되는 버그가 있어 `output.txt`가 빌 수 있다. 결과가 비면 호스트가 파일 산출물로 직접 통합하거나 codex로 폴백한다.
- 모델 지정 플래그(`-m`)는 헤드리스에서 미지원/고정으로 보고됨 → 명령에 넣지 않는다.
- 설치(검증 권장): `curl -fsSL https://antigravity.google/cli/install.sh -o /tmp/agy-install.sh` → 내용 확인 → `bash /tmp/agy-install.sh`.

**`claude` CLI** — 구조화 보고 지원 워커:
```text
claude --print --permission-mode acceptEdits --output-format json < .pumasi/tasks/<task>.md
# 더 좁게: claude --print --permission-mode acceptEdits --tools "Read,Edit,Write" --output-format json
```
- 프롬프트는 stdin. JSON 응답의 `structured_output`을 `report.json` 계약(files/status/summary/signatures/dependencies/risks)으로 정규화해 저장한다.
- API 에러 봉투·잘못된/누락 보고·타임아웃·비0 종료는 절대 성공으로 처리하지 않는다(텍스트 성공 폴백 없음). 워커 호출 시 상속된 `CLAUDECODE` 중첩 마커만 제거한다.

**task별 혼합**: 모듈마다 다른 명령을 지정하면 codex / grok / cursor / gjc / agy / claude에 병렬로 나눠 외주할 수 있다.

> ⚠️ **같은 과제를 여러 워커에게 시키는 "토너먼트"는 품앗이의 기능이 아니다.** 품앗이의 본질은 *분할*이고
> 토너먼트는 *중복*이라 "단일 파일 작업 = 병렬 이점 없음" 규칙과 충돌한다. 경쟁·채점·승자 채택이 필요하면
> 끼리끼리(kkirikkiri)의 Workflow 경로를 쓴다.

---

## 사전 조건

```bash
command -v codex   # 설치 확인
# 없으면: npm install -g @openai/codex
```

- Codex CLI 설치 + 로그인 완료
- 워커 스폰: Codex 멀티에이전트(v0.139+) 또는 `codex exec`
- (선택한 경우) 대체 워커 CLI 설치 + 인증: grok / cursor-agent / gjc / agy / claude

---

## 파일 구조

```
$PLUGIN_ROOT/skills/pumasi/
├── SKILL.md                    # 이 문서
├── references/
│   ├── anti-patterns.md        # 복붙형 instruction 금지 + Red Flags
│   ├── role-separation.md      # 호스트 vs 워커 역할 경계
│   ├── codex-guide.md          # Codex 워커 특성 + instruction 규칙
│   ├── instruction-templates.md # 템플릿 + 좋은/나쁜 예시
│   ├── tech-stack.md           # 모던 기술스택 추천표
│   └── examples.md             # 실행 예시 + 브리프 예시
└── scripts/
    ├── init_workspace.py       # .pumasi 공유 상태 초기화
    └── codex-output-schema.json # 워커 구조화 보고 스키마 (codex/claude 워커용)

프로젝트 디렉토리/
└── .pumasi/
    ├── job.json                # 잡 상태 + 선택된 워커 명령
    ├── plan.md                 # 통합 컨텍스트
    ├── tasks/<task>.md         # 태스크별 브리프
    └── reports/                # report.json / output.txt
```
