from Creatures import Creature
from random import randint


class Wizard(Creature):
    """Wizard class. Inherits from Creature. Player can play as Wizard

    Class Attributes:
    - default_attributes (dict[str, int]): Default abilities for this class, to be used if none supplied in constructor.

    Instance Attributes:
    - max_mana (int): Max mana Wizard can have.
    - mana (int): Amount of mana Wizard currently has
    - maxHP (int, optional): Max HP of the Wizard.
    - isPlayer: Whether the Wizard is a player. 

    Methods:
    - get_mana: Get the current mana of the Wizard
    - increase_mana: Increase the mana of the Wizard by a given amount.
    - decrease_mana:  Decrease the mana of the Wizard by a given amount. 
    - get_arcana: Get the player's arcana value.
    - attack: Attack a creature and recharge mana by 20.
    - recharge: Recharge mana by 30.
    - fire_bolt: Throw firebolt at target
    - heal: Heal target and reduce mana by 20.
    - mass_heal: Heal all allies (incl. self) and reduce mana by 30.
    - fire_storm: Hit all enemies and self with fire storm and reduce mana by 50.
    - select_target: Player to select enemy.
    - player_action: Undertakes player's action.
    - player_turn: Take turn for player.
    - turn: Take turn, calls player_turn if player.
    """

    default_abilities = {
        "attack": 3,
        "defence": 5,
        "speed": 5,
        "arcana": 10
    }

    def __init__(self, name: str, hp: int = 20, abilities: dict = default_abilities, player: bool = False):
        """Constructor for Wizard.

        Args:
            name (str): Name of Wizard
            hp (int, optional): HP of Wizard. Defaults to 20.
            abilities (dict, optional): abilities of wizard. Defaults to default_abilities.
            player (bool, optional): Whether the wizard is a player. Defaults to False.
        """
        Creature.__init__(self, name, hp, abilities)
        self.max_mana = 100
        self.mana = self.max_mana
        self.isPlayer = player

    def get_mana(self):
        # Gets the mana of the player
        return self.mana

    def increase_mana(self, points: int):
        """Increase the mana of the player by an amount. Will only increase to maxMana

        Args:
            points (int): number of points to increase by.
        """
        self.sleep_print(f"Mana +{points}")
        if self.get_mana() + points > self.max_mana:
            self.mana = self.max_mana

        else:
            self.mana += points

    def decrease_mana(self, points: int) -> bool:
        """Decrease mana of Wizard by an amount. If not enough mana will abort and return false.

        Args:
            points (int): Number of points to reduce by.

        Returns:
            bool: True if successful, False otherwise.
        """
        if points > self.get_mana():
            self.sleep_print(f"{self.get_name()} does not have enough mana.")
            return False
        self.sleep_print(f"Mana -{points}")
        self.mana -= points
        return True

    def get_arcana(self):
        # Get arcana of Wizard
        return self.abilities["arcana"]

    def attack(self, target: Creature):
        # Attack of Wizard. Uses creature attack and increases mana by 20.
        Creature.attack(self, target)
        self.increase_mana(20)

    def recharge(self):
        # Recharge mana by 30.
        self.sleep_print(f"{self.get_name()} channels magic energy...")
        self.increase_mana(30)
        self.sleep_print(f"{self.get_name()}'s mana is now {self.mana}.")

    def fire_bolt(self, target: Creature):
        """ Casts firebolt at target creature. Adds half Wizard's Arcana to attack roll.
        If attack successful, applies damage between 1 and current Arcana

        Args:
            target (Creature): _description_
        """
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
        """Attempts to heal target. If target already dead will not heal.
            Requires 20 mana.
        """
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
        """Heal all allies incl self. Requires 30 mana. Will not heal dead allies.

        Args:
            allies (list[Creature]): _description_
        """
        self.sleep_print(f"{self.get_name()} attempts to heal all allies")
        if not self.decrease_mana(30):
            return
        healing = randint(1, 10) + self.get_arcana()
        for ally in allies:
            if ally.check_life() != 0:
                ally.increase_life(healing)

    def fire_storm(self, enemies: list[Creature]):
        """Casts fire storm on all enemies.
            Requires 50 mana. Roll 1-20, if roll + arcana > Wizard arcana, apply 1/2 damage to wizard.
            Otherwise, apply full damage.
            Enemies get damaged by random amount betweem 5-20 + arcana.
        Args:
            enemies (list[Creature]): Enemies to cast firestorm on.
        """
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
        """Prompts player to select target from enemy list.

        Args:
            target_list (list[Creature]): List of enemies.

        Returns:
            Creature: Creature selected.
        """
        alive_targets = self.get_alive(target_list)
        if not alive_targets:  # If no alive targets return
            return

        choice = -1

        while not (0 <= choice < len(alive_targets)):
            self.sleep_print("Select target:")
            for i, target in enumerate(alive_targets):  # print out targets
                print(f"{i+1}: {target}")
            choice = input("Enter choice: ")

            try:
                # Makes sure game doesn't crash if non int is put in
                choice = int(choice) - 1
            except:
                self.sleep_print("Error, invalid input.")
                choice = -1

            # Restart process if int outside of range put in
            if not (0 <= choice < len(alive_targets)):

                self.sleep_print(
                    f"Error, please enter a number between 1 and {len(alive_targets)}")
        return alive_targets[choice]  # Return choice

    def player_action(self, action: str, round_num: int, alive_targets: list[Creature], alive_allies: list[Creature] = None) -> bool:
        """Logic for undertaking player's action (Assuming it's not quit)
            Valid options: "f": Attack "r": Recharge Mana
            "1": Heal "2": Firebolt "3": Mass Heal "4": Fire Storm
        Args:
            action (str): Action to be taken
            round_num (int): Current round num. Not used but in future could have certain actions blocked at certain rounds.
            alive_targets (list[Creature]): Targets that are currently alive. Does not check if they are alive. 
            alive_allies (list[Creature], optional): Allies that are currently alive. Does not check if they are alive. Defaults to None.

        Returns:
            bool: Returns True if action successful, false otherwise.
        """
        if not self.isPlayer:
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
        """Prompts player to take an action. options are as follows:
            F: Attack R: Recharge Mana
            1: Heal 2: Firebolt 3: Mass Heal 4: Fire Storm
            "Quit: Quits game

        Args:
            round_num (int): _description_
            target_list (list[Creature]): list of all targets
            allies (list[Creature], optional): List of all allies. Defaults to None.

        Returns:
            bool: _description_
        """
        if not self.isPlayer:
            self.sleep_print(
                "Error, non player character cannot take player turn.")
            return

        alive_targets = self.get_alive(target_list)

        self.sleep_print("=====================================")
        print(self)
        print("Allies:")
        alive_allies = self.get_alive(allies)
        for ally in alive_allies:
            print(ally)
        if not alive_targets:
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
        """Turn logic for Wizard. If player prompts player turn, if not uses creature logic.

        Args:
            round_num (int): Current round number
            target_list (list[Creature]): List of target creatures
            allies (list[Creature], optional): List of ally creatures. Defaults to None.
        """
        if self.isPlayer:
            return self.player_turn(round_num, target_list, allies)
        else:
            return Creature.turn(self, round_num, target_list, allies)

    def __str__(self):
        if self.isPlayer:
            return f"Player {self.get_name()} HP: {self.HP}/{self.maxHP} Mana: {self.get_mana()}/{self.max_mana}"

        return f"{self.get_name()} HP: {self.HP}/{self.maxHP} Mana: {self.get_mana()}/{self.max_mana}"
