from Fighter import Fighter
import random


def test():
    Fighter.delay = 0
    # Test 1 - check attributes
    f1 = Fighter("Sam")
    targets = [Fighter("A"), Fighter("B"), Fighter("C")]
    assert f1.check_life() == 50
    assert f1.get_attack() == 5
    assert f1.get_defence() == 8
    assert f1.get_speed() == 5

    # Test 2 - check secondary attack

    random.seed(10)
    f1.secondary_attack(targets[0])
    assert targets[0].check_life() == 47

    # Test 3 - check auto select
    targets[1].reduce_life(10)
    assert f1.auto_select(targets) == targets[2]

    targets[2].reduce_life(10)
    assert f1.auto_select(targets) == targets[0]

    targets[0].reduce_life(50)
    targets[1].reduce_life(50)
    targets[2].reduce_life(50)

    assert f1.auto_select(targets) == None


test()
