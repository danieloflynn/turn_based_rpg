from Warrior import Warrior
import random


def test():
    Warrior.delay = 0
    # Test 1
    w1 = Warrior("Tim")
    assert w1.get_attack() == 5, "Should be 5"
    assert w1.get_defence() == 10, "Should be 10"
    assert w1.get_speed() == 4, "Should be 4"

    # Test shield up
    w1.shield_up()
    assert w1.get_attack() == 1, "Should be 1"
    assert w1.get_defence() == 14, "Should be 14"
    assert w1.get_speed() == 4, "Should be 4"
    # Make sure 2 shield ups don't cause any issues
    w1.shield_up()
    assert w1.get_attack() == 1, "Should be 1"
    assert w1.get_defence() == 14, "Should be 14"
    assert w1.get_speed() == 4, "Should be 4"

    # Test shield down
    w1.shield_down()
    assert w1.get_attack() == 5, "Should be 5"
    assert w1.get_defence() == 10, "Should be 10"
    assert w1.get_speed() == 4, "Should be 4"
    # 2 shield downs should't cause any issues
    w1.shield_down()
    assert w1.get_attack() == 5, "Should be 5"
    assert w1.get_defence() == 10, "Should be 10"
    assert w1.get_speed() == 4, "Should be 4"

    # Check that Warrior attacks using correct attack amount (5)
    random.seed(1)
    w2 = Warrior("Warrior 2")
    w1.attack(w2)
    w1.attack(w2)
    assert w2.check_life() == 44, "Should be 44"

    # Check that each turn works
    targets = [Warrior("A"), Warrior("B"), Warrior("C")]
    random.seed(1)
    targets[0].increase_life(10)
    w1.turn(1, targets)
    assert w1.get_attack() == 1, "Should be 1"
    assert w1.get_defence() == 14, "Should be 14"
    assert targets[0].check_life(
    ) == 44, f"Life is {targets[0].check_life()}, should be 44"

    random.seed(1)
    targets[0].increase_life(10)
    w1.turn(2, targets)
    assert w1.get_attack() == 1, "Should be 1"
    assert w1.get_defence() == 14, "Should be 14"
    assert targets[0].check_life() == 48, "Should be 48"

    random.seed(1)
    targets[0].increase_life(10)
    w1.turn(3, targets)
    assert w1.get_attack() == 1, "Should be 1"
    assert w1.get_defence() == 14, "Should be 14"
    assert targets[0].check_life() == 48, "Should be 48"

    random.seed(1)
    targets[0].increase_life(10)
    w1.turn(4, targets)
    assert w1.get_attack() == 5, "Should be 5"
    assert w1.get_defence() == 10, "Should be 10"
    assert targets[0].check_life() == 44, "Should be 44"


test()
