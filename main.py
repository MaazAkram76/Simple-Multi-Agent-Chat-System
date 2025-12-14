from agents.coordinator import Coordinator

if __name__ == "__main__":
    print("--- System Starting ---")
    
    # 1. Initialize the system
    app = Coordinator()
    
    # 2. TEST: Manually add some data to memory
    print("\n--- Testing Memory Storage ---")
    app.memory.add_memory("Python Arrays", "Lists are mutable arrays in Python.", source="Test")
    app.memory.add_memory("Java Arrays", "Arrays in Java have fixed size.", source="Test")
    
    # 3. TEST: Search for that data
    print("\n--- Testing Memory Search ---")
    query = "tell me about Python arrays"
    results = app.memory.search_memory(query)
    
    # 4. Print results
    if results:
        print(f"Query: '{query}'")
        print(f"Best Match: {results[0]['fact']} (Score: {results[0]['score']:.2f})")
    else:
        print("No matches found.")