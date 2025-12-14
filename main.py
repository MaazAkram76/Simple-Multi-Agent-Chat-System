# main.py
from agents.coordinator import Coordinator

if __name__ == "__main__":
    # 1. Start the System
    app = Coordinator()
    
    # 2. First User Query (System doesn't know this yet)
    print("\n--- USER QUERY 1: 'What are transformers?' ---")
    response1 = app.process_query("transformers")
    print(f"\nFINAL OUTPUT:\n{response1}")
    
    # 3. Second User Query (Asking the SAME thing to test Memory)
    # The Coordinator should find this in memory and SKIP the research step.
    print("\n--- USER QUERY 2: 'Explain transformers' ---")
    response2 = app.process_query("Explain transformers architecture")
    print(f"\nFINAL OUTPUT:\n{response2}")