"""
LLM Verifier Module

This module uses HuggingFace's free Inference API to verify claims against evidence.
It takes a claim and retrieved evidence, then uses an LLM to determine if the claim is true or false.

Model Used: google/flan-t5-large (free tier)
API: HuggingFace Inference API (20,000 requests/month free)

Workflow:
1. Construct a prompt with the claim and evidence
2. Send to HuggingFace LLM for analysis
3. Parse the response to extract verdict and explanation
4. Return structured result
"""

from huggingface_hub import InferenceClient
from src.utils.config import Config

class LLMVerifier:
    def __init__(self):
        print("Initializing LLM Verifier with HuggingFace (FREE)...")
        self.client = None
        self.model = Config.HUGGINGFACE_MODEL
        
        # Try to initialize HuggingFace client if token is available
        if Config.HUGGINGFACE_TOKEN and "your_" not in Config.HUGGINGFACE_TOKEN:
            try:
                # Create inference client with user's token
                self.client = InferenceClient(token=Config.HUGGINGFACE_TOKEN)
                print(f"Connected to HuggingFace with model: {self.model}")
            except Exception as e:
                print(f"HuggingFace connection failed: {e}")
                print("Running in MOCK mode")
        else:
            print("No HuggingFace token found. Running in MOCK mode.")
        
    def verify_claim(self, claim: str, evidence: list):
        """
        Verify a claim using LLM analysis against retrieved evidence.
        
        Args:
            claim (str): The claim to verify
            evidence (list): List of Document objects containing relevant facts
            
        Returns:
            dict: Contains verdict and explanation
                - verdict: "TRUE", "FALSE", or "UNCERTAIN"
                - explanation: Detailed reasoning for the verdict
        """
        print(f"Verifying Claim: '{claim}' against {len(evidence)} evidence items.")
        
        # Extract text content from evidence documents
        context = "\n".join([doc.page_content for doc in evidence])
        
        # Construct the prompt for the LLM
        # This prompt instructs the model to act as a fact-checker
        prompt = f"""You are a fact-checker. Analyze the claim against the evidence and determine if it's TRUE or FALSE.

Claim: {claim}

Evidence:
{context}

Is the claim TRUE or FALSE? Provide a brief explanation.
Answer in this format:
Verdict: [TRUE/FALSE]
Explanation: [Your explanation]"""
        
        # Try to use HuggingFace API if available
        if self.client:
            try:
                # Call the LLM with the prompt
                response = self.client.text_generation(
                    prompt,
                    model=self.model,
                    max_new_tokens=200,  # Limit response length
                    temperature=0.3  # Lower temperature for more focused responses
                )
                
                # Parse the response
                verdict = "UNCERTAIN"
                explanation = response
                
                # Extract verdict from response
                if "FALSE" in response.upper():
                    verdict = "FALSE"
                elif "TRUE" in response.upper():
                    verdict = "TRUE"
                    
                # Extract explanation if formatted correctly
                if "Explanation:" in response:
                    explanation = response.split("Explanation:")[-1].strip()
                
                return {
                    "verdict": verdict,
                    "explanation": explanation
                }
            except Exception as e:
                print(f"HuggingFace API error: {e}")
                print("Falling back to MOCK mode")
        
        # Mock Response (fallback when API is unavailable)
        # This provides basic verification based on simple logic
        if "Earth orbits" in context and "flat" in claim.lower():
            return {
                "verdict": "FALSE",
                "explanation": "The evidence states that the Earth orbits the Sun, implying it is a celestial body in a solar system, contradicting the flat earth theory."
            }
        
        # Default uncertain response
        return {
            "verdict": "UNCERTAIN",
            "explanation": "Insufficient evidence to verify this claim definitively."
        }

# Test the verifier if run directly
if __name__ == "__main__":
    from src.rag.retriever import RAGRetriever
    
    # Initialize components
    retriever = RAGRetriever()
    verifier = LLMVerifier()
    
    # Test with a claim
    claim = "Is the earth flat?"
    evidence = retriever.retrieve(claim)
    result = verifier.verify_claim(claim, evidence)
    
    print(f"\nVerdict: {result['verdict']}")
    print(f"Explanation: {result['explanation']}")
