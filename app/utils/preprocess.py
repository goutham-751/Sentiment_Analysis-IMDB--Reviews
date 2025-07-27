import re
import string

def clean_text(text):
    """
    Clean and normalize text for sentiment analysis
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove punctuation except for important ones
    text = re.sub(r'[^\w\s!?.,]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def normalize_text(text):
    """
    Additional normalization for better model performance
    """
    # Replace common contractions
    contractions = {
        "n't": " not",
        "'ll": " will",
        "'re": " are",
        "'ve": " have",
        "'m": " am",
        "'d": " would",
        "'s": " is"  # Note: this is simplified
    }
    
    for contraction, expansion in contractions.items():
        text = text.replace(contraction, expansion)
    
    return text

def preprocess_for_sentiment(text):
    """
    Complete preprocessing pipeline for sentiment analysis
    """
    text = clean_text(text)
    text = normalize_text(text)
    return text
