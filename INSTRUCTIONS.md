# Running the GreenAI Chatbot

Follow these steps to set up and run the GreenAI chatbot on your local machine:

## Prerequisites

1. Python 3.8 or higher installed on your system
2. A Pinecone account for vector storage (free tier available)
3. A Google API key with access to Gemini models

## Installation Steps

1. **Clone the repository** (if you haven't already)

2. **Set up a virtual environment (Recommended)**

   Use the provided script to create a fresh virtual environment:
   ```
   python setup_venv.py
   ```

   Then activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install dependencies**

   **Option 1: Using the installation script (Recommended)**
   ```
   python install.py
   ```
   This script handles installing packages one by one to avoid conflicts.

   **Option 2: Manual installation (If you encounter issues)**
   ```
   pip install streamlit python-dotenv
   pip install google-generativeai pydantic
   pip install langchain langchain-core langchain-community
   pip install pinecone-client==2.0.0 langchain-pinecone==0.1.0
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   pip install sentence-transformers
   pip install pillow
   ```

4. **Check compatibility**

   Verify that all packages are installed correctly:
   ```
   python check_compatibility.py
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the root directory with the following variables:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
   PINECONE_INDEX=greenai-sindh-index
   GEMINI_API_KEY=your_gemini_api_key
   ```

   Replace the placeholder values with your actual API keys.

6. **Ingest data into the vector store**
   
   Run the data ingestion script:
   ```
   python ingest.py
   ```
   
   This will load the documents from the `data/` directory and index them in Pinecone.

7. **Run the application**
   
   Start the Streamlit application:
   ```
   streamlit run app.py
   ```
   
   The application should open in your default web browser at http://localhost:8501

## Adding Your Own Data

To add your own data about climate actions in Sindh:

1. Add your text, PDF, CSV, or Markdown files to the `data/` directory
2. Run the ingestion script again:
   ```
   python ingest.py
   ```

## Troubleshooting

- **Dependency Conflicts**: If you encounter dependency conflicts, try using a fresh virtual environment and install packages one by one using the `setup_venv.py` script.

- **Pinecone Package Error**: If you see an error about Pinecone package compatibility, run:
  ```
  pip uninstall -y pinecone-client pinecone langchain-pinecone
  pip install pinecone-client==2.0.0
  pip install langchain-pinecone==0.1.0
  ```

- **Sentence Transformers Installation**: If you have issues with sentence-transformers, first install PyTorch:
  ```
  pip install torch --index-url https://download.pytorch.org/whl/cpu
  pip install sentence-transformers
  ```

- If you encounter errors related to API keys, make sure your `.env` file is correctly set up and your API keys are valid.

- For issues with Streamlit, try running `streamlit clear_cache` before restarting the application.

## Additional Information

- The application supports English, Urdu, and Sindhi languages.
- The RAG system uses the multilingual-MiniLM-L12-v2 model for generating embeddings.
- The LLM is Google's Gemini Flash 2.0 model. 