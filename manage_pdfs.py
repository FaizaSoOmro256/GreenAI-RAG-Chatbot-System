#!/usr/bin/env python3
"""
PDF Management Script for GreenAI Climate Assistant

This script provides command-line utilities for managing PDF documents in the climate assistant.
It can:
1. List all PDFs in the data/pdfs directory
2. Add new PDFs (with automatic text extraction and metadata analysis)
3. Remove PDFs
4. Analyze PDF content
5. Extract text from PDFs (with OCR support)
"""

import os
import sys
import argparse
import shutil
from typing import List, Dict, Any
import logging
from utils.pdf_utils import extract_pdf_text, analyze_pdf_content, extract_pdf_metadata
from utils.ingest import ingest_pdfs

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_pdf_dir() -> str:
    """Get the PDF directory path."""
    return os.path.join(os.path.dirname(__file__), "data", "pdfs")

def list_pdfs() -> List[str]:
    """List all PDFs in the data/pdfs directory."""
    pdf_dir = get_pdf_dir()
    if not os.path.exists(pdf_dir):
        logger.warning(f"PDF directory {pdf_dir} does not exist.")
        return []
    
    pdfs = []
    for file in os.listdir(pdf_dir):
        if file.lower().endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, file)
            metadata = extract_pdf_metadata(pdf_path)
            pdfs.append({
                'filename': file,
                'size': metadata['file_size'],
                'pages': metadata.get('page_count', 'Unknown'),
                'creation_time': metadata['creation_time']
            })
    
    return pdfs

def add_pdf(source_path: str, analyze: bool = True) -> Dict[str, Any]:
    """
    Add a PDF to the data/pdfs directory.
    
    Args:
        source_path: Path to the PDF file to add
        analyze: Whether to analyze the PDF content
        
    Returns:
        Dict containing operation results
    """
    result = {
        "success": False,
        "message": "",
        "analysis": None,
        "error": None
    }
    
    try:
        # Validate source file
        if not os.path.exists(source_path):
            result["error"] = f"Source file {source_path} does not exist"
            return result
        
        if not source_path.lower().endswith('.pdf'):
            result["error"] = f"File {source_path} is not a PDF"
            return result
        
        # Create PDF directory if it doesn't exist
        pdf_dir = get_pdf_dir()
        os.makedirs(pdf_dir, exist_ok=True)
        
        # Copy file to PDF directory
        dest_path = os.path.join(pdf_dir, os.path.basename(source_path))
        shutil.copy2(source_path, dest_path)
        
        # Extract text and analyze content if requested
        if analyze:
            result["analysis"] = {
                "metadata": extract_pdf_metadata(dest_path),
                "content": analyze_pdf_content(dest_path),
                "text_extraction": extract_pdf_text(dest_path)
            }
        
        # Trigger ingestion of the new PDF
        ingest_pdfs()
        
        result["success"] = True
        result["message"] = f"Successfully added {os.path.basename(source_path)}"
        
    except Exception as e:
        result["error"] = str(e)
        logger.error(f"Error adding PDF {source_path}: {e}")
    
    return result

def remove_pdf(filename: str) -> Dict[str, Any]:
    """
    Remove a PDF from the data/pdfs directory.
    
    Args:
        filename: Name of the PDF file to remove
        
    Returns:
        Dict containing operation results
    """
    result = {
        "success": False,
        "message": "",
        "error": None
    }
    
    try:
        pdf_dir = get_pdf_dir()
        pdf_path = os.path.join(pdf_dir, filename)
        
        if not os.path.exists(pdf_path):
            result["error"] = f"PDF {filename} does not exist"
            return result
        
        os.remove(pdf_path)
        result["success"] = True
        result["message"] = f"Successfully removed {filename}"
        
    except Exception as e:
        result["error"] = str(e)
        logger.error(f"Error removing PDF {filename}: {e}")
    
    return result

def analyze_pdf(filename: str, use_ocr: bool = False) -> Dict[str, Any]:
    """
    Analyze a PDF file.
    
    Args:
        filename: Name of the PDF file to analyze
        use_ocr: Whether to use OCR for text extraction
        
    Returns:
        Dict containing analysis results
    """
    result = {
        "success": False,
        "analysis": None,
        "error": None
    }
    
    try:
        pdf_dir = get_pdf_dir()
        pdf_path = os.path.join(pdf_dir, filename)
        
        if not os.path.exists(pdf_path):
            result["error"] = f"PDF {filename} does not exist"
            return result
        
        result["analysis"] = {
            "metadata": extract_pdf_metadata(pdf_path),
            "content": analyze_pdf_content(pdf_path),
            "text": extract_pdf_text(pdf_path, use_ocr=use_ocr)
        }
        result["success"] = True
        
    except Exception as e:
        result["error"] = str(e)
        logger.error(f"Error analyzing PDF {filename}: {e}")
    
    return result

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="PDF Management Tool for GreenAI Climate Assistant")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all PDFs")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a PDF")
    add_parser.add_argument("file", help="Path to the PDF file to add")
    add_parser.add_argument("--no-analyze", action="store_true", help="Skip content analysis")
    
    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a PDF")
    remove_parser.add_argument("file", help="Name of the PDF file to remove")
    
    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a PDF")
    analyze_parser.add_argument("file", help="Name of the PDF file to analyze")
    analyze_parser.add_argument("--ocr", action="store_true", help="Use OCR for text extraction")
    
    args = parser.parse_args()
    
    if args.command == "list":
        pdfs = list_pdfs()
        if pdfs:
            print("\nAvailable PDFs:")
            print("-" * 80)
            for pdf in pdfs:
                print(f"• {pdf['filename']}")
                print(f"  - Size: {pdf['size']} bytes")
                print(f"  - Pages: {pdf['pages']}")
                print(f"  - Created: {pdf['creation_time']}")
                print("-" * 80)
        else:
            print("No PDFs found in the data/pdfs directory.")
    
    elif args.command == "add":
        result = add_pdf(args.file, analyze=not args.no_analyze)
        if result["success"]:
            print(f"\n✓ {result['message']}")
            if result.get("analysis"):
                print("\nAnalysis Results:")
                print("-" * 80)
                analysis = result["analysis"]
                print(f"• Pages: {analysis['metadata'].get('page_count', 'Unknown')}")
                print(f"• Has Tables: {analysis['content']['structure']['has_tables']}")
                print(f"• Has Images: {analysis['content']['structure']['has_images']}")
                print(f"• Document Type: ", end="")
                content_type = analysis['content']['content_type']
                if content_type['is_scientific']:
                    print("Scientific Document")
                elif content_type['is_report']:
                    print("Report")
                elif content_type['is_presentation']:
                    print("Presentation")
                elif content_type['is_form']:
                    print("Form")
                else:
                    print("General Document")
        else:
            print(f"\n✗ Error: {result['error']}")
    
    elif args.command == "remove":
        result = remove_pdf(args.file)
        if result["success"]:
            print(f"\n✓ {result['message']}")
        else:
            print(f"\n✗ Error: {result['error']}")
    
    elif args.command == "analyze":
        result = analyze_pdf(args.file, use_ocr=args.ocr)
        if result["success"]:
            print("\nAnalysis Results:")
            print("-" * 80)
            analysis = result["analysis"]
            print(f"• Metadata:")
            print(f"  - Pages: {analysis['metadata'].get('page_count', 'Unknown')}")
            print(f"  - File Size: {analysis['metadata']['file_size']} bytes")
            print(f"  - Created: {analysis['metadata']['creation_time']}")
            print("\n• Structure:")
            print(f"  - Has Tables: {analysis['content']['structure']['has_tables']}")
            print(f"  - Has Images: {analysis['content']['structure']['has_images']}")
            print(f"  - Has Text: {analysis['content']['structure']['has_text']}")
            print("\n• Content Type:")
            content_type = analysis['content']['content_type']
            if content_type['is_scientific']:
                print("  - Scientific Document")
            elif content_type['is_report']:
                print("  - Report")
            elif content_type['is_presentation']:
                print("  - Presentation")
            elif content_type['is_form']:
                print("  - Form")
            else:
                print("  - General Document")
            
            # Show first 500 characters of extracted text
            text = analysis['text']['text']
            if text:
                print("\n• First 500 characters of extracted text:")
                print("-" * 80)
                print(text[:500] + "...")
        else:
            print(f"\n✗ Error: {result['error']}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 