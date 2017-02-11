#!/usr/bin/python
import sys
import re
## script: top_n.py
## description: retain top n lines from stdin
## author: vladimir kulyukin
## to run: python top_n.py 10
## to run: ./top_n.py 10
n = int(sys.argv[1])
count = 0
for line in sys.stdin.readlines():
    if count < n:
        sys.stdout.write(line)
        count += 1
    else:
        break
sys.stdout.flush()

        
        
