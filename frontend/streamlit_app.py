import streamlit as st
import requests
from datetime import datetime


st.set_page_config(
    page_title="Support Assistant",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    .chat-header {
        text-align: center;
        padding: 10px 0 20px 0;
    }
    .chat-header h1 {
        font-size: 28px;
        margin-bottom: 0;
    }
    .chat-header p {
        color: gray;
        font-size: 14px;
    }
    .stChatMessage {
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm your support assistant. How can I help you today?",
            "time": datetime.now().strftime("%H:%M"),
        }
    ]

if "resolved" not in st.session_state:
    st.session_state.resolved = False


BACKEND_URL = "http://127.0.0.1:8000/chat"


def get_bot_response(user_message: str) -> str:
    """
    Calls the FastAPI backend's /chat endpoint, which runs the RAG pipeline.
    """
    try:
        response = requests.post(
            BACKEND_URL,
            #json={"message": user_message},
            json={"question": user_message},
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get("answer", "Sorry, I couldn't generate a response.")
    except requests.exceptions.ConnectionError:
        return "⚠️ Couldn't reach the backend. Make sure the FastAPI server is running on port 8000."
    except requests.exceptions.Timeout:
        return "⚠️ The backend took too long to respond. Please try again."
    except requests.exceptions.HTTPError as e:
        return f"⚠️ Backend returned an error: {e}"
    except Exception as e:
        return f"⚠️ Something went wrong: {e}"


with st.sidebar:
    st.markdown("### 🛠️ Support Options")
    st.write("Need something specific? Pick a quick topic:")

    quick_topics = ["Order status", "Refund request", "Account issue", "Talk to a human"]
    for topic in quick_topics:
        if st.button(topic, use_container_width=True):
            st.session_state.messages.append(
                {"role": "user", "content": topic, "time": datetime.now().strftime("%H:%M")}
            )
            reply = get_bot_response(topic)
            st.session_state.messages.append(
                {"role": "assistant", "content": reply, "time": datetime.now().strftime("%H:%M")}
            )
            st.rerun()

    st.divider()

    if st.button("🔄 Start New Conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi again! What can I help you with?",
                "time": datetime.now().strftime("%H:%M"),
            }
        ]
        st.rerun()

    st.divider()
    st.caption("Support hours: Mon–Fri, 9am–6pm")
    st.caption("Average response time: under 1 minute")


st.markdown(
    """
    <div class="chat-header">
        <h1>💬 Customer Support</h1>
        <p>Ask a question and we'll help you sort it out</p>
    </div>
    """,
    unsafe_allow_html=True,
)


for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])
        st.caption(msg["time"])


user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input, "time": datetime.now().strftime("%H:%M")}
    )
    with st.chat_message("user", avatar="🧑"):
        st.write(user_input)
        st.caption(datetime.now().strftime("%H:%M"))

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            reply = get_bot_response(user_input)
        st.write(reply)
        st.caption(datetime.now().strftime("%H:%M"))

    st.session_state.messages.append(
        {"role": "assistant", "content": reply, "time": datetime.now().strftime("%H:%M")}
    )


if len(st.session_state.messages) > 1:
    st.divider()
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("👍 Helpful"):
            st.toast("Thanks for your feedback!")
    with col2:
        if st.button("👎 Not helpful"):
            st.toast("Thanks — we'll use this to improve.")