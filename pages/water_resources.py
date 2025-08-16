"""
Water Resources Dashboard module for GreenAI.
Provides comprehensive analysis of water resources in Sindh region.
"""

import streamlit as st
from utils.water_resources import render_water_resources_dashboard

def show_water_resources():
    """
    Display the water resources dashboard with comprehensive analysis tools.
    """
    lang = st.session_state.get("language", "english")
    translations = {
        "english": {
            "description": "Analyze water availability, quality, and management strategies for Sindh districts."
        },
        "urdu": {
            "description": "سندھ کے اضلاع کے لیے پانی کی دستیابی، معیار اور انتظام کے حکمت عملیوں کا تجزیہ کریں۔"
        },
        "sindhi": {

            "description": "سنڌ جي ضلعن لاءِ پاڻي جي دستيابي، معيار ۽ انتظام جي حڪمت عملين جو تجزيو ڪريو."
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
                💧 Water Resources
            </h1>
            <p style="
                color: #455A64;
                font-size: 1.2rem;
                margin: 1rem 0 0 0;
                font-weight: 500;
                opacity: 0.9;
            ">
                Analyze water availability, quality, and management strategies for Sindh districts
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Render the water resources dashboard
    render_water_resources_dashboard() 