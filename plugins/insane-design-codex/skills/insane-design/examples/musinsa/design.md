---
slug: musinsa
service_name: Musinsa
site_url: https://www.musinsa.com/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#000000"
primary_font: Pretendard
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Musinsa (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Musinsa처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: Pretendard, "Apple SD Gothic Neo", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: `#245EFF` 파랑을 무신사 브랜드로 착각하는 것. `#245EFF`는 앱바 배지(notification dot)에만 쓰이는 알림 색이다. 무신사의 primary CTA(`.dialog-button__confirm`)와 FAB(`.fab__button--black`)은 `#000000` — 순수한 검정이 브랜드 컬러다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.musinsa.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Next.js CSS Modules (해시 suffix `_qtzt1_57` 패턴) |
| Token prefix | N/A (CSS Modules 해시, 리터럴 hex) |
| Method | CSS 셀렉터 역할 분석 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (CSS Modules — `_xxxxx_NN` 해시 패턴)
- **Design system**: 무신사 내부 커스텀 — `Pretendard` 기반
- **CSS architecture**: CSS Modules (컴포넌트별 해시 격리)
  ```
  _appbar__* (앱바 컴포넌트)
  _dialog-button__* (다이얼로그)
  _fab__* (Floating Action Button)
  developer-tools_* (개발 도구 오버레이)
  ```
- **Class naming**: CSS Modules 해시 (`_appbar__button-badge_qtzt1_57`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: Pretendard (한국 패션 특화 가변 폰트)
- **Canonical anchor**: `#000000` — confirm 버튼, FAB black 버튼 — 순수 검정

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Pretendard` (오픈소스, SIL 라이선스)
- **Code font**: `ui-monospace` (시스템 기본)
- **Weight normal / bold**: `400` / `500` (UI), `600` (강조)

```css
:root {
  --musinsa-font-family: Pretendard, "Apple SD Gothic Neo", sans-serif;
  --musinsa-font-weight-normal: 400;
  --musinsa-font-weight-medium: 500;
  --musinsa-font-weight-semibold: 600;
}
body {
  font-family: var(--musinsa-font-family);
  font-weight: var(--musinsa-font-weight-normal);
}
```

> 일본어: `Hiragino Sans, Noto Sans JP`, 중국어(간): `PingFang SC, Noto Sans, MiSans`, 중국어(번): `PingFang TC, Noto Sans CJK TC` — 다국어 지원.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ 명시적 타이포 스케일 없음. 리터럴 px 값 직접 적용.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| badge-notification | N/A | N/A | N/A | N/A |
| filter-btn-text | 12px | 500 | N/A | N/A |
| share-btn | 13px | 500 | 18px | N/A |
| marketing-link | 13px | 400 | 18px | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (2 steps)

| Token | Hex |
|---|---|
| brand-black | `#000000` |
| brand-white | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| black | `#000000` | — |
| bg-developer-actions | `#F5F5F5` | — |
| bg-developer-btn | `#F0F0F0` | — |
| border-muted | `#E0E0E0` | — |
| text-marketing | `#666666` | — |
| bg-nav-link | `#8A8A8A1A` | — |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| notification-badge | bg | `#245EFF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| confirm-btn-bg | `#000000` | 다이얼로그 확인 버튼 배경 |
| confirm-btn-color | `#FFFFFF` | 다이얼로그 확인 버튼 텍스트 |
| fab-black-bg | `#000000` | FAB 검정 버튼 |
| fab-white-bg | `#FFFFFF` | FAB 흰색 버튼 |
| fab-white-border | `#E0E0E0` | FAB 흰색 버튼 테두리 |
| notification-badge | `#245EFF` | 알림 배지 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| developer-actions-p | 16px | 개발자 도구 패딩 |
| developer-btn-py | 8px | 개발자 버튼 패딩 세로 |
| developer-btn-px | 16px | 개발자 버튼 패딩 가로 |
| badge-h | 16px | 배지 높이 |
| badge-min-w | 16px | 배지 최소 너비 |
| badge-px | 4px | 배지 좌우 패딩 |
| share-btn-w | 80px | 공유 버튼 너비 |
| marketing-btn-h | 44px | 마케팅 동의 버튼 높이 |

**주요 alias**:
- 배지: 16×16px, 패딩 4px (소형 고정)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| developer-btn | 4px | 개발자 도구 버튼 |
| badge | 100% | 배지 (완전 원형) |
| marketing-btn | 4px | 마케팅 동의 버튼 |
| nav-link | 4px | 하단 네비게이션 링크 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Dialog Button — Confirm (`._dialog-button__confirm`)

```html
<button class="dialog-button__confirm">확인</button>
```

| 속성 | 값 |
|---|---|
| border-color | `#000000` |
| background-color | `#000000` |
| color | `#FFFFFF` |

### FAB — Black (`._fab__button--black`)

```html
<button class="fab__button--black"></button>
```

| 속성 | 값 |
|---|---|
| background-color | `#000000` |
| border-color | `#000000` |

### FAB — White (`._fab__button--white`)

```html
<button class="fab__button--white"></button>
```

| 속성 | 값 |
|---|---|
| background-color | `#FFFFFF` |
| border | 1px solid `#E0E0E0` |

### Notification Badge (`._appbar__button-badge`)

```html
<span class="appbar__button-badge">1</span>
```

| 속성 | 값 |
|---|---|
| display | inline-flex |
| height | 16px |
| min-width | 16px |
| padding | 0 4px |
| background-color | `#245EFF` |
| color | `#FFFFFF` |
| border-radius | 100% |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Musinsa — copy into your root stylesheet */
:root {
  /* Fonts */
  --musinsa-font-family: Pretendard, "Apple SD Gothic Neo", sans-serif;
  --musinsa-font-weight-normal: 400;
  --musinsa-font-weight-medium: 500;
  --musinsa-font-weight-semibold: 600;

  /* Brand */
  --musinsa-color-brand: #000000;
  --musinsa-color-badge: #245EFF;

  /* Surfaces */
  --musinsa-bg-page: #FFFFFF;
  --musinsa-text: #000000;
  --musinsa-text-muted: #666666;

  /* Border */
  --musinsa-border: #E0E0E0;

  /* Radius */
  --musinsa-radius-sm: 4px;
  --musinsa-radius-full: 100%;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- CTA와 FAB primary는 `#000000` 순수 검정
- 알림 배지만 `#245EFF` 파랑 사용
- 버튼 모서리는 4px 또는 원형(100%)만
- Pretendard weight 400/500/600 스택 활용

### ❌ DON'T
- `#245EFF`를 메인 브랜드 색으로 사용 — 알림 배지 전용
- CSS Modules 해시 클래스(`_qtzt1_57`)를 직접 복사 — 빌드마다 바뀜
- 다국어 폰트 없이 일본어/중국어 서비스 — 별도 font-family 선언 필요
