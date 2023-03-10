import enum
import inspect
from datetime import datetime
from typing import Any, Iterable

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
        show_name: bool = True,
        show_level: bool = True,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        """
        Prints a message to the console, with optional formatting.

        The message is displayed in the format: `date` [`name`] `level` `message`.

        Args:
            message: message to be displayed in the console (can be any type)
            level: level of the message, describes by `LoggerLevel`. Defaults to LoggerLevel.DEBUG.
            name: custom logger name or the name of the function that called this function. Defaults to None.
            date_format: is the current datetime. Defaults to "%Y-%m-%d %H:%M:%S".
        """

        self.level: LoggerLevel = level
        self.message: Any = message
        self.date: str = f"{datetime.now().strftime(date_format)} " if show_date else ""
        self.log_name: str = name or inspect.stack()[1].function
        self.show_name = show_name
        self.show_level = show_level
        self.__print()

    # named constuctors

    @classmethod
    def info(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        show_name: bool = True,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.INFO,
            name=name,
            show_date=show_date,
            show_name=show_name,
            date_format=date_format,
        )

    @classmethod
    def debug(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        show_name: bool = True,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.DEBUG,
            name=name,
            show_date=show_date,
            show_name=show_name,
            date_format=date_format,
        )

    @classmethod
    def warning(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        show_name: bool = True,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.WARNING,
            name=name,
            show_date=show_date,
            show_name=show_name,
            date_format=date_format,
        )

    @classmethod
    def error(
        cls,
        message: Any,
        *,
        name: str | None = None,
        show_date: bool = False,
        show_name: bool = True,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        cls(
            message,
            level=LoggerLevel.ERROR,
            name=name,
            show_date=show_date,
            show_name=show_name,
            date_format=date_format,
        )

    def __print(self) -> Any:
        """
        If self.message is an iterable, it will be unpacked and displayed as a list.

        If self.message is not an iterable, it will be displayed as is. Used for displaying
        Tables, etc.
        """
        is_message_iterable: bool = isinstance(self.message, Iterable)

        text: Text = Text.assemble(
            (self.date, "dim"),
            (f"[{self.log_name}] ", "dim") if self.show_name else "",
            (f"{self.level.name} ", self.level.value) if self.show_level else "",
            *self.message if is_message_iterable else "",
        )

        rprint(text, "" if is_message_iterable else self.message)
