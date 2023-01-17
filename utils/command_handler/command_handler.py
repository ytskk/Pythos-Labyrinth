from datetime import datetime
import enum
import sys
import time
from typing import Optional

from information_printer import command_help_message, farewell_message, printer
from lib.logger import LoggerLevel, log
from utils.date import DateFormats, readable_seconds
from utils.singletons.app_singleton import AppSingleton


class Commands(str, enum.Enum):
    HELP = "?"
    EXIT = "qqq"

    @staticmethod
    def from_str(s: str) -> Optional["Commands"]:
        return Commands(s) if s in Commands.values() else None

    @staticmethod
    def values() -> list[str]:
        return [cmd.value for cmd in Commands]


def get_raw_input() -> str:
    return input(">>> ")


def commands_handler() -> None:
    while True:
        raw_input: str = get_raw_input()

        command = Commands.from_str(raw_input)

        if command is None:
            __print_command_message(
                command_help_message,
                level=LoggerLevel.ERROR,
            )
            continue

        if command == Commands.EXIT:

            session_playtime = readable_seconds(AppSingleton().session_playtime())
            farewell_message(session_playtime=session_playtime)
            time.sleep(1)
            sys.exit()
        elif command == Commands.HELP:
            __print_command_message("Help")


def __print_command_message(
    message,
    *,
    level: LoggerLevel | None = None,
) -> None:
    """
    Prints the command message.

    Args:
        message: Message to be displayed.
        level: If the level is not set, it will not be shown, otherwise the transmitted one
        will be used. Defaults to None.
    """
    logger_level = level if level is not None else LoggerLevel.INFO

    log(
        message,
        show_date=True,
        show_name=False,
        show_level=level is not None,
        date_format=DateFormats.TIME,
        level=logger_level,
    )
