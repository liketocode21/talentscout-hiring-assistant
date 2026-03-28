import streamlit as st
from chatbot import get_response
from prompts import get_system_prompt

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="TalentScout AI",
    page_icon="🤖",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------ #
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.stChatMessage {
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------ #
with st.sidebar:
    st.title("🚀 TalentScout")

    st.markdown("### AI Hiring Dashboard")

    st.markdown("""
    ✔ AI Screening  
    ✔ Skill Analysis  
    ✔ Company Matching  
    ✔ Smart Recommendations  
    """)

    st.markdown("---")

    if st.button("🔄 Start New Session"):
        st.session_state.messages = [
            {"role": "system", "content": get_system_prompt()}
        ]
        st.rerun()

# ------------------ HEADER ------------------ #
st.markdown("""
# 🤖 TalentScout Hiring Assistant  
### Smart AI-powered candidate screening system
""")

# ------------------ METRICS ------------------ #
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Candidates Screened", "120+")

with col2:
    st.metric("Avg Experience", "3.5 yrs")

with col3:
    st.metric("Tech Domains", "15+")

st.markdown("---")

# ------------------ SESSION STATE ------------------ #
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": get_system_prompt()}
    ]

# ------------------ CHAT DISPLAY ------------------ #
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ USER INPUT ------------------ #
user_input = st.chat_input("Type your message here...")

if user_input:

    # Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.success("✅ Thank you for interacting with TalentScout!")

        # Reset chat
        st.session_state.messages = [
            {"role": "system", "content": get_system_prompt()}
        ]

        st.rerun()

    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    response = get_response(st.session_state.messages)

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)