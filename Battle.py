from Archer import Archer
from Boss import Boss
from Creatures import Creature
from Fighter import Fighter
from Goblin import Goblin
from GoblinKing import GoblinKing
from OrcGeneral import OrcGeneral
from Orc import Orc
from Warrior import Warrior
from Wizard import Wizard
from time import sleep


class Battle:
    """Holds all the variables and methods for a battle.

    """
    delay = 0.8

    def __init__(self):
        self.new_battle()

    def new_battle(self):
        """Starts a new battle. Resets enemies and allies again.
        """
        self.enemies: list[Creature] = [
            GoblinKing("Griznakh Bloodaxe"),
            OrcGeneral("Drogosh Blackblade"),
            Goblin("Fizzlewort"),
            Orc("Urgor the Ruthless")
        ]

        self.allies: list[Creature] = [
            Fighter("Rurik Steelheart"),
            Archer("Elowen Windshot"),
            Warrior("Kellan Stormbringer"),
            Creature("Thornscale, the Drake")
        ]

        self.boss = Boss("Voragor the Dreadlord")

        self.hasPlayers = False

    def check_winner(self) -> bool:
        """Checks both teams to see if there is a winner.
            If all enemies + boss dead, player[s] win
            If player[s] in game and all players dead, player[s] lose.

        Returns:
            bool: True if there is winner, false is not
        """

        # Check allies first
        if self.hasPlayers:
            for player in self.players:
                if player.check_life() > 0:
                    break
            else:
                print("You lose.")
                return True
        else:
            for ally in self.allies:
                if ally.check_life() > 0:
                    break
            else:
                print("Allies lose.")
                return True

        # Check if enemies win
        # First check if Boss alive
        if self.boss.check_life() > 0:
            return False

        # If Boss dead, check the whole list of enemies to make sure there aren't any still alive
        for enemy in self.enemies:
            if enemy.check_life() > 0:
                return False  # If enemy not dead, we know battle isn't over as there's at least one ally alive

        return True

    def sort_by_speed(creatures: list[Creature]):
        # Sorts list of creatures by speed.
        creatures.sort(key=lambda c: c.get_speed(), reverse=True)

    def start(self):
        print("THE BATTLE BEGINS")
        print("==========================================")
        for round_num in range(1, 21):
            sleep(0.8)
            print(f"Round {round_num}")
            print("==========================================")

            for enemy in self.enemies:
                if enemy.check_life() < 0:
                    continue
                enemy.turn(round_num, target_list=self.allies,
                           allies=self.enemies)

            for ally in self.allies:
                if ally.check_life() < 0:
                    continue

                ally.turn(round_num, target_list=self.enemies,
                          allies=self.allies)

            if self.check_winner():
                break


B = Battle()
B.start()
