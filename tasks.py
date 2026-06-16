from crewai import Task

from agents import (
    code_analyzer,
    security_reviewer,
    bug_finder,
    documentation_writer
)


def create_tasks(
    code_content,
    security_report
):

    analyze_task = Task(
        description=f"""
Review the following code and provide:

1. Code quality analysis
2. Maintainability feedback
3. Best practice recommendations

Code:

{code_content[:3000]}
""",
        expected_output="Detailed code quality review",
        agent=code_analyzer
    )

    bug_task = Task(
        description=f"""
Find bugs, edge cases, logical issues, and potential runtime errors in the following code:

Code:

{code_content[:3000]}
""",
        expected_output="Detailed bug report",
        agent=bug_finder
    )

    security_task = Task(
        description=f"""
Analyze the following security report and identify vulnerabilities, risks, and remediation steps.

Security Report:

{security_report[:2000]}
""",
        expected_output="Detailed security assessment",
        agent=security_reviewer
    )

    documentation_task = Task(
        description="""
Combine the outputs from all previous agents into a final markdown report.

The report should contain:

1. Executive Summary
2. Code Quality Findings
3. Bug Analysis
4. Security Findings
5. Recommendations
6. Conclusion
""",
        expected_output="Final markdown report",
        agent=documentation_writer
    )

    return [
        analyze_task,
        bug_task,
        security_task,
        documentation_task
    ]