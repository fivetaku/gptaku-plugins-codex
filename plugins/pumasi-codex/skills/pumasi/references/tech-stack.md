# 모던 기술스택 기본 원칙

lead agent가 instruction을 작성할 때, 항상 최신 안정 버전 기준으로 기술을 선택한다.

## 2025-2026 기준 모던 스택

| 영역 | 추천 (최신) | 피해야 할 것 |
|------|------------|-------------|
| 프론트엔드 | React 19, Vue 3.5+, Svelte 5 | React 18 이하 |
| 빌드 | Vite 6+, Turbopack | Vite 5 이하, Webpack |
| CSS | Tailwind 4, CSS Modules | Tailwind 3 이하 |
| 백엔드 | Hono, Elysia, Express 5 | Express 4 |
| 런타임 | Bun, Node 22+ | Node 18 이하 |
| ORM/DB | Drizzle ORM, better-sqlite3 | Sequelize, TypeORM |
| TypeScript | 5.8+ | 5.3 이하 |
| 패키지매니저 | bun, pnpm | npm (가능하면) |
| 테스트 | Vitest | Jest (Vite 프로젝트에서) |
