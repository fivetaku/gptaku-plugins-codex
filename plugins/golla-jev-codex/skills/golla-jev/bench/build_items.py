"""R3 한국어 사무 워크플로 벤치 문항 생성. 정답(gold)은 설계자가 실행 전에 정하고 lock.txt 에 해시를 남긴다.

워크플로 5종(W1 영수증 · W2 메일 · W3 회의 · W4 만족도 · W5 계약)은 「사진·녹음·메일 → 받아 적기 → Jev → 양식」에서
Jev 가 받는 글(앞단이 받아 적었다고 가정한 텍스트)을 손으로 쓴 것이다. 실제 고객 자료가 아니다.
"""
import hashlib, json, pathlib

ROOT = pathlib.Path(__file__).parent

WF = {}

# ── W1 영수증 비목 (Choice) ─────────────────────────────────────────────
WF['w1_cat'] = dict(
    type='choice',
    ko='이 영수증은 지출결의서의 어느 비목으로 처리해야 하는가? `receipt`(영수증에서 읽은 글자)와 `memo`(사용자가 적은 용도)를 함께 보고 판단하라.',
    en='Which expense category on an expense report should this receipt be filed under? Judge from `receipt` (text read off the receipt) and `memo` (the purpose the user wrote).',
    options={
        'meeting': ('회의비', '회의·간담회·외부 손님 접대에 쓴 다과·식사', 'meeting', 'Refreshments or meals for a meeting, workshop or visiting guests.'),
        'meal': ('식대', '직원 본인들의 끼니(야근 식대 포함)', 'staff_meal', 'Meals for the staff themselves, including overtime meals.'),
        'travel': ('여비교통비', '택시·기차·버스·주유·통행료·주차 등 이동 비용', 'travel', 'Transport: taxi, train, bus, fuel, tolls, parking.'),
        'supplies': ('소모품비', '사무용품·전산 소모품·청소용품 등', 'supplies', 'Office supplies, printer consumables, cleaning goods.'),
        'print': ('도서인쇄비', '도서 구입·인쇄·제본·출력 비용', 'books_printing', 'Buying books, printing, binding, copy-shop output.'),
        'none': ('해당 없음', '개인 지출이거나 업무 용도가 불분명함', 'none_of_these', 'Personal spending or no clear business purpose.'),
    },
    items=[
        ('r01', {'receipt': '스타벅스 역삼점 / 아메리카노 T 4 / 카페라떼 T 2 / 합계 27,600', 'memo': '거래처 미팅 다과'}, 'meeting'),
        ('r02', {'receipt': '카카오T 택시 / 서울역 → 강남구청 / 18,400원', 'memo': '교육 장소 이동'}, 'travel'),
        ('r03', {'receipt': 'GS25 / A4용지 2박스 / 볼펜 12입 / 포스트잇 / 46,300', 'memo': '사무실 비품'}, 'supplies'),
        ('r04', {'receipt': '코레일 승차권 / KTX 서울-대전 / 왕복 2매 / 47,800', 'memo': '고객사 출강'}, 'travel'),
        ('r05', {'receipt': '김밥천국 / 라면 3 / 김밥 3 / 22,500 / 21:40', 'memo': '야근 저녁'}, 'meal'),
        ('r06', {'receipt': '종로 인쇄소 / 교안 컬러 출력 40부 / 스프링 제본 / 132,000', 'memo': '교육 교재'}, 'print'),
        ('r07', {'receipt': '교보문고 / 「데이터 분석 입문」 외 2권 / 61,200', 'memo': '팀 스터디 도서'}, 'print'),
        ('r08', {'receipt': 'SK에너지 / 휘발유 38.2L / 68,000', 'memo': '현장 방문 차량 주유'}, 'travel'),
        ('r09', {'receipt': '쿠팡 / HP 정품 토너 206A 세트 / 189,000', 'memo': '프린터 토너 교체'}, 'supplies'),
        ('r10', {'receipt': '올리브영 / 선크림 / 립밤 / 31,000', 'memo': ''}, 'none'),
        ('r11', {'receipt': '한우마을 / 등심 4인 / 공기밥 4 / 248,000 / 19:10', 'memo': '고객사 담당자 3명과 계약 협의'}, 'meeting'),
        ('r12', {'receipt': '이마트24 / 생수 2L 12병 / 종이컵 1000입 / 물티슈 / 28,700', 'memo': '세미나실 비치용'}, 'supplies'),
        ('r13', {'receipt': '하이패스 통행료 / 서울TG-천안TG / 6,300', 'memo': '출장'}, 'travel'),
        ('r14', {'receipt': '파리바게뜨 / 샌드위치 15 / 음료 15 / 112,500', 'memo': '워크숍 참석자 점심 다과'}, 'meeting'),
        ('r15', {'receipt': '본죽 / 전복죽 1 / 12,000 / 12:30', 'memo': '점심'}, 'meal'),
        ('r16', {'receipt': '넷플릭스 / 프리미엄 월정액 / 17,000', 'memo': ''}, 'none'),
        ('r17', {'receipt': '킨코스 / 대형 현수막 출력 1 / 포스터 A1 2 / 85,000', 'memo': '교육 행사 현수막'}, 'print'),
        ('r18', {'receipt': '주차장 / 강남파이낸스센터 / 3시간 / 18,000', 'memo': '고객 방문'}, 'travel'),
    ])

# ── W1b 주류 포함 여부 (Noul) — 회의비 불인정 규정 확인용 ─────────────────────
WF['w1_alcohol'] = dict(
    type='noul',
    ko='`receipt` 의 품목 가운데 술(소주·맥주·와인·막걸리·하이볼 등 주류)이 하나라도 있는가?',
    en='Does any line item in `receipt` contain an alcoholic drink (soju, beer, wine, makgeolli, highball or similar)?',
    items=[
        ('a01', {'receipt': '한우마을 / 등심 4인 / 공기밥 4 / 참이슬 2 / 248,000'}, True),
        ('a02', {'receipt': '스타벅스 / 아메리카노 4 / 케이크 2 / 31,000'}, False),
        ('a03', {'receipt': '이자카야 하루 / 모둠 사시미 / 하이볼 3 / 생맥주 2 / 128,000'}, True),
        ('a04', {'receipt': '김밥천국 / 라면 3 / 김밥 3 / 콜라 1 / 24,500'}, False),
        ('a05', {'receipt': '전주식당 / 비빔밥 5 / 해물파전 1 / 막걸리 1 / 72,000'}, True),
        ('a06', {'receipt': '빕스 / 런치 샐러드바 4 / 에이드 2 / 무알콜 맥주 1 / 136,000'}, False),
        ('a07', {'receipt': '이탈리안 키친 / 파스타 3 / 피자 1 / 하우스 레드 와인 1병 / 154,000'}, True),
        ('a08', {'receipt': '본가 / 갈비탕 6 / 공기밥 추가 2 / 사이다 2 / 84,000'}, False),
    ])

# ── W2 메일 분류 (Choice) ─────────────────────────────────────────────
WF['w2_cat'] = dict(
    type='choice',
    ko='이 메일은 업무 보드의 어느 칸으로 보내야 하는가? `mail.subject` 와 `mail.body` 를 보고 판단하라. 인용된 이전 메일보다 새로 쓴 부분을 기준으로 한다.',
    en='Which column of the work board should this email go to? Judge from `mail.subject` and `mail.body`. Go by the newly written part, not the quoted earlier messages.',
    options={
        'edu': ('교육 문의', '강의·교육 개설, 커리큘럼, 강사 섭외 문의', 'training_inquiry', 'Asking about running a course, curriculum or booking an instructor.'),
        'deal': ('견적·계약', '견적 요청, 단가 협의, 계약서 검토·날인', 'quote_contract', 'Quote requests, price negotiation, contract review or signing.'),
        'bill': ('정산·세금계산서', '세금계산서 발행, 입금 확인, 정산 서류', 'billing', 'Tax invoices, payment confirmation, settlement paperwork.'),
        'sched': ('일정 조율', '날짜·시간·장소를 정하거나 바꾸는 일', 'scheduling', 'Setting or changing dates, times or venues.'),
        'spam': ('광고·스팸', '광고, 뉴스레터, 무작위 영업, 피싱', 'spam_ads', 'Ads, newsletters, cold sales pitches or phishing.'),
    },
    items=[
        ('m01', {'mail': {'subject': '하반기 신입사원 AI 교육 문의', 'body': '안녕하세요. 신입 40명 대상 생성형 AI 실무 교육을 11월에 진행하려 합니다. 커리큘럼과 강사 프로필을 받아볼 수 있을까요?'}}, 'edu'),
        ('m02', {'mail': {'subject': 'RE: 교육 견적', 'body': '보내주신 견적 잘 받았습니다. 1일 8시간 기준 단가를 조금 조정할 수 있을지 여쭙니다. 예산이 400만 원으로 잡혀 있어서요.'}}, 'deal'),
        ('m03', {'mail': {'subject': '10월 교육비 세금계산서 발행 요청', 'body': '10월 15일 교육 건 세금계산서 발행 부탁드립니다. 사업자등록증 첨부합니다. 담당자 이메일로 보내 주세요.'}}, 'bill'),
        ('m04', {'mail': {'subject': '다음 주 미팅 시간 변경 가능할까요', 'body': '수요일 오후 2시 미팅을 목요일 오전 10시로 옮길 수 있을지요? 장소는 그대로 저희 회의실입니다.'}}, 'sched'),
        ('m05', {'mail': {'subject': '[광고] 사무실 복합기 렌탈 특가', 'body': '월 2만 원대 복합기 렌탈! 지금 상담 신청 시 토너 무료. 수신 거부는 하단 링크.'}}, 'spam'),
        ('m06', {'mail': {'subject': 'RE: RE: 교육 커리큘럼', 'body': '커리큘럼 확인했습니다. 진행하는 걸로 하겠습니다. 계약서 양식 보내주시면 법무 검토 후 날인하겠습니다.\n\n> 커리큘럼 초안 첨부드립니다.\n> 교육 문의 감사합니다.'}}, 'deal'),
        ('m07', {'mail': {'subject': '입금 확인 부탁드립니다', 'body': '어제 오후 교육비 330만 원 입금했습니다. 확인되면 회신 부탁드려요.'}}, 'bill'),
        ('m08', {'mail': {'subject': '귀하의 계정이 일시 정지되었습니다', 'body': '보안 확인을 위해 아래 링크에서 비밀번호를 다시 입력하세요. 24시간 내 미확인 시 계정이 삭제됩니다.'}}, 'spam'),
        ('m09', {'mail': {'subject': '교육 장소 안내', 'body': '11월 20일 교육 장소가 본관 3층 대회의실에서 별관 1층 세미나실로 바뀌었습니다. 시간은 동일합니다.'}}, 'sched'),
        ('m10', {'mail': {'subject': '중소기업 대상 AI 바우처 교육 가능 여부', 'body': '저희가 AI 바우처 수요기업인데, 바우처로 임직원 교육을 받을 수 있는지, 가능하다면 어떤 과정이 있는지 궁금합니다.'}}, 'edu'),
        ('m11', {'mail': {'subject': 'RE: 일정', 'body': '말씀하신 12월 3일은 어렵고 12월 5일이나 10일이 가능합니다. 둘 중 편하신 날로 정해 주세요.\n\n> 12월 3일 어떠신가요?'}}, 'sched'),
        ('m12', {'mail': {'subject': '[뉴스레터] 이번 주 AI 트렌드 5가지', 'body': '구독해 주셔서 감사합니다. 이번 주에는 에이전트, 멀티모달, 결정 모델 소식을 모았습니다.'}}, 'spam'),
        ('m13', {'mail': {'subject': '거래명세서 및 통장 사본 요청', 'body': '정산 처리를 위해 거래명세서와 통장 사본을 보내 주시면 이번 달 말일에 지급하겠습니다.'}}, 'bill'),
        ('m14', {'mail': {'subject': '계약서 수정본 송부', 'body': '2조 지급 조건과 7조 해지 조항을 수정했습니다. 변경 내용 확인 부탁드립니다. 문제없으면 날인본 회신 주세요.'}}, 'deal'),
        ('m15', {'mail': {'subject': '감사 인사', 'body': '어제 교육 정말 유익했습니다. 직원들 반응이 좋아서 내년 상반기에 심화 과정도 하고 싶은데, 어떤 내용으로 구성할 수 있을지 제안 부탁드려요.'}}, 'edu'),
        ('m16', {'mail': {'subject': '귀사 전용 리드 1,000건 판매합니다', 'body': '교육 업계 담당자 연락처 DB를 저렴하게 제공합니다. 샘플 요청 환영.'}}, 'spam'),
    ])

# ── W2b 답장 필요 (Noul) ─────────────────────────────────────────────
WF['w2_reply'] = dict(
    type='noul',
    ko='이 메일을 받은 사람이 답장(회신·확인·자료 송부 등 행동)을 해야 하는가? `mail.body` 를 보고 판단하라. 단순 공지·감사·광고는 답장이 필요 없다.',
    en='Does the recipient of this email need to reply or act (respond, confirm, send something)? Judge from `mail.body`. Pure notices, thank-you notes and ads need no reply.',
    items=[
        ('p01', {'mail': {'body': '수요일 미팅을 목요일로 옮길 수 있을지 회신 부탁드립니다.'}}, True),
        ('p02', {'mail': {'body': '교육 장소가 별관 세미나실로 바뀌었습니다. 시간은 같습니다. 참고 바랍니다.'}}, False),
        ('p03', {'mail': {'body': '어제 교육 감사했습니다. 다음에 또 뵙겠습니다.'}}, False),
        ('p04', {'mail': {'body': '세금계산서를 담당자 이메일로 발행해 주세요. 사업자등록증 첨부합니다.'}}, True),
        ('p05', {'mail': {'body': '[광고] 복합기 렌탈 특가. 수신 거부는 하단 링크.'}}, False),
        ('p06', {'mail': {'body': '계약서 수정본 확인하시고 문제 없으면 날인본 보내 주세요.'}}, True),
        ('p07', {'mail': {'body': '입금 완료했습니다. 따로 회신 안 주셔도 됩니다.'}}, False),
        ('p08', {'mail': {'body': '커리큘럼 잘 받았습니다. 내부 검토 후 다음 주 중 연락드리겠습니다.'}}, False),
        ('p09', {'mail': {'body': '강사 프로필과 지난 교육 만족도 자료를 금요일까지 보내 주실 수 있을까요?'}}, True),
        ('p10', {'mail': {'body': '혹시 12월 5일 가능하시면 그날로 하고, 아니면 10일로 하겠습니다. 편하신 날 알려 주세요.'}}, True),
    ])

# ── W3 회의 발언 (Choice) ────────────────────────────────────────────
WF['w3_kind'] = dict(
    type='choice',
    ko='회의록에 이 발언을 어떻게 적어야 하는가? `utterance` 가 회의에서 한 말이고 `speaker` 가 말한 사람이다.',
    en='How should this remark be recorded in the meeting minutes? `utterance` is what was said in the meeting and `speaker` is who said it.',
    options={
        'decision': ('결정사항', '회의에서 무엇을 하기로 확정한 내용', 'decision', 'Something the meeting settled or agreed to do.'),
        'action': ('할 일', '특정 사람이 언제까지 무엇을 하겠다·하라는 배정', 'action_item', 'A task assigned to or taken by a specific person, often with a deadline.'),
        'discussion': ('논의', '의견·우려·질문·검토 중인 안건으로 아직 확정되지 않음', 'discussion', 'An opinion, concern, question or proposal still under discussion.'),
        'chitchat': ('잡담', '안건과 관계없는 인사·농담·사적인 이야기', 'small_talk', 'Greetings, jokes or personal talk unrelated to the agenda.'),
    },
    items=[
        ('u01', {'speaker': '팀장', 'utterance': '그럼 교육은 11월 20일 하루 과정으로 확정합시다.'}, 'decision'),
        ('u02', {'speaker': '김 대리', 'utterance': '제가 금요일까지 강의 자료 초안 만들어서 공유드리겠습니다.'}, 'action'),
        ('u03', {'speaker': '박 과장', 'utterance': '실습 시간이 너무 짧은 거 아닌가 싶어요. 참가자들이 따라오기 어려울 수도 있고요.'}, 'discussion'),
        ('u04', {'speaker': '이 주임', 'utterance': '어제 야구 보셨어요? 9회에 역전하더라고요.'}, 'chitchat'),
        ('u05', {'speaker': '팀장', 'utterance': '예산은 400만 원 안에서 집행하는 걸로 정리하죠.'}, 'decision'),
        ('u06', {'speaker': '팀장', 'utterance': '최 사원은 다음 주 화요일까지 장소 세 군데 견적 받아 와 주세요.'}, 'action'),
        ('u07', {'speaker': '김 대리', 'utterance': '온라인으로 하면 참석률이 더 높을까요, 아니면 오프라인이 집중이 잘 될까요?'}, 'discussion'),
        ('u08', {'speaker': '박 과장', 'utterance': '다들 점심 맛있게 드셨죠? 오늘 김치찌개 괜찮았어요.'}, 'chitchat'),
        ('u09', {'speaker': '팀장', 'utterance': '강사는 외부 전문가 대신 내부 인력으로 가기로 합니다.'}, 'decision'),
        ('u10', {'speaker': '이 주임', 'utterance': '설문 문항은 제가 이번 주 안에 정리해서 메일로 보낼게요.'}, 'action'),
        ('u11', {'speaker': '최 사원', 'utterance': '작년에는 만족도가 4.2였는데 올해도 비슷하게 나올지 모르겠네요.'}, 'discussion'),
        ('u12', {'speaker': '팀장', 'utterance': '자, 늦었으니 오늘은 여기까지 하고 다음 주에 이어서 보죠. 수고들 했어요.'}, 'chitchat'),
        ('u13', {'speaker': '박 과장', 'utterance': '그 부분은 법무팀 의견을 들어 봐야 할 것 같은데요.'}, 'discussion'),
        ('u14', {'speaker': '팀장', 'utterance': '좋습니다, 그럼 실습은 두 시간으로 늘리는 걸로 결정.'}, 'decision'),
        ('u15', {'speaker': '김 대리', 'utterance': '박 과장님, 법무팀 검토 요청은 과장님이 이번 주 수요일까지 넣어 주시는 걸로 할까요?'}, 'action'),
        ('u16', {'speaker': '최 사원', 'utterance': '와, 창밖에 눈 온다. 첫눈이네요.'}, 'chitchat'),
    ])

# ── W3b 할 일 담당자 (Choice, 참석자 명단에서) ─────────────────────────────
WF['w3_owner'] = dict(
    type='choice',
    ko='`utterance` 에서 일을 맡게 된 사람은 누구인가? 말한 사람(`speaker`)이 아니라 그 일을 실제로 하게 될 사람을 고른다.',
    en='Who ends up owning the task in `utterance`? Pick the person who will actually do the work, not necessarily the `speaker`.',
    options={
        'kim': ('김 대리', '김 대리', 'kim', 'Deputy Kim'),
        'park': ('박 과장', '박 과장', 'park', 'Manager Park'),
        'lee': ('이 주임', '이 주임', 'lee', 'Assistant Lee'),
        'choi': ('최 사원', '최 사원', 'choi', 'Staff Choi'),
        'none': ('담당자 없음', '맡은 사람이 정해지지 않음', 'nobody', 'No owner was named.'),
    },
    items=[
        ('o01', {'speaker': '김 대리', 'utterance': '제가 금요일까지 강의 자료 초안 만들어서 공유드리겠습니다.'}, 'kim'),
        ('o02', {'speaker': '팀장', 'utterance': '최 사원은 다음 주 화요일까지 장소 세 군데 견적 받아 와 주세요.'}, 'choi'),
        ('o03', {'speaker': '김 대리', 'utterance': '박 과장님, 법무팀 검토 요청은 과장님이 이번 주 수요일까지 넣어 주시는 걸로 할까요?'}, 'park'),
        ('o04', {'speaker': '이 주임', 'utterance': '설문 문항은 제가 이번 주 안에 정리해서 메일로 보낼게요.'}, 'lee'),
        ('o05', {'speaker': '팀장', 'utterance': '참가자 명단은 누가 좀 정리해 주면 좋겠는데요.'}, 'none'),
        ('o06', {'speaker': '박 과장', 'utterance': '그건 이 주임이 지난번에 해 봤으니까 이번에도 이 주임이 맡아 줘요.'}, 'lee'),
    ])

# ── W4 만족도 주관식 주제 (Choice) ───────────────────────────────────────
WF['w4_topic'] = dict(
    type='choice',
    ko='교육 만족도 설문의 이 주관식 응답(`answer`)은 주로 무엇에 대한 이야기인가?',
    en='What is this open-ended answer (`answer`) from a training satisfaction survey mainly about?',
    options={
        'instructor': ('강사', '강사의 설명·태도·전문성', 'instructor', "The instructor's explanations, attitude or expertise."),
        'content': ('내용', '교육 내용의 수준·유용성·구성', 'content', 'The level, usefulness or structure of the course content.'),
        'practice': ('실습', '실습 과제·실습 시간·실습 환경', 'hands_on', 'Hands-on exercises, practice time or practice setup.'),
        'venue': ('시설·환경', '장소·의자·냉난방·식사·주차', 'venue', 'Room, seating, temperature, food or parking.'),
        'schedule': ('시간·일정', '교육 시간 길이·시작 시각·휴식', 'schedule', 'Length of the session, start time or breaks.'),
    },
    items=[
        ('s01', {'answer': '강사님이 어려운 개념을 비유로 쉽게 풀어 주셔서 이해가 잘 됐어요.'}, 'instructor'),
        ('s02', {'answer': '실습 PC가 너무 느려서 따라가기가 힘들었습니다.'}, 'practice'),
        ('s03', {'answer': '강의실이 너무 추웠어요. 히터 좀 틀어 주세요.'}, 'venue'),
        ('s04', {'answer': '8시간은 너무 길어요. 이틀로 나누면 좋겠습니다.'}, 'schedule'),
        ('s05', {'answer': '실무에 바로 쓸 수 있는 사례가 많아서 좋았습니다.'}, 'content'),
        ('s06', {'answer': '중간에 쉬는 시간이 거의 없어서 집중력이 떨어졌어요.'}, 'schedule'),
        ('s07', {'answer': '질문에 친절하게 답해 주셔서 감사했습니다.'}, 'instructor'),
        ('s08', {'answer': '기초 내용이 너무 많아서 이미 아는 사람한테는 지루했어요.'}, 'content'),
        ('s09', {'answer': '직접 만들어 보는 시간이 제일 재밌었어요. 더 늘려 주세요.'}, 'practice'),
        ('s10', {'answer': '점심 도시락이 맛있었어요. 주차가 좀 불편했지만요.'}, 'venue'),
        ('s11', {'answer': '진도가 빨라서 놓친 부분이 있는데 자료로 복습할 수 있어서 다행이었어요.'}, 'content'),
        ('s12', {'answer': '말씀이 좀 빠르셔서 받아 적기 어려웠습니다.'}, 'instructor'),
    ])

# ── W4b 만족도 단계 (Score) ──────────────────────────────────────────
WF['w4_score'] = dict(
    type='score',
    ko='교육 만족도 설문의 이 주관식 응답(`answer`)에 드러난 전체 만족도는 어느 단계인가?',
    en='What overall satisfaction level does this open-ended survey answer (`answer`) express?',
    levels_ko=['매우 불만: 강한 불만이나 다시는 안 듣겠다는 뜻', '불만: 아쉬운 점이 좋은 점보다 큼', '보통: 좋은 점과 아쉬운 점이 비슷하거나 중립', '만족: 좋았다는 쪽이 분명함', '매우 만족: 강한 칭찬, 추천하겠다는 뜻'],
    levels_en=['Very dissatisfied: strong complaints or would never attend again.', 'Dissatisfied: the downsides outweigh the positives.', 'Neutral: positives and negatives balance, or no clear opinion.', 'Satisfied: clearly positive overall.', 'Very satisfied: strong praise or would recommend it.'],
    items=[
        ('v01', {'answer': '인생 교육이었습니다. 동료들한테 꼭 들으라고 추천했어요.'}, 4),
        ('v02', {'answer': '내용은 괜찮았는데 시간이 너무 길었어요.'}, 2),
        ('v03', {'answer': '시간 낭비였습니다. 다시는 신청 안 할 겁니다.'}, 0),
        ('v04', {'answer': '전반적으로 유익했어요. 실습이 특히 좋았습니다.'}, 3),
        ('v05', {'answer': '강사님은 좋았는데 실습 환경이 엉망이라 절반은 따라가지도 못했어요. 아쉬움이 더 큽니다.'}, 1),
        ('v06', {'answer': '특별히 할 말 없습니다.'}, 2),
        ('v07', {'answer': '네~ 아주 "유익"했네요. 8시간 동안 아는 얘기만 들어서요.'}, 0),
        ('v08', {'answer': '기대 이상이었어요. 다음 심화 과정도 꼭 듣고 싶습니다!'}, 4),
    ])

# ── W5 계약 조항 (Noul 3종) ─────────────────────────────────────────
WF['w5_autorenew'] = dict(
    type='noul',
    ko='`clause` 는 별도 의사 표시가 없으면 계약이 자동으로 연장·갱신된다는 조항인가?',
    en='Does `clause` say the contract renews or extends automatically unless someone says otherwise?',
    items=[
        ('k01', {'clause': '제12조(계약기간) 본 계약의 기간은 1년으로 하며, 만료 1개월 전까지 어느 일방의 서면 해지 통보가 없으면 동일 조건으로 1년씩 연장된다.'}, True),
        ('k02', {'clause': '제12조(계약기간) 본 계약의 기간은 2026년 12월 31일까지로 하며, 연장이 필요한 경우 양 당사자가 별도로 합의한다.'}, False),
        ('k03', {'clause': '제5조(구독) 서비스 이용 기간 종료 시 등록된 결제 수단으로 다음 기간 요금이 결제되며 이용 기간이 갱신된다. 갱신을 원하지 않는 회원은 종료 7일 전까지 해지할 수 있다.'}, True),
        ('k04', {'clause': '제8조(계약의 종료) 본 계약은 교육 종료일에 종료되며, 자동으로 연장되지 아니한다.'}, False),
        ('k05', {'clause': '제3조(기간) 계약기간은 6개월이다. 갑은 계약 만료 후 을의 실적을 평가하여 재계약 여부를 결정할 수 있다.'}, False),
    ])
WF['w5_penalty'] = dict(
    type='noul',
    ko='`clause` 는 계약을 지키지 않거나 중도에 해지할 때 돈(위약금·손해배상 예정액·지체상금)을 물어야 한다고 정하는가?',
    en='Does `clause` require paying money (a penalty, liquidated damages or late-delivery charges) for breaching or terminating the contract early?',
    items=[
        ('k06', {'clause': '제9조(위약금) 을이 정당한 사유 없이 교육을 취소하는 경우 계약금액의 30%를 위약금으로 갑에게 지급한다.'}, True),
        ('k07', {'clause': '제9조(취소) 교육 7일 전까지 취소하는 경우 위약금 없이 전액 환불한다.'}, False),
        ('k08', {'clause': '제10조(지체상금) 을이 납품기한을 넘기는 경우 지체일수 1일당 계약금액의 1천분의 1.5를 지체상금으로 공제한다.'}, True),
        ('k09', {'clause': '제11조(분쟁) 본 계약과 관련한 분쟁은 갑의 소재지 관할 법원으로 한다.'}, False),
        ('k10', {'clause': '제9조(해지) 양 당사자는 30일 전 서면 통보로 계약을 해지할 수 있으며, 이 경우 해지일까지 이행된 부분에 한하여 대금을 정산한다.'}, False),
    ])
WF['w5_onesided'] = dict(
    type='noul',
    ko='`clause` 는 갑(발주자) 한쪽만 사유 없이 또는 일방적으로 계약을 해지하거나 내용을 바꿀 수 있게 하는가? 양쪽 모두에게 같은 권리가 있으면 아니다.',
    en='Does `clause` let only party A (the client) terminate or change the contract unilaterally or without cause? If both parties have the same right, the answer is no.',
    items=[
        ('k11', {'clause': '제13조(해지) 갑은 필요하다고 인정하는 경우 언제든지 을에게 통보하여 본 계약을 해지할 수 있으며, 을은 이에 대하여 이의를 제기할 수 없다.'}, True),
        ('k12', {'clause': '제13조(해지) 갑 또는 을은 상대방이 계약을 위반하고 14일 이내에 시정하지 않는 경우 계약을 해지할 수 있다.'}, False),
        ('k13', {'clause': '제6조(변경) 갑은 교육 일정과 장소를 사정에 따라 변경할 수 있으며 을은 이에 따라야 한다.'}, True),
        ('k14', {'clause': '제6조(변경) 계약 내용의 변경은 양 당사자의 서면 합의로만 할 수 있다.'}, False),
    ])


def split_of(item_id: str) -> str:
    """dev 약 40% · holdout 약 60%. id 해시로 고정한다."""
    return 'dev' if int(hashlib.sha256(item_id.encode()).hexdigest(), 16) % 10 < 4 else 'holdout'


def main():
    items = []
    for wf, spec in WF.items():
        for iid, state, gold in spec['items']:
            it = {'id': iid, 'wf': wf, 'type': spec['type'], 'state': state, 'gold': gold, 'split': split_of(iid),
                  'ko': spec['ko'], 'en': spec['en']}
            if spec['type'] == 'choice':
                it['options'] = [{'key': k, 'ko': v[0], 'ko_desc': v[1], 'en': v[2], 'en_desc': v[3]} for k, v in spec['options'].items()]
            if spec['type'] == 'score':
                it['levels_ko'], it['levels_en'] = spec['levels_ko'], spec['levels_en']
            items.append(it)
    body = json.dumps({'version': 3, 'items': items}, ensure_ascii=False, indent=1)
    (ROOT / 'items.json').write_text(body)
    digest = hashlib.sha256(body.encode()).hexdigest()
    (ROOT / 'lock.txt').write_text(f'items.json sha256 {digest}\nitems {len(items)}\n')
    by = {}
    for it in items:
        by.setdefault(it['wf'], [0, 0])[0 if it['split'] == 'dev' else 1] += 1
    print(len(items), 'items', digest[:16], {k: f'dev{v[0]}/hold{v[1]}' for k, v in by.items()})


if __name__ == '__main__':
    main()
