import random
import numpy as np
from mechanics.character.hero import Hero
from mechanics.leveling.leveling import LevelStats
from utils.logger import LoggerLevel, log
from mechanics.leveling.leveling_old import (
    xp_to_level_up,
    xp_to_level,
    actual_xp_from_level,
)


def generate_gamma_values(
    size: int,
    *,
    multiply: int = 20,
    min_value: int = 1,
    shape: int = 1,
    scale: int = 1,
) -> np.ndarray:
    """
    Generates gamma distributed random values.
    """
    values: np.ndarray = (
        np.random.gamma(shape, scale, size).round() * multiply + min_value
    )
    log(
        f"Configuration: {multiply=}, {min_value=}, [{min(values)}, {max(values)}]",
        level=LoggerLevel.INFO,
    )

    return values


def test_adding_xp(
    hero: Hero,
    *,
    test_count: int = 50,
    multiply: int = 20,
    min_value: int = 1,
) -> None:
    """
    Tests adding exp to hero.
    """
    random_values = generate_gamma_values(
        test_count, multiply=multiply, min_value=min_value
    )

    for ind in range(test_count):

        random_exp = int(random_values[ind])

        hero.add_xp(random_exp)

        log(f"Hero: {hero.level_stats.readable_detailed(round_digits=2)}")

        if hero.level_stats.is_level_up_available:
            will_level_up: bool = random.random() > 0.8
            if will_level_up:
                log("Level up!", level=LoggerLevel.INFO)
                hero.level_stats.level_up()


def main():
    TESTS_COUNT: int = 50
    random_values = generate_gamma_values(TESTS_COUNT, multiply=10)

    level_stats: LevelStats = LevelStats()

    for ind in range(TESTS_COUNT):
        log_name = f"Test {ind + 1}/{TESTS_COUNT}\t"

        random_xp = int(random_values[ind])

        log(f"+{random_xp} XP", name=log_name)
        level_stats.add(random_xp)

        if level_stats.is_level_up_available:
            level_up: bool = random.randint(0, 1) > 0.8
            if level_up:
                log("Level up!", name=log_name)
                level_stats.level_up()

        log(level_stats, name=log_name)


if __name__ == "__main__":
    main()
