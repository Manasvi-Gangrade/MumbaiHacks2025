from src.utils.ingestion import DataIngestion
from src.rag.detector import MisinformationDetector
from src.rag.retriever import RAGRetriever
from src.rag.llm_verifier import LLMVerifier
import time

class AgentManager:
    def __init__(self):
        print("Initializing Agent Manager...")
        self.ingestion = DataIngestion()
        self.detector = MisinformationDetector()
        self.retriever = RAGRetriever()
        self.verifier = LLMVerifier()
        
    def run_cycle(self):
        """
        Run one cycle of the autonomous workflow.
        """
        print("\n--- Starting Autonomous Cycle ---")
        
        # 1. Ingestion Agent
        print("🤖 Ingestion Agent: Scanning for content...")
        # Fetch 1 item for demo
        data_batch = self.ingestion.fetch_twitter_data(count=1)
        if not data_batch:
            print("No new data found.")
            return
            
        item = data_batch[0]
        print(f"   Found Item: {item['content'][:50]}...")
        
        # 2. Detection Agent
        print("🤖 Detection Agent: Analyzing content...")
        detection_result = self.detector.detect(item['content'])
        print(f"   Result: {detection_result['label']} (Confidence: {detection_result['confidence']:.2f})")
        
        if not detection_result['flagged']:
            print("   Content seems safe. Skipping verification.")
            return

        # 3. Verification Agent
        print("🤖 Verification Agent: Fact-checking...")
        evidence = self.retriever.retrieve(item['content'])
        print(f"   Retrieved {len(evidence)} evidence items.")
        
        verification_result = self.verifier.verify_claim(item['content'], evidence)
        print(f"   Verdict: {verification_result['verdict']}")
        print(f"   Explanation: {verification_result['explanation']}")
        
        # 4. Alert Agent
        if verification_result['verdict'] == "FALSE":
            self.send_alert(item, verification_result)
            
    def send_alert(self, item, verification_result):
        """
        Mock Alert Agent.
        """
        print("🚨 ALERT AGENT: Sending Public Alert!")
        alert_msg = f"""
        ⚠️ MISINFORMATION DETECTED ⚠️
        Original Content: "{item['content']}"
        Fact-Check: {verification_result['explanation']}
        Status: {verification_result['verdict']}
        """
        print(alert_msg)
        # In real app, call Telegram Bot here

if __name__ == "__main__":
    manager = AgentManager()
    # Run a few cycles
    for i in range(2):
        manager.run_cycle()
        time.sleep(1)
