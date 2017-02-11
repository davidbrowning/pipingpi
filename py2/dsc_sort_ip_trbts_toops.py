#!/usr/bin/python
from __future__ import print_function
from operator import itemgetter
import sys
print('')
spl = []
for n in sys.stdin.readlines():
    spli = n.split()
    spli[-1] = (spli[-1])
    tp = (spli[0],spli[-1])
    spl.append(tp)
    #print(tp)
    #print(type(spl))

fin = (sorted(spl, key=lambda s: s[1]))
for line in fin:
    print(line)
#print(spl)
#for item in spl:
#    print(item)
