#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = abs(arr[0] - arr[1])

    for i in xrange(len(arr) - 1):
        if abs(arr[i + 1] - arr[i]) < min_diff:
            min_diff = abs(arr[i + 1] - arr[i])

        if min_diff == 0:
            break

    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
