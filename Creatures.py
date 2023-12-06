from random import randint
from time import sleep
# TODO: Make variables private


class Creature:
    """Creature class.

    Class Attributes:
    - default_attributes (dict[str, int]): Default abilities for this class, to be used if none supplied in constructor.
    - isPlayer (bool): Whether the Creature is a player. Set to False.

    Instance Attributes:
    - name (str): Name of the creature
    - HP (int, optional): HP of the creature. Defaults to 10.
    - maxHP (int, optional): Max HP of the creature.
    - abilities (dict[str, int], optional): abilities (_type_, optional): Dictionary containing the abilities of the Archer (attack, defence, and speed). Defaults to default_abilities.

    Methods:
    - get_name: Getter method for the name of the creature (Encapsulation)
    - check_life: Gets the current HP of the creature.
    - get_attack: Gets the attack ability of the creature.
    - get_defence: Gets the defence ability of the creature.
    - get_speed: gets the speed ability of the creature.
    - reduce_life: reduces HP of the creature by a given amount. See function for more details.
    - increase_life: increase HP of the creature by a given amount. See functino for more details.
    - attack: Attack a given target.
    - get_alive: Returns a list of alive targets given a list of potential targets.
    - auto_select: Returns a random alive target given a list of targets.
    - turn: Turn logic for creature. Selects random alive target and attacks.
    """
    default_abilities = {
        "attack": 1,
        "defence": 5,
        "speed": 5
    }

    isPlayer = False

    delay = 0.8

    def __init__(self, name: str, HP: int = 10, abilities: dict[str, int] = default_abilities):
        """Constructor for Creature.

        Args:
            name (str): Name of the creature
            HP (int, optional): HP/ max HP for the creature. Defaults to 10.
            abilities (_type_, optional): Dictionary containing the abilities of the Creature (attack, defence, and speed).. Defaults to default_abilities.
        """
        self.name = name
        self.HP = HP
        self.maxHP = HP
        # Copy so that we're not sharing attributes with other creatures if they get modified.
        self.abilities = abilities.copy()

    def get_name(self):
        # Gets the name of the Creature
        return self.name

    def sleep_print(self, message: str):
        # Sets a slight delay, and then prints
        sleep(self.delay)
        print(message)

    def check_life(self):
        # Gets the current HP of the Creature
        return self.HP

    def get_attack(self):
        # Gets the current attack ability of the Creature
        return self.abilities["attack"]

    def get_defence(self):
        # Gets the current defence ability of the Creature
        return self.abilities["defence"]

    def get_speed(self):
        # Gets the current speed ability of the Creature
        return self.abilities["speed"]

    def reduce_life(self, points: int):
        """Reduces the life of the Creature by given amount. 
            If the amount is greater than current HP, HP will be set to 0.

        Args:
            points (int): Number of points for the health to be reduced by.
        """
        if self.HP <= points:  # If amount greater than HP, set HP to 0.
            self.HP = 0
            self.sleep_print(f"{self.get_name()} fainted.")
        else:  # Otherwise take points from HP.
            self.HP -= points

    def increase_life(self, points: int):
        """Increases the life of the creature by a given amount of points. 
            If amount makes HP greater than max, set HP = maxHP

        Args:
            points (int): _description_
        """
        if self.HP + points > self.maxHP:  # If HP will be greater than maxHP, set HP = maxHP
            self.HP = self.maxHP
        else:  # Else add points to HP
            self.HP += points
        # Print messages to the effect
        self.sleep_print(f"{self.get_name()} is healed by {points} points.")
        self.sleep_print(
            f"{self.get_name()}'s health is now {self.check_life()}.")

    def attack(self, target: 'Creature'):
        """Attacks a given target.
            Rolls a number between 1-20. If roll > defence + speed of target, attack successful.
            Damage: Damage applied will the the Creature's attack + a bonus roll from  1-4.

        Args:
            target (Creature): Target to be attacked.
        """
        self.sleep_print(f"{self.get_name()} attacks {target.get_name()}")

        roll = randint(1, 20)  # Roll number between 1-20
        if roll > target.get_defence() + target.get_speed():
            # If roll > target defence + speed, attack is successful
            bonus = randint(1, 4)  # bonus roll
            damage = self.get_attack() + bonus
            self.sleep_print(f"Attack hits for {damage} damage!")
            target.reduce_life(damage)  # Reduce life of target by damage
        else:  # Else attack misses
            self.sleep_print("Atack missed...")

    def get_alive(self, target_list: list['Creature']):
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

    def auto_select(self, target_list: list['Creature']):
        """Randomly selects an alive Creature from target list.

        Args:
            target_list (list[Creature]): List of potential targets.

        Returns:
            (Creature): Target.
        """
        alive_targets = self.get_alive(target_list)  # Get alive targets

        if not alive_targets:  # If no alive targets, return.
            return

        # Pick a random target from alive targets
        rand = randint(0, len(alive_targets)-1)
        return alive_targets[rand]

    def turn(self, round_num: int, target_list: list['Creature'], allies: list['Creature'] = None):
        """Take turn for Creature. Picks a random alive target and attacks.

        Args:
            round_num (int): Current round number. Not used but included for sake of polymorphism.
            target_list (list[Creature]): List of targets.
            allies (list[Creature], optional): List of allies. This has no function here but is included for the sake of polymorphism. Defaults to None.
        """
        target = self.auto_select(target_list)  # Pick a random alive target
        if target:  # If there is a target, attack.
            self.attack(target)

    def __str__(self):
        return f"{self.name}, health: {self.check_life()}/{self.maxHP}"

    def __repr__(self):
        return self.__str__()
