# Redesign Aesthetics — Lv3 전체 리디자인 미학 가이드

> **목적**: design.md가 "무엇을(What)" 강제한다면, 이 문서는 "어떻게 살아있게(How)" 채운다.
> **적용 범위**: Lv3 전체 리디자인에서만 사용. Lv1/Lv2는 무시.

---

## 🔒 절대 원칙 — 이층 브리프 구조

```
Layer 1 (HARD CONSTRAINT): design.md 명시 영역
  - 토큰 (color, font, spacing, radius)
  - 명시된 컴포넌트 마크업 + CSS
  - §11 Layout Patterns
  - §18 DO/DON'T
  → 절대 수정 금지, 환각 금지

Layer 2 (SOFT CREATIVITY): design.md 비명시 영역
  - 모션/애니메이션 (§10 Motion 없을 때)
  - Atmosphere (배경 텍스처, 그라디언트 메시)
  - 비대칭/오버랩 같은 spatial composition 디테일
  - 코드 복잡도 (미학에 맞춰)
  → 이 문서의 가이드라인 적용
```

**판단 기준**: design.md에 적힌 게 있으면 그것을, 없으면 이 문서를 따른다.

---

## 1. BOLD 방향성 Commit

### 추출 방법 (Step 0)

design.md §00 Visual Theme의 첫 문단에서 핵심 미학을 1~2 단어로 추출:

| 사이트 | §00 핵심 | BOLD 방향성 |
|--------|---------|------------|
| Stripe | "차갑고 기술적, fintech 신뢰감" | **Refined SaaS** |
| Tesla | "라이트 테마, 차량 사진, 절제" | **Industrial Minimalism** |
| Apple | "흑백, 미니멀, 프리미엄" | **Monochrome Luxury** |
| Figma | "흑백 + 컬러풀 액센트" | **Monochrome Maximalism** |
| Notion | "warm warm warm, 친근함" | **Warm Productivity** |
| Linear | "다크 + 인디고, 앱 느낌" | **Cool Productivity** |
| Toss | "쾌활한 블루, 핀테크" | **Friendly Fintech** |
| Warp | "크림+검정, 터미널" | **Editorial Minimalism** |
| Discord | "보랏빛 그라디언트, 장난기" | **Playful Gradient** |
| Resend | "에디토리얼, serif display" | **Editorial Magazine** |

### Commit 원칙

- 한 가지 방향만 선택 (혼합 금지)
- 이후 모든 결정의 기준
- 사용자가 "극단까지" 선택하면 → 100% commit
- 사용자가 "절충" 선택하면 → 60% commit (디테일 일부 완화)

---

## 2. AI Slop 안티패턴 — 회피 목록

### 🚫 폰트 (design.md에 명시 안 되어 있을 때만 적용)

```
금지:
- Inter, Roboto, Arial, Helvetica (default)
- system-ui (단독)
- Google Fonts 상위 10개 (Open Sans, Lato 등)
- Space Grotesk (지나치게 자주 사용됨)

대안:
- 사이트 §00 분위기에 맞는 distinctive 폰트
- display + body 페어링 (예: Tiempos + Inter Display)
- 시스템 폰트 활용 시 character 강조 (-apple-system 우선)

⚠️ 예외: design.md frontmatter에 폰트가 명시되면 무조건 그 폰트 사용
```

### 🚫 색상 패턴

```
금지:
- 보라 그라디언트 (135deg, #667eea → #764ba2 등)
- 흰 배경 + 보라 강조 (대표적 AI 스타일)
- 균등 분산된 6-8색 팔레트
- 무지개 그라디언트 (생일 카드 느낌)

대안:
- Dominant 1색 + Sharp accent 1색 (8:2 비율)
- 사이트의 실제 hex 활용
- design.md §06 컬러 분포 따라가기
```

### 🚫 레이아웃 패턴

```
금지:
- 12-column grid에 균등 분포 카드
- "Hero + Feature 3개 카드 + CTA" 천편일률 구조
- 둥근 카드(8-12px radius) 그리드의 무한 반복
- 중앙 정렬 텍스트 + 그 아래 버튼 패턴

대안:
- 사이트 §11 Layout Patterns 그대로 따르기
- 비대칭, 오버랩, grid-breaking (§11 명시 안 할 때만)
- 풀블리드 섹션, 다이애고날 플로우
```

### 🚫 컴포넌트 패턴

```
금지:
- "Lorem ipsum 같은 평범한 카드" (이미지 + 제목 + 설명 + 버튼)
- 모든 버튼이 같은 radius, padding, hover 효과
- 평범한 footer (회사명 + 링크 + 소셜)

대안:
- 사이트 §13 Components 충실히 재현
- 시그니처 컴포넌트 1개 강조
```

---

## 3. 톤앤매너 카탈로그 — 12가지 극단

각 미학별로 **타이포 / 컬러 / 레이아웃 / 모션** 가이드:

### Refined Minimalism (Apple, Stripe, Linear)
- 타이포: 절제된 sans, 큰 H1 vs 작은 본문 대비
- 컬러: 1 dominant + 1 brand accent, neutral 8단계
- 레이아웃: 넓은 여백, grid 정렬, 작은 카드
- 모션: 0.3s ease-out, hover만, 최소화

### Industrial Minimalism (Tesla, Vercel)
- 타이포: 시스템 sans, uppercase 헤더, wide letter-spacing
- 컬러: 흑백 + 1 sharp accent, neutral 4단계
- 레이아웃: 풀블리드 섹션, 100vh hero, 풀스크린 이미지
- 모션: staggered reveal 1회, scroll-triggered fadeIn

### Monochrome Luxury (Apple, Chanel)
- 타이포: serif display + sans body 대비
- 컬러: 흑백 only, 그라데이션 금지
- 레이아웃: 중앙 정렬, 넓은 여백, 큰 이미지
- 모션: 정적 또는 매우 절제된 fade

### Editorial Magazine (Resend, Medium)
- 타이포: serif display + sans body, drop cap, large H1
- 컬러: warm beige + black + 1 accent
- 레이아웃: column-based, 본문 max-width 720px
- 모션: 정적

### Playful Gradient (Discord, Figma)
- 타이포: rounded sans, weight bold
- 컬러: 다채로운 그라디언트, 5-7색 팔레트
- 레이아웃: 비대칭, 오버랩, 둥근 컴포넌트
- 모션: 활발한 hover, micro-interaction 풍부

### Cool Productivity (Linear, Notion 다크)
- 타이포: sans, 작은 사이즈, 빽빽한 위계
- 컬러: 다크 베이스 + 인디고/보라 accent
- 레이아웃: 사이드바 + 메인, density 높음
- 모션: 빠른 transitions (0.15s), keyboard friendly

### Warm Productivity (Notion 라이트)
- 타이포: sans, warm gray text
- 컬러: warm white bg, warm gray, 1 brand color
- 레이아웃: 여유로운 spacing, 친근한 카드
- 모션: 부드러운 ease-in-out

### Friendly Fintech (Toss, Robinhood)
- 타이포: rounded sans, 가독성 우선
- 컬러: 단일 brand color (강한 saturation), neutral
- 레이아웃: 모바일 우선, 큰 버튼, 분명한 위계
- 모션: 친근한 bounce, 빠른 피드백

### Maximalist Chaos (Awwwards 류)
- 타이포: 다양한 폰트 페어링, 큰 사이즈, 의도적 부조화
- 컬러: 5+색 팔레트, vivid
- 레이아웃: 비대칭, 오버랩, grid 파괴
- 모션: 풍부한 애니메이션, scroll-triggered

### Brutalist Raw (Vercel 일부, Hashnode)
- 타이포: monospace, system fonts, 의도적 ugly
- 컬러: 무채색 + 1 strong accent, no gradient
- 레이아웃: grid 명확, border 두꺼움, raw
- 모션: 거의 없음 또는 instant transitions

### Retro-Futuristic (Stripe blog, Linear)
- 타이포: pixel/grotesk, 80년대 SF 느낌
- 컬러: neon + dark, 보라/시안
- 레이아웃: grid-overlay, 격자 패턴
- 모션: glitch, scanline, terminal cursor

### Soft Pastel (당근, Notion campaign)
- 타이포: rounded sans, weight 500
- 컬러: 파스텔 5-6색
- 레이아웃: 둥근 카드, 부드러운 spacing
- 모션: 부드러운 ease, 절제된 bounce

---

## 4. 모션 가이드 (§10 Motion 없을 때)

### 기본값: Staggered Reveal (페이지 로드 1회)

```css
/* 모든 섹션의 자식 요소에 순차적 fade-in */
.section > * {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.8s var(--ease-out-expo) forwards;
}
.section > *:nth-child(1) { animation-delay: 0.1s; }
.section > *:nth-child(2) { animation-delay: 0.2s; }
.section > *:nth-child(3) { animation-delay: 0.3s; }
.section > *:nth-child(4) { animation-delay: 0.4s; }

@keyframes fadeInUp {
  to { opacity: 1; transform: translateY(0); }
}
```

### 미학별 모션 강도

| 미학 | 모션 강도 | 예시 |
|------|----------|------|
| Industrial Minimalism | 1회 staggered, 그 후 정적 | Tesla |
| Refined Minimalism | hover만, 0.3s | Apple |
| Playful Gradient | 풍부, 0.5s bounce | Discord |
| Maximalist Chaos | 스크롤 트리거 + parallax | Awwwards |
| Brutalist | 모션 없음 또는 instant | Hashnode |

### 사용자가 "정적" 선택 시
모션 코드 전혀 추가 안 함. 타이포/레이아웃으로만 임팩트.

### 사용자가 "풀 연출" 선택 시
- 페이지 로드 staggered reveal
- 스크롤 트리거 (`IntersectionObserver`)
- 호버 micro-interaction
- 페이지 전환 (있으면)

---

## 5. Atmosphere — 배경 깊이 가이드

### 언제 추가하는가
- design.md에 명시된 배경이 단색일 때
- Hero 영역이 평범해 보일 때
- 섹션 구분이 밋밋할 때

### 기법 카탈로그

#### Noise Texture
```css
body {
  background:
    url("data:image/svg+xml,%3Csvg ...%3E"),
    var(--bg);
  background-blend-mode: overlay;
}
```
- 적합: Industrial, Editorial, Brutalist

#### Gradient Mesh
```css
.hero {
  background:
    radial-gradient(at 20% 30%, var(--accent-1) 0px, transparent 50%),
    radial-gradient(at 80% 70%, var(--accent-2) 0px, transparent 50%),
    var(--bg);
}
```
- 적합: Playful, Maximalist, Refined SaaS

#### Subtle Border Lines
```css
section {
  border-top: 1px solid rgba(0,0,0,0.05);
}
```
- 적합: Minimalism, Brutalist

#### Grain Overlay
```css
.hero::after {
  content: '';
  position: absolute; inset: 0;
  background: url('grain.png');
  opacity: 0.04;
  mix-blend-mode: overlay;
  pointer-events: none;
}
```
- 적합: Editorial, Luxury

#### Layered Transparency
```css
.card {
  background: rgba(255,255,255,0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.2);
}
```
- 적합: Modern, Glassmorphism

---

## 6. 코드 복잡도 ↔ 미학 매칭

| 미학 | 코드 복잡도 | 특징 |
|------|------------|------|
| Refined Minimalism | **낮음** | CSS 변수, 1개 transition, 절제된 hover |
| Industrial Minimalism | **낮음~중간** | + staggered reveal, IntersectionObserver |
| Editorial Magazine | **중간** | + drop-cap, column layout, serif rendering |
| Playful Gradient | **높음** | + 다층 그라디언트, hover bounce, 풍부한 transitions |
| Maximalist Chaos | **매우 높음** | + parallax, scroll-triggered, particle, custom cursor |
| Brutalist Raw | **매우 낮음** | 거의 모든 효과 제거, 순수 CSS만 |

**규칙**: 미니멀리즘인데 화려한 코드 ❌ / 맥시멀리즘인데 단순 코드 ❌

---

## 7. Unforgettable 시그니처 — 한 가지 강조

사용자가 Step 1.7b에서 선택한 항목을 코드에 명확히 구현:

### Hero 임팩트
- 100vh 풀스크린
- 드라마틱 배경 (이미지/그라디언트/노이즈)
- 큰 H1 (clamp 60px ~ 120px)
- 강한 contrast (어두운 배경 위 흰 텍스트)

### 타이포 대비
- 거대 display vs 작은 body (10배 이상 차이)
- weight 대비 (300 display vs 600 caption)
- letter-spacing 극단 (display -0.02em, caption +0.15em)

### 섹션 전환
- 섹션마다 배경 톤 drastic 변화
- 다크 ↔ 라이트 전환
- 풀블리드 이미지 섹션 끼우기
- 스크롤에 따라 컬러 변하는 효과

### 미니멀 극단
- 장식 완전 제거 (border 최소, shadow 없음, radius 0~4px)
- 색상 3개 이내
- 폰트 1개만
- 모션 1개 (페이지 로드만)

---

## 8. §18 DON'T 위반 자동 체크

design.md §18 DON'T 리스트와 코드를 자동 대조:

```
Tesla §18 DON'T:
- "배경을 #FFFFFF 순백으로 두지 말 것"
→ 코드에 background: #fff 또는 white 있으면 경고

Stripe §18 DON'T:
- "body weight 400으로 두지 말 것"
→ body { font-weight: 400 } 있으면 경고

Notion §18 DON'T:
- "텍스트를 #000 순흑으로 두지 말 것"
→ color: #000 또는 black 있으면 경고
```

위반 발견 시 Step 3 검증에서 사용자에게 알리고 수정 옵션 제공.

---

## 9. 재현성 보장 (Anti-pattern hunter 경고 반영)

❌ **금지**: "매번 다른 결과" — frontend-design의 "No design should be the same"
✅ **준수**: 같은 slug + 같은 사용자 답변 = 같은 결과

이를 위해:
- AI가 자체 판단으로 폰트/색 변경 금지
- 사용자 답변에 따라 결정론적으로 코드 생성
- "더 나은 디자인" 같은 자의적 판단 금지

---

## 10. 검증 체크리스트 (Step 3에서 사용)

```
□ BOLD 방향성 commit 유지됨 (중간값 없음)
□ Unforgettable 요소가 코드에 구현됨
□ 모션 레벨이 사용자 선택대로 적용됨
□ AI slop 폰트/색/그라디언트 없음
□ §18 DON'T 위반 없음
□ design.md §15 토큰 모두 적용됨
□ 코드 복잡도가 미학과 매칭됨
□ 콘텐츠 100% 보존
```
