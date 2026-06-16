from crewai import LLM

llm = LLM(
    model="groq/llama3-70b-8192",
    api_key="YOUR_KEY"
)

print("LLM OK")