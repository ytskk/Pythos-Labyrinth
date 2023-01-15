def clamp(
    value,
    lower_limit,
    upper_limit,
):
    """
    Returns clamped value to be in the range lower_limit-upper_limit.
    """
    return min(upper_limit, max(lower_limit, value))
