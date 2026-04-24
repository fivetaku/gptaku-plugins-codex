---
slug: spotify-main
service_name: Spotify
site_url: https://open.spotify.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#1ED760"
primary_font: CircularSp
font_weight_normal: 400
token_prefix: --encore-*
---

# DESIGN.md — Spotify (Codex Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Spotify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "CircularSp", "Circular", -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 다크 배경 + 텍스트 */
:root { --bg: #121212; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 그린 */
:root { --brand: #1ED760; }
```

**절대 하지 말아야 할 것 하나**: 그린(#1ED760)을 배경색으로 넓게 깔거나, 모든 인터랙션 요소에 쓰는 것. Spotify 그린은 Play 버튼·Follow CTA 등 핵심 행동 유도에만 집중적으로 쓰여야 강렬함이 살아난다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://open.spotify.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| Token prefix | `--encore-*`, `--text-bright-accent`, `--essential-bright-accent` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · semantic_vars 추출 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React SPA (Spotify 인-하우스)
- **Design system**: Encore (Spotify 공식 DS) — `--encore-*` prefix
- **CSS architecture**: CSS 커스텀 프로퍼티 기반 토큰 시스템
- **Default theme**: dark (#121212 기반)
- **Font loading**: 자체 호스트 — CircularSp 패밀리 (다국어 variant)
- **Notable**: `--text-bright-accent` / `--essential-bright-accent` 으로 그린 토큰이 명시적으로 노출

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary**: `CircularSp` (Spotify custom Circular variant)
- **Title**: `SpotifyMixUITitle`, `SpotifyMixUITitleVariable`
- **UI**: `SpotifyMixUI`
- **다국어 variant**: `CircularSp-Arab`, `-Cyrl`, `-Deva`, `-Grek`, `-Hebr`
- **Weight**: `400` (normal), `700` (bold), `800` (extra bold)

```css
body {
  font-family: "CircularSp", "Circular", -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
  font-weight: 400;
}
.title-large {
  font-family: "SpotifyMixUITitleVariable", "SpotifyMixUITitle", "CircularSp", sans-serif;
  font-weight: 800;
}
```

> **라이선스 주의**: CircularSp Spotify 전용. 대체재: `Circular` (상용 폰트) 또는 `Nunito` (무료, 유사한 둥근 형태).

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Display | SpotifyMixUITitleVariable | 56–80px | 800 | 1.0 | -0.02em |
| Section H2 | CircularSp | 24–40px | 700 | 1.2 | -0.01em |
| Album/Track Title | CircularSp | 18–24px | 700 | 1.3 | 0 |
| Body | CircularSp | 14–16px | 400 | 1.5 | 0 |
| Caption / Meta | CircularSp | 12–13px | 400 | 1.4 | 0 |
| Number / Stat | CircularSp | 16–18px | 700 | 1 | 0 |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Green (Encore 토큰)

| CSS 변수 | Hex | 용도 |
|---|---|---|
| `--text-bright-accent` / `--essential-bright-accent` | `#1ED760` | **Play 버튼, Follow CTA, 강조** |
| Green Pressed | `#1ABC54` | 클릭/active 상태 |
| Green Hover | `#3BE477` | hover 상태 |

### Dark Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Base BG | `#121212` | body 기본 배경 |
| Surface | `#282828` | 카드, 사이드바 |
| Elevated | `#141414` | 경계 어두운 표면 |
| Subdued | `#B3B3B3` | muted 텍스트, 아이콘 |
| White | `#FFFFFF` | 기본 텍스트 |

### Dynamic / Accent Colors

| 이름 | Hex | 용도 |
|---|---|---|
| Orange | `#FFA42B` | Podcast 섹션 포인트 |
| Red | `#E91429` | Error, 라이브 배지 |
| Blue | `#0D72EA` | 링크, 정보 |
| Deep Blue | `#052A56` | 다크 섹션 배경 variant |

---

## 07. Spacing
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘·배지 |
| sm | 8px | 인라인 요소 |
| md | 16px | 카드 내부 |
| lg | 24px | 섹션 내부 |
| xl | 40px | 섹션 간격 |
| 2xl | 64px | 주요 섹션 |
| 3xl | 80px | hero 패딩 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| sm | 4px | 태그, 배지 |
| md | 8px | 카드, 패널 |
| lg | 16px | 큰 카드, 모달 |
| full | 100px | Play 버튼, 아바타, pill |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card | `0 4px 16px rgba(0,0,0,.5)` | 다크 카드 |
| player | `0 8px 40px rgba(0,0,0,.7)` | 플레이어 바 |
| green-glow | `0 0 20px rgba(30,215,96,.3)` | 플레이 버튼 글로우 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 120ms | hover 전환 |
| duration-base | 240ms | 카드·모달 |
| duration-slow | 400ms | 페이지 전환 |
| easing | `linear` | 그린 전환 (심플) |
| transition-color | `0.2s linear` | 링크 색 전환 (CSS에서 추출) |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **최대 너비**: 1600px
- **앱 레이아웃**: 좌측 네비 사이드바 + 메인 콘텐츠 + 우측 큐
- **마케팅 Hero**: full-viewport dark, 그린 CTA 버튼 중앙
- **Grid**: 앨범/플레이리스트 N-col 자동 그리드 (`repeat(auto-fill, minmax(180px, 1fr))`)
- **Player Bar**: 하단 고정, 3-zone (트랙정보 / 컨트롤 / 볼륨)

---

## 12. Components
<!-- SOURCE: manual -->

### Play 버튼 (그린)

```css
/* 핵심 Play CTA */
.btn-play {
  width: 56px; height: 56px;
  background: #1ED760;
  border-radius: 50%;
  border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: background 120ms, transform 120ms;
  box-shadow: 0 0 20px rgba(30,215,96,.3);
}
.btn-play:hover {
  background: #3BE477;
  transform: scale(1.06);
}
.btn-play:active { background: #1ABC54; transform: scale(0.98); }
```

### Follow 버튼 (아웃라인 그린)

```css
.btn-follow {
  background: transparent;
  color: #B3B3B3;
  border: 1px solid #B3B3B3;
  font-family: "CircularSp", sans-serif;
  font-size: 14px; font-weight: 700;
  padding: 8px 20px;
  border-radius: 100px;
  cursor: pointer;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  transition: border-color 120ms, color 120ms;
}
.btn-follow:hover {
  border-color: #FFFFFF;
  color: #FFFFFF;
}
.btn-follow.is-following {
  border-color: #1ED760;
  color: #1ED760;
}
```

### 음악 카드

```css
.music-card {
  background: #282828;
  border-radius: 8px;
  padding: 16px;
  cursor: pointer;
  transition: background 150ms;
  position: relative;
}
.music-card:hover { background: #3E3E3E; }
.music-card__play {
  position: absolute; bottom: 16px; right: 16px;
  opacity: 0; transform: translateY(8px);
  transition: opacity 150ms, transform 150ms;
}
.music-card:hover .music-card__play { opacity: 1; transform: translateY(0); }
.music-card__title { font-weight: 700; font-size: 16px; color: #FFFFFF; }
.music-card__sub { font-size: 14px; color: #B3B3B3; margin-top: 4px; }
```

---

## 13. Content Voice
<!-- SOURCE: manual -->

- **헤드라인**: "Music for every moment" — 보편적·포용적 감성
- **서브**: 사용자 혜택 + 숫자 (80M+ songs)
- **CTA**: "Play" / "Follow" / "Get Premium"
- **플레이리스트/큐레이션**: 분위기·맥락 중심 이름 ("Chill Vibes", "Monday Morning")
- **톤**: 친근·개인화·열정적

---

## 14. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Encore Brand Tokens */
  --text-bright-accent: #1ED760;
  --essential-bright-accent: #1ED760;

  /* Alias */
  --brand: #1ED760;
  --brand-hover: #3BE477;
  --brand-active: #1ABC54;

  /* Surface */
  --bg: #121212;
  --bg-surface: #282828;
  --bg-elevated: #141414;
  --fg: #FFFFFF;
  --fg-subdued: #B3B3B3;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 40px;
  --space-2xl: 64px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 100px;
}

body {
  font-family: "CircularSp", "Circular", -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
  font-weight: 400;
  background: var(--bg);
  color: var(--fg);
  -webkit-font-smoothing: antialiased;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: '#1ED760',
        'brand-hover': '#3BE477',
        'brand-active': '#1ABC54',
        'bg-base': '#121212',
        'bg-surface': '#282828',
        'bg-elevated': '#141414',
        'text-subdued': '#B3B3B3',
      },
      fontFamily: {
        sans: ['"CircularSp"', '"Circular"', '-apple-system', 'BlinkMacSystemFont', 'Helvetica', 'Arial', 'sans-serif'],
        title: ['"SpotifyMixUITitleVariable"', '"SpotifyMixUITitle"', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '8px',
        sm: '4px',
        lg: '16px',
        full: '100px',
      },
    },
  },
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- **그린(#1ED760)은 Play·Follow·CTA 핵심 행동에만** — 포인트 효과 극대화
- **배경은 #121212** — 순검정(#000) 아닌 약간 따뜻한 near-black
- **카드 배경은 #282828** — 배경과 레이어 구분
- **텍스트 subdued는 #B3B3B3** — 회색 톤으로 계층 구분
- **Play 버튼은 원형(border-radius: 50%)** + 그린 글로우 효과

### DON'T

- **그린(#1ED760)을 배경 전면 사용하지 않는다** — 포인트 컬러 효과 소멸
- **흰 배경을 기본으로 쓰지 않는다** — Spotify는 다크 퍼스트
- **`--text-bright-accent`를 임의 색으로 재정의하지 않는다** — Encore 시스템 파괴
- **CircularSp weight 100으로 쓰지 않는다** — 다크 배경에서 가독성 부족
- **Orange(#FFA42B)를 primary CTA로 쓰지 않는다** — Podcast 섹션 전용 포인트
