from random import randint


class Creature:
    maxHP = 10

    def __init__(self, name: str):
        self.name = name
        self.HP = Creature.maxHP
        self.abilities = {
            "attack": 1,
            "defence": 5,
            "speed": 5
        }

    def get_name(self):
        return self.name

    def check_life(self):
        return self.HP

    def get_attack(self):
        return self.abilities["attack"]

    def get_defence(self):
        return self.abilities["defence"]

    def get_speed(self):
        return self.abilities["speed"]

    def reduce_life(self, points: int):
        if self.HP < points:
            self.HP = 0
        else:
            self.HP -= points

    def attack(self, target):
        print(f"{self.get_name()} attacks {target.get_name()}")
        roll = randint(1, 20)
        if roll > target.get_defence() + target.get_speed:
            bonus = randint(1, 4)
            damage = self.get_attack() + bonus
            print(f"Attack hits for {damage} damage!")
            target.reduce_life(damage)
        else:
            print("Atack missed...")

    def auto_select(self, target_list):
        alive_targets = []
        for target in target_list:
            if target.check_life() != 0:
                alive_targets += [target]

        if len(alive_targets) == 0:
            return

        rand = randint(0, len(alive_targets)-1)
        # TODO: Make sure this actually returns the target class, not a new instance
        return alive_targets[rand]

    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        self.attack(target)
