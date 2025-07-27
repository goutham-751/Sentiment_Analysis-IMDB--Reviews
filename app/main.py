from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict import router as predict_router
from app.models.model_loader import sentiment_model
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Configure logging
log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=getattr(logging, log_level))
logger = logging.getLogger(__name__)

app = FastAPI(
    title=os.getenv("API_TITLE", "Sentiment Analysis API"),
    description=os.getenv("API_DESCRIPTION", "LSTM-based sentiment analysis for text"),
    version=os.getenv("API_VERSION", "1.0.0")
)

# Allow CORS for frontend
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
allow_credentials = os.getenv("ALLOW_CREDENTIALS", "true").lower() == "true"

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the prediction router
api_prefix = os.getenv("API_PREFIX", "/api/v1")
app.include_router(predict_router, prefix=api_prefix, tags=["sentiment"])

@app.on_event("startup")
async def startup_event():
    """Initialize the model on startup"""
    try:
        # Create and load the model
        sentiment_model.model = sentiment_model.create_model()
        
        # Load or create tokenizer
        sentiment_model.load_or_create_tokenizer()
        
        logger.info("Sentiment model initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize model: {str(e)}")
        # Don't raise the exception to allow the app to start
        logger.warning("App will start without model initialization")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": os.getenv("APP_NAME", "Sentiment Analysis API"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "endpoints": {
            "predict": f"{os.getenv('API_PREFIX', '/api/v1')}/predict",
            "health": f"{os.getenv('API_PREFIX', '/api/v1')}/health"
        }
    }

@app.get("/health")
async def health_check():
    """Global health check"""
    return {
        "status": "healthy",
        "model_loaded": sentiment_model.model is not None,
        "tokenizer_loaded": sentiment_model.tokenizer is not None,
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.get("/test")
async def test_endpoint():
    """Simple test endpoint"""
    return {
        "message": "API is working!",
        "timestamp": "2024-01-01T00:00:00Z",
        "version": os.getenv("APP_VERSION", "1.0.0")
    }
