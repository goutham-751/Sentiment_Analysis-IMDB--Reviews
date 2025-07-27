# Quick Vercel Deployment Guide (Using .env File)

## Step 1: Create Your .env File

1. Copy `env.example` to `.env`:
   ```bash
   cp env.example .env
   ```

2. Update the `.env` file with your actual values:
   - Replace `your-frontend-domain.vercel.app` with your actual frontend URL
   - Replace `your-backend-domain.vercel.app` with your actual backend URL
   - Change `SECRET_KEY` and `API_KEY` to secure random strings

## Step 2: Essential Variables to Update

Make sure these are set correctly in your `.env`:

```
APP_NAME=sentiment-analysis-app
APP_VERSION=1.0.0
ENVIRONMENT=production
DEBUG=false
ALLOWED_ORIGINS=https://your-actual-frontend-url.vercel.app,http://localhost:3000
BACKEND_URL=https://your-actual-backend-url.vercel.app
SECRET_KEY=your-actual-secret-key-here
API_KEY=your-actual-api-key-here
```

## Step 3: Deploy
1. Push your code (including `.env` file) to GitHub
2. Connect to Vercel
3. **No need to set environment variables in Vercel dashboard** - they'll be loaded from `.env`
4. Deploy!

## Step 4: Test
Visit your deployed URL + `/test` to verify it's working.

## Troubleshooting

**If deployment fails:**
1. Check Vercel logs for specific errors
2. Make sure `.env` file is in your repository
3. Verify all `__init__.py` files are present
4. Try deploying without TensorFlow first (comment out in requirements.txt)

**If TensorFlow is too large:**
- Use `tensorflow-cpu` instead of `tensorflow` (already done)
- Consider using a lighter ML library like `scikit-learn` only

**Common Issues:**
- Missing `__init__.py` files (fixed)
- Model files not found (handled gracefully now)
- `.env` file not found (make sure it's in your repository) 