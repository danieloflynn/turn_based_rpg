from Creatures import Creature
from Battle import Battle
from unittest import mock
import random


def test():
    Creature.delay = 0
    Battle.round_delay = 0
    # Test 1 - initialise battle
    with mock.patch('Battle.input', side_effect=["10", "a", "1", "Dan"]):

        b = Battle()

        assert b.enemies[0].check_life() == 50
        assert b.enemies[1].check_life() == 80
        assert b.enemies[2].check_life() == 15
        assert b.enemies[3].check_life() == 50

        assert b.allies[0].check_life() == 50
        assert b.allies[1].check_life() == 30
        assert b.allies[2].check_life() == 50
        assert b.allies[3].check_life() == 10
        assert b.allies[4].check_life() == 20
        assert b.allies[4] == b.players[0]

        assert b.boss.check_life() == 200

    # Test 2 - check winner

    # Should return false currently
    assert b.check_winner() == False

    # Should return true if player dead
    b.players[0].reduce_life(100)
    assert b.check_winner() == True

    # Should return false as boss not dead
    b.players[0].increase_life(100)
    for enemy in b.enemies:
        enemy.reduce_life(100)
    assert b.check_winner() == False

    b.boss.reduce_life(200)
    assert b.check_winner() == True

    # If no player should return True only when all allies dead
    with mock.patch('Battle.input', side_effect=["0"]):

        b = Battle()

    assert b.check_winner() == False

    for ally in b.allies:
        ally.reduce_life(100)

    assert b.check_winner() == True

    # Test 3 - sort by speed
    b.sort_by_speed(b.allies)

    curr_speed = b.allies[0].get_speed()
    for ally in b.allies[1:]:
        assert ally.get_speed() <= curr_speed
        curr_speed = ally.get_speed()

    # Test 4 - count alive
    assert b.count_alive(b.allies) == 0
    assert b.count_alive(b.enemies) == 4

    # Test 5 - add boss
    b.add_boss()

    assert len(b.enemies) == 5

    # Adding twice does nothing
    b.add_boss()
    assert len(b.enemies) == 5

    # Can't really test start.


if __name__ == "__main__":
    test()
