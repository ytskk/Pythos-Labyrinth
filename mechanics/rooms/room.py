import enum
import random
from lib.logger import log


class RoomType(str, enum.Enum):
    PLOY = "Ploy"
    TREASURE = "Treasure"

    @staticmethod
    def all():
        return RoomType.__members__.values()

    @staticmethod
    def random() -> "RoomType":
        return random.choice(list(RoomType.__members__.values()))

    @staticmethod
    def rooms_coefs():
        return {
            RoomType.PLOY: 70,
        }


class Room:
    def __init__(self, room_type: RoomType) -> None:
        self.type = room_type
