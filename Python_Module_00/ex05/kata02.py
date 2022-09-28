#!/usr/bin/env python3

import sys

if __name__ != "__main__":
    sys.exit()

kata = (2019, 9, 25, 3, 30)

print(f"{kata[1]:02d}/{kata[2]:02d}/{kata[0]:04d} {kata[3]:02d}:{kata[4]:02d}")
#print("%02d/%02d/%04d %02d:%02d" % (kata[1], kata[2], kata[0], kata[3], kata[4]))
#print("{:02d}/{:02d}/{:04d} {:02d}:{:02d}".format(kata[1], kata[2], kata[0], kata[3], kata[4]))
