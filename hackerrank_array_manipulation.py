#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# O(n) solution
def arrayManipulation(n, queries):
    count = [0] * n
    max_num = 0

    for query in queries:
        a, b, k = query

        for i in xrange(a - 1, b):
            count[i] += k
            if count[i] > max_num:
                max_num = count[i]

    return max_num


# # Inefficient O(n) solution
# def arrayManipulation(n, queries):
#     from collections import Counter
#     count = Counter()
#
#     for query in queries:
#         a, b, k = query
#         print a, b, k
#
#         for index in xrange(a, b + 1):
#             count[index] += k
#
#     max_num = 0
#     for item in count:
#         if count[item] > max_num:
#             max_num = count[item]
#
#     return max_num
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     nm = raw_input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     queries = []
#
#     for _ in xrange(m):
#         queries.append(map(int, raw_input().rstrip().split()))
#     result = arrayManipulation(n, queries)
#     fptr.write(str(result) + '\n')
#     fptr.close()
