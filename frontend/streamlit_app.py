import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .result-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .positive {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .negative {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎭 Sentiment Analysis</h1>', unsafe_allow_html=True)
st.markdown("### Analyze the sentiment of your text using our LSTM model")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    backend_url = st.text_input(
        "Backend URL",
        value="http://localhost:8000",
        help="URL of the FastAPI backend"
    )
    
    st.markdown("---")
    st.markdown("### 📊 Model Info")
    st.markdown("- **Model**: LSTM Neural Network")
    st.markdown("- **Dataset**: IMDB Movie Reviews")
    st.markdown("- **Accuracy**: ~88.6%")
    
    st.markdown("---")
    st.markdown("### 🔗 API Endpoints")
    st.markdown(f"- **Health**: `{backend_url}/health`")
    st.markdown(f"- **Predict**: `{backend_url}/api/v1/predict`")

# Movie selection (move this above columns)
st.subheader("🎬 Select a Movie")
movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "Inception",
    "Fight Club",
    "Interstellar",
    "The Matrix",
    "Parasite"
]
selected_movie = st.selectbox("Choose a movie to review:", movies)
st.markdown(f"**Selected Movie:** {selected_movie}")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Write Your Review")
    
    # Text input
    user_text = st.text_area(
        f"Write your review for '{selected_movie}':",
        height=200,
        placeholder=f"Enter your review for {selected_movie} here...",
        help="Enter your review for the selected movie."
    )
    
    # Analyze button
    if st.button("🔍 Analyze Sentiment", type="primary", use_container_width=True):
        if user_text.strip():
            with st.spinner("🤖 Analyzing sentiment..."):
                try:
                    # Make API request
                    response = requests.post(
                        f"{backend_url}/api/v1/predict",
                        json={"text": user_text},
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        # Display results
                        st.success("✅ Analysis Complete!")
                        
                        # Sentiment result with color coding
                        sentiment = result.get("sentiment", "unknown")
                        confidence = result.get("confidence", 0)
                        probability = result.get("probability", 0)
                        processed_text = result.get("processed_text", "")
                        
                        # Color-coded sentiment display
                        if sentiment == "positive":
                            st.markdown(f"""
                            <div class="result-box positive">
                                <h3>😊 Positive Sentiment</h3>
                                <p>Confidence: {confidence:.2%}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div class="result-box negative">
                                <h3>😞 Negative Sentiment</h3>
                                <p>Confidence: {confidence:.2%}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Metrics
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Sentiment", sentiment.title())
                        with col2:
                            st.metric("Confidence", f"{confidence:.2%}")
                        with col3:
                            st.metric("Probability", f"{probability:.2%}")
                        
                        # Processed text
                        with st.expander("🔧 Processed Text"):
                            st.text(processed_text)
                        
                        # Raw response
                        with st.expander("📋 Raw API Response"):
                            st.json(result)
                            
                    else:
                        st.error(f"❌ API Error: {response.status_code}")
                        st.text(response.text)
                        
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend. Please make sure the FastAPI server is running.")
                except requests.exceptions.Timeout:
                    st.error("⏰ Request timed out. Please try again.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter some text to analyze.")

# Remove example texts and add movie selection
if hasattr(st.session_state, 'example_text'):
    st.session_state.user_text = st.session_state.example_text
    del st.session_state.example_text
