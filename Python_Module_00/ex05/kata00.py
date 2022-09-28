#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

kata = (19, 42, 21)
print(f"The {len(kata)} numbers are:", ", ".join(str(x) for x in kata))
