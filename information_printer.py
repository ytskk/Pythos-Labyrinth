import random
from typing import Any

from rich import print as rprint
from rich.console import Console
from rich.text import Text

from constants import COMMAND_STYLE

console = Console()


def welcoming_message() -> None:
    """
    Prints welcoming message.
    """

    random_color: str = __random_message_color()
    max_width = min(console.width, max(100, int(console.width * 0.6)))

    welcoming_text: Text = Text()
    welcoming_text.append(
        " Welcome to Pythos Labyrinth ".center(max_width, "="),
        style=f"{random_color} bold",
    )
    welcoming_text.append("\n\n")
    welcoming_text.append_text(command_help_message)

    __announcing_wrapper(welcoming_text)


def farewell_message(session_playtime: str = "") -> None:
    """
    Prints farewell message.
    """

    random_color: str = __random_message_color()
    max_width = min(console.width, max(100, int(console.width * 0.6)))

    farewell_text: Text = Text()
    farewell_text.append(
        " Goodbye ".center(max_width, "="), style=f"{random_color} bold"
    )
    farewell_text.append("\n\n")
    farewell_text.append_text(
        Text.assemble(
            "Thank you for playing Pythos Labyrinth. ",
            f"Your session lasted {session_playtime}. ",
            "See you soon!",
        )
    )

    __announcing_wrapper(farewell_text)


command_help_message: Text = Text.assemble(
    "Type", (" ? ", COMMAND_STYLE), "to see the list of available commands"
)


def __random_message_color() -> str:
    """
    Returns random message color.
    """

    colors: tuple = ("yellow", "green", "dark_orange", "red")

    return random.choice(colors)


def __announcing_wrapper(message):
    """
    Prints the specified message.

    Args:
        message: The message to print.
    """

    console.bell()
    console.line(1)

    rprint(message)

    console.line(2)


def printer(
    *messages: Any,
) -> None:
    """
    Prints the specified message.

    Args:
        message: The message to print.
    """
    rprint(*messages)
