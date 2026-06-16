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
    backstory="Senior Python Engineer",
    llm=llm,
    verbose=False
)

task = Task(
    description="Review: def add(a,b): return a+b",
    expected_output="Code review",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=False
)

print(crew.kickoff())