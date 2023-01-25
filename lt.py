from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.box import ROUNDED


def main():
    console = Console()
    hero_table = Table(
        show_header=False,
        expand=True,
        box=ROUNDED,
        show_edge=False,
    )
    hero_table.add_row("Godot")
    hero_table.add_row("Race", "Human")
    # hero_table.add_section()
    hero_table.add_row("Level", "2")
    # hero_table.add_section()
    hero_table.add_row("Health", annotated_progress_bar(80, 104, width=20))
    overview_content = hero_table
    hero_panel = Panel(overview_content, title="Godot", width=100)

    console.print(hero_panel)


def annotated_progress_bar(
    progress,
    total,
    width: int = 20,
    symbol: str = "◼",
) -> str:
    return f"{progress}/{total} {progress_bar(progress=progress, total=total, width=width, symbol=symbol,)}"


def progress_bar(
    progress,
    total,
    width: int = 20,
    symbol: str = "◼",
) -> str:
    """
    Creates a progress bar.

    Args:
        progress: The current progress.
        total: The total progress.
        width: The width of the progress bar.
        symbol: The symbol to use in the progress bar.

    Returns:
        The progress bar.
    """
    complete_part = symbol * int(progress / total * width)
    incomplete_part = "◻" * (width - len(complete_part))

    return f"{complete_part}{incomplete_part}"


if __name__ == "__main__":
    main()
