import unittest_creature
import unittest_goblin
import unittest_orc
import unittest_warrior
import unittest_archer
import unittest_fighter
import unittest_orcgeneral
import unittest_goblinking
import unittest_boss
import unittest_wizard
import unittest_battle

# Test Creatures
print("Testing Creatures")
unittest_creature.test()
print("------------------------------------------------------")

# Test Goblin
# Test 2 - test Goblin
print("Testing Goblin...")
print("------------------------------------------------------")
unittest_goblin.test()

# Test 3 - test Orc
print("------------------------------------------------------")
print("Testing Orc...")
print("------------------------------------------------------")
unittest_orc.test()
print("Orc passed.")


# Test 4 - test Warrior methods
print("------------------------------------------------------")
print("Testing Warrior...")
print("------------------------------------------------------")
unittest_warrior.test()
print("Warior passed.")


# Test 5 - Archer
print("------------------------------------------------------")
print("Testing Archer...")
print("------------------------------------------------------")
unittest_archer.test()
print("Archer passed.")


# Test 6 - Fighter
print("------------------------------------------------------")
print("Testing Fighter...")
print("------------------------------------------------------")
unittest_fighter.test()
print("Fighter passed.")

# Test 7 - Orc General
print("------------------------------------------------------")
print("Testing OrcGeneral...")
print("------------------------------------------------------")
unittest_orcgeneral.test()
print("OrcGeneral passed.")

# Test 8 - Goblin King
print("------------------------------------------------------")
print("Testing Goblin King...")
print("------------------------------------------------------")
unittest_goblinking.test()
print("Goblin King passed.")

# Test 9 - Boss
print("------------------------------------------------------")
print("Testing Boss...")
print("------------------------------------------------------")
unittest_boss.test()
print("Boss passed.")

# Test 9 - Wizard
print("------------------------------------------------------")
print("Testing Wizard...")
print("------------------------------------------------------")
unittest_wizard.test()
print("Wizard passed.")

# Test 10 - Battle
print("------------------------------------------------------")
print("Testing Battle...")
print("------------------------------------------------------")
unittest_battle.test()
print("Battle passed.")


print("------------------------------------------------------")
print("All unit tests ok")
print("------------------------------------------------------")
