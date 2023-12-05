from Creatures import Creature
from time import sleep


class Goblin(Creature):
    """Goblin Class. Inherits from Creature.
    Class Attributes:
    - default_attributes (dict[str, int]): Default attributes for this class, to be used if none supplied in constructor.
    """
    default_abilities = {
        "attack": 3,
        "defence": 6,
        "speed": 3
    }

    def __init__(self, name: str, hp: int = 15, abilities: dict[str, int] = default_abilities):
        """Constructor for Goblin. Essentially the same as Creature except different default health and different default abilities.

        Args:
            name (str): Name of Goblin.
            hp (int, optional): Starting/Max HP of Goblin. Defaults to 15.
            abilities (_type_, optional): Dictionary containing the abilities of the Goblin (attack, defence, and speed).. Defaults to default_abilities.
        """
        Creature.__init__(self, name, hp, abilities)
