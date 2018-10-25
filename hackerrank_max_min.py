#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    unf = arr[len(arr) - 1] - arr[0]

    for i in xrange(len(arr) - k):
        diff = arr[i + k - 1] - arr[i]
        # print "current diff:", diff
        if diff < unf:
            unf = diff

        if diff == 0:
            break

    return unf

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(raw_input())
#     k = int(raw_input())
#     arr = []
#
#     for _ in xrange(n):
#         arr_item = int(raw_input())
#         arr.append(arr_item)
#
#     result = maxMin(k, arr)
#     fptr.write(str(result) + '\n')
#     fptr.close()

print maxMin(3, [10, 100, 300, 200, 1000, 20, 30])
print maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200])
print maxMin(2, [1, 2, 1, 2, 1])