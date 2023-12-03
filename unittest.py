from Creatures import Creature
from Goblin import Goblin
from Orc import Orc
from Warrior import Warrior
import random
import creature_unittest
import goblin_unittest
import orc_unittest
import warrior_unittest
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
warrior_unittest.test()
print("Warior passed.")


# Test 5 - Archer
print("------------------------------------------------------")
print("Testing Archer...")
print("------------------------------------------------------")
archer_unittest.test()
print("Archer passed.")
print("------------------------------------------------------")

print("All unit tests ok")
