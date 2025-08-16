"""
PDF utility functions for the GreenAI Climate Assistant.
"""

import os
import logging
from typing import List, Dict, Any, Optional
from langchain_community.document_loaders import PyPDFLoader, UnstructuredPDFLoader
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def extract_pdf_text(pdf_path: str, use_ocr: bool = False) -> Dict[str, Any]:
    """
    Extract text from a PDF file using multiple methods for better accuracy.
    
    Args:
        pdf_path: Path to the PDF file
        use_ocr: Whether to use OCR for text extraction (useful for scanned PDFs)
        
    Returns:
        Dict containing extracted text and metadata
    """
    result = {
        "text": "",
        "metadata": {},
        "pages": [],
        "error": None
    }
    
    try:
        # First try with pdfplumber for better text extraction
        with pdfplumber.open(pdf_path) as pdf:
            # Extract metadata
            result["metadata"] = {
                "title": pdf.metadata.get("Title", ""),
                "author": pdf.metadata.get("Author", ""),
                "creation_date": pdf.metadata.get("CreationDate", ""),
                "pages": len(pdf.pages),
                "source": pdf_path,
                "extraction_date": datetime.now().isoformat()
            }
            
            # Extract text from each page
            for page_num, page in enumerate(pdf.pages, 1):
                page_text = page.extract_text() or ""
                result["pages"].append({
                    "page_num": page_num,
                    "text": page_text,
                    "tables": len(page.find_tables())
                })
                result["text"] += f"\n\nPage {page_num}:\n{page_text}"
        
        # If text extraction yielded no results and OCR is enabled, try OCR
        if not result["text"].strip() and use_ocr:
            # Convert PDF to images
            images = convert_from_path(pdf_path)
            ocr_text = ""
            
            for i, image in enumerate(images, 1):
                # Perform OCR on each page
                page_text = pytesseract.image_to_string(image)
                ocr_text += f"\n\nPage {i}:\n{page_text}"
                result["pages"][i-1]["text"] = page_text
            
            result["text"] = ocr_text
            result["metadata"]["ocr_used"] = True
    
    except Exception as e:
        # Try alternative methods if primary method fails
        try:
            # Try PyPDFLoader as backup
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            result["text"] = "\n\n".join(doc.page_content for doc in docs)
            result["metadata"]["extraction_method"] = "PyPDFLoader"
        except Exception as e2:
            try:
                # Try UnstructuredPDFLoader as last resort
                loader = UnstructuredPDFLoader(pdf_path)
                docs = loader.load()
                result["text"] = "\n\n".join(doc.page_content for doc in docs)
                result["metadata"]["extraction_method"] = "UnstructuredPDFLoader"
            except Exception as e3:
                result["error"] = f"All extraction methods failed: {e}, {e2}, {e3}"
    
    return result

def analyze_pdf_content(pdf_path: str) -> Dict[str, Any]:
    """
    Analyze the content of a PDF file to determine its structure and content type.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Dict containing analysis results
    """
    analysis = {
        "structure": {
            "total_pages": 0,
            "has_tables": False,
            "has_images": False,
            "has_text": False,
            "language_hint": "en"  # Default to English
        },
        "content_type": {
            "is_report": False,
            "is_scientific": False,
            "is_presentation": False,
            "is_form": False
        },
        "metadata": {},
        "error": None
    }
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            analysis["structure"]["total_pages"] = len(pdf.pages)
            analysis["metadata"] = pdf.metadata
            
            # Analyze each page
            for page in pdf.pages:
                # Check for tables
                if page.find_tables():
                    analysis["structure"]["has_tables"] = True
                
                # Check for text
                if page.extract_text().strip():
                    analysis["structure"]["has_text"] = True
                
                # Check for images (if any image objects are found)
                if page.images:
                    analysis["structure"]["has_images"] = True
            
            # Try to determine content type based on structure and content
            text_content = "\n".join(page.extract_text() for page in pdf.pages).lower()
            
            # Check if it's a scientific document
            if any(term in text_content for term in ["abstract", "methodology", "conclusion", "references", "et al"]):
                analysis["content_type"]["is_scientific"] = True
            
            # Check if it's a report
            if any(term in text_content for term in ["executive summary", "findings", "recommendations"]):
                analysis["content_type"]["is_report"] = True
            
            # Check if it's a presentation
            if len(pdf.pages) > 0 and pdf.pages[0].width > pdf.pages[0].height:
                analysis["content_type"]["is_presentation"] = True
            
            # Check if it's a form
            if analysis["structure"]["has_tables"] and not analysis["content_type"]["is_scientific"]:
                analysis["content_type"]["is_form"] = True
    
    except Exception as e:
        analysis["error"] = str(e)
    
    return analysis

def extract_pdf_metadata(pdf_path: str) -> Dict[str, Any]:
    """
    Extract detailed metadata from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Dict containing metadata
    """
    metadata = {
        "filename": os.path.basename(pdf_path),
        "file_size": os.path.getsize(pdf_path),
        "creation_time": None,
        "modification_time": None,
        "pdf_metadata": {},
        "error": None
    }
    
    try:
        # Get file timestamps
        stats = os.stat(pdf_path)
        metadata["creation_time"] = datetime.fromtimestamp(stats.st_ctime).isoformat()
        metadata["modification_time"] = datetime.fromtimestamp(stats.st_mtime).isoformat()
        
        # Extract PDF-specific metadata
        with pdfplumber.open(pdf_path) as pdf:
            metadata["pdf_metadata"] = pdf.metadata
            metadata["page_count"] = len(pdf.pages)
            
            # Get page sizes
            if len(pdf.pages) > 0:
                first_page = pdf.pages[0]
                metadata["page_size"] = {
                    "width": first_page.width,
                    "height": first_page.height
                }
    
    except Exception as e:
        metadata["error"] = str(e)
    
    return metadata 