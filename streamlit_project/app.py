import streamlit as st
import requests
import json

# Initialize session state for chat history and active chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}  # Store all chats as a dictionary
if "active_chat" not in st.session_state:
    st.session_state.active_chat = None  # Track the currently active chat

# Function to create a new chat
def create_new_chat():
    chat_name = f"Chat {len(st.session_state.chat_history) + 1}"
    st.session_state.chat_history[chat_name] = []  # Initialize empty chat history
    st.session_state.active_chat = chat_name  # Set the new chat as active

# Function to switch between chats
def switch_chat(chat_name):
    st.session_state.active_chat = chat_name

st.logo(image="images/chatbot.png", size="large")

# Sidebar for chat management
with st.sidebar:
    # with st.container:
    st.header("Chats")
    # Button to create a new chat
    if st.button("New Chat"):
        create_new_chat()
    # Display list of chats and allow switching
    for chat_name in st.session_state.chat_history:
        if st.button(chat_name):
            switch_chat(chat_name)

@st.dialog("Model Prarameters settings")
def set_model_params():

    st.write("Max output tokens")

    max_output_tokens = st.slider(label="",min_value=1, max_value=1000, value=50)
    temperature = st.slider("temperature", min_value=1, max_value=1000, value=50)
    top_p = st.slider("top_p", min_value=1, max_value=1000, value=50)
    top_k = st.slider("tok_k", min_value=1, max_value=1000, value=50)
    penealty = st.slider("penealty", min_value=1, max_value=1000, value=50)
    
    submit = st.button(label="Submit")

# st.info('This is a purely informational message', icon="ℹ️")
with st.container():
    on = st.toggle("Change Model Default Parameters")

    if on:
        # with st.container:
        if st.button(label="Model Settings"):
            set_model_params()

    # Display chat header
    st.title("Simple Q&A Chatbot")
    st.markdown("Ask me a question, and I'll try to answer!")

# Display the active chat
if st.session_state.active_chat:
    st.header(st.session_state.active_chat)
    with st.container():
        # Display chat history
        for message in st.session_state.chat_history[st.session_state.active_chat]:
            
            with st.chat_message(message["role"]):
                st.write(message["content"])
    
    # Input for new message
    user_input = st.chat_input("Type your message here...")
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history[st.session_state.active_chat].append({"role": "user", "content": user_input})
        # Simulate a bot response (you can replace this with an actual AI model)
        

        url = "http://localhost:8000/chat"

        payload = json.dumps(
            {
                "question": user_input
            }
        )
        headers = {
        'Content-Type': 'application/json'
        }
        with st.spinner("Wait for it...", show_time=True):
            response = requests.request("POST", url, headers=headers, data=payload)

            print(type(response.text))
            # bot_response = f"Bot: You said '{user_input}'"
            bot_response = json.loads(response.text)
            # print(bot_response["response"])
            st.session_state.chat_history[st.session_state.active_chat].append({"role": "assistant", "content": bot_response["response"]})
            # Rerun to update the chat interface
        st.rerun()
else:
    st.write("No active chat. Create a new chat from the sidebar.")