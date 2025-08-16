import streamlit as st
import os

# Set environment variables directly (bypass .env file)
os.environ["GEMINI_API_KEY"] = "AIzaSyDOVJjB06O7xOL_bdBvTj9h3Uo1sjArr00"
os.environ["PINECONE_API_KEY"] = "pcsk_TY41N_9FYEBdgBfAKrWJAySRo3JxeYeBAH6krF9XWs5RCnza1n7B4jELvoxZwrUeUyqg7"
os.environ["PINECONE_ENVIRONMENT"] = "us-east-1"
os.environ["PINECONE_INDEX"] = "greenai-sindh"
os.environ["OPENWEATHERMAP_API_KEY"] = "807eac6885cb55c6dfe4b5cf9ca885be"

st.title("GreenAI RAG Chatbot - Test Without .env")
st.write("🚀 Testing without .env file to bypass encoding issues...")

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

# Test environment variables
st.header("Environment Variables Check")
st.write(f"GEMINI_API_KEY: {'✅ Set' if os.getenv('GEMINI_API_KEY') else '❌ Not set'}")
st.write(f"PINECONE_API_KEY: {'✅ Set' if os.getenv('PINECONE_API_KEY') else '❌ Not set'}")
st.write(f"PINECONE_ENVIRONMENT: {'✅ Set' if os.getenv('PINECONE_ENVIRONMENT') else '❌ Not set'}")
st.write(f"OPENWEATHERMAP_API_KEY: {'✅ Set' if os.getenv('OPENWEATHERMAP_API_KEY') else '❌ Not set'}")

# Test basic functionality
if st.button("Test Button"):
    st.success("Button works! 🎉")

# Show environment info
st.header("Environment Information")
st.write(f"Python version: {st.__version__}")
st.write("Streamlit is working correctly!")

st.header("Next Steps")
st.write("1. ✅ Basic deployment works")
st.write("2. 🔄 Environment variables set")
st.write("3. 🎯 Ready for full app") 