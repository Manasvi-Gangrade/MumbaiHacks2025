"""
FactSeeker Dashboard - Main Streamlit Application

This is the web interface for the FactSeeker misinformation detection system.
It provides a real-time dashboard for monitoring and detecting misinformation.

Flow:
1. User clicks "Run Detection Cycle" button
2. System fetches content from data sources (Twitter/News)
3. Detection agent analyzes content for potential misinformation
4. If flagged, verification agent fact-checks using RAG + LLM
5. Results are displayed as alerts with explanations
"""

import streamlit as st
import time
from src.utils.ingestion import DataIngestion
from src.rag.detector import MisinformationDetector
from src.rag.retriever import RAGRetriever
from src.rag.llm_verifier import LLMVerifier

# Configure the Streamlit page
st.set_page_config(page_title="FactSeeker Dashboard", layout="wide")

# Page title and description
st.title("FactSeeker: Autonomous Misinformation Detection")
st.markdown("Real-time monitoring of misinformation across social media platforms.")

# Initialize all components in session state (persists across reruns)
if 'ingestion' not in st.session_state:
    # Data ingestion component - fetches content from sources
    st.session_state.ingestion = DataIngestion()
    
    # Detection component - identifies potential misinformation
    st.session_state.detector = MisinformationDetector()
    
    # RAG retriever - searches knowledge base for relevant facts
    st.session_state.retriever = RAGRetriever()
    
    # LLM verifier - uses AI to verify claims
    st.session_state.verifier = LLMVerifier()
    
    # Store all alerts
    st.session_state.alerts = []
    
    # Track processed content to avoid duplicates
    st.session_state.processed_content = set()

# Sidebar with control panel
st.sidebar.header("Control Panel")

# Main action button - triggers the detection cycle
if st.sidebar.button("Run Detection Cycle"):
    with st.spinner("Agents are working..."):
        # Step 1: Fetch new content from data sources
        data_batch = st.session_state.ingestion.fetch_twitter_data(count=1)
        
        if data_batch:
            item = data_batch[0]
            
            # Check if we've already processed this exact content
            # This prevents duplicate alerts
            if item['content'] in st.session_state.processed_content:
                st.warning("This content was already scanned. Fetching new data...")
                # Fetch again to get different content
                data_batch = st.session_state.ingestion.fetch_twitter_data(count=1)
                item = data_batch[0]
            
            # Mark this content as processed
            st.session_state.processed_content.add(item['content'])
            
            # Step 2: Run detection algorithm
            # This checks if the content contains misinformation indicators
            detection_result = st.session_state.detector.detect(item['content'])
            
            # Step 3: If content is flagged, verify it with LLM
            if detection_result['flagged']:
                # Retrieve relevant evidence from knowledge base
                evidence = st.session_state.retriever.retrieve(item['content'])
                
                # Use LLM to verify the claim against evidence
                verification_result = st.session_state.verifier.verify_claim(item['content'], evidence)
                
                # Create alert object with all details
                new_alert = {
                    "timestamp": time.strftime("%H:%M:%S"),
                    "source": item['source'],
                    "author": item['author'],
                    "content": item['content'],
                    "verdict": verification_result['verdict'],
                    "confidence": detection_result['confidence'],
                    "explanation": verification_result['explanation']
                }
                
                # Add to beginning of alerts list (newest first)
                st.session_state.alerts.insert(0, new_alert)
                st.success(f"Misinformation Detected: {item['content'][:50]}...")
            else:
                # Content passed detection - not flagged
                st.info(f"Content seems safe: {item['content'][:50]}...")

# Main dashboard layout - two columns
col1, col2 = st.columns([2, 1])

# Left column - Recent Alerts
with col1:
    st.subheader("Recent Alerts")
    
    if st.session_state.alerts:
        # Display each alert as an expandable section
        for alert in st.session_state.alerts:
            with st.expander(f"{alert['verdict']}: {alert['content'][:50]}... ({alert['timestamp']})"):
                st.write(f"**Source:** {alert['source']} - {alert['author']}")
                st.write(f"**Content:** {alert['content']}")
                st.write(f"**Verdict:** {alert['verdict']}")
                st.write(f"**Explanation:** {alert['explanation']}")
                # Show confidence as a progress bar
                st.progress(alert['confidence'])
    else:
        st.info("No misinformation detected yet. Run a cycle to scan.")

# Right column - Statistics and System Status
with col2:
    st.subheader("Statistics")
    
    # Display key metrics
    st.metric("Total Scanned", len(st.session_state.processed_content))
    st.metric("Flagged Items", len(st.session_state.alerts))
    st.metric("Active Agents", "3")
    
    st.subheader("System Status")
    # Show status of each agent
    st.success("Ingestion Agent: ONLINE")
    st.success("Detection Agent: ONLINE")
    st.success("Verification Agent: ONLINE")
    
    # Button to clear all alerts and reset
    if st.button("Clear All Alerts"):
        st.session_state.alerts = []
        st.session_state.processed_content = set()
        st.rerun()

# Footer
st.markdown("---")
st.caption("FactSeeker v1.0 - Built with HuggingFace and Streamlit (100% FREE)")
