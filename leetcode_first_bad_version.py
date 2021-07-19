# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):  # O(log n) solution. Optimal as it's a search in a space of n ordered elements
    def firstBadVersion(self, n):
        start, end = 1, n

        while start < end:
            mid = (start + end) / 2

            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start
