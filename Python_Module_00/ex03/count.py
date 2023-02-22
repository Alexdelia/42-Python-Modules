#!/usr/bin/env python3

import sys
from string import punctuation


def text_analyzer(text: str = ""):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """

    if type(text) != str:
        print(
            f"\033[1;31mAssertionError:\033[35m\t{text}\033[0m",
            "\033[31mis not a string\033[0m"
        )
        return

    if text == "":
        text = input("What is the text to analyse?\n>> ")
    print("The text contains", len(text), "character(s):")
    print("-", sum(1 for c in text if c.isupper()), "upper letter(s)")
    print("-", sum(1 for c in text if c.islower()), "lower letter(s)")
    print("-", sum(1 for c in text if c in punctuation), "punctuation mark(s)")
    print("-", sum(1 for c in text if c.isspace()), "space(s)")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(
            f"\033[1;31mAssertionError:\033[35m\t{len(sys.argv) - 1}\033[0m",
            "\033[31marguments provided, expected \033[1;35m1\033[0m"
        )
        sys.exit()
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
