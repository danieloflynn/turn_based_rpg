from Creatures import Creature, Goblin, Orc
import random

# Test 1
# Check that get methods work
c1 = Creature("Test1")

print("Testing get methods...")
assert c1.get_name() == "Test1", "Should be Test1"
assert c1.check_life() == 10, "Should be 10"
assert c1.get_attack() == 1, "Should be 1"
assert c1.get_defence() == 5, "Should be 5"
assert c1.get_speed() == 5, "Should be 5"
print("Get methods passed")

print("Testing life assignment...")
c2 = Creature("Test", 20)
assert c2.check_life() == 20, f"Life should be 20, is {c2.check_life()}"
print("Passed.")

# Test 2
# Check reduce life and heal method
# Can reduce life
print("Testing reduce life and heal methods...")
c1.reduce_life(1)
assert c1.check_life() == 9, "Life should be 9"

# Heal works
c1.heal(1)
assert c1.check_life() == 10, "Life should be 10"

# Reducing by 0 works
c1.reduce_life(0)
assert c1.check_life() == 10, "Life should be 10"

# Reducing by > health makes health 0
c1.reduce_life(12)
assert c1.check_life() == 0, "Life should be 0"

# Can reduce life on a creature with custom health
c2.reduce_life(12)
assert c2.check_life() == 8, f"Life should be 8, is {c2.check_life()}"
print("Reduce life methods passed.")


# Test 3 - test attack and auto select
print("Testing attack and autoselect methods...")
targets = [Creature("A"), Creature("B"), Creature("C")]

random.seed(1)
c2.attack(targets[0])
assert targets[0].check_life(
) == 10, f"Attack should have missed, life should be 10, is {targets[0].check_life()}"

c2.attack(targets[0])
assert targets[0].check_life(
) == 8, f"Attack should have hit for 2 damage, life should be 8, is {targets[0].check_life()}"
print("Attack method passed.")

random.seed(1)
assert c2.auto_select(targets) == targets[0], f"Should have picked target 0."
print("Auto select method passed.")

random.seed(1)
c2.turn(1, targets)
assert targets[0].check_life(
) == 6, f"Attack should picked target 1, life should be 4, is {targets[0].check_life()}"
print("Creature attack, auto select and turn methods passed.")


# Test 4 - test Goblin methods, and make sure attack methods etc. work
print("Testing Goblin...")
g1 = Goblin("Derek")
assert g1.get_name() == "Derek", "Should be Derek"
assert g1.check_life() == 15, "Should be 15"
assert g1.get_attack() == 3, "Should be 3"
assert g1.get_defence() == 6, "Should be 6"
assert g1.get_speed() == 3, "Should be 3"

# Make sure super method takes correct "Get attack"
random.seed(1)
g1.attack(c2)
g1.attack(c2)
assert c2.check_life() == 4, "Should be 4"


print("Goblin passed.")

print("Testing Orc...")
o1 = Orc("Jeremy")
assert o1.get_name() == "Jeremy", "Should be Derek"
assert o1.check_life() == 50, "Should be 50"
assert o1.get_attack() == 5, "Should be 5"
assert o1.get_defence() == 8, "Should be 8"
assert o1.get_speed() == 3, "Should be 3"

# Make sure super method takes correct "Get attack"
random.seed(1)
o1.attack(g1)
o1.attack(g1)
assert g1.check_life() == 9, "Should be 9"

# Check heavy attack works
o1.heavy_attack(g1)
# Attack/defence values should now be different
assert o1.get_attack() == 10, "Should be 10"
assert o1.get_defence() == 5, "Should be 5"
assert o1.get_speed() == 3, "Should be 3"


g1.heal(15)
o1.heavy_attack(g1)
o1.heavy_attack(g1)
assert g1.check_life() == 1, "Should be 1"


print("All unit tests ok")
