import streamlit as st

with st.sidebar:
  st.header("닉네임 입력")
  user_name = st.text_input("닉네임", placeholder="게임닉을 입력해주세요")
  if st.button("확인"):
    if not user_name.strip():
        st.warning("⚠️ 내용을 작성하지 않았습니다! 입력 후 다시 시도해 주세요.")
    else:st.success("있는계정입니다")
st.title("😎이색 바텀조합 선택")
st.subheader("바텀조합")
Champion = st.radio("바텀조합", ["세나,사이온","세라핀,애쉬","야스오,요네","직스,레오나","베이가,알리스타","브랜드,럭스","럭스,소나","모르가나,파이크","스웨인,노틸러스","티모,신 짜오"], horizontal=True, label_visibility="collapsed")
