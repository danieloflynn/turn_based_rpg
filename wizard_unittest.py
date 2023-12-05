from Wizard import Wizard
from unittest import mock
import random


def test():
    # Test 1 - check all abilities correct
    w1 = Wizard("Dan")
    assert w1.check_life() == 20
    assert w1.maxHP == 20
    assert w1.get_attack() == 3
    assert w1.get_defence() == 5
    assert w1.get_speed() == 5
    assert w1.get_arcana() == 10
    assert w1.get_mana() == 100

    # Test 2 - check reduce and increase mana works correctly
    assert w1.decrease_mana(110) == False
    assert w1.get_mana() == 100
    assert w1.decrease_mana(50) == True
    assert w1.get_mana() == 50
    assert w1.decrease_mana(50) == True
    assert w1.get_mana() == 0
    w1.increase_mana(50)
    assert w1.get_mana() == 50
    w1.increase_mana(100)
    assert w1.get_mana() == 100

    # Test 3 - check attack works
    random.seed(30)
    w2 = Wizard("Fran")
    w1.decrease_mana(90)
    w1.attack(w2)
    assert w2.check_life() == 14
    assert w1.get_mana() == 30

    w1.attack(w2)
    assert w2.check_life() == 10
    assert w1.get_mana() == 50

    w1.attack(w2)
    assert w2.check_life() == 5
    assert w1.get_mana() == 70

    w1.attack(w2)
    assert w2.check_life() == 5
    assert w1.get_mana() == 90

    w1.attack(w2)
    assert w2.check_life() == 5
    assert w1.get_mana() == 100

    # Test 4 - check recharge
    random.seed(80)

    w1.decrease_mana(100)
    w1.recharge()
    assert w1.get_mana() == 30

    # Test 5 - check firebolt works
    w2.increase_life(100)
    random.seed(90)

    w1.fire_bolt(w2)
    assert w2.check_life() == 18
    assert w1.get_mana() == 40

    w1.fire_bolt(w2)
    assert w2.check_life() == 8
    assert w1.get_mana() == 50

    # create a character with defence>20 so attacks will always miss
    invincible = Wizard("Invincible", abilities={
                        "attack": 0, "defence": 50, "speed": 50})

    w1.fire_bolt(invincible)
    assert invincible.check_life() == 20
    assert w1.get_mana() == 50

    # Test 6 - check heal
    w1.heal(w2)
    assert w2.check_life() == 18
    assert w1.get_mana() == 30

    w1.heal(w2)
    assert w2.check_life() == 20
    assert w1.get_mana() == 10

    w2.reduce_life(20)
    w1.increase_mana(20)
    w1.heal(w2)
    assert w2.check_life() == 0
    assert w1.get_mana() == 10

    # Ensure action does not proceed if not enough mana
    w2.increase_life(10)
    w1.heal(w2)
    assert w2.check_life() == 10
    assert w1.get_mana() == 10

    # Test 7 - mass heal
    random.seed(11)
    allies = [w1, w2, Wizard("Phil"), Wizard("Jim"), Wizard("Tom", hp=100)]
    w1.increase_mana(20)
    # check will heal self
    w1.reduce_life(19)
    # last person will have to health to ensure it doesn't work
    allies[3].reduce_life(20)
    allies[4].reduce_life(80)

    w1.mass_heal(allies)

    assert w1.check_life() == 19
    assert allies[1].check_life() == 20
    assert allies[2].check_life() == 20
    assert allies[3].check_life() == 0
    assert allies[4].check_life() == 38

    assert w1.get_mana() == 0

    # Make sure it doesn't work if mana not high enough

    w1.mass_heal(allies)

    assert w1.check_life() == 19
    assert allies[4].check_life() == 38

    # Test 8 - fire storm
    random.seed(83)
    w1.increase_mana(60)
    # Remove self from enemies list
    enemies = allies[1:]
    for enemy in enemies:
        enemy.increase_life(100)

    w1.fire_storm(enemies)
    assert w1.check_life() == 9
    assert enemies[0].check_life() == 0
    assert enemies[1].check_life() == 3
    assert enemies[2].check_life() == 1
    assert enemies[3].check_life() == 73

    # Second roll is less than arcana
    w1.increase_mana(60)
    w1.increase_life(20)
    w1.fire_storm(enemies)
    assert w1.check_life() == 13
    assert w1.get_mana() == 20
    assert enemies[0].check_life() == 0
    assert enemies[1].check_life() == 0
    assert enemies[2].check_life() == 0
    assert enemies[3].check_life() == 53

    # Ensure attack won't go ahead if not enough mana
    w1.fire_storm(enemies)
    assert w1.check_life() == 13
    assert w1.get_mana() == 20
    assert enemies[0].check_life() == 0
    assert enemies[1].check_life() == 0
    assert enemies[2].check_life() == 0
    assert enemies[3].check_life() == 53

    enemies[0].increase_life(20)
    enemies[1].increase_life(20)

    # Test 9 - Select target - wrong inputs should be ignored and repeated
    with mock.patch('Wizard.input', side_effect=[0, 'f', 1, '4', 6, 2]):
        assert w1.select_target(enemies) == enemies[0]
        assert w1.select_target(enemies) == enemies[1]
    # Kill alll enemies
    for enemy in enemies:
        enemy.reduce_life(100)

    assert w1.select_target(enemies) == None

    # Test 10 - Test Player Action
    random.seed(110)
    player = Wizard("Dumbledore", player=True)
    allies = [Wizard("Phil"), Wizard("Jim"), Wizard("Tom", hp=100)]

    for enemy in enemies:
        enemy.increase_life(100)

    with mock.patch('Wizard.input', side_effect=[1, 2, 3]):

        player.player_action("f", 1, enemies, allies)
        assert enemies[0].check_life() == 15

        allies[1].reduce_life(15)
        assert player.player_action("1", 1, enemies, allies) == True
        print(allies[1].check_life())
        assert allies[1].check_life() == 17

        assert player.player_action("2", 1, enemies, allies) == True
        assert enemies[2].check_life() == 15

    for ally in allies:
        ally.reduce_life(10)

    assert player.player_action("r", 1, enemies, allies) == True
    assert player.get_mana() == 100

    assert player.player_action("3", 1, enemies, allies) == True
    assert allies[0].check_life() == 20
    assert allies[1].check_life() == 20
    assert allies[2].check_life() == 100

    assert player.player_action("4", 1, enemies, allies) == True
    assert player.check_life() == 12
    assert player.get_mana() == 20
    assert enemies[0].check_life() == 0
    assert enemies[1].check_life() == 0
    assert enemies[2].check_life() == 0
    assert enemies[3].check_life() == 82

    assert player.player_action("a", 1, enemies, allies) == False
    assert player.player_action("7", 1, enemies, allies) == False

    # Test 11 - Test Player turn
    random.seed(83)
    enemies[0].increase_life(100)
    # If not player, shouldn't be able to make player turn
    assert w1.player_turn(1, enemies) == None

    # If no alive enemies, should return None
    enemies[0].reduce_life(100)
    enemies[3].reduce_life(100)
    assert player.player_turn(1, enemies) == None

    for enemy in enemies:
        enemy.increase_life(100)
    for ally in allies:
        ally.reduce_life(10)
    player.increase_mana(100)
    # Test different player inputs

    with mock.patch('Wizard.input', side_effect=["f", "1", "1", "2", "1", "2", "2", "3", "r", "3", "4"]):
        player.player_turn(1, enemies, allies)
        assert enemies[0].check_life() == 13

        allies[1].reduce_life(15)
        player.player_turn(1, enemies, allies)
        assert allies[2].check_life() == 97

        player.player_turn(1, enemies, allies)
        player.player_turn(1, enemies, allies)
        assert enemies[2].check_life() == 19

        for ally in allies:
            ally.reduce_life(10)

        player.player_turn(1, enemies, allies)
        assert player.get_mana() == 100

        player.player_turn(1, enemies, allies)
        assert allies[0].check_life() == 0
        assert allies[1].check_life() == 0
        assert allies[2].check_life() == 100

        player.player_turn(1, enemies, allies)
        assert player.check_life() == 6
        assert player.get_mana() == 20
        assert enemies[0].check_life() == 0
        assert enemies[1].check_life() == 0
        assert enemies[2].check_life() == 0
        assert enemies[3].check_life() == 83
        player.increase_mana(100)


if __name__ == "__main__":
    test()
