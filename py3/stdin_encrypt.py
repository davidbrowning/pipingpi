#!/usr/bin/python3
import sys
from encrypt_py3 import encrypt_text, code_separator
import re

enc = ''
for line in [line for line in sys.stdin.readlines() if re.match(r'\S+', line)]:
    enc += encrypt_text(line)

sys.stdout.write(enc)
sys.stdout.flush()


