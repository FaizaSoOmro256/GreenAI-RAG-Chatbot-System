"""
Modern thematic chatbot UI component for the GreenAI application.
Provides an eye-catching animated UI for the climate assistant.
"""

import streamlit as st
import time
from datetime import datetime
import base64
import os
from utils.chatbot import ChatBot

# Load and encode the animation for the chatbot
def get_chatbot_animation_html():
    """
    Returns HTML for an animated robot-themed chatbot icon.
    Creates a modern, animated robot face with blinking eyes and pulsing effects.
    """
    return """
    <style>
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    @keyframes gradientBackground {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px #4ECDC4, 0 0 10px #4ECDC4, 0 0 15px #4ECDC4; }
        50% { box-shadow: 0 0 10px #4ECDC4, 0 0 20px #4ECDC4, 0 0 30px #4ECDC4; }
    }
    
    .chatbot-avatar {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        background: linear-gradient(135deg, #212121, #424242, #616161, #757575);
        background-size: 300% 300%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px auto;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        animation: pulse 3s infinite ease-in-out, gradientBackground 15s ease infinite;
        overflow: hidden;
        padding: 10px;
        position: relative;
    }
    
    .robot-head {
        position: relative;
        width: 85%;
        height: 85%;
    }
    
    .robot-face {
        position: absolute;
        width: 100%;
        height: 100%;
        background: #303030;
        border-radius: 20px;
        overflow: hidden;
    }
    
    .robot-eyes {
        position: absolute;
        top: 35%;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
    }
    
    .robot-eye {
        width: 18px;
        height: 10px;
        background: #4ECDC4;
        border-radius: 5px;
        animation: blink 3s infinite;
        box-shadow: 0 0 8px #4ECDC4;
    }
    
    .robot-mouth {
        position: absolute;
        bottom: 25%;
        left: 30%;
        width: 40%;
        height: 3px;
        background: #4ECDC4;
        box-shadow: 0 0 8px #4ECDC4;
        animation: glow 2s infinite;
    }
    
    .robot-antenna {
        position: absolute;
        top: -10%;
        left: 40%;
        width: 20%;
        height: 15%;
        background: #424242;
        border-radius: 50% 50% 0 0;
        box-shadow: 0 -2px 4px rgba(78, 205, 196, 0.5);
    }
    
    .robot-ear-left {
        position: absolute;
        left: -8%;
        top: 30%;
        width: 12%;
        height: 30%;
        background: #424242;
        border-radius: 5px 0 0 5px;
        box-shadow: -2px 0 4px rgba(78, 205, 196, 0.5);
    }
    
    .robot-ear-right {
        position: absolute;
        right: -8%;
        top: 30%;
        width: 12%;
        height: 30%;
        background: #424242;
        border-radius: 0 5px 5px 0;
        box-shadow: 2px 0 4px rgba(78, 205, 196, 0.5);
    }
    
    .chatbot-header {
        text-align: center;
        margin-bottom: 20px;
    }
    
    .chatbot-title {
        font-size: 24px;
        font-weight: bold;
        color: #4ECDC4;
        margin: 10px 0 5px 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .chatbot-subtitle {
        font-size: 16px;
        color: #555555;
        margin: 0 0 20px 0;
        max-width: 400px;
        margin: 0 auto;
    }
    
    .typing-indicator {
        display: flex;
        align-items: center;
        margin: 10px 0;
    }
    
    .typing-dot {
        height: 8px;
        width: 8px;
        margin: 0 2px;
        border-radius: 50%;
        background-color: #2E7D32;
        animation: typingAnimation 1.5s infinite ease-in-out;
    }
    
    .typing-dot:nth-child(1) { animation-delay: 0s; }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes typingAnimation {
        0% { transform: scale(1); opacity: 0.7; }
        50% { transform: scale(1.5); opacity: 1; }
        100% { transform: scale(1); opacity: 0.7; }
    }
    
    @keyframes slideIn {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    .slide-in {
        animation: slideIn 0.5s ease forwards;
    }
    
    .chatbot-container {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: 0 auto;
    }
    
    .message-container {
        max-height: 400px;
        overflow-y: auto;
        padding: 10px;
        border-radius: 10px;
        background: #f8f9fa;
        margin-bottom: 15px;
    }
    
    /* Dark mode support */
    .dark-mode .chatbot-container {
        background-color: #1e1e1e;
    }
    
    .dark-mode .message-container {
        background: #121212;
    }
    
    .dark-mode .chatbot-title {
        color: #81C784;
    }
    
    .dark-mode .chatbot-subtitle {
        color: #b0b0b0;
    }
    
    /* Simple chat input styling */
    .stTextInput > div > div > input {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 8px 12px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #4ECDC4;
        box-shadow: 0 0 0 2px rgba(78, 205, 196, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 10px;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:first-child {
        background-color: #4ECDC4;
        color: white;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    </style>
    
    <div class="chatbot-header">
        <div class="chatbot-avatar">
            <div class="robot-head">
                <div class="robot-antenna"></div>
                <div class="robot-ear-left"></div>
                <div class="robot-ear-right"></div>
                <div class="robot-face">
                    <div class="robot-eyes">
                        <div class="robot-eye"></div>
                        <div class="robot-eye"></div>
                    </div>
                    <div class="robot-mouth"></div>
                </div>
            </div>
        </div>
        <div class="chatbot-title">GreenAI Climate Assistant</div>
        <div class="chatbot-subtitle">Your AI assistant for climate information in Sindh</div>
    </div>
    """

def render_typing_animation():
    """
    Display a typing animation while waiting for a response.
    """
    return """
    <div class="typing-indicator">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    </div>
    """

def render_chatbot_interface(translations=None):
    """
    Render the modern chatbot interface with animations and theme support.
    
    Args:
        translations (dict, optional): Dictionary containing:
            - chat_desc: Description text for the chatbot
            - chat_placeholder: Placeholder text for the input field
            - response_generator: Function that takes user input and returns response
            If None, default translations will be used.
    """
    try:
        # Set default translations if none provided
        if translations is None:
            translations = {
                "chat_desc": "Your AI assistant for climate information in Sindh",
                "chat_placeholder": "Type your message here...",
                "response_generator": lambda x: "I'm sorry, no response generator was provided."
            }
        
        # Initialize messages in session state if they don't exist
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        # Apply theme class based on session state
        theme_class = "dark-mode" if st.session_state.get("theme", "light") == "dark" else ""
        
        # Render animated chatbot avatar and header
        st.markdown(get_chatbot_animation_html(), unsafe_allow_html=True)
        
        # Chat container
        chat_container = st.container()
        
        with chat_container:
            # Display chat messages
            for i, message in enumerate(st.session_state.messages):
                if message["is_user"]:
                    st.markdown(f"""
                    <div class="slide-in" style="display: flex; justify-content: flex-end; margin-bottom: 10px;">
                        <div style="background-color: #E8F5E9; padding: 12px 16px; border-radius: 18px 18px 0 18px; max-width: 80%; box-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                            <p style="margin: 0; color: #333;">{message["content"]}</p>
                            <div style="font-size: 0.7em; text-align: right; margin-top: 5px; opacity: 0.7;">
                                {message.get("timestamp", datetime.now().strftime("%H:%M"))}
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    content = message["content"]
                    content = content.replace("• ", "<span style='margin-right: 5px; color: #2E7D32;'>•</span>")
                    content = content.replace("\n", "<br>")
                    
                    st.markdown(f"""
                    <div class="slide-in" style="display: flex; margin-bottom: 10px;">
                        <div style="background-color: #F5F5F5; padding: 12px 16px; border-radius: 18px 18px 18px 0; max-width: 85%; box-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                            <p style="margin: 0; color: #333;">{content}</p>
                            <div style="font-size: 0.7em; margin-top: 5px; opacity: 0.7;">
                                {message.get("timestamp", datetime.now().strftime("%H:%M"))}
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        # Create form for chat input
        with st.form(key="chat_form", clear_on_submit=True):
            user_input = st.text_input(
                label="Message",
                placeholder=translations.get("chat_placeholder", "Type your message here..."),
                key="chat_input",
                label_visibility="collapsed"
            )
            
            col1, col2 = st.columns([5, 2])
            
            with col1:
                submit_button = st.form_submit_button(
                    "Send Message",
                    use_container_width=True,
                    type="primary"
                )
            
            with col2:
                clear_button = st.form_submit_button(
                    "Clear Chat",
                    type="secondary",
                    use_container_width=True
                )
        
        # Handle form submission
        if submit_button and user_input:
            # Add user message
            st.session_state.messages.append({
                "content": user_input,
                "is_user": True,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            
            # Get response using the provided generator
            try:
                response = translations.get("response_generator", lambda x: "No response generator provided.")(user_input)
            except Exception as e:
                response = f"I'm sorry, I couldn't process your request. Error: {str(e)}"
            
            # Add bot response
            st.session_state.messages.append({
                "content": response,
                "is_user": False,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            
            st.rerun()
            
        # Handle clear button click
        if clear_button:
            st.session_state.messages = []
            st.rerun()

        return chat_container
    
    except Exception as e:
        st.error(f"Error rendering chatbot interface: {str(e)}")
        # Fallback basic chat interface
        user_input = st.text_input("Your message:", key="fallback_input")
        submit_button = st.button("Send", key="fallback_send")
        clear_button = st.button("Clear Chat", key="fallback_clear")
        return user_input, submit_button, clear_button

def show_chatbot():
    """Initialize and display the chat interface."""
    
    # Initialize the chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = ChatBot()
    
    # Initialize messages if not already done
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add welcome message
        st.session_state.messages.append({
            "content": st.session_state.chatbot.get_welcome_message(),
            "is_user": False,
            "timestamp": datetime.now().strftime("%H:%M")
        })
    
    # Render the chat interface
    render_chatbot_interface({
        "chat_desc": "Your AI assistant for climate information in Sindh",
        "chat_placeholder": "Ask me about climate in any Sindh district...",
        "response_generator": st.session_state.chatbot.get_response
    }) 