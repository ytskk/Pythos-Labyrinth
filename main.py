import random

from information_printer import welcoming_message
from leveling_test import test_adding_xp
from lib.logger import log
from mechanics.character.attributes import Attribute, Attributes
from mechanics.character.character_wrapper import choose_attribute
from mechanics.character.hero import Hero
from mechanics.character.race import Races
from mechanics.leveling.leveling import LevelStats


def main():
    welcoming_message()

    luck: int = random.randint(1, 100)

    hero: Hero = Hero(
        race=Races.random(),
        level_stats=LevelStats(),
        attributes=Attributes(
            luck=luck,
        ),
    )
    log(f"{hero.readable_detailed(round_digits=2, include_private_methods=False)}")

    test_adding_xp(hero, test_count=200)

    while hero.level_stats.points > 0:
        choose_attribute(hero, Attribute.random_without_luck())

    log(f"{hero.readable_detailed(round_digits=2, include_private_methods=False)}")


if __name__ == "__main__":
    main()
