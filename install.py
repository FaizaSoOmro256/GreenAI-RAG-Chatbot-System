"""
Installation script for GreenAI chatbot dependencies.
This handles installing packages one by one to avoid dependency conflicts.
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a command and print output"""
    print(f"Running: {command}")
    process = subprocess.run(command, shell=True, check=False)
    if process.returncode != 0:
        print(f"Command failed with exit code {process.returncode}")
        return False
    return True

def main():
    print("Installing GreenAI dependencies...")
    
    # Install packages one by one to avoid conflicts
    packages = [
        "streamlit",
        "python-dotenv",
        "pydantic",
        "google-generativeai",
        "langchain",
        "langchain-core",
        "langchain-community",
        "langchain-text-splitters"
    ]
    
    for package in packages:
        print(f"\nInstalling {package}...")
        if not run_command(f"pip install {package}"):
            print(f"Failed to install {package}, but continuing...")
    
    # Install PyTorch CPU version
    print("\nInstalling PyTorch (CPU version, this may take some time)...")
    if not run_command("pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu"):
        print("Failed to install PyTorch. You can try installing it manually later.")
    
    # Install sentence-transformers
    print("\nInstalling sentence-transformers...")
    if not run_command("pip install sentence-transformers"):
        print("Failed to install sentence-transformers. You can try installing it manually later.")
    
    # Install pinecone directly
    print("\nInstalling Pinecone...")
    run_command("pip install pinecone-client")
    
    # Install pillow
    print("\nInstalling Pillow...")
    run_command("pip install pillow")
    
    print("\nInstallation completed!")
    print("\nTo run the application:")
    print("1. Set up your .env file with API keys")
    print("2. Run 'python ingest.py' to populate the vector database")
    print("3. Start the app with 'streamlit run app.py'")

if __name__ == "__main__":
    main() 