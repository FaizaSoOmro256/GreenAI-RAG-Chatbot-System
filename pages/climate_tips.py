"""
Climate Tips module for GreenAI.
Provides personalized climate action recommendations.
"""

import streamlit as st
from utils.ui import get_translation
from utils.climate_tips import render_climate_tips_generator

def show_climate_tips():
    """
    Display the personalized climate tips generator page.
    """
    lang = st.session_state.get("language", "english")
    translations = {
        "english": {
            "description": "Get personalized recommendations for sustainable living based on your location in Sindh."
        },
        "urdu": {
            "description": "سندھ میں اپنے مقام کی بنیاد پر پائیدار زندگی کے لیے ذاتی سفارشات حاصل کریں۔"
        },
        "sindhi": {
            "description": "سنڌ ۾ پنهنجي جاءِ جي بنياد تي پائدار زندگي لاءِ ذاتي سفارشون حاصل ڪريو."
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
                🌿 Climate Action Tips
            </h1>
            <p style="
                color: #455A64;
                font-size: 1.2rem;
                margin: 1rem 0 0 0;
                font-weight: 500;
                opacity: 0.9;
            ">
                Get personalized recommendations for sustainable living based on your location in Sindh
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Render the climate tips generator
    render_climate_tips_generator() 