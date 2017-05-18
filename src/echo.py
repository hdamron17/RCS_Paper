#! /usr/bin/env python

''' 
Hackertyper.net clone
'''

from os.path import join as pathjoin, abspath, dirname, normpath
import sys
from random import randint
from readchar import readkey


ASSETS_ROOT = normpath(pathjoin(dirname(abspath(sys.argv[0])), "..", "assets"))
MAX_JUMP = 3
FILENAME = "text.md"
END_KEYS = ['\x03', '\x04', '\x1a']

def main():
    with open(pathjoin(ASSETS_ROOT, FILENAME), "r") as fp:
        text = fp.read() + "\n\nQ.E.D."

    index = 0
    c = readkey()
    while index < len(text) and c not in END_KEYS:
        jump = randint(1, min(len(text)-index, MAX_JUMP))
        new_index = index + jump
        print(text[index:new_index], end='', flush=True)
        index = new_index
        c = readkey()
    print()

if __name__ == "__main__":
    main()
