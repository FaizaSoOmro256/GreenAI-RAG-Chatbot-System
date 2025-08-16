# GreenAI: Multilingual RAG Chatbot for Sindh's Sustainable Climate Actions

A web-based intelligent chatbot that provides information about sustainable climate actions in Sindh using Retrieval Augmented Generation (RAG) technology. The application supports multiple languages including English, Urdu, and Sindhi.

## Features

- Multilingual support (English, Urdu, Sindhi)
- Beautiful and professional user interface
- Powered by Google's Gemini Flash 2.0
- Enhanced with Pinecone vector database for efficient knowledge retrieval
- Responsive web design using Streamlit
- Performance monitoring system with metrics collection
- Embedding caching system for improved response times
- Backup & restore system for metrics data preservation
- Interactive carbon footprint calculator with personalized recommendations
- Real-time environmental monitoring with sensor integration
- Comprehensive climate data visualization
- Water resource management tools
- Weather forecasting and analysis

## Prerequisites

- Python 3.x
- Streamlit
- Google Gemini Flash 2.0 API key
- Pinecone API key

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd greenai
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install PyTorch (CPU version):
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

5. Create a `.env` file with your API keys:
```
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
GEMINI_API_KEY=your_gemini_api_key
```

6. Run the application:
```bash
streamlit run app.py
```

## Project Structure

- `app.py`: Main Streamlit application
- `utils/`: Helper functions and utilities
  - `monitoring.py`: Performance monitoring and metrics tracking
  - `ui.py`: UI components and rendering functions
  - `weather_api.py`: Weather data retrieval functions
  - `forecast.py`: Weather forecast visualization
  - `district_dashboard.py`: Climate data visualization dashboard
  - `carbon_calculator.py`: Carbon footprint calculation and visualization
  - `sensor_integration.py`: Environmental sensor integration
  - `water_resources.py`: Water resource management
  - `climate_tips.py`: Climate action recommendations
- `sensors/`: Sensor system implementation
  - `base_sensor.py`: Base sensor class
  - `sensor_manager.py`: Sensor management system
  - `temperature_humidity_sensor.py`: Temperature and humidity monitoring
  - `air_quality_sensor.py`: Air quality monitoring
  - `soil_moisture_sensor.py`: Soil moisture monitoring
- `pages/`: Web application pages
  - `home.py`: Main dashboard
  - `chatbot.py`: Chat interface
  - `knowledge_base.py`: Information repository
  - `weather_dashboard.py`: Weather monitoring
  - `climate_analysis.py`: Climate data analysis
  - `carbon_calculator.py`: Carbon footprint calculator
  - `water_resources.py`: Water resource management
- `data/`: Contains knowledge base documents and multilingual data
- `config.py`: Configuration settings
- `embeddings.py`: Embedding model setup with caching functionality
- `rag_chain.py`: RAG pipeline implementation
- `pinecone_loader.py`: Vector store implementation

## Technologies Used

- Streamlit for web interface
- Sentence-transformers (multilingual-MiniLM-L12-v2) for embeddings
- Pinecone for vector storage
- Google Gemini Flash 2.0 for LLM
- LangChain for RAG pipeline
- HuggingFace Transformers for language models
- PyTorch for deep learning operations
- Pandas and NumPy for data processing
- Matplotlib, Plotly, and Seaborn for visualization
- Folium for geographical data visualization

## Future Improvements Roadmap

### Performance Optimizations
- [x] Implement caching for embeddings and frequently asked questions
- [ ] Add background batch processing for heavy computational tasks
- [ ] Optimize image assets for faster loading
- [ ] Implement lazy loading for UI components
- [x] Add backup & restore system for metrics data

### Model Enhancements
- [ ] Evaluate and test alternative embedding models for improved multilingual performance
- [ ] Add support for fine-tuning the model with local Sindh-specific data
- [ ] Implement hybrid search (combining dense and sparse retrieval)
- [ ] Add streaming responses for better user experience
- [ ] Implement content moderation for user inputs

### UI/UX Improvements
- [ ] Implement mobile-first responsive design optimizations
- [ ] Add voice input/output capability
- [ ] Develop offline mode with essential functionality
- [ ] Improve accessibility features (screen readers, keyboard navigation)
- [ ] Implement customizable UI themes
- [ ] Add guided tours for first-time users

### Data Enhancements
- [ ] Expand knowledge base with more recent climate publications
- [ ] Add real-time data integration from environmental monitoring stations
- [ ] Implement automatic data updates from trusted sources
- [ ] Add support for user-contributed knowledge (with verification)
- [ ] Implement semantic search filters by topic or domain

### Functionality Extensions
- [x] Add carbon footprint calculator with personalized recommendations
- [x] Add real-time environmental monitoring
- [ ] Add personalized recommendations based on user location
- [ ] Implement social sharing of climate insights
- [ ] Add export functionality for chat history and data visualizations
- [ ] Develop community features for collaborative climate action
- [ ] Enable scheduled reports and alerts for climate events

### Security & Infrastructure
- [ ] Implement robust error handling and logging
- [ ] Add comprehensive unit and integration tests
- [ ] Set up CI/CD pipeline for automated testing and deployment
- [ ] Implement user authentication for personalized experiences
- [ ] Optimize Docker container for production deployment
- [ ] Add rate limiting and abuse prevention mechanisms

### Documentation
- [ ] Create comprehensive API documentation
- [ ] Add inline code documentation
- [ ] Create user manual and FAQ section
- [ ] Document the knowledge base sources and update process
- [ ] Provide developer onboarding guide 