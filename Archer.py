from Creatures import Creature
from random import randint


class Archer(Creature):
    default_abilities = {
        "attack": 7,
        "defence": 9,
        "speed": 8
    }

    default_powerup = {
        "attack": 3,
        "defence": -3,
        "speed": 0
    }

    def __init__(self, name: str, hp: int = 30, abilities=default_abilities, powerup_abilities=default_powerup):
        super().__init__(name, hp, abilities)
        self.powerup_abilities = powerup_abilities
        self.powerUp = 0

    def get_attack(self):
        return self.abilities["attack"] + self.powerUp * self.powerup_abilities["attack"]

    def get_defence(self):
        return self.abilities["defence"] + self.powerUp * self.powerup_abilities["defence"]

    def get_speed(self):
        return self.abilities["speed"] + self.powerUp * self.powerup_abilities["speed"]

    def attack(self, target):
        if self.powerUp:
            print(f"{self.get_name()} is powering down...")
            self.powerUp = 0
        super().attack(target)

    def power_shot(self, target):
        if not self.powerUp:
            print(f"{self.get_name()} is powering up...")
            self.powerUp = 1
        print(f"{self.get_name()} attacks {target.get_name()} with power shot")
        roll = max(randint(1, 20), randint(1, 20))

        if self.get_speed() > target.get_speed():
            roll += self.get_speed() - target.get_speed()

        if roll > target.get_defence() + target.get_speed():
            bonus = randint(1, 8)
            damage = self.get_attack + bonus
            print(f"Attack hits for {damage} damage!")
            target.reduce_life(damage)
        else:
            print("Attack missed...")

    def auto_select(self, target_list):
        alive_targets = self.get_alive(target_list)

        if not alive_targets:
            return

        return min(alive_targets, lambda creature: creature.check_life())

    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)

        if target:
            match round_num % 4:
                case 1:
                    self.attack(target)
                case _:
                    self.power_shot(target)
