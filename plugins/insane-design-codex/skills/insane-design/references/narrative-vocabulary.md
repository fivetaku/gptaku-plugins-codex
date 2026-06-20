# Narrative Vocabulary Catalog (v3.3)

§00 Narrative와 §13-3 Signature Micro-Specs에서 사이트 정체성을 살리는 metaphor 어휘 가이드. 71 getdesign.md ref 분석 (2026-05-03) 기반.

## 사용법

§00 narrative 작성 시 **archetype 식별 → 해당 archetype의 top metaphor에서 최소 1개 + 보편 어휘에서 최소 2개** 결합. 총 3+ metaphor 사용이 floor.

generic 형용사("절제된 / 모던한 / 미니멀한 / 세련된")만으로 끝내는 문장 금지. 사이트 archetype에 맞는 공간/도구/매체 metaphor로 정체성 anchoring.

## Archetype별 Top Metaphor

### saas-marketing (8 ref sites — vercel, supabase, neon, resend, clerk, frame, github 등)
- **Top:** accent(66), canvas(50), editorial(16), terminal(15), parchment(13), magazine(12), console(12)
- **Signature:** terminal / console / parchment — 코드 친화 + 문서 톤
- **Pattern:** "X's marketing surface is [color] canvas holding [type] in [layout grid]"
- **Sample first sentence:** "Vercel은 monochrome canvas 위에 terminal-grade typography를 깔고, accent를 keyword로만 sprinkle한다"

### ai-products (6 ref sites — openai, anthropic, runway, midjourney 등)
- **Top:** canvas(80), editorial(34), accent(31), runway(11), magazine(8), gallery(8), terminal(6)
- **Signature:** runway / gallery / canvas — 작품 진열 + 무대 호출
- **Pattern:** "X reads like [a/an] [editorial/gallery/runway] for [model output]"
- **Sample first sentence:** "Midjourney는 runway 위 작품을 walking spotlight로 비추는 gallery"

### app-dashboard (4 ref sites — notion, figma, linear-app 등)
- **Top:** canvas(45), accent(24), editorial(11), rhythm(8), dashboard(4), monochrome(2)
- **Signature:** canvas + dashboard + rhythm — 작업대 + 진행감
- **Pattern:** "X is [a/an] [working canvas / dashboard cockpit] where [user action] feels [sensation]"

### editorial-product (apple, nothing 등 럭셔리 제품)
- **Top:** canvas(27), store(22), parchment(20), rhythm(6), accent(5), gallery(2), museum(2)
- **Signature:** parchment / store / museum — 진열 + 박물관 권위
- **Pattern:** "X is a museum-grade store where [product] sits like [artifact]"
- **Sample first sentence:** "Apple은 product를 museum artifact처럼 진열하고 parchment 같은 typography로 설명문을 깐다"

### automotive (5 ref sites — ferrari, bmw, tesla, porsche 등)
- **Top:** canvas(122), editorial(34), accent(19), magazine(11), rhythm(8), gallery(5), studio(4)
- **Signature:** showroom / gallery / cockpit — 진열 + 운전석
- **Pattern:** "X stages [vehicle] like a [showroom hero / cockpit blueprint]"

### fintech-payment (4 ref sites — stripe, ramp, mercury 등)
- **Top:** canvas(30), accent(30), editorial(11), rhythm(5), dashboard(5), exchange(1), spreadsheet(1)
- **Signature:** dashboard / spreadsheet / exchange — 신뢰 + 정밀
- **Pattern:** "X reads like [a/an] [trading floor / ledger / exchange] rendered in [type]"

### commerce-marketplace (uniqlo, zara, nike 등)
- **Top:** accent(12), canvas(2), editorial(1), store(1), magazine(1), cathedral(1), theatre(1)
- **Signature:** marketplace / store / boutique — 매장 정체성
- **Pattern:** "X turns [product] into [marketplace stalls / theatre acts]"

### editorial-magazine (medium, substack 등)
- **Top:** editorial(17), accent(6), canvas(2), magazine(2), rhythm(1), broadsheet(1)
- **Signature:** broadsheet / editorial / magazine — 신문 권위
- **Pattern:** "X is a [broadsheet / magazine] in browser form"

### travel-hospitality (airbnb, booking 등)
- **Top:** canvas(22), editorial(7), marketplace(7), accent(4), magazine(1)
- **Signature:** marketplace / canvas — 호스트/게스트 양방향
- **Pattern:** "X is a marketplace where [host content] becomes [editorial spreads]"

### entertainment (spotify, netflix 등)
- **Top:** accent(4), magazine(1), theater(1)
- **Signature:** theater / stage / concert-hall

## 보편 어휘 (모든 archetype 공용 — 보강용)

| 카테고리 | 어휘 |
|---------|------|
| 공간 | canvas, gallery, museum, theatre, stage, arena, atelier, studio, lab, workshop, lounge, library, archive |
| 매체 | editorial, magazine, broadsheet, parchment, manuscript, blueprint, specification, ledger, chronicle |
| 도구 | terminal, console, dashboard, cockpit, spreadsheet, instrument |
| 진열 | showroom, showcase, vitrine, shelf, boutique, store, marketplace |
| 행위 | rhythm, masterclass, runway, exchange |

## First-Sentence 패턴 5종 (ref 빈도 순)

1. **"X is the canonical example of [archetype/space]"** — 정체성 선언형
   - 예: "Linear is the canonical example of editorial saas marketing"

2. **"X reads like [persona/space]"** — 비유 직접 호출형
   - 예: "Stripe reads like a ledger rendered in browser-grade typography"

3. **"X's [surface/marketing surface] is [color] canvas holding [type] in [layout]"** — 구조형
   - 예: "Vercel's marketing surface is monochrome canvas holding terminal-grade type in 12-col grid"

4. **"X is a masterclass in [signature]"** — 찬사형 (sparingly)
   - 예: "Apple is a masterclass in product-as-artifact museography"

5. **"X stages [object] like [stage metaphor]"** — 무대 호출형
   - 예: "Ferrari stages each model like a showroom hero with cinematic gradient backdrops"

## Negative Constraints (다시 금지)

§00 narrative에서 **사용 금지**:

- "절제된 / 차가운 / 모던한 / 세련된 / 미니멀한" 형용사로만 끝나는 문장
- "premium / clean / elegant / refined / sophisticated" 영문 일반 형용사로만 끝나는 문장
- archetype과 무관한 보편 도구 metaphor 단독 사용 (예: editorial-magazine 사이트에 "cockpit" 단독)
- 빈도 1 metaphor를 main signature로 채택 (해당 archetype에서 ref 빈도 ≥3 어휘 우선)

## Aesthetic Anchoring 적용 예시

**Bad (generic-only):**
> "이 사이트는 절제된 모노크롬 미니멀리즘으로 모던하고 세련된 인상을 준다."

**Good (archetype + boundary):**
> "Vercel은 monochrome canvas 위에 terminal-grade typography를 깔고, weight 700/regular 두 톤만으로 rhythm을 만든다. accent는 keyword 근처에만 sprinkle되고, **두 번째 brand color는 존재하지 않는다**."

핵심 차이: archetype 어휘(canvas, terminal-grade, rhythm) 3개 + Negative-Space 정체성 ("두 번째 brand color는 존재하지 않는다") 1개.
