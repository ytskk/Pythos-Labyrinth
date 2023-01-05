import random
from leveling_test import test_adding_xp
from mechanics.character.attributes import Attributes
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

    log(f"Hero: {hero}")

    test_adding_xp(hero, test_count=40)

    log(f"Hero: {hero}")

    # for _ in range(hero.level_stats.points):
    #     hero.choose_attribute(Attribute.random())

    log(f"Hero: {hero}")


if __name__ == "__main__":
    main()
