# 비율·퀄리티 키워드 자동 매핑

> 사용자 입력에 아래 키워드가 있으면 해당 파라미터를 자동 확정하고 질문에서 스킵한다.
> Codex `/imagen`은 Size/Quality 파라미터를 직접 제어할 수 없으므로, 최종적으로는 **프롬프트 자연어 힌트**로 삽입한다.

---

## 비율 (aspect_ratio)

### 자동 매핑

| 사용자 키워드 | 확정 비율 |
|--------------|----------|
| "유튜브", "썸네일", "배경화면", "프레젠테이션", "가로" | `16:9` |
| "프로필", "아이콘", "로고", "SNS 게시물" | `1:1` |
| "포스터", "인스타 스토리", "세로", "모바일" | `9:16` |
| "인스타 피드" | `1:1` (인스타 메인 피드는 정사각 권장) |
| "배너", "헤더" | `4:1` |

매핑 성공 시 질문 스킵.

### 질문 선택지 (매핑 실패 시)

| label | description | 자연어 힌트 |
|-------|-------------|------------|
| 정사각형 (1:1) | 프로필, 아이콘, SNS 게시물 | `Square 1:1 aspect ratio, balanced central composition` |
| 가로형 (16:9) | 유튜브 썸네일, 프레젠테이션, 배경화면 | `Widescreen 16:9 horizontal composition, landscape orientation` |
| 세로형 (9:16) | 모바일 세로, 인스타 스토리, 포스터 | `Vertical 9:16 portrait composition, tall orientation` |
| 와이드 배너 (4:1) | 웹 헤더, 이메일 배너 | `Ultra-wide 4:1 banner composition, panoramic horizontal strip` |
| 자동 | 내용에 맞게 AI 판단 | (자연어 힌트 삽입하지 않음) |

---

## 퀄리티 (quality)

### 자동 매핑

| 사용자 키워드 | 확정 퀄리티 |
|--------------|------------|
| "빨리", "시안", "초안", "대충", "드래프트" | `Low` |
| "고품질", "정교하게", "세밀하게", "선명하게" | `High` |
| "4K", "최고 품질", "초고해상도", "대형 인쇄" | `4K` |
| (기본, 명시 없음) | `Auto` (자연어 힌트 삽입하지 않음) |

매핑 성공 시 질문 스킵.

### 질문 선택지 (매핑 실패 시)

| label | description | 자연어 힌트 |
|-------|-------------|------------|
| 빠른 시안 (Low) | 초안 확인용, 5-10초 | `Quick draft quality, sketch-level detail, fast turnaround` |
| 표준 (Medium) | 일반 용도 | `Standard quality, balanced detail and speed` |
| 고품질 (High) | 꼼꼼한 결과물 | `High quality, refined detail, crisp rendering, professional-grade` |
| 최고 (4K) | 대형 인쇄, 최고 해상도 | `4K ultra-high-resolution, maximum detail, print-grade quality, professional post-production level` |
| 자동 | AI 판단 | (자연어 힌트 삽입하지 않음) |

---

## 힌트 삽입 위치

영문 프롬프트 작성 시 Technical Specifications 섹션에 추가:

```markdown
## Technical Specifications
- {비율 자연어 힌트}
- {퀄리티 자연어 힌트}
- Format: PNG
- Deliver raw generated image as-is; no post-processing, no crop, no resize
- (기타 모드별 technical specs ...)
```

"자동" 선택 시엔 해당 힌트 줄을 생략한다.

---

## Codex /imagen 한계 (사용자에게 안내 필요)

**실험적으로 확인된 한계**:
- Size/Quality 자연어 힌트는 "방향성 제공" 수준. 정확한 해상도 지정 불가.
  - 16:9 힌트 → 정확한 2560x1440이 아니라 1672x941 같은 근사값
  - 4K 힌트 → 해상도 높게 시도하지만 3840x2160 보장 X
- 9:16 세로, 4:1 배너는 Codex 이미지 모델이 지원하지 않을 가능성 있음 (실험 필요)

**권장**:
- 정밀한 비율·해상도가 필요한 작업엔 별도 도구 사용 권장 (플러그인 스코프 밖)
- 일반 용도에서는 "대충 맞는 방향성"으로 충분
