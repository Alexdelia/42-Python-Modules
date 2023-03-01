#!/usr/bin/env python3

import pytest
from the_bank import Account, Bank

if hasattr(Bank, "_is_corrupted"):
    is_corrupted = Bank._is_corrupted
else:

    def is_corrupted(account: Account) -> bool:
        """ Check if an account is corrupted
            @account:   Account() account to check
            @return     True if corrupted, False if not
        """
        # even number of attributes
        if len(account.__dict__) % 2 == 0:
            return True

        # attribute starting with b
        if any(attr.startswith("b") for attr in account.__dict__):
            return True

        # no attribute starting with zip or addr
        if not any(attr.startswith("zip") or attr.startswith("addr")
                   for attr in account.__dict__):
            return True

        # attribute name, id, value
        for a, t in (
            ("name", str),
            ("id", int),
            ("value", (int, float)),
        ):
            if a not in account.__dict__ or \
                    not isinstance(account.__dict__[a], t):
                return True

        return False


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
    assert not is_corrupted(a)

    assert bank.add(a)
    assert not bank.add(a)
    assert bank.transfer(a.name, a.name, 42.0)


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
    assert not is_corrupted(bob)
    assert bank.add(bob)
    assert bank.accounts[0].value == BOB_VALUE

    A_VALUE = account_args["value"]
    a = Account(**account_args)
    assert not is_corrupted(a)
    assert bank.add(a)
    assert bank.accounts[1].value == A_VALUE

    for src, dst, amount, values, success in (
        (
            a.name,
            a.name,
            42.0,
            ((1, A_VALUE), (0, BOB_VALUE)),
            True,
        ),
        (
            a.name,
            bob.name,
            42.0,
            ((1, A_VALUE - 42.0), (0, BOB_VALUE + 42.0)),
            True,
        ),
        (
            bob.name,
            a.name,
            42,
            ((1, A_VALUE), (0, BOB_VALUE)),
            True,
        ),
        (
            bob.name,
            a.name,
            BOB_VALUE * 2,
            ((1, A_VALUE), (0, BOB_VALUE)),
            False,
        ),
        (
            bob.name,
            a.name,
            -42.0,
            ((1, A_VALUE), (0, BOB_VALUE)),
            False,
        ),
        (
            bob.name,
            a.name,
            0.0,
            ((1, A_VALUE), (0, BOB_VALUE)),
            True,
        ),
        (
            bob.name,
            a.name,
            BOB_VALUE,
            ((1, A_VALUE + BOB_VALUE), (0, 0.0)),
            True,
        ),
    ):
        assert bank.transfer(src, dst, amount) == success, \
            f"transfer({src}, {dst}, {amount}) should return {success}"

        for i, v in values:
            assert bank.accounts[i].value == v, \
                f"after transfer({src}, {dst}, {amount}), " \
                f"account {i} should have value {v}"


def _seen_corrupted(account: Account) -> bool:
    bank = Bank()
    assert bank.add(account)
    if hasattr(account, "value"):
        assert bank.accounts[0].value == account.value

    dummy = Account(
        name="dummy",
        zip="123-456",
        value=42.0,
        ref="42",
    )
    assert not is_corrupted(dummy)
    assert bank.add(dummy)
    assert bank.accounts[1].value == 42.0

    r = not bank.transfer(dummy.name, account.name, 42.0)
    assert not bank.transfer(account.name, dummy.name, 42.0) == r
    return r


@pytest.mark.parametrize(
    "corrupt",
    (
        {
            "name": "corrupted",
            "zip": "123-456",
            "value": 42.0,
            "ref": "42",
            "uneven": "corrupted",
        },
        {
            "name": "corrupted",
            "zip": "123-456",
            "value": 42.0,
            "bref": "42",
        },
        {
            "name": "corrupted",
            "no_zip": "123-456",
            "value": 42.0,
            "ref": "42",
        },
        {
            "name": "corrupted",
            "no_addr": "123-456",
            "value": 42.0,
            "ref": "42",
        },
    ),
    ids=(
        "uneven",
        "b",
        "no zip",
        "no addr",
    ),
)
def test_bank_corupted(corrupt):
    bank = Bank()

    c = Account(**corrupt)
    assert is_corrupted(c)
    assert _seen_corrupted(c)

    assert bank.add(c)
    assert bank.fix_account(c.name)
    assert not is_corrupted(c)
    assert not _seen_corrupted(c)


@pytest.mark.parametrize(
    ("key", "value", "expected"),
    (
        ("name", 42, "42"),
        ("value", "81000", (0, 0.0)),
        ("id", "42", None),
    ),
    ids=(
        "name int",
        "value str",
        "id str",
    ),
)
def test_bank_advanced_corupted(account_args, key, value, expected):
    bank = Bank()

    c = Account(**account_args)
    assert not is_corrupted(c)
    assert not _seen_corrupted(c)

    c.__dict__[key] = value
    assert is_corrupted(c)
    assert _seen_corrupted(c)

    assert bank.add(c)
    assert bank.fix_account(c.name)
    assert not is_corrupted(c)
    assert not _seen_corrupted(c)

    if expected is not None:
        if isinstance(expected, tuple):
            assert any(c.__dict__[key] == v for v in expected)
        else:
            assert c.__dict__[key] == expected
