import os
from dotenv import load_dotenv

# Load environment variables (only if .env file exists, to avoid overriding Streamlit Cloud secrets)
if os.path.exists('.env'):
    load_dotenv()

# API Keys and credentials
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX = os.getenv("PINECONE_INDEX", "greenai-sindh")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

# Model configuration
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
GEMINI_MODEL_NAME = "models/gemini-2.0-flash"
TEMPERATURE = 0.2
MAX_OUTPUT_TOKENS = 2048
TOP_K = 30
TOP_P = 0.85

# RAG configuration
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
NUM_RESULTS = 4
SIMILARITY_SCORE_THRESHOLD = 0.65

# UI configuration
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "english")
SUPPORTED_LANGUAGES = {
    "english": "English", 
    "urdu": "اردو", 
    "sindhi": "سنڌي"
}

APP_TITLE = "Green AI: Sindh's Sustainable Climate Actions"
APP_DESCRIPTION = {
    "english": "An intelligent chatbot for information on sustainable climate actions in Sindh",
    "urdu": "سندھ میں پائیدار آب و ہوا کے اقدامات کے بارے میں معلومات کے لیے ایک ذہین چیٹ بوٹ",
    "sindhi": "سنڌ ۾ پائيدار آب و هوا جي قدمن بابت معلومات لاءِ هڪ ذهين چيٽ بوٽ"
}

WELCOME_MESSAGE = {
    "english": "👋 Hello! I'm Green AI, your assistant for sustainable climate actions in Sindh. How can I help you today?",
    "urdu": "👋 ہیلو! میں ایکوسفیئر اے آئی ہوں، سندھ میں پائیدار آب و ہوا کے اقدامات کے لیے آپکا اسسٹنٹ۔ میں آج آپ کی کیسے مدد کر سکتا ہوں؟",
    "sindhi": "👋 هيلو! مان ايڪوسفيئر اي آئي آهيان، سنڌ ۾ پائيدار آب و هوا جي قدمن لاءِ توهان جو اسسٽنٽ. مان اڄ توهان جي ڪيئن مدد ڪري سگھان ٿو؟"
}

INPUT_PLACEHOLDER = {
    "english": "Ask me anything about climate actions in Sindh...",
    "urdu": "سندھ میں آب و ہوا کے اقدامات کے بارے میں مجھ سے کچھ بھی پوچھیں...",
    "sindhi": "سنڌ ۾ آب و هوا جي قدمن بابت مون کان ڪجھ به پڇو..."
}

# Debug mode
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true" 