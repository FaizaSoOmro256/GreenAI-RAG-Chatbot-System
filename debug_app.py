import streamlit as st
import sys
import os
from dotenv import load_dotenv

st.title("Debug Console")

# Section 1: Environment Verification
st.header("1. Environment Checks")
st.write(f"Python version: {sys.version}")
st.write(f"Working directory: {os.getcwd()}")
st.write(f"Environment variables: {dict(os.environ)}")

# Section 2: Package Verification
st.header("2. Package Verification")
try:
    import pinecone
    st.success(f"✅ Pinecone imported (v{pinecone.__version__})")
except ImportError as e:
    st.error(f"❌ Pinecone import failed: {str(e)}")

try:
    import google.generativeai as genai
    st.success("✅ Gemini imported")
except ImportError as e:
    st.error(f"❌ Gemini import failed: {str(e)}")

# Section 3: API Connection Tests
st.header("3. API Connection Tests")
if st.button("Run Connection Tests"):
    load_dotenv()
    
    # Test Pinecone
    try:
        import pinecone
        pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        indexes = pc.list_indexes().names()
        st.success(f"✅ Pinecone connected! Indexes: {indexes}")
    except Exception as e:
        st.error(f"❌ Pinecone connection failed: {str(e)}")
    
    # Test Gemini
    try:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        models = [m.name for m in genai.list_models()]
        st.success(f"✅ Gemini connected! Models: {models}")
    except Exception as e:
        st.error(f"❌ Gemini connection failed: {str(e)}")