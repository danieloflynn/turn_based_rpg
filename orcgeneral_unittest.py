from OrcGeneral import OrcGeneral
import random


def test():
    og1 = OrcGeneral("Davinia")

    # Test 1 - ensure all variables have been inherited correctly
    assert og1.check_life() == 80
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"
    abilities = {
        "attack": 10,
        "defence": 9,
        "speed": 2
    }

    # Test 2 - check that a second instantiation can be created with cusom values
    og2 = OrcGeneral("Roseline", hp=100, abilities=abilities)

    assert og2.check_life() == 100
    assert og2.get_attack() == 10, f"Should be 10"
    assert og2.get_defence() == 9, f"Should be 9"
    assert og2.get_speed() == 2, f"Should be 2"

    # Check that this hasn't changed any of the values of 1
    assert og1.check_life() == 80
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    # Test 3 - regular attack
    random.seed(50)
    og1.attack(og2)
    assert og2.check_life() == 92

    og1.attack(og2)
    assert og2.check_life() == 85

    og1.attack(og2)
    assert og2.check_life() == 77

    og1.attack(og2)
    assert og2.check_life() == 77
    print("here")
    og1.attack(og2)
    assert og2.check_life() == 69

    og1.attack(og2)
    assert og2.check_life() == 69

    og1.attack(og2)
    assert og2.check_life() == 63

    og1.attack(og2)
    assert og2.check_life() == 63

    # Test 3 - Orc rage on/off
    random.seed(50)
    og2.heal(37)
    # Rage should be on
    og1.heavy_attack(og2)

    assert og2.check_life() == 87
    assert og1.get_attack() == 10, f"Should be 5"
    assert og1.get_defence() == 5, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    # Check that other orc hasn't gotten rage too
    assert og2.get_attack() == 10, f"Should be 10"
    assert og2.get_defence() == 9, f"Should be 9"
    assert og2.get_speed() == 2, f"Should be 2"

    og1.heavy_attack(og2)
    assert og2.check_life() == 75
    assert og1.get_attack() == 10, f"Should be 5"
    assert og1.get_defence() == 5, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.heavy_attack(og2)
    assert og2.check_life() == 62
    assert og1.get_attack() == 10, f"Should be 5"
    assert og1.get_defence() == 5, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.heavy_attack(og2)
    assert og2.check_life() == 62

    og1.attack(og2)
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.attack(og2)
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    # Test 4 - Warrior shield up/down
    random.seed(100)
    og1.shield_up()
    assert og1.get_attack() == 1, f"Should be 5"
    assert og1.get_defence() == 12, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.shield_up()
    assert og1.get_attack() == 1, f"Should be 5"
    assert og1.get_defence() == 12, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.attack(og2)
    assert og2.check_life() == 54

    og1.attack(og2)
    assert og2.check_life() == 49

    og1.shield_down()
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.shield_down()
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"
    assert og1.get_speed() == 3, f"Should be 3"

    # Test 5 - Orc Rage + Warrior shield
    # Ensure all combinations of up/down heavy_attack/attack work
    og1.heavy_attack(og2)
    og1.shield_up()
    assert og2.check_life() == 49
    assert og1.get_attack() == 6, f"Should be 5, is {og1.get_attack()}"
    assert og1.get_defence() == 9, f"Should be 8, is {og1.get_defence()}"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.heavy_attack(og2)
    og1.shield_up()
    assert og2.check_life() == 40
    assert og1.get_attack() == 6, f"Should be 5, is {og1.get_attack()}"
    assert og1.get_defence() == 9, f"Should be 8, is {og1.get_defence()}"
    assert og1.get_speed() == 3, f"Should be 3"

    og1.shield_down()
    assert og1.get_attack() == 10, f"Should be 5"
    assert og1.get_defence() == 5, f"Should be 8"

    og1.attack(og2)
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"

    og1.shield_up()
    og1.heavy_attack(og2)
    assert og1.get_attack() == 6, f"Should be 6, is {og1.get_attack()}"
    assert og1.get_defence() == 9, f"Should be 9, is {og1.get_defence()}"

    og1.attack(og2)
    assert og1.get_attack() == 1, f"Should be 1"
    assert og1.get_defence() == 12, f"Should be 12"

    og1.shield_down()
    # Test 6 - check that the turns work correctly
    random.seed(154)
    targets = [OrcGeneral("A"), OrcGeneral("B"), OrcGeneral("B")]

    og1.turn(1, targets)
    assert targets[0].check_life() == 71
    assert og1.get_attack() == 1, f"Should be 5"
    assert og1.get_defence() == 12, f"Should be 8"

    og1.turn(2, targets)
    assert targets[0].check_life() == 69
    assert og1.get_attack() == 1, f"Should be 5"
    assert og1.get_defence() == 12, f"Should be 8"

    og1.turn(3, targets)
    assert targets[0].check_life() == 69
    assert targets[1].check_life() == 80
    assert targets[2].check_life() == 80
    assert og1.get_attack() == 5, f"Should be 5"
    assert og1.get_defence() == 8, f"Should be 8"

    og1.turn(4, targets)
    assert targets[1].check_life() == 69
    assert og1.get_attack() == 10, f"Should be 5"
    assert og1.get_defence() == 5, f"Should be 8"


if __name__ == "__main__":
    test()
