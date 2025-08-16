"""
GreenAI: Simplified Test Version
This is a simplified version to test deployment step by step.
"""

import streamlit as st
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize session state
if "theme" not in st.session_state:
    st.session_state.theme = "light"
if "language" not in st.session_state:
    st.session_state.language = "english"

st.title("GreenAI RAG Chatbot - Simplified Test")
st.write("🚀 Testing deployment step by step...")

# Test basic imports
try:
    import pandas as pd
    st.success("✅ pandas imported successfully")
except Exception as e:
    st.error(f"❌ pandas import failed: {e}")

try:
    import numpy as np
    st.success("✅ numpy imported successfully")
except Exception as e:
    st.error(f"❌ numpy import failed: {e}")

try:
    import plotly.graph_objects as go
    st.success("✅ plotly imported successfully")
except Exception as e:
    st.error(f"❌ plotly import failed: {e}")

try:
    import altair as alt
    st.success("✅ altair imported successfully")
except Exception as e:
    st.error(f"❌ altair import failed: {e}")

# Test basic functionality
if st.button("Test Button"):
    st.success("Button works! 🎉")

# Show environment info
st.header("Environment Information")
st.write(f"Python version: {st.__version__}")
st.write("Streamlit is working correctly!")

st.header("Next Steps")
st.write("1. ✅ Basic deployment works")
st.write("2. 🔄 Test each import individually")
st.write("3. 🎯 Add back full functionality") 