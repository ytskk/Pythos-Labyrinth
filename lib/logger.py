import enum
import inspect
from datetime import datetime
from typing import Any

from rich import print as rprint
from rich.text import Text
from constants import INFO_STYLE, DEBUG_STYLE, WARNING_STYLE, ERROR_STYLE


class LoggerLevel(str, enum.Enum):
    INFO = INFO_STYLE
    DEBUG = DEBUG_STYLE
    WARNING = WARNING_STYLE
    ERROR = ERROR_STYLE


class log:
    def __init__(
        self,
        message: Any,
        *,
        level: LoggerLevel = LoggerLevel.DEBUG,
        name: str | None = None,
        show_date: bool = False,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        """
        This function prints a message to the console, with optional formatting.
        The message is displayed in the format: `date` [`name`] `level` `message`.

        - `date` is the current datetime
        - `name` custom logger name or the name of the function that called this function
        - `level` is the level of the message, describes by `LoggerLevel`
        - `message` is the message to be displayed in the console (can be any type)
        """
        self.level: LoggerLevel = level
        self.message: Any = message
        self.date: str = f"{datetime.now().strftime(date_format)} " if show_date else ""
        self.log_name: str = name or inspect.stack()[1].function
        self.__print()

    # named constuctors

    @classmethod
    def info(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.INFO,
            name=name,
            show_date=show_date,
            date_format=date_format,
        )

    @classmethod
    def debug(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.DEBUG,
            name=name,
            show_date=show_date,
            date_format=date_format,
        )

    @classmethod
    def warning(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.WARNING,
            name=name,
            show_date=show_date,
            date_format=date_format,
        )

    @classmethod
    def error(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.ERROR,
            name=name,
            show_date=show_date,
            date_format=date_format,
        )

    def __print(self) -> Any:
        text: Text = Text()
        text.append(self.date, style="dim")
        text.append(f"[{self.log_name}] ", style="dim")
        text.append(self.level.name, style=self.level.value)
        text.append(f" {self.message}")

        rprint(text)
