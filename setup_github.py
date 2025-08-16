#!/usr/bin/env python3
"""
GitHub Setup Helper for GreenAI RAG Chatbot
This script helps you set up your repository on GitHub and prepare for Streamlit Cloud deployment.
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return None

def main():
    print("🚀 GreenAI RAG Chatbot - GitHub Setup Helper")
    print("=" * 50)
    
    # Check if git is initialized
    if not os.path.exists('.git'):
        print("❌ Git repository not found. Please run 'git init' first.")
        return
    
    # Check current status
    status = run_command("git status --porcelain", "Checking git status")
    if status and status.strip():
        print("⚠️  You have uncommitted changes. Please commit them first.")
        return
    
    print("\n📋 Next Steps:")
    print("1. Create a new repository on GitHub:")
    print("   - Go to https://github.com")
    print("   - Click 'New repository'")
    print("   - Name it: greenai-rag-chatbot")
    print("   - Make it PUBLIC (required for Streamlit Cloud free tier)")
    print("   - Don't initialize with README (you already have one)")
    
    print("\n2. After creating the repository, run these commands:")
    print("   git remote add origin https://github.com/YOUR_USERNAME/greenai-rag-chatbot.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    
    print("\n3. For Streamlit Cloud deployment:")
    print("   - Go to https://share.streamlit.io")
    print("   - Sign in with GitHub")
    print("   - Click 'New app'")
    print("   - Select your repository")
    print("   - Set main file path to: app.py")
    
    print("\n📖 See DEPLOYMENT.md for detailed instructions!")
    
    # Ask if user wants to proceed with remote setup
    username = input("\nEnter your GitHub username (or press Enter to skip): ").strip()
    if username:
        repo_url = f"https://github.com/{username}/greenai-rag-chatbot.git"
        print(f"\n🔄 Adding remote origin: {repo_url}")
        run_command(f"git remote add origin {repo_url}", "Adding remote origin")
        run_command("git branch -M main", "Renaming branch to main")
        print(f"\n✅ Ready to push! Run: git push -u origin main")

if __name__ == "__main__":
    main() 