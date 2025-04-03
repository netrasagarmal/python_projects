import streamlit as st
from PyPDF2 import PdfReader
import os

import uuid

session_id = uuid.uuid4().hex

# print(session_id)

# Initialize session state for sidebar if it doesn't exist
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

# Function to toggle sidebar
def toggle_sidebar():
    st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'

# Set the sidebar state
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state,page_title="Ask your PDF")



# Sidebar for chat management
with st.sidebar:
    # with st.container:
    st.header("Configurations")

    # Get OpenAI API key
    openai_api_key = st.text_input("Enter your OpenAI API key", type="password")


st.header("Ask your PDF 💬")

# Upload PDF file
pdf = st.file_uploader("Upload your PDF", type="pdf")


# Show user input
user_question = st.chat_input("Ask a question about your PDF:")

