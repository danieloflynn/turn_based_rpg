import creature_unittest
import goblin_unittest
import orc_unittest
import warrior_unittest
import archer_unittest
import fighter_unittest
import orcgeneral_unittest
import goblinking_unittest
import boss_unittest

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


# Test 6 - Fighter
print("------------------------------------------------------")
print("Testing Fighter...")
print("------------------------------------------------------")
fighter_unittest.test()
print("Fighter passed.")

# Test 7 - Orc General
print("------------------------------------------------------")
print("Testing OrcGeneral...")
print("------------------------------------------------------")
orcgeneral_unittest.test()
print("OrcGeneral passed.")

# Test 8 - Goblin King
print("------------------------------------------------------")
print("Testing Goblin King...")
print("------------------------------------------------------")
goblinking_unittest.test()
print("Goblin King passed.")

# Test 9 - Boss
print("------------------------------------------------------")
print("Testing Boss...")
print("------------------------------------------------------")
boss_unittest.test()
print("Boss passed.")


print("------------------------------------------------------")
print("All unit tests ok")
print("------------------------------------------------------")
