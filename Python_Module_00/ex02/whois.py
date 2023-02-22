#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

if len(sys.argv) == 1:
    print("usage:\t\033[1m" + __file__, "\033[35m<number>\033[0m")
    sys.exit()
elif len(sys.argv) > 2:
    print(
        f"\033[1;31mAssertionError:\033[35m\t{len(sys.argv) - 1}\033[0m",
        "\033[31marguments provided, expected \033[1;35m1\033[0m"
    )
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print(
        f"\033[1;31mAssertionError:\033[35m\t{sys.argv[1]}\033[0m",
        "\033[31mis not an integer\033[0m"
    )
    sys.exit()

print("I'm", [["Even", "Odd"][n % 2], "Zero"][n == 0] + ".")
