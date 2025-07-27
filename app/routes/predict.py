from fastapi import APIRouter, HTTPException
from app.schemas.request_schema import SentimentRequest, SentimentResponse, ErrorResponse
from app.models.model_loader import sentiment_model
from app.utils.preprocess import preprocess_for_sentiment
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/predict", response_model=SentimentResponse)
async def predict_sentiment(request: SentimentRequest):
    """
    Predict sentiment for the given text using the LSTM model
    """
    try:
        # Preprocess the text
        processed_text = preprocess_for_sentiment(request.text)
        
        # Make prediction
        result = sentiment_model.predict_sentiment(processed_text)
        
        # Add processed text to response
        result["processed_text"] = processed_text
        
        return SentimentResponse(**result)
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error during sentiment analysis: {str(e)}"
        )

@router.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "model_loaded": sentiment_model.model is not None}
