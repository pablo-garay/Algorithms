#!/bin/python

import math
import os
import random
import re
import sys
from collections import deque

# O(N^2) time complexity solution
def riddle(arr):
    n = len(arr)
    max_wind_size = [0] * n
    results = [None] * n
    max_dict = {}

    for i in xrange(n):
        count = 1
        left, right = (i - 1, i + 1)

        while left >= 0 and arr[left] >= arr[i]:
            count += 1
            left -= 1

        while right < n and arr[right] >= arr[i]:
            count += 1
            right += 1

        max_wind_size[i] = count

    for i in xrange(n):
        size = max_wind_size[i]
        num = arr[i]

        if size not in max_dict:
            max_dict[size] = num
        elif num > max_dict[size]:
            max_dict[size] = num

    last = max_dict[n]
    for window_size in xrange(n, 0, -1):
        if window_size in max_dict and max_dict[window_size] > last:
            last = max_dict[window_size]
        results[window_size - 1] = last

    return results


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(raw_input())
#     arr = map(long, raw_input().rstrip().split())
#     res = riddle(arr)
#     fptr.write(' '.join(map(str, res)))
#     fptr.write('\n')
#     fptr.close()


print riddle([2, 6, 1, 12])  # output: 12 2 1 1
print riddle([1, 2, 3, 5, 1, 13, 3])  # output: 13 3 2 1 1 1 1
print riddle([3, 5, 4, 7, 6, 2])  # output: 7 6 4 4 3 2
print riddle([9, 9, 9, 9, 9])  # output: 9, 9, 9, 9, 9
print riddle([9, 9, 9, 6, 9])  # output: 9, 9, 9, 6, 6
print riddle([9, 9, 6, 9, 9])  # output: 9, 9, 6, 6, 6
print riddle([1])  # output: 1

