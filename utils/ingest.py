import os
import glob
from typing import List, Dict, Any
from langchain_community.document_loaders import (
    TextLoader,
    CSVLoader,
    PyPDFLoader,
    UnstructuredMarkdownLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import config
from pinecone_loader import get_vector_store

def load_documents(directory: str) -> List[Document]:
    """
    Load documents from the specified directory.
    """
    documents = []
    
    # Define loader mapping
    loader_mapping = {
        ".txt": TextLoader,
        ".csv": CSVLoader,
        ".pdf": PyPDFLoader,
        ".md": UnstructuredMarkdownLoader
    }
    
    # Check if directory exists
    if not os.path.exists(directory):
        return documents
    
    # Walk through directory and load documents
    for ext, loader_cls in loader_mapping.items():
        files = glob.glob(os.path.join(directory, f"**/*{ext}"), recursive=True)
        for file_path in files:
            try:
                # Special handling for PDFs
                if ext == ".pdf":
                    try:
                        loader = loader_cls(file_path)
                        loaded_docs = loader.load()
                        
                        # Add metadata to PDF documents
                        for doc in loaded_docs:
                            doc.metadata["source"] = file_path
                            doc.metadata["file_type"] = "pdf"
                            doc.metadata["file_name"] = os.path.basename(file_path)
                            
                            # Try to extract title from first page if available
                            if "title" in doc.metadata:
                                pass
                        
                        documents.extend(loaded_docs)
                    except Exception as pdf_error:
                        # Try alternative PDF loader if available
                        try:
                            from langchain_community.document_loaders import UnstructuredPDFLoader
                            alt_loader = UnstructuredPDFLoader(file_path)
                            loaded_docs = alt_loader.load()
                            documents.extend(loaded_docs)
                        except Exception as alt_error:
                            pass
                else:
                    # Handle other document types
                    loader = loader_cls(file_path)
                    loaded_docs = loader.load()
                    documents.extend(loaded_docs)
            except Exception as e:
                pass
    
    return documents

def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Split the documents into chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len
    )
    
    chunks = text_splitter.split_documents(documents)
    return chunks

def ingest_documents(directory: str) -> None:
    """
    Ingest documents into the vector store.
    """
    # Load documents
    documents = load_documents(directory)
    
    if not documents:
        return
    
    # Chunk documents
    chunks = chunk_documents(documents)
    
    # Initialize vector store with our custom implementation
    vector_store = get_vector_store()
    
    # Add documents to vector store
    vector_store.add_documents(chunks)

def ingest_pdfs(pdf_directory: str = None) -> None:
    """
    Specifically ingest PDF documents from the PDFs directory.
    
    Args:
        pdf_directory: Optional path to PDF directory. If None, uses default data/pdfs.
    """
    if pdf_directory is None:
        pdf_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "pdfs")
    
    if not os.path.exists(pdf_directory):
        os.makedirs(pdf_directory, exist_ok=True)
    
    ingest_documents(pdf_directory)

if __name__ == "__main__":
    # If this file is run directly, ingest documents from the data directory
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    ingest_documents(data_dir)
    
    # Also specifically ingest PDFs
    ingest_pdfs() 