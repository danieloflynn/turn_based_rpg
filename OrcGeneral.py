from Orc import Orc
from Warrior import Warrior
from Creatures import Creature


class OrcGeneral(Orc, Warrior):
    def __init__(self, name: str, hp: int = 80, abilities=Orc.default_abilities, rage_abilities=Orc.default_rage, shield_abilities=Warrior.default_shield):
        Orc.__init__(self, name, hp, abilities, rage_abilities)
        self.shield_abilities = shield_abilities
        self.isShieldUp = 0

    def turn(self, round_num: int, target_list: list[Creature]):
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
