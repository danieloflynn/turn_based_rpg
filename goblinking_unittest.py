from GoblinKing import GoblinKing
import random


def test():
    gk1 = GoblinKing("Terry")

    # Test 1 - check correct values for life, attack
    assert gk1.check_life() == 50
    assert gk1.get_attack() == 3
    assert gk1.get_defence() == 6
    assert gk1.get_speed() == 3

    # Test 2 - ensure turn works the same as archer
    random.seed(15)
    targets = [GoblinKing("A"), GoblinKing("B"), GoblinKing("C")]

    gk1.turn(1, targets)
    assert targets[0].check_life() == 50

    gk1.turn(2, targets)
    assert targets[0].check_life() == 43

    gk1.turn(3, targets)
    assert targets[0].check_life() == 43

    gk1.turn(4, targets)
    assert targets[0].check_life() == 43

    gk1.turn(1, targets)
    assert targets[0].check_life() == 43

    gk1.turn(2, targets)
    assert targets[0].check_life() == 35


if __name__ == "__main__":
    test()
