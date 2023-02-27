#!/usr/bin/env python3

import pytest
from the_bank import Account, Bank

if __name__ == "__main__":
    pytest.main(args=["-v", __file__])


def test_subject_1():
    bank = Bank()
    bank.add(
        Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
    )
    bank.add(
        Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None,
            other='This is the vice president of the corporation'
        )
    )

    assert bank.transfer('William John', 'Smith Jane', 545.0) is False


def test_subject_2():
    bank = Bank()
    bank.add(
        Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        )
    )
    bank.add(
        Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None
        )
    )

    assert bank.transfer('William John', 'Smith Jane', 1000.0) is False

    bank.fix_account('William John')
    bank.fix_account('Smith Jane')

    assert bank.transfer('William John', 'Smith Jane', 1000.0) is True


ACT_NAME = "John Doe"


@pytest.fixture(scope="function")
def account_args():
    return {
        "name": "John Doe",
        "zip": "444-222",
        "value": 42000.0,
        "ref": "42",
    }


def test_bank_add_basic(account_args):
    bank = Bank()
    a = Account(**account_args)

    assert bank.add(a)

    assert not bank.add(a)


# def test_bank_add_invalid(account_args):
#     bank = Bank()

# def test_evaluator_basic(words, coefs):
#     assert Evaluator.zip_evaluate(coefs, words) == 32.0

#     assert Evaluator.enumerate_evaluate(coefs, words) == 32.0

# def test_evaluator_empty():
#     words = []
#     coefs = []

#     assert Evaluator.zip_evaluate(coefs, words) == 0.0

#     assert Evaluator.enumerate_evaluate(coefs, words) == 0.0

# def test_evaluator_int(words, coefs):
#     coefs = [int(c) for c in coefs]

#     assert Evaluator.zip_evaluate(coefs, words) == 29

#     assert Evaluator.enumerate_evaluate(coefs, words) == 29

# def test_evaluator_negative(words, coefs):
#     coefs = [-c for c in coefs]

#     assert Evaluator.zip_evaluate(coefs, words) == -32.0

#     assert Evaluator.enumerate_evaluate(coefs, words) == -32.0

# def test_evaluator_invalid_type():
#     with pytest.raises(TypeError):
#         Evaluator.zip_evaluate([42.0], [42.0])  # type: ignore

#     with pytest.raises(TypeError):
#         Evaluator.enumerate_evaluate([42.0], [42.0])  # type: ignore

#     with pytest.raises(TypeError):
#         Evaluator.zip_evaluate(["42"], ["42"])  # type: ignore

#     with pytest.raises(TypeError):
#         Evaluator.enumerate_evaluate(["42"], ["42"])  # type: ignore

# def test_evaluator_invalid_len(words, coefs):
#     coefs = coefs[:-1]

#     assert Evaluator.zip_evaluate(coefs, words) == -1

#     assert Evaluator.enumerate_evaluate(coefs, words) == -1

#     coefs += [1.0, 1.0]

#     assert Evaluator.zip_evaluate(coefs, words) == -1

#     assert Evaluator.enumerate_evaluate(coefs, words) == -1
