# 🌱 Green AI: Multilingual RAG Chatbot for Sustainable Climate Actions in Sindh

[![Python](https://img.shields.io/badge/Python-3.10+-blue)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)](https://greenai-rag-chatbot-system-32xlcpdknofq7uasauq76v.streamlit.app/)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%202.0%20Flash-orange)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20Database-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

Green AI is a multilingual Retrieval-Augmented Generation (RAG) chatbot designed to support sustainable climate awareness and environmental decision-making in Sindh, Pakistan. The platform combines Google Gemini 2.0 Flash, LangChain, and Pinecone to deliver accurate, context-aware responses from a curated climate knowledge base while providing interactive environmental analysis tools.

---
## Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [System Architecture](#system-architecture)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [RAG Pipeline](#-retrieval-augmented-generation-rag-pipeline)
- [Core Modules](#-core-modules)
- [Performance Optimizations](#-performance-optimizations)
- [Multilingual Support](#-multilingual-support)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Application](#-running-the-application)
- [Project Modules](#-project-modules)
- [Technology Stack](#-technology-stack)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)
- [Author](#-author)

# 📖 Overview

Climate change has become one of the most significant challenges affecting communities worldwide. Access to reliable environmental information remains limited, particularly in regional languages.

Green AI addresses this challenge by providing an intelligent multilingual assistant capable of answering climate-related questions using Retrieval-Augmented Generation (RAG). Instead of relying solely on a large language model, the system retrieves relevant information from a curated climate knowledge base before generating responses, improving factual accuracy and reducing hallucinations.

The application is specifically designed to support users in Sindh by providing climate knowledge in **English, Urdu, and Sindhi**, making environmental information accessible to students, researchers, NGOs, policymakers, and local communities.

Beyond conversational AI, Green AI integrates multiple sustainability-focused modules, including a carbon footprint calculator, weather monitoring dashboard, climate analytics, and water resource management tools.

# 🚀 Live Demo

### 🌐 Streamlit Application

https://greenai-rag-chatbot-system-32xlcpdknofq7uasauq76v.streamlit.app/

---
---

# ✨ Features

## 🤖 AI Chatbot

- Multilingual conversational AI
- English, Urdu, and Sindhi support
- Context-aware responses using RAG
- Google Gemini 2.0 Flash integration
- Pinecone semantic vector search
- Fast and relevant knowledge retrieval

---

## 🌍 Climate Intelligence

- Carbon footprint calculator
- Personalized sustainability recommendations
- Weather dashboard
- Climate data visualization
- Environmental monitoring
- Water resource management

---

## 📊 Analytics

- Performance monitoring
- Embedding caching
- Knowledge retrieval metrics
- Climate statistics dashboard
- Interactive visualizations

---

## 💻 User Experience

- Responsive Streamlit interface
- Modern and intuitive dashboard
- Interactive charts
- Easy navigation
- Fast response generation

---

# 🏗️ System Architecture

```
                     User
                       │
                       ▼
              Streamlit Frontend
                       │
                       ▼
                 FastAPI Backend
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
 Google Gemini 2.0 Flash      Pinecone Database
          │                         │
          └────────────┬────────────┘
                       ▼
              LangChain RAG Pipeline
                       │
                       ▼
            Context-Aware AI Response
```

---

# 📂 Project Structure

```
GreenAI/
│
├── app.py
├── config.py
├── embeddings.py
├── rag_chain.py
├── pinecone_loader.py
├── requirements.txt
├── server.py
│
├── data/
│
├── pages/
│   ├── home.py
│   ├── chatbot.py
│   ├── knowledge_base.py
│   ├── weather_dashboard.py
│   ├── climate_analysis.py
│   ├── carbon_calculator.py
│   └── water_resources.py
│
├── utils/
│   ├── ui.py
│   ├── monitoring.py
│   ├── weather_api.py
│   ├── district_dashboard.py
│   ├── forecast.py
│   ├── carbon_calculator.py
│   ├── climate_tips.py
│   ├── sensor_integration.py
│   └── water_resources.py
│
├── sensors/
│
└── README.md
```

---

# 🎯 Objectives

- Improve access to climate information in regional languages.
- Support sustainable decision-making using AI.
- Provide accurate answers through Retrieval-Augmented Generation.
- Promote environmental awareness among communities in Sindh.
- Offer practical sustainability tools such as carbon footprint estimation and weather insights.

---

# 👥 Target Users

- Students
- Researchers
- Environmental NGOs
- Government organizations
- Farmers
- Climate scientists
- Educational institutions
- General public

# 📊 Dataset

Green AI uses a curated climate knowledge base containing environmental reports, climate policies, sustainability guidelines, weather information, water resource data, and region-specific documents related to Sindh.

The knowledge base is converted into vector embeddings and stored in Pinecone, allowing the Retrieval-Augmented Generation (RAG) pipeline to retrieve the most relevant context before generating responses.

## Knowledge Sources

- Climate reports
- Environmental policies
- Sustainable development documents
- Water resource information
- Agricultural guidelines
- Weather and climate data
- Government publications
- Educational materials

---

# 🧠 Retrieval-Augmented Generation (RAG) Pipeline

Unlike a traditional chatbot that relies only on a Large Language Model, Green AI first retrieves relevant knowledge from its vector database before generating a response.

```
User Question
      │
      ▼
Embedding Generation
      │
      ▼
Pinecone Vector Search
      │
      ▼
Relevant Climate Documents
      │
      ▼
LangChain Prompt Construction
      │
      ▼
Google Gemini 2.0 Flash
      │
      ▼
Final AI Response
```

This workflow improves factual accuracy, reduces hallucinations, and provides responses grounded in the project's climate knowledge base.

---

# ⚙️ Core Modules

## 🤖 AI Climate Chatbot

The chatbot enables users to ask climate-related questions in multiple languages. It retrieves relevant information using semantic search and generates responses using Google Gemini.

### Features

- Multilingual conversations
- Context-aware responses
- Conversation history
- Climate knowledge retrieval
- Quick response generation

---

## 🌍 Carbon Footprint Calculator

The Carbon Footprint Calculator estimates environmental impact based on user activities and provides recommendations to reduce emissions.

### Features

- Carbon emission estimation
- Personalized recommendations
- Tree equivalence calculation
- Sustainability suggestions
- Environmental impact visualization

---

## 🌦️ Weather Dashboard

Displays weather information and environmental conditions through an interactive dashboard.

### Features

- Current weather
- Weather forecasts
- Climate indicators
- Interactive charts
- Environmental monitoring

---

## 💧 Water Resource Management

Provides information related to water availability, conservation, and sustainable management.

### Features

- Water resource information
- Conservation recommendations
- Regional water insights
- Sustainable usage guidance

---

## 📈 Climate Analytics

Visualizes environmental trends and climate-related information through interactive charts.

### Features

- Climate statistics
- Environmental trends
- Interactive graphs
- Regional analysis
- Data visualization

---

# ⚡ Performance Optimizations

The application includes several optimizations to improve performance and user experience.

## Embedding Cache

Frequently accessed embeddings are cached to reduce repeated computations and improve response times.

## Performance Monitoring

The system tracks application performance and collects metrics for monitoring and future optimization.

## Backup & Restore

Application metrics can be backed up and restored to preserve monitoring data.

---

# 🌐 Multilingual Support

Green AI is designed to make climate information accessible to a wider audience by supporting multiple languages.

Supported Languages:

- English
- Urdu
- Sindhi

This enables users to interact with the system using their preferred language while accessing the same climate knowledge base.

---

# 🔍 Key Technologies

## Artificial Intelligence

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Natural Language Processing (NLP)

## Machine Learning

- Sentence Transformers
- Embedding Models
- Vector Similarity Search

## Backend Technologies

- FastAPI
- LangChain
- Pinecone
- Google Gemini API

## Frontend Technologies

- Streamlit
- HTML
- CSS
- JavaScript

---

# 📚 Project Highlights

- AI-powered climate assistant
- Region-specific climate knowledge
- Multilingual interface
- Semantic document retrieval
- Interactive environmental tools
- Responsive web application
- Real-time analytics
- Modern dashboard
- Educational platform
- Sustainable development support

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/FaizaSoOmro256/GreenAI-RAG-Chatbot.git

cd GreenAI-RAG-Chatbot
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

If PyTorch is not installed:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

# 🔑 Configuration

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_google_gemini_api_key

PINECONE_API_KEY=your_pinecone_api_key

PINECONE_ENVIRONMENT=your_pinecone_environment
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Default URL:

```
http://localhost:8501
```

---

# 📂 Project Modules

## Main Application

| File | Description |
|-------|-------------|
| app.py | Streamlit application entry point |
| config.py | Application configuration |
| embeddings.py | Embedding generation |
| rag_chain.py | RAG pipeline |
| pinecone_loader.py | Vector database loader |
| server.py | FastAPI backend |

---

## Pages

| Page | Purpose |
|-------|---------|
| Home | Dashboard |
| Chatbot | AI Climate Assistant |
| Knowledge Base | Climate documents |
| Weather Dashboard | Weather insights |
| Climate Analysis | Data visualization |
| Carbon Calculator | Carbon estimation |
| Water Resources | Water management |

---

## Utilities

- Monitoring
- Weather API
- Forecasting
- UI Components
- Climate Tips
- Carbon Calculator
- Sensor Integration
- Water Resources

---

# 💻 Technology Stack

## Artificial Intelligence

- Google Gemini 2.0 Flash
- LangChain
- Retrieval-Augmented Generation (RAG)

## Vector Database

- Pinecone

## Embedding Model

- Sentence Transformers
- multilingual-MiniLM-L12-v2

## Machine Learning

- Hugging Face Transformers
- PyTorch

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit
- HTML
- CSS
- JavaScript

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly
- Matplotlib
- Seaborn
- Folium

---

# 📈 Future Roadmap

## AI Improvements

- Hybrid Search
- Streaming Responses
- Voice Interaction
- Fine-tuned Local Models
- Explainable AI

---

## Performance

- Lazy Loading
- Background Processing
- Faster Embedding Retrieval
- Response Optimization

---

## User Experience

- Mobile Optimization
- Offline Support
- Accessibility Improvements
- Additional Themes
- Personalized Dashboard

---

## Infrastructure

- Docker Support
- CI/CD Pipeline
- Cloud Deployment
- User Authentication
- API Rate Limiting

---

## Data Expansion

- Additional Climate Datasets
- Live Sensor Integration
- Government Open Data
- Automatic Knowledge Base Updates

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve Green AI:

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📈 Future Improvements

Green AI is designed with scalability in mind. Future enhancements include:

## 🎨 User Interface & Experience

- Redesign the interface with a more modern and visually engaging user experience.
- Add advanced animations, interactive dashboards, and improved accessibility.
- Enhance mobile responsiveness for seamless use across all devices.
- Introduce customizable themes, including light and dark modes.

## 🌍 Language Expansion

- Extend multilingual support beyond English, Urdu, and Sindhi.
- Add languages such as Arabic, Hindi, Chinese, French, Spanish, and Turkish.
- Improve translation quality for low-resource languages.

## 🤖 AI Model Enhancements

- Support multiple Large Language Models (LLMs), including:
  - Google Gemini
  - OpenAI GPT
  - Claude
  - Llama
  - Mistral
- Allow users to switch between AI models based on their capabilities.
- Improve retrieval accuracy using hybrid search and reranking techniques.

## 🌎 Global Expansion

- Expand the knowledge base to include climate and sustainability information from multiple countries.
- Support country-specific environmental policies, weather data, and climate initiatives.
- Provide localized recommendations based on the user's region.

## 📊 Advanced Analytics

- Add AI-powered climate trend prediction.
- Generate personalized sustainability reports.
- Enable downloadable environmental impact reports.
- Integrate real-time environmental monitoring data.

## 🔒 Infrastructure & Deployment

- Containerize the application using Docker.
- Implement CI/CD pipelines for automated testing and deployment.
- Add secure user authentication and role-based access control.
- Deploy scalable cloud infrastructure for production use.

## 🌱 Community Features

- Enable user feedback and community contributions.
- Allow organizations to upload their own climate knowledge bases.
- Support collaborative research and knowledge sharing.

# 📜 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgements

Special thanks to the open-source technologies that made this project possible.

- Google Gemini
- LangChain
- Pinecone
- Hugging Face
- Sentence Transformers
- Streamlit
- FastAPI
- Plotly
- Pandas
- NumPy

---

# 👩‍💻 Author

**Faiza Soomro**

AI & Machine Learning Enthusiast

### GitHub

https://github.com/FaizaSoOmro256

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps improve the project and encourages future development.

---

## 📬 Contact

For suggestions, collaborations, or feedback, feel free to connect through GitHub.

---

## 🌍 Vision

Green AI aims to make climate knowledge accessible through Artificial Intelligence by combining multilingual support, Retrieval-Augmented Generation, and interactive sustainability tools to empower communities, researchers, and policymakers in making informed environmental decisions.
