# 산출 문서 만들기 (있어빌리티)

## 원칙

- 산출물은 "그 조직의 서식"이다. 일반 요약문보다 결재 양식·일지·대장 모양이 사무직에게 와닿는다.
- 문장은 코드 템플릿이 만든다. Jev는 칸에 들어갈 값(갈래·여부·단계)만 낸다. 같은 판정이면 같은 문서가 나와야 결재에 올릴 수 있다.
- 모르는 칸은 비운다. 지어내지 않는다. 비운 칸을 화면·문서에 표시하면 신뢰가 오른다.
- 사람이 문구를 고치면 그 문구를 다음 회차 템플릿에 얹는다(patrol-jev `report.ts` `Wording`).
- 미리보기 표에서 칸마다 출처를 밝힌다: [J] Jev 값 · [C] 코드 계산 · [원] 받아 적은 원문 · [사람] 사람 몫. 실제 화면에서는 색으로 나눈다(patrol-jev: Jev 값만 무지개, 나머지 회색).

## hwpx (한글 파일) — patrol-jev 생성기 재사용

원본: https://github.com/patrol-jev/patrol-jev `src/core/hwpx/` (MIT, 커밋 3051c3d8). 클론해 필요한 파일만 복사해 쓰고, MIT 고지를 함께 둔다.

- 작성자가 2026-10-14 커밋 3051c3d8 복사본에서 check-hwpx 62/62, check-period 81/81 통과를 확인했다. 의존은 fflate 0.8.3 하나.
- 그대로 쓰는 것: `packHwpx`(`package.ts:75`, zip 순서·무압축 mimetype), `buildSection`(`section.ts:203`, A4·여백), `esc`/`tag`(`xml.ts`).
- 표: `table()`(`section.ts:99`) + `Cell`(`section.ts:29-45`)의 `colSpan`/`rowSpan`/`fill`. 병합으로 덮인 칸은 body에 적지 않는다(`section.ts:88`). 합계 행·항목 행은 이것으로.
- 결재란: 전용 함수 없음. `table()`로 새로 짠다(`Table.para` 오른쪽 정렬 `head.ts:31`).
- 새 양식은 `ilji.ts:77-111` 흐름을 본떠 빌더 하나(예: `expense.ts`)를 새로 쓴다. 글자 모양이 더 필요하면 `head.ts`의 `CHAR`/`PARA` 번호표와 `charPr` 목록을 함께 고친다.
- 사진 칸: `photoTable`(`photos.ts:42`). 테두리를 다 등록한 뒤 그림 채움을 등록한다(순서 어긋나면 `ilji.ts:108` 예외).
- 지뢰: 셀 크기는 정수 HWPUNIT(`ilji.ts:28`). `hp:linesegarray`는 적지 않는다(손상 문서 원인, `section.ts:7`).
- 미확인: 맥 한글 Viewer에서 1쪽 본문 표가 2쪽으로 밀림(원본 산출물도 같음, 원인 미확정 — 폰트 대체 추정). 윈도 한글에서는 열어 보지 않았다. 시연 전에 대상 PC 한글에서 한 번 열어 본다.

## 다른 출력

- xlsx: 표 중심 대장·집계는 xlsx가 편하다(anthropic-skills:xlsx).
- 보드·알림: 메일 보드, 슬랙 브리프는 문서 대신 칸·메시지로.
- 화면: 확률 막대·출처 색을 그대로 보여 주는 화면이 시연에서 효과적이다(patrol-jev 무지개/회색 규칙).
