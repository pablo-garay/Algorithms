from collections import Counter

class Solution(object):  # O(n) solution. Optimal as in the worst case we have to see each letter at least once
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        diff = 0
        charset_a, duplicate_chars = set(), False
        diff_a, diff_b = set(), set()

        for i in xrange(len(A)):
            if A[i] != B[i]:
                diff += 1
                diff_a.add(A[i])
                diff_b.add(B[i])

            if A[i] in charset_a:
                duplicate_chars = True
            else:
                charset_a.add(A[i])

        if diff == 0 and duplicate_chars:
            return True
        elif diff == 2 and diff_a == diff_b:
            return True

        return False


print Solution().buddyStrings(A = "ab", B = "ba")
print Solution().buddyStrings(A = "ab", B = "ab")
print Solution().buddyStrings(A = "aa", B = "aa")
print Solution().buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")
print Solution().buddyStrings(A = "", B = "aa")
