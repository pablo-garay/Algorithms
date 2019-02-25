#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    bin_reversed_s = [0] * len(s)
    result = ""
    letter_count = Counter(s)

    # Reversed s contains A in right order (not reversed)
    reversed_s = s[::-1]

    # divide count of each letter by 2
    for latest in letter_count:
        letter_count[latest] /= 2

    # greedy search for each letter which composes string A
    sorted_letters = sorted(letter_count.keys())
    earliest, latest = sorted_letters[0], sorted_letters[-1]
    print "string: " + s + " earliest, latest", earliest, latest

    start = 0
    while letter_count[earliest] > 0:
        ind = reversed_s.index(earliest, start)
        start = ind + 1
        bin_reversed_s[ind] = 1
        letter_count[earliest] -= 1
    del letter_count[earliest]

    end_ind = len(reversed_s)
    while letter_count[latest] > 0:
        ind = reversed_s.rfind(latest, 0, end_ind)
        end_ind = ind
        bin_reversed_s[ind] = 1
        letter_count[latest] -= 1
    del letter_count[latest]

    for i in xrange(len(reversed_s)):
        if bin_reversed_s[i] != 0:
            result += reversed_s[i]

    print "still to fill:", letter_count

    return result


    # print shuffled_a, length_a
    # print reversed_s

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = raw_input()
#     result = reverseShuffleMerge(s)
#     fptr.write(result + '\n')
#     fptr.close()

s = "abcdefgabcdefg"
print reverseShuffleMerge(s)
s = "abab"
print reverseShuffleMerge(s)
s = "eggegg"
print reverseShuffleMerge(s)
