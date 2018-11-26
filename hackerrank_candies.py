#!/bin/python

import math
import os
import random
import re
import sys


def candies(n, arr):
    output = [1] * n

    for i in xrange(n):
        if i > 0 and arr[i] > arr[i - 1] and output[i] <= output[i - 1]:
            output[i] = output[i - 1] + 1
        if (i + 1) < n and arr[i] > arr[i + 1] and output[i] <= output[i + 1]:
            output[i] = output[i + 1] + 1

    for i in xrange(n - 1, -1, -1):
        if (i + 1) < n and arr[i] > arr[i + 1] and output[i] <= output[i + 1]:
            output[i] = output[i + 1] + 1
        if i > 0 and arr[i] > arr[i - 1] and output[i] <= output[i - 1]:
            output[i] = output[i - 1] + 1

    # print arr  # for debugging
    # print output  # for debugging
    return sum(output)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(raw_input())
#     arr = []
#
#     for _ in xrange(n):
#         arr_item = int(raw_input())
#         arr.append(arr_item)
#
#     result = candies(n, arr)
#     fptr.write(str(result) + '\n')
#     fptr.close()

print candies(3, [1, 2, 2])  # 4
print candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1])  # 19
print candies(8, [2, 4, 3, 5, 2, 6, 4, 5])  # 12
print candies(10, [9, 2, 3, 6, 5, 4, 3, 2, 2, 2])  # 22
