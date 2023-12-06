from Creatures import Creature


class Warrior(Creature):
    """Archer class. Inherits from Creature class

    Class Attributes:
    - default_attributes (dict[str, int]): Default attributes for this class, to be used if none supplied in constructor.
    - default_shield (dict[str, int]): Default shield attributes for this class, to be used as shield_abilities if none supplied in constructor.

    Instance Attributes:
    - shield_abilities(dict[str, int], optional): abilities (_type_, optional): Dictionary containing the abilities of the Warrior (attack, defence, and speed). Defaults to Warrior default_shield.
    - isShieldUp (bool) - Flag variable to check if shield up buff is applied.

    Methods:
    - shield_up: Puts the shield up if not already. If shield put up will add shield_abilities buff to abilities.
    - shield_down:Puts the shield down if not already. If shield up will remove shield_abilities buff to abilities.
    - auto_select: Automatically selects target, given target list. See function for further details.
    - turn: Turn function for Warrior. See function for further details


    """
    default_abilities = {
        "attack": 5,
        "defence": 10,
        "speed": 4
    }

    default_shield = {
        "attack": -4,
        "defence": 4,
        "speed": 0
    }

    def __init__(self, name: str, hp: int = 50, abilities=default_abilities, shield_abilities=default_shield):
        """Constructor for Warrior. Essentially the same as Creature except different default health and uses shield abilities.

        Args:
            name (str): Name of Warrior.
            hp (int, optional): Starting/Max HP of Warrior. Defaults to 50.
            abilities (dict[str, int], optional): Dictionary containing the abilities of the Warrior (attack, defence, and speed).. Defaults to default_abilities.
            shield_abilities (dict[str, int], optional): Dictionary containing the shield_up abilities of the Warrior (attack, defence, and speed).. Defaults to default_shield.
        """
        Creature.__init__(self, name, hp, abilities)
        self.shield_abilities = shield_abilities
        self.isShieldUp = 0

    def shield_up(self):
        """Puts the shield up if shield currently down. If shield put up, shield_abilities buff added to abilities.
        """
        if not self.isShieldUp:
            self.sleep_print(f"{self.get_name()} puts their shield up.")
            self.isShieldUp = 1
            self.abilities["attack"] += self.shield_abilities["attack"]
            self.abilities["defence"] += self.shield_abilities["defence"]

    def shield_down(self):
        """Puts the shield down if shield currently up. If shield put down, shield_abilities buff removed from abilities.
        """
        if self.isShieldUp:
            self.sleep_print(f"{self.get_name()} puts their shield down.")
            self.isShieldUp = 0
            self.abilities["attack"] -= self.shield_abilities["attack"]
            self.abilities["defence"] -= self.shield_abilities["defence"]

    def turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):
        """Turn logic for Warrior. Goes in round robin style:
            Round 1: Fighter attacks target and uses shield_up.
            Round 2-3: Attacks target regularly.
            Round 4: Uses shield_down and attacks target.

        Args:
            round_num (int): Current round number.
            target_list (list[Creature]): List of targets.
            allies (list[Creature], optional): List of allies. This has no function here but is included for the sake of polymorphism. Defaults to None.
        """
        target = self.auto_select(target_list)
        if target:
            match round_num % 4:
                case 0:
                    self.shield_down()
                    self.attack(target)
                case 1:
                    self.attack(target)
                    self.shield_up()
                case _:
                    self.attack(target)
