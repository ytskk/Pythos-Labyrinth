import random
from lib.utils import clamp
from mechanics.rooms.room import Room, RoomType
from lib.logger import log


def generate_room(luck: int = 50) -> Room:
    room_type: RoomType = random_room_type_weighted(luck)

    room = Room.from_type(room_type, luck=luck)

    return room


def random_room_type_weighted(luck: int = 50) -> RoomType:
    """
    Returns a random room, weighted by the room type.

    Luck affects the weights. Luck 50 is the default value. Ploy weight is
    clamped to be in the range 65-85.
    """
    ploy_base_weight: int = RoomType.rooms_coefs()[RoomType.PLOY]

    ploy_weight: int = _get_ploy_weight(
        ploy_base_weight,
        luck,
        upper_limit=85,
        lower_limit=65,
    )

    weight_coef: float = ploy_weight / ploy_base_weight

    weights = tuple(
        int(weight * weight_coef) for weight in RoomType.rooms_coefs().values()
    )

    room_weights = (
        *weights,
        100 - sum(weights),
    )

    # log.debug(
    #     f"{weight_coef=}, Room weights: {room_weights}",
    #     name="Room weights",
    # )

    room_type = random.choices(
        population=list(RoomType.all()),
        weights=room_weights,
        k=1,
    )[0]

    return room_type


def _get_ploy_weight(
    base_weight: int,
    luck: int,
    lower_limit: int = 50,
    upper_limit: int = 90,
) -> int:
    """
    Returns the ploy room weight.

    By default the weight is 70. Luck affects the weight. Luck 50 is the
    default value. Ploy weight is clamped to be in the range 50-90.
    """
    return clamp(int(base_weight - (luck - 50) / 2), lower_limit, upper_limit)
