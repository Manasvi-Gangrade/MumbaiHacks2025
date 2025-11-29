FactSeeker : Detect, Verify, Alert
<img width="1361" height="907" alt="Screenshot 2025-10-19 232629" src="https://github.com/user-attachments/assets/768516e5-1f84-4baf-9eaa-4ecf85572de9" />

Demonstration Video : https://youtu.be/tI_SYASY7Wk

FactSeeker is an autonomous, multi-agent AI system designed to detect, verify, and mitigate misinformation in real-time. Leveraging Large Language Models (LLMs), Generative AI, Retrieval-Augmented Generation (RAG), and multimodal analysis, FactSeeker scans multiple platforms—text, images, video, and audio—to identify false content and verify it against trusted, verified sources.

Overview
FactSeeker is built to proactively protect public trust and safety by delivering verified information before misinformation spreads. It integrates a working dashboard, autonomous alerting system, and an explainability layer that shows the reasoning behind flagged content.
The system is scalable and modular, suitable for health crises, political events, or public safety situations where misinformation can have severe consequences.

Features
1. Multi-Agent Architecture: Detection, Verification, and Alert Agents work autonomously.
2. Multimodal Analysis: Processes text, images, videos, and audio.
3. LLM Integration: Context-aware understanding and summarization.
4. RAG Fact-Checking: Retrieves verified information from trusted sources.
5. Real-Time Alerts: Telegram, WhatsApp, and web dashboard notifications.
6. Explainability Layer: Provides reasoning behind each flagged item.
7. Impact Scoring: Prioritizes high-risk misinformation based on virality and severity.
8. User Feedback Loop: Enables continuous model improvement.

Architecture
FactSeeker follows a modular, multi-layer architecture:

1. Data Ingestion Layer: Streams data from social media, news, and messaging platforms.
2. Preprocessing & Embeddings Layer: Cleans data and generates embeddings for text, images, and audio/video.
3. Detection Layer: Multimodal AI classifies content as true or potential misinformation.
4. Fact-Checking Layer: RAG + LLM verifies flagged content using trusted sources.
5. Agentic Decision Layer: Multi-agent system calculates Impact Score and triggers alerts.
6. Dashboard & Notification Layer: Displays flagged content and sends real-time alerts.
7. Explainability & Feedback Layer: Provides reasoning and incorporates user feedback for model fine-tuning.

Implementation

1. Backend & AI Orchestration: Python, FastAPI/Flask, LangChain/AutoGPT
2. Data Storage: MongoDB (NoSQL), FAISS/Pinecone (Vector DB)
3. NLP Models: BERT, RoBERTa, GPT-4.5, LLaMA, Sentence-BERT
4. Multimodal Models: Vision Transformer, CNN, Whisper (audio)
5. Frontend/Dashboard: Streamlit / React.js, D3.js for visualizations
6. Notifications: Telegram Bot API, WhatsApp Business API, Web Push Notifications
7. Explainability: SHAP, LIME, LLM-generated rationale

Workflow:
1. Stream content from APIs and messaging platforms.
2. Preprocess and generate embeddings for all modalities.
3. Detect potential misinformation using AI models.
4. Verify flagged content with RAG + LLM.
5. Prioritize alerts based on Impact Score.
6. Notify users and update dashboard autonomously.
7. Provide reasoning and incorporate user feedback.

Installation

1. Clone the repository:
git clone https://github.com/yourusername/MumbaiHacks2025.git
cd MumbaiHacks2025

2. Create virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Set API keys for social media/news integrations in .env file.

Usage
1. Start backend server:
uvicorn backend.main:app --reload

2. Launch dashboard:
streamlit run frontend/dashboard.py

Alerts will be sent automatically via Telegram/WhatsApp.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS

