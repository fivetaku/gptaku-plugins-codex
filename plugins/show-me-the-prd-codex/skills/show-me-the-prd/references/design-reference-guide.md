# 디자인 레퍼런스 수집 가이드

> UI 산출물이 있는 기획에서만 발동한다. 백엔드/CLI/라이브러리 기획에서는 이 파일을 읽을 일이 없어야 한다.

## 게이트 — 언제 수집하는가

| 판정 | 기준 | 동작 |
|------|------|------|
| **UI 있음** | 웹/앱/랜딩/대시보드/어드민 등 사용자가 보는 화면이 핵심 산출물 | 수집 실행 |
| **UI 없음** | API 서버, CLI, 파이프라인, 라이브러리, 봇 | **스킵** — 이 단계 전체 생략, 질문도 추가하지 않음 |
| **부분 UI** | "API 서버 + 간단한 어드민" 류 | **기본 스킵.** 사용자가 스타일/디자인을 먼저 언급했을 때만 실행 |

판정 재료는 `$ARGUMENTS`와 Turn 1 답변이다. 별도 질문으로 판정하지 않는다.

## 스타일 입력 3경로

1. **사용자가 스타일을 말함** ("깔끔하게", "토스 느낌") → 스타일 어휘 매핑 후 바로 수집
2. **사용자가 레퍼런스 URL을 줌** → 수집 대신 그 URL을 sources.json에 기록. insane-design이 설치돼 있으면 "이 URL로 `/insane-design:analysis` 돌리면 CSS 수준 분석 가능"을 납품 시 안내
3. **아무 말 없음** → 카드 문항으로 스타일 1개 질문 (아래 어휘에서 도메인에 맞는 3~4개 추림)

## 스타일 어휘 매핑 (사용자 표현 → 검색 키워드)

| 사용자 표현 | 검색 키워드 |
|------------|------------|
| 깔끔한, 심플한, 여백 많은 | minimal, clean |
| 개성있는, 투박한, 강렬한 | neobrutalism, brutalist |
| 투명한, 유리 느낌 | glassmorphism |
| 부드러운, 아기자기한 | soft ui, pastel, rounded |
| 어두운, 시크한 | dark mode, dark theme |
| 고급스러운, 명품 느낌 | luxury, premium, editorial |
| 레트로, 옛날 느낌 | retro, y2k, vintage |

여기 없는 표현은 가장 가까운 영문 디자인 용어로 스스로 변환한다. 이 표는 예시이지 전체 목록이 아니다.

## 쿼리 조립과 소스 어댑터

쿼리 = `{서비스 도메인} + {스타일}` (영문). 예: 핀테크 대시보드 + 미니멀 → `minimal fintech dashboard`.

| 소스 | URL 패턴 | 특징 |
|------|---------|------|
| Dribbble | `https://dribbble.com/search/{kw1}-{kw2}-{kw3}` (하이픈 슬러그) | UI 샷 최다. AWS WAF — 브라우저 경로 필요 |
| Cosmos | `https://www.cosmos.so/search?q={query}` | 큐레이션 무드. curl 직접 통과 |
| Mobbin | `https://mobbin.com/search/...` | 실제 앱 플로우. 목록은 통과, 상세는 로그인 |
| Land-book | `https://land-book.com/?search={query}` | 랜딩 특화. Cloudflare — 브라우저 경로 필요 |
| Awwwards | `https://www.awwwards.com/websites/{tag}/` | 수상작. 브라우저 경로 필요 |

## 수집 절차

1. **접근 순서**: insane-search 플러그인이 캐시에 있으면 `python3 -m engine "<URL>"` (스킬 디렉토리에서) 먼저. 없거나 실패하면 Playwright/브라우저 MCP로 페이지 로드 후 `img` 태그에서 CDN URL 추출 (`cdn.dribbble.com/userupload`, `cdn.cosmos.so` 등).
2. **다운로드**: CDN 이미지는 Referer 헤더(출처 사이트 루트)를 넣어 curl로 저장. Dribbble은 `?format=webp&resize=800x600` 파라미터로 적정 크기 지정.
3. **비전 스크리닝 (필수)**: 다운로드한 이미지를 Read 도구로 직접 열어 판정한다. alt 텍스트 매칭만 믿지 않는다 — 모바일/데스크톱 구분, 스타일 부합 여부는 이미지를 봐야만 안다. 6~8장 받아 **상위 3~5장만 keep**.
4. **저장**: `PRD/references/` 폴더에 이미지 + `sources.json`.

목표 수량: 3~5장. 그 이상은 과잉 — 기획 참고용이지 아카이브가 아니다.

## sources.json 스키마

```json
{
  "query": { "service": "...", "style": "...", "source": "dribbble", "searchUrl": "..." },
  "retrievedAt": "YYYY-MM-DD",
  "license_note": "Reference-only local cache. Do NOT republish in deliverables; link to source instead.",
  "items": [
    { "file": "ref1.webp", "title": "...", "sourceImage": "https://...", "sourcePage": "https://... (알 수 없으면 searchUrl)", "screen": "mobile|desktop", "match": "스타일 ✓ / 도메인 ✓ / 비고", "verdict": "keep|keep — best fit" }
  ]
}
```

## 저작권 가드 (절대 규칙)

- 수집 이미지는 **로컬 참고 전용**. PRD 본문에는 파일 경로 + 출처 링크만 넣는다.
- 산출물(앱, 랜딩, 공개 문서)에 수집 이미지를 재게시하지 않는다. PRD의 references 섹션에 이 규칙을 한 줄 명시한다.
- 레퍼런스는 "따라 그리기" 대상이 아니라 방향 합의용 무드보드다.

## 실패 처리

- 소스 하나가 막히면 다음 소스로 넘어간다 (Dribbble → Cosmos → Land-book 순 추천).
- 전 소스 실패 시: 수집 없이 진행하고, PRD 가정 원장에 "디자인 레퍼런스 미수집 — 스타일 방향은 텍스트 합의({스타일})에만 근거" 항목을 기록한다. 기획을 막지 않는다.
