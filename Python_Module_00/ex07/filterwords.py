#!/usr/bin/env python3

import sys
from string import punctuation

if __name__ != "__main__":
    sys.exit()

if len(sys.argv) != 3:
    print("ERROR")
    sys.exit()

try:
    N = int(sys.argv[2])
except ValueError:
    print("ERROR")
    sys.exit()

s = sys.argv[1].translate(str.maketrans('', '', punctuation))
print([w for w in s.split() if len(w) > N])
