from Creatures import Creature


class Goblin(Creature):
    default_abilities = {
        "attack": 3,
        "defence": 6,
        "speed": 3
    }

    def __init__(self, name: str, hp: int = 15, abilities=default_abilities):
        super().__init__(name, hp, abilities)
