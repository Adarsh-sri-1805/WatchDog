import streamlit as st
from datetime import datetime  # Add this import

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="SIA - Your Sentiment Intelligence Assistant",
    layout="wide",
    page_icon="🤖"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            height: calc(100vh - 120px);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            overflow: hidden;
            margin-top: 20px;
        }
        .control-panel {
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        iframe {
            flex-grow: 1;
            border: none;
        }
        .header {
            color: #1F4068;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTROL PANEL ---
with st.container():
    st.markdown('<h2 class="header">SIA - Sentiment Intelligence Assistant</h2>', unsafe_allow_html=True)
    
    with st.expander("⚙️ Control Panel", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Conversation Mode", ["Support", "Technical", "General"])
            
        with col2:
            st.selectbox("Knowledge Base", ["Current Month", "Last 3 Months", "All Time"])
            

    st.markdown("---")

# --- CHATBOT IFRAME ---
st.markdown("""
    <div class="chat-container">
        <iframe
            src="https://www.chatbase.co/chatbot-iframe/tQ8je6dCXo7fMtZxtqf9n"
            width="100%"
            frameborder="0"
            allow="microphone">
        </iframe>
    </div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; margin-top: 20px; color: #666; font-size: 12px;">
       • SIA v2.1 • Updated: {datetime.now().strftime('%Y-%m-%d')}
    </div>
""", unsafe_allow_html=True)
