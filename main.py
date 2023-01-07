import random
from leveling_test import test_adding_xp
from mechanics.character.attributes import Attribute, Attributes
from mechanics.character.character_wrapper import choose_attribute
from mechanics.character.hero import Hero
from mechanics.character.race import Races
from mechanics.leveling.leveling import LevelStats
from utils.logger import log


def main():
    luck: int = random.randint(1, 100)

    hero: Hero = Hero(
        race=Races.random(),
        level_stats=LevelStats(),
        attributes=Attributes(
            luck=luck,
        ),
    )

    test_adding_xp(hero, test_count=200)

    log(f"Hero: {hero.attributes}")

    while hero.level_stats.points > 0:
        choose_attribute(hero, Attribute.random())

    log(f"Hero: {hero.attributes}")


if __name__ == "__main__":
    main()
