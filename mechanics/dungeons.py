import random
from mechanics.character.hero import Hero
from utils.logger import log


def generate_turn(hero: Hero) -> list[str]:
    """Generate a turn for the current dungeon level."""
    luck: int = hero.attributes.luck

    dungeon_count_weights: tuple = (0.3, 0.5, 0.01)
    dungeon_count_values: tuple = (1, 2, 3)

    dungeon_count = random.choices(
        dungeon_count_values,
        dungeon_count_weights,
        k=1,
    )[0]

    return get_dungeon_types(count=dungeon_count, luck=luck)


def get_dungeon_types(
    *,
    count: int,
    luck: int,
) -> list[str]:
    """
    Get a list of dungeon types, based on the luck.
    """
    types: list[str] = [
        "Ploy",
        "Treasure",
        "Meeting",
    ]
    luck_factor: float = 0.4 * (luck - 50)
    weights: tuple = (
        0.6 - luck_factor,
        0.2 + luck_factor,
        0.05 + luck_factor,
    )
    log(weights)

    return random.choices(
        types,
        weights=weights,
        k=count,
    )
