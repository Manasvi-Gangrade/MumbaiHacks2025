"""
Misinformation Detector Module

This module contains the logic for detecting potential misinformation in text content.
Currently uses a heuristic-based approach with keyword matching.

In a production system, this would be replaced with:
- Fine-tuned BERT/RoBERTa model
- Multi-modal transformers for image/video analysis
- Ensemble of multiple detection models

Detection Strategy:
1. Check for suspicious keywords (fake, scam, conspiracy)
2. Check for unverified health claims (cure, treatment, prevents)
3. Check for extreme/absolute claims (100%, guaranteed, always)
4. Assign confidence score based on matches
"""

import random

class MisinformationDetector:
    def __init__(self):
        print("Initializing Misinformation Detector...")
        # In a real system, we would load a fine-tuned BERT/RoBERTa model here
        # Example: self.model = AutoModelForSequenceClassification.from_pretrained("bert-misinformation")
        
    def detect(self, text: str, image_embedding=None):
        """
        Classify content as potential misinformation or likely true.
        
        Args:
            text (str): The content to analyze
            image_embedding (optional): Vector embedding of associated image
            
        Returns:
            dict: Contains label, confidence score, and flagged status
                - label: "Potential Misinformation" or "Likely True"
                - confidence: float between 0 and 1
                - flagged: boolean indicating if content should be verified
        """
        
        # Keywords that indicate potential misinformation
        # These are common in conspiracy theories and fake news
        suspicious_keywords = ["fake", "scam", "conspiracy", "secret", "staged"]
        
        # Medical/health claims that need verification
        # Unverified health advice is a major source of misinformation
        health_claims = ["cure", "cures", "treatment", "heal", "remedy", "prevent", "prevents"]
        
        # Extreme/absolute claims are often exaggerated or false
        # Real information typically includes nuance and uncertainty
        extreme_claims = ["all diseases", "all illness", "100%", "guaranteed", "never", "always"]
        
        # Convert text to lowercase for case-insensitive matching
        text_lower = text.lower()
        
        # Default confidence score (low suspicion)
        score = 0.1
        
        # Check for suspicious keywords
        if any(k in text_lower for k in suspicious_keywords):
            # High confidence of misinformation
            score = 0.9
            
        # Check for unverified health claims
        elif any(h in text_lower for h in health_claims):
            # Health claims should be verified
            score = 0.85
            
        # Check for extreme claims
        elif any(e in text_lower for e in extreme_claims):
            # Extreme claims are often exaggerated
            score = 0.8
        else:
            # Random noise for demo purposes
            # In production, this would be the model's prediction
            score = random.uniform(0.1, 0.4)
        
        # Determine label based on confidence threshold
        # Threshold is 0.7 - anything above is flagged
        label = "Potential Misinformation" if score > 0.7 else "Likely True"
        
        return {
            "label": label,
            "confidence": score,
            "flagged": score > 0.7  # Flag for verification if confidence > 70%
        }

# Test the detector if run directly
if __name__ == "__main__":
    detector = MisinformationDetector()
    
    # Test with a conspiracy theory
    sample = "This is a secret conspiracy about the moon."
    result = detector.detect(sample)
    print(f"Input: {sample}")
    print(f"Result: {result}")
