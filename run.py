"""
Startup script for GreenAI chatbot that handles PyTorch initialization issues with Streamlit.
"""

import os
import subprocess
import sys
import importlib.util

def check_file_exists(file_path):
    """Check if a file exists"""
    return os.path.isfile(file_path)

def run_streamlit():
    """
    Run the Streamlit app with proper environment variables to avoid PyTorch initialization issues.
    """
    print("Starting GreenAI chatbot...")
    
    # Set environment variables to avoid PyTorch-Streamlit conflicts
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    os.environ["PYTHONPATH"] = os.getcwd()
    
    # Try to apply PyTorch fixes
    try:
        from fix_pytorch import apply_pytorch_fixes
        apply_pytorch_fixes()
    except ImportError:
        print("Fix module not found, continuing without PyTorch fixes.")
    
    # Check if .env file exists
    if not check_file_exists(".env"):
        print("Warning: .env file not found. Please create it with your API keys.")
        print("The application may not work correctly without API keys.")
    
    # Check which app to run - use simple_app.py if it exists
    app_file = "simple_app.py" if check_file_exists("simple_app.py") else "app.py"
    print(f"Running {app_file}...")
    
    # Use a direct subprocess call to start Streamlit
    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", app_file],
            check=True
        )
    except KeyboardInterrupt:
        print("\nApplication stopped.")
    except Exception as e:
        print(f"Error running application: {e}")
        
        # Fallback to simple app if regular app fails
        if app_file == "app.py" and check_file_exists("simple_app.py"):
            print("Trying simplified app instead...")
            try:
                subprocess.run(
                    [sys.executable, "-m", "streamlit", "run", "simple_app.py"],
                    check=True
                )
            except Exception as e2:
                print(f"Error running simplified application: {e2}")

if __name__ == "__main__":
    run_streamlit() 