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
        self.name = name
        self.HP = hp
        self.maxHP = hp
        self.abilities = abilities
        self.rage_abilities = rage_abilities
        self.inRage = 0

    def get_attack(self):
        return self.abilities["attack"] + self.inRage * self.rage_abilities["attack"]

    def get_defence(self):
        return self.abilities["defence"] + self.inRage * self.rage_abilities["defence"]

    def get_speed(self):
        return self.abilities["speed"] + self.inRage * self.rage_abilities["speed"]

    def attack(self, target):
        if self.inRage == 1:
            print(f"{self.name} cooled down.")
            self.inRage = 0

        super().attack(target)

    def heavy_attack(self, target):
        if self.inRage == 0:
            print(f"{self.name} is in rage.")
            self.inRage = 1

        super().attack(target)

    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        if target:
            if round_num % 4 != 0:
                self.attack(target)
            else:
                self.heavy_attack(target)
