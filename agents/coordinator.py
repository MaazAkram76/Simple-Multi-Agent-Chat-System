# agents/coordinator.py
# We use the dot (.) to say "look in this same folder"
from .research_agent import ResearchAgent
from .analysis_agent import AnalysisAgent
from .memory_agent import MemoryAgent

class Coordinator:
    def __init__(self):
        print("Coordinator: I am hiring my team...")
        self.researcher = ResearchAgent()
        self.analyst = AnalysisAgent()
        self.memory = MemoryAgent()
        print("Coordinator: Team is ready!")