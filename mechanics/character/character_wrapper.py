from mechanics.character.attributes import Attribute
from mechanics.character.hero import Hero


def level_up_hero(hero: Hero) -> None:
    hero.level_stats.level_up()
    hero.increase_max_health(amount=hero.attributes.strength // 10)


def choose_attribute(hero: Hero, attribute: Attribute) -> None:
    if hero.level_stats.points > 0:
        hero = hero.copy_with(
            attributes=hero.attributes.add_attribute(
                attribute,
                count=hero.race.attribute_coefficient(attribute),
            )
        )
        hero.level_stats.spend_skill_points()
