import subprocess


def run_bandit_scan(repo_path):
    """
    Run Bandit security scan.
    """

    try:

        result = subprocess.run(
            [
                "bandit",
                "-r",
                repo_path
            ],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return f"Bandit Error: {e}"