from lib.utils import clamp


class AliveEntity:
    def __init__(self, max_health):
        self.__max_health = max_health
        self.__current_health = max_health

    # getters.

    @property
    def max_health(self) -> int:
        return self.__max_health

    @property
    def health(self) -> int:
        return self.__current_health

    def subtract(self, amount) -> None:
        self.__current_health = clamp(
            self.__current_health - amount,
            lower_limit=0,
            upper_limit=self.__max_health,
        )

    def add(self, amount) -> None:
        self.__current_health = clamp(
            self.__current_health + amount,
            lower_limit=0,
            upper_limit=self.__max_health,
        )

    def increase_max_health(self, amount: int) -> None:
        self.__max_health += amount

    @property
    def is_alive(self) -> bool:
        return self.__current_health > 0
