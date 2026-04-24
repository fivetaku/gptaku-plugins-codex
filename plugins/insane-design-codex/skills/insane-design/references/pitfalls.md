# 14가지 함정 — 35개 서비스 분석에서 발견

> Step 4 (INTERPRET)에서 반드시 참조. AI 판정 시 아래 패턴에 빠지지 않도록 주의.

## 1. 가상 토큰명
`color-brand`, `space-1` 같은 이름은 어떤 사이트에도 없다. 실제는 `--hds-color-core-brand-600`, `--ds-space-200` 등 prefix-scoped.

## 2. 브랜드 키트 ≠ UI 색
로고 5색(Figma, Slack)은 일러스트/로고 전용. 실제 UI는 전혀 다른 색을 쓴다.

## 3. 리브랜딩 지체
Atlassian `#0052CC` → `#1868DB`, Prisma indigo → teal, Retool orange → cream/bordeaux. 구 브랜드 hex가 소수만 남아있을 수 있다.

## 4. Light/Dark 역전
Warp 마케팅 사이트는 light(cream). 터미널 앱 ≠ 마케팅 사이트.

## 5. 앱 UI vs 마케팅 레이어 혼동
Linear, Framer, GitHub은 앱 내부와 마케팅 사이트가 다른 팔레트.

## 6. Hero 구체 수치 필수
"spacious feel" 같은 추상 서술 금지. clamp font-size, gradient angle, overlay opacity 등 수치 명시.

## 7. DS 네임스페이스 보존
`--hds-*`, `--ds-*`, `--framer-*` 등 실제 prefix 유지. 일반화 금지.

## 8. Tailwind v4 `@theme`
`--tw-*`, `--spacing: .25rem`, `--color-*-NNN` 시그너처 감지. v3과 다름.

## 9. next/font metric fallback
`Inter Fallback`, `Mona Sans Header Fallback` 등 layout-shift 방지 폰트. 모든 Next.js 사이트에 있음.

## 10. Warm vs Cool neutral
Notion `#37352F`(warm ink), Retool `#E9EBDF`(cream) — 순흑/순백 아님. 색온도가 브랜드 핵심.

## 11. Multi-layer shadow
Stripe 2-layer, GitHub 5-layer, Linear 5-layer. 단층 box-shadow로 환원하면 깊이 무너짐.

## 12. Customer logo wall 오염
"trusted by" 섹션의 SVG 로고 hex가 frequency top에 침투. 필터링 필요.

## 13. Letter-spacing optical compensation
큰 headings의 negative tracking: `-0.01em` (md~xl), `-0.02em` (xxl). 없으면 "풀어진" 느낌.

## 14. Variable font 비표준 weight
Saans `300/380/570`, ShopifySans `330/420/550`. 일반 Inter로 재현 불가.
