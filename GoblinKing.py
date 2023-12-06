from Goblin import Goblin
from Archer import Archer
from Creatures import Creature
from time import sleep


class GoblinKing(Goblin, Archer):
    """Goblin King Class. Inherits from Goblin and Archer.
    Instance Attributes:
    - powerup_abilities: (dict[str, int], optional): abilities (_type_, optional): Dictionary containing the abilities of the Archer (attack, defence, and speed). Defaults to archer default_powerup.
    - powerUp (bool): Flag variable. Used to check if GoblinKing is in power up/down state

    Methods:
    - attack: Attacks the same as Archer parent class.
    """

    def __init__(self, name, hp=50, abilities: dict[str, int] = Goblin.default_abilities, powerup_abilities: dict[str, int] = Archer.default_powerup):
        """Constructor for GoblinKing. Essentially the same as Goblin except different default health and uses Archer's default powerup.

        Args:
            name (str): Name of GoblinKing.
            hp (int, optional): Starting/Max HP of Goblin. Defaults to 50.
            abilities (_type_, optional): Dictionary containing the abilities of the GoblinKing (attack, defence, and speed).. Defaults to default_abilities.
            powerup_abilities (_type_, optional): Dictionary containing the powerup abilities of the GoblinKing (attack, defence, and speed).. Defaults to archer default_powerup.
        """
        Goblin.__init__(self, name, hp, abilities)
        self.powerup_abilities = powerup_abilities
        self.powerUp = 0

    def attack(self, target: Creature):
        """Attack of GoblinKing. Uses same logic as Archer

        Args:
            target (Creature): _description_
        """
        Archer.attack(self, target)
