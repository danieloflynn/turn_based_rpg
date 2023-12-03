from Creatures import Creature
from Goblin import Goblin
from Orc import Orc
from Warrior import Warrior
import random
import creature_unittest
import goblin_unittest
import orc_unittest
import archer_unittest

# Test Creatures
print("Testing Creatures")
creature_unittest.test()
print("------------------------------------------------------")

# Test Goblin
# Test 2 - test Goblin
print("Testing Goblin...")
print("------------------------------------------------------")
goblin_unittest.test()

# Test 3 - test Orc
print("------------------------------------------------------")
print("Testing Orc...")
print("------------------------------------------------------")
orc_unittest.test()
print("Orc passed.")


# Test 4 - test Warrior methods
print("------------------------------------------------------")
print("Testing Warrior...")
print("------------------------------------------------------")
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
g1.heal(15)
w1.attack(g1)
w1.attack(g1)
assert g1.check_life() == 9, "Should be 9"

# Check that each turn works
random.seed(1)
targets[0].heal(10)
w1.turn(1, targets)
assert w1.get_attack() == 1, "Should be 1"
assert w1.get_defence() == 14, "Should be 14"
assert targets[0].check_life() == 4, "Should be 4"

random.seed(1)
targets[0].heal(10)
w1.turn(2, targets)
assert w1.get_attack() == 1, "Should be 1"
assert w1.get_defence() == 14, "Should be 14"
assert targets[0].check_life() == 8, "Should be 4"

random.seed(1)
targets[0].heal(10)
w1.turn(3, targets)
assert w1.get_attack() == 1, "Should be 1"
assert w1.get_defence() == 14, "Should be 14"
assert targets[0].check_life() == 8, "Should be 8"

random.seed(1)
targets[0].heal(10)
w1.turn(4, targets)
assert w1.get_attack() == 5, "Should be 5"
assert w1.get_defence() == 10, "Should be 10"
assert targets[0].check_life() == 4, "Should be 4"
print("Warior passed.")
print("------------------------------------------------------")

print("All unit tests ok")
