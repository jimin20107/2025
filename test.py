import streamlit as st
import random

st.set_page_config(page_title="밸런스 게임 🎲", page_icon="🔥", layout="centered")

st.markdown("<h1 style='text-align: center;'>⚖️ 밸런스 게임 월드컵 🎮</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>✨ 카테고리를 고르고, 오늘의 질문을 뽑아보세요! ✨</h3>", unsafe_allow_html=True)

# =========================
# 질문 데이터
# =========================

questions = {
    "연애편 💕": [
        ("모두에게 시크한 애인 😎", "모두에게 다정한 애인 🥰"),
        ("연하같은 연상 👶➡️👴", "연상같은 연하 👴➡️👶"),
        ("강아지상 🐶", "고양이상 🐱"),
        ("힙한 스타일 🧢", "포멀한 스타일 👔"),
        ("전 애인이 50명 이상인 애인 😱", "모쏠인 애인 🙈"),
        ("커플룩 입자고 조르는 애인 👕💕👚", "커플룩 절대 안 입는 애인 🚫👕"),
        ("나랑 찍은 셀카 절대 안 올리는 애인 📵🤳", "내 모든 사진을 올리는 애인 📸✨"),
        ("얼굴은 내 취향인데 입만 열면 깨는 사람 🤐", "얼굴은 별로인데 말은 잘하는 사람 🗣️"),
        ("이모티콘 폭발형 🤩😂🥹🤣✨🔥", "이모티콘 금지형 🚫😐"),
        ("사소한 맞춤법도 틀리는 애인 ✏️❌", "사소한 맞춤법도 지적하는 애인 🧐"),
        ("1년에 여행 20번 이상 가는 애인 🌍", "집돌이/집순이 🏠"),
        ("바람둥이 양다리 애인 💔", "심각한 마마걸/마마보이 👩‍👦"),
        ("대머리 애인 🧑‍🦲", "라푼젤 애인(머리 말리는 데 8시간) 🧝‍♀️"),
        ("방구 소리 개큰 애인 💨🔊", "소리는 없는데 냄새 고약한 애인 🤢"),
        ("매일매일 프사가 바뀌는 애인 📱", "10년째 기본 프사 애인 🖼️"),
        ("데이트코스 초단위로 짜오는 애인 ⏱️", "데이트코스 다 나한테 맡기는 애인 😑"),
        ("머리 안 감는 애인 🤯", "볼일 보고 손 안 씻는 애인 🚽❌🧼"),
        ("천년의 이상형인데 해외 사는 애인 🌎", "그냥 그런데 바로 옆집 사는 애인 🏠"),
        ("공공장소에서 스킨십 폭발 애인 💋", "손만 닿아도 도망가는 애인 🏃‍♂️"),
        ("나를 이름 세 글자로 저장하는 애인 📝", "나를 '주인님'이라고 저장하는 애인 🙇‍♂️"),
        ("매운 음식 못 먹는 애인 🌶️🚫", "단 음식 못 먹는 애인 🍫🚫"),
        ("선톡 절대 안 하는 애인 😶", "1초마다 연락하는 애인 📲"),
        ("5조 부자 유병재 💸", "빛 5억 차은우 🧾✨"),
        ("똥냄새 나는 강동원 💩", "뭘 해도 향기나는 미미미누 🌸"),
        ("인스타 인플루언서 📷", "인터넷방송 애청자 🎥"),
        ("취미가 덕질인 애인 🫶", "취미가 없는 애인 😐"),
        ("질투가 너무 많은 애인 😤", "질투를 아예 안 하는 애인 🥱"),
        ("세상 귀차니즘 🛋️", "열정과다 🔥"),
        ("동물 싫어하는 애인 🚫🐶", "주말마다 동물이랑 노느라 연락 안 되는 애인 🐕"),
        ("친구 500명인 애인 👯", "친구 -1명인 애인 🥲"),
    ],

    "학교편 🏫": [
        ("급식 무조건 두 그릇 먹기 🍛", "급식 무조건 반만 먹기 🥗"),
        ("시험시간 10분 연장 ⏰", "시험문제 2개 덜 나오기 📄"),
        ("체육쌤이 담임 🏃", "미술쌤이 담임 🎨"),
        ("수학 매일 10분 시험 🧮", "국어 매일 받아쓰기 ✏️"),
        ("휴대폰 하루종일 압수 📵", "체육복 하루종일 입기 👕"),
        ("청소 당번 매일 걸리기 🧹", "급식 당번 매일 걸리기 🍲"),
        ("필기구 절대 안 챙겨옴 ✒️", "교과서 절대 안 챙겨옴 📚"),
        ("중간고사 면제 🎉", "기말고사 면제 🥳"),
        ("급식 메뉴 치킨만 🍗", "급식 메뉴 라면만 🍜"),
        ("교실에 에어컨 빵빵 ❄️", "교실에 난방 빵빵 🔥"),
    ],

    "우정편 👯": [
        ("내 비밀을 다 아는 친구 🤐", "내 비밀을 하나도 모르는 친구 🙃"),
        ("놀 땐 최고인데 공부 안 하는 친구 🎉", "공부는 잘하는데 노잼인 친구 📖"),
        ("항상 간식 사주는 친구 🍫", "항상 숙제 보여주는 친구 📘"),
        ("내 생일 절대 안 챙기는 친구 🎂🚫", "기념일마다 감동 주는 친구 🎁"),
        ("사진만 찍으면 눈 감는 친구 📸", "사진 찍으면 항상 이상한 표정 친구 😜"),
        ("10분 늦게 오는 친구 ⏰", "10분 일찍 오는 친구 😎"),
    ],

    "음식편 🍔": [
        ("탄산 빠진 콜라 🥤 vs 미지근한 사이다 🫠"),
        ("녹아버린 아이스크림 🍦 vs 눅눅해진 과자 🍪"),
        ("회 고추장 찍어먹기 🐟🌶 vs 회 간장 찍어먹기 🐟🍶"),
        ("삭힌 홍어 🤢 vs 두리안 🥴"),
        ("짜장면에 단무지 없는 거 🍜 vs 치킨에 무 없는 거 🍗"),
        ("뜨거운 피자 위에 파인애플 🍕🍍 vs 초밥 위에 파인애플 🍣🍍"),
        ("설탕 뿌린 김치 🥬🍬 vs 소금 뿌린 수박 🍉🧂"),
        ("무한 리필 콜라 vs 무한 리필 아이스크림 🍨"),
    ],
}

# "랜덤 전체편" 추가
all_questions = []
for q_list in questions.values():
    all_questions.extend(q_list)
questions["랜덤 전체편 🎲"] = all_questions

# =========================
# 앱 기능
# =========================

# 카테고리 선택
category = st.selectbox("📂 카테고리를 선택하세요:", list(questions.keys()))

# 현재 카테고리 질문 불러오기
balance_questions = questions[category]

# 세션 상태 관리
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "votes" not in st.session_state:
    st.session_state.votes = [0, 0]

# 새로운 질문 뽑기
if st.button("🎲 새로운 질문 뽑기! 🎉"):
    st.session_state.current_question = random.choice(balance_questions)
    st.session_state.votes = [0, 0]  # 투표 초기화

# 질문 출력
if st.session_state.current_question:
    q1, q2 = st.session_state.current_question
    st.markdown("<h2 style='text-align: center;'>📌 오늘의 질문!</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"👉 {q1}"):
            st.session_state.votes[0] += 1
    with col2:
        if st.button(f"👉 {q2}"):
            st.session_state.votes[1] += 1

    # 투표 결과
    total_votes = sum(st.session_state.votes)
    if total_votes > 0:
        st.subheader("📊 투표 현황")
        percent1 = (st.session_state.votes[0] / total_votes) * 100
        percent2 = (st.session_state.votes[1] / total_votes) * 100

        st.progress(int(percent1))
        st.write(f"{q1} 👉 {percent1:.1f}% ({st.session_state.votes[0]}표)")
        st.progress(int(percent2))
        st.write(f"{q2} 👉 {percent2:.1f}% ({st.session_state.votes[1]}표)")

st.markdown("---")
st.markdown("<p style='text-align: center;'>💖 친구랑 같이 하면 더 꿀잼! 💖</p>", unsafe_allow_html=True)
