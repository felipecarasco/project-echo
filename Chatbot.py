import time
import streamlit as st
import random
from PIL import Image

st.logo(
    "assets/echo_logo_light.png",
    size="large",
    link=None,
    icon_image="assets/logo.png",
)

st.title("💬 Echo Chatbot")
st.caption("🤖 A simple chatbot")

USER_AVATAR = "👤" 
BOT_AVATAR = "🤖"

CHATBOT_KEY_PREFIX = "chatbot_"

if f"{CHATBOT_KEY_PREFIX}messages" not in st.session_state:
    st.session_state[f"{CHATBOT_KEY_PREFIX}messages"] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

for msg in st.session_state[f"{CHATBOT_KEY_PREFIX}messages"]:
    with st.chat_message(msg["role"], avatar=BOT_AVATAR if msg["role"] == "assistant" else USER_AVATAR):
        st.write(msg["content"])

def stream_data(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def mock_response(user_input):
    mock_responses = {
        "hi": ["Hi! How are you?", "Hello! How can I help you?"],
        "what's your name": ["I am a chatbot!", "I am called Virtual Assistant."],
        "how does it work": ["I am just a mock, but I can pretend to be a chatbot!", "I work by responding based on keywords."],
    }
    for key, responses in mock_responses.items():
        if key in user_input.lower():
            return random.choice(responses)
    
    return "Sorry, I didn't understand that. Could you rephrase the question?"

if prompt := st.chat_input("Type your message..."):
    st.session_state[f"{CHATBOT_KEY_PREFIX}messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):  
        st.write(prompt)

    mock_response_text = mock_response(prompt)
    # with st.spinner("Loading..."):
    #     time.sleep(1)
    st.session_state[f"{CHATBOT_KEY_PREFIX}messages"].append({"role": "assistant", "content": mock_response_text})
    with st.chat_message("assistant", avatar=BOT_AVATAR):  
        st.write(stream_data(mock_response_text))
