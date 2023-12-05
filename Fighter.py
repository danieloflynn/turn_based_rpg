from Creatures import Creature
from time import sleep


class Fighter(Creature):
    """Figher class. Inherits from Creature class.

    Class Attributes:
    - default_attributes (dict[str, int]): Default abilities for this class, to be used if none supplied in constructor.


    Instance Attributes:
    - Same as Creature class

    Methods:
    - secondary_attack: Secondary attack released in a flurry of attacks. Has a 3 point attack penalty.
    - auto_select: Selects target from list of targets with highest HP.
    - turn: Turn logic for creature. Releases a flurry of strikes. One regular attack and two secondary attacks.

    """

    default_abilities = {
        "attack": 5,
        "defence": 8,
        "speed": 5
    }

    def __init__(self, name: str, hp: int = 50, abilities: dict[str, int] = default_abilities):
        """Constructor for Fighter. Essentially the same as Creature except higher default health and different default abilities.

        Args:
            name (str): Name of Figher.
            hp (int, optional): Starting/Max HP of Fighter. Defaults to 200.
            abilities (_type_, optional): Dictionary containing the abilities of the Fighter (attack, defence, and speed).. Defaults to default_abilities.
        """
        Creature.__init__(self, name, hp, abilities)

    def secondary_attack(self, target: Creature):
        """Secondary attack for figher. Reduces attack ability by 3 points for the duration of the attack.

        Args:
            target (Creature): Target to attack.
        """
        if not target:  # If no target return
            return

        self.abilities["attack"] -= 3  # Reduce attack by 3 points temporarily
        self.attack(target)  # Attack target
        self.abilities["attack"] += 3  # Increase attack again.

    def auto_select(self, target_list: list[Creature]):
        """Selects the alive target from the target list with the highest health. Choice done depending on mode selected
            Returns None if no targets alive.


        Args:
            target_list (list[Creature]): List of targets.

        Returns:
            Creature: Target that was selected.
        """
        alive_targets = self.get_alive(target_list)  # Get alive targets

        if not alive_targets:  # If no alive targets, return
            return

        # Return alive target with max life
        return max(alive_targets, key=lambda creature: creature.check_life())

    def turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):
        """Take turn for Fighter. Releases a flurry of blows (1 regular attack followed by 2 secondary attacks with 3 pt penalty).

        Args:
            round_num (int): Current round number. Not used but included for sake of polymorphism.
            target_list (list[Creature]): List of targets.
            allies (list[Creature], optional): List of allies. This has no function here but is included for the sake of polymorphism. Defaults to None.
        """
        self.sleep_print(f"{self.get_name()} unleashes a flurry of strikes")
        target = self.auto_select(target_list)  # Select target with highest HP

        if not target:  # If no alive target, return.
            return

        self.attack(target)  # Regular attack

        for _ in range(2):  # 2 secondary attacks
            if target.check_life() == 0:  # If current target dead, pick a new one before continuing
                target = self.auto_select(target_list)

            # Secondary attack with 3 pt penalty.
            self.secondary_attack(target)
