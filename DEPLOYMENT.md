# Deployment Guide for GreenAI RAG Chatbot

## GitHub Setup

### 1. Initialize Git Repository (if not already done)
```bash
git init
git add .
git commit -m "Initial commit: GreenAI RAG Chatbot"
```

### 2. Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "New repository"
3. Name it: `greenai-rag-chatbot`
4. Make it **Public** (required for Streamlit Cloud free tier)
5. Don't initialize with README (you already have one)
6. Click "Create repository"

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/greenai-rag-chatbot.git
git branch -M main
git push -u origin main
```

## Streamlit Cloud Deployment

### 1. Connect to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"

### 2. Configure App Settings
- **Repository**: Select your `greenai-rag-chatbot` repository
- **Branch**: `main`
- **Main file path**: `app.py`
- **App URL**: Will be auto-generated

### 3. Environment Variables Setup
In Streamlit Cloud dashboard, add these secrets:

```toml
[secrets]
GOOGLE_API_KEY = "your_google_api_key"
PINECONE_API_KEY = "your_pinecone_api_key"
PINECONE_ENVIRONMENT = "your_pinecone_environment"
PINECONE_INDEX_NAME = "your_index_name"
```

### 4. Deploy
Click "Deploy" and wait for the build to complete.

## Environment Variables Required

Create a `.env` file locally (don't commit this to GitHub):

```env
GOOGLE_API_KEY=your_google_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment_here
PINECONE_INDEX_NAME=your_index_name_here
```

## Troubleshooting

### Common Issues:
1. **Import errors**: Make sure all dependencies are in `requirements.txt`
2. **API key errors**: Check that all environment variables are set in Streamlit Cloud
3. **Memory issues**: Consider upgrading to paid tier if app uses too much memory

### Local Testing:
```bash
streamlit run app.py
```

## Security Notes
- Never commit API keys to GitHub
- Use Streamlit Cloud secrets for sensitive data
- Keep your `.env` file local only 