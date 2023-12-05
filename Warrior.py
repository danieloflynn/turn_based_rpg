from Creatures import Creature
from time import sleep


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
        Creature.__init__(self, name, hp, abilities)
        self.shield_abilities = shield_abilities
        self.isShieldUp = 0

    def shield_up(self):
        if not self.isShieldUp:
            self.sleep_print(f"{self.get_name()} puts their shield up.")
            self.isShieldUp = 1
            self.abilities["attack"] += self.shield_abilities["attack"]
            self.abilities["defence"] += self.shield_abilities["defence"]

    def shield_down(self):
        if self.isShieldUp:
            self.sleep_print(f"{self.get_name()} puts their shield down.")
            self.isShieldUp = 0
            self.abilities["attack"] -= self.shield_abilities["attack"]
            self.abilities["defence"] -= self.shield_abilities["defence"]

    def turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):
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
