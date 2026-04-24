# Fallback Strategies for Technologies Without llms.txt

When a technology doesn't have llms.txt, use these strategies in order.

## Strategy Priority

```
1. Per-technology lookup → known best strategy for specific tech (40+ mapped)
2. GitHub raw markdown → docs/ folder direct fetch (most reliable for OSS)
3. sitemap.xml → URL list parsing → docs pattern filter → WebFetch
4. Platform-specific signals → MkDocs search_index / Sphinx objects.inv
5. Package registry API → docs URL extraction
6. WebSearch → official site direct fetch (last resort)
```

> GitHub raw MD가 platform detection보다 우선입니다. 플랫폼 감지는 Hugo 등에서 실패율이 높지만(테스트 3/8), GitHub MD는 거의 모든 오픈소스에서 작동합니다.

---

## Doc Hosting Platform Detection

Before per-technology lookup, check if the doc site uses a known hosting platform.
This single check can cover hundreds of technologies automatically.

### Detection Order

1. **HTTP headers**: `X-Llms-Txt` header → **Mintlify** (auto llms.txt)
2. **Try `/llms.txt`**: If 200, use it (Mintlify, GitBook, ReadTheDocs all auto-generate)
3. **Meta generator tag**: `<meta name="generator" content="...">` → Docusaurus, Sphinx, VitePress
4. **Probe known files**:
   - `/objects.inv` → **Sphinx**
   - `/search/search_index.json` → **MkDocs**
   - `/searchindex.js` → **Sphinx**
   - `/_pagefind/pagefind.js` → **Nextra**
5. **Domain pattern**: `*.readthedocs.io`, `*.gitbook.io`
6. **Footer text**: "Powered by GitBook", "Built with MkDocs", "Built with Sphinx"
7. **Fallback**: `/sitemap.xml` (nearly universal)

### Platform Strategies

| Platform | Detection | llms.txt | Best Fetch Strategy |
|----------|-----------|:--------:|---------------------|
| **Mintlify** | `X-Llms-Txt` header | Auto | `/llms.txt` or send `Accept: text/markdown` on any page |
| **GitBook** | "Powered by GitBook" footer | Auto (since Jan 2025) | `/llms.txt` or append `.md` to any page URL |
| **ReadTheDocs** | `*.readthedocs.io` domain | Via config | `/llms.txt` → `/sitemap.xml` → Embed API |
| **Docusaurus** | `<meta generator="Docusaurus">` | Plugin only | `/sitemap.xml` (always present in preset-classic) |
| **MkDocs/Material** | `md-*` CSS classes, footer | Plugin only | `/search/search_index.json` (contains ALL page text!) |
| **Sphinx** | `/objects.inv` exists | Plugin only | `/objects.inv` + `/searchindex.js` |
| **VitePress** | `<meta generator="VitePress">` | No | `/sitemap.xml` (with config) |
| **Nextra** | `/_next/static/` + `/_pagefind/` | No | `/sitemap.xml` or `__NEXT_DATA__` JSON |

> **Note: Hugo sites are undetectable** — Hugo does not inject meta tags, footer text, or other detectable signals. Sites like grpc.io, grafana.com use Hugo but cannot be auto-detected. For Hugo sites, skip platform detection and go straight to sitemap.xml or GitHub source.

### Mintlify Sites (auto llms.txt)

Many API-focused companies use Mintlify which auto-generates llms.txt:
ChromaDB, Pinecone, Anthropic, Replit, Coinbase, Resend, Loops, etc.
→ Always try `/llms.txt` first on `docs.*` subdomains.

### MkDocs Search Index (hidden gem)

`/search/search_index.json` contains full text of every page:
```json
{"docs": [{"location": "page/", "title": "Page Title", "text": "Full page content..."}]}
```
Used by: FastAPI, Pydantic, Traefik, and many Python projects.

---

## Per-Technology Best Strategies

### Backend Frameworks

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| FastAPI | sitemap.xml (160 URLs) | https://fastapi.tiangolo.com/sitemap.xml |
| Express | sitemap.xml | https://expressjs.com/sitemap.xml |
| NestJS | GitHub raw MD | https://github.com/nestjs/docs.nestjs.com/tree/master/content |
| Spring Boot | GitHub AsciiDoc | https://github.com/spring-projects/spring-boot/tree/main/spring-boot-project/spring-boot-docs |
| Ruby on Rails | GitHub raw MD (81 files) | https://github.com/rails/rails/tree/main/guides/source |
| Laravel | GitHub raw MD (103 files) | https://github.com/laravel/docs |
| Flask | GitHub RST + sitemap | https://github.com/pallets/flask/tree/main/docs |

### Databases

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| PostgreSQL | sitemap.xml + version URL pattern | https://www.postgresql.org/docs/{version}/ |
| MySQL | Download HTML zip | https://downloads.mysql.com/docs/ |
| SQLite | HTML doc index (213 pages) | https://www.sqlite.org/doclist.html |

### Vector / Graph Databases

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| FAISS | GitHub Wiki (no sitemap) | https://github.com/facebookresearch/faiss/wiki |
| LanceDB | GitHub MD + sitemap | https://github.com/lancedb/documentation |
| ArangoDB | GitHub MD (Hugo) | https://github.com/arangodb/docs-hugo |

> ChromaDB, Pinecone, Weaviate, Milvus, Neo4j는 llms.txt 보유 → llms-txt-sites.md 참조

### Message Queues

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Apache Kafka | sitemap.xml (1000+ URLs) | https://kafka.apache.org/sitemap.xml |
| RabbitMQ | GitHub MDX (Docusaurus) | https://github.com/rabbitmq/rabbitmq-website |

> NATS는 llms.txt 보유 → llms-txt-sites.md 참조

### Search Engines

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Elasticsearch | GitHub source (⚠️ version branch) + sitemap | https://github.com/elastic/elasticsearch/tree/8.17/docs |

> **Elasticsearch 주의**: docs가 `main` 브랜치에 없음. `8.17` 등 버전 브랜치를 사용해야 함. 파일 형식은 AsciiDoc.
| OpenSearch | GitHub MD (Jekyll) | https://github.com/opensearch-project/documentation-website |

### Monitoring / Observability

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Prometheus | GitHub MD | https://github.com/prometheus/docs |
| Grafana | GitHub MD + sitemap index (13 sub-sitemaps) | https://grafana.com/docs/grafana/latest/ |

### Caching / Proxy

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Nginx | WebFetch (⚠️ GitHub repo ≠ 공식 문서) | https://nginx.org/en/docs/http/ngx_http_proxy_module.html |

> **Nginx 주의**: `nginx/documentation` GitHub repo는 NGINX Plus 상용 문서만 포함. 오픈소스 Nginx 문서는 `nginx.org/en/docs/`에서 직접 WebFetch.
| Traefik | GitHub MD (MkDocs) + sitemap | https://github.com/traefik/traefik/tree/master/docs |

### ML / Data Science

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| pandas | GitHub RST (Sphinx) | https://github.com/pandas-dev/pandas/tree/main/doc/source |
| NumPy | GitHub RST (Sphinx) | https://github.com/numpy/numpy/tree/main/doc/source |
| scikit-learn | GitHub RST (Sphinx) | https://github.com/scikit-learn/scikit-learn/tree/main/doc |
| PyTorch | GitHub RST (primary, ⚠️ site is JS-heavy) | https://github.com/pytorch/pytorch/tree/main/docs/source |

> **PyTorch 주의**: pytorch.org는 JS 렌더링이 무거워 WebFetch로 내용 추출 실패 가능. GitHub RST 소스를 우선 사용.
| TensorFlow | GitHub MD + sitemap index | https://github.com/tensorflow/docs |
| Hugging Face | GitHub MD + sitemap (`sitemap-doc.xml`) | https://huggingface.co/docs |

### Auth / Identity

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Auth.js (NextAuth) | GitHub MD + sitemap (500+ URLs) | https://github.com/nextauthjs/next-auth/tree/main/docs |
| Keycloak | GitHub AsciiDoc + sitemap | https://github.com/keycloak/keycloak/tree/main/docs/documentation |
| Firebase Auth | GitHub MD + sitemap index | https://github.com/firebase/firebase-docs |

> Auth0는 llms.txt 보유 → llms-txt-sites.md 참조

### API / Protocol

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| gRPC | GitHub MD (Hugo) + sitemap | https://github.com/grpc/grpc.io/tree/main/content/en/docs |
| Swagger/OpenAPI | GitHub MD (Starlight/Astro) | https://github.com/swagger-api/swagger.io-docs |

### Frontend

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Tailwind CSS | GitHub MDX (194 files) | https://github.com/tailwindlabs/tailwindcss.com/tree/main/src/docs |

### Mobile

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| SwiftUI | WebFetch only (Apple closed docs) | https://developer.apple.com/documentation/swiftui |
| Jetpack Compose | sitemap.xml (Google DevSite) | https://developer.android.com/sitemap.xml |

### DevOps / Infra

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Kubernetes | sitemap.xml OR GitHub | https://kubernetes.io/sitemap.xml |
| Terraform | GitHub + Registry API | https://registry.terraform.io/v1/providers/ |

### Testing

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Playwright | sitemap.xml (400+ URLs) | https://playwright.dev/sitemap.xml |
| Jest | sitemap.xml (230+ URLs) | https://jestjs.io/sitemap.xml |
| pytest | sitemap.xml + GitHub RST | https://docs.pytest.org/sitemap.xml |

### Code Quality

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| ESLint | sitemap.xml (600+ URLs) | https://eslint.org/sitemap.xml |
| Biome | sitemap index | https://biomejs.dev/sitemap-index.xml |

### State Management

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| Redux | sitemap.xml (97 URLs) | https://redux.js.org/sitemap.xml |
| Zustand | GitHub docs folder | https://github.com/pmndrs/zustand/tree/main/docs |

### Other

| Tech | Best Strategy | Key URL |
|------|--------------|---------|
| GraphQL | GitHub source (Nextra) | https://github.com/graphql/graphql.github.io/tree/main/src |
| Webpack | sitemap.xml (327 URLs) | https://webpack.js.org/sitemap.xml |
| Flutter | sitemap.xml (1000+ URLs) | https://docs.flutter.dev/sitemap.xml |

---

## Alternative Machine-Readable Formats

### sitemap.xml
Most useful fallback. Parse XML to get URL list, filter for `/docs/` pattern, then WebFetch individual pages.

### GitHub Raw Content
For open-source projects, fetch markdown directly:
```
https://raw.githubusercontent.com/{owner}/{repo}/main/docs/{file}.md
```

**Branch fallback order**: `main` → `master` → version branches (e.g., `8.17`, `v3.x`)
**Common doc paths**: `docs/`, `doc/`, `content/`, `website/docs/`, `src/docs/`

### Package Registry APIs
- **PyPI**: `https://pypi.org/pypi/{package}/json` → extract `info.project_urls.Documentation`
- **npm**: `https://registry.npmjs.org/{package}/latest` → extract `homepage` field
- **RubyGems**: `https://rubygems.org/api/v1/gems/{gem}.json`

### OpenAPI/Swagger Specs
For REST APIs, check:
- `{site}/openapi.json`
- `{site}/swagger.json`
- `{site}/api-docs`

---

## Error Recovery Strategies

### 404 Recovery
1. Strip `.md` extension → retry (React 등 llms.txt에서 .md URL 제공하지만 실제 페이지는 확장자 없음)
2. Try parent path → table of contents 탐색 (`/docs/v1/intro` → `/docs/v1/`)
3. GitHub branch fallback → `main` 404시 `master`, 버전 브랜치 시도

### JS-rendered sites (WebFetch 실패)
- `developer.apple.com`, `docs.oracle.com` 등 SPA 사이트
- 대안: GitHub 소스 우선, 없으면 내부 지식으로 답변 + 공식 URL 제공

### Version branch mapping
일부 프로젝트는 docs를 버전 브랜치에 보관:
- Elasticsearch: `8.17` 브랜치
- Django: `stable/5.0.x` 브랜치
- 프로젝트 context (package.json 등)에서 버전 감지 후 매핑
