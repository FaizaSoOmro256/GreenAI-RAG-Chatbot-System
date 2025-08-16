"""
Test script for the GreenAI chatbot.
"""

from utils.sensor_integration import RealTimeClimateData
from utils.chatbot import generate_response

def test_chatbot():
    """Test the chatbot with various queries."""
    test_queries = [
        "What's the current temperature in Karachi?",
        "Show me the climate data for Northern Sindh",
        "What are the climate challenges in Tharparkar?",
        "What's the weather like in Hyderabad?"
    ]
    
    print("Testing GreenAI Chatbot...\n")
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 50)
        response = generate_response(query)
        print(f"Response:\n{response}")
        print("-" * 50)

if __name__ == "__main__":
    test_chatbot() 