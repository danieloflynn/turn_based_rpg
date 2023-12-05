from Orc import Orc
from Creatures import Creature


class Boss(Orc):
    """Boss Class. Inherits from Orc.

    Class Attributes:
    - default_attributes (dict[str, int]): Default attributes for this class, to be used if none supplied in constructor.

    Instance Attributes:
    All inherited from Orc.

    Methods:
    - auto_select: Selects the strongest, weakest, or a random target depending on mode supplied. Chooses target from target list. 
    - turn: Turn function for Boss. See function for further details.
    """

    default_abilities = {
        "attack": 5,
        "defence": 8,
        "speed": 5
    }

    def __init__(self, name: str, hp=200, abilities=default_abilities, rage_abilities=Orc.default_rage):
        """Constructor for Boss. Essentially the same as Orc except higher default health and different default abilities.

        Args:
            name (str): Name of Boss.
            hp (int, optional): Starting/Max HP of Boss. Defaults to 200.
            abilities (_type_, optional): Dictionary containing the abilities of the Archer (attack, defence, and speed).. Defaults to default_abilities.
            rage_abilities (_type_, optional): Dictionary containing the rage abilities of the Archer (attack, defence, and speed).. Defaults to Orc.default_rage.
        """
        Orc.__init__(self, name, hp, abilities, rage_abilities)

    def auto_select(self, target_list: list[Creature], mode) -> Creature:
        """Auto selects an alive target from the target list (alive or not alive). Choice done depending on mode selected
            Returns None if no targets alive.


        Args:
            target_list (list[Creature]): List of targets.
            mode (_type_): Selection mode. If "Strong", selects target with highest HP, if "Weak", selects target with lowest HP, If "Random", selects random alive target.

        Returns:
            Creature: Target that was selected.
        """
        alive_targets = self.get_alive(target_list)  # Get alive targets
        if not alive_targets:  # If none alive return
            return

        match mode:
            case 'Strong':  # If mode is strong select Creature with highest HP
                return max(alive_targets, key=lambda creature: creature.check_life())
            case 'Weak':  # If mode is weak select Creature with min HP that is
                return min(alive_targets, key=lambda creature: creature.check_life())
            case 'Random':  # If random use same functionality as parent class
                return Orc.auto_select(self, target_list)

    def turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):
        """Take turn for Archer. Goes in round robin style. 
            Round 1: Attack strongest target with a succession of 3 attacks. If target faints pick another. 
            Round 2-4: Regular attack. Pick weakest target.

        Args:
            round_num (int): Current round number.
            target_list (list[Creature]): List of targets.
            allies (list[Creature], optional): List of allies. This has no function here but is included for the sake of polymorphism. Defaults to None.
        """
        if round_num % 4 == 1:  # If round 1, 5 etc. pick strongest player and attack with 3 attacks
            target = self.auto_select(target_list, "Strong")
            for _ in range(3):
                if target.check_life() == 0:  # If target is dead pick a random one
                    target = self.auto_select(target_list, "Random")
                self.attack(target)
        else:  # Rest of the time pick the weakest target
            target = self.auto_select(target_list, "Weak")
            self.heavy_attack(target)
