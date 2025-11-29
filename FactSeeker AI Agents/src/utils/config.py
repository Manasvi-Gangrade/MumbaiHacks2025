import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # API Keys (All FREE!)
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # Database
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
    DB_NAME = os.getenv("DB_NAME", "factseeker_db")

    # Models (Free!)
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "google/flan-t5-large")

    @staticmethod
    def validate_keys():
        """Check for missing critical keys."""
        missing = []
        if not Config.HUGGINGFACE_TOKEN:
            missing.append("HUGGINGFACE_TOKEN (Get free at https://huggingface.co/settings/tokens)")
        if missing:
            print(f" Warning: Missing API Keys: {', '.join(missing)}")
            print("The system will run in MOCK mode without these keys.")

# Auto-validate on import
Config.validate_keys()
