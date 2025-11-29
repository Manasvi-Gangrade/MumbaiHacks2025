import json
import os
from datetime import datetime

class ExplainabilityLogger:
    """
    Logs all agent decisions with explanations for transparency.
    """
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.log_file = os.path.join(log_dir, f"factseeker_{datetime.now().strftime('%Y%m%d')}.jsonl")
        
    def log_decision(self, content, detection_result, verification_result=None, action_taken=None):
        """
        Log a complete decision cycle with all reasoning.
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "content": content,
            "detection": {
                "label": detection_result.get("label"),
                "confidence": detection_result.get("confidence"),
                "flagged": detection_result.get("flagged")
            },
            "verification": verification_result if verification_result else None,
            "action": action_taken,
            "reasoning": self._generate_reasoning(detection_result, verification_result, action_taken)
        }
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
            
        print(f"📝 Logged decision to {self.log_file}")
        
    def _generate_reasoning(self, detection_result, verification_result, action_taken):
        """
        Generate human-readable reasoning for the decision.
        """
        reasoning = []
        
        # Detection reasoning
        if detection_result.get("flagged"):
            reasoning.append(f"Content was flagged as potential misinformation with {detection_result['confidence']:.0%} confidence.")
        else:
            reasoning.append(f"Content appears legitimate with {1-detection_result['confidence']:.0%} confidence.")
            
        # Verification reasoning
        if verification_result:
            reasoning.append(f"Fact-checking verdict: {verification_result.get('verdict')}")
            reasoning.append(f"Explanation: {verification_result.get('explanation')}")
            
        # Action reasoning
        if action_taken:
            reasoning.append(f"Action taken: {action_taken}")
            
        return " ".join(reasoning)

if __name__ == "__main__":
    logger = ExplainabilityLogger()
    
    # Test logging
    logger.log_decision(
        content="The moon landing was fake!",
        detection_result={"label": "Potential Misinformation", "confidence": 0.95, "flagged": True},
        verification_result={"verdict": "FALSE", "explanation": "NASA and multiple independent sources confirm moon landing."},
        action_taken="Alert sent to users"
    )
    print("✅ Test log created successfully!")
