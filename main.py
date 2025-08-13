import streamlit as st
import random

st.set_page_config(page_title="💖✨ 궁합 테스트 ✨💖", page_icon="💘", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: hotpink;'>💖✨ 운명 궁합 테스트 ✨💖</h1>", 
    unsafe_allow_html=True
)
st.write("두 사람의 이름을 입력하고, 운명 같은 궁합을 확인해보세요! 💫")

# 입력 받기
name1 = st.text_input("💌 첫 번째 이름을 입력해주세요:")
name2 = st.text_input("💌 두 번째 이름을 입력해주세요:")

if st.button("💘 궁합 확인하기 💘"):
    if name1.strip() == "" or name2.strip() == "":
        st.warning("🙈 두 이름을 모두 입력해야 해요!")
    else:
        # 이름 기반 점수 생성 (0~100)
        combined = name1 + name2
        score = sum(ord(c) for c in combined) % 101  

        st.markdown(f"<h2 style='text-align: center;'>💘 {name1} ❤️ {name2} 💘</h2>", unsafe_allow_html=True)
        st.metric(label="✨ 궁합 점수 ✨", value=f"{score}%")

        # 점수별 멘트 + 이모지
        if score > 80:
            messages = [
                "🌟 운명적인 사랑이에요! 💍💖\n두 분은 서로를 비추는 별 ✨",
                "💞 영혼의 단짝이네요! 💫\n함께라면 모든 게 반짝일 거예요 🌸",
                "💕 서로를 위해 태어난 커플! 🥰\n세상이 부러워할 사랑이에요 💎"
            ]
            st.success(random.choice(messages))
            st.balloons()

        elif score > 50:
            messages = [
                "💐 서로에게 기분 좋은 바람 같은 존재 🌿\n노력한다면 더 멋진 인연으로! 🌈",
                "🌸 따뜻하게 서로를 감싸주는 사이 💕\n앞으로 더 깊어질 사랑이에요 💖",
                "💫 조화로운 두 분의 에너지 ✨\n조금씩 맞춰가면 최고의 궁합! 🌷"
            ]
            st.info(random.choice(messages))

        else:
            messages = [
                "🌱 시작은 조금 달라도, 시간이 사랑을 키울 거예요 💖",
                "🌙 서로의 차이를 이해하면, 오히려 더 끌릴 수 있어요 ✨",
                "☀️ 인연은 노력으로 만들어져요 🌼\n오늘부터 한 걸음씩 다가가 보세요 💌"
            ]
            st.warning(random.choice(messages))
