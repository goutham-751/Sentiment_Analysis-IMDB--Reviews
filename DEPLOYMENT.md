# Vercel Deployment Guide

## Environment Variables

Copy these environment variables to your Vercel project settings:

### Application Configuration
```
APP_NAME=sentiment-analysis-app
APP_VERSION=1.0.0
DEBUG=false
ENVIRONMENT=production
```

### Server Configuration
```
HOST=0.0.0.0
PORT=8000
WORKERS=1
```

### CORS Configuration
```
ALLOWED_ORIGINS=https://your-actual-frontend-url.vercel.app,http://localhost:3000
ALLOW_CREDENTIALS=true
```

### Model Configuration
```
MODEL_PATH=app/models/
TOKENIZER_PATH=app/models/tokenizer.pkl
MAX_SEQUENCE_LENGTH=200
NUM_WORDS=5000
```

### TensorFlow Configuration
```
TF_CPP_MIN_LOG_LEVEL=2
TF_FORCE_GPU_ALLOW_GROWTH=true
```

### Logging Configuration
```
LOG_LEVEL=INFO
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

### API Configuration
```
API_PREFIX=/api/v1
API_TITLE=Sentiment Analysis API
API_DESCRIPTION=LSTM-based sentiment analysis for text
API_VERSION=1.0.0
```

### Frontend Configuration (if using Streamlit)
```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
```

### Backend URL for frontend
```
BACKEND_URL=https://your-actual-backend-url.vercel.app
```

### Security (Change these in production!)
```
SECRET_KEY=your-actual-secret-key-here
API_KEY=your-actual-api-key-here
```

## How to Set Environment Variables in Vercel

1. Go to your Vercel dashboard
2. Select your project
3. Go to "Settings" tab
4. Click on "Environment Variables"
5. Add each variable from the list above
6. Make sure to set the environment to "Production" (and optionally "Preview" and "Development")

## Important Notes

1. **Update URLs**: Replace `your-frontend-domain.vercel.app` and `your-backend-domain.vercel.app` with your actual Vercel domains
2. **Security**: Change the `SECRET_KEY` and `API_KEY` to secure random strings
3. **Model Files**: Make sure your model files (`tokenizer.pkl` and any trained models) are included in your repository
4. **TensorFlow**: The app uses TensorFlow, which might have size limitations on Vercel's free tier

## Deployment Steps

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Set all environment variables in Vercel dashboard
4. Deploy!

## Troubleshooting

- If you get timeout errors, increase the `maxDuration` in `vercel.json`
- If TensorFlow is too large, consider using a lighter model or different hosting
- Make sure all required files are in your repository
- Check Vercel logs for any missing dependencies 

## ✅ **Updated Configuration for .env Files:**

### 1. **Modified `app/main.py`:**
- Now loads environment variables from `.env` file with `override=True`
- This means your `.env` file will take precedence over any system environment variables

### 2. **Cleared `vercel.json`:**
- Removed all hardcoded environment variables
- Now relies entirely on your `.env` file

### 3. **Created `env.example`:**
- Comprehensive template with all possible environment variables
- Well-documented with comments

### 4. **Updated `QUICK_DEPLOY.md`:**
- Instructions for using `.env` files
- No need to set variables in Vercel dashboard

## 🚀 **How to Deploy with .env File:**

### Step 1: Create Your .env File
```bash
cp env.example .env
```

### Step 2: Update Your .env File
Edit `.env` and change these critical values:
```
<code_block_to_apply_changes_from>
```

### Step 3: Deploy
1. Push your code (including `.env`) to GitHub
2. Connect to Vercel
3. **No need to set environment variables in Vercel dashboard**
4. Deploy!

## 🔒 **Important Security Notes:**

- Make sure your `.env` file is in your repository (for Vercel to access it)
- Change the `SECRET_KEY` and `API_KEY` to secure random strings
- Update the URLs with your actual Vercel domains

The app will now automatically load all environment variables from your `.env` file when deployed to Vercel! 