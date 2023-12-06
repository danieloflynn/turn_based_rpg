from Orc import Orc
from Warrior import Warrior
from Creatures import Creature


class OrcGeneral(Orc, Warrior):
    """OrcGeneral class. Inherits from Orc and Warrior

    Instance Attributes:
    - shield_abilities(dict[str, int], optional): abilities (_type_, optional): Dictionary containing the abilities of the Warrior (attack, defence, and speed). Defaults to Warrior default_shield.
    - isShieldUp (bool) - Flag variable to check if shield up buff is applied.

    """

    def __init__(self, name: str, hp: int = 80, abilities: dict[str, int] = Orc.default_abilities, rage_abilities: dict[str, int] = Orc.default_rage, shield_abilities=Warrior.default_shield):
        """Constructor for OrcGeneral. Essentially the same as Orc except different default health and uses Warrior's default shield abilities.

        Args:
            name (str): Name of OrcGeneral.
            hp (int, optional): Starting/Max HP of OrcGeneral. Defaults to 50.
            abilities (dict[str, int], optional): Dictionary containing the abilities of the OrcGeneral (attack, defence, and speed).. Defaults to default_abilities.
            shield_abilities (dict[str, int], optional): Dictionary containing the shield_up abilities of the OrcGeneral (attack, defence, and speed).. Defaults to Warrior default_shield.
        """
        Orc.__init__(self, name, hp, abilities, rage_abilities)
        self.shield_abilities = shield_abilities
        self.isShieldUp = False

    def turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):
        """Turn logic for OrcGeneral. Goes round robin style.
            Round 1: Attacks target and uses shield_up.
            Round 2: attacks normally.
            Round 3: Uses shield_down and attacks.
            Round 4: Uses heavy_attack on target.

        Args:
            round_num (int): _description_
            target_list (list[Creature]): _description_
            allies (list[Creature], optional): _description_. Defaults to None.
        """
        target = self.auto_select(target_list)
        if target:
            match round_num % 4:
                case 0:
                    self.heavy_attack(target)
                case 1:
                    self.attack(target)
                    self.shield_up()
                case 2:
                    self.attack(target)
                case 3:
                    self.shield_down()
                    self.attack(target)
