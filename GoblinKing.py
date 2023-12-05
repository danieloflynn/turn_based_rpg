from Goblin import Goblin
from Archer import Archer
from Creatures import Creature


class GoblinKing(Goblin, Archer):
    def __init__(self, name, hp=50, abilities: dict[str, int] = Goblin.default_abilities, powerup_abilities: dict[str, int] = Archer.default_powerup):
        Goblin.__init__(self, name, hp, abilities)
        self.powerup_abilities = powerup_abilities
        self.powerUp = 0

    def attack(self, target: Creature):
        Archer.attack(self, target)
