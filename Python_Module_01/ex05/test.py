#!/usr/bin/env python3

import pytest
from the_bank import Account, Bank

if __name__ == "__main__":
    pytest.main(args=["-v", __file__])


def test_subject_1():
    bank = Bank()
    assert bank.add(
        Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            bref='1044618427ff2782f0bbece0abd05f31'
        )
    )
    assert bank.add(
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
    assert bank.add(
        Account(
            'Smith Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        )
    )
    assert bank.add(
        Account(
            'William John',
            zip='100-064',
            value=6460.0,
            ref='58ba2b9954cd278eda8a84147ca73c87',
            info=None
        )
    )

    print([a.name for a in bank.accounts])

    assert bank.transfer('William John', 'Smith Jane', 1000.0) is False

    assert bank.fix_account('William John')
    assert bank.fix_account('Smith Jane')

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
    assert bank.transfer(a.name, a.name, 0.0)


def test_bank_add_invalid(account_args):
    bank = Bank()

    for a in (
            "invalid",
            42,
            None,
    ):
        assert not bank.add(a), f"add({a}) should return False"  # type: ignore


def test_bank_transfer_basic(account_args):
    bank = Bank()
    BOB_VALUE = 1000.0
    bob = Account(
        "Bob",
        zip="123-456",
        value=BOB_VALUE,
        ref="42",
    )
    assert bank.add(bob)
    assert bank.accounts[0].value == BOB_VALUE

    A_VALUE = account_args["value"]
    a = Account(**account_args)
    assert bank.add(a)
    assert bank.accounts[1].value == A_VALUE

    for src, dst, amount, src_new_value, dst_new_value, success in (
        (a.name, a.name, 42.0, A_VALUE, A_VALUE, True),
        (a.name, bob.name, 42.0, BOB_VALUE + 42.0, A_VALUE - 42.0, True),
        (bob.name, a.name, 42, BOB_VALUE, A_VALUE, True),
        (bob.name, a.name, BOB_VALUE * 2, BOB_VALUE, A_VALUE, False),
        (bob.name, a.name, -42.0, BOB_VALUE, A_VALUE, False),
        (bob.name, a.name, 0.0, BOB_VALUE, A_VALUE, True),
        (bob.name, a.name, BOB_VALUE, 0.0, A_VALUE, True),
    ):
        assert bank.transfer(src, dst, amount) == success, \
            f"transfer({src}, {dst}, {amount}) should return {success}"
        src_i = 0 if src == a.name else 1
        dst_i = 1 if dst == bob.name else 0
        assert bank.accounts[src_i].value == src_new_value, \
            f"transfer({src}, {dst}, {amount})\
 should change {src} value to {src_new_value}"
        assert bank.accounts[dst_i].value == dst_new_value, \
            f"transfer({src}, {dst}, {amount})\
 should change {dst} value to {dst_new_value}"


def test_bank_transfer_invalid(account_args):
    bank = Bank()
    bob = Account(
        "Bob",
        zip="123-456",
        value=1000.0,
        ref="42",
    )
    assert bank.add(bob)

    for k, v in (
        ("name", 42),
        ("value", -42),
    ):
        pass


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
