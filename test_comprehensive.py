"""
Comprehensive test script for the GreenAI chatbot.
Tests all categories of questions from test_questions.txt.
"""

import sys
import os
import re
from typing import List, Dict

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.chatbot_response_generator import ChatbotResponseGenerator

def load_test_questions() -> Dict[str, List[str]]:
    """Load test questions from test_questions.txt."""
    questions = {}
    current_category = ""
    subcategory = ""
    
    with open("test_questions.txt", "r") as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line or line.startswith("="):  # Skip empty lines and separator lines
            continue
            
        # Check for main category (numbered sections)
        if re.match(r"^\d+\.", line):
            current_category = re.sub(r"^\d+\.\s*", "", line)  # Remove number and dot
            current_category = current_category.replace("Questions", "").strip()
            questions[current_category] = []
            continue
            
        # Check for subcategory
        if line.endswith(":"):
            subcategory = line[:-1]
            continue
            
        # Add question if it starts with "-"
        if line.startswith("- "):
            if current_category:  # Only add if we have a valid category
                questions[current_category].append(line[2:])
    
    return questions

def run_tests(questions: Dict[str, List[str]], output_file: str = "test_results.txt"):
    """Run all test questions and save results."""
    chatbot = ChatbotResponseGenerator()
    
    with open(output_file, "w", encoding='utf-8') as f:
        f.write("GreenAI Chatbot Test Results\n")
        f.write("==========================\n\n")
        
        total_questions = sum(len(q) for q in questions.values())
        current_question = 0
        
        for category, category_questions in questions.items():
            f.write(f"\n{category}\n")
            f.write("-" * len(category) + "\n\n")
            
            for question in category_questions:
                current_question += 1
                print(f"Testing question {current_question}/{total_questions}: {question[:50]}...")
                
                f.write(f"Q: {question}\n")
                response = chatbot.generate_response(question)
                f.write(f"A: {response}\n")
                f.write("-" * 80 + "\n\n")

def analyze_results(output_file: str = "test_results.txt") -> Dict[str, int]:
    """Analyze test results for response patterns."""
    with open(output_file, "r", encoding='utf-8') as f:
        content = f.read()
    
    # Count response types
    stats = {
        "total_questions": len(re.findall(r"^Q:", content, re.MULTILINE)),
        "welcome_message": len(re.findall(r"Welcome to GreenAI Climate Assistant!", content)),
        "district_responses": len(re.findall(r"Climate Information for", content)),
        "sdg_responses": len(re.findall(r"SDG 13", content)),
        "research_responses": len(re.findall(r"Research Findings:", content)),
        "adaptation_responses": len(re.findall(r"Adaptation Measures", content))
    }
    
    return stats

def print_analysis(stats: Dict[str, int]):
    """Print analysis of test results."""
    print("\nTest Analysis")
    print("=============")
    print(f"Total Questions Tested: {stats['total_questions']}")
    print(f"Default Welcome Responses: {stats['welcome_message']}")
    print(f"District-Specific Responses: {stats['district_responses']}")
    print(f"SDG-Related Responses: {stats['sdg_responses']}")
    print(f"Research-Related Responses: {stats['research_responses']}")
    print(f"Adaptation-Related Responses: {stats['adaptation_responses']}")
    
    coverage = (stats['total_questions'] - stats['welcome_message']) / stats['total_questions'] * 100
    print(f"\nResponse Coverage: {coverage:.1f}%")

def main():
    """Run comprehensive tests and analysis."""
    print("Loading test questions...")
    questions = load_test_questions()
    
    print(f"\nLoaded {sum(len(q) for q in questions.values())} questions across {len(questions)} categories:")
    for category, category_questions in questions.items():
        print(f"- {category}: {len(category_questions)} questions")
    
    print("\nRunning tests...")
    run_tests(questions)
    
    print("\nAnalyzing results...")
    stats = analyze_results()
    print_analysis(stats)
    
    print("\nTest results have been saved to test_results.txt")

if __name__ == "__main__":
    main() 