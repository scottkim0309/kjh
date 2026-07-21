import streamlit as st
from openai import OpenAI

ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "넌 최고의 롤(LoL) 코치야."}]

with st.sidebar:
    st.header("닉네임 입력")
    input_name = st.text_input("닉네임", placeholder="게임닉을 입력해주세요")
    if st.button("확인"):
        if not input_name.strip():
            st.warning("⚠️ 내용을 작성하지 않았습니다! 입력 후 다시 시도해 주세요.")
            st.session_state.user_name = ""
        else:
            st.session_state.user_name = input_name
            st.success("확인되었습니다!")

if not st.session_state.user_name:
    st.info("👈 사이드바에서 닉네임을 입력하고 [확인] 버튼을 눌러주세요.")
    st.stop()

st.title("😎 이색 바텀조합 선택")
st.write(f"🎮 **{st.session_state.user_name}**님, 원하는 바텀 조합을 선택해보세요!")
st.markdown("---")

st.subheader("바텀조합")
Champion = st.radio(
    "바텀조합", 
    ["세나,사이온", "세라핀,애쉬", "야스오,요네", "직스,레오나", "베이가,알리스타", 
     "브랜드,럭스", "럭스,소나", "모르가나,파이크", "스웨인,노틸러스", "티모,신 짜오"], 
    horizontal=True, 
    label_visibility="collapsed"
)

descriptions = {
    "세나,사이온": "사이온이 E로 미니언을 날리고 세나의 W를 연계하여 강력한 견제가 가능합니다.",
    "세라핀,애쉬": "애쉬의 궁극기 스턴 이후 세라핀 궁극기로 이어지는 원거리 CC 사기 조합입니다.",
    "야스오,요네": "에어본 연계와 강력한 맞딜로 한타 파괴력이 매우 뛰어난 칼바람/이색 조합입니다.",
    "직스,레오나": "레오나의 든든한 CC기 속에서 직스가 안전하게 포킹 및 타워 철거를 진행합니다.",
    "베이가,알리스타": "베이가의 사건 지평선(E) 벽 쪽으로 알리스타가 W(밀치기)로 박아버리는 확정 스턴 조합입니다.",
    "브랜드,럭스": "스킬 하나만 맞춰도 체력이 다 깎이는 무지막지한 딜찍누 듀오입니다.",
    "럭스,소나": "무한 쉴드와 힐, 속도 증가로 죽지 않고 끈질기게 버티는 유지력 조합입니다.",
    "모르가나,파이크": "모르가나의 블랙실드로 파이크의 진입을 돕고, 속박 후 파이크 궁으로 킬을 쓸어담습니다.",
    "스웨인,노틸러스": "끌어당기는 CC기가 2개! 한번 잡히면 절대 살아나갈 수 없는 통곡의 벽 조합입니다.",
    "티모,신 짜오": "신 짜오의 돌진과 티모의 실명/실버 스킬로 상대 원딜을 아무것도 못 하게 만드는 조합입니다."
}

st.markdown("---")
if Champion in descriptions:
    st.info(f"💡 **[{Champion}] 조합 특징**\n\n{descriptions[Champion]}")

st.markdown("---")
st.header("💬 AI 코치와 대화하기")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

question = st.chat_input("질문을 입력하세요")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        status_context = f"현재 유저 닉네임: {st.session_state.user_name}, 선택한 조합: {Champion}"
        api_prompt = st.session_state.messages + [{"role": "system", "content": status_context}]
        
        with st.spinner("AI 코치가 생각 중...🤔"):
            response = ai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=api_prompt
            )
            ai_response = response.choices[0].message.content
            st.markdown(ai_response)

    st.session_state.messages.append({"role": "assistant", "content": ai_response})

























