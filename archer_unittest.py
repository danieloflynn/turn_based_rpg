from Archer import Archer
import random


def test():
    a1 = Archer("Archy")
    targets = [Archer("A"), Archer("B"), Archer("C")]

    assert a1.check_life() == 30
    assert a1.get_attack() == 7
    assert a1.get_defence() == 9
    assert a1.get_speed() == 8


test()
print("All unit tests ok.")
