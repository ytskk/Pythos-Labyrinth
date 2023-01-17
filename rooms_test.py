from mechanics.rooms.room import RoomType, Room
from mechanics.rooms.rooms_generator import generate_room
from lib.logger import log


def main():
    room: Room = generate_room()

    log(room.readable_detailed())
    room_content = room.generate_room_content()
    log(room_content.readable_detailed())

    # rooms_count = 4
    #
    # __test_room_generation(rooms_count, luck=-10000, test_name="Unlucky")
    # __test_room_generation(rooms_count, luck=10000, test_name="Lucky  ")


def __test_room_generation(it: int = 4, luck: int = 50, test_name: str = "Normal"):
    stats: dict[str, int] = {room_type.name.lower(): 0 for room_type in RoomType.all()}

    for _ in range(it):
        room = generate_room(luck)
        stats[room.room_type.name.lower()] += 1

    log(
        f"{test_name} "
        + " | ".join(f"{key}: {value / it * 100:.2f}%" for key, value in stats.items()),
        name=test_name,
    )


if __name__ == "__main__":
    main()
