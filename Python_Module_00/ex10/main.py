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
        ret += f(item)
        sleep(sleep_time)
    print(f"\n>> \033[1;3;32m{ret}\033[0m\n")

listy = range(1000)
test("0", listy, lambda x: (x + 3) % 5, 0.01)
print("TEST 0")
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)

print("TEST 1")
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
