# FactSeeker: Autonomous Misinformation Detection System 🕵️

**Shree ganeshay namah, Bhagwaan ji please saath dena, I'll try my best, bas ab aage aapki iccha** 🙏

> **NEW**: Now using 100% FREE APIs! No paid services required.

## Overview
FactSeeker is an advanced, autonomous, multi-agent AI system designed to detect and verify misinformation in real-time across social media platforms. Built with free-tier LLMs, RAG, and multimodal analysis.

## Features
- 🤖 **Multi-Agent Architecture**: Autonomous agents for ingestion, detection, verification, and alerting
- 🔍 **Misinformation Detection**: Heuristic and ML-based content analysis
- 📚 **RAG-based Verification**: Fact-checking against trusted knowledge bases using FAISS
- 🧠 **Free LLM Integration**: HuggingFace Inference API for context-aware verification
- 📊 **Real-time Dashboard**: Streamlit-based monitoring interface
- 📱 **Telegram Alerts**: Instant notifications for flagged content
- 💰 **100% Free Tier**: All APIs and services are free!

## Setup

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration (All FREE!)
Copy `.env.example` to `.env` and add your **FREE** API keys:

```bash
cp .env.example .env
```

**Required API Keys** (All Free!):
- `HUGGINGFACE_TOKEN` - Get free at https://huggingface.co/settings/tokens (20k requests/month)

**Optional API Keys** (All Free!):
- `NEWS_API_KEY` - Get free at https://newsapi.org (100 requests/day)
- `TELEGRAM_BOT_TOKEN` - Get free from @BotFather on Telegram
- `REDDIT_CLIENT_ID/SECRET` - Get free at https://www.reddit.com/prefs/apps
- `MONGODB_URI` - Get free at https://mongodb.com/atlas (512MB)

See [FREE_API_REQUIREMENTS.md](FREE_API_REQUIREMENTS.md) for detailed instructions.

### 3. Running the System

#### Run the Dashboard
```bash
streamlit run app.py
```

#### Run Agent Manager (CLI)
```bash
python -m src.agents.manager
```

#### Test Individual Components
```bash
# Test RAG retriever
python -m src.rag.retriever

# Test detector
python -m src.rag.detector

# Test LLM verifier (HuggingFace)
python -m src.rag.llm_verifier
```

## How It Works

### Autonomous Workflow
1. **Ingestion Agent**: Monitors social media and news sources for new content
2. **Detection Agent**: Analyzes content using heuristics and ML models
3. **Verification Agent**: Fact-checks flagged content using RAG + Free LLM
4. **Alert Agent**: Sends notifications for confirmed misinformation

### Technology Stack (100% Free!)
- **Backend**: Python, FastAPI
- **AI/ML**: Transformers, Sentence-Transformers, LangChain
- **LLM**: HuggingFace Inference API (google/flan-t5-large) - FREE
- **Embeddings**: Sentence-Transformers (local) - FREE
- **Vector DB**: FAISS (local) - FREE
- **Frontend**: Streamlit - FREE
- **Notifications**: Telegram Bot API - FREE

## Project Structure
```
FactSeeker/
├── src/
│   ├── agents/
│   │   └── manager.py          # Agent orchestration
│   ├── rag/
│   │   ├── detector.py         # Misinformation detection
│   │   ├── retriever.py        # RAG retrieval with FAISS
│   │   └── llm_verifier.py     # HuggingFace LLM verification
│   └── utils/
│       ├── config.py           # Configuration management
│       ├── database.py         # MongoDB connection
│       ├── ingestion.py        # Data ingestion
│       ├── preprocessing.py    # Text embeddings
│       ├── multimodal.py       # Image processing
│       ├── telegram_bot.py     # Telegram integration
│       └── explainability.py   # Decision logging
├── app.py                      # Streamlit dashboard
├── requirements.txt            # Dependencies
├── .env.example               # Environment template
├── FREE_API_REQUIREMENTS.md   # API key guide
└── README.md                  # This file
```

## Current Status
✅ Environment Setup
✅ Data Ingestion Layer
✅ Preprocessing & Multimodal Analysis
✅ Detection & Verification Layer (with FREE HuggingFace LLM)
✅ Agentic Decision Layer
✅ Notification & Dashboard Layer
✅ Explainability & Feedback
✅ **Migrated to 100% Free APIs**

## Next Steps
- [ ] Add your HuggingFace token to `.env`
- [ ] Add more trusted sources to RAG knowledge base
- [ ] Fine-tune detection models
- [ ] Deploy to production

## License
MIT License

## Acknowledgments
Built with dedication and divine blessings. 🙏
Powered by free and open-source technologies.