from mechanics.character.hero import Hero
from utils.printer.information_printer import welcoming_message

from utils.command_handler.command_handler import commands_handler
from utils.singletons.app_singleton import AppSingleton
from utils.singletons.game_singletons import GameSingleton


def main():
    hero: Hero = Hero.random()

    AppSingleton()
    GameSingleton().init(hero=hero)
    welcoming_message()

    commands_handler()


if __name__ == "__main__":
    main()
