#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = Counter()
    reverse_freq = Counter()
    array_out = []

    for tup in queries:
        elem = tup[1]

        if tup[0] == 1:
            if freq[elem] > 0:
                reverse_freq[freq[elem]] -= 1
                freq[elem] += 1
                reverse_freq[freq[elem]] += 1
            else:
                freq[elem] = 1
                reverse_freq[1] += 1

        elif tup[0] == 2:
            if freq[elem] > 0:
                reverse_freq[freq[elem]] -= 1
                freq[elem] -= 1
                if freq[elem] > 0:
                    reverse_freq[freq[elem]] += 1

        elif tup[0] == 3:
            if reverse_freq[elem] > 0:
                array_out.append(1)
            else:
                array_out.append(0)

    return array_out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
