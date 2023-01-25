import random

from rich import print as rprint
from rich.text import Text
from rich import get_console
from rich.table import Table
from rich.panel import Panel
from rich.box import SIMPLE

from constants import COMMAND_STYLE, STYLE_COLORS
from mechanics.character.hero import Hero
from mechanics.character.race import Ascenag, Durrok, Scrof, Seraphim

# Props

command_help_message = (
    "Type",
    (" ? ", COMMAND_STYLE),
    "to see the list of available commands",
)


# Printers


def welcoming_message() -> None:
    """
    Prints welcoming message.
    """

    random_color: str = __random_message_color()
    max_width = __get_max_console_width()

    welcoming_text: Text = Text()
    welcoming_text.append(
        " Welcome to Pythos Labyrinth ".center(max_width, "="),
        style=f"{random_color} bold",
    )
    welcoming_text.append("\n\n")
    welcoming_text.append_text(Text.assemble(*command_help_message))

    __announcing_wrapper(welcoming_text)


def farewell_message(session_playtime: str = "") -> None:
    """
    Prints farewell message.
    """

    random_color: str = __random_message_color()
    max_width = __get_max_console_width()

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


# Hero printers
def print_hero_overview(hero: Hero) -> None:

    max_width = __get_max_console_width() // 2

    hero_color: str = __match_race_color(hero.race_name)

    hero_table = Table(
        show_header=False,
        expand=True,
        show_edge=False,
        box=SIMPLE,
    )

    hero_table.add_row("Race", hero.race_name)
    hero_table.add_row("Health", f"{hero.health}/{hero.max_health}")

    readable_level = __wrap_up_level(
        level=hero.level,
        xp=hero.level_stats.effective_xp,
        xp_to_level_up=hero.level_stats.xp_to_next_level,
    )

    hero_table.add_row("Level", readable_level)

    hero_panel = Panel(
        hero_table,
        title=hero.name,
        width=max_width,
        border_style=hero_color,
    )

    printer(hero_panel)


# Utils


def printer(*parts) -> None:
    """
    Prints the specified message.

    Args:
        message: The message to print.
    """
    rprint(*parts)


def __get_max_console_width() -> int:
    """
    Returns the maximum console width.
    """
    console = get_console()

    return min(console.width, max(100, int(console.width * 0.6)))


def __random_message_color() -> str:
    """
    Returns random message color.
    """

    return random.choice(STYLE_COLORS)


def __match_race_color(race_name: str) -> str:
    if race_name == Ascenag.name():
        return STYLE_COLORS[0]
    elif race_name == Seraphim.name():
        return STYLE_COLORS[1]
    elif race_name == Durrok.name():
        return STYLE_COLORS[2]
    elif race_name == Scrof.name():
        return STYLE_COLORS[3]

    return ""


def __announcing_wrapper(message):
    """
    Prints the specified message.

    Args:
        message: The message to print.
    """
    console = get_console()

    console.bell()
    console.line(1)

    printer(message)

    console.line(2)


def __progress_bar(
    progress: int,
    total: int,
    width: int = 10,
    fill: str = "◼",
    empty: str = "◻",
) -> str:
    """
    Returns a progress bar.

    Args:
        progress: The current progress.
        total: The total progress.
        width: The progress bar width.
        fill: The fill character.
        empty: The empty character.
        style: The progress bar style.
    """
    return f"{fill * int(progress / total * width)}{empty * (width - int(progress / total * width))}"


def __annotate_progress_bar(
    progress: int,
    total: int,
    width: int = 10,
    fill: str = "◼",
    empty: str = "◻",
) -> str:
    """
    Returns a progress bar with the progress percentage.

    Args:
        progress: The current progress.
        total: The total progress.
        width: The progress bar width.
        fill: The fill character.
        empty: The empty character.
        style: The progress bar style.
    """
    return f"{progress}/{total} {__progress_bar(progress, total, width, fill, empty)} {round(progress / total * 100)}%"


# Helpers


def __wrap_up_level(
    *,
    level: int,
    xp: int,
    xp_to_level_up: int,
) -> str:
    level_up_available: bool = xp >= xp_to_level_up
    level_up_available_text: str = "↑" if level_up_available else ""

    level_value: str = f"{level}{level_up_available_text}"

    level_progress: str = __annotate_progress_bar(xp, xp_to_level_up, 20)

    return "\n".join([level_value, level_progress])
