# agents/coordinator.py
from .research_agent import ResearchAgent
from .analysis_agent import AnalysisAgent
from .memory_agent import MemoryAgent

class Coordinator:
    def __init__(self):
        print("Coordinator: System initializing...")
        self.researcher = ResearchAgent()
        self.analyst = AnalysisAgent()
        self.memory = MemoryAgent()
        print("Coordinator: System Ready.\n")

    def process_query(self, user_query):
        """
        The Master Logic:
        1. Check Memory -> 2. Research -> 3. Analyze -> 4. Store
        """
        print(f"Coordinator: Received query: '{user_query}'")

        # --- STEP 1: Check Memory (Semantic Search) ---
        print("Coordinator: Checking memory for existing answers...")
        # We use a high threshold (0.5) to ensure we only use relevant memories
        past_memories = self.memory.search_memory(user_query, threshold=0.5)
        
        if past_memories:
            best_match = past_memories[0]
            print(f"Coordinator: Found answer in memory! (Confidence: {best_match['score']:.2f})")
            return f"Match Found in Memory: {best_match['fact']}"

        # --- STEP 2: Research (If memory failed) ---
        print("Coordinator: No memory found. Assigning task to Research Agent...")
        raw_data = self.researcher.search(user_query)
        
        # Check if research failed
        if "No information found" in raw_data:
            return "Coordinator: I could not find information on that topic."

        # --- STEP 3: Analysis ---
        print("Coordinator: Data found. Sending to Analysis Agent...")
        report = self.analyst.analyze(raw_data)

        # --- STEP 4: Learning (Store in Memory) ---
        print("Coordinator: Storing new knowledge in Memory Agent...")
        self.memory.add_memory(topic=user_query, fact=raw_data, source="Research Agent")

        return report