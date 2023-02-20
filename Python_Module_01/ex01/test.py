#!/usr/bin/env python3

import pytest
from game import GoTCharacter, Stark

if __name__ == "__main__":
    pytest.main(args=["-v", __file__])

FIRST_NAME = "Arya"
FAMILY_NAME = "Stark"
HOUSE_WORDS = "Winter is Coming"


def test_game_basic():
    arya = Stark(FIRST_NAME)
    assert arya.first_name == FIRST_NAME
    assert arya.is_alive is True
    assert arya.family_name == FAMILY_NAME
    assert arya.house_words == HOUSE_WORDS


def test_Stark_dict():
    arya = Stark(FIRST_NAME)
    assert arya.__dict__ == {
        "first_name": FIRST_NAME,
        "is_alive": True,
        "family_name": FAMILY_NAME,
        "house_words": HOUSE_WORDS,
    }


def test_GoTCharacter_dict():
    arya = GoTCharacter(FIRST_NAME)
    assert arya.__dict__ == {
        "first_name": FIRST_NAME,
        "is_alive": True,
    }


def test_print_house_words(capsys):
    arya = Stark(FIRST_NAME)
    arya.print_house_words()
    assert capsys.readouterr().out == HOUSE_WORDS + '\n'


def test_die():
    arya = Stark(FIRST_NAME)
    assert arya.is_alive
    arya.die()
    assert not arya.is_alive


def test_docstring():
    assert (
        Stark.__doc__ == """A class representing the Stark family.\
Or when bad things happen to good people."""
    )
