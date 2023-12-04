from Goblin import Goblin
from Archer import Archer


class GoblinKing(Goblin, Archer):
    def __init__(self, name, hp=50, abilities=Goblin.default_abilities, powerup_abilities=Archer.default_powerup):
        Goblin.__init__(self, name, hp, abilities)
        self.powerup_abilities = powerup_abilities
        self.powerUp = 0

    def attack(self, target):
        Archer.attack(self, target)
