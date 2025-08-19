import streamlit as st
import random

st.set_page_config(page_title="밸런스 게임 🎲", page_icon="🎮", layout="centered")

st.markdown("<h1 style='text-align: center;'>⚖️ 밸런스 게임 자동 생성기 🎮</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>✨ 버튼을 눌러 오늘의 질문을 뽑아보고, 투표에 참여해보세요! ✨</h3>", unsafe_allow_html=True)

# 고정된 질문 리스트
balance_questions = [
    ("🍗 치킨 평생 금지", "🍜 라면 평생 금지"),
    ("📱 휴대폰 없이 살기", "🌐 인터넷 없이 살기"),
    ("😂 웃을 때 돼지소리 나기", "🤣 울 때 강아지 소리 나기"),
    ("👩‍🏫 매일 아침 0교시 수업 듣기", "📚 매일 밤 자율학습 3시간 하기"),
    ("✈️ 해외여행 1년 자유이용권 받기", "💸 현금 100만 원 받기"),
    ("💕 이상형이 내 옆반에 전학 오기", "💌 좋아하는 사람이 나한테 먼저 고백하기"),
    ("🍫 평생 단 음식만 먹기", "🍟 평생 짠 음식만 먹기"),
    ("🎤 콘서트 1열 직관하기", "📸 아이돌이 내 SNS에 댓글 달아주기"),
    ("🏫 학교에서 하루 종일 시험 보기", "🏠 집에서 숙제만 하루 종일 하기"),
    ("🕺 체육대회에서 메인 댄서 하기", "🎤 교내 장기자랑 무대 올라가기"),
    ("🍕 피자 한 판 혼자 먹기", "🍦 아이스크림 10개 혼자 먹기"),
    ("📸 사진 찍을 때 항상 눈 감기", "😂 사진 찍을 때 항상 이상한 표정 나오기"),
    ("🎧 이어폰 한쪽만 평생 쓰기", "🔋 휴대폰 배터리 20%로 평생 살기"),
    ("💡 미래의 나랑 10분 대화하기", "🍼 과거의 나랑 10분 대화하기"),
]

# 세션 상태로 현재 질문/투표 저장
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "votes" not in st.session_state:
    st.session_state.votes = [0, 0]

# 새로운 질문 뽑기 버튼
if st.button("🎲 새로운 밸런스 게임 뽑기! 🎉"):
    st.session_state.current_question = random.choice(balance_questions)
    st.session_state.votes = [0, 0]  # 투표 초기화

# 질문이 있을 때만 보여주기
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

    # 투표 결과 출력
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
st.markdown("<p style='text-align: center;'>💖 친구랑 같이 하면 더 재밌는 밸런스 게임! 💖</p>", unsafe_allow_html=True)
