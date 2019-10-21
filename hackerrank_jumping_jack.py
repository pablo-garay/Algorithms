# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#
import math

def maxStep(n, k):  # O(1) solution. Use quadratic formula (it's a math problem).
    hypoth_max = n * (n + 1) / 2
    x = (math.sqrt(1 + 8 * k) - 1) / 2  # iff x is integer: x is step in which conflict will occur

    if x.is_integer() and x <= n:
        return hypoth_max - 1
    else:
        return hypoth_max

print maxStep(2, 2)  # res = 3
print maxStep(2, 1)  # res = 2
print maxStep(3, 3)  # res = 5
print maxStep(4, 3)  # res = 9
print maxStep(5, 3)  # res = 14
