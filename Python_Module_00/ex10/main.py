#!/usr/bin/env python3

import sys
from time import sleep

from loading import ft_progress

if __name__ != "__main__":
    sys.exit()

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
