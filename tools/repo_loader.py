import os


def get_python_files(repo_path):
    """
    Return all Python files from repository.
    """

    python_files = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in [
                ".git",
                "__pycache__",
                "venv",
                ".venv"
            ]
        ]

        for file in files:
            if file.endswith(".py"):
                python_files.append(
                    os.path.join(root, file)
                )

    return python_files