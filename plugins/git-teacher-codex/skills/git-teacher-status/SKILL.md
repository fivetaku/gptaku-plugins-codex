---
name: git-teacher-status
description: Translates current Git status into plain-language explanations for non-developers. Korean triggers — "상태 확인", "지금 어떤 상태?", "뭐가 바뀌었어?", "git status", "변경 사항", "뭐가 달라졌어?", "파일 확인". English triggers — "check status", "what changed", "git status".
---

# 상태 확인 (바르다 깃선생 — Codex)

`git status`와 관련 명령의 결과를 비개발자가 이해할 수 있는 한국어 자연어로 번역한다.

> 설명·교육 시 `git-teacher-help`의 §교육 원칙(`shared/questioning-policy.md` §3 Teaching)을 따른다. 상태가 헷갈리는 초보에게는 비유로 안심시키며 천천히 짚어준다(§2a). 사용자가 그냥 결과만 빨리 원하면 핵심만 번역해서 준다(§2c).
> Codex CLI에는 `question prompt` 카드 UI가 없다. 결정이 필요한 곳은 `shared/questioning-policy.md` §A의 **채팅 번호형 선택지 블록**으로 묻는다.

## 실행 순서

### Step 1: 병렬 상태 수집

다음 명령을 **병렬로(가능한 한 함께)** 실행한다:

```bash
git rev-parse --is-inside-work-tree    # .git 존재 확인
git symbolic-ref --short HEAD          # 현재 branch (detached HEAD 감지)
git status --porcelain                 # 변경 파일 목록
git log --oneline -3                   # 최근 저장 기록 3개
git remote -v                          # 원격 연결 상태
git stash list                         # 임시 저장(stash) 확인
```

### Step 2: 안전 검사

우선순위 순서로 검사하고, 문제 발견 시 즉시 안내 후 중단:

1. **`.git` 없음**: "여기는 Git 프로젝트 폴더가 아니에요. '깃 시작해줘'로 먼저 설정하세요." → 중단
2. **Detached HEAD**: "안전한 위치에서 벗어났어요. 자동으로 돌아갈게요." → 대상 브랜치(`main` 또는 `master`)가 **존재할 때만** `git checkout main` (또는 `master`) 실행
3. **Merge Conflict** (`UU`, `AA` 등): 충돌 파일 목록을 보여주고, 채팅 번호형 선택지로 해결 방법을 묻는다 (`shared/questioning-policy.md` §A):
   ```text
   두 사람이 같은 파일의 같은 부분을 동시에 고쳐서 충돌이 생겼어요.
   충돌 파일: {파일 목록}

   질문: 어떻게 할까요?
   1. 내가 수정한 걸로 유지 — 내 변경 내용을 사용해요
   2. 상대방이 수정한 걸로 유지 — 상대방의 변경 내용을 사용해요
   3. 문장으로 직접 수정 요청
   ```
   선택에 따라:
   - "내 거 유지": `git checkout --ours {파일}` → `git add {파일}`
   - "상대방 거 유지": `git checkout --theirs {파일}` → `git add {파일}`
   충돌 해결 후 "저장해줘"로 다음 단계를 안내한다.

### Step 3: 상태 번역

`git status --porcelain` 결과를 자연어로 번역한다:

| Porcelain 코드 | 자연어 번역 |
|---|---|
| `M` (modified) | 수정됨 |
| `A` (added) | 새로 추가됨 |
| `D` (deleted) | 삭제됨 |
| `R` (renamed) | 이름 바뀜 |
| `??` (untracked) | 새 파일 (아직 Git이 모르는 파일) |

### Step 4: 결과 출력

상황별 출력 형식:

#### 변경 사항이 있을 때
```
현재 상태:

변경된 파일 3개:
  - index.html (수정됨)
  - style.css (새 파일)
  - old-logo.png (삭제됨)

아직 저장(Commit)하지 않은 상태예요.
저장하려면 "저장해줘"라고 하세요.
```

#### 저장은 했지만 올리지 않았을 때
```
현재 상태:

저장(Commit)은 되어 있지만, 아직 내 컴퓨터에만 있어요.
GitHub에 올리지 않은 저장이 2개 있어요:
  - "로고 변경" (10분 전)
  - "메인 페이지 수정" (30분 전)

클라우드에 올리려면 "올려줘"라고 하세요.
```

#### 모든 게 깨끗할 때
```
현재 상태: 깨끗해요!

모든 변경 내용이 저장되고 GitHub에도 올라가 있어요.
마지막 저장: "로고 변경" (10분 전)
```

#### 원격 연결이 없을 때
```
현재 상태:

이 폴더는 Git으로 관리되고 있지만, GitHub에 연결되어 있지 않아요.
연결하려면 "깃 시작해줘"라고 하세요.
```

## Step 5: Branch 상태 안내

현재 브랜치 정보도 자연어로 번역한다.

```bash
git branch --show-current
git log --oneline origin/{branch}..HEAD 2>/dev/null  # 올리지 않은 저장
git log --oneline HEAD..origin/{branch} 2>/dev/null  # 내려받지 않은 변경
```

### 브랜치 상태별 출력

#### main/master 브랜치에 있을 때
```
현재 위치: main (기본 브랜치)
```

#### 별도 브랜치에 있을 때
```
현재 위치: feature/add-login (작업 브랜치)
기본 브랜치(main)에서 분기된 상태예요.
```

#### 올리지 않은 저장이 있을 때
```
GitHub에 올리지 않은 저장이 2개 있어요:
  - "로그인 기능 추가" (10분 전)
  - "스타일 수정" (30분 전)
```

#### GitHub에 새 변경이 있을 때
```
GitHub에 아직 내려받지 않은 변경이 1개 있어요.
최신 상태로 맞추려면 "내려받아줘"라고 하세요.
```

## Step 6: Stash 상태 확인

```bash
git stash list
```

임시 저장(stash)이 있으면 안내한다:

```
임시로 보관 중인 변경 내용이 1개 있어요:
  - "작업 중이던 헤더 수정" (3일 전)

복원하려면 알려주세요.
```

## 복합 상태 처리

여러 상태가 동시에 존재할 때 우선순위에 따라 가장 중요한 것을 먼저 보여준다.

### 우선순위

1. **충돌** (즉시 해결 필요)
2. **Detached HEAD** (위험한 상태)
3. **변경 사항 있음** (저장 권유)
4. **저장했지만 안 올림** (올리기 권유)
5. **GitHub 새 변경** (내려받기 권유)
6. **깨끗함** (모든 게 정상)

### 복합 상태 출력 예시
```
현재 상태:

⚠ 변경된 파일 2개:
  - index.html (수정됨)
  - style.css (새 파일)

또한, GitHub에 올리지 않은 이전 저장이 1개 있어요:
  - "로고 변경" (1시간 전)

먼저 "저장해줘"로 현재 변경을 저장한 뒤,
"올려줘"로 모든 저장을 GitHub에 올리세요.
```

## 다음 행동 안내

모든 상태 결과 끝에 다음 행동을 안내한다:

| 상태 | 안내 |
|------|------|
| 변경 사항 있음 | "저장하려면 '저장해줘'라고 하세요" |
| 저장만 됨 | "GitHub에 올리려면 '올려줘'라고 하세요" |
| 깨끗함 | "모든 변경이 저장되고 올라가 있어요" |
| 충돌 | 충돌 해결 선택지 제시 |
| GitHub 새 변경 | "최신 내용을 받으려면 '내려받아줘'라고 하세요" |
| 원격 미연결 | "'깃 시작해줘'로 GitHub에 연결하세요" |

여러 상태가 겹치면 위 우선순위에 따라 가장 시급한 것부터 안내하되, 전체 흐름을 함께 알려준다.

## 톤

- 클라우드 폴더 비유는 답을 더 명확하게 만들 때만 쓴다.
- 구체적으로: 무엇이 바뀌었는지, 그게 무슨 뜻인지, 다음 안전한 행동이 무엇인지.
- 사용자가 묻지 않으면 고급 Git 용어는 피한다.
