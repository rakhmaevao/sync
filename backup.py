import os
import subprocess
from datetime import datetime

from src.logging import MainStorageToFirstBackup, sync_logger

MAIN_VAULT_DIR = "/media/rahmaevao/42AB9F9C6511B3E0"
FIRST_BACKUP_VAULT_DIR = "/media/rahmaevao/70AEE6D577AD4A48/"


def _rsync(src: str, dest: str):
    subprocess.call(["rsync", "-cavz", "--delete", src, dest])


if __name__ == "__main__":
    t_0 = datetime.now()
    for filename in os.listdir(MAIN_VAULT_DIR):
        _rsync(f"{MAIN_VAULT_DIR}/{filename}", f"{FIRST_BACKUP_VAULT_DIR}/{filename}")
    sync_logger.add_event(MainStorageToFirstBackup(datetime.now() - t_0))
