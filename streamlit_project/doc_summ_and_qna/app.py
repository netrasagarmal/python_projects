import streamlit as st
from PyPDF2 import PdfReader
import os
from typing import List, Dict, Optional, Union
import uuid
from base64 import b64encode
import tempfile
from supporting_methods import create_session, generate_summary, qna
import time



# session_id = uuid.uuid4().hex

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
# pdf = st.file_uploader("Upload your PDF", type="pdf")
uploaded_file = None
file_uploaded : bool = False
reset_file : bool = False
st.session_state.current_session_id : str= None


if uploaded_file is None:
   
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a file", 
        type=["pdf", "docx", "doc", "txt"],
        accept_multiple_files=False
    )

    col1, col2 = st.columns(2)

    with col1:

        if uploaded_file is not None:
            file_uploaded = st.button(label="Submit", type="primary")
            if file_uploaded:
                st.session_state.current_session_id = create_session()
                print(st.session_state.current_session_id)

    # with col2:
    #     if file_uploaded:
    #         reset_file = st.button(label="Reset", type="primary")
    #         uploaded_file = None
    #         st.session_state.current_session_id = None
    #         file_uploaded = False

if file_uploaded and st.session_state.current_session_id is not None:

    # Show user input
    user_input = st.chat_input("Ask a question about your PDF:")
            
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)

        summary = generate_summary()
        st.write(summary)

    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.spinner("Wait for it...", show_time=True):
            time.sleep(5)
            answer = qna()
            with st.chat_message("assistant"):
                st.write(answer)

        
        
        


    

