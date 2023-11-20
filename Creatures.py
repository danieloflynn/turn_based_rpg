from random import randint


class Creature:
    maxHP = 10

    def __init__(self, name: str):
        self.name = name
        self.HP = Creature.maxHP
        self.abilities = {
            "Attack": 1,
            "Defence": 5,
            "Speed": 5
        }

    def check_life(self):
        return self.HP

    def get_attack(self):
        return self.abilities.Attack

    def get_defence(self):
        return self.abilities.Defence

    def get_speed(self):
        return self.abilities.Speed

    def reduce_life(self, points: int):
        if self.HP < points:
            self.HP = 0
        else:
            self.HP -= points

    def attack(self, target):
        roll = randint(1, 20)
        if roll > target.get_defence() + target.get_speed:
            bonus = randint(1, 4)
            target.reduce_life(self.get_attack() + bonus)

    def auto_select(self, target_list):
        alive_targets = []
        for target in target_list:
            if target.check_life() != 0:
                alive_targets += [target]

        if len(alive_targets) == 0:
            return

        rand = randint(0, len(alive_targets)-1)

        alive_targets
