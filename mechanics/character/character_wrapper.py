from mechanics.character.hero import Hero
from mechanics.character.attributes import Attribute


def choose_attribute(hero: Hero, attribute: Attribute) -> None:
    hero.level_stats.level_up()
    hero.attributes = hero.attributes.add_attribute(attribute)
    hero.level_stats.spend_skill_points()
