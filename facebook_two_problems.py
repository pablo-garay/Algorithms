# Write a function that returns whether the given string, ignoring punctuation
# and capitalization, is a palindrome.
# "A man, a plan, a canal, Panama!"
#    -> True

def is_palindrome(s):  # O(n) where n is length of string s
    left, right = (0, len(s) - 1)

    while left <= right:
        if not s[left].isalpha():
            left += 1
            continue

        if not s[right].isalpha():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


print is_palindrome("")
print is_palindrome(", ")
print is_palindrome(" ")
print is_palindrome("Aa ")
print is_palindrome("")

----


# Before recess, the children of a classroom line up. Each child knows two
# pieces of information:

# 1. their own height
# 2. the number of children in front of them who are taller

# During recess, they scramble and loss this order and after recess, they
# must reconstruct the original order of the line. Design an algorithm to do so.

# Example:

# In: (child's height, # of taller children in front) =>
#   Set { (130, 1), (140, 0), (120, 3), (110, 3), (150, 0) }


# Out: [140, 130, 150, 110, 120]
# (Order of children: [front] 140 <- 130 <- 150 <- 110 <- 120 [back])


# In: [(110, 0), (120, 0), ...] (n-1)n / 2
# Out: [110, 120, 130, 140, 150]


def order(li):
    li.sort(lambda
                (height, num_taller): height)  # [(110, 3), (120, 3), (130, 1), (140, 0), (150, 0)]  # O(n log n) - can sort in different array to not modify original input (if that's not wanted)
    li2 = [None for _ in xrange(len(li))]

    for (h, num) in li:  # O(n^2)
        pos = num

        while li2[pos] is not None:
            pos += 1

        li2[pos] = (h, num)

    return li2

    # [null, null, null, null, null]

    # [null, null, null, (110, 3), null]
    # [(140, 0), (130, 1), (150, 0), (110, 3), (120, 3)]

    # [(140, 0), (120, 3), (130, 1), (110, 3), (150, 0)]
    # [(150, 0), (130, 1), (140, 0), (110, 3), (120, 3)]




