from src.sync import GitHubSynchronizer, WorkedCache

if __name__ == "__main__":
    WorkedCache().sync()
    GitHubSynchronizer().sync()
