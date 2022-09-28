#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

kata = "The right format"

print(f"{'-' * (42 - len(kata))}{kata}", end='')
