#!/usr/bin/env python3

import pytest
from generator import generator

if __name__ == "__main__":
    pytest.main(args=["-v", __file__])


def test_generator_basic():
    text = "Le Lorem Ipsum est simplement du faux texte."
    assert list(generator(text)) == [
        "Le",
        "Lorem",
        "Ipsum",
        "est",
        "simplement",
        "du",
        "faux",
        "texte.",
    ]


def test_generator_shuffle():
    text = "Le Lorem Ipsum est simplement du faux texte."
    available: set[str] = set(text.split())
    found: list[str] = []

    assert len(available) == 8

    for word in generator(text, option="shuffle"):
        # it will raise a KeyError if word is not in available
        available.remove(word)
        found.append(word)

    assert not available

    assert len(found) == 8
    assert found != text.split()


def test_generator_ordered():
    text = "Le Lorem Ipsum est simplement du faux texte."
    assert list(generator(text, option="ordered")) == [
        "Ipsum",
        "Le",
        "Lorem",
        "du",
        "est",
        "faux",
        "simplement",
        "texte.",
    ]


def test_generator_unique():
    text = "I am Sam. Sam I am and ham.\
 I do not like green eggs and ham."

    assert list(generator(text, option="unique")) == [
        "I",
        "am",
        "Sam.",
        "Sam",
        "and",
        "ham.",
        "do",
        "not",
        "like",
        "green",
        "eggs",
    ]


def test_generator_sep():
    text = "Le.Lorem.Ipsum.est.simplement.du.faux.texte."
    assert list(generator(text, sep=".")) == [
        "Le",
        "Lorem",
        "Ipsum",
        "est",
        "simplement",
        "du",
        "faux",
        "texte",
        "",
    ]


def test_generator_sep_and_option():
    text = "Le.Lorem.Ipsum.est.simplement.du.faux.texte."
    assert list(generator(text, sep=".", option="ordered")) == [
        "",
        "Ipsum",
        "Le",
        "Lorem",
        "du",
        "est",
        "faux",
        "simplement",
        "texte",
    ]


def test_generator_text_invalid():
    assert list(generator(42)) == ["ERROR"]  # type: ignore

    assert list(generator(["42"])) == ["ERROR"]  # type: ignore

    assert list(generator({42: 42})) == ["ERROR"]  # type: ignore

    assert list(generator((42, 42))) == ["ERROR"]  # type: ignore

    assert list(generator({42})) == ["ERROR"]  # type: ignore

    assert list(generator(None)) == ["ERROR"]  # type: ignore

    assert list(generator(True)) == ["ERROR"]  # type: ignore

    assert list(generator(b"42")) == ["ERROR"]  # type: ignore

    assert list(generator(42.42)) == ["ERROR"]  # type: ignore


def test_generator_sep_invalid():
    assert list(generator(
        "some text",
        sep=42,  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep=["42"],  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep={42: 42},  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep=(42, 42),  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep={42},  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep=None,  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep=True,  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep=b"42",  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        sep=42.42,  # type: ignore
    )) == ["ERROR"]

    with pytest.raises(ValueError):
        list(generator("some text", sep=""))


def test_generator_option_invalid():
    assert list(generator(
        "some text",
        option=42,  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option=["42"],  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option={42: 42},  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option=(42, 42),  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option={42},  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option=True,  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option=b"42",  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option=42.42,  # type: ignore
    )) == ["ERROR"]

    assert list(generator(
        "some text",
        option="invalid",  # type: ignore
    )) == ["ERROR"]
