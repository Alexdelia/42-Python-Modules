#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for i in kata.items():
    print(f"{i[0]} was created by {i[1]}")
