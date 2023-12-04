from Creatures import Creature
from random import randint


class Wizard(Creature):
    default_abilities = {
        "attack": 3,
        "defence": 5,
        "speed": 5,
        "arcana": 10
    }

    def __init__(self, name: str, hp: int, abilities: dict = default_abilities):
        Creature.__init__(self, name, hp, abilities)
        self.max_mana = 100
        self.mana = self.max_mana

    def get_mana(self):
        return self.mana

    def increase_mana(self, points: int):
        if self.get_mana() + points > self.max_mana:
            self.mana = self.max_mana

        else:
            self.mana += points

    def decrease_mana(self, points: int) -> bool:
        if points > self.get_mana():
            print(f"{self.get_name()} does not have enough mana.")
            return False
        self.mana -= points
        return True

    def attack(self, target: Creature):
        Creature.attack(self, target)
        self.increase_mana(20)

    def recharge(self):
        print(f"{self.get_name()} is recharging")
        self.increase_mana(30)
        print(f"{self.get_name()}'s mana is now {self.mana}.")

    def fire_bolt(self, target: Creature):
        print(f"{self.get_name()} casts fire bolt on {target.get_name()}")
        roll = randint(1, 20)
        roll += self.abilities["arcana"]//2

        if roll > target.get_defence() + target.get_speed():
            print("Fire bolt hits.")
            damage = randint(1, self.abilities["arcana"])
            self.increase_mana(10)
        else:
            print("Fire bolt misses.")

    def heal(self, target: Creature):
        print(f"{self.get_name()} attempts to heal {target.get_name}.")
        if not self.decrease_mana(20):
            return
        if target.check_life() == 0:
            print(f"{target.get_name()} is dead and cannot be revived.")
            return
        target.increase_health(randint(1, 8) + self.abilities["arcana"]//2)

    def mass_heal(self, allies: list(Creature)):
        print(f"{self.get_name} attempts to heal all allies")
        if not self.decrease_mana(30):
            return
        healing = randint(1, 10) + self.abilities["arcana"]
        for ally in allies:
            if ally.check_life() != 0:
                ally.increase_health(healing)

    def fire_storm(self, enemies):
        pass
