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
    round_delay = 1

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
        self.bossAdded = False
        self.players = []
        self.add_players()

    def add_players(self):
        input_valid = False
        while not input_valid:
            try:
                num_players = int(input("Please enter number of players: "))
            except:
                print("Error: User input not valid.")

            if 0 <= num_players <= 3:
                self.num_players = num_players
                for i in range(1, num_players + 1):
                    name = input(f"Player {i}, please enter your name: ")
                    # Make player HP 30 because it's impossible otherwise
                    player = Wizard(name, hp=30, player=True)
                    self.players += [player]
                    self.allies += [player]

                input_valid = True
            else:
                print("Error, please enter a number of players between 0 and 3")

    def check_winner(self) -> bool:
        """Checks both teams to see if there is a winner.
            If all enemies + boss dead, player[s] win
            If player[s] in game and all players dead, player[s] lose.

        Returns:
            bool: True if there is winner, false is not
        """

        # Check allies first
        if self.num_players:
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
        if self.num_players:
            print("You win!")
        else:
            print("Allies win!")

        return True

    def sort_by_speed(self, creatures: list[Creature]):
        # Sorts list of creatures by speed.
        creatures.sort(key=lambda c: c.get_speed(), reverse=True)

    def count_alive(self, creatures: list[Creature]):
        count = 0
        for creature in creatures:
            if creature.check_life() > 0:
                count += 1
        return count

    def add_boss(self):

        if self.bossAdded:
            return

        self.bossAdded = True
        self.enemies += [self.boss]
        print(f"Suddenly....")
        sleep(self.round_delay)
        print(f"{self.boss.get_name()} appears.")
        sleep(self.round_delay)
        print(r"""
                 _____
                /     \
               | () () |
                \  ^  /
                 |||||
                 |||||
                """)
        sleep(self.round_delay)
        print("Get ready.")

    def start(self):

        playGame = "y"

        while playGame == "y":
            print("THE BATTLE BEGINS")
            print("==========================================")
            for round_num in range(1, 21):

                if self.count_alive(self.enemies) < 2 and not self.bossAdded:
                    self.add_boss()

                sleep(self.round_delay)
                print(f"Round {round_num}")
                print("==========================================")
                sleep(self.round_delay)

                self.sort_by_speed(self.allies)
                self.sort_by_speed(self.enemies)

                for enemy in self.enemies:
                    if enemy.check_life() <= 0:
                        continue
                    enemy.turn(round_num, target_list=self.allies,
                               allies=self.enemies)

                for ally in self.allies:
                    if ally.check_life() <= 0:
                        continue

                    quit = ally.turn(round_num, target_list=self.enemies,
                                     allies=self.allies)
                    if quit:
                        break

                if quit:
                    break

                if self.check_winner():
                    break

                print("==========================================")
            sleep(self.round_delay)
            print("==========================================")
            print("Game over.")

            playGame = input("Play again? y/[n]").lower()

            if playGame == "y":
                self.new_battle()


if __name__ == "__main__":
    B = Battle()
    B.start()
