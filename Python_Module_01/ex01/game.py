from typing import Optional


class GoTCharacter:

    def __init__(
        self,
        first_name: str | None,
        is_alive: bool = True,
    ):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GoTCharacter):
    """A class representing the Stark family.\
Or when bad things happen to good people."""

    def __init__(
        self,
        first_name: Optional[str] = None,
        is_alive: bool = True,
    ):
        super().__init__(first_name, is_alive)
        self.family_name = self.__class__.__name__
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
