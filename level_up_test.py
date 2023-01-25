import random
from leveling_test import test_adding_xp
from mechanics.character.attributes import Attribute, Attributes
from mechanics.character.character_wrapper import choose_attribute, level_up_hero

from mechanics.character.hero import Hero
from mechanics.character.race import Races
from mechanics.leveling.leveling import LevelStats
from lib.logger import log


def main():
    luck: int = random.randint(1, 100)

    hero: Hero = Hero(
        race=Races.random(),
        level_stats=LevelStats(),
        attributes=Attributes(
            luck=luck,
        ),
    )

    log(f"{hero.readable_detailed(round_digits=2, include_private_methods=False)}")

    test_adding_xp(hero, test_count=100)

    available_commands: list[str | None] = [
        "l - level up" if hero.level_stats.is_level_up_available else None,
        "c - choose attribute" if hero.level_stats.points > 0 else None,
    ]

    log.info(
        f"Available commands: {', '.join([command for command in available_commands if command is not None])}"
    )

    while (command := input("Choose command: ")) != "q":

        if command == "l":
            level_up_hero(hero)

        elif command == "c":
            log.info(
                "Choosing attribute:\ns - strength\nc - charisma\ni - intelligence\na - agility\nl - luck"
            )

            attribute: str = input("Choose attribute: ")

            if attribute == "s":
                choose_attribute(hero, Attribute.STRENGTH)
            elif attribute == "c":
                choose_attribute(hero, Attribute.CHARISMA)
            elif attribute == "i":
                choose_attribute(hero, Attribute.INTELLIGENCE)
            elif attribute == "a":
                choose_attribute(hero, Attribute.AGILITY)
            elif attribute == "l":
                choose_attribute(hero, Attribute.LUCK)

        log.info(
            f"Level up: {hero.readable_detailed(round_digits=2, include_private_methods=False)}"
        )

        available_commands: list[str | None] = [
            "l - level up" if hero.level_stats.is_level_up_available else None,
            "c - choose attribute" if hero.level_stats.points > 0 else None,
        ]

        log.info(
            f"Available commands: {', '.join([command for command in available_commands if command is not None])}"
        )

    log(f"{hero.readable_detailed(round_digits=2, include_private_methods=False)}")


if __name__ == "__main__":
    main()
