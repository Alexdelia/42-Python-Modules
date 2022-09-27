#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

if len(sys.argv) == 1:
    print("usage:\t\033[1m" + __file__, "\033[35m<number1> <number2>\033[0m")
    sys.exit()
elif len(sys.argv) != 3:
    print(
        f"\033[1;31mAssertionError:\033[35m\t{len(sys.argv) - 1}\033[0m \033[31marguments provided, expected \033[1;35m2\033[0m")
    sys.exit()

try:
    x = int(sys.argv[1])
except ValueError:
    print(
        f"\033[1;31mAssertionError:\033[35m\t{sys.argv[1]}\033[0m \033[31mis not an integer\033[0m")
    sys.exit()
try:
    y = int(sys.argv[2])
except ValueError:
    print(
        f"\033[1;31mAssertionError:\033[35m\t{sys.argv[2]}\033[0m \033[31mis not an integer\033[0m")
    sys.exit()

print(f"\033[1mSum:\033[0m\t\t\033[1;35m{x + y}\033[0m")
print(f"\033[1mDifference:\033[0m\t\033[1;35m{x - y}\033[0m")
print(f"\033[1mProduct:\033[0m\t\033[1;35m{x * y}\033[0m")
print("\033[1mQuotient:\033[0m\t", end="")
try:
    print(f"\033[1;35m{x / y}\033[0m")
except ZeroDivisionError:
    print("\033[1;31mERROR\033[0m\t\033[31m(division by zero)\033[0m")
print("\033[1mRemainder:\033[0m\t", end="")
try:
    print(f"\033[1;35m{x % y}\033[0m")
except ZeroDivisionError:
    print("\033[1;31mERROR\033[0m\t\033[31m(modulo by zero)\033[0m")
