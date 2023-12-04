from Creatures import Creature
from random import randint


class Wizard(Creature):
    default_abilities = {
        "attack": 3,
        "defence": 5,
        "speed": 5,
        "arcana": 10
    }

    def __init__(self, name: str, hp: int = 20, abilities: dict = default_abilities, player=False):
        Creature.__init__(self, name, hp, abilities)
        self.max_mana = 100
        self.mana = self.max_mana
        self.player = player

    def get_mana(self):
        return self.mana

    def increase_mana(self, points: int):
        print(f"Mana +{points}")
        if self.get_mana() + points > self.max_mana:
            self.mana = self.max_mana

        else:
            self.mana += points

    def decrease_mana(self, points: int) -> bool:
        if points > self.get_mana():
            print(f"{self.get_name()} does not have enough mana.")
            return False
        print(f"Mana -{points}")
        self.mana -= points
        return True

    def get_arcana(self):
        return self.abilities["arcana"]

    def attack(self, target: Creature):
        Creature.attack(self, target)
        self.increase_mana(20)

    def recharge(self):
        print(f"{self.get_name()} channels magic energy...")
        self.increase_mana(30)
        print(f"{self.get_name()}'s mana is now {self.mana}.")

    def fire_bolt(self, target: Creature):
        print(f"{self.get_name()} casts fire bolt on {target.get_name()}")
        roll = randint(1, 20)
        roll += self.get_arcana()//2

        if roll > target.get_defence() + target.get_speed():
            damage = randint(1, self.get_arcana())
            print(f"Fire bolt hits for {damage} damage.")
            target.reduce_life(damage)
            self.increase_mana(10)
        else:
            print("Fire bolt misses.")

    def heal(self, target: Creature):
        print(f"{self.get_name()} attempts to heal {target.get_name()}.")
        if not self.decrease_mana(20):
            return
        if target.check_life() == 0:
            print(f"{target.get_name()} is dead and cannot be revived.")
            return
        target.increase_health(randint(1, 8) + self.get_arcana()//2)

    def mass_heal(self, allies: list[Creature]):
        print(f"{self.get_name()} attempts to heal all allies")
        if not self.decrease_mana(30):
            return
        healing = randint(1, 10) + self.get_arcana()
        for ally in allies:
            if ally.check_life() != 0:
                ally.increase_health(healing)

    def fire_storm(self, enemies: list[Creature]):
        if not self.decrease_mana(50):
            return
        roll = randint(1, 20)
        roll += self.get_speed()

        if roll >= self.get_arcana():
            print(f"{self.get_name()} takes {roll//2} damage.")
            self.reduce_life(roll//2)
        else:
            print(f"{self.get_name()} takes {roll} damage.")
            self.reduce_life(roll)

        for enemy in enemies:
            roll = randint(5, 20)
            roll += self.get_arcana()
            print(f"{enemy.get_name()} takes {roll} damage.")
            enemy.reduce_life(roll)

    def select_target(self, target_list: list[Creature]):
        alive_targets = self.get_alive(target_list)
        if not alive_targets:
            return

        choice = -1

        while not (0 <= choice < len(alive_targets)):
            print("Select target:")
            for i, target in enumerate(alive_targets):
                print(f"{i+1}: {target}")
            choice = input("Enter choice: ")

            try:
                choice = int(choice) - 1
            except:
                print("Error, invalid input.")
                choice = -1

            if not (0 <= choice < len(alive_targets)):

                print(
                    f"Error, please enter a number between 1 and {len(alive_targets)}")
        return alive_targets[choice]

    def player_turn(self, round_num: int, target_list: list[Creature], allies=None):
        alive_targets = self.get_alive(target_list)

        if not alive_targets:
            return
        print("=====================================")
        print(self)
        print("Allies:")
        alive_allies = self.get_alive(allies)
        if alive_allies:
            for ally in alive_allies:
                print(ally)
        else:
            print("None.")
        print("=====================================")
        print("Actions. F: Attack R: Recharge Mana")
        print("Spells. 1: Heal 2: Firebolt 3: Mass Heal 4: Fire Storm")
        print("To Quit game type: Quit")
        print("=====================================")
        input_valid = False

        while not input_valid:
            user_input = input("Enter action: ").toLower()
            # TODO: Continue here

    def turn(self, round_num: int, target_list: list[Creature], allies=None):
        if self.player:
            self.player_turn(round_num, target_list)
        else:
            Creature.turn(self, round_num, target_list)

    def __str__(self):
        if self.player:
            return f"Player {self.get_name()} HP: {self.HP}/{self.maxHP} Mana: {self.get_mana()}/{self.max_mana}"

        return f"{self.get_name()} HP: {self.HP}/{self.maxHP} Mana: {self.get_mana()}/{self.max_mana}"
