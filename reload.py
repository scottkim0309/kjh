import streamlit as st

with st.sidebar:
  st.header("닉네임 입력")
  user_name = st.text_input("닉네임", placeholder="게임닉을 입력해주세요")
  if st.button("확인"):
    if not user_name.strip():
        st.warning("⚠️ 내용을 작성하지 않았습니다! 입력 후 다시 시도해 주세요.")
    else:st.success("있는계정입니다")
st.title("😎wildrift 탑챔프 추천")
champion = st.radio("챔프", ["가렌","다리우스","아트록스","레넥톤","세트","볼리베어","피오라","요네","카밀","잭스","이렐리아","말파이트","오른","쉔","사이온"], horizontal = true)
