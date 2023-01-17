import enum

from lib.readable import Readable


class RoomContents(str, enum.Enum):
    MONSTER = "Monster"
    TRAP = "Trap"
    TREASURE = "Treasure"


class RoomContent(Readable):
    ...

    def generate_content(self):
        ...


class MonsterContent(RoomContent):
    ...


class TreasureContent(RoomContent):
    ...
