from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant"
)
code_analyzer = Agent(
    role="Senior Code Reviewer",
    goal="Analyze code quality and maintainability",
    backstory="Experienced software architect",
    llm=llm,
    verbose=True
)

bug_finder = Agent(
    role="Bug Detection Expert",
    goal="Find bugs and edge cases",
    backstory="Expert software tester",
    llm=llm,
    verbose=True
)

# security_reviewer = Agent(
#     role="Security Reviewer",
#     goal="Find security vulnerabilities",
#     backstory="OWASP security expert",
#     llm=llm,
#     verbose=True
# )

documentation_writer = Agent(
    role="Technical Writer",
    goal="Generate final review report",
    backstory="Professional documentation writer",
    llm=llm,
    verbose=True
)