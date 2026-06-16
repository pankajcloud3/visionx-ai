from tools.github_loader import clone_repository
from tools.repo_loader import get_python_files
from tools.code_parser import read_code_file
from tools.security_scan import run_bandit_scan


repo_path = clone_repository(
    "https://github.com/pallets/flask.git"
)

files = get_python_files(repo_path)

print(f"Total Files: {len(files)}")

print(files[:5])

content = read_code_file(files[0])

print(content[:300])

security_report = run_bandit_scan(
    repo_path
)

print(security_report[:1000])