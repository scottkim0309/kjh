import streamlit as st

with st.sidebar:
  st.header("닉네임 입력")
  user_name = st.text_input("닉네임", key="user_name")
st.title("😎wildrift 탑챔프 추천")
