import enum
import sys
import time
from typing import Optional
from constants import COMMAND_STYLE
from leveling_test import test_adding_xp
from rich.table import Table
from rich.text import Text
from rich.box import SIMPLE

from utils.printer.information_printer import (
    command_help_message,
    farewell_message,
    print_hero_overview,
)
from lib.logger import LoggerLevel, log
from utils.date import DateFormats, readable_seconds
from utils.singletons.app_singleton import AppSingleton
from utils.singletons.game_singletons import GameSingleton


class Command:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description


class Commands(enum.Enum):
    HELP = Command(name="?", description="Prints this message")
    EXIT = Command(name="qqq", description="Exits the game")
    HERO = Command(name="hero", description="Prints hero overview")

    @staticmethod
    def from_str(s: str) -> Optional["Commands"]:
        return Commands(s) if s in Commands.values() else None

    @staticmethod
    def values() -> list[str]:
        return [cmd.value.name for cmd in Commands]

    @staticmethod
    def all() -> list["Commands"]:
        return list(Commands)


def get_raw_input() -> str:
    return input(">>> ")


def commands_handler() -> None:
    while True:
        try:
            command: str = get_raw_input()

            # uncomment when all command will be added to Commands enum
            # if command not in Commands.values():
            #     raise ValueError(
            #         f"Unknown command '{command}'. ",
            #         *command_help_message,
            #     )

            if command == Commands.EXIT.value.name:
                session_playtime = readable_seconds(AppSingleton().session_playtime())
                farewell_message(session_playtime=session_playtime)
                time.sleep(1)
                sys.exit()
            elif command == Commands.HELP.value.name:
                __help_message()
            elif command == Commands.HERO.value.name:
                hero = GameSingleton().hero
                print_hero_overview(hero=hero)
            elif command.startswith("add xp"):
                values = command.split(" ")
                if len(values) != 3:
                    raise ValueError("Wrong command format. Expected: add xp <value>")

                xp = int(values[2])
                hero = GameSingleton().hero
                hero.add_xp(xp)
            elif command == "fight 10":
                hero = GameSingleton().hero
                test_adding_xp(hero, test_count=10)
            else:
                raise ValueError(
                    f"Unknown command '{command}'. ",
                    *command_help_message,
                )
        # if command was not recognized. Replace for FormatError
        except ValueError as error:
            __print_command_message(
                error.args,
                level=LoggerLevel.ERROR,
            )
        # if session was interrupted by user. (Ctrl + C)
        except KeyboardInterrupt:
            session_playtime = readable_seconds(AppSingleton().session_playtime())
            farewell_message(session_playtime=session_playtime)
            time.sleep(1)
            sys.exit()


def __help_message() -> None:
    commands: list = Commands.all()
    commands_table = Table(
        title="Commands",
        title_justify="left",
        show_header=False,
        box=SIMPLE,
    )

    for command in commands:
        commands_table.add_row(
            Text(command.value.name, style=COMMAND_STYLE),
            command.value.description,
        )

    __print_command_message(commands_table)


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
