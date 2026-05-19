"""
Compatibility check script for Ecosphere AI dependencies.
This helps diagnose package compatibility issues.
"""

import subprocess
import importlib.util
import sys

def check_package_installed(package_name):
    """Check if a package is installed and return version if available"""
    try:
        result = subprocess.run(f"pip show {package_name}", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            # Extract version from output
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    version = line.split(':', 1)[1].strip()
                    return True, version
            return True, "Unknown version"
        else:
            return False, None
    except Exception as e:
        return False, f"Error checking: {str(e)}"

def check_import(module_name):
    """Check if a module can be imported"""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            try:
                module = importlib.import_module(module_name)
                return True, getattr(module, '__version__', 'Unknown version')
            except Exception as e:
                return False, f"Import error: {str(e)}"
        else:
            return False, "Module not found"
    except Exception as e:
        return False, f"Error checking: {str(e)}"

def main():
    print("Checking compatibility of Ecosphere AI dependencies...\n")
    
    # Key packages to check
    packages = [
        "streamlit",
        "langchain",
        "langchain_core",
        "langchain_community",
        "langchain_pinecone",
        "pinecone",
        "sentence_transformers",
        "torch",
        "google.generativeai",
        "dotenv",
        "pydantic"
    ]
    
    print("Package status:")
    print("--------------")
    for package in packages:
        pip_name = package.replace('_', '-')
        installed, version = check_package_installed(pip_name)
        importable, import_version = check_import(package)
        
        status = "OK" if installed and importable else "Issue"
        
        print(f"{package.ljust(20)} | {status} | Pip: {version or 'Not installed'} | Import: {import_version if importable else 'Failed'}")
    
    print("\nChecking for compatibility issues...")
    
    # Check pinecone compatibility
    pinecone_installed, pinecone_version = check_package_installed("pinecone-client")
    langchain_pinecone_installed, langchain_pinecone_version = check_package_installed("langchain-pinecone")
    
    if pinecone_installed and langchain_pinecone_installed:
        print(f"\nPinecone version: {pinecone_version}")
        print(f"LangChain Pinecone version: {langchain_pinecone_version}")
        
        # Known compatibility combinations
        if pinecone_version.startswith("2.0.") and langchain_pinecone_version.startswith("0.1."):
            print("[OK] This combination of pinecone and langchain-pinecone should be compatible")
        else:
            print("[WARNING] This combination of pinecone and langchain-pinecone might have compatibility issues")
            
            # Suggest fixes
            print("\nSuggested fix:")
            print("pip uninstall -y pinecone-client pinecone langchain-pinecone")
            print("pip install pinecone-client==2.0.0")
            print("pip install langchain-pinecone==0.1.0")
    
    print("\nTo fix dependency issues, try running:")
    print("python install.py")
    
    print("\nIf you still encounter issues, try manual installation:")
    print("1. Create a fresh virtual environment")
    print("2. Install packages one by one starting with the most basic ones")

if __name__ == "__main__":
    main() 