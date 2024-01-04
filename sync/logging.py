from abc import ABC
from datetime import datetime, timedelta
from enum import Enum


class EventType(Enum):
    ABSTRACT = "abstruct"
    WORKED_CACHE_TO_MAIN_STORAGE = "worked_cache_to_main_storage"
    GITHUB_TO_MAIN_STORAGE = "github_to_main_storage"


class SyncEvent(ABC):
    type = EventType.ABSTRACT

    def __init__(self, duration: timedelta):
        self.date = datetime.now()
        self.duration = duration


class WorkedCacheToMainStorage(SyncEvent):
    type = EventType.WORKED_CACHE_TO_MAIN_STORAGE


class GitHubToMainStorage(SyncEvent):
    type = EventType.GITHUB_TO_MAIN_STORAGE


class SyncLogger:
    @staticmethod
    def add_event(event: SyncEvent):
        with open("events.log", "a") as f:
            f.write(f"{event.date}, {event.type}, {event.duration}\n")


sync_logger = SyncLogger()
