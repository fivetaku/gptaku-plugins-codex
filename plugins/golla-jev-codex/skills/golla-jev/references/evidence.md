# 근거 수치 (여기 없는 수치는 제안에 쓰지 않는다)

## 작성자 실측 (재측정 2026-11-13, jev-1.14.0 — 모델이 바뀌면 다시 잰다. 원 실험 10-14 수치는 `bench/REPORT.md`)

| 항목 | 값 | 출처 |
|---|---|---|
| 한국어 사무 108문항, 질문·보기 한국어 | 208/216 (96.3%) | R3 재측정 `bench/REPORT.md` |
| 같은 문항, 질문·보기 영어 | 202/216 (93.5%) | R3 |
| Choice 6건 묶음(경로 지정) | 132/136 (97.1%) | R3 |
| Choice 보기 순서 뒤집기로 바뀐 문항 | 0/68 | R3 |
| 반복 일치 | 108/108 | R3 |
| 단건 지연 p50 / p90 | 205 / 241 ms | R3 (HTTP 왕복) |
| 6건 묶음 한 요청 p50 | 203 ms | R3 |
| 문턱 0.70 (dev에서 고름) holdout 자동 처리 | 57/59 (97%), 자동 처리 중 오답 0 | R3 `results/threshold-sweep.txt`, 오답 0 규칙 (원 실험은 0.85에서 54/59). `summary.json`의 0.52는 정밀도 97% 목표 규칙이라 다르다 |
| 확실도 0.95 이상 / 0.80~0.95 / 0.80 미만 | 170/170 · 31/31 · 7/15 | R3 |

## 공식 문서 (확인일 2026-11-13, 바뀔 수 있음 — 쓰기 전에 다시 읽는다)

- 모델 `jev-1.14.0`(`jev-latest`·`jev-preview` 모두 이 버전), 입력 $0.042/1M 토큰, 출력 무료. 입력은 텍스트와 PNG·JPEG 이미지. https://docs.typesafe.ai/models.md
- 이미지·Box 질문은 "Dreamer-ready"(운영 준비 전)이고 요청마다 `TypeSafe-Danger-Zone-Images: true` 헤더가 필요하다. 형식·정확도가 릴리스마다 바뀔 수 있다. https://docs.typesafe.ai/images.md
- 사진에서 읽은 값을 Jev로 다시 확인하는 공식 레시피: OCR confidence and bounding boxes. https://docs.typesafe.ai/cookbooks/ocr_confidence_bounding_boxes.md
- 요청당 64k 토큰, state+가장 긴 질문 32k. 영어가 주 언어, CJK는 같지 않음.
- 약점: 문자 그대로 읽기·숫자 세기·날짜 비교·다단계 참조·큰 무관 state·적대적 텍스트·지시 모순·질문 간 불변식·글 생성, 보기 순서 편향. https://docs.typesafe.ai/model-jaggedness/jev-1.13.md ("Jev is not a calculator", 개수 세기·날짜 비교는 코드로)

## 외부 사례 (저자 보고, 재현 안 함)

| 사례 | 수치 | 출처 |
|---|---|---|
| GC AI 12시간 해커톤 | 38개 시도·23개 제출. 약관 함정 F1 89%(정규식 57%), 온콜 알림 136건 오경보 1, 받은편지함 26/26, 배열 96%→72% | https://gc.ai/blog/what-we-learned-building-38-projects-with-jev-in-12-hours (2026-10-06, 직접 확인) |
| Jack & Jill 채용 선별 | 1,000명당 $0.755→$0.092, 처리 20.3→10.3초, 10일 만에 운영 | https://typesafe.ai/blog/jack-jill-jev-case-study |
| You.com + Jev 뉴스 브리프 | 674기사 8주, 잘못 게시 22/60→5/39, 기사당 약 $0.00004 | https://github.com/youdotcom-oss/n8n-ai-brief-workflow |
| 보니야 육아 앱(한국어) | 182문항 Haiku 178 → Jev 179, 판단 p50 1,523ms→약 0.2초(가상 데이터) | https://brunch.co.kr/@6280ce27834d483/86 (2026-10-01) |
| patrol-jev 순찰일지 | 30장 25초, 주소 대조 5/9→9/9, 평균 대신 최강 1장 라벨로 모르겠음 9/10 해소 | https://github.com/patrol-jev/patrol-jev 저자 문서 |
| 피싱 판정 | Jev 단독 62.6%, 신호 5개 회귀 95.0%, Haiku 81.3% | https://github.com/fivetaku/awesome-jev-study `ko/projects/454-jev-phishing-bench.md` |
| 라우팅 손해 | codex-jev-router 단일 에이전트 대비 +69.7% 비용, 라우터 철회 | https://github.com/suenot/codex-jev-router (코드 읽기) |
| 피지컬 AI 판단 주기 | 드론 제어 약 500Hz · Jev 약 2.5Hz, 쌍팔 로봇 응답 약 500ms, Doom 초당 약 10회 · 시간당 약 $7, Tetris 한 수 약 0.3초 | https://github.com/fivetaku/awesome-jev-study `ko/projects/` 193·318·319·410 |
| 사진 → 글(비전 LLM) 속도 | 장당 중앙값 4,170ms, Jev 판정은 258ms | patrol-jev `docs/guide.md:316-317` |
| Made with Jev 집계 | 결정당 중앙 비용 $0.000065, 중앙 지연 300ms | https://madewithjev.com/jev-use-cases |

## 경쟁·대체 결정 모델 (2026-10 기준, 참고만)

Microsoft Decision-1, Cloudflare Clef(이미지·오디오 state 지원), OpenAI Decisions, 로컬 THX-01·Dex. 이미지 앞단을 없애고 싶을 때 Clef가 후보지만 한국어 실측은 없다.
