from Creatures import Creature
from time import sleep


class Orc(Creature):
    """Orc class. Inherits from Creature class

    Class Attributes:
    - default_attributes (dict[str, int]): Default attributes for this class, to be used if none supplied in constructor.
    - default_rage (dict[str, int]): Default rage attributes for this class, to be used as rage_abilities if none supplied in constructor.

    Instance Attributes:
    - rage_abilities (dict[str, int]): To be added to abilities when Orc "powers up" i.e. when heacy_attack is used.
    - inRage (bool): Flag variable. Used to check if Orc is in rage.

    Methods:
    - attack: Same as normal attack. If in "rage" state will cool down, removing rage buff.
    - heavy_attack: if not in rage goes in rage (adds rage_abilities buff to abilities) and attacks like normal. 
    - turn: Turn function for Orc. See function for further details

    """
    default_abilities = {
        "attack": 5,
        "defence": 8,
        "speed": 3
    }

    default_rage = {
        "attack": 5,
        "defence": -3,
        "speed": 0
    }

    def __init__(self, name: str, hp: int = 50, abilities: dict[str, int] = default_abilities, rage_abilities: dict[str, int] = default_rage):
        """Constructor for Orc

        Args:
            name (str): Name of Orc
            hp (int, optional): Starting/Max HP of Orc. Defaults to 30.
            abilities (_type_, optional): Dictionary containing the abilities of the Orc (attack, defence, and speed). Defaults to default_abilities.
            rage_abilities (_type_, optional): Dictionary containing the buff abilities of the Orc (attack, defence, and speed). Defaults to default_rage.
        """
        Creature.__init__(self, name, hp, abilities)
        self.rage_abilities = rage_abilities
        self.inRage = 0

    def attack(self, target: Creature):
        """Attacks a given target. Powers Orc back down first if currently in rage. Otherwise functionality is same as Creature

        Args:
            target (Creature): Creature for the Orc to attack
        """
        if self.inRage:
            self.sleep_print(f"{self.get_name()} cooled down.")
            self.inRage = 0
            self.abilities["attack"] -= self.rage_abilities["attack"]
            self.abilities["defence"] -= self.rage_abilities["defence"]
        Creature.attack(self, target)

    def heavy_attack(self, target: Creature):
        """Puts Orc in rage if not already, and attacks target with powerful attack.
            When Orc goes into rage adds rage_abilities to abilities and setting inRage = 1 if not currently powered up. 

        Args:
            target (Creature): Creature to be attacked.
        """
        if not self.inRage:
            self.sleep_print(f"{self.get_name()} is in rage.")
            self.inRage = 1
            self.abilities["attack"] += self.rage_abilities["attack"]
            self.abilities["defence"] += self.rage_abilities["defence"]

        Creature.attack(self, target)

    def turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):
        """Take turn for Orc. Goes in round robin style. Round 1-3: normal attack. Round 4: Heavy attack.

        Args:
            round_num (int): Current round number.
            target_list (list[Creature]): List of targets.
            allies (list[Creature], optional): List of allies. This has no function here but is included for the sake of polymorphism. Defaults to None.
        """
        target = self.auto_select(target_list)
        if target:
            if round_num % 4 != 0:
                self.attack(target)
            else:
                self.heavy_attack(target)
