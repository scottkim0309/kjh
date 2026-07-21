import streamlit as st
import time

def reset_game():
    st.session_state.start_time = 0
    st.session_state.end_time = 0
    st.session_state.result = 0

# session_state 초기화
if 'start_time' not in st.session_state:
    reset_game()

st.title("10초 맞추기 게임!")
st.write("시작 버튼을 누르고, 마음속으로 10초를 센 뒤 종료 버튼을 누르세요.")

# 상태 값 정의
is_started = st.session_state.start_time != 0
is_ended = st.session_state.end_time != 0

col1, col2 = st.columns(2)

with col1:
    # 게임 중이거나 이미 끝난 상태에서는 시작 버튼 비활성화
    if st.button("시작", disabled=is_started):
        st.session_state.start_time = time.time()
        st.session_state.end_time = 0
        st.rerun()

with col2:
    # 시작하지 않았거나 이미 종료된 경우 종료 버튼 비활성화 (한 번만 클릭 가능)
    if st.button("종료", disabled=(not is_started or is_ended)):
        st.session_state.end_time = time.time()
        st.session_state.result = st.session_state.end_time - st.session_state.start_time
        st.rerun()

# 결과 출력
if is_ended:
    diff = st.session_state.result
    st.header(f"결과: {diff:.2f}초")
    
    if 9.7 <= diff <= 10.3:
        st.success("대단해요! 정확합니다!")
    else:
        st.error(f"10초와 {abs(10-diff):.2f}초 차이가 납니다. 다시 도전해보세요!")

# 리셋 버튼
if st.button("다시 하기"):
    reset_game()
    st.rerun()
