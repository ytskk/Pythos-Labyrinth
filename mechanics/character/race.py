import enum
import random

from lib.readable import Readable
from mechanics.character.attributes import Attributes, Attribute


class Race(Readable):
    BASE_HEALTH: int = 100

    @property
    def name(self) -> str:
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
        Returns the coefficient of the attribute.
        """
        di = self.attributes_coefficient().dict(use_short_names=False)
        return di.get(attribute.name, 1)

    def attributes_coefficient(self) -> Attributes:
        """
        Returns the coefficients of attributes.
        """
        return Attributes(
            strength=1,
            charisma=1,
            intelligence=1,
            agility=1,
            luck=1,
        )

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Race({self.name})"


class Ascenag(Race):
    """
    The Ascenag have lots of talents and can do lots of things. They're good at changing and
    doing well in different roles. They're also known for being brave and determined,
    and not giving up easily. The Ascenag are well-rounded, with strengths and weaknesses
    in all areas. They're good at fighting, using magic and being stealthy, and they
    can do well in any role they choose.
    """

    @property
    def name(self) -> str:
        return "Ascenag"


class Seraphim(Race):
    """
    Seraphim have a natural aptitude for magic, and they are the most skilled spellcasters
    in the game world. They are also agile and fast, making them difficult to defeat in combat.
    Seraphs are also known for their intelligence and wisdom and are skilled at diplomacy and negotiation.
    """

    BASE_HEALTH: int = 80

    @property
    def name(self) -> str:
        return "Seraphim"


class Durrok(Race):
    """
    They can hack traps to avoid taking damage, and they can peek through doors.
    """

    BASE_HEALTH: int = 120

    @property
    def name(self) -> str:
        return "Durrok"


class Scrof(Race):
    """
    The most fearsome of the four races, with a natural talent for physical combat.
    They have the highest resistance to magical attacks and curses. Because of their
    unprecedented strength, they can overlook the effects of traps.
    """

    BASE_HEALTH: int = 150

    @property
    def name(self) -> str:
        return "Scrof"


class Races(Race, enum.Enum):
    """
    Ascenag, Seraphim, Durrok, Scrof
    """

    ASCENAG = Ascenag
    SERAPHIM = Seraphim
    DURROK = Durrok
    SCROF = Scrof

    @property
    def new(self):
        return self.value()

    @classmethod
    def random(cls) -> Race:
        return random.choice(list(cls)).new

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Race({self.value})"
