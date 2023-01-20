from datetime import datetime
from utils.singletons.singleton import MetaSingleton


class AppSingleton(metaclass=MetaSingleton):
    def __init__(self):
        self.name = "AppSingleton"
        self.session_starttime = datetime.now()

    def session_playtime(self) -> float:
        diff = datetime.now() - self.session_starttime

        return diff.total_seconds()
