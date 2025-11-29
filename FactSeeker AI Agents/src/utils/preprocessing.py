from sentence_transformers import SentenceTransformer
import re

class TextPreprocessor:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print(f"Loading Embedding Model: {model_name}...")
        self.model = SentenceTransformer(model_name)

    def clean_text(self, text: str) -> str:
        """
        Basic text cleaning: remove URLs, special chars, etc.
        """
        text = re.sub(r'http\S+', '', text) # Remove URLs
        text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
        text = text.lower().strip()
        return text

    def get_embedding(self, text: str):
        """
        Generate vector embedding for text.
        """
        cleaned_text = self.clean_text(text)
        embedding = self.model.encode(cleaned_text)
        return embedding

if __name__ == "__main__":
    preprocessor = TextPreprocessor()
    sample_text = "Check out this fake news! http://fake.com #scam"
    print(f"Original: {sample_text}")
    print(f"Cleaned: {preprocessor.clean_text(sample_text)}")
    emb = preprocessor.get_embedding(sample_text)
    print(f"Embedding Shape: {emb.shape}")
