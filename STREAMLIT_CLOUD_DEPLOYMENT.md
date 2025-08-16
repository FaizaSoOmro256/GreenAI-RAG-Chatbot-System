# 🚀 Streamlit Cloud Deployment Guide for GreenAI

## Prerequisites
- ✅ GitHub repository is public (or Streamlit Cloud Pro account)
- ✅ All code is committed and pushed to GitHub
- ✅ API keys ready for Pinecone and Google Gemini

## 🎯 Quick Deployment Steps

### 1. **Go to Streamlit Cloud**
- Visit [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click "New app"

### 2. **Configure Your App**
- **Repository**: Select your GreenAI repository
- **Branch**: `main` or `master`
- **Main file path**: `app.py`
- **App URL**: Choose your preferred subdomain

### 3. **Advanced Settings**
- **Python version**: 3.11 (recommended)
- **Requirements file**: `requirements-streamlit-cloud.txt`

### 4. **Add Secrets (API Keys)**
Click "Advanced settings" → "Secrets" and add:
```toml
PINECONE_API_KEY = "your_actual_pinecone_api_key"
PINECONE_ENVIRONMENT = "your_pinecone_environment"
GEMINI_API_KEY = "your_actual_gemini_api_key"
```

### 5. **Deploy**
- Click "Deploy"
- Wait 3-5 minutes for build and deployment

## 🔧 Configuration Files Created

### `packages.txt` - System Dependencies
```
build-essential
python3-dev
gcc
g++
libopenblas-dev
liblapack-dev
libatlas-base-dev
```

### `requirements-streamlit-cloud.txt` - Python Dependencies
- CPU-only PyTorch versions
- Compatible LangChain versions
- All necessary ML libraries

### `.streamlit/config.toml` - Streamlit Configuration
- Production-ready settings
- Optimized for cloud deployment

## 🚨 Important Notes

### **PyTorch CPU Version**
- Using `torch==2.4.1+cpu` for Streamlit Cloud compatibility
- Avoids GPU-related build issues

### **System Dependencies**
- `libopenblas-dev` and `liblapack-dev` for numerical computations
- `gcc` and `g++` for compiling C extensions

### **API Keys**
- **NEVER** commit API keys to GitHub
- Use Streamlit Cloud secrets management
- Keys are encrypted and secure

## 🐛 Troubleshooting

### **Build Failures**
1. Check if all dependencies are in `requirements-streamlit-cloud.txt`
2. Verify system dependencies in `packages.txt`
3. Check Streamlit Cloud logs for specific errors

### **Import Errors**
1. Ensure all imports use correct package names
2. Check for version compatibility issues
3. Verify `langchain-pinecone` compatibility

### **Memory Issues**
1. Streamlit Cloud has memory limits
2. Consider using smaller models
3. Optimize data loading

## 📱 Your App URL
After successful deployment, your app will be available at:
```
https://your-app-name.streamlit.app
```

## 🔄 Updates
- Push changes to GitHub
- Streamlit Cloud automatically redeploys
- Monitor deployment logs for any issues

## 📞 Support
- Check Streamlit Cloud documentation
- Review deployment logs
- Ensure all dependencies are compatible
