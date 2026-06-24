---
name: pumasi-image
description: Image-generation companion skill for the pumasi plugin family. Use when the user wants an image, thumbnail, poster, logo, illustration, or related visual artifact. In Codex this maps directly to the native image generation/editing tool. Korean triggers — "이미지 만들어줘", "그림 생성", "썸네일 만들어", "로고 만들어줘". English triggers — "create image", "make thumbnail", "make logo", "draw illustration". DO NOT trigger on code-generation requests like "함수/컴포넌트/페이지 만들어줘" — those go to the pumasi skill.
---

# /pumasi-image — Codex 이미지 생성

> Codex CLI의 네이티브 이미지 생성/편집 도구(`/imagen`, gpt-image-2)로 이미지를 만든다.
> 코드 병렬 외주(pumasi)와 완전히 분리된 독립 스킬.

## 먼저 읽을 것

- `references/clarification-matrix.md` — 모드별 의도 파악 질문 매트릭스
- `references/keyword-mapping.md` — 비율·퀄리티 키워드 자동 매핑 + 자연어 힌트 변환표
- `references/image-studio-prompt.md` — 모드 분류 + Output Template 시스템 프롬프트 (영문 프롬프트 작성 직전에만 Read)

---

## 핵심 원칙

1. **백엔드는 Codex 네이티브 이미지 도구 단일** — nanobanana 등 다른 백엔드 사용 안 함
2. **image-studio 시스템 프롬프트 내면화** — 모드 분류 + Output Template 작성
3. **후처리 절대 금지** — sips/ImageMagick/재인코딩 금지, 생성 원본(반환된 base64) 그대로 저장. `generated_images/` watch·복사 금지(스테일 중복 버그)
4. **저장 경로 고정** — `{BASE_DIR}/images/{YYYY-MM-DD}/{slug}-{seq}.png`
5. **최대 5개 질문** — 기술 2개 + 의도 3개, 조건부 스킵
6. **텍스트는 이미지 도구가 직접 렌더링한다** — 썸네일·포스터·로고의 한글/영문 카피는 프롬프트의 Text Integration 섹션에 따옴표로 묶어 그대로 명시. **HTML/CSS 분리·후합성·텍스트 레이어 분할 절대 금지.** 구세대 diffusion(SD/Midjourney) 가정으로 "텍스트 못 그림"이라고 회피하지 말 것 — 다음 §의 capability snapshot 참조.

---

## gpt-image-2 capability snapshot (as of 2026-05)

> 목적: 구세대 diffusion 직감으로 회피 행동(HTML/CSS 분리, 텍스트 빼고 합성, 재시도 회피)을 하지 못하게 capability를 명시적으로 박는다. 모델 업데이트 시 `as of` 날짜 기준으로 갱신.

### CAN (자신 있게 시도)
- **한글/영문 헤드라인 텍스트** — 16pt 이상 굵은 sans-serif/serif, 정확한 자모/획
- **다국어 혼용** — 한+영 동시 노출(예: "광안대교 BEST 5 / Best Spots")
- **로고 타이포그래피** — 워드마크, 레터마크, 한자/한글 디자인 타이포
- **숫자/날짜 단순 표기** — "2026", "BEST 5", "Vol.3" 정도는 안정적
- **복잡한 레이아웃** — 헤드라인 + 서브카피 + 가격표 + CTA 버튼 한 컷에
- **표·UI 목업·차트** — 행/열 정렬, 라벨, 범례, 막대그래프 텍스트
- **손/얼굴/포즈 디테일** — 손가락 개수, 표정, 시선 방향 정확
- **사진 사실성** — DSLR 룩, 조명 일관성, 그림자/반사 물리

### WEAK (조심해서 시도, 결과 보고 판단)
- **매우 작은 글씨** — 8pt 이하 본문은 깨질 확률 높음 → 헤드라인 위주로 설계
- **긴 본문 단락** — 한 블록 50자 이상은 중간에 자모 흔들림 가능
- **정확성이 중요한 숫자** — 가격/날짜/전화번호는 1-2글자 변형 위험 (생성 후 검수 필수)
- **손글씨/캘리그래피 한글** — 자모 결합 흔들림 잦음, 정자체 폰트가 안전

### CAN'T 가정 금지 (구세대 diffusion 직감 차단)
- ❌ "한글은 어차피 깨지니까 영문으로만 만들자" — gpt-image-2는 한글 OK
- ❌ "텍스트는 빼고 만든 후 HTML/CSS로 합성하자" — 1차 직접 렌더 금지 사유 아님
- ❌ "썸네일이니까 텍스트 부분만 따로 디자인하자" — 한 컷에 통합 렌더가 정석
- ❌ "로고에 한자/한글 들어가면 안 됨" — 워드마크 직접 렌더 가능

### 운영 룰
1. **1차는 무조건 네이티브 이미지 도구로 직접 렌더** — 텍스트 포함 여부 무관
2. **결과 검수** — 이미지 표시 후 텍스트 정확도 사용자 확인 (Step 7 모드 참조)
3. **재시도 우선** — 첫 결과가 깨졌으면 프롬프트 보강(폰트 명시, 크기 명시)해서 1-2회 재생성
4. **합성 옵션은 사용자 명시 거부 후** — "직접 렌더 결과 마음에 안 들어, 합성으로 가자"는 사용자 발화가 있을 때만 후합성 워크플로우 제안

---

## 워크플로우

### Step 1: 모드 자동 감지

사용자 요청에서 7가지 모드 중 하나를 결정한다:

| 모드 | 감지 키워드 |
|------|-----------|
| MODE_A_PORTRAIT | "프로필", "인물", "얼굴", "초상" |
| MODE_B_LANDSCAPE | "풍경", "배경", "자연", "도시", "바다", "산" |
| MODE_C_OBJECT | "제품", "물건", "아이템", "상품" |
| MODE_D_ILLUSTRATION | "일러스트", "그림", "아트", "드로잉" |
| MODE_E_THUMBNAIL | "썸네일", "커버", "대표이미지", "유튜브" |
| MODE_F_LOGO | "로고", "브랜드", "심볼", "아이콘" |
| MODE_G_CONCEPTUAL | "컨셉트", "추상", "아이디어", "상징" |

모드 판단 불확실 시 Step 3의 질문에 "모드 선택" 1개를 추가한다.

### Step 2: 키워드 자동 매핑 → 파라미터 추출

`references/keyword-mapping.md`를 Read하여 비율·퀄리티 자연어 힌트를 추출한다.

- 비율 키워드가 입력에 있으면 → 비율 질문 스킵
- 퀄리티 키워드가 입력에 있으면 → 퀄리티 질문 스킵

### Step 3: 사용자 질문 (§A 번호형 블록, 최대 5개)

Codex CLI에는 Claude Code의 `AskUserQuestion` 카드 UI가 **없다.** 결정이 꼭 필요하면
`shared/questioning-policy.md §A`의 **채팅 번호형 선택지 블록**으로 대체한다.

`references/clarification-matrix.md`를 Read하여 모드별 의도 파악 카테고리 3개를 확정한다.

**질문 순서**:
1. 비율 (Step 2에서 확정됐으면 스킵)
2. 퀄리티 (Step 2에서 확정됐으면 스킵)
3~5. 의도 파악 3개 (모드 매트릭스 기반)

**질문 원칙**:
- §1 + §2c: 이미 입력에서 확정된 차원은 **묻지 않는다**. 요청이 구체적이면 질문 없이 바로 생성한다(과잉 질문 = 마찰 실패).
- 물을 때는 §A 번호형 블록으로 — 각 슬롯당 5개 이상 선택지, 그중 1~2개는 창의적 대안(★), 마지막은 "문장으로 직접 알려주기"(Other 대체).
- "자동 추천(AI 판단)" 안전망 선택지를 항상 포함하고, "모르면 1번(자동 추천)으로 진행하겠습니다"로 안내한다.
- 여러 슬롯을 한 번에 물을 때는 각 질문 블록을 이어서 출력하고 "여러 개면 1,3처럼 적어주세요"로 안내. 카드 UI를 흉내내지 말 것.

§A 블록 예시 (단일 슬롯):
```text
질문: 어떤 분위기로 갈까요?
1. 자동 추천 — 내용에 맞게 판단. 결정 피로 없이 진행
2. 다크 시네마틱 — 영화적, 깊은 그림자
3. 따뜻함 — 친근, 햇살, 파스텔
4. 조용한 위로감 (★) — 잔잔함, 여운
5. 문장으로 직접 알려주기
```

### Step 4: image-studio 내면화 + Output Template 작성

`references/image-studio-prompt.md`를 Read하여 시스템 프롬프트를 내면화한다.

내면화 후:
1. Normalization JSON 내부적으로 작성 (노출하지 않음)
2. 선택된 모드의 Output Template을 200~500 단어 영문 프롬프트로 작성
3. 사용자 선택 값(비율·퀄리티·의도 3개)을 Technical Specifications / Anti-Patterns 섹션에 반영
4. 비율·퀄리티 자연어 힌트를 Technical Specifications에 삽입 (keyword-mapping.md 참조)

프롬프트를 다음 경로에 저장 (없으면 `mkdir -p`):
```
{BASE_DIR}/.pumasi/imagen/prompt-{timestamp}.md
```

### Step 5: 저장 경로 계산

**기준 디렉토리 (하드코딩 금지, 동적 계산)**:

```bash
BASE_DIR=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
DATE=$(date +%Y-%m-%d)
TARGET_DIR="${BASE_DIR}/images/${DATE}"
mkdir -p "$TARGET_DIR"

SLUG="busan-gwangan-bridge-night"  # 요청에서 계산 (핵심 명사 1~2개 → 영문 kebab-case)
SEQ=1
TARGET_PATH="${TARGET_DIR}/${SLUG}-$(printf '%02d' $SEQ).png"
while [[ -e "$TARGET_PATH" ]]; do
  SEQ=$((SEQ + 1))
  TARGET_PATH="${TARGET_DIR}/${SLUG}-$(printf '%02d' $SEQ).png"
done
echo "$TARGET_PATH"
```

**왜 git root 기준인가**: 세션의 cwd가 항상 프로젝트 루트는 아니다. 단순 상대경로는 엉뚱한 곳에 저장될 위험이 있어, 프로젝트 루트의 `images/` 하위를 기본값으로 둔다. git 저장소 밖이면 `pwd` 기준.

slug 예: "부산 광안대교 야경" → `busan-gwangan-bridge-night`, "AI 마켓플레이스 로고" → `ai-marketplace-logo`.

### Step 6: 네이티브 이미지 도구 호출

Codex의 **네이티브 이미지 생성/편집 도구(`/imagen`, gpt-image-2)** 를 직접 호출한다.

- 백그라운드 CLI 세션을 띄우지 않는다.
- Step 4의 영문 프롬프트 + Step 5의 타깃 경로를 도구에 전달한다.
- 프롬프트 끝에 후처리 금지 가드(원본 유지, 재인코딩 금지)를 명시한다.
- 텍스트가 깨졌으면 합성하지 말고 프롬프트를 보강해 1~2회 재생성한다(운영 룰 3).

#### ⚠️ base64 캡처 규칙 (codex 이미지 도구의 핵심 동작)

`codex` 이미지 생성은 인터랙티브 TUI와 **다르게** 동작한다:

- **이미지를 base64(inline)로만 반환**한다. 도구 결과의 `image_generation_call` / `image_generation_end`
  이벤트 `result` 필드에 base64 PNG가 실려 온다.
- `~/.codex/generated_images/` 에 파일을 **저장하지 않는다.** 따라서 그 디렉토리를 watch 하거나
  "방금 생긴 폴더를 복사"하는 방식은 **금지**한다 — 스테일 이미지를 잘못 집어오는 중복 버그의 원인이다.
- 호스트는 **이번 호출에서 돌아온 base64를 디코딩해 Step 5의 타깃 경로에 직접 저장**한다.
  생성이 0장이면 거짓 성공을 보고하지 말고 실패로 처리한다.

#### codex exec 위임 경로 (선택) — scripts 사용

직접 이미지 도구를 부르는 대신 별도 `codex exec` 워커에 위임하려면(또는 영문 프롬프트
작성까지 위임하려면) `scripts/`의 결정적 래퍼를 쓴다. 래퍼는 `codex exec --json`으로 이벤트(JSONL)를
받아 `extract_image.py`로 base64를 디코딩해 타깃에 직접 저장한다(스테일 오집음 불가, 0장이면 exit≠0):

```bash
# 영문 프롬프트는 호스트가 작성, 생성만 위임
bash $PLUGIN_ROOT/skills/pumasi-image/scripts/imagen.sh \
  "{prompt_file_path}" "{target_image_path}" "{aspect e.g. 16:9 — 생략 가능}"

# 영문 프롬프트 작성까지 codex에 위임 (PUMASI_IMAGE_DELEGATE_PROMPT 경로)
bash $PLUGIN_ROOT/skills/pumasi-image/scripts/imagen-full.sh \
  "{intent}" "{mode}" "{aspect}" "{quality}" "{target_image_path}"

# 여러 장 일괄 (partial success + per-item retry manifest)
bash $PLUGIN_ROOT/skills/pumasi-image/scripts/imagen-batch.sh "{batch_json_path}"
```

> ⚠️ **샌드박스/승인 우회 경계 (opt-in).** 래퍼는 `codex exec --skip-git-repo-check
> --dangerously-bypass-approvals-and-sandbox`로 비대화형 실행한다 — 동작은 대상 이미지 경로 1개
> 쓰기로 한정된다. **신뢰하는 본인 프로젝트에서만** 사용한다.

### Step 7: 결과 확인 + 표시 (모드별)

생성 모드를 판정한 후 그에 맞게 동작한다. (PNG 1장 표시 = 약 1,400~3,000 비전 토큰이 cached prefix에 박히므로 기본값은 표시 안 함.)

#### 모드 판정 규칙
- **fast/no-show** (기본값): 검수/audit 키워드 없고, 모드가 텍스트 의존(E_THUMBNAIL/F_LOGO)도 아니고, 의도에 한글/영문 카피가 없을 때
- **review/show-one**: 모드가 `MODE_E_THUMBNAIL` / `MODE_F_LOGO` / 의도에 직접 인용된 카피(따옴표)가 있을 때 — 마지막 1장만 표시
- **audit/show-all**: 사용자가 "검수해줘", "전부 보여줘", "꼼꼼히 확인", "review all" 명시할 때 — 전체 표시

#### 동작
1. 파일 존재 확인 + `file {target_image_path}`로 해상도/포맷/sha1 확인
2. 모드별 분기:
   - **fast**: 경로만 안내 (`✅ 생성 완료: {path} ({해상도} PNG)` + "깨졌으면 '이미지 보여줘'라고 말씀해주세요"). 이미지 표시 안 함.
   - **review**: 위 안내 + 마지막 1장만 표시 (텍스트 렌더링 검수). 안내에 "[review 모드]" 추가.
   - **audit**: 위 안내 + 모든 이미지 표시. 안내에 "[audit 모드]" 추가.

### Step 8: MODE_REFINE 루프 (state 유지 + Step 4 재로드 금지)

생성 직후 다음을 대화 컨텍스트(skill state)로 유지:
- `last_prompt_path`: 마지막 영문 프롬프트 파일 경로 (Step 4 산출물)
- `last_image_path`: 마지막 PNG 경로
- 선택 파라미터 (mode / aspect / quality / 의도 답변 3개)

**리파인 판정**:
- **동일 이미지 리파인** ("색감 좀 바꿔줘", "더 밝게"):
  - Step 4 재로드 **금지** — `last_prompt_path` Read + 사용자 델타만 patch
  - 시각 컨텍스트 필요 시 `last_image_path` 표시 (자동 review 모드)
  - `image-studio-prompt.md`는 **절대 재로드 X** (28KB)
- **완전 새 요청**: Step 1부터 다시

---

## 운영 규칙 (토큰 효율)

1. **Step 7 기본값 fast** — 명시적 검수 요청이 없으면 PNG 표시 안 함 (비전 토큰이 cached prefix에 영구 누적되는 것 방지).
2. **MODE_REFINE 시 Step 4 재로드 금지** — `last_prompt_path` + 델타 patch만. `image-studio-prompt.md`는 절대 재로드 X.
3. **여러 장 일괄 생성** — 호출 사이 결과 보고를 묶어 처리 (라운드트립 감소).
4. **검수 분리 권장** — 5장 이상 생성 후 검수가 필요하면 별도 짧은 세션에서 audit 모드 사용.

---

## 기존 pumasi와의 분리

| 구분 | pumasi (코드) | pumasi-image (이미지) |
|------|---------------|---------------------|
| 스킬 디렉토리 | `skills/pumasi/` | `skills/pumasi-image/` |
| 자동 트리거 | "구현", "개발", "기능", "코드" | "이미지", "그림", "썸네일", "로고" |
| 백엔드 | Codex 워커 (멀티에이전트/`codex exec`) | Codex 네이티브 이미지 도구 |
| 작업 dir | `.pumasi/` | 없음 (단발 요청) |

두 스킬은 같은 플러그인 안의 독립 모듈이며 서로 간섭하지 않는다.

---

## References

- `references/image-studio-prompt.md` — 모드 분류 + Output Template 시스템 프롬프트
- `references/clarification-matrix.md` — 모드별 의도 파악 질문 매트릭스
- `references/keyword-mapping.md` — 비율·퀄리티 키워드 자동 매핑 + 자연어 힌트 변환표

## Scripts (선택 — codex exec 위임 경로)

- `scripts/extract_image.py` — `codex exec --json` 출력(또는 세션 rollout)의 `image_generation_call`
  base64를 구조 검증 후 타깃 PNG로 디코딩 저장
- `scripts/imagen.sh` — feature flag 확인·활성화 + `codex exec --json` 호출 + base64 추출·저장 + SHA1/해상도 검증
- `scripts/imagen-full.sh` — 영문 프롬프트 작성까지 codex에 위임(manifest/prompt/log 보존)
- `scripts/imagen-batch.sh` — 여러 장 일괄(partial success + per-item retry manifest)
- `scripts/imagen-cleanup.sh` — `~/.codex/generated_images/` 누적 정리(기본 DRY-RUN, 디스크 위생용)
- `scripts/test-imagen-capture.sh` — base64 캡처/실패 처리 회귀 테스트(codex mock)

## 사전 조건

- Codex CLI 설치 + 로그인 완료
- 네이티브 이미지 생성 도구(`/imagen`, gpt-image-2) 사용 가능
