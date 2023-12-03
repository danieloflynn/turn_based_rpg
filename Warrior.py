from Creatures import Creature


class Warrior(Creature):
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
        super().__init__(name, hp, abilities)
        self.shield_abilities = shield_abilities
        self.isShieldUp = 0

    def get_attack(self):
        return self.abilities["attack"] + self.isShieldUp * self.shield_abilities["attack"]

    def get_defence(self):
        return self.abilities["defence"] + self.isShieldUp * self.shield_abilities["defence"]

    def get_speed(self):
        return self.abilities["speed"] + self.isShieldUp * self.shield_abilities["speed"]

    def shield_up(self):
        if not self.isShieldUp:
            print(f"{self.get_name()} puts their shield up.")
            self.isShieldUp = 1

    def shield_down(self):
        if self.isShieldUp:
            print(f"{self.get_name()} puts their shield down.")
            self.isShieldUp = 0
