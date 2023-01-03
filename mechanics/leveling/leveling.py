import math
from lib.utils import clamp
from mechanics.character.attributes import Attribute
from utils.logger import log


class LevelStats:
    BASE_START_POINTS: int = 2
    LEVELS_TO_SKILL_POINT: int = 3

    def __init__(
        self,
        xp: int = 0,
        points: int = BASE_START_POINTS,
    ) -> None:
        self.__xp = xp
        self.__level = xp_to_level(xp)
        self.__points: float = points

    # getters.

    @property
    def xp_to_next_level(self) -> int:
        """
        XP required to level up, based on current level.
        """
        return xp_to_level_up_from_level(self.__level)

    @property
    def effective_xp(self) -> int:
        """
        XP progress for current level.
        """
        return clamp(self.__xp, lower_limit=0, upper_limit=self.xp_to_next_level)

    @property
    def is_level_up_available(self) -> bool:
        return self.__xp >= self.xp_to_next_level

    @property
    def level(self) -> int:
        """
        Returns current level.
        """
        return self.__level

    @property
    def points(self) -> int:
        """
        Unspend skill points.

        See also:
        - LevelStats.LEVELS_TO_SKILL_POINT
        - LevelStats.BASE_START_POINTS
        """
        return math.floor(self.__points)

    # methods.

    def add(self, xp: int) -> None:
        self.__xp += xp

    def level_up(self) -> None:
        required_xp: int = self.xp_to_next_level
        if self.__xp >= required_xp:
            self.__level += 1
            self.__xp -= required_xp
            self.__points += 1 / LevelStats.LEVELS_TO_SKILL_POINT

    # utils.

    def readable(self) -> str:
        return f"Level: {self.level}, {self.effective_xp} of {self.xp_to_next_level}, {self.points} points.{' Level up available' if self.is_level_up_available else ''}"

    def detailed_read(self) -> str:
        return f"{self.level=}, {self.effective_xp=}, {self.xp_to_next_level=}, {self.points=}.{' Level up available' if self.is_level_up_available else ''}"

    # magic methods.
    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"LevelStats({self.readable()})"


def xp_to_level_up_from_level(level: int) -> int:
    """
    Returns the required amount of experience needed to level up from the current level
    """
    return 75 + level * 25


def xp_to_level_up_from_xp(xp: int) -> int:
    """
    Returns the required amount of experience needed to level up from the total xp.
    """
    current_level = xp_to_level(xp)
    return 75 + current_level * 25


def remained_xp_to_next_level(current_xp: int) -> int:
    """
    Remained experience to level up.
    """
    current_level: int = xp_to_level(current_xp)
    total_xp_to_level = level_to_xp(current_level + 1)
    return total_xp_to_level - current_xp


def actual_xp_from_level(xp: int) -> int:
    """
    Experience from the current level.
    """
    total_xp_to_level = level_to_xp(xp_to_level(xp))
    return xp - total_xp_to_level


def level_to_xp(level: int) -> int:
    """
    Converts level to experience.
    """

    return int(12.5 * (level**2) + 62.5 * level - 75)


def xp_to_level(xp: int) -> int:
    """
    Converts experience to level.
    """

    return int(-2.5 + math.sqrt(8 * xp + 1225) / 10)
