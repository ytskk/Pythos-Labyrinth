from mechanics.character.hero import Hero
from mechanics.rooms.room import RoomType
from mechanics.rooms.rooms_generator import generate_room
from lib.logger import log


def main():
    rooms_count = 4

    test_hero: Hero = Hero.random_hero()

    __test_room_generation(rooms_count, luck=-10000, test_name="Unlucky")
    __test_room_generation(rooms_count, luck=10000, test_name="Lucky  ")


def __test_room_generation(it: int = 4, luck: int = 50, test_name: str = "Normal"):
    stats: dict[str, int] = {room_type.name.lower(): 0 for room_type in RoomType.all()}

    for _ in range(it):
        room = generate_room(luck)
        stats[room.type.name.lower()] += 1

    log(
        f"{test_name} "
        + " | ".join(f"{key}: {value/it*100:.2f}%" for key, value in stats.items()),
        name=test_name,
    )


if __name__ == "__main__":
    main()