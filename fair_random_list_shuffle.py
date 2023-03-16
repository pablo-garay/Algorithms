
# list of integers : fair & random shuffle
# [1, 2, 3, 4, 5, 6, 7]

import random

def uniform_shuffle(nums):  # Time: O(n) for array of n elems
    out = []

    lo, hi = (0, len(nums) - 1)

    while nums:
        ind = random.randint(0, hi)
        nums[ind], nums[hi] = (nums[hi], nums[ind])
        out.append(nums.pop())
        hi -= 1

    return out



print uniform_shuffle([1, 2, 3, 4, 5, 6, 7])


# Tests
print uniform_shuffle([])
print uniform_shuffle([1])
print uniform_shuffle([2, 1])


# len(input) == len(output)

# input
# uniform_shuffle(input)

# {
#     1 -> 4
# }
