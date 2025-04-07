# # import streamlit as st
# # from PyPDF2 import PdfReader
# # import os
# # from typing import List, Dict, Optional, Union
# # import uuid
# # from base64 import b64encode
# # import tempfile
# # from supporting_methods import create_session, generate_summary, qna
# # import time

# # ########################################################### V A R I A B L E S #####################################################
# # # Initialize session state for chat input availability
# # if "input_disabled" not in st.session_state:
# #     st.session_state.input_disabled = True

# # # session_id = uuid.uuid4().hex
# # if 'chat_history' not in st.session_state:
# #     st.session_state.chat_history = []

# # # Initialize session state for sidebar if it doesn't exist
# # if 'sidebar_state' not in st.session_state:
# #     st.session_state.sidebar_state = 'collapsed'


# # uploaded_file = None
# # file_uploaded : bool = False
# # reset_file : bool = False
# # st.session_state.current_session_id : str = None

# # ########################################################### F u n c t i o n s #####################################################
# # def chat_input_action():
# #     st.session_state.chat_history.append(
# #         {"role": "user", "content": st.session_state["chat_input"]},
# #     )

# #     st.session_state.chat_history.append(
# #         {
# #             "role": "assistant",
# #             "content": qna(),
# #         },  # This can be replaced with your chat response logic
# #     )

# # # print(session_id)



# # # Function to toggle sidebar
# # def toggle_sidebar():
# #     st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'

# # # Set the sidebar state
# # st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state,page_title="Ask your PDF")


# # # Sidebar for chat management
# # with st.sidebar:
# #     # with st.container:
# #     st.header("Configurations")

# #     # Get OpenAI API key
# #     openai_api_key = st.text_input("Enter your OpenAI API key", type="password")


# # st.header("Ask your PDF 💬")


# # if uploaded_file is None:
   
# #     # File uploader
# #     uploaded_file = st.file_uploader(
# #         "Choose a file", 
# #         type=["pdf", "docx", "doc", "txt"],
# #         accept_multiple_files=False
# #     )

# #     col1, col2 = st.columns(2)

# #     with col1:

# #         if uploaded_file is not None:
# #             file_uploaded = st.button(label="Submit", type="primary")
# #             if file_uploaded:
# #                 st.session_state.current_session_id = create_session()
# #                 print(st.session_state.current_session_id)

# #     # with col2:
# #     #     if file_uploaded:
# #     #         reset_file = st.button(label="Reset", type="primary")
# #     #         uploaded_file = None
# #     #         st.session_state.current_session_id = None
# #     #         file_uploaded = False

# # # Show user input
# # # st.chat_input("Ask a question about your document:", on_submit=chat_input_action, key="chat_input", disabled=chat_disabled)
# # # Placeholder for our custom chat input
# # chat_container = st.empty()

# # # Show disabled or enabled input based on state
# # if st.session_state.input_disabled:
# #     # Disabled chat input (shows grayed out)
# #     chat_container.chat_input("Processing...", disabled=True)
# # else:
# #     # Enabled chat input
# #     st.session_state.input_disabled = False
# #     user_input = chat_container.chat_input("Your message...", on_submit=chat_input_action, key="chat_input", disabled=st.session_state.input_disabled)
    
# #     # if user_input:
# #     #     st.session_state.input_disabled = True
# #     #     st.rerun()  # Rerun to immediately show disabled state


# # if st.session_state.current_session_id is not None:

    
            
# #     with st.spinner("Wait for it...", show_time=True):
# #         time.sleep(3)

# #         summary = generate_summary()
        
# #         st.session_state.chat_history.append(
# #             {
# #                 "role": "assistant",
# #                 "content": summary,
# #             },  # This can be replaced with your chat response logic
# #         )
# #         st.session_state.input_disabled = False
# #         st.rerun()
        
# #     # Display chat history
# #     for message in st.session_state.chat_history:
        
# #         with st.chat_message(message["role"]):
# #             st.write(message["content"])
    


        
# # import streamlit as st
# # from PyPDF2 import PdfReader
# # import os
# # from typing import List, Dict, Optional, Union
# # import uuid
# # from base64 import b64encode
# # import tempfile
# # from supporting_methods import create_session, generate_summary, qna
# # import time

# # ########################################################### V A R I A B L E S #####################################################
# # # Initialize session states
# # if "input_disabled" not in st.session_state:
# #     st.session_state.input_disabled = True

# # if 'chat_history' not in st.session_state:
# #     st.session_state.chat_history = []

# # if 'sidebar_state' not in st.session_state:
# #     st.session_state.sidebar_state = 'collapsed'

# # if 'current_session_id' not in st.session_state:
# #     st.session_state.current_session_id = None

# # if 'file_processed' not in st.session_state:
# #     st.session_state.file_processed = False

# # if 'openai_api_key' not in st.session_state:
# #     st.session_state.openai_api_key = None

# # ########################################################### F u n c t i o n s #####################################################
# # def chat_input_action():
# #     user_input = st.session_state.chat_input
# #     if user_input:
# #         st.session_state.chat_history.append({"role": "user", "content": user_input})
# #         st.session_state.input_disabled = True  # Disable input while processing
# #         st.session_state.pending_response = True
# #         st.rerun()

# # def process_file_and_generate_summary():
# #     """Process the file and generate summary"""
# #     st.session_state.current_session_id = create_session()
# #     with st.spinner("Processing your document...", show_time=True):
# #         time.sleep(2.5)
# #         summary = generate_summary()
# #         st.session_state.chat_history.append({"role": "assistant", "content": summary})
# #         st.session_state.file_processed = True
# #         st.session_state.input_disabled = False  # Enable input after processing
# #     st.rerun()

# # def generate_response():
# #     """Generate response to user query"""
# #     with st.spinner("Thinking...", show_time=True):
# #         time.sleep(4)
# #         response = qna()
# #         st.session_state.chat_history.append({"role": "assistant", "content": response})
# #         st.session_state.input_disabled = False  # Re-enable input
# #     st.rerun()

# # # Function to toggle sidebar
# # def toggle_sidebar():
# #     st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'


# # ########################################################### U I #####################################################
# # # Set page config
# # st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state, page_title="Ask your PDF")

# # # Sidebar for chat management
# # with st.sidebar:
# #     st.header("Configurations")
# #     st.session_state.openai_api_key = st.text_input("Enter your OpenAI API key", type="password")

# # st.header("Ask your PDF 💬")

# # # File upload section
# # uploaded_file = st.file_uploader(
# #     "Choose a file", 
# #     type=["pdf", "docx", "doc", "txt"],
# #     accept_multiple_files=False
# # )

# # # Submit button for file processing
# # if uploaded_file is not None and not st.session_state.file_processed:
# #     if st.button("Submit", type="primary"):
# #         if st.session_state.openai_api_key is None:
# #             toggle_sidebar()
        
# #         process_file_and_generate_summary()

# # # Chat interface
# # if st.session_state.file_processed:
# #     # Display chat history
# #     for message in st.session_state.chat_history:
# #         with st.chat_message(message["role"]):
# #             st.write(message["content"])
    
# #     # Chat input (state managed by session_state.input_disabled)
# #     if st.session_state.input_disabled and hasattr(st.session_state, 'pending_response'):
# #         generate_response()
# #     else:
# #         st.chat_input(
# #             "Ask a question about your document",
# #             on_submit=chat_input_action,
# #             key="chat_input",
# #             disabled=st.session_state.input_disabled
# #         )

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
# # Initialize all session states
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

# if 'current_file' not in st.session_state:
#     st.session_state.current_file = None

# if 'openai_api_key' not in st.session_state:
#     st.session_state.openai_api_key = ""

# ########################################################### F u n c t i o n s #####################################################
# def chat_input_action():
#     if not st.session_state.openai_api_key:
#         st.session_state.sidebar_state = 'expanded'
#         st.toast("Please enter your OpenAI API key first", icon="🔑")
#         st.rerun()
        
#     user_input = st.session_state.chat_input
#     if user_input:
#         st.session_state.chat_history.append({"role": "user", "content": user_input})
#         st.session_state.input_disabled = True  # Disable input while processing
#         st.session_state.pending_response = True
#         st.rerun()

# def process_file_and_generate_summary():
#     """Process the file and generate summary"""
#     if not st.session_state.openai_api_key:
#         st.session_state.sidebar_state = 'expanded'
#         st.toast("Please enter your OpenAI API key first", icon="🔑")
#         st.rerun()
    
#     st.session_state.current_session_id = create_session()
#     st.session_state.current_file = uploaded_file
#     with st.spinner("Processing your document..."):
#         summary = generate_summary()
#         st.session_state.chat_history.append({"role": "assistant", "content": summary})
#         st.session_state.file_processed = True
#         st.session_state.input_disabled = False  # Enable input after processing
#     st.rerun()

# def generate_response():
#     """Generate response to user query"""
#     if not st.session_state.openai_api_key:
#         st.session_state.sidebar_state = 'expanded'
#         st.toast("Please enter your OpenAI API key first", icon="🔑")
#         st.rerun()
        
#     with st.spinner("Thinking..."):
#         response = qna()
#         st.session_state.chat_history.append({"role": "assistant", "content": response})
#         st.session_state.input_disabled = False  # Re-enable input
#     st.rerun()

# def reset_file():
#     """Reset the current file while maintaining chat history"""
#     st.session_state.current_file = None
#     st.session_state.file_processed = False
#     st.session_state.input_disabled = True
#     st.rerun()

# ########################################################### U I #####################################################
# # Set page config
# st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state, page_title="Ask your PDF")

# # Sidebar for configuration
# with st.sidebar:
#     st.header("Configurations")
    
#     # API key input with save button
#     new_api_key = st.text_input("Enter your OpenAI API key", 
#                               value=st.session_state.openai_api_key,
#                               type="password",
#                               key="new_api_key_input")
    
#     if st.button("Save API Key"):
#         st.session_state.openai_api_key = new_api_key
#         st.toast("API Key saved!", icon="✅")
#         st.session_state.sidebar_state = 'collapsed'
#         st.rerun()
    
#     # File reset option
#     if st.session_state.current_file:
#         st.divider()
#         st.header("File Management")
#         if st.button("Change Document", type="secondary"):
#             reset_file()
    
#     # Display current file info
#     if st.session_state.current_file:
#         st.divider()
#         st.subheader("Current Document")
#         st.write(f"📄 {st.session_state.current_file.name}")

# st.header("Ask your PDF 💬")

# # File upload section
# uploaded_file = st.file_uploader(
#     "Choose a file", 
#     type=["pdf", "docx", "doc", "txt"],
#     accept_multiple_files=False,
#     key="file_uploader"
# )

# # Submit button for file processing
# if uploaded_file is not None and not st.session_state.file_processed:
#     if st.button("Submit", type="primary", key="submit_button"):
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

# import streamlit as st
# import time
# import random

# def extract_text(file):
#     """
#     Placeholder function to extract text from uploaded files
#     This would be replaced with actual extraction logic for different file types
#     """
#     return "This is sample extracted text from the document. It contains information about artificial intelligence, machine learning, and natural language processing. This text would normally be the actual content of your uploaded document."

# def generate_summary(text, api_key):
#     """
#     Placeholder function for generating summary using OpenAI API
#     """
#     # In a real implementation, this would call the OpenAI API
#     time.sleep(2)  # Simulate API call delay
#     return "This document discusses advances in AI technology, focusing on natural language processing and its applications in various industries. The text highlights key developments in machine learning models and their impact on business processes."

# def get_ai_response(query, context, api_key):
#     """
#     Placeholder function for AI Q&A using OpenAI API
#     """
#     # In a real implementation, this would call the OpenAI API with the context and query
#     time.sleep(1)  # Simulate API call delay
#     responses = [
#         f"Based on the document, the answer to '{query}' is related to AI technologies and their implementations.",
#         f"The document suggests that '{query}' can be addressed through natural language processing techniques.",
#         f"According to the text, '{query}' is connected to recent developments in machine learning applications."
#     ]
#     return random.choice(responses)


# st.set_page_config(
#     page_title="Document Q&A Assistant",
#     page_icon="📚",
#     layout="wide"
# )

# # Initialize session state variables if they don't exist
# if 'welcome_completed' not in st.session_state:
#     st.session_state.welcome_completed = False
# if 'document_text' not in st.session_state:
#     st.session_state.document_text = ""
# if 'api_key' not in st.session_state:
#     st.session_state.api_key = ""
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []
# if 'summary' not in st.session_state:
#     st.session_state.summary = ""

# # Welcome dialog
# if not st.session_state.welcome_completed:
#     st.title("Welcome to Document Q&A Assistant")
    
#     with st.container():
#         st.write("Please provide a document or text for analysis and your OpenAI API key.")
        
#         # Create columns for the two options
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.subheader("Option 1: Upload a document")
#             uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])
#             if uploaded_file is not None:
#                 st.session_state.document_text = extract_text(uploaded_file)
#                 st.success(f"File {uploaded_file.name} uploaded successfully!")
        
#         with col2:
#             st.subheader("Option 2: Paste text")
#             pasted_text = st.text_area("Or paste your text here:", height=150)
#             if pasted_text:
#                 st.session_state.document_text = pasted_text
    
#     # API Key input
#     st.subheader("OpenAI API Key (Required)")
#     api_key = st.text_input("Enter your OpenAI API Key:", type="password")
#     if api_key:
#         st.session_state.api_key = api_key
    
#     # Submit button with validation
#     if st.button("Submit and Generate Summary"):
#         if not st.session_state.api_key:
#             st.error("⚠️ Please enter your OpenAI API key to continue.")
#         elif not st.session_state.document_text:
#             st.error("⚠️ Please either upload a file or paste text to continue.")
#         else:
#             with st.spinner("Generating summary..."):
#                 summary = generate_summary(st.session_state.document_text, st.session_state.api_key)
#                 st.session_state.summary = summary
#                 st.session_state.welcome_completed = True
#                 st.experimental_rerun()

# # Main chat interface after welcome is completed
# else:
#     st.title("Document Q&A Assistant")
    
#     # Display summary
#     with st.expander("Document Summary", expanded=True):
#         st.write(st.session_state.summary)
    
#     # Chat interface
#     st.subheader("Ask questions about your document")
    
#     # Display chat history
#     chat_container = st.container()
#     with chat_container:
#         for message in st.session_state.chat_history:
#             if message["role"] == "user":
#                 st.write(f"🧑 **You:** {message['content']}")
#             else:
#                 st.write(f"🤖 **Assistant:** {message['content']}")
    
#     # Input for new questions
#     user_question = st.text_input("Your question:")
#     if st.button("Ask") and user_question:
#         # Add user question to chat history
#         st.session_state.chat_history.append({
#             "role": "user",
#             "content": user_question
#         })
        
#         # Get and display AI response
#         with st.spinner("Thinking..."):
#             response = get_ai_response(user_question, st.session_state.document_text, st.session_state.api_key)
#             st.session_state.chat_history.append({
#                 "role": "assistant",
#                 "content": response
#             })
        
#         # Force a rerun to update the chat display
#         st.experimental_rerun()
    
#     # Option to reset and start over
#     if st.button("Reset and Upload New Document"):
#         st.session_state.welcome_completed = False
#         st.session_state.document_text = ""
#         st.session_state.chat_history = []
#         st.session_state.summary = ""
#         st.experimental_rerun()

import streamlit as st
import os

# Dummy function to simulate text extraction
def extract_text(file):
    # This is a dummy function that doesn't actually extract text
    return "This is dummy text extracted from the uploaded file. In a real application, this would contain the actual content of the file."

# Dummy function to simulate OpenAI API call
def call_openai_chat_model(prompt, api_key, context):
    # In a real app, you would use the actual OpenAI API here
    # This is just a simulation that returns dummy responses
    
    if "summarize" in prompt.lower():
        return "This is a sample summary of the provided text. The text discusses various topics and contains important information that would be summarized here in a real application."
    
    responses = {
        "what is this about?": "This is about the content you uploaded or pasted. In a real app, I would analyze it properly.",
        "tell me more": "The document contains detailed information that would be analyzed here. It might include key points, arguments, or data.",
        "explain": "The explanation would be based on the actual content of your document or pasted text.",
        "hello": "Hello! I'm your document assistant. How can I help you with your document today?",
        "hi": "Hi there! I'm ready to answer questions about your document."
    }
    
    return responses.get(prompt.lower(), "I'm a dummy response simulating what the AI would say about your document or text.")

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'text_content' not in st.session_state:
    st.session_state.text_content = ""
if 'welcome_done' not in st.session_state:
    st.session_state.welcome_done = False
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False
if 'text_pasted' not in st.session_state:
    st.session_state.text_pasted = False

# Welcome dialog - only show if not already done
if not st.session_state.welcome_done:
    st.title("Welcome to Document Chat Assistant")
    st.write("This app allows you to upload a document or paste text, then ask questions about it.")
    
    # Options for input
    input_method = st.radio("Choose your input method:", ("Upload a file (PDF, TXT, DOCX)", "Paste text directly"))
    
    # File upload or text area based on selection
    if input_method == "Upload a file (PDF, TXT, DOCX)":
        uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'txt', 'docx'])
        if uploaded_file is not None:
            st.session_state.text_content = extract_text(uploaded_file)
            st.session_state.file_uploaded = True
    else:
        pasted_text = st.text_area("Paste your text here:", height=200)
        if pasted_text.strip() != "":
            st.session_state.text_content = pasted_text
            st.session_state.text_pasted = True
    
    # API key input
    st.session_state.api_key = st.text_input("Enter your OpenAI API key:", type="password")
    
    # Submit button with validation
    if st.button("Submit"):
        if not st.session_state.api_key:
            st.error("Please enter your OpenAI API key.")
        elif not st.session_state.file_uploaded and not st.session_state.text_pasted:
            st.error("Please either upload a file or paste some text.")
        else:
            st.session_state.welcome_done = True
            # Add welcome message from assistant
            st.session_state.messages.append({"role": "assistant", "content": "Welcome! I've processed your document. Here's a sample summary:"})
            
            # Generate sample summary
            summary = call_openai_chat_model("Please summarize this", st.session_state.api_key, st.session_state.text_content)
            st.session_state.messages.append({"role": "assistant", "content": summary})
            st.session_state.messages.append({"role": "assistant", "content": "You can now ask me questions about your document."})
            
            st.rerun()
    
    st.stop()  # Stop execution here until welcome is done

# Main app after welcome is done
st.title("Document Chat Assistant")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your document..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = call_openai_chat_model(prompt, st.session_state.api_key, st.session_state.text_content)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})