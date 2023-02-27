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

        if not isinstance(new_account, Account) \
                or self._get_account(new_account.name) is not None \
                or Bank._is_corrupted(new_account):
            return False

        self.accounts.append(new_account)

        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:    str(name) of the first account
            @dest:      str(name) of the destination account
            @amount:    float(amount) amount to transfer
            @return     True if success, False if an error occured
        """
        if not isinstance(origin, str) \
                or not isinstance(dest, str) \
                or not isinstance(amount, (int, float)):
            return False

        if (src := self._get_account(origin)) is None \
                or (dst := self._get_account(dest)) is None:
            return False

        if src == dst:
            return True

        if amount < 0:
            return False

        if src.value < amount:
            return False

        src.transfer(-amount)
        dst.transfer(amount)

        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:      str(name) of the account
            @return     True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False

        if (account := self._get_account(name)) is None:
            return False

        if not Bank._is_corrupted(account):
            return True

        account = Bank._fix_name(name, account)
        account = self._fix_id(account)
        account = Bank._fix_value(account)
        account = Bank._fix_b(account)

        # cannot create a zip or addr attribute without any additional info
        if not any(attr.startswith("zip") or attr.startswith("addr")
                   for attr in account.__dict__):
            return False

        account = Bank._fix_even(account)

        return True

    @staticmethod
    def _fix_name(name: str, account: Account) -> Account:
        """ Fix the name of an account
            @name:      str(name) of the account
            @account:   Account() account to fix
            @return     Account() fixed account
        """
        if not isinstance(account.name, str):
            account.name = name
        return account

    def _fix_id(self, account: Account) -> Account:
        """ Fix the id of an account
            @account:   Account() account to fix
            @return     Account() fixed account
        """
        try:
            if not isinstance(account.__dict__["id"], int):
                account.__dict__["id"] = int(account.__dict__["id"])
        except Exception:  # if id is not in account.__dict__ or int() fails
            account.id = max(account.id for account in self.accounts) + 1

        return account

    @staticmethod
    def _fix_value(account: Account) -> Account:
        """ Fix the value of an account
            @account:   Account() account to fix
            @return     Account() fixed account
        """
        if "value" not in account.__dict__ or \
                not isinstance(account.__dict__["value"], (int, float)):
            account.__dict__["value"] = 0

        return account

    @staticmethod
    def _fix_b(account: Account) -> Account:
        """ Fix the b attributes of an account
            @account:   Account() account to fix
            @return     Account() fixed account
        """
        for b in (attr for attr in account.__dict__ if attr.startswith("b")):
            del account.__dict__[b]

        return account

    @staticmethod
    def _fix_even(account: Account) -> Account:
        """ Fix the even attributes of an account
            @account:   Account() account to fix
            @return     Account() fixed account
        """
        if len(account.__dict__) % 2 == 0:
            k = "_even"
            while k in account.__dict__:
                k += "_"
            account.__dict__[k] = 0

        return account

    def _get_account(self, name: str) -> Account | None:
        """ Get the account associated to name
            @name:      str(name) of the account
            @return     Account() if found, None if not
        """
        return next(filter(lambda x: x.name == name, self.accounts), None)

    @staticmethod
    def _is_corrupted(account: Account) -> bool:
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
            ("name", (str,)),
            ("id", (int,)),
            ("value", (int, float)),
        ):
            if a not in account.__dict__ \
                    or not any(
                        isinstance(account.__dict__[a], st) for st in t
                    ):
                return True

        return False
