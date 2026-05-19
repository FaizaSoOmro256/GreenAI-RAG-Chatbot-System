import streamlit as st
from PIL import Image
import base64
import os
import config
from utils.logger import logger
from translations import TRANSLATIONS

__all__ = [
    'set_page_config',
    'apply_custom_css',
    'render_sidebar',
    'render_chat_history',
    'render_footer',
    'init_session_state',
    'render_theme_toggle',
]

def set_page_config():
    """
    Configure the Streamlit page settings.
    """
    st.set_page_config(
        page_title=config.APP_TITLE,
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def apply_custom_css():
    """
    Apply custom CSS to enhance the UI appearance with dark mode support.
    """
    # Check for theme in session state
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
    
    # Determine which theme colors to use
    if st.session_state.theme == "dark":
        main_bg = "#0A1929"  # Darker blue background
        card_bg = "#132F4C"  # Dark blue cards
        text_color = "#E0E0E0"
        secondary_text = "#B0B0B0"
        primary_color = "#00E5FF"  # Bright cyan
        secondary_color = "#00B8D4"  # Darker cyan
        border_color = "#1E4976"
        user_msg_bg = "#1E4976"
        bot_msg_bg = "#132F4C"
        hover_color = "#00B8D4"
        gradient_start = "#0A1929"
        gradient_end = "#132F4C"
        accent_color = "#00E5FF"
        success_color = "#00E676"
        warning_color = "#FFD600"
        error_color = "#FF1744"
    else:
        main_bg = "#F0F7FF"  # Light blue background
        card_bg = "#FFFFFF"
        text_color = "#1A237E"  # Deep blue text
        secondary_text = "#455A64"
        primary_color = "#2196F3"  # Material blue
        secondary_color = "#1976D2"  # Darker blue
        border_color = "#BBDEFB"
        user_msg_bg = "#E3F2FD"
        bot_msg_bg = "#FFFFFF"
        hover_color = "#1976D2"
        gradient_start = "#F0F7FF"
        gradient_end = "#E3F2FD"
        accent_color = "#2196F3"
        success_color = "#4CAF50"
        warning_color = "#FFC107"
        error_color = "#F44336"
    
    css = f"""
    <style>
    /* Main container styling */
    .main {{
        background: linear-gradient(135deg, {gradient_start}, {gradient_end});
        color: {text_color};
        min-height: 100vh;
        padding: 2rem;
    }}
    
    /* Header styling */
    .stTitle, .stHeader {{
        color: {primary_color};
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        letter-spacing: 0.5px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}
    
    /* Chat message styling */
    .user-message {{
        background: linear-gradient(145deg, {user_msg_bg}, {gradient_end});
        padding: 20px 25px;
        border-radius: 20px 20px 3px 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        max-width: 75%;
        margin-left: auto;
        word-wrap: break-word;
        border-left: 4px solid {primary_color};
        color: {text_color};
        transition: all 0.3s ease;
        animation: slideIn 0.5s ease-out;
    }}
    
    .user-message:hover {{
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 12px 20px rgba(0,0,0,0.15);
    }}
    
    .bot-message {{
        background: linear-gradient(145deg, {bot_msg_bg}, {gradient_end});
        padding: 20px 25px;
        border-radius: 20px 20px 20px 3px;
        margin-bottom: 25px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        max-width: 75%;
        word-wrap: break-word;
        border-left: 4px solid {secondary_color};
        color: {text_color};
        transition: all 0.3s ease;
        animation: slideIn 0.5s ease-out;
    }}
    
    .bot-message:hover {{
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 12px 20px rgba(0,0,0,0.15);
    }}
    
    /* Section card styling */
    .section-card {{
        background: linear-gradient(145deg, {card_bg}, {gradient_end});
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-left: 5px solid {primary_color};
        color: {text_color};
        transition: all 0.3s ease;
        animation: fadeIn 0.5s ease-out;
    }}
    
    .section-card:hover {{
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    }}
    
    .section-title {{
        color: {primary_color};
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 20px;
        border-bottom: 2px solid {border_color};
        padding-bottom: 12px;
        letter-spacing: 0.5px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 6px;
        padding: 8px;
        background: {card_bg};
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}

    .stTabs [data-baseweb="tab"] {{
        background: linear-gradient(145deg, {card_bg}, {gradient_end});
        border-radius: 12px;
        padding: 15px 30px;
        color: {primary_color};
        transition: all 0.3s ease;
        font-weight: 500;
    }}

    .stTabs [aria-selected="true"] {{
        background: linear-gradient(145deg, {primary_color}, {secondary_color});
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transform: translateY(-2px);
    }}
    
    /* Button styling */
    div[data-testid="stButton"] button {{
        background: linear-gradient(145deg, {primary_color}, {secondary_color});
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        transition: all 0.3s ease;
        border: none;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        font-size: 14px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}
    
    div[data-testid="stButton"] button:hover {{
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        background: linear-gradient(145deg, {secondary_color}, {primary_color});
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {card_bg}, {gradient_end});
        border-right: 1px solid {border_color};
        padding: 1.5rem;
        box-shadow: 4px 0 15px rgba(0,0,0,0.1);
    }}

    /* Sidebar heading */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {{
        color: {primary_color};
        font-weight: 600;
        letter-spacing: 0.5px;
        font-family: 'Segoe UI', Arial, sans-serif;
    }}
    
    /* Footer styling */
    .footer {{
        text-align: center;
        color: {secondary_text};
        padding: 25px 15px;
        font-size: 0.9em;
        border-top: 1px solid {border_color};
        margin-top: 40px;
        background: linear-gradient(145deg, {card_bg}, {gradient_end});
        border-radius: 15px;
        box-shadow: 0 -4px 15px rgba(0,0,0,0.05);
    }}
    
    /* Theme toggle styling */
    .theme-toggle {{
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background: linear-gradient(145deg, {card_bg}, {gradient_end});
        border-radius: 15px;
        margin-bottom: 25px;
        border: 1px solid {border_color};
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    
    .theme-toggle-btn {{
        background: linear-gradient(145deg, {primary_color}, {secondary_color});
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 600;
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}
    
    .theme-toggle-btn:hover {{
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {{
        width: 10px;
        height: 10px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: {card_bg};
        border-radius: 5px;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(145deg, {primary_color}, {secondary_color});
        border-radius: 5px;
        border: 2px solid {card_bg};
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(145deg, {secondary_color}, {primary_color});
    }}
    
    /* Animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(30px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    
    @keyframes pulse {{
        0% {{ transform: scale(1); opacity: 0.8; }}
        50% {{ transform: scale(1.05); opacity: 1; }}
        100% {{ transform: scale(1); opacity: 0.8; }}
    }}
    
    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
        100% {{ transform: translateY(0px); }}
    }}
    
    @keyframes gradientBackground {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.7; }}
    }}
    
    /* Success, Warning, Error states */
    .success-message {{
        background: linear-gradient(145deg, {success_color}20, {success_color}40);
        border-left: 4px solid {success_color};
        color: {success_color};
    }}
    
    .warning-message {{
        background: linear-gradient(145deg, {warning_color}20, {warning_color}40);
        border-left: 4px solid {warning_color};
        color: {warning_color};
    }}
    
    .error-message {{
        background: linear-gradient(145deg, {error_color}20, {error_color}40);
        border-left: 4px solid {error_color};
        color: {error_color};
    }}
    
    /* Responsive container for smaller screens */
    @media screen and (max-width: 768px) {{
        .user-message, .bot-message {{
            max-width: 90%;
            padding: 15px 20px;
        }}
        
        .section-card {{
            padding: 20px;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            padding: 10px 20px;
        }}
    }}
    
    /* Input field styling */
    .stTextInput > div > div > input {{
        background: {card_bg};
        border: 2px solid {border_color};
        border-radius: 12px;
        padding: 12px 20px;
        color: {text_color};
        font-size: 16px;
        transition: all 0.3s ease;
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: {primary_color};
        box-shadow: 0 0 0 2px {primary_color}40;
    }}
    
    /* Metric cards */
    .metric-card {{
        background: linear-gradient(145deg, {card_bg}, {gradient_end});
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }}
    
    .metric-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }}
    
    .metric-value {{
        font-size: 2.5rem;
        font-weight: bold;
        color: {primary_color};
        margin: 10px 0;
    }}
    
    .metric-label {{
        color: {secondary_text};
        font-size: 1rem;
        margin-top: 5px;
    }}
    
    /* Enhanced Sidebar Styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {card_bg}, {gradient_end});
        border-right: 1px solid {border_color};
        padding: 1.5rem;
        box-shadow: 4px 0 15px rgba(0,0,0,0.1);
    }}
    
    /* Sidebar Navigation Buttons */
    .nav-btn {{
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    
    .nav-btn:hover {{
        background: {primary_color}20 !important;
        transform: translateX(5px);
    }}
    
    .nav-btn.active {{
        background: {primary_color}20 !important;
        color: {primary_color} !important;
        font-weight: 600 !important;
    }}
    
    /* Language Buttons */
    .lang-btn {{
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    
    .lang-btn:hover {{
        background: {primary_color}20 !important;
    }}
    
    .lang-btn.active {{
        background: {primary_color}20 !important;
        color: {primary_color} !important;
        font-weight: 600 !important;
    }}
    
    /* Theme Toggle Buttons */
    .theme-toggle-btn {{
        width: 40px !important;
        height: 40px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 1.2rem !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }}
    
    .theme-toggle-btn:hover {{
        transform: scale(1.1) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }}
    
    /* Quick Stats Cards */
    .quick-stat-card {{
        background: {card_bg};
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s ease;
    }}
    
    .quick-stat-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    
    /* Dark Mode Adjustments */
    @media (prefers-color-scheme: dark) {{
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {main_bg}, {card_bg});
        }}
        
        .nav-btn, .lang-btn {{
            color: {text_color} !important;
        }}
        
        .nav-btn:hover, .lang-btn:hover {{
            background: {primary_color}30 !important;
        }}
        
        .nav-btn.active, .lang-btn.active {{
            background: {primary_color}30 !important;
            color: {primary_color} !important;
        }}
    }}

    /* Custom styles for headings */
    h1, h2, h3, h4, h5, h6 {{
        color: {primary_color}; /* Dark green color */
        margin-top: 25px;
        margin-bottom: 15px;
        font-weight: bold;
    }}

    h1 {{
        font-size: 2.5em;
        border-bottom: 2px solid {primary_color}; /* Light green underline */
        padding-bottom: 10px;
    }}

    h2 {{
        font-size: 2em;
        border-bottom: 1px solid {primary_color}; /* Lighter green underline */
        padding-bottom: 8px;
    }}

    h3 {{
        font-size: 1.5em;
    }}

    /* Add some spacing around Streamlit heading components */
    .stTitle, .stHeader, .stSubheader {{
        margin-top: 25px;
        margin-bottom: 15px;
    }}

    .stHeader h1, .stHeader h2, .stHeader h3, .stHeader h4, .stHeader h5, .stHeader h6,
    .stSubheader h1, .stSubheader h2, .stSubheader h3, .stSubheader h4, .stSubheader h5, .stSubheader h6 {{
        color: {primary_color}; /* Apply the custom color to Streamlit headings */
    }}

    /* Custom style for main section headings */
    .page-main-heading {{
        font-size: 2em;
        font-weight: bold;
        color: {primary_color}; /* Use primary color */
        margin-top: 30px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 3px solid {secondary_color}; /* Thicker underline with secondary color */
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_theme_toggle():
    """
    Render a toggle button for switching between light and dark mode.
    """
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
        
    current_theme = st.session_state.theme
    
    with st.sidebar:
        st.subheader("🎨 Theme Settings")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if st.button("🌞 Light", key="light_theme", 
                    use_container_width=True,
                    type="primary" if current_theme == "light" else "secondary"):
                st.session_state.theme = "light"
                st.rerun()
                
        with col2:
            if st.button("🌙 Dark", key="dark_theme", 
                    use_container_width=True,
                    type="primary" if current_theme == "dark" else "secondary"):
                st.session_state.theme = "dark"
                st.rerun()

def user_message_html(message):
    """
    Format a user message with HTML styling.
    """
    return f"""
    <div class="user-message">
        <div style="display: flex; align-items: flex-start;">
            <div style="background-color: #2E7D32; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 10px; flex-shrink: 0;">
                <span style="font-size: 14px;">👤</span>
            </div>
            <div>{message}</div>
        </div>
    </div>
    """

def bot_message_html(message):
    """
    Format a bot message with HTML styling.
    """
    return f"""
    <div class="bot-message">
        <div style="display: flex; align-items: flex-start;">
            <div style="background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #43A047 100%); color: white; width: 30px; height: 30px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 10px; flex-shrink: 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <span style="font-size: 14px;">🔍</span>
            </div>
            <div>{message}</div>
        </div>
    </div>
    """

def render_chat_message(message, is_user):
    """
    Render a chat message with appropriate styling.
    """
    if is_user:
        st.markdown(user_message_html(message), unsafe_allow_html=True)
    else:
        st.markdown(bot_message_html(message), unsafe_allow_html=True)

def render_chat_history():
    """
    Render the chat history from the session state.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        render_chat_message(message["content"], message["is_user"])

def render_footer():
    """
    Render the footer section with enhanced styling.
    """
    footer_html = """
    <div style="
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 3rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    ">
        <div style="
            max-width: 800px;
            margin: 0 auto;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        ">
            <p style="
                color: #455A64;
                font-size: 0.95rem;
                margin: 0 0 0.5rem 0;
                opacity: 0.9;
            ">Ecosphere AI - Sindh's Sustainable Climate Actions Chatbot | Powered by Gemini Flash 2.0</p>
            <p style="
                color: #1976D2;
                font-size: 1.1rem;
                font-weight: 600;
                margin: 0;
                letter-spacing: 0.5px;
            ">Ecosphere AI v1.0.0 All Rights Reserved 2026</p>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

def init_session_state():
    """
    Initialize session state variables.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "language" not in st.session_state:
        st.session_state.language = config.DEFAULT_LANGUAGE
        
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
        
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
        
    if "user" not in st.session_state:
        st.session_state.user = None
        
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

# Add new functions for UI sections

def render_section_card(title, content, icon="🔍"):
    """
    Render a styled section card with title and content.
    """
    html = f"""
    <div class="section-card">
        <div class="section-title">
            <div style="display: flex; align-items: center;">
                <div style="background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #43A047 100%); color: white; width: 26px; height: 26px; border-radius: 6px; display: flex; align-items: center; justify-content: center; margin-right: 8px;">
                    <span style="font-size: 14px;">{icon}</span>
                </div>
                <span>{title}</span>
            </div>
        </div>
        <div>{content}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_climate_data_section():
    """
    Render a section for climate data visualization.
    """
    st.subheader("📊 Climate Data Visualization")
    
    tabs = st.tabs(["Temperature Trends", "Rainfall Patterns", "Climate Impact"])
    
    with tabs[0]:
        st.write("Visual representation of temperature trends in Sindh region")
        # Sample chart
        data = {
            'Year': list(range(2010, 2023)),
            'Avg Temperature (°C)': [28.1, 28.3, 28.7, 29.0, 29.2, 29.5, 29.8, 30.1, 30.3, 30.5, 30.8, 31.0, 31.2]
        }
        st.line_chart(data, x='Year', y='Avg Temperature (°C)')
    
    with tabs[1]:
        st.write("Annual rainfall patterns in Sindh")
        # Sample chart
        data = {
            'Year': list(range(2010, 2023)),
            'Rainfall (mm)': [180, 165, 210, 195, 170, 220, 200, 190, 230, 250, 240, 210, 200]
        }
        st.bar_chart(data, x='Year', y='Rainfall (mm)')
    
    with tabs[2]:
        st.write("Climate impact assessment for different regions")
        st.info("This section will display impact assessment data for different districts of Sindh.")

def render_resources_section():
    """
    Render a section for climate resources and links.
    """
    st.subheader("📚 Resources & Information")
    
    # Two columns layout
    col1, col2 = st.columns(2)
    
    with col1:
        render_section_card(
            "Key Climate Policies", 
            """
            <ul>
                <li>Sindh Climate Change Policy (2018)</li>
                <li>Sindh Environmental Protection Act</li>
                <li>National Climate Change Policy</li>
                <li>Pakistan's Nationally Determined Contributions</li>
            </ul>
            """, 
            icon="📄"
        )
    
    with col2:
        render_section_card(
            "Climate Organizations", 
            """
            <ul>
                <li>Sindh Environmental Protection Agency</li>
                <li>WWF Pakistan</li>
                <li>IUCN Pakistan</li>
                <li>UNDP Climate Change Initiatives</li>
            </ul>
            """, 
            icon="🏢"
        )

def render_action_cards():
    """
    Render action cards for climate actions.
    """
    st.subheader("🌍 Climate Action Areas")
    
    # Three columns layout for action cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_section_card(
            "Renewable Energy", 
            """
            Sindh is developing significant wind power installations 
            in the Jhimpir-Gharo corridor and expanding solar energy projects 
            throughout the province.
            """, 
            icon="⚡"
        )
    
    with col2:
        render_section_card(
            "Water Management", 
            """
            Implementing improved irrigation systems and water 
            conservation efforts to address water scarcity and changing 
            rainfall patterns in the region.
            """, 
            icon="💧"
        )
    
    with col3:
        render_section_card(
            "Coastal Protection", 
            """
            Mangrove restoration projects in the Indus Delta to protect 
            coastal areas from erosion, sea-level rise, and to preserve 
            biodiversity.
            """, 
            icon="🌊"
        )

def get_translation(translations, key):
    """
    Get a translation string for the current language.
    
    Args:
        translations (dict): Dictionary of translations
        key (str): Key to look up (can be nested using dot notation, e.g. "climate_trends.temperature")
        
    Returns:
        str: Translated string or original key if not found
    """
    lang = st.session_state.get("language", "english")
    
    # Handle nested keys (e.g. "climate_trends.temperature")
    if "." in key:
        main_key, sub_key = key.split(".", 1)
        try:
            return TRANSLATIONS[lang][main_key][sub_key]
        except KeyError:
            try:
                return TRANSLATIONS["english"][main_key][sub_key]
            except KeyError:
                return key
    else:
        try:
            return TRANSLATIONS[lang][key]
        except KeyError:
            try:
                return TRANSLATIONS["english"][key]
            except KeyError:
                return key

def render_sidebar():
    """
    Render an enhanced sidebar with better styling and more interactive elements.
    """
    with st.sidebar:
        # Navigation
        st.markdown("""
            <div style='margin: 1.5rem 0;'>
                <h3 style='color: #2196F3; font-size: 1.1rem; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #E0E0E0;'>Navigation</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Navigation buttons
        nav_options = [
            {"icon": "🏠", "label": "Home", "page": "home"},
            {"icon": "📊", "label": "Climate Analysis", "page": "analytics"},
            {"icon": "🌍", "label": "Climate Map", "page": "climate_map"},
            {"icon": "📈", "label": "Weather Dashboard", "page": "reports"},
            {"icon": "💡", "label": "Climate Tips", "page": "climate_tips"},
            {"icon": "📚", "label": "Knowledge Base", "page": "knowledge_base"},
            {"icon": "💬", "label": "Chatbot", "page": "chatbot"},
            {"icon": "💧", "label": "Water Resources", "page": "water_resources"},
            {"icon": "📊", "label": "Carbon Calculator", "page": "carbon_calculator"},
            {"icon": "🌱", "label": "Offsets Recommender", "page": "offsets_recommender"},
            {"icon": "ℹ️", "label": "About", "page": "about"}
        ]
        
        for option in nav_options:
            if st.button(
                f"{option['icon']} {option['label']}",
                key=f"nav_{option['page']}",
                use_container_width=True,
                type="primary" if st.session_state.get("current_page") == option['page'] else "secondary"
            ):
                st.session_state.current_page = option['page']
                st.rerun()
        
        # Quick Stats
        st.markdown("""
            <div style='margin: 1.5rem 0;'>
                <h3 style='color: #2196F3; font-size: 1.1rem; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #E0E0E0;'>Quick Stats</h3>
                <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.8rem;'>
                    <div style='background: #E3F2FD; padding: 1rem; border-radius: 10px; text-align: center;'>
                        <div style='font-size: 1.2rem; color: #1976D2; font-weight: bold;'>32°C</div>
                        <div style='font-size: 0.8rem; color: #455A64;'>Temperature</div>
                    </div>
                    <div style='background: #E3F2FD; padding: 1rem; border-radius: 10px; text-align: center;'>
                        <div style='font-size: 1.2rem; color: #1976D2; font-weight: bold;'>65%</div>
                        <div style='font-size: 0.8rem; color: #455A64;'>Humidity</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Language Selector
        st.markdown("""
            <div style='margin: 1.5rem 0;'>
                <h3 style='color: #2196F3; font-size: 1.1rem; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #E0E0E0;'>Language</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Language buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("EN", key="lang_en", use_container_width=True, 
                        type="primary" if st.session_state.get("language") == "english" else "secondary"):
                st.session_state.language = "english"
                st.rerun()
        with col2:
            if st.button("اردو", key="lang_urdu", use_container_width=True,
                        type="primary" if st.session_state.get("language") == "urdu" else "secondary"):
                st.session_state.language = "urdu"
                st.rerun()
        with col3:
            if st.button("سنڌي", key="lang_sindhi", use_container_width=True,
                        type="primary" if st.session_state.get("language") == "sindhi" else "secondary"):
                st.session_state.language = "sindhi"
                st.rerun()
        
        # Footer
        st.markdown("""
            <div style='margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #E0E0E0;'>
                <p style='color: #78909C; font-size: 0.8rem; text-align: center; margin: 0;'>Version 1.0.0</p>
                <p style='color: #78909C; font-size: 0.8rem; text-align: center; margin: 0.5rem 0 0 0;'>© 2026 Ecosphere AI</p>
            </div>
        """, unsafe_allow_html=True)

def apply_theme_styles():
    """Apply theme-specific styles."""
    if st.session_state.theme == "dark":
        st.markdown("""
        <style>
        :root {
            --background-color: #1E1E1E;
            --text-color: #FFFFFF;
            --border-color: #2E2E2E;
            --hover-color: #2E2E2E;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        :root {
            --background-color: #FFFFFF;
            --text-color: #000000;
            --border-color: #E6E9EF;
            --hover-color: #F0F2F6;
        }
        </style>
        """, unsafe_allow_html=True) 