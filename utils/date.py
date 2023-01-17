import enum


class DateFormats(str, enum.Enum):
    FULL_DATE = "%Y-%m-%d %H:%M:%S"
    DATE = "%Y-%m-%d"
    FULL_TIME = "%H:%M:%S"
    TIME = "%H:%M"


def readable_seconds(seconds: float) -> str:
    rounded_seconds = int(seconds)

    return f"{rounded_seconds}s"
