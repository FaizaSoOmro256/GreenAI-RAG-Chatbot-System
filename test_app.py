import streamlit as st

st.title("GreenAI RAG Chatbot - Test Deployment")
st.write("🚀 Basic deployment test successful!")

st.header("Environment Check")
st.write(f"Python version: {st.__version__}")
st.write("Streamlit is working correctly!")

st.header("Next Steps")
st.write("1. ✅ Basic deployment works")
st.write("2. 🔄 Add back dependencies gradually")
st.write("3. 🎯 Full app functionality")

# Test basic functionality
if st.button("Test Button"):
    st.success("Button works! 🎉")

# Test session state
if "test_counter" not in st.session_state:
    st.session_state.test_counter = 0

if st.button("Increment Counter"):
    st.session_state.test_counter += 1

st.write(f"Counter: {st.session_state.test_counter}") 