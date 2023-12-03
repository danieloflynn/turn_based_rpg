from Orc import Orc
import random


def test():
    o1 = Orc("Jeremy")
    assert o1.get_name(
    ) == "Jeremy", f"Name should be Derek, is {o1.get_name()}"
    assert o1.check_life() == 50, f"Should be 50"
    assert o1.get_attack() == 5, f"Should be 5"
    assert o1.get_defence() == 8, f"Should be 8"
    assert o1.get_speed() == 3, f"Should be 3"

    o2 = Orc("Orc2")
    # Make sure super method takes correct "Get attack"
    random.seed(1)
    o1.attack(o2)
    o1.attack(o2)
    assert o2.check_life() == 44, f"Should be 44, is {o2.check_life()}"

    # Check heavy attack works
    o1.heavy_attack(o2)
    # Attack/defence values should now be different
    assert o1.get_attack() == 10, f"Should be 10"
    assert o1.get_defence() == 5, f"Should be 5"
    assert o1.get_speed() == 3, f"Should be 3"

    o2.heal(15)
    o1.heavy_attack(o2)
    o1.heavy_attack(o2)
    assert o2.check_life() == 36, "Should be 36"


if __name__ == "__main__":
    test()
