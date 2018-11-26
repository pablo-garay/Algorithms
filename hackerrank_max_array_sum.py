#!/bin/python

import math
import os
import random
import re
import sys


def maxSubsetSum(arr):
    if max(arr) < 0:
        return max(arr)

    n = len(arr)
    opt = [None] * (n + 2)
    opt[n + 1] = opt[n] = 0

    for i in reversed(xrange(0, n)):
        opt[i] = max(arr[i] + opt[i + 2], opt[i + 1])

    return opt[0]


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(raw_input())
#     arr = map(int, raw_input().rstrip().split())
#     res = maxSubsetSum(arr)
#     fptr.write(str(res) + '\n')
#     fptr.close()


print maxSubsetSum([3, 7, 4, 6, 5])  # output: 13
print maxSubsetSum([2, 1, 5, 8, 4])  # output: 11
print maxSubsetSum([3, 5, -7, 8, 10])  # output: 15
print maxSubsetSum([-231, -23, -7, -8, -10])  # output: -7

