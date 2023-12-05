from Creatures import Creature
from random import randint


class Wizard(Creature):
    default_abilities = {
        "attack": 3,
        "defence": 5,
        "speed": 5,
        "arcana": 10
    }

    def __init__(self, name: str, hp: int = 20, abilities: dict = default_abilities, player: bool = False):
        Creature.__init__(self, name, hp, abilities)
        self.max_mana = 100
        self.mana = self.max_mana
        self.player = player

    def get_mana(self):
        return self.mana

    def increase_mana(self, points: int):
        self.sleep_print(f"Mana +{points}")
        if self.get_mana() + points > self.max_mana:
            self.mana = self.max_mana

        else:
            self.mana += points

    def decrease_mana(self, points: int) -> bool:
        if points > self.get_mana():
            self.sleep_print(f"{self.get_name()} does not have enough mana.")
            return False
        self.sleep_print(f"Mana -{points}")
        self.mana -= points
        return True

    def get_arcana(self):
        return self.abilities["arcana"]

    def attack(self, target: Creature):
        Creature.attack(self, target)
        self.increase_mana(20)

    def recharge(self):
        self.sleep_print(f"{self.get_name()} channels magic energy...")
        self.increase_mana(30)
        self.sleep_print(f"{self.get_name()}'s mana is now {self.mana}.")

    def fire_bolt(self, target: Creature):
        self.sleep_print(
            f"{self.get_name()} casts fire bolt on {target.get_name()}")
        roll = randint(1, 20)
        roll += self.get_arcana()//2

        if roll > target.get_defence() + target.get_speed():
            damage = randint(1, self.get_arcana())
            self.sleep_print(f"Fire bolt hits for {damage} damage.")
            target.reduce_life(damage)
            self.increase_mana(10)
        else:
            self.sleep_print("Fire bolt misses.")

    def heal(self, target: Creature):
        self.sleep_print(
            f"{self.get_name()} attempts to heal {target.get_name()}.")
        if not self.decrease_mana(20):
            return
        if target.check_life() == 0:
            self.sleep_print(
                f"{target.get_name()} is dead and cannot be revived.")
            return
        target.increase_life(randint(1, 8) + self.get_arcana()//2)

    def mass_heal(self, allies: list[Creature]):
        self.sleep_print(f"{self.get_name()} attempts to heal all allies")
        if not self.decrease_mana(30):
            return
        healing = randint(1, 10) + self.get_arcana()
        for ally in allies:
            if ally.check_life() != 0:
                ally.increase_life(healing)

    def fire_storm(self, enemies: list[Creature]):
        if not self.decrease_mana(50):
            return
        roll = randint(1, 20)
        roll += self.get_speed()

        if roll >= self.get_arcana():
            self.sleep_print(f"{self.get_name()} takes {roll//2} damage.")
            self.reduce_life(roll//2)
        else:
            self.sleep_print(f"{self.get_name()} takes {roll} damage.")
            self.reduce_life(roll)

        for enemy in enemies:
            roll = randint(5, 20)
            roll += self.get_arcana()
            self.sleep_print(f"{enemy.get_name()} takes {roll} damage.")
            enemy.reduce_life(roll)

    def select_target(self, target_list: list[Creature]):
        alive_targets = self.get_alive(target_list)
        if not alive_targets:
            return

        choice = -1

        while not (0 <= choice < len(alive_targets)):
            self.sleep_print("Select target:")
            for i, target in enumerate(alive_targets):
                print(f"{i+1}: {target}")
            choice = input("Enter choice: ")

            try:
                choice = int(choice) - 1
            except:
                self.sleep_print("Error, invalid input.")
                choice = -1

            if not (0 <= choice < len(alive_targets)):

                self.sleep_print(
                    f"Error, please enter a number between 1 and {len(alive_targets)}")
        return alive_targets[choice]

    def player_action(self, action: str, round_num: int, alive_targets: list[Creature], alive_allies: list[Creature] = None) -> bool:

        if not self.player:
            print("Error, non player character cannot take player turn.")
            return True

        if not alive_targets:
            return True

        match action:
            case "f":
                target = self.select_target(alive_targets)
                self.attack(target)

            case "r":
                self.recharge()
            case "1":
                if alive_allies:
                    ally = self.select_target(alive_allies)
                    self.heal(ally)
                else:
                    self.sleep_print("You have no allies currently alive.")
                    return False
            case "2":
                target = self.select_target(alive_targets)
                self.fire_bolt(target)
            case "3":
                if alive_allies:
                    self.mass_heal(alive_allies)
                else:
                    self.sleep_print("You have no allies alive.")
                    return False
            case "4":
                self.fire_storm(alive_targets)
            case _:
                return False

        return True

    def player_turn(self, round_num: int, target_list: list[Creature], allies: list[Creature] = None):

        if not self.player:
            self.sleep_print(
                "Error, non player character cannot take player turn.")
            return

        alive_targets = self.get_alive(target_list)

        if not alive_targets:
            return
        self.sleep_print("=====================================")
        print(self)
        print("Allies:")
        alive_allies = self.get_alive(allies)
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
            action = input("Enter action: ").lower()
            if action == "quit":
                return True
            input_valid = self.player_action(
                action, round_num, alive_targets, alive_allies)

    def turn(self, round_num: int, target_list: list[Creature], allies=None):
        if self.player:
            return self.player_turn(round_num, target_list, allies)
        else:
            return Creature.turn(self, round_num, target_list, allies)

    def __str__(self):
        if self.player:
            return f"Player {self.get_name()} HP: {self.HP}/{self.maxHP} Mana: {self.get_mana()}/{self.max_mana}"

        return f"{self.get_name()} HP: {self.HP}/{self.maxHP} Mana: {self.get_mana()}/{self.max_mana}"
