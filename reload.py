import streamlit as st

with st.sidebar:
  st.header("닉네임 입력")
  user_name = st.text_input("닉네임", placeholder="게임닉을 입력해주세요")
  if not user_input.strip(user_name):
        st.warning("⚠️ 내용을 작성하지 않았습니다! 입력 후 다시 시도해 주세요.")
    else:
        st.success("있는계정입니다")
st.title("😎wildrift 탑챔프 추천")
