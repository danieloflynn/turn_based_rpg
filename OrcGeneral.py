from Orc import Orc
from Warrior import Warrior


class OrcGeneral(Orc, Warrior):
    def __init__(self, name: str, hp: int = 80, abilities=Orc.default_abilities, rage_abilities=Orc.default_rage, shield_abilities=Warrior.default_shield):
        Orc.__init__(self, name, hp, abilities, rage_abilities)
        self.shield_abilities = shield_abilities
        self.isShieldUp = 0
