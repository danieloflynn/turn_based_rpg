from Goblin import Goblin
import random


def test():
    Goblin.delay = 0
    # Test 1 - test Goblin methods, and make sure attack methods etc. work
    print("Testing Goblin...")
    print("------------------------------------------------------")
    g1 = Goblin("Derek")
    assert g1.get_name() == "Derek", f"Should be Derek"
    assert g1.check_life() == 15, f"Life is {g1.check_life()} Should be 15"
    assert g1.get_attack() == 3, f"Should be 3"
    assert g1.get_defence() == 6, f"Should be 6"
    assert g1.get_speed() == 3, f"Should be 3"

    # Test 2 - Make sure super method takes correct "Get attack"
    g2 = Goblin("Goblin 2")
    random.seed(1)
    g1.attack(g2)
    g1.attack(g2)
    assert g2.check_life() == 11, f"Life is {g1.check_life()} Should be 11"

    print("Goblin passed.")
