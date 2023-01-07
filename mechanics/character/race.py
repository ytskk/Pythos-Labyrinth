import enum
import random

from lib.readable import Readable
from mechanics.character.attributes import Attributes


class Race(Readable):
    @property
    def name(self) -> str:
        """
        Returns string representation of race name.
        """
        return "Race"

    def basic_attributes(self) -> Attributes:
        """
        Returns the basic attributes of the race.
        """
        ...

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

    def basic_attributes(self) -> Attributes:
        return Attributes(
            strength=2,
            charisma=2,
            intelligence=2,
            agility=2,
            luck=5,
        )


class Seraphim(Race):
    """
    Seraphim have a natural aptitude for magic, and they are the most skilled spellcasters
    in the game world. They are also agile and fast, making them difficult to defeat in combat.
    Seraphs are also known for their intelligence and wisdom and are skilled at diplomacy and negotiation.
    """

    @property
    def name(self) -> str:
        return "Seraphim"

    def basic_attributes(self) -> Attributes:
        return Attributes(
            strength=1,
            charisma=3,
            intelligence=5,
            agility=2,
            luck=3,
        )


class Durrok(Race):
    """
    They can hack traps to avoid taking damage, and they can peek through doors.
    """

    @property
    def name(self) -> str:
        return "Durrok"

    def basic_attributes(self) -> Attributes:
        return Attributes(
            strength=4,
            charisma=2,
            intelligence=2,
            agility=5,
            luck=2,
        )


class Scrof(Race):
    """
    The most fearsome of the four races, with a natural talent for physical combat.
    They have the highest resistance to magical attacks and curses. Because of their
    unprecedented strength, they can overlook the effects of traps.
    """

    @property
    def name(self) -> str:
        return "Scrof"

    def basic_attributes(self) -> Attributes:
        return Attributes(
            strength=8,
            charisma=1,
            intelligence=1,
            agility=2,
            luck=1,
        )


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
