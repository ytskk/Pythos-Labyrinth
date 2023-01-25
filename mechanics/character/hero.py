from typing import Optional

from lib.readable import Readable
from mechanics.character.attributes import Attributes
from mechanics.character.race import Race, Races
from mechanics.entities.alive_entity import AliveEntity
from mechanics.leveling.leveling import LevelStats


class Hero(Readable, AliveEntity):
    def __init__(
        self,
        *,
        name: str,
        race: Race,
        level_stats: LevelStats,
        attributes: Optional[Attributes] = None,
    ) -> None:
        self.__name = name
        self.__race = race
        self.__attributes = race.basic_attributes().copy_from_attributes(attributes)
        self.__level_stats = level_stats
        super().__init__(max_health=self.__start_health())

    @staticmethod
    def random() -> "Hero":
        """
        Creates a random hero.
        """
        return Hero(
            name="Godot",
            race=Races.random(),
            level_stats=LevelStats(),
        )

    # getters.
    @property
    def name(self) -> str:
        return self.__name

    @property
    def attributes(self) -> Attributes:
        return self.__attributes

    @property
    def level_stats(self) -> LevelStats:
        return self.__level_stats

    @property
    def level(self) -> int:
        return self.__level_stats.level

    @property
    def race(self) -> Race:
        return self.__race

    @property
    def race_name(self) -> str:
        return self.__race.name()

    # methods.

    def add_xp(self, xp: int) -> None:
        self.__level_stats.add(xp)

    def copy_with(
        self,
        *,
        name: Optional[str] = None,
        race: Optional[Race] = None,
        level_stats: Optional[LevelStats] = None,
        attributes: Optional[Attributes] = None,
    ):
        return Hero(
            name=name or self.__name,
            race=race or self.__race,
            level_stats=level_stats or self.__level_stats,
            attributes=attributes or self.__attributes,
        )

    def __start_health(self) -> int:
        return self.__race.base_health + int(self.__attributes.strength * 0.15)
