import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

class ResearchAgent:
    def __init__(self):
        print("Research Agent: Connecting to Groq API...")
        
        # 1. Get the API Key securely
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("Error: GROQ_API_KEY not found in .env file.")
            
        # 2. Initialize the Client
        self.client = Groq(api_key=api_key)
        print("Research Agent: Connection Established.")

    def search(self, query):
        """
        Sends the user's query to the Llama-3 model via Groq.
        """
        print(f"Research Agent: Querying Llama-3 for '{query}'...")
        
        try:
            # 3. Create the API completion request
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a concise research assistant. Provide a clear, factual definition or explanation in 2-3 sentences."
                    },
                    {
                        "role": "user",
                        "content": query,
                    }
                ],
                model="llama-3.1-8b-instant",
                temperature=0.5,
            )

            # 4. Extract the response text
            result = chat_completion.choices[0].message.content
            return result

        except Exception as e:
            return f"Research Agent Error: API request failed. Details: {e}"