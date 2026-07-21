import streamlit as st
from openai import OpenAI

ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "넌 최고의 롤 코치임"}]

if "selected_combination" not in st.session_state:
    st.session_state.selected_combination = ""

if "combination_completed" not in st.session_state:
    st.session_state.combination_completed = False

with st.sidebar:
    st.header("닉네임 입력")
    input_name = st.text_input("닉네임", placeholder="게임닉을 입력해주세요")
    if st.button("확인"):
        if not input_name.strip():
            st.warning("⚠️ 내용을 작성하지 않았습니다! 입력 후 다시 시도해 주세요.", key="")
            st.session_state.user_name = ""
        else:
            st.session_state.user_name = input_name
            st.success("확인되었습니다!")       

if not st.session_state.user_name:
    st.info("👈 사이드바에서 닉네임을 입력하고 [확인] 버튼을 눌러주세요.")
    st.stop()

def page_combination():
    st.title("😎 이색 바텀조합 선택")
    st.write(f"🎮 **{st.session_state.user_name}**님, 원하는 바텀 조합을 선택해보세요!")
    st.markdown("---")

    st.subheader("바텀조합")
    Champion = st.radio(
        "바텀조합", 
        ["세나,사이온", "세라핀,애쉬", "야스오,요네", "직스,레오나", "베이가,알리스타", 
         "노틸러스,럭스", "럭스,소나", "모르가나,리신", "스웨인,노틸러스"], 
        horizontal=True, 
        label_visibility="collapsed"
    )

    descriptions = {
        "세나,사이온": "사이온이 E로 미니언을 날리고 세나의 W를 연계하여 강력한 견제가 가능합니다.",
        "세라핀,애쉬": "애쉬의 궁극기 스턴 이후 세라핀 궁극기로 이어지는 원거리 CC 사기 조합입니다.",
        "야스오,요네": "에어본 연계와 강력한 맞딜로 한타 파괴력이 매우 뛰어난 칼바람/이색 조합입니다.",
        "직스,레오나": "레오나의 든든한 CC기 속에서 직스가 안전하게 포킹 및 타워 철거를 진행합니다.",
        "베이가,알리스타": "베이가의 사건 지평선(E) 벽 쪽으로 알리스타가 W(밀치기)로 박아버리는 확정 스턴 조합입니다.",
        "노틸러스,럭스": "스킬 하나만 맞춰도 체력이 다 깎이는 무지막지한 딜찍누 듀오입니다.",
        "럭스,소나": "무한 쉴드와 힐, 속도 증가로 죽지 않고 끈질기게 버티는 유지력 조합입니다.",
        "모르가나,리신": "모르가나의 블랙실드로 리신의 진입을 돕고, 속박 후 리신 궁으로 킬을 쓸어담습니다.",
        "스웨인,노틸러스": "끌어당기는 CC기가 2개! 한번 잡히면 절대 살아나갈 수 없는 통곡의 벽 조합입니다."
    }
    videos = {
        "세나,사이온": "https://www.youtube.com/watch?v=4dxhXf72yfg",
        "세라핀,애쉬": "https://www.youtube.com/watch?v=HnYeF5-q6Q0",
        "야스오,요네": "https://www.youtube.com/watch?v=3yBE8bLLl0g",
        "직스,레오나": "https://www.youtube.com/watch?v=0e-Fd1HAjzw",
        "베이가,알리스타": "https://www.youtube.com/watch?v=7uQksFN-AlI",
        "노틸러스,럭스": "https://www.youtube.com/watch?v=R9EzrzHIHZI",
        "럭스,소나": "https://www.youtube.com/watch?v=Yzee-hU0HMM",
        "모르가나,리신": "https://www.youtube.com/shorts/G_rAwQIEz3U",
        "스웨인,노틸러스": "https://www.youtube.com/shorts/-V2aHtQj3m8"
    }

    st.markdown("---")
    
    if st.button("🔥 조합 완성하기"):
        st.session_state.selected_combination = Champion
        st.session_state.combination_completed = True

    if st.session_state.combination_completed:
        with st.container(border=True):
            st.subheader("🎯 선택한 조합 정보")
            st.write(f"👤 **소환사:** {st.session_state.user_name}")
            st.write(f"⚔️ **선택한 조합:** {st.session_state.selected_combination}")
            st.info(f"💡 **조합 특징**\n\n{descriptions[st.session_state.selected_combination]}")
            st.subheader("🎬 플레이 영상")
            current_video = videos.get(st.session_state.selected_combination)
            if current_video:
                st.video(current_video)


def page_ai():
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
            status_context = f"현재 유저 닉네임: {st.session_state.user_name}, 선택한 조합: {st.session_state.selected_combination}"
            api_prompt = st.session_state.messages + [{"role": "system", "content": status_context}]
            
            with st.spinner("AI 코치가 생각 중...🤔"):
                response = ai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=api_prompt
                )
                ai_response = response.choices[0].message.content
                st.markdown(ai_response)

        st.session_state.messages.append({"role": "assistant", "content": ai_response})

pg = st.navigation([
    st.Page(page_combination, title="바텀 조합 선택", icon="⚔️"),
    st.Page(page_ai, title="AI 코치 대화", icon="💬")
])

pg.run()

if st.button("초기화"):
        st.session_state.clear()
        st.rerun()

























