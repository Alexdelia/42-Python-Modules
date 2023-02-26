# subject code
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:   Account() new account to append
            @return         True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts

        if not isinstance(new_account, Account):
            return False

        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:    str(name) of the first account
            @dest:      str(name) of the destination account
            @amount:    float(amount) amount to transfer
            @return     True if success, False if an error occured
        """
        # ... Your code ...

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:      str(name) of the account
            @return     True if success, False if an error occured
        """
        # ... Your code ...

    def _get_account(self, name: str) -> Account | None:
        """ Get the account associated to name
            @name:      str(name) of the account
            @return     Account() if found, None if not
        """
        return next(filter(lambda x: x.name == name, self.accounts), None)

    def _is_corrupted(self, account: Account) -> bool:
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
        for a, t in [
            ("name", str),
            ("id", int),
            ("value", (int, float)),
        ]:
            # fix
            if not hasattr(account, a) \
                    or not isinstance(getattr(account, a), t):
                return True

        return False
