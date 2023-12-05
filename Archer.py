from Creatures import Creature
from random import randint


class Archer(Creature):
    """Archer class. Inherits from Creature class

    Class Attributes:
    - default_attributes (dict[str, int]): Default attributes for this class, to be used if none supplied in constructor.
    - default_powerup (dict[str, int]): Default powerup attributes for this class, to be used as powerup_abilities if none supplied in constructor.

    Instance Attributes:
    - powerup_abilities (dict[str, int]): To be added to abilities when Archer "powers up" i.e. when power_shot is used.
    - powerUp (bool): Flag variable. Used to check if Archer is in power up/down state

    Methods:
    - attack: Same as normal attack. If in "powered up" state will power down, removing powerup buff.
    - power_shot: works like normal attack, except with better roll chances and bonuses. 
        Also adds powerup buff to current abilities (+3 attack -3 defence).
    - auto_select: Automatically selects target, given target list. See function for further details.
    - turn: Turn function for archer. See function for further details


    """
    default_abilities = {
        "attack": 7,
        "defence": 9,
        "speed": 8
    }

    default_powerup = {
        "attack": 3,
        "defence": -3,
        "speed": 0
    }

    def __init__(self, name: str, hp: int = 30, abilities: dict[str, int] = default_abilities, powerup_abilities: dict[str, int] = default_powerup):
        """Constructor for Archer

        Args:
            name (str): Name of Archer
            hp (int, optional): Starting/Max HP of Archer. Defaults to 30.
            abilities (_type_, optional): Dictionary containing the abilities of the Archer (attack, defence, and speed). Defaults to default_abilities.
            powerup_abilities (_type_, optional): Dictionary containing the buff abilities of the Archer (attack, defence, and speed). Defaults to default_powerup.
        """
        Creature.__init__(self, name, hp, abilities)
        self.powerup_abilities = powerup_abilities
        self.powerUp = 0

    def attack(self, target: Creature):
        """Attacks a given target. Powers Archer back down first if currently powered up. Otherwise functionality is same as Creature

        Args:
            target (Creature): Creature for the Archer to attack
        """
        if self.powerUp:  # If powered up, power down
            print(f"{self.get_name()} is powering down...")

            print(f"{self.get_name()}'s attack is reduced.")
            self.abilities["attack"] -= self.powerup_abilities["attack"]

            print(f"{self.get_name()}'s defence rises.")
            self.abilities["defence"] -= self.powerup_abilities["defence"]

            self.powerUp = 0

        Creature.attack(self, target)  # Attack using same function as Creature

    def power_shot(self, target: Creature):
        """Powers creature up, and attacks target with powerful attack.
            Adds powerup_abilities to abilities and setting powerUp = 1 if not currently powered up. 
            Attack: Roll is the highest of 2 rolls 1-20, adding the difference in speed between self and target if speed is greater. Bonus attack roll 1-8 

        Args:
            target (Creature): Creature to be attacked.
        """
        if not self.powerUp:  # If not powered up, power up
            print(f"{self.get_name()} is powering up...")

            print(f"{self.get_name()}'s attack rises.")
            self.abilities["attack"] += self.powerup_abilities["attack"]

            print(f"{self.get_name()}'s defence is reduced.")
            self.abilities["defence"] += self.powerup_abilities["defence"]

            self.powerUp = 1

        # Attack
        print(f"{self.get_name()} attacks {target.get_name()} with power shot")
        roll = max(randint(1, 20), randint(1, 20))  # Highest of 2 rolls

        if self.get_speed() > target.get_speed():  # Add speed to roll if speed greater than target
            roll += self.get_speed() - target.get_speed()

        # If roll > attack + speed of creature, attack hits.
        if roll > target.get_defence() + target.get_speed():
            bonus = randint(1, 8)  # Add bonus to damage
            damage = self.get_attack() + bonus
            print(f"Attack hits for {damage} damage!")
            target.reduce_life(damage)
        else:  # Else attack misses
            print("Attack missed...")

    def auto_select(self, target_list: list[Creature]):
        """Auto selects an alive target given a target list (alive and not alive). Picks alive target with the lowest health. If no targets are alive returns without attacking. 

        Args:
            target_list (list[Creature]): List of targets to be selected from. Targets can be alive and not alive.
        """
        alive_targets = self.get_alive(target_list)  # Get alive targets

        if not alive_targets:  # If no alive targets return
            return

        return min(alive_targets, key=lambda creature: creature.check_life())

    def turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):
        """Take turn for Archer. Goes in round robin style. Round 1: normal attack. Round 2-4: Power shot.

        Args:
            round_num (int): Current round number.
            target_list (list[Creature]): List of targets.
            allies (list[Creature], optional): List of allies. This has no function here but is included for the sake of polymorphism. Defaults to None.
        """

        target = self.auto_select(target_list)  # Auto select target
        if not target:  # If no targets, return without attacking
            return

        match round_num % 4:  # Round 1 - normal attack. Round 2-4 - heavy attack
            case 1:
                self.attack(target)
            case _:
                self.power_shot(target)
