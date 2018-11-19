#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    for char in s:
        if char == "{" or char == "(" or char == "[":
            stack.append(char)
        else:  # char is a closing bracket
            if not stack:  # empty stack
                return "NO"
            else:
                top_stack = stack.pop()
                if (top_stack == "(" and char != ")") or (top_stack == "{" and char != "}") or (top_stack == "[" and char != "]"):
                    return "NO"

    if not stack:  # stack is empty
        return "YES"
    return "NO"

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     t = int(raw_input())
#
#     for t_itr in xrange(t):
#         s = raw_input()
#         result = isBalanced(s)
#         fptr.write(result + '\n')
#     fptr.close()

print isBalanced("{[()]}")
print isBalanced("{[(])}")
print isBalanced("{{[[(())]]}}")
