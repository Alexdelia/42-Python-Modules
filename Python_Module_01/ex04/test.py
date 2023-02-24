#!/usr/bin/env python3

import pytest
from eval import Evaluator

if __name__ == "__main__":
    pytest.main(args=["-v", __file__])


@pytest.fixture(scope="function")
def words():
    return ["Le", "Lorem", "Ipsum", "est", "simple"]


@pytest.fixture(scope="function")
def coefs():
    return [1.0, 2.0, 1.0, 4.0, 0.5]


def test_evaluator_basic(words, coefs):
    assert Evaluator.zip_evaluate(coefs, words) == 32.0

    assert Evaluator.enumerate_evaluate(coefs, words) == 32.0


def test_evaluator_empty():
    words = []
    coefs = []

    assert Evaluator.zip_evaluate(coefs, words) == 0.0

    assert Evaluator.enumerate_evaluate(coefs, words) == 0.0


def test_evaluator_int(words, coefs):
    coefs = [int(c) for c in coefs]

    assert Evaluator.zip_evaluate(coefs, words) == 29

    assert Evaluator.enumerate_evaluate(coefs, words) == 29


def test_evaluator_negative(words, coefs):
    coefs = [-c for c in coefs]

    assert Evaluator.zip_evaluate(coefs, words) == -32.0

    assert Evaluator.enumerate_evaluate(coefs, words) == -32.0


def test_evaluator_invalid_type():
    with pytest.raises(TypeError):
        Evaluator.zip_evaluate([42.0], [42.0])  # type: ignore

    with pytest.raises(TypeError):
        Evaluator.enumerate_evaluate([42.0], [42.0])  # type: ignore

    with pytest.raises(TypeError):
        Evaluator.zip_evaluate(["42"], ["42"])  # type: ignore

    with pytest.raises(TypeError):
        Evaluator.enumerate_evaluate(["42"], ["42"])  # type: ignore


def test_evaluator_invalid_len(words, coefs):
    coefs = coefs[:-1]

    assert Evaluator.zip_evaluate(coefs, words) == -1

    assert Evaluator.enumerate_evaluate(coefs, words) == -1

    coefs += [1.0, 1.0]

    assert Evaluator.zip_evaluate(coefs, words) == -1

    assert Evaluator.enumerate_evaluate(coefs, words) == -1
