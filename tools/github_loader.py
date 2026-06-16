from git import Repo
import os
import shutil


def clone_repository(repo_url, clone_dir="temp_repo"):
    """
    Clone a GitHub repository locally.
    """

    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)

    Repo.clone_from(repo_url, clone_dir)

    return clone_dir