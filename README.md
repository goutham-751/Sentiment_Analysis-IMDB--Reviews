# 🎭 Sentiment Analysis App

A modern web application for analyzing sentiment in movie reviews using an LSTM neural network. Built with FastAPI backend and Streamlit frontend.

## 🌟 Features

- **LSTM Neural Network**: Trained on IMDB movie reviews dataset with ~88.6% accuracy
- **Real-time Analysis**: Instant sentiment predictions with confidence scores
- **Movie Review Interface**: Select from popular movies and write your reviews
- **Beautiful UI**: Modern, responsive design with color-coded results
- **RESTful API**: FastAPI backend with automatic documentation
- **Text Preprocessing**: Advanced text cleaning and normalization

## 🏗️ Architecture

```
sentiment_app/
├── app/                    # FastAPI Backend
│   ├── main.py            # FastAPI application
│   ├── models/
│   │   └── model_loader.py # LSTM model wrapper
│   ├── routes/
│   │   └── predict.py     # Prediction endpoints
│   ├── schemas/
│   │   └── request_schema.py # API schemas
│   └── utils/
│       └── preprocess.py  # Text preprocessing
├── frontend/
│   └── streamlit_app.py   # Streamlit UI
├── Notebooks/
│   └── Sentiment_Analysis_IMDB_Reviews.ipynb # ML model notebook
├── requirements.txt       # Python dependencies
├── run.sh                # Startup script
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sentiment_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend**
   ```bash
   python -m uvicorn app.main:app --reload
   ```
   The API will be available at: http://localhost:8000

4. **Start the frontend** (in a new terminal)
   ```bash
   python -m streamlit run frontend/streamlit_app.py
   ```
   The UI will be available at: http://localhost:8501

### Alternative: Using the startup script (Linux/Mac)
```bash
chmod +x run.sh
./run.sh
```

## 📖 Usage

### Web Interface

1. **Select a Movie**: Choose from the dropdown list of popular movies
2. **Write Your Review**: Enter your review in the text area
3. **Analyze**: Click "Analyze Sentiment" to get results
4. **View Results**: See sentiment prediction, confidence score, and processed text

### API Usage

#### Predict Sentiment
```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "This movie was absolutely fantastic!"}'
```

**Response:**
```json
{
  "sentiment": "positive",
  "confidence": 0.95,
  "probability": 0.95,
  "processed_text": "this movie was absolutely fantastic"
}
```

#### Health Check
```bash
curl http://localhost:8000/health
```

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/health` | GET | Health check |
| `/api/v1/predict` | POST | Sentiment analysis |
| `/docs` | GET | Interactive API documentation |

## 🤖 Model Details

### Architecture
- **Model Type**: LSTM (Long Short-Term Memory) Neural Network
- **Input**: Text sequences (max length: 200 tokens)
- **Output**: Binary classification (Positive/Negative)
- **Accuracy**: ~88.6% on test set

### Preprocessing
- Text cleaning (HTML tags, URLs removal)
- Tokenization (5000 most common words)
- Sequence padding (maxlen=200)
- Contraction expansion

### Training Data
- **Dataset**: IMDB Movie Reviews (50,000 reviews)
- **Split**: 80% training, 20% testing
- **Labels**: 1 (Positive), 0 (Negative)

## 🛠️ Development

### Project Structure
- **Backend**: FastAPI with modular architecture
- **Frontend**: Streamlit with custom CSS styling
- **Model**: TensorFlow/Keras LSTM implementation
- **API**: RESTful design with Pydantic validation

### Adding New Movies
Edit the `movies` list in `frontend/streamlit_app.py`:
```python
movies = [
    "Your Movie Title 1",
    "Your Movie Title 2",
    # ... add more movies
]
```

### Customizing the Model
1. Train your model using the notebook in `Notebooks/`
2. Save the model: `model.save('app/models/sentiment_model.h5')`
3. Save the tokenizer: `pickle.dump(tokenizer, open('app/models/tokenizer.pkl', 'wb'))`
4. Update `model_loader.py` to load your saved model

## 📊 Performance

- **Model Accuracy**: 88.6%
- **Inference Time**: ~100-200ms per prediction
- **API Response Time**: <500ms
- **Concurrent Users**: Supports multiple simultaneous requests

## 🔍 Troubleshooting

### Common Issues

1. **"uvicorn not recognized"**
   ```bash
   pip install uvicorn
   python -m uvicorn app.main:app --reload
   ```

2. **"streamlit not recognized"**
   ```bash
   pip install streamlit
   python -m streamlit run frontend/streamlit_app.py
   ```

3. **Model not loading**
   - Check if `app/models/` directory exists
   - Ensure TensorFlow is installed: `pip install tensorflow`

4. **API connection errors**
   - Verify backend is running on port 8000
   - Check CORS settings in `app/main.py`

### Logs
- Backend logs: Check terminal running uvicorn
- Frontend logs: Check terminal running streamlit
- Model logs: Check `app/main.py` logging configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- IMDB dataset for training data
- TensorFlow/Keras for the neural network framework
- FastAPI for the backend framework
- Streamlit for the frontend framework

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the API documentation at http://localhost:8000/docs
3. Open an issue on GitHub

---

**Happy Sentiment Analysis! 🎭✨**
