---
name: pumasi-image
description: Image-generation companion skill for the pumasi plugin family. Use when the user asks for an image, thumbnail, poster, logo, illustration, banner, profile image, cover, icon, or any visual artifact — including casual phrasing like "그림 하나 뽑아줘", "비주얼 만들어줘", and Codex-named requests like "코덱스로 이미지 만들어줘"; this skill owns every image request. In Codex it maps to the native image generation/editing tool (gpt-image-2), with an optional Grok image_gen backend through the bundled scripts. Korean triggers — "이미지 만들어줘", "그림 생성해줘", "썸네일 만들어", "로고 만들어줘", "일러스트 그려줘", "포스터 만들어", "배너 만들어", "아이콘 만들어", "표지 이미지". English triggers — "create image", "make thumbnail", "make logo", "make illustration", "draw image". DO NOT trigger on code-generation requests like "함수/컴포넌트/페이지/배너 컴포넌트 만들어줘" — those go to the pumasi skill.
---

# /pumasi-image — Codex 이미지 생성

> Codex의 네이티브 이미지 생성/편집 도구(`image_gen`, gpt-image-2)로 이미지를 만든다.
> 코드 병렬 외주(pumasi)와 완전히 분리된 독립 스킬.
> **이미지 요청은 사용자가 "코덱스로"라고 말해도 전부 이 스킬이 담당한다** — pumasi로 넘기지 않는다.

## 먼저 읽을 것

- `references/clarification-matrix.md` — 모드별 의도 파악 질문 매트릭스
- `references/keyword-mapping.md` — 비율·퀄리티 키워드 자동 매핑 + 자연어 힌트 변환표
- `references/image-studio-prompt.md` — 모드 분류 + Output Template 시스템 프롬프트 (영문 프롬프트 작성 직전에만 Read)

---

## 핵심 원칙

1. **백엔드는 2종 — Codex 네이티브 이미지 도구(기본)·Grok `image_gen`(선택)** — nanobanana 등 다른 백엔드 사용 안 함. 백엔드는 Step 3에서 사용자가 고른다(입력에 지명이 있으면 스킵). Grok을 쓸 때는 반드시 `scripts/imagen.sh`(`--backend grok`)를 경유한다(비율 강제·확장자 정합·실패 사유 표면화가 그 안에 있다). `grok`을 직접 부르지 말 것.
2. **API 키를 꺼내 직접 호출하지 않는다** — 볼트·환경변수·설정 파일에서 OpenAI(또는 xAI) API 키를 읽어 `api.openai.com` 등 이미지 API 엔드포인트를 직접 부르는 행동은 **금지**. 이미지는 오직 (a) Codex 네이티브 이미지 도구 또는 (b) `scripts/`의 codex/grok 백엔드로만 만든다. 구독 세션이 인증을 담당하며, 이 스킬은 어떤 키도 만들거나 복사하지 않는다.
3. **image-studio 시스템 프롬프트 내면화** — 모드 분류 + Output Template 작성
4. **후처리 절대 금지** — sips/ImageMagick/재인코딩 금지, 생성 원본 그대로 저장(SHA1 유지)
5. **저장 경로 고정** — `{BASE_DIR}/images/{YYYY-MM-DD}/{slug}-{seq}.png`
6. **최대 5개 질문** — 기술 2개 + 의도 3개, 조건부 스킵
7. **텍스트는 이미지 도구가 직접 렌더링한다** — 썸네일·포스터·로고의 한글/영문 카피는 프롬프트의 Text Integration 섹션에 따옴표로 묶어 그대로 명시. **HTML/CSS 분리·후합성·텍스트 레이어 분할 절대 금지.** 구세대 diffusion(SD/Midjourney) 가정으로 "텍스트 못 그림"이라고 회피하지 말 것 — 다음 §의 capability snapshot 참조.

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

### Grok image_gen 차이 (선택 백엔드)
- 비율은 **9:16 / 16:9 / 1:1만** 지원 — 그 외를 주면 스크립트가 1:1로 강제하고 경고한다
- 퀄리티 파라미터 없음 (퀄리티 질문 스킵)
- 산출물이 보통 **JPEG** — 스크립트가 타깃 확장자를 소스에 맞춰 자동 조정하고 최종 경로를 `path:`로 보고한다
- 텍스트 렌더 품질은 gpt-image-2 대비 미검증. SuperGrok 구독이면 한계비용 0

### 운영 룰
1. **1차는 무조건 이미지 도구로 직접 렌더** — 텍스트 포함 여부 무관
2. **결과 검수** — 이미지 표시 후 텍스트 정확도 사용자 확인 (Step 7 모드 참조)
3. **재시도 우선** — 첫 결과가 깨졌으면 프롬프트 보강(폰트 명시, 크기 명시)해서 1-2회 재생성
4. **합성 옵션은 사용자 명시 거부 후** — "직접 렌더 결과 마음에 안 들어, 합성으로 가자"는 사용자 발화가 있을 때만 후합성 워크플로우 제안

---

## 워크플로우

### Step 0: feature flag 확인 (scripts 경로를 쓸 때만)

네이티브 도구를 직접 쓰면 이 단계는 없다. `scripts/imagen.sh` 위임 경로를 쓸 때는 스크립트가 `codex features list`로 `image_generation` 플래그를 확인하고 꺼져 있으면 `codex features enable image_generation`으로 켠다 — 사용자에게는 조용히 수행한다고만 짧게 알린다.

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

### Step 3: 사용자 질문 (§A 질문 도구 1콜, 최대 5개)

결정이 꼭 필요하면 `$PLUGIN_ROOT/shared/questioning-policy.md §A`의 **질문 도구**(`request_user_input_async`, Plan 모드면 `request_user_input`)로 묻는다.
`request_user_input_async`는 호출 후 한 줄 안내만 쓰고 턴을 끝내며, 답은 다음 메시지로 받는다. 두 도구가 모두 없을 때만 **채팅 번호형 선택지 블록**(폴백)으로 묻는다.

async 호출 형식: `{"questions":[{"title":"헤더 — 질문","options":["추천안 (추천) — 설명","대안 — 설명"]}]}`. 문항에는 `title`·`options`(문자열 배열)만 넣는다. `question`·`header`·`id`는 Plan 모드 `request_user_input` 전용이라 async에 넣으면 파싱 오류가 난다. "기타·직접 적기" 선택지는 넣지 않는다(자유 입력 칸이 자동으로 붙는다).

`references/clarification-matrix.md`를 Read하여 모드별 의도 파악 카테고리 3개를 확정한다.

**질문 순서** (한 턴 최대 4문항 — 초과분은 우선순위 낮은 의도 질문부터 잘라낸다):
0. **백엔드** (입력에 "그록으로"/"grok"/"코덱스로"/"codex" 지명이 있으면 스킵)
   번호 블록 폴백일 때의 모양:
   ```text
   질문: 어떤 백엔드로 생성할까요?
   1. Codex gpt-image-2 (권장) — 임의 비율, 한글/영문 텍스트 렌더 강함
   2. Grok image_gen — SuperGrok 구독 시 한계비용 0. 단 비율 9:16/16:9/1:1만, 텍스트 렌더 미검증
   3. 문장으로 직접 알려주기
   ```
1. 비율 (Step 2에서 확정됐으면 스킵. **Grok 선택 시 선택지를 9:16/16:9/1:1로 제한**)
2. 퀄리티 (Step 2에서 확정됐으면 스킵. Grok에는 퀄리티 파라미터가 없으므로 Grok 선택 시 스킵)
3~5. 의도 파악 3개 (모드 매트릭스 기반)

**질문 원칙**:
- §1 + §2c: 이미 입력에서 확정된 차원은 **묻지 않는다**. 요청이 구체적이면 질문 없이 바로 생성한다(과잉 질문 = 마찰 실패).
- 물을 때는 §A 질문 도구로 — 각 슬롯당 5개 이상 선택지, 그중 1~2개는 창의적 대안(★). `request_user_input_async`는 선택지가 자유 문자열이라 5개 이상도 되고, 자유 입력이 자동 추가되므로 "문장으로 직접 알려주기"는 넣지 않는다. Plan 모드 `request_user_input`은 선택지 2~3개 제한이라 추천안 먼저 상위 3개만 남긴다. 도구가 없을 때만 번호 블록 폴백을 쓰고, 이때 마지막에 "문장으로 직접 알려주기"(Other 대체)를 둔다.
- "자동 추천(AI 판단)" 안전망 선택지를 항상 포함하고, "모르면 1번(자동 추천)으로 진행하겠습니다"로 안내한다.
- 여러 슬롯을 한 번에 물을 때는 도구 1콜에 묶는다(Plan 모드는 3문항씩). 폴백이면 각 질문 블록을 이어서 출력하고 "여러 개면 1,3처럼 적어주세요"로 안내. 질문 도구가 있는데 번호 블록으로 때우지 말 것.

번호 블록 폴백일 때의 모양 (단일 슬롯):
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
5. **Format / Medium Guard** — 단일 심볼 컨셉(돋보기·로켓·방패 등)을 사용자가 로고/아이콘을 요청하지 않았는데 앱아이콘·글래스 배지로 만들지 않는다. hero/배너/커버/씬은 프레임을 가득 채우는 full-bleed 장면으로 번역한다 (image-studio-prompt.md의 가드 참조)

프롬프트를 다음 경로에 저장 (없으면 `mkdir -p`):
```
{BASE_DIR}/.imagen/prompt-{timestamp}.md
```

### Step 4-bis (선택, feature flag 뒤): 영문 프롬프트 작성을 codex 워커에 위임

환경변수 `PUMASI_IMAGE_DELEGATE_PROMPT=1` 설정 시:

1. Step 4의 image-studio-prompt.md Read + 영문 프롬프트 작성 단계 **스킵**
2. Step 6에서 `scripts/imagen-full.sh` 호출 — 의도 한 줄 + mode + aspect + quality + 타깃 경로(+ 선택 ref 이미지)만 전달
3. 영문 프롬프트 작성은 codex 워커 측에서 수행하고 prompt.md + manifest.json + codex.log를 `{타깃디렉토리}/.imagen-full/`에 저장 (refine 복구용)
4. **자동 fallback**: imagen-full.sh가 exit ≠ 0이면 즉시 Step 4(직접 작성) + 기본 경로로 폴백. 사용자에게는 "위임 경로 실패 → 직접 작성 경로로 전환" 한 줄 안내. codex 백엔드 전용(Grok에는 없음).

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
확장자는 `.png`. Grok 백엔드는 산출물이 보통 JPEG라 스크립트가 확장자를 맞춰 조정하므로 **결과 보고는 스크립트 출력의 `path:`를 기준**으로 한다.

### Step 6: 이미지 생성 호출

**기본 경로 — Codex 네이티브 이미지 도구를 직접 호출한다.**

- 백그라운드 CLI 세션을 띄우지 않는다.
- Step 4의 영문 프롬프트 + Step 5의 타깃 경로를 도구에 전달한다.
- 프롬프트 끝에 후처리 금지 가드(원본 유지, 재인코딩 금지)를 명시한다.
- 텍스트가 깨졌으면 합성하지 말고 프롬프트를 보강해 1~2회 재생성한다(운영 룰 3).
- 도구가 돌려준 이미지를 **이번 호출 산출물만** Step 5의 타깃 경로에 저장한다. 생성이 0장이면 거짓 성공을 보고하지 말고 실패로 처리한다.

**스타일 앵커(레퍼런스)**: 여러 장을 같은 스타일로 뽑을 때는 1장을 먼저 생성·승인받고, 나머지를 전부 그 파일을 레퍼런스로 물려 편집 도구로 생성한다(앵커 우선 패턴). 레퍼런스가 있으면 프롬프트에서 스타일 서술을 걷어내고 "첨부 이미지의 스타일·조명·색감 유지" + 피사체·구도 델타만 쓴다 — 레퍼런스가 이미 묶은 것을 긴 산문으로 재서술하면 둘이 싸운다. 스타일 일관성 수단 서열(1차 출처 리서치 2026-08-22): 레퍼런스 이미지 ≫ 텍스트 재사용 ≫ seed(어느 벤더도 프롬프트가 달라진 뒤의 재현을 보장하지 않음).

#### 위임 경로 (선택) — scripts 사용

별도 `codex exec` 워커에 생성을 위임하거나(호스트 컨텍스트 절약), **Grok 백엔드**를 쓰거나, 영문 프롬프트 작성까지 위임하려면 `scripts/`의 결정적 래퍼를 쓴다:

```bash
# 영문 프롬프트는 호스트가 작성, 생성만 위임 (3번째 인자 비율은 실측 비교 경고용, --ref 반복 가능)
bash $PLUGIN_ROOT/skills/pumasi-image/scripts/imagen.sh \
  "{prompt_file_path}" "{target_image_path}" "{aspect e.g. 16:9 — 생략 가능}" \
  --backend "{codex|grok — Step 3 선택 결과, 생략 시 codex}" \
  --ref "{anchor_image_path — 생략 가능}"

# 영문 프롬프트 작성까지 codex 워커에 위임 (PUMASI_IMAGE_DELEGATE_PROMPT 경로)
bash $PLUGIN_ROOT/skills/pumasi-image/scripts/imagen-full.sh \
  "{intent}" "{mode}" "{aspect}" "{quality}" "{target_image_path}" "{ref_image — 생략 가능}"

# 여러 장 일괄 (partial success + per-item retry manifest; 항목에 "ref" 키로 앵커 지정 가능)
bash $PLUGIN_ROOT/skills/pumasi-image/scripts/imagen-batch.sh "{batch_json_path}"
```

`--backend grok`: `grok` 헤드리스 `image_gen`으로 생성한다(`--ref`를 주면 `image_edit`). 사전 조건: grok CLI 설치(`$HOME/.grok/bin/grok`) + `grok login`. 미설치/미로그인이면 스크립트가 exit 3으로 실패하니 사용자에게 알리고 codex 재생성 여부를 §A 질문 도구(없으면 번호 블록)로 확인한다.

래퍼 내부 동작(codex 백엔드):
1. `codex features list`로 image_generation feature flag 재확인 (안전망)
2. `codex exec --json … < /dev/null` 호출 — codex가 이미지 도구로 1장 생성. `< /dev/null`은 exec가 stdin EOF를 무한 대기(헤드리스 행)하는 것을 막는다. 레퍼런스는 `--image=<path>`(파일당 1개)로 전달 — `-i FILE...`은 가변 인자라 뒤따르는 프롬프트를 이미지 경로로 삼켜 "No prompt provided" 실패를 만든다(실측 2026-08-22).
3. **회수 계약 (codex-cli 0.147+ 실측)**: `codex exec`는 이미지를 `~/.codex/generated_images/<thread_id>/exec-*.png`로 **저장**하고 stdout JSONL에는 base64를 싣지 않는다. 래퍼는 stdout의 `thread.started.thread_id`(디렉토리명과 1:1)로 **이 세션 산출물만** 집어 타깃에 복사한다(동시 실행과 경합 없음, 스테일 오집음 없음). 구버전 codex 호환용으로 stdout(JSONL)·세션 rollout의 base64 디코딩 폴백(`extract_image.py`)을 유지한다. 생성 0장이면 거짓 성공 없이 exit 5.
4. 실측 해상도(`sips`) + 요청 비율과 15%↑ 괴리 시 경고. 후처리는 절대 하지 않음.
5. **프록시 우회** — 로컬 프록시(`HTTP_PROXY`/`HTTPS_PROXY`)가 환경에 상속돼 있으면 codex 호출에서만 벗긴다. 프록시를 경유하면 이미지 엔드포인트 요청이 ~153초 뒤 `network error`로 죽는다(2026-07-23 실측: 경유 89/89 실패, 우회 시 동일 프롬프트 44초 성공). 해제는 `PUMASI_IMAGE_KEEP_PROXY=1`.
6. **실패 사유 표면화** — codex가 남긴 `image generation failed: …` 원문을 `REASON:`으로 출력하고, network error면 프록시 힌트를 덧붙인다. 네트워크 실패와 정책 거부를 구분해 보고한다.

> ⚠️ **샌드박스/승인 우회 경계 (opt-in).** 래퍼는 `codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox`로
> 비대화형 실행한다 — 동작은 대상 이미지 경로 1개 쓰기로 한정된다. **신뢰하는 본인 프로젝트에서만** 사용한다.

### Step 7: 결과 확인 + 표시 (모드별)

생성 모드를 판정한 후 그에 맞게 동작한다. (PNG 1장 표시 = 약 1,400~3,000 비전 토큰이 cached prefix에 박히므로 기본값은 표시 안 함.)

#### 모드 판정 규칙
- **fast/no-show** (기본값): 검수/audit 키워드 없고, 모드가 텍스트 의존(E_THUMBNAIL/F_LOGO)도 아니고, 의도에 한글/영문 카피가 없을 때
- **review/show-one**: 모드가 `MODE_E_THUMBNAIL` / `MODE_F_LOGO` / 의도에 직접 인용된 카피(따옴표)가 있을 때 — 마지막 1장만 표시
- **audit/show-all**: 사용자가 "검수해줘", "전부 보여줘", "꼼꼼히 확인", "review all" 명시할 때 — 전체 표시

#### 동작
1. 파일 존재 확인 + `file {target_image_path}`로 해상도/포맷/sha1 확인 (스크립트 경로면 출력의 `path:` 기준)
2. 모드별 분기:
   - **fast**: 경로만 안내 (`✅ 생성 완료: {path} ({해상도} {포맷}, sha1: {prefix})` + "깨졌으면 '이미지 보여줘'라고 말씀해주세요"). 이미지 표시 안 함.
   - **review**: 위 안내 + 마지막 1장만 표시 (텍스트 렌더링 검수). 안내에 "[review 모드]" 추가.
   - **audit**: 위 안내 + 모든 이미지 표시. 안내에 "[audit 모드]" 추가.

### Step 8: MODE_REFINE 루프 (state 유지 + Step 4 재로드 금지)

생성 직후 다음을 대화 컨텍스트(skill state)로 유지:
- `last_prompt_path`: 마지막 영문 프롬프트 파일 경로 (Step 4 산출물)
- `last_image_path`: 마지막 이미지 경로 (앵커 후보)
- `last_manifest_path`: 마지막 manifest.json 경로 (imagen-full.sh 사용 시)
- 선택 파라미터 (backend / mode / aspect / quality / 의도 답변 3개)

**리파인 판정**:
- **동일 이미지 리파인** ("색감 좀 바꿔줘", "더 밝게"):
  - Step 4 재로드 **금지** — `last_prompt_path` Read + 사용자 델타만 patch
  - 시각 컨텍스트 필요 시 `last_image_path` 표시 (자동 review 모드)
  - 영문 프롬프트 재작성 필요 시 직전 호출 경로(네이티브 / imagen.sh / imagen-full.sh)와 백엔드 유지
  - `image-studio-prompt.md`는 **절대 재로드 X** (28KB)
- **완전 새 요청**: Step 1부터 다시

---

## 운영 규칙 (토큰 효율)

1. **Step 7 기본값 fast** — 명시적 검수 요청이 없으면 PNG 표시 안 함 (비전 토큰이 cached prefix에 영구 누적되는 것 방지).
2. **MODE_REFINE 시 Step 4 재로드 금지** — `last_prompt_path` + 델타 patch만. `image-studio-prompt.md`는 절대 재로드 X.
3. **여러 장 일괄 생성** — imagen-batch.sh 가용하면 사용, 아니면 호출 사이 결과 보고를 묶어 처리 (라운드트립 감소).
4. **검수 분리 권장** — 5장 이상 생성 후 검수가 필요하면 별도 짧은 세션에서 audit 모드 사용.
5. **A+B 동시 기본값 금지** — `PUMASI_IMAGE_DELEGATE_PROMPT=1`은 feature flag로만 활성화. Step 7 fast 모드와 동시 적용 시 MODE_REFINE 컨텍스트 부서짐 위험.

---

## 기존 pumasi와의 분리

| 구분 | pumasi (코드) | pumasi-image (이미지) |
|------|---------------|---------------------|
| 스킬 디렉토리 | `skills/pumasi/` | `skills/pumasi-image/` |
| 자동 트리거 | "구현", "개발", "기능", "코드" | "이미지", "그림", "썸네일", "로고" (Codex 지명 포함) |
| 백엔드 | CLI 워커 (Codex 멀티에이전트/`codex exec`/grok/cursor…) | Codex 네이티브 이미지 도구 (+ 선택 Grok image_gen) |
| 작업 dir | `.pumasi/` | 없음 (단발 요청) |

두 스킬은 같은 플러그인 안의 독립 모듈이며 서로 간섭하지 않는다.

---

## References

- `references/image-studio-prompt.md` — 모드 분류 + Output Template 시스템 프롬프트 (Format/Medium Guard 포함)
- `references/clarification-matrix.md` — 모드별 의도 파악 질문 매트릭스
- `references/keyword-mapping.md` — 비율·퀄리티 키워드 자동 매핑 + 자연어 힌트 변환표

## Scripts (선택 — 위임 경로 / Grok 백엔드)

- `scripts/imagen.sh` — feature flag 확인·활성화 + `codex exec --json` 호출(또는 `--backend grok`) + thread_id 기반 산출물 회수(+base64 폴백) + 프록시 우회 + 실패 사유 표면화 + `--ref` 스타일 앵커 + SHA1/해상도 검증
- `scripts/imagen-full.sh` — 영문 프롬프트 작성까지 codex 워커에 위임(manifest/prompt/log 보존). 프록시 우회·실패 사유 표면화 동일 적용
- `scripts/imagen-batch.sh` — 여러 장 일괄(partial success + per-item retry manifest, 항목별 `ref`)
- `scripts/imagen-cleanup.sh` — `~/.codex/generated_images/` 누적 정리(기본 DRY-RUN, `--apply` 시 trash)
- `scripts/extract_image.py` — 구버전 codex 호환: JSONL/세션 rollout의 `image_generation_call` base64를 구조 검증 후 PNG로 저장
- `scripts/test-imagen-capture.sh` — 회수 계약 회귀 테스트(mock codex/grok, 32 assertions)

## 사전 조건

- Codex CLI 설치 + 로그인 완료, 네이티브 이미지 생성 도구(gpt-image-2) 사용 가능
- (scripts 경로) `codex features` 서브커맨드 사용 가능
- (Grok 백엔드 선택 시) grok CLI 설치(`$HOME/.grok/bin/grok`) + `grok login` (구독 세션, `XAI_API_KEY` 불필요)
