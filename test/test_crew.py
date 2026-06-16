from crewai import Task, Crew, Process

from agents import (
    code_analyzer,
)

task = Task(
    description="""
    Review this code:

    def add(a,b):
        return a+b
    """,
    expected_output="Code review",
    agent=code_analyzer
)

crew = Crew(
    agents=[code_analyzer],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print(result)