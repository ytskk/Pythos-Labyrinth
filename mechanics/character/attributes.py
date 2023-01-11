import enum
import random
from typing import Optional

from lib.logger import log
from lib.readable import Readable


class Attribute(str, enum.Enum):
    """
    Strength, Charisma, Intelligence, Agility and Luck.
    """

    STRENGTH = "STR"
    CHARISMA = "CHA"
    INTELLIGENCE = "INT"
    AGILITY = "AGI"
    LUCK = "LCK"

    @staticmethod
    def all():
        return Attribute.__members__.values()

    @staticmethod
    def random() -> "Attribute":
        random_attr = random.choice(list(Attribute.__members__.values()))
        log(f"Random attribute: {random_attr}")
        return random_attr


class Attributes(Readable):
    def __init__(
        self,
        *,
        strength: Optional[int] = None,
        charisma: Optional[int] = None,
        intelligence: Optional[int] = None,
        agility: Optional[int] = None,
        luck: Optional[int] = None,
    ) -> None:
        self.strength = strength
        self.charisma = charisma
        self.intelligence = intelligence
        self.agility = agility
        self.luck = luck

    @staticmethod
    def basic_attributes() -> "Attributes":
        """
        By default, creates attributes with 1 point in each attribute and 3 points in luck.
        """
        return Attributes(
            strength=1,
            charisma=1,
            intelligence=1,
            agility=1,
            luck=3,
        )

    def add_attribute(self, attribute: Attribute) -> "Attributes":
        return self.copy_with(
            **{attribute.name.lower(): getattr(self, attribute.name.lower()) + 1}
        )

    def copy_with(
        self,
        *,
        strength: Optional[int] = None,
        charisma: Optional[int] = None,
        intelligence: Optional[int] = None,
        agility: Optional[int] = None,
        luck: Optional[int] = None,
    ) -> "Attributes":
        return Attributes(
            strength=strength or self.strength,
            charisma=charisma or self.charisma,
            intelligence=intelligence or self.intelligence,
            agility=agility or self.agility,
            luck=luck or self.luck,
        )

    def copy_from_attributes(self, attributes: Optional["Attributes"]) -> "Attributes":
        """
        Wrapper for copy_with() method. If attributes is None, returns self,
        otherwise pass attributes to copy_with().

        Difference between copy_with() and copy_from_attributes() is that
        copy_with() requires all arguments to be passed, while copy_from_attributes()
        only requires attributes to be passed. For easy copying.
        """
        if attributes is None:
            return self

        return self.copy_with(
            strength=attributes.strength,
            charisma=attributes.charisma,
            intelligence=attributes.intelligence,
            agility=attributes.agility,
            luck=attributes.luck,
        )

    def dict(self, *, use_short_names: bool = True) -> dict[Attribute | str, int]:
        return {
            attribute.value
            if use_short_names
            else attribute.name: getattr(self, attribute.name.lower())
            for attribute in Attribute.all()
        }

    def __repr__(self) -> str:
        return f"Attributes({self.dict()})"
