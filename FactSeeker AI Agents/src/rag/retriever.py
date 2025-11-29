from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_core.documents import Document
import faiss
from src.utils.preprocessing import TextPreprocessor

class RAGRetriever:
    def __init__(self):
        print("Initializing RAG Retriever...")
        self.preprocessor = TextPreprocessor()
        # Initialize FAISS
        # Dimension of all-MiniLM-L6-v2 is 384
        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
        self.vector_store = FAISS(
            embedding_function=self.preprocessor.model.encode,
            index=self.index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={}
        )
        self._populate_knowledge_base()

    def _populate_knowledge_base(self):
        """
        Populate with some initial trusted facts (Mock Knowledge Base).
        """
        facts = [
            "The World Health Organization (WHO) states that vaccines are safe and effective.",
            "The Earth orbits the Sun, and it takes approximately 365.25 days to complete one orbit.",
            "Drinking water is essential for human survival.",
            "COVID-19 is caused by the SARS-CoV-2 virus.",
            "The capital of France is Paris."
        ]
        documents = [Document(page_content=fact, metadata={"source": "TrustedSource"}) for fact in facts]
        self.vector_store.add_documents(documents)
        print(f"✅ Indexed {len(facts)} trusted facts.")

    def retrieve(self, query: str, k: int = 2):
        """
        Retrieve relevant documents for a query.
        """
        print(f"Searching for: '{query}'")
        results = self.vector_store.similarity_search(query, k=k)
        return results

if __name__ == "__main__":
    retriever = RAGRetriever()
    query = "Is the earth flat?"
    docs = retriever.retrieve(query)
    for doc in docs:
        print(f"Found: {doc.page_content}")
