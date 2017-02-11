#!/usr/bin/python

import sys


for n in sys.stdin.readlines():
    spl = n.split()
    print(spl[-1])

