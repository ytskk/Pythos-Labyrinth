import enum
import random

from lib.readable import Readable
from mechanics.character.attributes import Attributes, Attribute


class Race(Readable):
    BASE_HEALTH: int = 100

    @staticmethod
    def name() -> str:
        """
        Returns string representation of race name.
        """
        return "Race"

    @property
    def base_health(self) -> int:
        """
        Returns the base health for the race.
        """
        return self.BASE_HEALTH

    def basic_attributes(self) -> Attributes:
        """
        Returns the basic attributes of the race.

        By default all is 40.
        """
        return Attributes(
            strength=40,
            charisma=40,
            intelligence=40,
            agility=40,
            luck=40,
        )

    def attribute_coefficient(self, attribute: Attribute) -> int:
        """
        Returns the coefficient for the specified attribute.

        Args:
            attribute: The attribute to get coefficient for. Defaults to 1.
        """
        attrs = self.attributes_coefficient().dict(use_short_names=False)

        return attrs.get(attribute.name, 1)

    def attributes_coefficient(self) -> Attributes:
        """
        Returns the coefficients of all attributes.
        """
        return Attributes(
            strength=1,
            charisma=1,
            intelligence=1,
            agility=1,
            luck=0,
        )


class Ascenag(Race):
    @staticmethod
    def name() -> str:
        return "Ascenag"


class Seraphim(Race):
    @staticmethod
    def name() -> str:
        return "Seraphim"


class Durrok(Race):
    @staticmethod
    def name() -> str:
        return "Durrok"


class Scrof(Race):
    @staticmethod
    def name() -> str:
        return "Scrof"


class Races(Race, enum.Enum):
    """
    Ascenag, Seraphim, Durrok, Scrof
    """

    ASCENAG = Ascenag
    SERAPHIM = Seraphim
    DURROK = Durrok
    SCROF = Scrof

    def new(self):
        return self.value()

    @classmethod
    def all(cls) -> list["Races"]:
        return list(cls)

    @classmethod
    def random(cls) -> Race:
        return random.choice(cls.all()).new()
