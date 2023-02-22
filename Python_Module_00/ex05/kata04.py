#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

kata = (0, 4, 132.42222, 10000, 12345.67)

print(
    f"module_{kata[0]:02d}, ex_{kata[1]:02d} :",
    f"{kata[2]:0>3.2f}, {kata[3]:0>3.2e}, {kata[4]:0>3.2e}"
)
