from information_printer import welcoming_message

from utils.command_handler.command_handler import commands_handler
from utils.singletons.app_singleton import AppSingleton


def main():
    app_singleton: AppSingleton = AppSingleton()
    welcoming_message()
    commands_handler()

    # luck: int = random.randint(1, 100)
    #
    # hero: Hero = Hero(
    #     race=Races.random(),
    #     level_stats=LevelStats(),
    #     attributes=Attributes(
    #         luck=luck,
    #     ),
    # )
    #
    # log(f"{hero.readable_detailed(round_digits=2, include_private_methods=False)}")
    #
    # test_adding_xp(hero, test_count=200)
    #
    # while hero.level_stats.points > 0:
    #     choose_attribute(hero, Attribute.random_without_luck())
    #
    # log(f"{hero.readable_detailed(round_digits=2, include_private_methods=False)}")


if __name__ == "__main__":
    main()
