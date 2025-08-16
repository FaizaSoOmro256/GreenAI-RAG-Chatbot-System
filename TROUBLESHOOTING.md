# Streamlit Cloud Deployment Troubleshooting

## Current Status: Minimal Test Deployment

### Step 1: Test Basic Deployment
1. **Current setup**: Minimal `requirements.txt` with only essential packages
2. **Test app**: `test_app.py` - Simple Streamlit app to verify deployment
3. **Goal**: Get basic deployment working first

### Step 2: Check Deployment Logs
If you still get errors, check the **specific error message** in Streamlit Cloud logs:

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click on your app
3. Click "Manage App" → "Logs"
4. Look for the **exact error message**

### Step 3: Common Error Types

#### A. Package Installation Errors
```
ERROR: No matching distribution found for [package_name]
```
**Solution**: Remove problematic package from requirements.txt

#### B. Import Errors
```
ModuleNotFoundError: No module named '[module_name]'
```
**Solution**: Add missing dependency to requirements.txt

#### C. Memory/Resource Errors
```
MemoryError or timeout errors
```
**Solution**: Reduce dependencies or upgrade to paid tier

#### D. Python Version Issues
```
Requires-Python <3.12
```
**Solution**: Update package versions to support Python 3.12

### Step 4: Gradual Dependency Addition

Once basic deployment works:

1. **Add one dependency at a time**
2. **Test deployment after each addition**
3. **Identify which package causes issues**

### Step 5: Alternative Approaches

#### Option A: Use test_app.py temporarily
- Set main file to `test_app.py` in Streamlit Cloud
- Verify deployment works
- Gradually add dependencies

#### Option B: Create separate requirements files
- `requirements-minimal.txt` - Basic deployment
- `requirements-full.txt` - Complete app
- Switch between them as needed

### Step 6: Environment Variables

Make sure to set these in Streamlit Cloud Secrets:
```toml
[secrets]
GOOGLE_API_KEY = "your_key"
PINECONE_API_KEY = "your_key"
PINECONE_ENVIRONMENT = "your_env"
PINECONE_INDEX_NAME = "your_index"
```

## Getting Help

1. **Share the exact error message** from logs
2. **Include the requirements.txt content**
3. **Mention which step failed**

## Quick Commands

```bash
# Check current status
git status

# Push latest changes
git add .
git commit -m "Update requirements"
git push origin main

# Test locally
streamlit run test_app.py
``` 