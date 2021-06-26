import pytest
from game_of_greed.game_logic import GameLogic

def test_2_dice():
    values = GameLogic.roll_dice(2)
    assert len(values) == 2

    for value in values:
        assert 1 <= value <= 6


def test_3_dice():
    values = GameLogic.roll_dice(3)
    assert len(values) == 3

    for value in values:
        assert 1 <= value <= 6


def test_4_dice():
    values = GameLogic.roll_dice(4)
    assert len(values) == 4

    for value in values:
        assert 1 <= value <= 6


def test_5_dice():
    values = GameLogic.roll_dice(5)
    assert len(values) == 5

    for value in values:
        assert 1 <= value <= 6


def test_6_dice():
    values = GameLogic.roll_dice(6)
    assert len(values) == 6

    for value in values:
        assert 1 <= value <= 6
 
