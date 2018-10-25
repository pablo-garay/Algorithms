#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0

    for num in arr:
        if num in r3:
            count += r3[num]

        if num in r2:
            r3[num * r] += r2[num]

        r2[num * r] += 1

    return count

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nr = raw_input().rstrip().split()
#     n = int(nr[0])
#     r = int(nr[1])
#     arr = map(long, raw_input().rstrip().split())
#     ans = countTriplets(arr, r)
#     fptr.write(str(ans) + '\n')
#     fptr.close()


print countTriplets([1, 2, 2, 4], 2)  # output: 2
print countTriplets([1, 3, 9, 9, 27, 81], 3)  # output: 6
print countTriplets([1, 5, 5, 25, 125], 5)  # output: 4
print countTriplets([1, 1, 1, 125], 1)  # output: 1
print countTriplets([1, 1, 1, 1, 125], 1)  # output: 4
print countTriplets([1, 1, 1, 1, 125, 125, 125], 1)  # output: 5
print countTriplets([1, 2, 1, 2, 4], 2)  # output: 3

