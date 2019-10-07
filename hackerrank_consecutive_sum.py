#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'consecutive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER num as parameter.
#

def consecutive(num):  # complexity: O(n) where n is the value of the number (i.e. num)
    if num <= 1: return 0
    ways = 0
    coeff, constant, delta = (2, 1, 2)

    while (coeff + constant) <= num:
        ways += check_equation(coeff, constant, num)

        coeff += 1
        constant += delta
        delta += 1

    return ways

def check_equation(a, b, c):  # equation: a * x + b = c
    if (c - b) % a == 0:
        return 1
    else:
        return 0


print consecutive(15)
print consecutive(10)
print consecutive(16)
print consecutive(1)
print consecutive(2)
print consecutive(3)
print consecutive(4)
print consecutive(5)
print consecutive(6)
print consecutive(7)
print consecutive(8)
print consecutive(9)
