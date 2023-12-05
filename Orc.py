from Creatures import Creature


class Orc(Creature):
    default_abilities = {
        "attack": 5,
        "defence": 8,
        "speed": 3
    }

    default_rage = {
        "attack": 5,
        "defence": -3,
        "speed": 0
    }

    def __init__(self, name: str, hp: int = 50, abilities=default_abilities, rage_abilities=default_rage):
        Creature.__init__(self, name, hp, abilities)
        self.rage_abilities = rage_abilities
        self.inRage = 0

    def attack(self, target):
        if self.inRage:
            print(f"{self.get_name()} cooled down.")
            self.inRage = 0
            self.abilities["attack"] -= self.rage_abilities["attack"]
            self.abilities["defence"] -= self.rage_abilities["defence"]
        Creature.attack(self, target)

    def heavy_attack(self, target):
        if not self.inRage:
            print(f"{self.get_name()} is in rage.")
            self.inRage = 1
            self.abilities["attack"] += self.rage_abilities["attack"]
            self.abilities["defence"] += self.rage_abilities["defence"]

        Creature.attack(self, target)

    def turn(self, round_num, target_list, allies=None):
        target = self.auto_select(target_list)
        if target:
            if round_num % 4 != 0:
                self.attack(target)
            else:
                self.heavy_attack(target)
