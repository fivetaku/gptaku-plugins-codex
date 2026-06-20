# gptaku-plugins-codex 재포팅 / 최신화 계획서 (v2 — 리서치 반영)

> 작성: 2026-06-20 · 대상: `gptaku-plugins-codex` · 기준 본진: `gptaku-plugins`(June 2026)
> v2 변경: docs-guide 리서치로 **"Codex=skill-only·훅 없음" 전제를 폐기**. Codex 플러그인 모델은
> 본진과 거의 패리티(hooks·agents·MCP·/goal). 실질 갭은 **AskUserQuestion 하나**.
> 결정 반영: ①goaljaby=native /goal로 이식 ②update-notifier=SessionStart hook ③버전=본진과 동일 ④풀 기능 패리티.

---

## 1. 현황 (baseline)

| | Codex 레포 | 본진 `plugins/` |
|--|--|--|
| 마지막 커밋 | **2026-04-24** (3커밋) | 2026-06-19 (지속) |
| 플러그인 | 11개, **전부 v0.1.0** | 14개, v0.3~v2.3 |
| 사용 중인 구조 | skill-only (`.codex-plugin/`) | commands + skills + agents + hooks |
| 횡단 기능 | 없음 | questioning-policy · update-notifier · auto-star |

콘텐츠 드리프트(git-teacher, skill 6개 이름 동일): Codex판 = 본진의 **20~40% 분량**. v0.1.0 1패스에서 동결.

---

## 2. ★ 리서치로 확정된 프리미티브 패리티 (방향의 핵심)

Codex CLI(~v0.140, 2026-06)는 본진 Claude Code 플러그인의 거의 모든 구성요소에 **네이티브 대응**이 있다. 기존 Codex 포트가 skill-only였던 건 v0.1.0 최소 포팅이었을 뿐, **Codex의 한계가 아니다.**

| 본진 (Claude Code) | Codex 대응 | 판정 | 출처 |
|--|--|--|--|
| commands | skills (`SKILL.md`) | 1:1 (콘텐츠만 최신화) | codex/skills |
| agents | **런타임 multi-agent spawn**(지침을 소유 스킬에 임베드) — ⚠️ 플러그인에 `agents/` 로스터 폴더 **없음**(`agents/openai.yaml`은 인터페이스 메타데이터지 서브에이전트 정의 아님) | 기능은 이식되나 구조는 다름 | 검증: validate_plugin.py |
| settings.json hooks (`SessionStart`·`UserPromptSubmit`·`PreToolUse`…) | `hooks.json`/config.toml `[hooks]` (**동일 이벤트군**) | **1:1 이식** | codex/hooks |
| MCP servers | 매니페스트 `mcpServers`(→`.mcp.json`) | 1:1 | codex/plugins/build |
| `/goal` (OMC ultragoal) | **native `/goal`** + `/plan` + ExecPlan(`PLANS.md`) | 1:1 (이름까지 동일) | codex/use-cases/follow-goals |
| `${CLAUDE_PLUGIN_ROOT}` | `$PLUGIN_ROOT` (+ `CLAUDE_PLUGIN_ROOT` alias 호환) | 1:1 | codex/plugins/build |
| auto-star (setup.sh + Step 0) | `SessionStart` hook + marker 게이트 | 1:1 | codex/hooks |
| update-notifier hook | `SessionStart` hook → `{"systemMessage":"…"}` | 1:1 (마켓 자동알림 無 → 자체 notifier 유지) | codex/hooks · plugins/build |
| **`AskUserQuestion`** | **없음** | ★**유일 실질 갭** → §A 번호채팅 치환 | codex/cli/features |

**결론**: 풀 기능 패리티 재포팅은 전적으로 실현 가능. 창의적 치환이 필요한 건 AskUserQuestion 단 하나(이미 §A로 해결).

---

## 3. 워크스트림 (v2)

### WS1. AskUserQuestion 치환 — 유일한 실질 갭 / P0 토대 완료
- Codex에 카드 UI 없음(확정). 치환 = `shared/questioning-policy.md §A`(번호 선택지+예시 프리뷰).
- **완료**: §A SSOT 신설 + show-me-the-prd-codex 인용·시연.
- **남음**: 인터뷰 플러그인 7종 §A+§0~§4 인용 연결.

### WS2. 콘텐츠 풀 재포팅 (기능 패리티)
- 각 Codex skill을 **현재 본진 command/skill에서 재생성**, 최신 인터뷰 단계·리서치 전략·템플릿을 Codex 어법으로 재서술. 본진 기능 100% 패리티 목표(결정 ④).

### WS3. agents → 런타임 multi-agent (로스터 파일 아님)
- 본진 agents 보유: **docs-guide(1), vibe-sunsang(1)**.
- ⚠️ **교정(P1에서 확정)**: Codex 플러그인 스키마에 `agents/` 폴더·`plugin.json "agents"` 필드 **없음**(validate_plugin.py가 거부). `agents/openai.yaml`은 *인터페이스 메타데이터*다.
- 올바른 이식: 에이전트 지침을 **소유 스킬 안에 임베드**하고, 무거우면 Codex 런타임 `multi_agent` spawn(정의 파일 없이 지침을 프롬프트로 직접 전달)으로 분리, 불가 시 인라인. vibe-sunsang growth가 이 패턴으로 완료됨.

### WS4. hooks 이식 (auto-star + update-notifier)
- 매니페스트에 `hooks` 필드 추가 → `SessionStart`(`matcher:"startup|resume"`) hook.
- **auto-star**: hook command가 marker(`~/.gptaku-star/` 등가) 체크 후 1회 star, self-disable.
- **update-notifier**: hook이 버전 비교 후 `{"systemMessage":"Update available vX.Y.Z — codex plugin marketplace upgrade <name>"}` 출력. (Codex 마켓은 자동 업데이트 알림 없음 → 자체 notifier 필수.)
- 본진 `setup.sh` 첫-실행 부트스트랩 → 동일 SessionStart hook + marker로 흡수(Codex엔 별도 plugin-load 이벤트 없음).

### WS5. 미포팅 3종 풀 포팅
| 플러그인 | 본진 의존성 | Codex 포팅 방안(결정 반영) |
|--|--|--|
| **goaljaby** | `/goal` 핸드오프 | **native `/goal`로 이식**(결정 ①). 한국어 검토문서 + `PLANS.md`(ExecPlan: Progress/Validation/Decision-Log) 생성 후 `/goal Execute ./PLANS.md …; keep Progress current; stop when <done>`. 객관식은 §A. ⚠️`codex features list`로 goals 활성화 확인 |
| **dd** | OS clipboard→Claude 컨텍스트 주입 | clipboard(pbpaste)는 OS-level 유지, 주입은 Codex SKILL.md가 캡처본을 읽어 컨텍스트화 |
| **insane-review** | `bin/pack_and_ask.py`(독립 py 웹브릿지) | 거의 독립 → `$PLUGIN_ROOT` env 치환 + Codex skill 래핑. 본진 안정화(45커밋 활발) 후 막차로 |

### WS6. 버전·릴리즈 정렬 (결정 ③)
- 각 Codex plugin.json 버전을 **본진과 동일**하게 bump(예: show-me-the-prd v0.1.0 → v0.8.2). marketplace 카탈로그·README 갱신. `scripts/` smoke test 통과.

---

## 4. 페이즈 로드맵

- **P0 — 토대** ✅: §A SSOT + show-me-the-prd-codex 시연.
- **P1 — 핵심 인터뷰 3종 풀 재포팅**: kkirikkiri(§2b)·vibe-sunsang(§2c)·git-teacher(§2a) — WS1+WS2(+vibe-sunsang는 WS3 agent).
- **P2 — 잔여 인터뷰/메뉴 6종**: skillers-suda·insane-research·pumasi·nopal·insane-design·docs-guide(WS3 agent) — WS1+WS2.
- **P3 — hooks 횡단 적용**: 전 플러그인 auto-star + update-notifier(WS4). shared hook 1벌 + 매니페스트 배선.
- **P4 — 미포팅 3종**: goaljaby(native /goal) → dd → insane-review (WS5).
- **P5 — 버전 정렬·릴리즈**: WS6 + 전수 smoke test.

각 페이즈 종료 시 버전 bump + 본진 CLAUDE.md Step 1~8 동등 절차로 캐시/매니페스트 정합.

---

## 5. 검증 caveats (셸에서 확인 후 진행)

1. **goals 활성화** — `/goal`이 기본 on인지 `[features] goals=true`/`codex features enable goals` 필요한지 타깃 버전에서 `codex features list`로 확인.
2. **SessionStart→systemMessage 왕복** — 설치된 Codex 버전에서 plugin-scoped hook이 `$PLUGIN_ROOT` 읽어 `systemMessage` 띄우는지 end-to-end 테스트 후 의존.
3. ~~`agents/openai.yaml` 스키마~~ — **해소(P1)**: `agents/` 로스터는 무효. WS3 교정 참조.

### ★ 공식 검증 게이트 (P1에서 확립 — 모든 페이즈 필수)
- 매 플러그인 변경 후 **`python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py <plugin-path>`** 통과 필수. P1에서 실제 결함 2건(무효 `agents` 필드 / YAML frontmatter 깨짐) 포착.
- **유효 plugin.json 필드**: name·version·description·author·homepage·repository·license·keywords·skills·**hooks**(경로)·mcpServers·apps·interface. (그 외 필드는 거부 → WS4 hooks는 `hooks` 필드로 선언 가능 = P3 청신호)
- **YAML 함정**: 스킬 frontmatter `description`에 `Korean triggers: "…"` 처럼 **콜론+공백**이 있으면 평문 스칼라가 깨짐 → `triggers — "…"`(엠대시)로. P2/P4 신규 스킬 작성 시 주의.

---

## 6. 진행 현황 (2026-06-20)

- [x] P0: `shared/questioning-policy.md`(Codex §A) 신설
- [x] P0: `show-me-the-prd-codex` SKILL.md — 정책 인용 + §A 명시
- [x] 리서치: Codex /goal·hooks·notify·skills·agents 프리미티브 패리티 확정(§2)
- [x] **P1 완료(검증됨)**: kkirikkiri v0.21.3 · vibe-sunsang v2.1.2 · git-teacher v1.5.2 풀 재포팅. §A 치환·§2x 인라인·버전 정렬. 공식 validate_plugin.py 11종 전부 pass. (codex env 확정: goals·hooks·multi_agent 모두 stable/true)
- [ ] P2~P5: 위 로드맵

### 결정 로그
- ① goaljaby → native `/goal` + ExecPlan으로 이식 (비이식 폐기)
- ② update-notifier → `SessionStart` hook + `systemMessage` (Codex 자체 알림 없음 확인)
- ③ 버전 → Codex 포트를 본진과 **동일 버전**으로 정렬
- ④ 깊이 → **풀 기능 패리티** 재포팅
