import os.path
import subprocess
from datetime import datetime
from typing import NamedTuple

import yaml
from loguru import logger

from src.logging import WorkedCacheToMainStorage, sync_logger


class SynchronizedPair(NamedTuple):
    source_path: str
    destination_dir: str

    def sync(self):
        logger.info(f"Синхронизация пары {self}")
        if os.path.isdir(self.source_path):
            source_path = f"{self.source_path}/"
        else:
            source_path = self.source_path
        subprocess.call(
            [
                "rsync",
                "-a",  # a - не сохранение доступа, ссылок, расширенных атрибутов
                "—checksum",  # сравнения файлов по контрольной сумме
                "—compress",  # сжатие файлов при передаче
                "--delete",  # файлы, удалённые в src, должны быть удалены и из dst
                source_path,
                self.destination_dir,
            ]
        )


class WorkedCache:
    """
    Класс, отвечающий за работу с рабочим кешем, который хранится на рабочих
    устройствах.
    Каждый путь из кеша должен иметь назначение в основном хранилище.
    Пары задаются в файле `pairs_with_worked_cache.yml`.
    """

    def __init__(self) -> None:
        self.__pairs = self.__parse_sync_pairs()

    def sync(self):
        t_0 = datetime.now()
        for pair in self.__pairs:
            pair.sync()
        sync_logger.add_event(WorkedCacheToMainStorage(datetime.now() - t_0))

    @staticmethod
    def __parse_sync_pairs() -> list[SynchronizedPair]:
        with open("pairs_with_worked_cache.yml") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        pairs = []
        for pair in data["pairs"]:
            pairs.append(SynchronizedPair(pair["src"], pair["dest"]))
        return pairs
