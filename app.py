import streamlit as st
st.title("카운트 앱")
if 'count' not in st.session_state:
   st.session_state.count=0
if st.button("증가"):
   st.session_state.count +=1
st.markdown(f"## 현재숫자: '{st.session_state.count}'")
