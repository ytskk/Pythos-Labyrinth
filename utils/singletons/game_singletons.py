from mechanics.character.hero import Hero
from utils.singletons.singleton import MetaSingleton


class GameSingleton(metaclass=MetaSingleton):
    """
    Holds the game state.
    """

    @property
    def hero(self) -> Hero:
        return self.__hero

    def init(self, hero: Hero) -> None:
        self.__hero = hero
