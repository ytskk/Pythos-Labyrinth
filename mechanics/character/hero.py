from typing import Any, Optional

from lib.readable import Readable
from mechanics.character.attributes import Attributes
from mechanics.character.race import Race
from mechanics.leveling.leveling import LevelStats


class Hero(Readable):
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

    def props(self) -> list[Any]:
        """
        Converts self.race to attribute name
        """
        return [
            "race",
            "attributes",
            "level_stats",
        ]
