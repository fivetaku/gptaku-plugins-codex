---
name: git-teacher-upload
description: Pushes committed work to GitHub cloud, returning the GitHub URL on success. For non-developers. Korean triggers — "올려줘", "푸시", "업로드", "GitHub에 올려줘", "클라우드에 보내줘", "올리기". English triggers — "push", "upload", "push to GitHub".
---

# 올리기 — Phase 4 (바르다 깃선생 — Codex)

저장(Commit)한 내용을 GitHub 클라우드에 올린다(Push). 성공 시 GitHub URL을 제공한다.

> 설명·교육 시 `git-teacher-help`의 §교육 원칙(`shared/questioning-policy.md` §3 Teaching)을 따른다. "Push가 뭔지" 헷갈려하는 초보면 "저장(Commit)이랑 뭐가 다를까요?"로 비유+질문 교정(§2a). 그냥 올리기만 원하면 강의하지 않는다(§2c).
> Codex CLI에는 `question prompt` 카드 UI가 없다. 결정이 필요한 곳은 `shared/questioning-policy.md` §A의 **채팅 번호형 선택지 블록**으로 묻는다.

## 실행 순서

### Step 1: 병렬 상태 수집

다음 명령을 **병렬로(가능한 한 함께)** 실행한다:

```bash
git rev-parse --is-inside-work-tree    # .git 존재 확인
git symbolic-ref --short HEAD          # 현재 branch
git status --porcelain                 # 미저장 변경 확인
git rev-list --count @{u}..HEAD 2>/dev/null || echo "no-upstream"  # 올리지 않은 commit 수
git remote get-url origin 2>/dev/null  # 원격 저장소 URL
```

### Step 2: 안전 검사

1. **`.git` 없음**: "여기는 Git 프로젝트 폴더가 아니에요." → 중단
2. **Detached HEAD**: 자동 복구 후 재시도
3. **원격 저장소 없음**: "GitHub에 연결되어 있지 않아요. '깃 시작해줘'로 먼저 설정하세요." → 중단
4. **저장하지 않은 변경 있음**: "아직 저장(Commit)하지 않은 변경 사항이 있어요. 먼저 '저장해줘'로 저장하세요." → 중단
5. **올릴 게 없음** (HEAD와 upstream이 동일): "이미 모든 내용이 GitHub에 올라가 있어요." → 중단

### Step 3: Push 실행

```bash
git push origin HEAD
```

### Step 4: 영수증 출력

#### 성공 시

GitHub URL을 구성하여 안내한다:

```
업로드 완료!

GitHub에서 확인: https://github.com/username/my-project
저장한 내용 2개가 클라우드에 올라갔어요.

이제 다른 사람도 이 내용을 볼 수 있어요.
```

GitHub URL은 `git remote get-url origin` 결과에서 추출한다. SSH URL인 경우 HTTPS URL로 변환한다:
- `git@github.com:user/repo.git` → `https://github.com/user/repo`

#### 실패 시

```
업로드에 실패했어요.
```

흔한 실패 원인별 안내:
- **rejected (non-fast-forward)**: "다른 사람이 먼저 올린 내용이 있어요. 최신 내용을 먼저 받아올게요." → 작업 트리가 깨끗할 때만, 현재 branch 이름을 감지하여 `git pull --rebase origin {현재 branch}` 자동 실행 시도. 성공 시 다시 push.
- **permission denied**: "GitHub 접근 권한이 없어요. '깃 시작해줘'로 다시 로그인해보세요."
- **remote not found**: "GitHub 연결이 끊어졌어요. '깃 시작해줘'로 다시 설정하세요."

### Pull 후 충돌 발생 시

`git pull --rebase` 후 충돌이 발생하면 충돌 파일 목록을 보여주고, 채팅 번호형 선택지로 묻는다 (`shared/questioning-policy.md` §A):

```text
클라우드의 최신 내용을 받아오다가 충돌이 생겼어요. 두 사람이 같은 부분을 동시에 고쳤거든요.
충돌 파일: {파일 목록}

질문: 어떻게 할까요?
1. 내가 수정한 걸로 유지 — 내 변경 내용을 사용해요
2. 상대방이 수정한 걸로 유지 — 상대방의 변경 내용을 사용해요
3. 문장으로 직접 수정 요청
```

선택에 따라:

> ⚠️ **rebase에서는 `ours`/`theirs`가 merge와 반대다.** `git pull --rebase`는 상대방(upstream) 위에 내 커밋을 재적용하므로, 충돌 시 `--ours`=상대방(upstream) 쪽, `--theirs`=재적용 중인 **내 커밋**이다. 아래 매핑을 절대 바꾸지 말 것.

- "내 거 유지": `git checkout --theirs {파일}` → `git add {파일}` → `git rebase --continue`
- "상대방 거 유지": `git checkout --ours {파일}` → `git add {파일}` → `git rebase --continue`

충돌 해결 후 자동으로 push를 재시도한다.

## 다음 행동 안내

- 성공 시: "팀원에게 검토를 요청하려면 '검토 요청해줘'라고 하세요."
- 실패 시: 원인별 해결 방법 제시

## Safety

- `git reset --hard` 같은 파괴적 명령은 실행하지 않는다.
- 사용자가 명시적으로 요청하지 않으면 이미 commit된 히스토리를 재작성하지 않는다.
- `git pull --rebase`는 작업 트리가 깨끗할 때만 시도한다.
