"""
Fixes for PyTorch integration with Streamlit.
This module monkey patches torch classes to avoid the '__path__._path' error.
"""

import sys
import logging
import types

def apply_pytorch_fixes():
    """
    Apply fixes to prevent PyTorch custom classes issues with Streamlit.
    """
    try:
        import torch
        
        # Create a dummy __path__ attribute for torch._classes to prevent errors
        class DummyPath:
            _path = []
            
            def __iter__(self):
                return iter([])
        
        # Check if torch._classes exists
        if hasattr(torch, "_classes"):
            # Add the dummy __path__ to the _classes module
            torch._classes.__path__ = DummyPath()
            
            # Override the original __getattr__ if it's causing issues
            original_getattr = getattr(torch._classes, "__getattr__", None)
            
            def safe_getattr(self, name):
                if name == "__path__" or name == "_path":
                    return DummyPath()
                if original_getattr:
                    return original_getattr(self, name)
                raise AttributeError(f"module 'torch._classes' has no attribute '{name}'")
            
            # Only apply the patch if the original __getattr__ exists
            if original_getattr:
                torch._classes.__getattr__ = types.MethodType(safe_getattr, torch._classes)
        
        print("PyTorch fix applied successfully.")
        return True
    except ImportError:
        print("PyTorch not found, skipping fixes.")
        return False
    except Exception as e:
        print(f"Error applying PyTorch fix: {e}")
        return False

if __name__ == "__main__":
    # Apply fixes when run directly
    apply_pytorch_fixes() 