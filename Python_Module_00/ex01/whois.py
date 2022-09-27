#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

if len(sys.argv) == 0:
    print("usage:\t\033[1m./whois.py \033[35m<number>\033[0m")
    sys.exit()
elif len(sys.argv) > 2:
    print(
        "\033[1;31mAssertionError:\033[0m\t\033[31mmore than one argument are provided\033[0m")
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print(
        "\033[1;31mAssertionError:\033[0m\t\033[31margument is not an integer\033[0m")
    sys.exit()

print([["I'm Even", "I'm Odd"][n % 2], "I'm Zero"][n == 0])
