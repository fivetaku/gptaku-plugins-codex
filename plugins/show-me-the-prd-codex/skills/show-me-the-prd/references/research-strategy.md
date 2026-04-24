# 리서치 전략 -- 도구 라우팅과 배치 오케스트레이션

## 리서치 엔진: 기존 gptaku 플러그인 활용

바퀴를 새로 만들지 않는다. gptaku에 이미 있는 플러그인을 활용한다.

| 용도 | 사용 도구 | 사용 조건 | 예시 |
|------|----------|----------|------|
| 공식 문서 기반 기술 조사 | docs-guide 스킬 | 플러그인 설치됨 | "Next.js App Router 캐싱" |
| 종합 리서치 (시장, 트렌드) | deep-research 스킬 | 플러그인 설치됨 | "인보이싱 앱 시장 조사" |
| 빠른 검색 (가격, 비교, 팩트) | WebSearch (빌트인) | 항상 사용 가능 | "Supabase 무료 용량 2026" |
| 페이지 내용 추출 | WebFetch (빌트인) | 항상 사용 가능 | 특정 URL의 가격표 확인 |

---

## 플러그인 의존성 확인 방법

Phase 0에서 자동 확인. 유저에게 묻지 않고 내부적으로 기억.

```
확인 방법:
사용 가능한 스킬 목록에 docs-guide, deep-research가 있는지 확인.
있으면 Skill 도구로 호출, 없거나 호출 실패 시 WebSearch로 폴백.

결과:
- 있음 -> Skill(skill="docs-guide", args="...") / Skill(skill="deep-research", args="...") 활용
- 없음 -> WebSearch로 폴백 (기본 동작에 문제 없음)
```

**없어도 동작한다** -- docs-guide/deep-research가 없으면 빌트인 WebSearch로 폴백.
있으면 더 정확하고 깊이 있는 리서치가 가능.

---

## 리서치 라우팅 -- 질문 종류별 도구 선택

```
"Next.js에서 이미지 최적화 어떻게 해?"
  -> docs-guide (공식문서 기반 정확한 답)
  -> 폴백: WebSearch("{framework} image optimization guide")

"사진 앱 시장 규모와 트렌드"
  -> deep-research (멀티소스 종합 리서치)
  -> 폴백: WebSearch("{domain} market size trends 2026")

"Supabase Storage 무료 용량"
  -> WebSearch (빠른 팩트 체크)

"Vercel 배포 가격"
  -> docs-guide (공식문서) 또는 WebSearch
```

### 라우팅 규칙

| 질문 유형 | 1순위 | 2순위 (폴백) |
|----------|-------|-------------|
| 프레임워크/라이브러리 사용법 | docs-guide | WebSearch + WebFetch |
| 시장 조사, 경쟁 분석 | deep-research | WebSearch (여러 쿼리) |
| 가격, 용량, 스펙 비교 | WebSearch | WebFetch (공식 페이지) |
| 베스트 프랙티스, 구조 | docs-guide | WebSearch |
| 최신 트렌드 | WebSearch | deep-research |

---

## 리서치 배치 오케스트레이션

리서치를 아무 때나 하면 유저가 기다려야 한다. **인터뷰 사이사이 빈 시간에 배치**한다.

### 배치 타이밍

| 배치 | 타이밍 | 목적 | 도구 |
|------|--------|------|------|
| Batch 1 | Step 1 답변 직후 | 시장/경쟁 빠른 파악 | WebSearch |
| Batch 2 | Step 2 기능 선택 직후 | 기능별 기술 난이도 확인 | WebSearch + docs-guide |
| Batch 3 | Step 4 Phase 확인 후 | 모던 스택 비교, 공식문서 | docs-guide + WebSearch |
| Batch 4 | Step 5 스택 선택 후 | 프로젝트 구조, 배포 가이드 | docs-guide |
| (선택) | 유저 요청 시 | 깊은 시장 조사 | deep-research |

### 배치 원칙

| 원칙 | 설명 |
|------|------|
| 유저 대기 시간 = 0 | 리서치는 유저가 답변한 직후 or AI 처리 중에 병렬 실행 |
| 다음 질문에 반영 | 리서치 결과가 바로 다음 질문의 선택지/설명에 녹아듦 |
| 점진적 구체화 | 처음엔 넓게(WebSearch), 나중엔 깊게(docs-guide) |
| deep-research는 선택적 | 시장 조사가 필요한 경우에만. 기본 흐름에서는 WebSearch + docs-guide로 충분 |
| 캐싱 | 같은 주제 중복 검색 방지. 배치 1 결과를 배치 2-4에서 재활용 |

---

## 배치별 검색 쿼리 패턴

### Batch 1: 아이디어 직후 (시장 파악)

```
WebSearch: "{도메인} app features 2026"
WebSearch: "{유사 서비스명} 불만 사항 대안 앱"
WebSearch: "{도메인} 앱 필수 기능 목록"
```

목적: Step 2에서 "이런 기능들이 일반적이에요" 목록을 근거 있게 제시.

### Batch 2: 기능 선택 직후 (기술 조사)

```
docs-guide: "{핵심 기능} implementation best practice"
WebSearch: "{핵심 기능} 구현 난이도 비용"
WebSearch: "{도메인} data model design pattern"
```

목적: Step 3 데이터 모델 자동 추출의 근거. 기능별 복잡도 판단.

### Batch 3: 기술 스택 선택 전 (스택 비교)

```
WebSearch: "best tech stack for {플랫폼} {도메인} app 2026"
WebSearch: "{프레임워크A} vs {프레임워크B} 2026 comparison"
docs-guide: "{후보 프레임워크} getting started tutorial"
WebSearch: "{DB 후보} free tier pricing 2026"
```

목적: Step 5에서 리서치 기반 2-3개 추천 근거.

### Batch 4: 문서 생성 전 (구조 보강)

```
docs-guide: "{선택된 프레임워크} project structure recommended"
WebSearch: "{선택된 스택} deployment guide 2026"
WebSearch: "{도메인} 앱 보안 규정 주의사항"
```

목적: Step 6 문서에 구체적인 프로젝트 구조와 배포 가이드 포함.

---

## 검색 쿼리 규칙

1. **항상 현재 연도 포함**: "React vs Vue" (X) -> "React vs Vue 2026" (O)
2. **영어 + 한국어 병행**: 영어 쿼리가 결과 품질 높음. 한국어 쿼리로 로컬 정보 보완.
3. **구체적 질문**: "best framework" (X) -> "best framework for photo sharing web app 2026" (O)
4. **비교 쿼리**: "X vs Y comparison 2026 pros cons"
5. **가격 쿼리**: "{서비스} pricing free tier 2026"

---

## 리서치 결과 활용 방법

리서치 결과는 유저에게 직접 보여주지 않는다. 다음 방식으로 녹여낸다:

1. **선택지 설명에 반영**: "조사해봤는데, 현재 가장 많이 쓰이는 조합이에요"
2. **복잡도 판단 근거**: "이 기능은 {API} 연동이 필요해서 좀 복잡해요"
3. **가격 정보 포함**: "{서비스}는 무료로 시작 가능하고, {용량} 무료"
4. **문서에 근거 삽입**: "기술 스택 선택 이유: {리서치 결과 요약}"

---

## docs-guide / deep-research 스킬 호출 방법

플러그인이 설치되어 있을 때, 해당 스킬을 Skill 도구로 호출한다.

```
# docs-guide 호출
Skill(skill="docs-guide", args="Next.js App Router 프로젝트 구조")

# deep-research 호출
Skill(skill="deep-research", args="인보이싱 앱 시장 분석")
```

**주의**: deep-research는 시간이 오래 걸린다. 기본 흐름에서는 WebSearch로 충분하고, 유저가 명시적으로 시장 조사를 원할 때만 사용.
