import abc
import enum
import random
from lib.logger import log
from lib.readable import Readable
from mechanics.rooms.rooms_content.room_content import (
    MonsterContent,
    RoomContent,
    TreasureContent,
)


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


class Room(Readable):
    def contents(self) -> list[RoomContent]:
        ...

    def generate_room_content(self) -> RoomContent:
        return random.choice(self.contents())(luck=self._luck)

    @property
    def room_type(self) -> RoomType:
        return self._room_type

    @classmethod
    def from_type(cls, room_type: RoomType, luck: int):
        if room_type == RoomType.PLOY:
            return PloyRoom(luck=luck)
        elif room_type == RoomType.TREASURE:
            return TreasureRoom(luck=luck)


class PloyRoom(Room):
    def __init__(self, luck: int):
        self._room_type = RoomType.PLOY
        self._luck = luck

    def contents(self):
        return [MonsterContent]


class TreasureRoom(Room):
    def __init__(self, luck: int):
        self._room_type = RoomType.TREASURE
        self._luck = luck

    def contents(self) -> list[RoomContent]:
        return [TreasureContent]
