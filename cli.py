from chatbot import GreenAIChatbot
import argparse
import sys

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='GreenAI RAG Chatbot CLI')
    parser.add_argument('--user-id', type=str, default='test_user',
                      help='User ID for conversation tracking')
    args = parser.parse_args()

    # Initialize chatbot
    chatbot = GreenAIChatbot()
    
    print("Welcome to GreenAI RAG Chatbot!")
    print("Type 'exit' to quit, 'history' to view conversation history, or 'clear' to clear history.")
    print("You can ask about climate data, research papers, or SDG indicators.")
    print("\nExample queries:")
    print("- What's the climate like in Karachi?")
    print("- Show me research papers about climate change")
    print("- What are the SDG 13 indicators?")
    print("\nEnter your message:")

    while True:
        try:
            # Get user input
            message = input("> ").strip()
            
            # Handle special commands
            if message.lower() == 'exit':
                print("Goodbye!")
                break
            elif message.lower() == 'history':
                history = chatbot.get_conversation_history(args.user_id)
                print("\nConversation History:")
                for msg in history:
                    print(f"[{msg['timestamp']}] {msg['user_id']}: {msg['message']}")
                print()
                continue
            elif message.lower() == 'clear':
                chatbot.clear_conversation_history(args.user_id)
                print("Conversation history cleared.")
                continue
            
            # Process message
            if message:
                response = chatbot.process_message(message, args.user_id)
                print(f"\nBot: {response['message']}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")

if __name__ == "__main__":
    main() 