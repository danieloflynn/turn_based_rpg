from Archer import Archer
from Fighter import Fighter

team1 = [Archer("Dan")]
team2 = [Fighter("Adam")]


for member in team2:
    print(member.check_life())
for round in range(1, 21):
    print(f"Round {round}:")

    # Attack each other
    for member in team1:
        if member.check_life() > 0:
            member.turn(round, team2)

    for member in team2:
        if member.check_life() > 0:
            member.turn(round, team1)

    # Check for winner
    isWinner = False
    for member in team1:
        if member.check_life() != 0:
            break

    else:
        print("Team 2 wins!")
        isWinner = True

    for member in team2:
        if member.check_life() != 0:
            break
    else:
        print("Team 1 wins!")
        isWinner = True

    if isWinner:
        break

    print("----------------------------------------")
