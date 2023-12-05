from Archer import Archer
import random


def test():
    Archer.delay = 0
    a1 = Archer("Archy")
    targets = [Archer("A"), Archer("B"), Archer("C")]

    # Test 1 - check get methods
    assert a1.check_life() == 30
    assert a1.get_attack() == 7
    assert a1.get_defence() == 9
    assert a1.get_speed() == 8

    # Test 2 - check power shot works and attack/defence get changed
    random.seed(1)
    print(a1.powerup_abilities)
    a1.power_shot(targets[0])
    assert targets[0].check_life() == 18
    assert a1.get_attack() == 10
    assert a1.get_defence() == 6
    assert a1.get_speed() == 8

    a1.power_shot(targets[0])
    a1.power_shot(targets[0])
    a1.power_shot(targets[0])
    a1.power_shot(targets[0])
    a1.power_shot(targets[0])
    a1.power_shot(targets[0])
    a1.power_shot(targets[0])

    assert targets[0].check_life() == 0
    assert a1.get_attack() == 10
    assert a1.get_defence() == 6
    assert a1.get_speed() == 8

    targets[0].increase_life(30)

    # Test 3 - check regular attack works
    random.seed(1)
    a1.attack(targets[0])
    a1.attack(targets[0])

    assert targets[0].check_life() == 22
    assert a1.get_attack() == 7
    assert a1.get_defence() == 9
    assert a1.get_speed() == 8

    random.seed(1)
    a1.attack(targets[0])
    a1.attack(targets[0])
    # Attacking twice with normal should yield the same thing
    assert targets[0].check_life() == 14
    assert a1.get_attack() == 7
    assert a1.get_defence() == 9
    assert a1.get_speed() == 8

    # Test 4 - check auto select works
    assert a1.auto_select(targets) == targets[0]

    targets[0].increase_life(20)
    targets[1].reduce_life(10)

    assert a1.auto_select(targets) == targets[1]

    # Make sure it doesn't return a dead target
    targets[0].reduce_life(30)
    assert a1.auto_select(targets) == targets[1]

    # Test 5 - Make sure each of the 4 turns works correctly
    random.seed(1)
    a1.turn(1, targets)
    a1.turn(1, targets)
    a1.turn(1, targets)
    assert targets[1].check_life() == 12

    random.seed(1)
    targets[1].increase_life(8)
    a1.turn(2, targets)
    assert targets[1].check_life() == 8

    random.seed(1)
    targets[1].increase_life(12)
    a1.turn(3, targets)
    assert targets[1].check_life() == 8

    random.seed(1)
    targets[1].increase_life(12)
    a1.turn(4, targets)
    assert targets[1].check_life() == 8


if __name__ == "__main__":
    test()
