#!/usr/bin/python

## your code here


import sys


for n in sys.stdin.readlines():
    spl = n.split()
    tp = (spl[0],spl[-1])
    tp = str(tp).strip('()')
    tp = tp.replace("'","")
    tp = tp.replace(',',' ')
    print tp

