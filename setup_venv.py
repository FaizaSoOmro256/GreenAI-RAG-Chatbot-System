"""
Virtual environment setup script for GreenAI chatbot.
This creates a fresh virtual environment and installs initial dependencies.
"""

import subprocess
import os
import sys
import platform

def run_command(command):
    """Run a command and print output"""
    print(f"Running: {command}")
    process = subprocess.run(command, shell=True, check=False)
    if process.returncode != 0:
        print(f"Command failed with exit code {process.returncode}")
        return False
    return True

def main():
    print("Setting up a fresh virtual environment for GreenAI...")
    
    # Determine the Python executable to use
    python_cmd = sys.executable
    print(f"Using Python: {python_cmd}")
    
    # Create virtual environment directory
    venv_dir = "venv"
    if os.path.exists(venv_dir):
        response = input(f"Virtual environment '{venv_dir}' already exists. Recreate? (y/n): ")
        if response.lower() == 'y':
            if platform.system() == "Windows":
                run_command(f"rmdir /s /q {venv_dir}")
            else:
                run_command(f"rm -rf {venv_dir}")
        else:
            print("Using existing virtual environment...")
            
    if not os.path.exists(venv_dir):
        print("\nCreating virtual environment...")
        run_command(f"{python_cmd} -m venv {venv_dir}")
    
    # Determine activation command and pip command
    if platform.system() == "Windows":
        activate_cmd = f"{venv_dir}\\Scripts\\activate"
        pip_cmd = f"{venv_dir}\\Scripts\\pip"
    else:
        activate_cmd = f"source {venv_dir}/bin/activate"
        pip_cmd = f"{venv_dir}/bin/pip"
    
    # Upgrade pip
    print("\nUpgrading pip...")
    if platform.system() == "Windows":
        run_command(f"{pip_cmd} install --upgrade pip")
    else:
        run_command(f"{activate_cmd} && {pip_cmd} install --upgrade pip")
    
    print("\nVirtual environment created successfully!")
    print("\nTo activate the virtual environment:")
    if platform.system() == "Windows":
        print(f"{venv_dir}\\Scripts\\activate")
    else:
        print(f"source {venv_dir}/bin/activate")
    
    print("\nAfter activation, install dependencies:")
    print("python install.py")
    
    # Instructions for installing packages after activation
    print("\nOr install key packages manually:")
    print(f"1. {pip_cmd} install streamlit python-dotenv")
    print(f"2. {pip_cmd} install google-generativeai pydantic")
    print(f"3. {pip_cmd} install langchain langchain-core langchain-community")
    print(f"4. {pip_cmd} install pinecone-client==2.0.0 langchain-pinecone==0.1.0")
    print(f"5. {pip_cmd} install torch --index-url https://download.pytorch.org/whl/cpu")
    print(f"6. {pip_cmd} install sentence-transformers")

if __name__ == "__main__":
    main() 