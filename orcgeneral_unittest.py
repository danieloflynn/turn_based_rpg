from OrcGeneral import OrcGeneral
import random


def test():
    og1 = OrcGeneral("Davinia")

    # Test 1 - ensure all variables have been inherited correctly
    assert og1.check_life() == 80


if __name__ == "__main__":
    test()
