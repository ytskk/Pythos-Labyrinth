from datetime import datetime
import enum
from typing import Any
import inspect
from colorama import Fore, Style


class LoggerLevel(enum.Enum):
    INFO = Fore.GREEN
    DEBUG = Style.DIM
    WARNING = Fore.RED + Style.DIM
    ERROR = Fore.RED


def log(
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

    date: str = f"{datetime.now().strftime(date_format)} " if show_date else ""
    log_name: str = name or inspect.stack()[1].function
    print(
        f"{Style.DIM}{date}[{log_name}] {Style.RESET_ALL}{level.value}{level.name} {Style.RESET_ALL}{message}"
    )
