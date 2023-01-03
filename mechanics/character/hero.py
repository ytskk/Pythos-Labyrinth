from typing import Optional
from mechanics.character.attributes import Attribute, Attributes
from mechanics.character.race import Race
from mechanics.leveling.leveling import LevelStats
from utils.logger import log, LoggerLevel


class Hero:
    def __init__(
        self,
        *,
        race: Race,
        attributes: Optional[Attributes] = None,
        level_stats: LevelStats,
    ) -> None:
        self.race = race
        self.attributes = race.basic_attributes().copy_from_attributes(attributes)
        self.level_stats = level_stats

    @property
    def level(self) -> int:
        return self.level_stats.level

    def add_xp(self, xp: int) -> None:
        self.level_stats.add(xp)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Hero({self.race}, {self.attributes}, {self.level_stats})"
