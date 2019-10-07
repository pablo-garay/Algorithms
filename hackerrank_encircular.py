#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#

def doesCircleExist(commands):
    out = []

    for command in commands:
        pos = [0, 0]
        dir = 0
        prev_pos = set()
        found = False

        num_displac = command.count("G")
        num_displac = num_displac * 4 if num_displac > 0 else 4

        for i in xrange(num_displac):
            for c in command:
                if c == "G":
                    if dir == 0: pos[1] += 1    # up
                    elif dir == 1: pos[0] += 1  # right
                    elif dir == 2: pos[1] -= 1  # down
                    elif dir == 3: pos[0] -= 1  # left

                if c == "L":
                    dir = (dir + 4 - 1) % 4

                if c == "R":
                    dir = (dir + 1) % 4

            if str(pos) in prev_pos:
                found = True
                out.append("YES")
                break
            else:
                prev_pos.add(str(pos))

        if not found:
            out.append("NO")

    return out


print doesCircleExist(["G", "L", "GRGL", "LLLLG", "L", "LL", "LLL"])
print doesCircleExist(["GGGGR"])
print doesCircleExist(["GGGGRLGGGGR"])
print doesCircleExist(["GGGGRLGGGG"])
