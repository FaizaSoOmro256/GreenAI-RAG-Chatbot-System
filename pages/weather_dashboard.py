"""
Weather Dashboard module for GreenAI.
Provides enhanced weather visualization and analysis tools.
"""

import streamlit as st
from utils.ui import get_translation
from utils.weather_visualizations import render_enhanced_weather_dashboard

def show_weather_dashboard():
    """
    Display the enhanced weather dashboard with interactive maps and visualizations.
    """
    lang = st.session_state.get("language", "english")
    translations = {
        "english": {
            "description": "Real-time weather data and climate analysis for districts in Sindh."
        },
        "urdu": {
            "description": "سندھ کے اضلاع کے لیے حقیقی وقت کے موسمی اعداد و شمار اور آب و ہوا کا تجزیہ۔"
        },
        "sindhi": {
            "description": "سنڌ جي ضلعن لاءِ حقيقي وقت جا موسمي انگ اکر ۽ آب و هوا جو تجزيو."
        }
    }
    
    t = translations[lang]
    
    # Display the main title with custom styling
    st.markdown("""
        <div style="
            text-align: center;
            margin: 2rem 0 3rem 0;
            padding: 2rem;
            background: linear-gradient(135deg, #F0F7FF, #E3F2FD);
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(33, 150, 243, 0.2);
            border-left: 5px solid #2196F3;
        ">
            <h1 style="
                color: #2196F3;
                font-size: 3rem;
                font-weight: bold;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                letter-spacing: 1px;
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #2196F3, #1976D2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">
                🌤️ Weather Dashboard
            </h1>
            <p style="
                color: #455A64;
                font-size: 1.2rem;
                margin: 1rem 0 0 0;
                font-weight: 500;
                opacity: 0.9;
            ">
                Real-time weather data and climate analysis for districts in Sindh
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Render the enhanced weather dashboard
    render_enhanced_weather_dashboard() 