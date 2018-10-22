#!/bin/python

import math
import os
import random
import re
import sys

# O(n) solution
def substrCount(n, s):
    count = len(s)
    prev_char = ""
    streak = 1

    for i in range(0, n):
        char = s[i]

        if char == prev_char:
            count += streak
            streak += 1
        else:
            streak = 1
            left, right = (i - 1, i + 1)

            # there was a change in char, check if current char is a middle one in special palindromic strings
            while left >= 0 and right <= (len(s) - 1) and prev_char == s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            prev_char = char

    return count

# O(n^2) solution
# def substrCount(n, s):
#     count = len(s)
#
#     for i in range(0, n):
#         char = s[i]
#         diff_chars_found, diff_char_pos = (0, -1)
#
#         for j in range(i + 1, n):
#             added_char = s[j]
#
#             if added_char != char:
#                 diff_chars_found += 1
#                 if diff_chars_found > 1:
#                     break
#                 else:
#                     diff_char_pos = j
#
#             if diff_chars_found == 0:
#                 count += 1
#                 # print "%s is special palindromic" %s[i:j + 1]
#             elif diff_chars_found == 1 and (j - i) % 2 == 0 and diff_char_pos == (i + j) / 2:
#                 count += 1
#                 # print "%s is special palindromic" %s[i:j + 1]
#
#     return count

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(raw_input())
#     s = raw_input()
#     result = substrCount(n, s)
#     fptr.write(str(result) + '\n')
#     fptr.close()

print substrCount(8, "mnonopoo")  # should return 12
print substrCount(5, "asasd")  # should return 7
print substrCount(7, "abcbaba")  # should return 10
print substrCount(4, "aaaa")  # should return 10
print substrCount(0, "")  # should return 0
print substrCount(1, "a")   # should return 1
