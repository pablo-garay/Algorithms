#!/bin/python
import math
import os
import random
import re
import sys


def maxCircle(queries):
    circle = {}
    smallest_friend_pointer = {}
    max_circle_len = 0
    result = []

    for query in queries:
        num1, num2 = query[0], query[1]

        if num1 not in smallest_friend_pointer:
            smallest_friend_pointer[num1] = num1
            circle[num1] = [num1]
        if num2 not in smallest_friend_pointer:
            smallest_friend_pointer[num2] = num2
            circle[num2] = [num2]

        if smallest_friend_pointer[num1] < smallest_friend_pointer[num2]:
            largest, smallest = num2, num1
        else:
            largest, smallest = num1, num2

        if smallest_friend_pointer[largest] != smallest_friend_pointer[smallest]:  # check if they're not in the same circle already
            for num in circle[largest]:
                circle[smallest].append(num)
                circle[num] = circle[smallest]
                smallest_friend_pointer[num] = smallest_friend_pointer[smallest]
        # print "circle:", circle[smallest]  # for debugging purposes!

        if len(circle[smallest]) > max_circle_len:  # check if length of updated circle is greater than current maximum
            max_circle_len = len(circle[smallest])

        result.append(max_circle_len)

    return result


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(raw_input())
#     queries = []
#
#     for _ in xrange(q):
#         queries.append(map(int, raw_input().rstrip().split()))
#
#     ans = maxCircle(queries)
#     fptr.write('\n'.join(map(str, ans)))
#     fptr.write('\n')
#     fptr.close()


print maxCircle([
    [1, 2],
    [3, 4],
    [2, 3],
])  # output: [2, 2, 4]

print maxCircle([
    [1, 2],
    [1, 3],
])  # output: [2, 3]

print maxCircle([
    [1000000000, 23],
    [11, 3778],
    [7, 47],
    [11, 1000000000]
])  # output: [2, 2, 2, 4]

print maxCircle([
    [1, 2],
    [3, 4],
    [1, 3],
    [5, 7],
    [5, 6],
    [7, 4],
])  # output: [2, 2, 4, 4, 4, 7]
