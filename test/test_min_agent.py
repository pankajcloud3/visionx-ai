from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

agent = Agent(
    role="Reviewer",
    goal="Review code",
    backstory="Python developer",
    llm=llm
)

task = Task(
    description="Review: def add(a,b): return a+b",
    expected_output="Review",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task]
)

print(crew.kickoff())