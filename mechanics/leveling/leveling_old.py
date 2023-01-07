import math

from lib.logger import log


class LevelStats:
    LEVELS_TO_SKILL_POINT: int = 3

    def __init__(self, xp: int = 0):
        self.xp = xp
        self.level = xp_to_level(xp)
        self.__unspend_points = 2
        self.update(xp)

    def add(self, xp: int):
        """
        Adds experience and updates properties.
        """
        log(
            f"+{xp}XP",
            name="LevelStats::add",
        )
        self.update(self.xp + xp)

    def update(self, xp: int):
        """
        Sets experience and updates properties.
        """
        self.xp = xp

        new_level: int = xp_to_level(xp)
        self.__unspend_points += (
            new_level - self.level
        ) / LevelStats.LEVELS_TO_SKILL_POINT

        self.level = xp_to_level(xp)
        self.xp_progress = actual_xp_from_level(xp)
        self.xp_to_level_up = xp_to_level_up(xp)

    @property
    def points(self) -> int:
        return int(self.__unspend_points)

    def subtract_points(self, points: int = 1) -> None:
        self.__unspend_points -= points

    def readable(self) -> str:
        return f"Current level: {self.level} ({self.points} points), {self.xp_progress} of {self.xp_to_level_up}"

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"LevelStats({self.readable()})"


def xp_to_level_up(xp: int) -> int:
    """
    Returns the required amount of experience needed to level up from the current level
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
