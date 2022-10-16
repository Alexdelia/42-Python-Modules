#!/usr/bin/env python3

import random


def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    text = text.split(sep)
    if option == "shuffle":
        text = sorted(text, key = lambda x: random.random())
    elif option == "unique":
        text = set(text)
    elif option == "ordered":
        text = sorted(text)

    for word in text:
        yield word


if __name__ == "__main__":
    text = "some text with several words"
    for word in generator(text):
        print(word)
    print()


