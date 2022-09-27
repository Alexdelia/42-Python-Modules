#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

s = " ".join(sys.argv[1:])
if s:
    print(s[::-1].swapcase())
