class AnalysisAgent:
    def __init__(self):
        print("Analysis Agent: Ready.")

    def analyze(self, data):
        """
        Analyzes the provided text data and returns a summary.
        """
        print("Analysis Agent: Analyzing data...")
        
        if not data or "No information found" in data:
            return "Analysis Failed: Insufficient data."

        # Logic to simulate 'reasoning'
        word_count = len(data.split())
        
        # Construct a structured summary
        summary = (
            f"--- ANALYSIS REPORT ---\n"
            f"Input Data Length: {len(data)} chars\n"
            f"Word Count: {word_count}\n"
            f"Key Insight: {data}\n"
            f"-----------------------"
        )
        return summary