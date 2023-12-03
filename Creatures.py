from random import randint


class Creature:
    default_abilities = {
        "attack": 1,
        "defence": 5,
        "speed": 5
    }

    def __init__(self, name: str, hp: int = 10, abilities=default_abilities):
        self.name = name
        self.HP = hp
        self.maxHP = hp
        self.abilities = abilities

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
            print(f"{self.get_name()} fainted.")
        else:
            self.HP -= points

    def attack(self, target):
        print(f"{self.get_name()} attacks {target.get_name()}")
        roll = randint(1, 20)
        if roll > target.get_defence() + target.get_speed():
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
        return alive_targets[rand]

    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        if target:
            self.attack(target)

    def __str__(self):
        return f"{self.name}, health: {self.check_life()}"

    def __repr__(self):
        return self.__str__()


class Goblin(Creature):
    default_abilities = {
        "attack": 3,
        "defence": 6,
        "speed": 3
    }

    def __init__(self, name: str, hp: int = 15, abilities=default_abilities):
        super().__init__(self, name, hp, abilities)


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
            self.inRage == 1

        super().attack(target)

    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        if target:
            if round_num % 4 != 0:
                self.attack(target)
            else:
                self.heavy_attack(target)
