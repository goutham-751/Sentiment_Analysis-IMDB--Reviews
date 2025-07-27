import pickle
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os

class SentimentModel:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.maxlen = 200
        self.num_words = 5000
        
    def create_model(self):
        """Create the LSTM model architecture"""
        model = Sequential()
        model.add(Embedding(input_dim=self.num_words, output_dim=self.num_words))
        model.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
    
    def load_or_create_tokenizer(self, training_texts=None):
        """Load existing tokenizer or create new one"""
        tokenizer_path = "app/models/tokenizer.pkl"
        
        if os.path.exists(tokenizer_path):
            with open(tokenizer_path, 'rb') as f:
                self.tokenizer = pickle.load(f)
        else:
            # Create new tokenizer with some basic vocabulary for demo
            self.tokenizer = Tokenizer(num_words=self.num_words)
            
            # Add some basic vocabulary for demo purposes
            basic_texts = [
                "this is a great movie",
                "terrible film",
                "amazing performance",
                "bad acting",
                "excellent story",
                "poor plot",
                "wonderful cinematography",
                "disappointing ending",
                "fantastic direction",
                "mediocre script"
            ]
            self.tokenizer.fit_on_texts(basic_texts)
            
            # Save tokenizer
            os.makedirs(os.path.dirname(tokenizer_path), exist_ok=True)
            with open(tokenizer_path, 'wb') as f:
                pickle.dump(self.tokenizer, f)
    
    def predict_sentiment(self, text):
        """Predict sentiment for given text"""
        if self.tokenizer is None:
            raise ValueError("Tokenizer not loaded. Please load the model first.")
        
        # Preprocess text
        sequence = self.tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=self.maxlen)
        
        # Make prediction
        prediction = self.model.predict(padded_sequence, verbose=0)
        probability = prediction[0][0]
        
        # Determine sentiment
        sentiment = "negative" if probability > 0.5 else "positive"
        confidence = probability if sentiment == "negative" else 1 - probability
        
        return {
            "sentiment": sentiment,
            "confidence": float(confidence),
            "probability": float(probability)
        }

# Global model instance
sentiment_model = SentimentModel()
