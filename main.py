import os
from dotenv import load_dotenv
import streamlit as st
import openai

# Load environment variables from .env file
load_dotenv()

# configuring openai - api key
openai.api_key = os.getenv("OPENAI_API_KEY")

# configuring streamlit UI page settings
st.set_page_config(
    page_title="GPT Chat",
    page_icon="💭",
    layout="centered"
)

# initialize chat session in streamlit
st.session_state.chat_history = []

# streamlit page title
st.title("🗣️ OpenAI GPT - ChatBot")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# input field for user's message
user_prompt = st.chat_input("Ask GPT...")

if user_prompt:
    # add user's message to chat_history and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user's message to openAI gpt and get a response
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant"},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display GPT's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)