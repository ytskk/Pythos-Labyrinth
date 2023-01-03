def clamp(
    value,
    *,
    lower_limit,
    upper_limit,
):
    """
    Returns this num clamped to be in the range lowerLimit-upperLimit.
    """
    return min(upper_limit, max(lower_limit, value))
