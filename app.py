"""
GreenAI: An Intelligent RAG Chatbot for Sindh's Sustainable Climate Actions

A multilingual (English/Urdu/Sindhi) web-based application with a professional UI
that provides information about sustainable climate actions in Sindh.
"""

import streamlit as st
import time
import os
from dotenv import load_dotenv
import config

# Initialize critical session state variables first
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "language" not in st.session_state:
    st.session_state.language = "english"  # Default language
if "calculated_result" not in st.session_state:
    st.session_state.calculated_result = None
# Load environment variables
load_dotenv()


# Apply custom CSS
from utils.ui import apply_custom_css
apply_custom_css()

# Hide Streamlit branding
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Local imports - after initializing session state
from utils.ui import (
    render_footer,
    render_theme_toggle,
    apply_custom_css,
    render_sidebar,
)
from utils.chatbot_ui import show_chatbot
from pages.home import show_home
from pages.knowledge_base import show_knowledge_base
from pages.carbon_calculator import show_carbon_calculator
from pages.offsets_recommender import show_offsets_recommender
from pages.about import show_about
from pages.weather_dashboard import show_weather_dashboard
from pages.climate_tips import show_climate_tips
from pages.water_resources import show_water_resources

# Sidebar navigation
st.sidebar.title("GreenAI")
# Use text-based branding instead of image
st.sidebar.markdown("🤖 **Climate Action Platform**")

# Add theme toggle to sidebar
render_theme_toggle()

# Navigation menu
menu_options = {
    "Home": show_home,
    "Carbon Calculator": show_carbon_calculator,
    "Knowledge Base": show_knowledge_base,
    "Climate Assistant": show_chatbot,
    "Offsets Recommender": show_offsets_recommender,
    "Weather Dashboard": show_weather_dashboard,
    "Water Resources": show_water_resources,
    "Climate Tips": show_climate_tips,
    "About": show_about
}

selected_option = st.sidebar.selectbox("Navigate", list(menu_options.keys()))

# Display the selected page
if selected_option in menu_options:
    menu_options[selected_option]()

# Add footer information
st.sidebar.markdown("---")
st.sidebar.caption("© 2025 GreenAI")
st.sidebar.caption("Helping reduce AI's carbon footprint")

# Language selection
st.sidebar.subheader("🌐 Language | زبان | ٻولي")
langs = [
    {"id": "english", "label": "English", "flag": "🇬🇧"},
    {"id": "urdu", "label": "اردو", "flag": "🇵🇰"},
    {"id": "sindhi", "label": "سنڌي", "flag": "🏞️"}
]

lang_cols = st.sidebar.columns(3)
for i, lang in enumerate(langs):
    with lang_cols[i]:
        if st.button(
            f"{lang['flag']} {lang['label']}", 
            key=f"lang_{lang['id']}", 
            use_container_width=True,
            type="primary" if st.session_state.language == lang['id'] else "secondary"
        ):
            st.session_state.language = lang['id']
            st.rerun()

# Information about the app
st.sidebar.subheader("ℹ️ About")
st.sidebar.markdown("GreenAI helps users learn about climate actions in Sindh, calculate their carbon footprint, and discover offset options.")

# Add some helpful instructions
st.sidebar.subheader("🔍 How to use")
st.sidebar.markdown("""
- Use the navigation menu to explore different sections
- Switch language using the selector above
- Toggle between light and dark mode for comfort
""") 

render_footer()