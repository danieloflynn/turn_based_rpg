from Creatures import Creature
from unittest.mock import patch
import random

# Test 1
# Check that get methods work
c1 = Creature("Test1")

assert c1.get_name() == "Test1", "Should be Test1"
assert c1.check_life() == 10, "Should be 10"
assert c1.get_attack() == 1, "Should be 1"
assert c1.get_defence() == 5, "Should be 5"
assert c1.get_speed() == 5, "Should be 5"


# Test 2
# Check reduce life method
# Can reduce life
c1.reduce_life(1)
assert c1.check_life() == 9, "Life should be 9"

# Reducing by 0 works
c1.reduce_life(0)
assert c1.check_life() == 9, "Life should be 9"

# Reducing by > health makes health 0
c1.reduce_life(12)
assert c1.check_life() == 0, "Life should be 0"


cList = [Creature("A"), Creature("B")]


print("All unit tests ok")
