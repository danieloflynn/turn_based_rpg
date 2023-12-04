from Wizard import Wizard
from Orc import Orc
from Creatures import Creature


w1 = Wizard("Dan")
team2 = [Creature("Adam"), Orc("Tim")]

w1.attack(team2[0])
w1.fire_bolt(team2[1])
w1.heal(team2[1])
w1.mass_heal(team2)
w1.fire_storm(team2)

w1.recharge()
