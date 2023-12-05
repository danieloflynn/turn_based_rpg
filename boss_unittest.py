from Boss import Boss
from Creatures import Creature
import random


def test():
    Boss.delay = 0
    # Test 1 - check that all
    b1 = Boss("Ted")
    assert b1.check_life() == 200
    assert b1.get_attack() == 5
    assert b1.get_defence() == 8
    assert b1.get_speed() == 5

    # Test 2 - check that auto select works
    random.seed(60)
    targets = [Boss("A"), Boss("B"), Boss("C")]
    targets[0].reduce_life(20)
    targets[1].reduce_life(30)
    assert b1.auto_select(targets, "Strong") == targets[2]
    assert b1.auto_select(targets, "Weak") == targets[1]
    assert b1.auto_select(targets, "Random") == targets[1]

    # Test 3 - check that turn and all attacks work correctly
    # Turn 1 should attack 3 times
    random.seed(10)
    b1.turn(1, targets)
    assert targets[2].check_life() == 179

    # Check if first target faints that it picks another target
    random.seed(11)
    targets2 = [Creature("A"), Creature("B"), Creature("C")]
    b1.turn(1, targets2)
    assert targets2[0].check_life() == 0
    assert targets2[1].check_life() == 1

    # Check other turns working
    b1.turn(2, targets)
    assert targets[1].check_life() == 158

    b1.turn(3, targets)
    assert targets[1].check_life() == 158

    b1.turn(4, targets)
    assert targets[1].check_life() == 145

    b1.turn(2, targets)
    assert targets[1].check_life() == 145

    b1.turn(3, targets)
    assert targets[1].check_life() == 145

    b1.turn(4, targets)
    assert targets[1].check_life() == 134


if __name__ == "__main__":
    test()
