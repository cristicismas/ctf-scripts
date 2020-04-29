#!/usr/bin/python

import sys

print(int(sys.argv[1][2:], 16).to_bytes(4, 'little'))
