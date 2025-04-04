# import streamlit as st
# from PyPDF2 import PdfReader
# import os
# from typing import List, Dict, Optional, Union
# import uuid
# from base64 import b64encode
# import tempfile
# from supporting_methods import create_session, generate_summary, qna
# import time

# ########################################################### V A R I A B L E S #####################################################
# # Initialize session state for chat input availability
# if "input_disabled" not in st.session_state:
#     st.session_state.input_disabled = True

# # session_id = uuid.uuid4().hex
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# # Initialize session state for sidebar if it doesn't exist
# if 'sidebar_state' not in st.session_state:
#     st.session_state.sidebar_state = 'collapsed'


# uploaded_file = None
# file_uploaded : bool = False
# reset_file : bool = False
# st.session_state.current_session_id : str = None

# ########################################################### F u n c t i o n s #####################################################
# def chat_input_action():
#     st.session_state.chat_history.append(
#         {"role": "user", "content": st.session_state["chat_input"]},
#     )

#     st.session_state.chat_history.append(
#         {
#             "role": "assistant",
#             "content": qna(),
#         },  # This can be replaced with your chat response logic
#     )

# # print(session_id)



# # Function to toggle sidebar
# def toggle_sidebar():
#     st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'

# # Set the sidebar state
# st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state,page_title="Ask your PDF")


# # Sidebar for chat management
# with st.sidebar:
#     # with st.container:
#     st.header("Configurations")

#     # Get OpenAI API key
#     openai_api_key = st.text_input("Enter your OpenAI API key", type="password")


# st.header("Ask your PDF 💬")


# if uploaded_file is None:
   
#     # File uploader
#     uploaded_file = st.file_uploader(
#         "Choose a file", 
#         type=["pdf", "docx", "doc", "txt"],
#         accept_multiple_files=False
#     )

#     col1, col2 = st.columns(2)

#     with col1:

#         if uploaded_file is not None:
#             file_uploaded = st.button(label="Submit", type="primary")
#             if file_uploaded:
#                 st.session_state.current_session_id = create_session()
#                 print(st.session_state.current_session_id)

#     # with col2:
#     #     if file_uploaded:
#     #         reset_file = st.button(label="Reset", type="primary")
#     #         uploaded_file = None
#     #         st.session_state.current_session_id = None
#     #         file_uploaded = False

# # Show user input
# # st.chat_input("Ask a question about your document:", on_submit=chat_input_action, key="chat_input", disabled=chat_disabled)
# # Placeholder for our custom chat input
# chat_container = st.empty()

# # Show disabled or enabled input based on state
# if st.session_state.input_disabled:
#     # Disabled chat input (shows grayed out)
#     chat_container.chat_input("Processing...", disabled=True)
# else:
#     # Enabled chat input
#     st.session_state.input_disabled = False
#     user_input = chat_container.chat_input("Your message...", on_submit=chat_input_action, key="chat_input", disabled=st.session_state.input_disabled)
    
#     # if user_input:
#     #     st.session_state.input_disabled = True
#     #     st.rerun()  # Rerun to immediately show disabled state


# if st.session_state.current_session_id is not None:

    
            
#     with st.spinner("Wait for it...", show_time=True):
#         time.sleep(3)

#         summary = generate_summary()
        
#         st.session_state.chat_history.append(
#             {
#                 "role": "assistant",
#                 "content": summary,
#             },  # This can be replaced with your chat response logic
#         )
#         st.session_state.input_disabled = False
#         st.rerun()
        
#     # Display chat history
#     for message in st.session_state.chat_history:
        
#         with st.chat_message(message["role"]):
#             st.write(message["content"])
    


        
# import streamlit as st
# from PyPDF2 import PdfReader
# import os
# from typing import List, Dict, Optional, Union
# import uuid
# from base64 import b64encode
# import tempfile
# from supporting_methods import create_session, generate_summary, qna
# import time

# ########################################################### V A R I A B L E S #####################################################
# # Initialize session states
# if "input_disabled" not in st.session_state:
#     st.session_state.input_disabled = True

# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# if 'sidebar_state' not in st.session_state:
#     st.session_state.sidebar_state = 'collapsed'

# if 'current_session_id' not in st.session_state:
#     st.session_state.current_session_id = None

# if 'file_processed' not in st.session_state:
#     st.session_state.file_processed = False

# if 'openai_api_key' not in st.session_state:
#     st.session_state.openai_api_key = None

# ########################################################### F u n c t i o n s #####################################################
# def chat_input_action():
#     user_input = st.session_state.chat_input
#     if user_input:
#         st.session_state.chat_history.append({"role": "user", "content": user_input})
#         st.session_state.input_disabled = True  # Disable input while processing
#         st.session_state.pending_response = True
#         st.rerun()

# def process_file_and_generate_summary():
#     """Process the file and generate summary"""
#     st.session_state.current_session_id = create_session()
#     with st.spinner("Processing your document...", show_time=True):
#         time.sleep(2.5)
#         summary = generate_summary()
#         st.session_state.chat_history.append({"role": "assistant", "content": summary})
#         st.session_state.file_processed = True
#         st.session_state.input_disabled = False  # Enable input after processing
#     st.rerun()

# def generate_response():
#     """Generate response to user query"""
#     with st.spinner("Thinking...", show_time=True):
#         time.sleep(4)
#         response = qna()
#         st.session_state.chat_history.append({"role": "assistant", "content": response})
#         st.session_state.input_disabled = False  # Re-enable input
#     st.rerun()

# # Function to toggle sidebar
# def toggle_sidebar():
#     st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'


# ########################################################### U I #####################################################
# # Set page config
# st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state, page_title="Ask your PDF")

# # Sidebar for chat management
# with st.sidebar:
#     st.header("Configurations")
#     st.session_state.openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

# st.header("Ask your PDF 💬")

# # File upload section
# uploaded_file = st.file_uploader(
#     "Choose a file", 
#     type=["pdf", "docx", "doc", "txt"],
#     accept_multiple_files=False
# )

# # Submit button for file processing
# if uploaded_file is not None and not st.session_state.file_processed:
#     if st.button("Submit", type="primary"):
#         if st.session_state.openai_api_key is None:
#             toggle_sidebar()
        
#         process_file_and_generate_summary()

# # Chat interface
# if st.session_state.file_processed:
#     # Display chat history
#     for message in st.session_state.chat_history:
#         with st.chat_message(message["role"]):
#             st.write(message["content"])
    
#     # Chat input (state managed by session_state.input_disabled)
#     if st.session_state.input_disabled and hasattr(st.session_state, 'pending_response'):
#         generate_response()
#     else:
#         st.chat_input(
#             "Ask a question about your document",
#             on_submit=chat_input_action,
#             key="chat_input",
#             disabled=st.session_state.input_disabled
#         )

import streamlit as st
from PyPDF2 import PdfReader
import os
from typing import List, Dict, Optional, Union
import uuid
from base64 import b64encode
import tempfile
from supporting_methods import create_session, generate_summary, qna
import time

########################################################### V A R I A B L E S #####################################################
# Initialize all session states
if "input_disabled" not in st.session_state:
    st.session_state.input_disabled = True

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

if 'current_session_id' not in st.session_state:
    st.session_state.current_session_id = None

if 'file_processed' not in st.session_state:
    st.session_state.file_processed = False

if 'current_file' not in st.session_state:
    st.session_state.current_file = None

if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""

########################################################### F u n c t i o n s #####################################################
def chat_input_action():
    if not st.session_state.openai_api_key:
        st.session_state.sidebar_state = 'expanded'
        st.toast("Please enter your OpenAI API key first", icon="🔑")
        st.rerun()
        
    user_input = st.session_state.chat_input
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.input_disabled = True  # Disable input while processing
        st.session_state.pending_response = True
        st.rerun()

def process_file_and_generate_summary():
    """Process the file and generate summary"""
    if not st.session_state.openai_api_key:
        st.session_state.sidebar_state = 'expanded'
        st.toast("Please enter your OpenAI API key first", icon="🔑")
        st.rerun()
    
    st.session_state.current_session_id = create_session()
    st.session_state.current_file = uploaded_file
    with st.spinner("Processing your document..."):
        summary = generate_summary()
        st.session_state.chat_history.append({"role": "assistant", "content": summary})
        st.session_state.file_processed = True
        st.session_state.input_disabled = False  # Enable input after processing
    st.rerun()

def generate_response():
    """Generate response to user query"""
    if not st.session_state.openai_api_key:
        st.session_state.sidebar_state = 'expanded'
        st.toast("Please enter your OpenAI API key first", icon="🔑")
        st.rerun()
        
    with st.spinner("Thinking..."):
        response = qna()
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.session_state.input_disabled = False  # Re-enable input
    st.rerun()

def reset_file():
    """Reset the current file while maintaining chat history"""
    st.session_state.current_file = None
    st.session_state.file_processed = False
    st.session_state.input_disabled = True
    st.rerun()

########################################################### U I #####################################################
# Set page config
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state, page_title="Ask your PDF")

# Sidebar for configuration
with st.sidebar:
    st.header("Configurations")
    
    # API key input with save button
    new_api_key = st.text_input("Enter your OpenAI API key", 
                              value=st.session_state.openai_api_key,
                              type="password",
                              key="new_api_key_input")
    
    if st.button("Save API Key"):
        st.session_state.openai_api_key = new_api_key
        st.toast("API Key saved!", icon="✅")
        st.session_state.sidebar_state = 'collapsed'
        st.rerun()
    
    # File reset option
    if st.session_state.current_file:
        st.divider()
        st.header("File Management")
        if st.button("Change Document", type="secondary"):
            reset_file()
    
    # Display current file info
    if st.session_state.current_file:
        st.divider()
        st.subheader("Current Document")
        st.write(f"📄 {st.session_state.current_file.name}")

st.header("Ask your PDF 💬")

# File upload section
uploaded_file = st.file_uploader(
    "Choose a file", 
    type=["pdf", "docx", "doc", "txt"],
    accept_multiple_files=False,
    key="file_uploader"
)

# Submit button for file processing
if uploaded_file is not None and not st.session_state.file_processed:
    if st.button("Submit", type="primary", key="submit_button"):
        process_file_and_generate_summary()

# Chat interface
if st.session_state.file_processed:
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input (state managed by session_state.input_disabled)
    if st.session_state.input_disabled and hasattr(st.session_state, 'pending_response'):
        generate_response()
    else:
        st.chat_input(
            "Ask a question about your document",
            on_submit=chat_input_action,
            key="chat_input",
            disabled=st.session_state.input_disabled
        )