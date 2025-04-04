import os
from typing import List, Dict, Optional, Union
import uuid
from base64 import b64encode
import tempfile


def create_session() -> str:
    session_id = uuid.uuid4().hex

    return session_id

def generate_summary()->str:
    summary = """

        Introduction
        LangChain is a framework for developing applications powered by large language models (LLMs).

        LangChain simplifies every stage of the LLM application lifecycle:

        Development: Build your applications using LangChain's open-source components and third-party integrations. Use LangGraph to build stateful agents with first-class streaming and human-in-the-loop support.
        Productionization: Use LangSmith to inspect, monitor and evaluate your applications, so that you can continuously optimize and deploy with confidence.
        Deployment: Turn your LangGraph applications into production-ready APIs and Assistants with LangGraph Platform.

    """

    return summary

def process_file(uploaded_file ) -> Optional[Dict[str,str]] :
    """Process the uploaded file based on its type"""
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        # Process based on file type
        if uploaded_file.type == "application/pdf":
            file_type = "PDF"
            
        elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
                                  "application/msword"]:
            file_type = "DOCX"
            
        elif uploaded_file.type == "text/plain":
            file_type = "TXT"
            
        else:
            raise ValueError("Unsupported file type")
            
        # Clean up temp file
        os.unlink(tmp_file_path)
        
        return {
            "file_type": file_type,
            "file_name": uploaded_file.name,
            "file_path": tmp_file_path
        }
        
    except Exception as e:
        if os.path.exists(tmp_file_path):
            os.unlink(tmp_file_path)
        st.error(f"Error processing file: {str(e)}")
        return None
    
def qna()->str:
    return "Hi sagar"

    