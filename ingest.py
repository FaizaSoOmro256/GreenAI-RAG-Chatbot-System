"""
Data Ingestion Script for GreenAI Chatbot

This script ingests documents from the data directory into the Pinecone vector store.
Run this script before starting the main application.
"""

import os
import sys
from utils.ingest import ingest_documents

if __name__ == "__main__":
    # Get the data directory
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    print(f"Starting data ingestion from {data_dir}...")
    
    try:
        # Ingest documents
        ingest_documents(data_dir)
        print("Data ingestion completed successfully!")
    except Exception as e:
        print(f"Error during data ingestion: {e}")
        sys.exit(1) 