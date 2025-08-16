"""
Web interface for the climate data chatbot.
"""

import streamlit as st
from pages.chatbot import show_chatbot

def main():
    """Main web interface"""
    st.set_page_config(
        page_title="Climate Data Assistant",
        page_icon="🌡️",
        layout="centered"
    )
    
    show_chatbot()

if __name__ == "__main__":
    main() 