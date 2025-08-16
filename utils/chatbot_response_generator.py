"""
Response generator for the GreenAI Climate Chatbot.
Handles response generation and integration with the chatbot core.
"""

from utils.chatbot import ChatBot

# Initialize the chatbot instance
chatbot = ChatBot()

def generate_response(user_input: str) -> str:
    """
    Generate a response for the given user input.
    
    Args:
        user_input (str): The user's message/query
        
    Returns:
        str: The chatbot's response
    """
    try:
        # Get response from chatbot core
        response = chatbot.get_response(user_input)
        return response
    except Exception as e:
        return f"I apologize, but I encountered an error processing your request: {str(e)}" 