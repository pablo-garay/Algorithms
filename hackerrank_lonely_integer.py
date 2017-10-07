#!/bin/python

import sys
from collections import Counter

def lonely_integer(a):
    ht = Counter(a)
    for key in ht.keys():
        if ht[key] == 1:
            return key


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
print lonely_integer(a)
