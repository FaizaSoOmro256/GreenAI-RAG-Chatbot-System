"""
Test cases for verifying specific value responses from the chatbot.
"""

import pytest
from utils.chatbot import chatbot

def test_specific_responses():
    """Test that the chatbot returns exact values for specific questions."""
    
    test_cases = [
        # Rainfall queries
        {
            "query": "How much annual rainfall does Sukkur receive?",
            "expected_contains": "180mm",
            "should_not_contain": ["Temperature", "Humidity", "Wind"]
        },
        {
            "query": "What is the annual rainfall in Sukkur?",
            "expected_contains": "180mm",
            "should_not_contain": ["Temperature", "Humidity", "Wind"]
        },
        
        # Temperature queries
        {
            "query": "What is the current temperature in Sukkur?",
            "expected_contains": "31°C",
            "should_not_contain": ["Rainfall", "Humidity", "Wind"]
        },
        {
            "query": "What is the average temperature in Sukkur?",
            "expected_contains": "31°C",
            "should_not_contain": ["Rainfall", "Humidity", "Wind"]
        },
        
        # Trend queries
        {
            "query": "What is the temperature trend in Sukkur?",
            "expected_contains": "Increasing by 0.35°C per decade",
            "should_not_contain": ["Rainfall", "Humidity", "Wind"]
        },
        {
            "query": "What is the rainfall trend in Sukkur?",
            "expected_contains": "Decreasing by 2mm per year",
            "should_not_contain": ["Temperature", "Humidity", "Wind"]
        },
        
        # Humidity queries
        {
            "query": "What is the humidity in Sukkur?",
            "expected_contains": "50%",
            "should_not_contain": ["Temperature", "Rainfall", "Wind"]
        },
        {
            "query": "What is the average humidity in Sukkur?",
            "expected_contains": "50%",
            "should_not_contain": ["Temperature", "Rainfall", "Wind"]
        },
        
        # Wind speed queries
        {
            "query": "What is the wind speed in Sukkur?",
            "expected_contains": "12 km/h",
            "should_not_contain": ["Temperature", "Rainfall", "Humidity"]
        },
        {
            "query": "What is the average wind speed in Sukkur?",
            "expected_contains": "12 km/h",
            "should_not_contain": ["Temperature", "Rainfall", "Humidity"]
        }
    ]
    
    for test_case in test_cases:
        response = chatbot.generate_response(test_case["query"])
        response_lower = response.lower()
        
        # Check that the response contains the expected value
        assert any(expected.lower() in response_lower for expected in test_case["expected_contains"].split("|")), \
            f"Response should contain {test_case['expected_contains']} for query: {test_case['query']}"
        
        # Check that the response doesn't contain unwanted information
        for unwanted in test_case["should_not_contain"]:
            assert unwanted.lower() not in response_lower, \
                f"Response should not contain {unwanted} for query: {test_case['query']}"

def test_general_queries():
    """Test that the chatbot still returns full information for general queries."""
    
    general_queries = [
        "Tell me about the climate in Sukkur",
        "What are the weather conditions in Sukkur?",
        "Describe Sukkur's climate",
        "Give me information about Sukkur"
    ]
    
    expected_sections = ["Temperature", "Rainfall", "Humidity", "Wind"]
    
    for query in general_queries:
        response = chatbot.generate_response(query)
        response_lower = response.lower()
        
        # For general queries, response should contain all sections
        for section in expected_sections:
            assert section.lower() in response_lower, \
                f"General query response should contain {section} section for query: {query}"

if __name__ == "__main__":
    pytest.main([__file__]) 