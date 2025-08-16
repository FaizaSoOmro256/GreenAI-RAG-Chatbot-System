"""
Test cases for the chatbot response generator.
Tests various conversation flows and response patterns.
"""

import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.chatbot_response_generator import ChatbotResponseGenerator

def test_chatbot_responses():
    """Test various chatbot queries and verify responses."""
    chatbot = ChatbotResponseGenerator()
    
    # Test Project Information Queries
    project_queries = [
        "Who created this project?",
        "Tell me about the team members",
        "Who is supervising this project?",
        "What is the project about?",
        "Tell me about SDG 13",
        "What are the project's future plans?"
    ]
    
    # Test Climate Information Queries
    climate_queries = [
        "What's the weather like in Karachi?",
        "Tell me about rainfall in Hyderabad",
        "What's the temperature in Sukkur?",
        "How is the climate in Larkana?",
        "What are the climate challenges in Thatta?",
        "Compare rainfall between Karachi and Hyderabad",
        "What's tomorrow's forecast for Mirpurkhas?"
    ]
    
    # Test SDG Related Queries
    sdg_queries = [
        "What is SDG 13?",
        "How does this project relate to climate action?",
        "Tell me about sustainable development goals",
        "What are the SDG targets?",
        "How does this help climate action?"
    ]
    
    # Test Research and Data Queries
    research_queries = [
        "What research has been done?",
        "Show me climate data for Sindh",
        "What are the findings about climate change?",
        "Tell me about adaptation measures",
        "What solutions are proposed?"
    ]
    
    def run_test_queries(queries, category):
        """Run a set of test queries and print responses."""
        print(f"\n=== Testing {category} ===\n")
        for query in queries:
            print(f"Query: {query}")
            response = chatbot.generate_response(query)
            print(f"Response: {response}\n")
            print("-" * 50)
    
    # Run all test categories
    run_test_queries(project_queries, "Project Information")
    run_test_queries(climate_queries, "Climate Information")
    run_test_queries(sdg_queries, "SDG Information")
    run_test_queries(research_queries, "Research Information")

if __name__ == "__main__":
    test_chatbot_responses() 