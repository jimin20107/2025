import streamlit as st
import random

st.set_page_config(page_title="밸런스 게임 자동 생성기", page_icon="🎮", layout="centered")

st.title("🎮 밸런스 게임 자동 생성기")
st.write("버튼을 눌러 랜덤 밸런스 게임 질문을 뽑아보세요!")

# 밸런스 게임 질문 리스트
balance_questions = [
    ("치킨 1년 금지", "떡볶이 1년 금지"),
    ("여름에만 살기", "겨울에만 살기"),
    ("휴대폰 없이 살기", "인터넷 없이 살기"),
    ("평생 단 음식만 먹기", "평생 짠 음식만 먹기"),
    ("10분마다 재채기", "하루 종일 딸꾹질"),
    ("과거로 돌아가기", "미래로 가보기"),
    ("자유 시간은 많지만 돈 없음", "돈은 많지만 자유 시간 없음"),
    ("평생 한식만 먹기", "평생 양식만 먹기"),
    ("친구 100명과 얕은 사이", "친구 1명과 깊은 사이"),
    ("평생 같은 옷 입기", "평생 같은 음식 먹기"),
]

# 버튼 눌렀을 때 랜덤 질문 뽑기
if st.button("🎲 새로운 밸런스 게임 뽑기"):
    q = random.choice(balance_questions)
    st.subheader("📌 오늘의 질문!")
    col1, col2 = st.columns(2)
    with col1:
        st.button(q[0])
    with col2:
        st.button(q[1])
