import time
import json
# specialized library for semantic search
from sentence_transformers import SentenceTransformer, util

class MemoryAgent:
    def __init__(self):
        print("Memory Agent: Loading embedding model (this may take a moment)...")
        # Load a pre-trained model for creating embeddings
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # 1. Knowledge Base: Stores dictionary with text and pre-computed embedding
        # Format: {"fact": "...", "embedding": tensor, "metadata": {...}}
        self.knowledge_base = [] 
        
        # 2. Conversation History
        self.conversations = [] 
        
        print("Memory Agent: Ready.")
        
    def add_memory(self, topic, fact, source="User"):
        """Stores a new finding and computes its vector embedding immediately."""
        # Convert the text fact into a vector (Tensor)
        embedding = self.model.encode(fact, convert_to_tensor=True)
        
        entry = {
            "topic": topic,
            "fact": fact,
            "source": source,
            "timestamp": time.time(),
            "embedding": embedding
        }
        self.knowledge_base.append(entry)
        print(f"Memory Agent: Stored and vectorized fact about '{topic}'")

    def search_memory(self, query, threshold=0.3):
        """
        Performs semantic search using Cosine Similarity.
        Args:
            query (str): The user's search text.
            threshold (float): Minimum similarity score (0 to 1) to return a result.
        """
        if not self.knowledge_base:
            return []

        # 1. Vectorize the query
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        
        results = []
        
        # 2. Compare query vector against all stored fact vectors
        for entry in self.knowledge_base:
            # Calculate Cosine Similarity
            score = util.cos_sim(query_embedding, entry["embedding"]).item()
            
            if score > threshold:
                results.append({
                    "topic": entry["topic"],
                    "fact": entry["fact"],
                    "score": score,
                    "source": entry["source"]
                })

        # 3. Sort by highest similarity score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results

    def get_context(self):
        """Returns the last 3 messages as a string."""
        if not self.conversations:
            return ""
        recent = self.conversations[-3:]
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent])

    def log_interaction(self, role, content):
        """Saves a chat message to history."""
        self.conversations.append({
            "role": role, 
            "content": content, 
            "timestamp": time.time()
        })