import streamlit as st
import random

st.set_page_config(page_title="밸런스 게임 자동 생성기", page_icon="⚖️", layout="centered")

st.title("⚖️ 밸런스 게임 자동 생성기")
st.write("버튼을 눌러 완전히 새로운 밸런스 게임 질문을 만들어보세요!")

# 카테고리별 선택지
foods = ["치킨", "피자", "떡볶이", "초콜릿", "삼겹살", "라면", "커피", "아이스크림"]
situations = ["휴대폰 없이 살기", "인터넷 없이 살기", "TV 없이 살기", "친구 없이 살기", "하루 종일 혼자 있기"]
funny = ["10분마다 재채기", "하루 종일 딸꾹질", "웃을 때마다 이상한 소리 나기", "하루에 한 번 랜덤 순간이동"]
lifestyle = ["미래로 가보기", "과거로 돌아가기", "평생 같은 옷 입기", "평생 같은 음식 먹기", "잠을 하루에 2시간만 자기"]

# 모든 카테고리 묶기
all_choices = [foods, situations, funny, lifestyle]

def generate_question():
    # 서로 다른 카테고리에서 하나씩 뽑거나, 같은 카테고리에서 랜덤 2개 뽑기
    if random.random() > 0.5:  
        # 서로 다른 카테고리에서 뽑기
        category1, category2 = random.sample(all_choices, 2)
        option1 = random.choice(category1)
        option2 = random.choice(category2)
    else:
        # 같은 카테고리에서 뽑기
        category = random.choice(all_choices)
        option1, option2 = random.sample(category, 2)
    return option1, option2

# 버튼 눌렀을 때 새로운 질문 생성
if st.button("🎲 새로운 밸런스 게임 생성"):
    q1, q2 = generate_question()
    st.subheader("📌 오늘의 질문!")
    col1, col2 = st.columns(2)
    with col1:
        st.button(q1)
    with col2:
        st.button(q2)
