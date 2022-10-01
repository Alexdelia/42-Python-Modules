#!/usr/bin/env python3

import sys
from time import sleep
from typing import Callable

from loading import ft_progress

if __name__ != "__main__":
    sys.exit()


def test(name: str, listy: range, f: Callable[[int], int], sleep_time: float = 0.01) -> None:
    """
    This function tests the ft_progress function.
    """
    print(f">> \033[1;3;36mTEST {name}\033[0m")
    ret = 0
    for item in ft_progress(listy):
        if type(item) is int:
            ret += f(item)
        sleep(sleep_time)
    print("\n>>\033[1;3;32m",
          [f"{ret}", f"{ret:e}"][ret > 1000000],
          end="\033[0m\n\n")

def test_w(name: str, listy: range, f: Callable[[int], int], w: int, sleep_time: float = 0.01) -> None:
    """
    This function tests the ft_progress function with a custom width.
    """
    print(f">> \033[1;3;36mTEST {name} (width {w})\033[0m")
    ret = 0
    for item in ft_progress(listy, w):
        ret += f(item)
        sleep(sleep_time)
    print(f"\n>> \033[1;3;32m{ret}\033[0m\n")

def test_w_fill_tip(name: str, listy: range, f: Callable[[int], int], w: int, fill: str, tip: str, sleep_time: float = 0.01) -> None:
    """
    This function tests the ft_progress function with a custom width, fill and tip.
    """
    print(f">> \033[1;3;36mTEST {name} (width: {w}, fill '{fill}', tip: '{tip}')\033[0m")
    ret = 0
    for item in ft_progress(listy, w, fill, tip):
        ret += f(item)
        sleep(sleep_time)
    print(f"\n>> \033[1;3;32m{ret}\033[0m\n")

test("0", range(1000), lambda x: (x + 3) % 5, 0.01)
test("1", range(3333), lambda x: x, 0.005)
test("2", range(100), lambda x: x * x)
test_w("3", range(1000), lambda x: x, 10)
test_w("4", range(1000), lambda x: x, 0)
test_w("5", range(1000), lambda x: x, -10)
test("6 (range(0))", range(0), lambda x: x, 1)
test("7 (range(1))", range(1), lambda x: x, 1)
test("8 (range(2))", range(2), lambda x: x, 1)
test("9 (range(3))", range(3), lambda x: x, 1)
test("10 ([])", [], lambda x: x, 1)
try:
    test("11 (None)", None, lambda x: x, 1)
except TypeError:
    print(">> \033[1;3;31mTypeError\t[KO]\033[0m\n")
test("12 (str)", "Hello World!", lambda x: 0, 0.1)
test("13 (x**x + sleep(0)", range(100), lambda x: x**x, 0)
test_w_fill_tip("14 (width: 10, fill: '>', tip: '=')", range(1000), lambda x: x, 10, '>', '=')
test_w_fill_tip("15 (width: 10, fill: '█', tip: ' ')", range(1000), lambda x: x, 10, '█', ' ')
