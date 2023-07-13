from loguru import logger
from github import Github
import os
import subprocess
from typing import NamedTuple


class GithubRepo(NamedTuple):
    name: str
    ssh_url: str

    def sync(self):
        if os.path.exists(f"../Storage/Repositories/{self.name}"):
            logger.warning(f"Repository {self.name} is already exists. Only pulling...")
            subprocess.call(
                f"cd ../Storage/Repositories/{self.name} && "
                f"git pull --all && "
                f"cd -",
                shell=True,
            )
        else:
            logger.warning("Repositorie is not exist. Cloning...")   
            subprocess.call(
                f"cd ../Storage/Repositories && "
                f"git clone {self.ssh_url} && cd {self.name} && git pull --all && "
                f"cd -",
                shell=True,
            )


class GitHubSynchronizer:
    def __init__(self):
        g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))
        self.__repositories_ssh_urls = []
        for repo in g.get_user().get_repos():
            self.__repositories_ssh_urls.append(GithubRepo(repo.name, repo.ssh_url))

    def sync(self):
        for repo in self.__repositories_ssh_urls:
            repo.sync()
