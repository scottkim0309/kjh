import streamlit as st

st.header("앱 UI만들기")
user_id = st.text_input("이름", placeholder="이름")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
tone = st.selectbox("반", ["1", "2", "3","4","5","6"])
creativity = st.select_slider("난이도",options=["쉬움", "보통", "어려움"],value="보통")
ai_speed = st.slider("점수",0,100,50)
question = st.text_area("소감", placeholder="소감입력.")
st.markdown("---")
if st.button("확인"):
        st.success(f"{user_id} / {ai_model}학년 / {tone}반 / {creativity}")
        st.markdown(f"점수: `{ai_speed}`")
        st.info(f"소감: {question}")
