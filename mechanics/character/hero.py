from typing import Any, Optional

from lib.readable import Readable
from mechanics.character.attributes import Attributes
from mechanics.character.race import Race
from mechanics.entities.alive_entity import AliveEntity
from mechanics.leveling.leveling import LevelStats


class Hero(Readable, AliveEntity):
    def __init__(
        self,
        *,
        race: Race,
        level_stats: LevelStats,
        attributes: Optional[Attributes] = None
    ) -> None:
        self.race = race
        self.attributes = race.basic_attributes().copy_from_attributes(attributes)
        self.level_stats = level_stats
        super().__init__(max_health=self.__max_health)

    @property
    def __max_health(self) -> int:
        return self.race.base_health + self.attributes.strength * 15

    def health(self) -> int:
        return self.current_health

    @property
    def level(self) -> int:
        return self.level_stats.level

    def add_xp(self, xp: int) -> None:
        self.level_stats.add(xp)
