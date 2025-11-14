from typing import Set
from backend.core import run_llm
import streamlit as st


# Configure page - ChatGPT-like layout
st.set_page_config(
    page_title="Documentation Helper",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ChatGPT-inspired CSS styling
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    /* ChatGPT-like dark theme */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #ffffff !important;
        color: #0d0d0d !important;
    }
    
    /* Sidebar - Smooth 20% width */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        width: 20% !important;
        min-width: 20% !important;
        padding: 1.5rem 1rem !important;
        border-right: 1px solid #e5e5e5;
        overflow-y: auto;
        scroll-behavior: smooth;
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        padding: 0 !important;
    }
    
    /* Main content area - 80% width */
    .main {
        background-color: #f7f7f7 !important;
        padding: 2rem 2.5rem !important;
        margin-left: 0 !important;
        width: 80% !important;
    }
    
    .block-container {
        padding: 0 !important;
        max-width: 100%;
        background-color: #f7f7f7 !important;
        width: 100% !important;
    }
    
    section[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f7f7f7 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Header - Clean and minimal ChatGPT style */
    .header-container {
        background: linear-gradient(135deg, #10a37f 0%, #1a9970 100%);
        padding: 2rem 2rem !important;
        border-radius: 12px;
        margin: 2.6rem 0 1.5rem 0 !important;
        color: white;
        text-align: center;
        box-shadow: 0 2px 10px rgba(16, 163, 127, 0.15);
        border: none;
    }
    
    .header-container h1 {
        margin: 0 !important;
        padding: 0 !important;
        font-size: 2.2rem;
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: -0.3px;
    }
    
    .header-container p {
        margin: 0.5rem 0 0 0 !important;
        padding: 0 !important;
        font-size: 0.95rem;
        opacity: 0.95;
        line-height: 1.5;
    }
    
    /* Input box - ChatGPT style */
    .input-box {
        background-color: white !important;
        padding: 1.25rem 1.5rem !important;
        border-radius: 12px;
        border: 1.5px solid #d1d5db;
        margin: 0 0 1.5rem 0 !important;
        transition: all 0.2s ease;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    
    .input-box:focus-within {
        border-color: #10a37f;
        box-shadow: 0 2px 12px rgba(16, 163, 127, 0.15);
    }
    
    /* Button styling - ChatGPT style */
    .stButton > button {
        background: linear-gradient(135deg, #10a37f 0%, #0d9364 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 6px rgba(16, 163, 127, 0.2) !important;
        font-size: 0.95rem !important;
        height: 44px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(16, 163, 127, 0.3) !important;
        background: linear-gradient(135deg, #0d9364 0%, #0a7f54 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* Text input styling - ChatGPT style */
    .stTextInput > div > div > input {
        background-color: #f7f7f7 !important;
        color: #0d0d0d !important;
        border: 1px solid #d1d5db !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #10a37f !important;
        box-shadow: 0 0 0 3px rgba(16, 163, 127, 0.1) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #9ca3af !important;
    }
    
    /* Profile card styling - ChatGPT style */
    .profile-card {
        background: white;
        padding: 1.2rem !important;
        border-radius: 12px;
        color: #0d0d0d;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        margin: 0 0 1rem 0 !important;
        border: 1px solid #e5e5e5;
    }
    
    .profile-card h3 {
        margin: 0 !important;
        padding: 0 !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.8rem !important;
        line-height: 1.2 !important;
        color: #0d0d0d;
    }
    
    .profile-emoji {
        font-size: 3.5rem;
        margin: 0.3rem 0 0.8rem 0 !important;
        line-height: 1 !important;
        filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.1));
    }
    
    .profile-info {
        margin: 1rem 0 0.5rem 0 !important;
        padding: 1rem 0 !important;
        border-top: 1px solid #e5e5e5;
        border-bottom: 1px solid #e5e5e5;
    }
    
    .info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0.6rem 0 !important;
        padding: 0 !important;
        font-size: 0.9rem;
        gap: 1rem;
        color: #0d0d0d;
    }
    
    .info-label {
        font-weight: 600;
        opacity: 0.7;
        text-align: left;
        flex: 0 0 auto;
        color: #565869;
    }
    
    .info-value {
        text-align: right;
        font-weight: 500;
        word-break: break-word;
        flex: 1;
        color: #0d0d0d;
    }
    
    /* Chat message styling - ChatGPT style */
    .chat-message {
        margin: 1rem 0 !important;
        padding: 1rem 1.5rem !important;
        border-radius: 8px;
        line-height: 1.6;
        font-size: 0.95rem;
        animation: slideIn 0.3s ease;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .user-message {
        background-color: #10a37f;
        border-left: none;
        margin-left: 3rem;
        margin-right: 0;
        color: white;
        border-radius: 8px;
    }
    
    .user-message strong {
        color: white;
        font-weight: 600;
    }
    
    .assistant-message {
        background-color: #f7f7f7;
        border-left: none;
        margin-right: 3rem;
        margin-left: 0;
        color: #0d0d0d;
        border: 1px solid #e5e5e5;
        border-radius: 8px;
    }
    
    .assistant-message strong {
        color: #0d0d0d;
        font-weight: 600;
    }
    
    /* Conversation header with proper spacing */
    .conversation-header {
        margin: 1.5rem 0 1rem 0 !important;
        padding: 0.75rem 0 !important;
        color: #0d0d0d;
        font-size: 1.1rem;
        font-weight: 700 !important;
        line-height: 1.2;
        border-bottom: 1px solid #e5e5e5;
    }
    
    /* Text styling */
    p, div, span {
        color: #e0e0e0 !important;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1f2e;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #2d3748;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #3a4556;
    }
    
    /* Tips box with proper spacing */
    .tips-box {
        background-color: #f0f4f8 !important;
        border: 1px solid #e1e4e8 !important;
        border-radius: 8px;
        padding: 1rem !important;
        margin: 1rem 0 !important;
    }
    
    .tips-box p {
        font-size: 0.85rem !important;
        margin: 0.3rem 0 !important;
        color: #0d0d0d;
    }
    
    /* Divider styling */
    hr {
        margin: 1rem 0 !important;
        border-color: #e5e5e5 !important;
    }
    
    /* General text styling */
    p, div, span {
        color: #0d0d0d !important;
    }
    
    /* Column container spacing */
    [data-testid="column"] {
        padding: 0 0.5rem !important;
    }
    
    /* Scrollbar styling - light theme */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f7f7f7;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #d1d5db;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a3a3a3;
    }
</style>
""", unsafe_allow_html=True)
    
# Initialize session state for logged in status
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = True

# Sidebar with user information
with st.sidebar:
    if st.session_state["logged_in"]:
        st.markdown("""
        <div class="profile-card">
            <h3>User Profile</h3>
            <div class="profile-emoji">👩</div>
            <div class="profile-info">
                <div class="info-row">
                    <span class="info-label">👤 Name</span>
                    <span class="info-value">Shreya C</span>
                </div>
                <div class="info-row">
                    <span class="info-label">📧 Email</span>
                    <span class="info-value">shreya@c.com</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        col1, col2 = st.columns(2, gap="small")
        with col1:
            if st.button("🔄 Refresh", key="refresh", use_container_width=True):
                st.session_state["user_prompt_history"] = []
                st.session_state["chat_answer_history"] = []
                st.session_state["chat_history"] = []
                st.rerun()
        
        with col2:
            if st.button("🚪 Logout", key="logout", use_container_width=True):
                st.session_state["logged_in"] = False
                st.rerun()
        
        st.divider()
        
        st.markdown("""
        <div class="tips-box">
            <p>💡 <strong>Tip:</strong> Ask questions about documentation and get AI-powered answers with source references.</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="tips-box" style="border-color: #fbbf24; background-color: #fef3c7;">
            <p style="color: #b45309;"><strong>🔐 Logged Out</strong></p>
            <p style="color: #b45309; font-size: 0.85rem;">Click the button below to log back in</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔓 Login Again", key="login_again", use_container_width=True):
            st.session_state["logged_in"] = True
            st.rerun()

# Main content header
st.markdown("""
<div class="header-container">
    <h1>📚 Langchain Documentation Helper</h1>
    <p>Get instant AI-powered answers to your documentation questions</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "chat_answer_history" not in st.session_state:
    st.session_state["chat_answer_history"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []



col1, col2 = st.columns([5, 1], gap="small")
with col1:
    prompt = st.text_input("💬 Ask your question", placeholder="What would you like to know about the documentation?", label_visibility="collapsed")
with col2:
    submit_button = st.button("🚀 Submit", key="submit_btn", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Add some spacing
st.markdown("")

def create_source_string(source_urls : Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "📚 **Sources:**\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if submit_button and prompt:
    with st.spinner("⏳ Generating response..."):
        # import time
        # time.sleep(3)
        generated_response = run_llm(query = prompt,chat_history = st.session_state["chat_history"])
        sources = set([doc.metadata["source"] for doc in generated_response["source_documents"]])

        formatted_response = f"{generated_response['result']} \n\n {create_source_string(sources)}"
        
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answer_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response['result']))
        
        st.rerun()

# Chat display section
if st.session_state["chat_answer_history"]:
    st.markdown('<h3 class="conversation-header">💬 Conversation History</h3>', unsafe_allow_html=True)
    
    for idx, (user_query, generated_response) in enumerate(zip(st.session_state["user_prompt_history"], st.session_state["chat_answer_history"])):
        # User message - aligned to right
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>👤 You</strong><br/>
            <span style="opacity: 0.95;">{user_query}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Assistant message - aligned to left  
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>🤖 Assistant</strong><br/>
            <span style="opacity: 0.95;">{generated_response}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("")  # Spacing between conversations