#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the pairs function below.
def pairs(k, arr):
    total_pairs = 0
    num_count = Counter(arr)

    for n in arr:
        if n + k in num_count:
            total_pairs += num_count[n + k]

    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = map(int, raw_input().rstrip().split())
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
