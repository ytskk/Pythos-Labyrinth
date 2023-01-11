def guaranteed_random(
    *,
    attempt,
    base_prob,
    max_attempts: int | None,
):
    """
    Probability between 0 and 1 after `attempt` unsuccessful attempts. Each attempt increases the probability.
    If attempt will close to `max_attempts` then probability will be close to 1.

    Example:
        >>> guaranteed_random(attempt=0, base_prob=0.1, max_attempts=10)
        Att Probability
        0   0.10
        1   0.11
        2   0.14
        3   0.19
        4   0.26
        5   0.35
        6   0.46
        7   0.59
        8   0.74
        9   0.91
        10  1.10
    """
    if max_attempts:
        return base_prob + (attempt / max_attempts) ** 2

    return base_prob
