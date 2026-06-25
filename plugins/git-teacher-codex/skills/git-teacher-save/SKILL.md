---
name: git-teacher-save
description: Commits changed files to Git, explained in plain language for non-developers. Runs `git add -A` + `git commit` and describes what was saved. Korean triggers — "저장해줘", "커밋", "커밋해줘", "변경 내용 저장", "지금까지 한 거 저장", "세이브". English triggers — "save", "commit", "save my work".
---

# 저장하기 — Phase 3 (바르다 깃선생 — Codex)

변경된 파일을 Commit (저장)한다. `git add -A` + `git commit`을 실행하고, 사후에 무엇을 했는지 설명한다.

> 설명·교육 시 `git-teacher-help`의 §교육 원칙(`shared/questioning-policy.md` §3 Teaching)을 따른다. "Commit하면 GitHub에 올라간다"는 오개념은 비유+질문으로 교정한다(§2a). 사용자가 그냥 저장만 빨리 원하면 강의하지 않는다(§2c).
> Codex CLI에는 `question prompt` 카드 UI가 없다. 결정이 필요한 곳은 `shared/questioning-policy.md` §A의 **채팅 번호형 선택지 블록**으로 묻는다.

## 실행 순서

### Step 1: 병렬 상태 수집

다음 명령을 **병렬로(가능한 한 함께)** 실행한다:

```bash
git rev-parse --is-inside-work-tree    # .git 존재 확인
git symbolic-ref --short HEAD          # 현재 branch
git status --porcelain                 # 변경 파일 목록
git diff --stat                        # 변경 통계
ls .gitignore 2>/dev/null              # .gitignore 존재 여부
```

### Step 2: 안전 검사

1. **`.git` 없음**: "여기는 Git 프로젝트 폴더가 아니에요. '깃 시작해줘'로 먼저 설정하세요." → 중단
2. **Detached HEAD**: "안전한 위치에서 벗어났어요." → `git checkout main` 실행 후 재시도
3. **Merge Conflict** (`UU`, `AA` 등): 충돌 파일 목록을 보여주고, 채팅 번호형 선택지로 묻는다 (`shared/questioning-policy.md` §A):
   ```text
   충돌이 있어서 바로 저장할 수 없어요. 두 사람이 같은 부분을 동시에 고쳤거든요.
   충돌 파일: {파일 목록}

   질문: 어떻게 할까요?
   1. 내가 수정한 걸로 유지 — 내 변경 내용을 사용해요
   2. 상대방이 수정한 걸로 유지 — 상대방의 변경 내용을 사용해요
   3. 문장으로 직접 수정 요청
   ```
   선택에 따라:
   - "내가 수정한 걸로 유지": `git checkout --ours {파일}` → `git add {파일}`
   - "상대방이 수정한 걸로 유지": `git checkout --theirs {파일}` → `git add {파일}`
   충돌 해결 후 자동으로 저장(commit) 단계로 진행한다.
4. **변경 사항 없음**: "저장할 변경 사항이 없어요. 파일을 수정한 뒤 다시 시도하세요." → 중단

### Step 3: .gitignore 자동 생성

`.gitignore`가 없으면 프로젝트 타입을 감지하여 기본 `.gitignore`를 생성한다:

- Node.js (`package.json` 존재) → `node_modules/`, `.env`, `dist/` 등
- Python (`requirements.txt` 또는 `pyproject.toml` 존재) → `__pycache__/`, `.env`, `venv/` 등
- 일반 → `.env`, `.DS_Store`, `*.log`, `thumbs.db` 등

생성 후 안내: "보안을 위해 .gitignore 파일을 만들었어요. 비밀번호나 임시 파일은 자동으로 제외됩니다."

### Step 4: 변경 파일 안내 + 커밋 메시지 요청

변경된 파일 목록을 보여준 뒤 커밋 메시지를 물어본다.

`git status --porcelain` 결과로 파일 목록을 **동적 생성**하여 먼저 보여주고, 채팅 번호형 선택지로 묻는다 (`shared/questioning-policy.md` §A):

```text
변경된 파일 N개:
  - file1 (수정됨)
  - file2 (새 파일)

질문: 뭘 바꿨는지 한 줄로 적어주세요.
1. 직접 입력 — 한 줄로 알려주세요 (예: "로고 변경", "메인 페이지 수정")
2. 자동 생성 — 변경 내용을 분석해서 메시지를 자동으로 만들어요
3. 문장으로 직접 수정 요청
```

**사용자가 빈 값이나 애매한 답을 주면**: 변경 내용(diff)을 분석하여 짧은 자연어 메시지를 자동 생성한다.

### Step 5: 저장 실행

```bash
git add -A
git commit -m "사용자가 입력한 메시지"
```

커밋 메시지 규칙:
- 사용자가 입력한 자연어 그대로 사용 (conventional commits 강제하지 않음)
- 한국어/영어 모두 허용
- 예: "로고 변경", "메인 페이지 수정", "오타 고침"

### Step 6: 영수증 출력

실행 후 결과를 알려준다:

```
저장 완료! 파일 3개를 포장해서 '로고 변경'이라고 기록했어요.

아직 내 컴퓨터에만 있어요.
GitHub 클라우드에도 올리려면 "올려줘"라고 하세요.
```

## 핵심 강조사항

- 저장 후 **매번** "아직 내 컴퓨터에만 있어요" 리마인드
- Commit과 Push의 차이를 체감하게 함 — 겁먹은 초보면 "방금 저장한 건 어디에 있는 걸까요?"로 한 번 더 확인(§2a)
- 다음 행동(Push)을 안내

## Safety

- `git reset --hard` 같은 파괴적 명령은 절대 실행하지 않는다.
- 사용자가 명시적으로 요청하지 않으면 히스토리를 재작성하지 않는다.
- 사용자의 무관한 변경 내용은 그대로 보존한다.
