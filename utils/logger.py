"""
Logger module for Green AI.
Provides centralized logging functionality.
"""

import logging
import os
from datetime import datetime

def setup_logger():
    """Setup and configure the logger."""
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Configure logger
    logger = logging.getLogger('GreenAI')
    logger.setLevel(logging.INFO)
    
    # Create file handler
    log_file = os.path.join(log_dir, f'greenai_{datetime.now().strftime("%Y%m%d")}.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Create logger instance
logger = setup_logger()

# Export the logger
__all__ = ['logger'] 