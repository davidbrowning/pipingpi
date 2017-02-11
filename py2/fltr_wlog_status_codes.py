#!/usr/bin/python
import sys

for n in sys.stdin.readlines():
    spl = n.split()
    if(spl[-2] == sys.argv[1]):
        print(spl[3]+' '+spl[4]+' '+spl[5]+' '+spl[6]+' '+spl[7])
