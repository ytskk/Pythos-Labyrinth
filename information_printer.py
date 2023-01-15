import random

from rich import print as rprint
from rich.console import Console
from rich.text import Text

from constants import COMMAND_STYLE

console = Console()


def welcoming_message() -> None:
    """
    Prints welcoming message.
    """

    colors: tuple = ("yellow", "green", "dark_orange", "red")

    random_color: str = random.choice(colors)
    max_width = min(console.width, max(100, int(console.width * 0.6)))

    console.bell()
    console.line(1)

    welcoming_text: Text = Text()
    welcoming_text.append(
        " Welcome to Pythos Labyrinth ".center(max_width, "="),
        style=f"{random_color} bold",
    )
    welcoming_text.append("\n\n")
    welcoming_text.append_text(
        Text.assemble(
            "Type", (" ? ", COMMAND_STYLE), "to see the list of available commands"
        )
    )

    rprint(welcoming_text)

    console.line(2)
