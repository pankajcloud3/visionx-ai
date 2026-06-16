import sys
from crewai import Crew, Process

from tools.github_loader import clone_repository
from tools.repo_loader import get_python_files
from tools.code_parser import read_code_file

from tasks import create_tasks
from agents import (
    code_analyzer,
    bug_finder,
    security_reviewer,
    documentation_writer
)


# REPO_URL = "https://github.com/pallets/flask.git"
if len(sys.argv) < 2:
    print("Usage: python3 run_review.py <repo_url>")
    sys.exit(1)

REPO_URL = sys.argv[1]

def main():
    print("Cloning repository...")
    repo_path = clone_repository(REPO_URL)

    print("Loading Python files...")
    files = get_python_files(repo_path)

    if not files:
        print("No Python files found.")
        return

    # For initial testing, analyze only first file
    target_file = files[0]

    print(f"Analyzing: {target_file}")

    code_content = read_code_file(target_file)

    security_report = ""

    tasks = create_tasks(
        code_content,
        security_report
    )

    crew = Crew(
        agents=[
            code_analyzer,
            bug_finder,
            security_reviewer,
            documentation_writer
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    with open(
        "reports/review_report.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(str(result))

    print("\nReport saved:")
    print("reports/review_report.md")


if __name__ == "__main__":
    main()