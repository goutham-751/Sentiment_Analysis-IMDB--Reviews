from pydantic import BaseModel, Field
from typing import Optional

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=10000, description="Text to analyze for sentiment")
    
class SentimentResponse(BaseModel):
    sentiment: str = Field(..., description="Predicted sentiment (positive/negative)")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score of the prediction")
    probability: float = Field(..., ge=0.0, le=1.0, description="Raw probability score")
    processed_text: str = Field(..., description="Preprocessed text that was analyzed")
    
class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Additional error details")
