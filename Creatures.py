from random import randint
# TODO: Make variables private
# TODO: Make PowerCreature class


class Creature:
    # Define default abilities to be used if none specified
    default_abilities = {
        "attack": 1,
        "defence": 5,
        "speed": 5
    }

    def __init__(self, name: str, HP: int = 10, abilities=default_abilities):
        self.name = name
        self.HP = HP
        self.maxHP = HP
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

    def heal(self, points: int):
        if self.HP + points > self.maxHP:
            self.HP = self.maxHP
        else:
            self.HP += points
        print(f"{self.get_name()} is healed by {points} points.")
        print(f"{self.get_name()}'s health is now {self.check_life()}.")

    def attack(self, target):
        # TODO: if health is 0, don't allow attack
        print(f"{self.get_name()} attacks {target.get_name()}")
        roll = randint(1, 20)
        if roll > target.get_defence() + target.get_speed():
            bonus = randint(1, 4)
            damage = self.get_attack() + bonus
            print(f"Attack hits for {damage} damage!")
            target.reduce_life(damage)
        else:
            print("Atack missed...")

    def get_alive(self, target_list: list):
        """Gets the list of alive creatures from a target list

        Args:
            target_list (_list_): List of potential targets
        Returns:
            alive_targets: List of alive targets 
        """
        alive_targets = []
        for target in target_list:
            if target.check_life() != 0:
                alive_targets += [target]

        return alive_targets

    def auto_select(self, target_list):
        alive_targets = self.get_alive(target_list)

        if not alive_targets:
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
