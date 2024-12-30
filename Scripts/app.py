import streamlit as st
import pandas as pd
import time
from chatbot import chatbot

# Load intents JSON file
df = pd.read_json('chatbot-intents.json')
intents = df.intents.values

def main():
    # Set up the Streamlit app configuration
    st.set_page_config(
        page_title="Mental Health Support - Feel Good Chatbot",
        page_icon="❤️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    with st.sidebar:
        st.title("Mental Health Support Chatbot 😊")
        st.markdown(
            """
            **Welcome to Jolly - Your Mental Health Assistant!**  
            Let's talk and feel better. 💬  
            """
        )

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input and process it
    if user_input := st.chat_input("Start Conversation with Jolly..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display user's message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate assistant's response
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response = chatbot(user_input, intents)
            full_response = ""

            # Simulate typing effect
            for word in response.split():
                full_response += word + " "
                time.sleep(0.05)  # Adjust typing speed
                response_placeholder.markdown(full_response + "▌")  # Blinking cursor
            response_placeholder.markdown(full_response)

        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == '__main__':
    main()
