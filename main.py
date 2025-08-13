# app.py
import streamlit as st
import random

st.set_page_config(page_title="이름 궁합 앱", page_icon="💖", layout="centered")

st.title("💖 이름 궁합 테스트")
st.write("이름 두 개를 입력하면 궁합 점수를 알려드립니다!")

# 입력 받기
name1 = st.text_input("첫 번째 이름을 입력하세요:")
name2 = st.text_input("두 번째 이름을 입력하세요:")

if st.button("궁합 보기"):
    if name1.strip() == "" or name2.strip() == "":
        st.warning("이름을 모두 입력해주세요!")
    else:
        # 난수로 궁합 점수 생성
        random.seed(name1 + name2)  # 동일한 이름 조합이면 같은 점수
        score = random.randint(0, 100)

        st.subheader(f"💘 {name1} ❤️ {name2} 의 궁합은...")
        st.metric(label="궁합 점수", value=f"{score}%")

        if score > 80:
            st.success("환상의 커플이에요! 💍")
        elif score > 50:
            st.info("잘 맞는 편이네요! 😊")
        else:
            st.error("서로 노력하면 더 좋아질 수 있어요! 🌱")
